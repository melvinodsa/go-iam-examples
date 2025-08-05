package main

import (
	"fmt"
	"io"
	"net/http"
	"os"
)

func main() {
	// Load JWT token from environment variable
	jwtToken := os.Getenv("JWT_TOKEN")
	if jwtToken == "" {
		fmt.Println("❌ JWT_TOKEN environment variable is not set")
		fmt.Println("\nTo set up the JWT token:")
		fmt.Println("1. Login to Go IAM web interface")
		fmt.Println("2. Open browser Developer Tools")
		fmt.Println("3. Go to Application/Storage tab")
		fmt.Println("4. Find 'access_token' in Local Storage")
		fmt.Println("5. Copy the token value")
		fmt.Println("6. Set the environment variable: export JWT_TOKEN=your_actual_token")
		fmt.Println("7. Or create a .env file with: JWT_TOKEN=your_actual_token")
		return
	}

	// Load server URL from environment variable with default
	serverURL := os.Getenv("SERVER_URL")
	if serverURL == "" {
		serverURL = "http://localhost:3001"
	}

	fmt.Printf("🚀 Testing Go IAM server at %s...\n", serverURL)

	// Create HTTP request
	req, err := http.NewRequest("GET", serverURL, nil)
	if err != nil {
		panic(fmt.Sprintf("Failed to create request: %v", err))
	}

	// Set Authorization header with JWT token
	req.Header.Set("Authorization", "Bearer "+jwtToken)
	req.Header.Set("Content-Type", "application/json")

	client := http.DefaultClient
	resp, err := client.Do(req)
	if err != nil {
		panic(fmt.Sprintf("Failed to make request: %v", err))
	}
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusOK {
		fmt.Printf("❌ Request failed with status: %d %s\n", resp.StatusCode, resp.Status)
		if resp.StatusCode == 401 {
			fmt.Println("\nTroubleshooting tips:")
			fmt.Println("• Check that your JWT token is valid and not expired")
			fmt.Println("• Verify the Go IAM server is running on http://localhost:3000")
			fmt.Println("• Ensure the example server is running on http://localhost:3001")
		}
		return
	}

	fmt.Println("✅ Request successful!")
	bytes, err := io.ReadAll(resp.Body)
	if err != nil {
		panic(fmt.Sprintf("Failed to read response: %v", err))
	}
	fmt.Printf("Response: %s\n", string(bytes))
}
