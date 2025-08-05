# Go IAM Example - Python

This example demonstrates how to integrate Go IAM authentication into a Python web application using FastAPI and the official `goiam-python` SDK package.

## Overview

The example consists of:

- **`server.py`**: A FastAPI web server with JWT authentication middleware that validates tokens using the Go IAM 3. **Exception Handling**: Proper error handling with custom exception handlers

4. **Environment Variables**: Secure configuration management with python-dotenv
5. **Class-Based Design**: Object-oriented approach for the HTTP client
6. **Context Managers**: Proper resource management and cleanup
7. **Testing Utilities**: Comprehensive testing tools for validation and debugging
8. **Interactive Development**: Scripts for testing and validating authentication flow- **`client/httpclient.py`**: A Python HTTP client that demonstrates how to make authenticated requests to the server

- **`test_auth.py`**: Advanced testing script for the authenticate_token function with detailed diagnostics
- **`test_token.py`**: Interactive token tester for validating JWT tokens with Go IAM
- **`test_setup.py`**: Setup validation script to verify installation and configuration
- **`setup.sh`**: Automated setup script for virtual environment and dependencies
- **Modern Python features**: Type hints, dependency injection, comprehensive error handling, and testing utilities

## Prerequisites

- Python 3.8 or later
- pip (Python Package Manager)
- Virtual environment (recommended)
- Docker and Docker Compose (for running Go IAM server)
- Access to the Go IAM server

## Quick Setup

For a fast setup, you can use the provided setup script:

```bash
cd python
./setup.sh
```

This script will:

- Create a virtual environment
- Install all dependencies
- Copy the environment template
- Run setup tests
- Validate the installation

After running the script, edit the `.env` file with your credentials and start the server.

## Manual Setup Instructions

### 1. Setup Go IAM Server

First, you need to set up and run the Go IAM server using Docker:

1. Follow the setup instructions at: https://github.com/melvinodsa/go-iam-docker
2. After setting up, configure Go IAM by following the configuration video/documentation
3. Start the Go IAM server (it should be running on `http://localhost:3000`)

### 2. Create Virtual Environment (Recommended)

Create and activate a Python virtual environment:

```bash
cd python

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate
```

### 3. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Copy the environment template and customize it:

```bash
cp .env.example .env
```

Edit the `.env` file with your specific configuration:

```env
# Go IAM Configuration
GO_IAM_BASE_URL=http://localhost:3000
GO_IAM_CLIENT_ID=your-actual-client-id
GO_IAM_CLIENT_SECRET=your-actual-client-secret

# Server Configuration
SERVER_PORT=3004
ENVIRONMENT=development

# Client Configuration (for testing)
JWT_TOKEN=your_actual_jwt_token_here
SERVER_URL=http://localhost:3004
```

### 5. Obtain JWT Token

1. Open your browser and navigate to the Go IAM login page
2. Login with your credentials
3. After successful login, open your browser's Developer Tools
4. Go to the **Application** tab (Chrome) or **Storage** tab (Firefox)
5. Navigate to **Local Storage**
6. Find and copy the value of the `access_token` key

### 6. Configure JWT Token for HTTP Client

Add the JWT token to your `.env` file:

```env
# Add to your .env file
JWT_TOKEN=your_actual_jwt_token_here
SERVER_URL=http://localhost:3004
```

Or set it directly as an environment variable:

```bash
export JWT_TOKEN=your_actual_jwt_token_here
export SERVER_URL=http://localhost:3004  # optional, defaults to localhost:3004
```

## Testing Your Setup

Before running the full example, you can test your authentication setup using the provided testing utilities:

### 1. Validate Installation

```bash
# Test that all packages are installed correctly
python test_setup.py
```

### 2. Test JWT Token Authentication

#### Interactive Token Tester (Recommended)

```bash
# Interactive token validation with detailed feedback
python test_token.py
```

This will prompt you for a JWT token and test it against your Go IAM server.

#### Command Line Token Tester

```bash
# Test with environment variable
export JWT_TOKEN="your_actual_jwt_token_here"
python test_auth.py

# Or pass token directly
python test_auth.py "your_actual_jwt_token_here"
```

#### Manual Testing in Python Shell

```python
# Import the authentication function
from server import authenticate_token

# Create mock credentials
class MockCredentials:
    def __init__(self, token): self.credentials = token

# Test your token
token = "your_jwt_token_here"
credentials = MockCredentials(token)
user_data = authenticate_token(credentials)
print(user_data)  # Should show user information
```

## Running the Example

### 1. Start the FastAPI Server

In the python directory with your virtual environment activated:

```bash
# Development mode with auto-reload
python server.py
```

Or using uvicorn directly:

```bash
uvicorn server:app --host 0.0.0.0 --port 3004 --reload
```

The server will start on `http://localhost:3004` and display logs indicating it's ready.

### 2. Test with Python HTTP Client

In a new terminal, ensure your virtual environment is activated and run the Python HTTP client:

```bash
# Activate virtual environment if not already active
source venv/bin/activate

# Run the client
python client/httpclient.py
```

Or run directly with environment variables:

```bash
JWT_TOKEN=your_actual_jwt_token_here python client/httpclient.py
```

### Expected Output

If everything is configured correctly, you should see:

```
🚀 Starting Go IAM Python client tests...

🔗 Server URL: http://localhost:3004
🔑 Using JWT token: eyJhbGciOiJIUzI1NiIs...

Testing main endpoint...
✅ Main endpoint successful!
Response: {
  'message': 'Hello, <your-name>!',
  'user': {
    'id': 'user-id',
    'name': '<your-name>',
    'email': 'your-email@example.com',
    # ... other user properties
  }
}

Testing health endpoint...
✅ Health endpoint successful!
Response: {
  'status': 'healthy',
  'user': '<your-name>',
  'timestamp': '2025-01-XX...'
}

Testing profile endpoint...
✅ Profile endpoint successful!
Response: {
  'profile': {
    'id': 'user-id',
    'name': '<your-name>',
    # ... full user profile
  },
  'timestamp': '2025-01-XX...'
}

Testing API info endpoint...
✅ API info endpoint successful!
Response: {
  'api': 'Go IAM Python Example',
  'version': '1.0.0',
  'framework': 'FastAPI',
  'sdk': 'goiam-python',
  'user_id': 'user-id',
  'authenticated': True
}

🎉 Tests completed! 4/4 successful
```

Where `<your-name>` will be replaced with your actual name from the Go IAM user profile.

## Code Explanation

### Server (`server.py`)

- **FastAPI Framework**: Modern, fast web framework with automatic API documentation
- **Go IAM SDK Integration**: Uses the official `goiam-python` package for authentication
- **Dependency Injection**: FastAPI's dependency injection system for clean authentication middleware
- **Type Hints**: Full type annotations for better code clarity and IDE support
- **Async Support**: Asynchronous request handling for better performance
- **Automatic Documentation**: FastAPI generates interactive API docs at `/docs`

### Client (`client/httpclient.py`)

- **Object-Oriented Design**: Clean class-based HTTP client implementation
- **Environment Configuration**: Automatic loading of configuration from environment variables
- **Comprehensive Testing**: Tests multiple endpoints with proper error handling
- **Type Safety**: Type hints for better code maintainability
- **User-Friendly Output**: Structured logging with emojis and clear success/failure indicators

### Testing Utilities

#### `test_setup.py`

- **Installation Validation**: Verifies all packages are installed correctly
- **Service Creation**: Tests Go IAM service initialization
- **Compilation Check**: Validates server.py compiles without errors

#### `test_auth.py`

- **Advanced Token Testing**: Detailed testing of the authenticate_token function
- **Direct SDK Testing**: Tests the Go IAM SDK directly
- **Error Diagnostics**: Comprehensive error reporting and debugging information

#### `test_token.py`

- **Interactive Testing**: User-friendly interactive token validation
- **Multiple Test Modes**: Environment variable or manual token input
- **Real-time Feedback**: Immediate validation results with detailed user information

## API Endpoints

### `GET /`

- **Description**: Main protected endpoint that returns a personalized greeting
- **Authentication**: Required (JWT token)
- **Response**: JSON with message and user information

### `GET /health`

- **Description**: Health check endpoint with user context
- **Authentication**: Required (JWT token)
- **Response**: JSON with status, user name, and timestamp

### `GET /profile`

- **Description**: User profile endpoint returning full user information
- **Authentication**: Required (JWT token)
- **Response**: JSON with complete user profile and timestamp

### `GET /api/info`

- **Description**: API information endpoint with framework and SDK details
- **Authentication**: Required (JWT token)
- **Response**: JSON with API metadata and user information

## Python Features Demonstrated

1. **Type Hints**: Comprehensive type annotations throughout the codebase
2. **Async/Await**: Modern asynchronous programming patterns
3. **Dependency Injection**: FastAPI's dependency system for clean middleware
4. **Exception Handling**: Proper error handling with custom exception handlers
5. **Environment Variables**: Secure configuration management with python-dotenv
6. **Class-Based Design**: Object-oriented approach for the HTTP client
7. **Context Managers**: Proper resource management and cleanup

## Configuration Options

### Environment Variables

The application supports the following environment variables:

| Variable               | Description                   | Default                 | Used By |
| ---------------------- | ----------------------------- | ----------------------- | ------- |
| `GO_IAM_BASE_URL`      | Go IAM server URL             | `http://localhost:3000` | Server  |
| `GO_IAM_CLIENT_ID`     | Go IAM client ID              | -                       | Server  |
| `GO_IAM_CLIENT_SECRET` | Go IAM client secret          | -                       | Server  |
| `SERVER_PORT`          | Server port                   | `3004`                  | Server  |
| `ENVIRONMENT`          | Environment name              | `development`           | Server  |
| `JWT_TOKEN`            | JWT token for client requests | -                       | Client  |
| `SERVER_URL`           | Target server URL for client  | `http://localhost:3004` | Client  |

### Setting Environment Variables

#### Using .env file (Recommended)

```bash
# Copy the example file
cp .env.example .env

# Edit the .env file with your values
# The python-dotenv package will automatically load these
```

#### Direct export

```bash
export GO_IAM_BASE_URL=http://localhost:3000
export GO_IAM_CLIENT_ID=your-client-id
export GO_IAM_CLIENT_SECRET=your-client-secret
export JWT_TOKEN=your_actual_jwt_token_here
```

## FastAPI Features

### Interactive API Documentation

FastAPI automatically generates interactive API documentation:

- **Swagger UI**: Available at `http://localhost:3004/docs`
- **ReDoc**: Available at `http://localhost:3004/redoc`
- **OpenAPI Schema**: Available at `http://localhost:3004/openapi.json`

### Security

- **HTTP Bearer Authentication**: Proper JWT token handling
- **Automatic Validation**: Request/response validation with Pydantic
- **Error Handling**: Structured error responses

## Troubleshooting

### Common Issues

1. **"ModuleNotFoundError: No module named 'goiam_python'"**:

   - Ensure virtual environment is activated: `source venv/bin/activate`
   - Install dependencies: `pip install -r requirements.txt`
   - Run setup validation: `python test_setup.py`

2. **"JWT_TOKEN environment variable is not set"**:

   - Ensure you've set the JWT_TOKEN environment variable
   - Check that the .env file exists and contains JWT_TOKEN
   - Verify the JWT token is copied correctly from the browser
   - Make sure python-dotenv is loading the .env file properly
   - Test your token: `python test_token.py`

3. **Import Errors**:

   - Ensure virtual environment is activated: `source venv/bin/activate`
   - Install dependencies: `pip install -r requirements.txt`
   - Check Python version: `python --version` (should be 3.8+)
   - Validate setup: `python test_setup.py`

4. **"Unauthorized" Response**:

   - Ensure your JWT token is valid and not expired
   - Check that the token is properly formatted in the Authorization header
   - Verify Go IAM server is running on the correct port
   - Test token directly: `python test_auth.py "your_token_here"`

5. **Connection Refused**:

   - Ensure Go IAM server is running on `http://localhost:3000`
   - Ensure the example server is running on `http://localhost:3004`
   - Check that SERVER_URL environment variable is set correctly
   - Test connectivity: `python test_token.py`

6. **Port Already in Use**:
   - Change the port in the .env file or SERVER_PORT environment variable
   - Kill any processes using port 3004: `lsof -ti:3004 | xargs kill -9`

### Debugging Tips

- Run setup validation first: `python test_setup.py`
- Test JWT tokens interactively: `python test_token.py`
- Check server logs for detailed error messages
- Verify client credentials match your Go IAM configuration
- Use the FastAPI interactive docs at `/docs` for manual testing
- Test the Go IAM server directly with tools like Postman or curl
- Verify environment variables are set: `echo $JWT_TOKEN`
- Check that .env file is in the correct directory and properly formatted
- Use Python's built-in logging for debugging
- Test authentication function directly: `python test_auth.py`

## Development Workflow

1. **Setup**: Create virtual environment and install dependencies (`./setup.sh`)
2. **Validation**: Run setup tests (`python test_setup.py`)
3. **Token Testing**: Validate JWT tokens (`python test_token.py`)
4. **Configuration**: Set up environment variables
5. **Development**: Use auto-reload for development (`python server.py`)
6. **Testing**: Use the HTTP client or FastAPI docs for testing
7. **Documentation**: View interactive docs at `/docs`
8. **Debugging**: Use testing utilities for troubleshooting

## Project Structure

```
python/
├── README.md              # This documentation
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
├── .gitignore           # Git ignore patterns
├── setup.sh             # Automated setup script
├── server.py            # FastAPI server with Go IAM authentication
├── test_setup.py        # Installation and setup validation
├── test_auth.py         # Advanced authenticate_token function testing
├── test_token.py        # Interactive JWT token validation
├── client/              # HTTP client examples
│   ├── __init__.py     # Python package marker
│   └── httpclient.py   # HTTP client for testing endpoints
├── venv/               # Virtual environment (after setup)
└── __pycache__/        # Python compiled bytecode (auto-generated)
```

## Virtual Environment Management

```bash
# Create virtual environment
python -m venv venv

# Activate (macOS/Linux)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Deactivate when done
deactivate
```

## Next Steps

- Explore additional Go IAM SDK features with Python
- Implement role-based access control with FastAPI dependencies
- Add more protected endpoints with different functionality
- Integrate with your existing Python applications
- Add comprehensive testing with pytest
- Implement advanced FastAPI features (WebSockets, background tasks)
- Add request/response logging and monitoring

## Dependencies

- **FastAPI**: Modern, fast web framework for building APIs with Python
- **goiam-python**: Official Go IAM SDK for Python applications
- **uvicorn**: ASGI server for running FastAPI applications
- **requests**: HTTP library for making requests in the client
- **python-dotenv**: Environment variable management
- **python-multipart**: For form data parsing (FastAPI dependency)

For more information about Go IAM, visit the official documentation and repository.
