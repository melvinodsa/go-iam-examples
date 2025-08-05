# Go IAM Example - Golang

This example demonstrates how to integrate Go IAM authentication into a Golang web application using the Fiber framework and the go-iam-sdk.

## Overview

The example consists of:

- **`main.go`**: A Fiber web server with JWT authentication middleware that validates tokens using Go IAM
- **`client/httpclient.go`**: A simple HTTP client that demonstrates how to make authenticated requests to the server

## Prerequisites

- Go 1.23.3 or later
- Docker and Docker Compose (for running Go IAM server)
- Access to the go-iam-sdk

## Setup Instructions

### 1. Setup Go IAM Server

First, you need to set up and run the Go IAM server using Docker:

1. Follow the setup instructions at: https://github.com/melvinodsa/go-iam-docker
2. After setting up, configure Go IAM by following the [configuration video/documentation](https://youtu.be/k6DakLyca_s)
3. Start the Go IAM server (it should be running on `http://localhost:3000`)

### 2. Install Dependencies

Navigate to the golang directory and install the required dependencies:

```bash
cd golang
go mod tidy
```

### 3. Configure Client Credentials

In `main.go`, update the client credentials if needed:

```go
const (
    baseUrl      = "http://localhost:3000"  // Go IAM server URL
    clientId     = "abcdef1234567890abcdef1234567890"     // Your client ID
    clientSecret = "abcdef1234567890abcdef1234567890"     // Your client secret
)
```

### 4. Obtain JWT Token

1. Open your browser and navigate to the Go IAM login page
2. Login with your credentials
3. After successful login, open your browser's Developer Tools
4. Go to the **Application** tab (Chrome) or **Storage** tab (Firefox)
5. Navigate to **Local Storage**
6. Find and copy the value of the `access_token` key

### 5. Configure JWT Token

You have two options to set the JWT token:

#### Option A: Environment Variables (Recommended)

1. Create a `.env` file in the golang directory based on the example:

   ```bash
   cp .env.example .env
   ```

2. Edit the `.env` file and replace the JWT token:

   ```env
   JWT_TOKEN=your_actual_jwt_token_here
   SERVER_URL=http://localhost:3001
   ```

3. Source the environment file before running the client:
   ```bash
   export $(cat .env | xargs)
   ```

#### Option B: Direct Environment Variable

Set the JWT token directly as an environment variable:

```bash
export JWT_TOKEN=your_actual_jwt_token_here
export SERVER_URL=http://localhost:3001  # optional, defaults to localhost:3001
```

## Running the Example

### 1. Start the Server

In the golang directory, run the main server:

```bash
go run main.go
```

The server will start on `http://localhost:3001` and display logs indicating it's ready.

### 2. Test with HTTP Client

In a new terminal, ensure your environment variables are set and navigate to the client directory:

```bash
# If using .env file
export $(cat .env | xargs)

# Navigate to client directory
cd client

# Run the HTTP client
go run httpclient.go
```

Or run directly with environment variables:

```bash
cd client
JWT_TOKEN=your_actual_jwt_token_here go run httpclient.go
```

### Expected Output

If everything is configured correctly, you should see:

```
🚀 Testing Go IAM server at http://localhost:3001...
✅ Request successful!
Response: Hello, <your-name>!
```

Where `<your-name>` will be replaced with your actual name from the Go IAM user profile.

## Code Explanation

### Server (`main.go`)

- **Authentication Middleware**: Validates JWT tokens on every request
- **Go IAM Integration**: Uses the `go-iam-sdk` to verify tokens and retrieve user information
- **Protected Endpoint**: Returns a personalized greeting using the authenticated user's name

### Client (`client/httpclient.go`)

- **HTTP Request**: Makes a GET request to the protected endpoint
- **Authorization Header**: Includes the JWT token in the `Authorization` header
- **Response Handling**: Displays the server response

## Key Features Demonstrated

1. **JWT Token Validation**: Server validates incoming JWT tokens with Go IAM
2. **User Information Retrieval**: Server fetches user details using the validated token
3. **Protected Routes**: All routes require valid authentication
4. **Environment Variable Configuration**: Secure token management using environment variables
5. **Error Handling**: Proper error responses for invalid or missing tokens

## Environment Variables

The HTTP client supports the following environment variables:

| Variable     | Description                 | Default                 | Required |
| ------------ | --------------------------- | ----------------------- | -------- |
| `JWT_TOKEN`  | JWT token from Go IAM login | -                       | Yes      |
| `SERVER_URL` | Target server URL           | `http://localhost:3001` | No       |

### Setting Environment Variables

#### Using .env file (Recommended)

```bash
# Copy the example file
cp .env.example .env

# Edit the .env file with your values
# Then source it
export $(cat .env | xargs)
```

#### Direct export

```bash
export JWT_TOKEN=your_actual_jwt_token_here
export SERVER_URL=http://localhost:3001
```

## Troubleshooting

### Common Issues

1. **"JWT_TOKEN environment variable is not set"**:

   - Ensure you've set the JWT_TOKEN environment variable
   - Check that you've sourced the .env file: `export $(cat .env | xargs)`
   - Verify the JWT token is copied correctly from the browser

2. **"Unauthorized" Response**:

   - Ensure your JWT token is valid and not expired
   - Check that the token is properly formatted in the Authorization header
   - Verify Go IAM server is running on the correct port

3. **Connection Refused**:

   - Ensure Go IAM server is running on `http://localhost:3000`
   - Ensure the example server is running on `http://localhost:3001`
   - Check that SERVER_URL environment variable is set correctly

4. **Module Issues**:
   - Run `go mod tidy` to ensure all dependencies are properly installed
   - Check that you have the correct Go version (1.23.3+)

### Debugging Tips

- Check server logs for detailed error messages
- Verify client credentials match your Go IAM configuration
- Ensure ports 3000 (Go IAM) and 3001 (example server) are not in use by other applications
- Verify environment variables are set: `echo $JWT_TOKEN`
- Test JWT token validity by checking its expiration date
- Use verbose output to debug HTTP requests

## Next Steps

- Explore additional Go IAM SDK features
- Implement role-based access control
- Add more protected endpoints
- Integrate with your existing Go applications

## Dependencies

- **Fiber v2**: Web framework for Go
- **go-iam-sdk**: Official Go IAM SDK for Golang
- **Standard Library**: HTTP client functionality

For more information about Go IAM, visit the official documentation and repository.
