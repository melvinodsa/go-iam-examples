const axios = require("axios");
require("dotenv").config();

async function testServer() {
  try {
    // Load JWT token from environment variable
    const jwtToken = process.env.JWT_TOKEN || "<your_jwt_token>";
    const serverUrl = process.env.SERVER_URL || "http://localhost:3002";

    console.log("🚀 Testing Go IAM Node.js server...\n");

    if (jwtToken === "<your_jwt_token>" || !jwtToken) {
      console.error(
        "❌ JWT_TOKEN environment variable is not set or is using the default placeholder"
      );
      console.log("\nTo set up the JWT token:");
      console.log("1. Login to Go IAM web interface");
      console.log("2. Open browser Developer Tools");
      console.log("3. Go to Application/Storage tab");
      console.log('4. Find "access_token" in Local Storage');
      console.log("5. Copy the token value");
      console.log(
        "6. Set the environment variable: export JWT_TOKEN=your_actual_token"
      );
      console.log(
        "7. Or create/update a .env file with: JWT_TOKEN=your_actual_token"
      );
      console.log("8. Re-run the client: npm run client");
      return;
    }

    console.log(`🔗 Server URL: ${serverUrl}`);
    console.log(`🔑 Using JWT token: ${jwtToken.substring(0, 20)}...`);

    // Make request to protected endpoint
    const response = await axios.get(`${serverUrl}/`, {
      headers: {
        Authorization: `Bearer ${jwtToken}`,
        "Content-Type": "application/json",
      },
    });

    console.log("✅ Main endpoint successful!");
    console.log("Response:", response.data);

    // Test health endpoint as well
    const healthResponse = await axios.get(`${serverUrl}/health`, {
      headers: {
        Authorization: `Bearer ${jwtToken}`,
        "Content-Type": "application/json",
      },
    });

    console.log("\n✅ Health endpoint successful!");
    console.log("Response:", healthResponse.data);

    console.log("\n🎉 All tests completed!");
  } catch (error) {
    console.error("❌ Request failed:");
    if (error.response) {
      console.error("Status:", error.response.status);
      console.error("Data:", error.response.data);
    } else {
      console.error("Error:", error.message);
    }

    console.log("\nTroubleshooting tips:");
    console.log("• Make sure the server is running: npm start");
    console.log("• Ensure your JWT token is valid and not expired");
    console.log("• Verify Go IAM server is running on http://localhost:3000");
    console.log("• Check that environment variables are set: echo $JWT_TOKEN");
    console.log(
      `• Make sure the server is accessible on ${
        process.env.SERVER_URL || "http://localhost:3002"
      }`
    );
  }
}

testServer();
