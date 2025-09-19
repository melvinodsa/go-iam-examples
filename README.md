# Go IAM Examples

> ✅ Admin UI: [go-iam-ui](https://github.com/melvinodsa/go-iam-ui)  
> 🐳 Docker Setup: [go-iam-docker](https://github.com/melvinodsa/go-iam-docker)  
> 🔐 Backend: [go-iam](https://github.com/melvinodsa/go-iam)  
> 📦 SDK: [go-iam-sdk](https://github.com/melvinodsa/go-iam-sdk)  
> 🚀 Examples: [go-iam-examples](https://github.com/melvinodsa/go-iam-examples)
> 💬 Reddit Community: [r/GoIAM](https://www.reddit.com/r/GoIAM/)

This repository contains examples demonstrating how to integrate Go IAM authentication into applications using different programming languages and frameworks.

## Overview

Go IAM is a comprehensive Identity and Access Management solution. This repository provides practical examples showing how to:

- Authenticate users with JWT tokens
- Validate tokens using the Go IAM SDK
- Retrieve user information
- Implement protected routes and middleware
- Handle authentication errors

## Available Examples

### 🟢 Golang

**Status**: ✅ Available  
**Framework**: Fiber v2  
**Location**: [`/golang`](./golang/)

A complete example showing:

- JWT authentication middleware
- User information retrieval
- Protected HTTP endpoints
- HTTP client for testing

**Quick Start**: Navigate to the `golang` directory and follow the [README](./golang/README.md) for detailed setup instructions.

### 🟢 Node.js

**Status**: ✅ Available  
**Framework**: Express.js  
**SDK**: @goiam/typescript  
**Location**: [`/nodejs`](./nodejs/)

A complete example showing:

- Official Go IAM SDK integration
- Express.js authentication middleware
- Type-safe JWT token validation
- RESTful API endpoints
- Modern async/await patterns

**Quick Start**: Navigate to the `nodejs` directory and follow the [README](./nodejs/README.md) for detailed setup instructions.

### 🟢 TypeScript

**Status**: ✅ Available  
**Framework**: Express.js  
**SDK**: @goiam/typescript  
**Location**: [`/typescript`](./typescript/)

A complete example showing:

- Full TypeScript support with strict type checking
- Official Go IAM SDK integration with type safety
- Strongly typed Express.js server and HTTP client
- Environment variable configuration
- Advanced TypeScript patterns and interfaces

**Quick Start**: Navigate to the `typescript` directory and follow the [README](./typescript/README.md) for detailed setup instructions.

### 🟢 Python

**Status**: ✅ Available  
**Framework**: FastAPI  
**SDK**: goiam-python (v0.0.1)  
**Location**: [`/python`](./python/)

A complete example showing:

- FastAPI framework with dependency injection
- Official Go IAM SDK integration for Python
- Virtual environment setup with automated scripts
- Type hints and comprehensive error handling
- Interactive API documentation with Swagger UI
- Comprehensive testing and setup validation

**Quick Start**: Navigate to the `python` directory and run `./setup.sh` for automated setup, or follow the [README](./python/README.md) for manual setup instructions.

---

## Coming Soon

We're working on examples for additional languages and frameworks:

### 🟡 Java

**Status**: 🚧 In Development  
**Framework**: Spring Boot  
**Expected**: Q2 2025

---

## Prerequisites

Before using any example, ensure you have:

1. **Go IAM Server**: Set up and running

   - Follow the setup guide: https://github.com/melvinodsa/go-iam-docker
   - Server should be accessible at `http://localhost:3000`

2. **Development Environment**:

   - Appropriate runtime for your chosen language
   - Package manager (go mod, npm, pip, etc.)

3. **Valid Credentials**:
   - Client ID and Client Secret from Go IAM
   - Access to Go IAM login interface

## General Usage Pattern

All examples follow a similar pattern:

1. **Setup Go IAM Server** - Use Docker setup
2. **Configure Credentials** - Update client ID/secret in example code
3. **Obtain JWT Token** - Login via Go IAM web interface and extract token from browser storage
4. **Run Server** - Start the example application server
5. **Test Client** - Use provided client code to test authentication

## Project Structure

```
go-iam-examples/
├── README.md                 # This file - main documentation
├── golang/                   # Golang examples
│   ├── README.md            # Golang-specific documentation
│   ├── main.go              # Main server application
│   ├── client/              # HTTP client examples
│   └── go.mod               # Dependencies
├── nodejs/                   # Node.js examples
│   ├── README.md            # Node.js-specific documentation
│   ├── server.js            # Express.js server application
│   ├── client/              # HTTP client examples
│   └── package.json         # Dependencies and scripts
├── typescript/               # TypeScript examples
│   ├── README.md            # TypeScript-specific documentation
│   ├── src/                 # TypeScript source files
│   │   ├── server.ts        # Express.js server with full typing
│   │   └── client/          # HTTP client examples
│   ├── dist/                # Compiled JavaScript (after build)
│   ├── tsconfig.json        # TypeScript configuration
│   ├── package.json         # Dependencies and scripts
│   └── .env.example         # Environment variables template
├── python/                   # Python examples
│   ├── README.md            # Python-specific documentation
│   ├── server.py            # FastAPI server application
│   ├── client/              # HTTP client examples
│   ├── requirements.txt     # Python dependencies
│   ├── venv/                # Virtual environment (after setup)
│   └── .env.example         # Environment variables template
└── [future directories]     # Additional language examples
```

## Getting Started

1. **Choose Your Language**: Navigate to the appropriate directory
2. **Read the Specific README**: Each example has detailed setup instructions
3. **Follow Prerequisites**: Ensure Go IAM server is running
4. **Run the Example**: Follow the step-by-step guide in each directory

## Support and Documentation

- **Go IAM Docker Setup**: https://github.com/melvinodsa/go-iam-docker
- **Go IAM SDK Documentation**: Check individual example directories for SDK usage
- **Issues**: Report problems in the respective example directories

## Contributing

We welcome contributions! If you'd like to add examples for additional languages or frameworks:

1. Create a new directory for your language/framework
2. Follow the existing structure and documentation patterns
3. Include a comprehensive README with setup instructions
4. Add your example to this main README

## License

This project follows the same license as the Go IAM project. Please refer to the main Go IAM repository for license details.

---

**Note**: This repository contains example code for demonstration purposes. For production use, ensure you follow security best practices and review the code according to your specific requirements.
