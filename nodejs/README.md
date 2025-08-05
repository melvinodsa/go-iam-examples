# Go IAM Example - Node.js

This example demonstrates how to integrate Go IAM authentication into a Node.js web application using Express.js and the official `@goiam/typescript` SDK package.

## Overview

The example consists of:

- **`server.js`**: An Express.js web server with JWT authentication middleware that validates tokens using the Go IAM SDK
- **`client/httpclient.js`**: A simple HTTP client that demonstrates how to make authenticated requests to the server

## Prerequisites

- Node.js 18.0.0 or later
- npm (Node Package Manager)
- Docker and Docker Compose (for running Go IAM server)
- Access to the Go IAM server

## Setup Instructions

### 1. Setup Go IAM Server

First, you need to set up and run the Go IAM server using Docker:

1. Follow the setup instructions at: https://github.com/melvinodsa/go-iam-docker
2. After setting up, configure Go IAM by following the [configuration video/documentation](https://youtu.be/k6DakLyca_s)
3. Start the Go IAM server (it should be running on `http://localhost:3000`)

### 2. Install Dependencies

Navigate to the nodejs directory and install the required dependencies:

```bash
cd nodejs
npm install
```

### 3. Configure Client Credentials

In `server.js`, update the client credentials if needed:

```javascript
const config = {
  baseUrl: "http://localhost:3000", // Go IAM server URL
  clientId: "abcdef1234567890abcdef1234567890", // Your client ID
  clientSecret: "abcdef1234567890abcdef1234567890", // Your client secret
  port: 3002, // Server port (different from Go IAM)
};
```

### 4. Obtain JWT Token

1. Open your browser and navigate to the Go IAM login page
2. Login with your credentials
3. After successful login, open your browser's Developer Tools
4. Go to the **Application** tab (Chrome) or **Storage** tab (Firefox)
5. Navigate to **Local Storage**
6. Find and copy the value of the `access_token` key

### 5. Configure HTTP Client

Edit `client/httpclient.js` and replace `<your_jwt_token>` with the actual JWT token you copied:

```javascript
const jwtToken = "your_actual_jwt_token_here";
```

## Running the Example

### 1. Start the Server

In the nodejs directory, run the server:

```bash
npm start
```

Or for development with auto-reload:

```bash
npm run dev
```

The server will start on `http://localhost:3002` and display logs indicating it's ready.

### 2. Test with HTTP Client

In a new terminal, run the HTTP client:

```bash
npm run client
```

Or directly:

```bash
node client/httpclient.js
```

### Expected Output

If everything is configured correctly, you should see:

```
Testing Go IAM Node.js server...
Request successful!
Response: {
  message: 'Hello, <your-name>!',
  user: {
    id: 'user-id',
    name: '<your-name>',
    email: 'your-email@example.com',
    // ... other user properties
  }
}

Health check response: {
  status: 'healthy',
  user: '<your-name>',
  timestamp: '2025-01-XX...'
}
```

Where `<your-name>` will be replaced with your actual name from the Go IAM user profile.

## Code Explanation

### Server (`server.js`)

- **Go IAM SDK Integration**: Uses the official `@goiam/typescript` package for seamless authentication
- **Authentication Middleware**: Validates JWT tokens using the GoIAMService.me() method
- **Express.js Setup**: RESTful API server with JSON middleware
- **Protected Endpoints**: All routes require valid authentication
- **Error Handling**: Comprehensive error handling for authentication failures

### Client (`client/httpclient.js`)

- **HTTP Requests**: Uses axios to make GET requests to protected endpoints
- **Authorization Header**: Includes the JWT token in the `Authorization` header
- **Response Handling**: Displays server responses and handles errors gracefully
- **Multiple Endpoints**: Tests both main route and health check endpoint

## API Endpoints

### `GET /`

- **Description**: Main protected endpoint that returns a personalized greeting
- **Authentication**: Required (JWT token)
- **Response**: JSON with message and user information

### `GET /health`

- **Description**: Health check endpoint with user context
- **Authentication**: Required (JWT token)
- **Response**: JSON with status, user name, and timestamp

## Key Features Demonstrated

1. **Official SDK Integration**: Uses the `@goiam/typescript` package for type-safe Go IAM integration
2. **JWT Token Validation**: Server validates incoming JWT tokens using the GoIAMService
3. **User Information Retrieval**: Server fetches user details using the SDK's me() method
4. **Protected Routes**: All routes require valid authentication
5. **RESTful API**: Clean Express.js API structure
6. **Error Handling**: Proper error responses for invalid or missing tokens
7. **Async/Await**: Modern JavaScript patterns for handling asynchronous operations

## Configuration Options

You can customize the server by modifying the `config` object in `server.js`:

```javascript
const config = {
  baseUrl: "http://localhost:3000", // Go IAM server URL
  clientId: "your-client-id", // Your Go IAM client ID
  clientSecret: "your-client-secret", // Your Go IAM client secret
  port: 3002, // Server port
};
```

## Available Scripts

- **`npm start`**: Start the production server
- **`npm run dev`**: Start the development server with auto-reload (requires nodemon)
- **`npm run client`**: Run the HTTP client test

## Troubleshooting

### Common Issues

1. **"Unauthorized" Response**:

   - Ensure your JWT token is valid and not expired
   - Check that the token is properly formatted in the Authorization header
   - Verify Go IAM server is running on the correct port

2. **Connection Refused**:

   - Ensure Go IAM server is running on `http://localhost:3000`
   - Ensure the example server is running on `http://localhost:3002`
   - Check that no other services are using these ports

3. **Module Not Found**:

   - Run `npm install` to ensure all dependencies are properly installed
   - Check that you have the correct Node.js version (18.0.0+)

4. **Port Already in Use**:
   - Change the port in the config object in `server.js`
   - Kill any processes using port 3002: `lsof -ti:3002 | xargs kill -9`

### Debugging Tips

- Check server logs for detailed error messages
- Verify client credentials match your Go IAM configuration
- Use `console.log()` to debug request/response data
- Test the Go IAM server directly with tools like Postman or curl

## Environment Variables (Optional)

You can use environment variables instead of hardcoding values:

Create a `.env` file:

```env
GO_IAM_BASE_URL=http://localhost:3000
GO_IAM_CLIENT_ID=your-client-id
GO_IAM_CLIENT_SECRET=your-client-secret
SERVER_PORT=3002
```

Then update `server.js` to use them:

```javascript
require("dotenv").config();

const config = {
  baseUrl: process.env.GO_IAM_BASE_URL || "http://localhost:3000",
  clientId: process.env.GO_IAM_CLIENT_ID || "abcdef1234567890abcdef1234567890",
  clientSecret:
    process.env.GO_IAM_CLIENT_SECRET || "abcdef1234567890abcdef1234567890",
  port: process.env.SERVER_PORT || 3002,
};
```

## Next Steps

- Explore additional Go IAM API endpoints
- Implement role-based access control
- Add more protected endpoints with different functionality
- Integrate with your existing Node.js applications
- Add request logging and monitoring
- Implement token refresh logic

## Dependencies

- **Express.js**: Fast, unopinionated web framework for Node.js
- **@goiam/typescript**: Official Go IAM SDK for Node.js/TypeScript applications
- **dotenv**: For environment variable management
- **nodemon**: Development tool for auto-reloading (dev dependency)

For more information about Go IAM, visit the official documentation and repository.
