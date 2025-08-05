# Go IAM Example - TypeScript

This example demonstrates how to integrate Go IAM authentication into a TypeScript/Node.js web application using Express.js and the official `@goiam/typescript` SDK package with full type safety.

## Overview

The example consists of:

- **`src/server.ts`**: A TypeScript Express.js web server with JWT authentication middleware that validates tokens using the Go IAM SDK
- **`src/client/httpclient.ts`**: A TypeScript HTTP client that demonstrates how to make authenticated requests to the server
- **Full TypeScript support**: Type-safe development with strict TypeScript configuration

## Prerequisites

- Node.js 18.0.0 or later
- npm (Node Package Manager)
- TypeScript knowledge (basic understanding recommended)
- Docker and Docker Compose (for running Go IAM server)
- Access to the Go IAM server

## Setup Instructions

### 1. Setup Go IAM Server

First, you need to set up and run the Go IAM server using Docker:

1. Follow the setup instructions at: https://github.com/melvinodsa/go-iam-docker
2. After setting up, configure Go IAM by following the [configuration video/documentation](https://youtu.be/k6DakLyca_s)
3. Start the Go IAM server (it should be running on `http://localhost:3000`)

### 2. Install Dependencies

Navigate to the typescript directory and install the required dependencies:

```bash
cd typescript
npm install
```

### 3. Configure Environment Variables (Optional)

Copy the environment template and customize it:

```bash
cp .env.example .env
```

Edit `.env` file with your specific configuration:

```env
# Go IAM Configuration
GO_IAM_BASE_URL=http://localhost:3000
GO_IAM_CLIENT_ID=your-actual-client-id
GO_IAM_CLIENT_SECRET=your-actual-client-secret

# Server Configuration
SERVER_PORT=3003
NODE_ENV=development
```

### 4. Configure Client Credentials (Alternative)

If not using environment variables, you can update the configuration directly in `src/server.ts`:

```typescript
const config: Config = {
  baseUrl: "http://localhost:3000", // Go IAM server URL
  clientId: "your-actual-client-id", // Your client ID
  clientSecret: "your-actual-client-secret", // Your client secret
  port: 3003, // Server port (different from Go IAM and Node.js examples)
};
```

### 5. Obtain JWT Token

1. Open your browser and navigate to the Go IAM login page
2. Login with your credentials
3. After successful login, open your browser's Developer Tools
4. Go to the **Application** tab (Chrome) or **Storage** tab (Firefox)
5. Navigate to **Local Storage**
6. Find and copy the value of the `access_token` key

### 6. Configure JWT Token for HTTP Client

You have two options to set the JWT token for the HTTP client:

#### Option A: Environment Variables (Recommended)

Add the JWT token to your `.env` file:

```env
# Add to your .env file
JWT_TOKEN=your_actual_jwt_token_here
SERVER_URL=http://localhost:3003
```

#### Option B: Direct Environment Variable

Set the JWT token directly as an environment variable:

```bash
export JWT_TOKEN=your_actual_jwt_token_here
export SERVER_URL=http://localhost:3003  # optional, defaults to localhost:3003
```

## Running the Example

### 1. Build the TypeScript Code (Production)

For production deployment, build the TypeScript code:

```bash
npm run build
npm start
```

### 2. Development Mode (Recommended)

For development with auto-reload and TypeScript compilation:

```bash
npm run dev
```

The server will start on `http://localhost:3003` and display logs indicating it's ready.

### 3. Test with TypeScript Client

In a new terminal, ensure your environment variables are set and run the TypeScript HTTP client:

```bash
# If using .env file (already loaded automatically by dotenv)
npm run client
```

Or run directly with environment variables:

```bash
JWT_TOKEN=your_actual_jwt_token_here npm run client
```

Or directly with ts-node:

```bash
npx ts-node src/client/httpclient.ts
```

### Expected Output

If everything is configured correctly, you should see:

```
🚀 Starting Go IAM TypeScript client tests...

🔗 Server URL: http://localhost:3003
🔑 Using JWT token: eyJhbGciOiJIUzI1NiIs...

Testing main endpoint...
✅ Main endpoint successful!
🚀 Starting Go IAM TypeScript client tests...

Testing main endpoint...
✅ Main endpoint successful!
Response: {
  message: 'Hello, <your-name>!',
  user: {
    id: 'user-id',
    name: '<your-name>',
    email: 'your-email@example.com',
    // ... other user properties
  }
}

Testing health endpoint...
✅ Health endpoint successful!
Response: {
  status: 'healthy',
  user: '<your-name>',
  timestamp: '2025-01-XX...'
}

Testing profile endpoint...
✅ Profile endpoint successful!
Response: {
  profile: {
    id: 'user-id',
    name: '<your-name>',
    // ... full user profile
  },
  timestamp: '2025-01-XX...'
}

🎉 All tests completed!
```

Where `<your-name>` will be replaced with your actual name from the Go IAM user profile.

## Code Explanation

### Server (`src/server.ts`)

- **TypeScript Interfaces**: Strongly typed configuration and request/response objects
- **Go IAM SDK Integration**: Uses the official `@goiam/typescript` package for seamless authentication
- **Authentication Middleware**: Type-safe JWT token validation using GoIamSdk.me() method
- **Express.js with Types**: Fully typed Express.js setup with custom Request interface extension
- **Environment Configuration**: Support for both environment variables and direct configuration
- **Error Handling**: Comprehensive error handling with proper TypeScript error types

### Client (`src/client/httpclient.ts`)

- **Type-Safe HTTP Requests**: Strongly typed axios requests with proper response interfaces
- **Multiple Endpoint Testing**: Tests main, health, and profile endpoints
- **Comprehensive Error Handling**: Proper error typing and user-friendly error messages
- **Configuration Constants**: Type-safe configuration with `as const` assertions
- **Detailed Logging**: Structured logging with success/failure indicators

## API Endpoints

### `GET /`

- **Description**: Main protected endpoint that returns a personalized greeting
- **Authentication**: Required (JWT token)
- **Response Type**: `UserResponse`
- **Response**: JSON with message and user information

### `GET /health`

- **Description**: Health check endpoint with user context
- **Authentication**: Required (JWT token)
- **Response Type**: `HealthResponse`
- **Response**: JSON with status, user name, and timestamp

### `GET /profile`

- **Description**: User profile endpoint returning full user information
- **Authentication**: Required (JWT token)
- **Response Type**: `ProfileResponse`
- **Response**: JSON with complete user profile and timestamp

## TypeScript Features Demonstrated

1. **Strict Type Checking**: Enabled strict mode with additional safety options
2. **Interface Definitions**: Properly typed configuration and API responses
3. **Express.js Type Extensions**: Custom Request interface extensions for user data
4. **Generic Types**: Typed HTTP client with AxiosResponse generics
5. **Environment Variable Typing**: Type-safe environment variable handling
6. **Error Type Guards**: Proper error handling with type checking
7. **Const Assertions**: Using `as const` for immutable configuration
8. **Async/Await with Types**: Properly typed asynchronous operations

## Configuration Options

### Environment Variables (Recommended)

Create a `.env` file based on `.env.example`:

```env
# Server Configuration
GO_IAM_BASE_URL=http://localhost:3000
GO_IAM_CLIENT_ID=your-client-id
GO_IAM_CLIENT_SECRET=your-client-secret
SERVER_PORT=3003
NODE_ENV=development

# Client Configuration
JWT_TOKEN=your_actual_jwt_token_here
SERVER_URL=http://localhost:3003
```

#### Supported Environment Variables

| Variable               | Description                   | Default                 | Used By |
| ---------------------- | ----------------------------- | ----------------------- | ------- |
| `GO_IAM_BASE_URL`      | Go IAM server URL             | `http://localhost:3000` | Server  |
| `GO_IAM_CLIENT_ID`     | Go IAM client ID              | -                       | Server  |
| `GO_IAM_CLIENT_SECRET` | Go IAM client secret          | -                       | Server  |
| `SERVER_PORT`          | Server port                   | `3003`                  | Server  |
| `NODE_ENV`             | Node environment              | `development`           | Server  |
| `JWT_TOKEN`            | JWT token for client requests | -                       | Client  |
| `SERVER_URL`           | Target server URL for client  | `http://localhost:3003` | Client  |

### Direct Configuration

Alternatively, modify the config object in `src/server.ts`:

```typescript
const config: Config = {
  baseUrl: process.env.GO_IAM_BASE_URL || "http://localhost:3000",
  clientId: process.env.GO_IAM_CLIENT_ID || "your-client-id",
  clientSecret: process.env.GO_IAM_CLIENT_SECRET || "your-client-secret",
  port: parseInt(process.env.SERVER_PORT || "3003", 10),
};
```

## Available Scripts

- **`npm run build`**: Compile TypeScript to JavaScript in `dist/` directory
- **`npm start`**: Start the production server (requires build first)
- **`npm run dev`**: Start development server with auto-reload and TypeScript compilation
- **`npm run client`**: Run the TypeScript HTTP client test
- **`npm run clean`**: Clean the `dist/` directory

## TypeScript Configuration

The project uses a strict TypeScript configuration (`tsconfig.json`) with:

- **Target**: ES2020 for modern JavaScript features
- **Strict Mode**: All strict type-checking options enabled
- **Additional Safety**: `noUncheckedIndexedAccess`, `exactOptionalPropertyTypes`
- **Source Maps**: Enabled for debugging
- **Declaration Files**: Generated for library usage

## Troubleshooting

### Common Issues

1. **"JWT_TOKEN environment variable is not set"**:

   - Ensure you've set the JWT_TOKEN environment variable
   - Check that the .env file exists and contains JWT_TOKEN
   - Verify the JWT token is copied correctly from the browser
   - Make sure dotenv is loading the .env file properly

2. **TypeScript Compilation Errors**:

   - Run `npm run build` to check for type errors
   - Ensure all dependencies are installed: `npm install`
   - Check TypeScript version compatibility

3. **"Unauthorized" Response**:

   - Ensure your JWT token is valid and not expired
   - Check that the token is properly formatted in the Authorization header
   - Verify Go IAM server is running on the correct port

4. **Connection Refused**:

   - Ensure Go IAM server is running on `http://localhost:3000`
   - Ensure the example server is running on `http://localhost:3003`
   - Check that SERVER_URL environment variable is set correctly
   - Check that no other services are using these ports

5. **Module Not Found**:

   - Run `npm install` to ensure all dependencies are properly installed
   - Check that you have the correct Node.js version (18.0.0+)
   - Verify TypeScript is installed: `npx tsc --version`

6. **Port Already in Use**:
   - Change the port in `.env` file or config object
   - Kill any processes using port 3003: `lsof -ti:3003 | xargs kill -9`

### Debugging Tips

- Use `npm run build` to check for TypeScript compilation errors
- Check server logs for detailed error messages with proper typing
- Verify client credentials match your Go IAM configuration
- Use TypeScript's IntelliSense for better development experience
- Test the Go IAM server directly with tools like Postman or curl
- Verify environment variables are set: `echo $JWT_TOKEN`
- Check that .env file is in the correct directory and properly formatted
- Use verbose output to debug HTTP requests

## Development Workflow

1. **Setup**: Install dependencies and configure environment
2. **Development**: Use `npm run dev` for auto-reload during development
3. **Testing**: Use `npm run client` to test API endpoints
4. **Building**: Use `npm run build` for production builds
5. **Deployment**: Use `npm start` to run the built application

## Type Safety Benefits

- **Compile-time Error Detection**: Catch errors before runtime
- **IntelliSense Support**: Better IDE support with autocomplete
- **Refactoring Safety**: Confident code refactoring with type checking
- **API Contract Enforcement**: Ensure API responses match expected types
- **Documentation**: Types serve as living documentation

## Next Steps

- Explore additional Go IAM SDK features with full type support
- Implement role-based access control with typed permissions
- Add more protected endpoints with proper TypeScript interfaces
- Integrate with your existing TypeScript applications
- Add comprehensive testing with typed test frameworks (Jest, Vitest)
- Implement advanced TypeScript patterns (decorators, generics)

## Dependencies

- **Express.js**: Fast, unopinionated web framework for Node.js
- **@goiam/typescript**: Official Go IAM SDK for TypeScript/Node.js applications
- **axios**: Promise-based HTTP client with TypeScript support
- **dotenv**: Environment variable management
- **TypeScript**: Static type checking for JavaScript
- **ts-node**: TypeScript execution for Node.js
- **ts-node-dev**: Development tool for TypeScript auto-reloading

### Dev Dependencies

- **@types/express**: TypeScript definitions for Express.js
- **@types/node**: TypeScript definitions for Node.js
- **rimraf**: Cross-platform directory cleaning utility

For more information about Go IAM, visit the official documentation and repository.
