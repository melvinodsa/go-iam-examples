"""
Go IAM Python Example - FastAPI Server

This example demonstrates how to integrate Go IAM authentication into a Python web application
using FastAPI and the official goiam-python SDK package.
"""

import os
from typing import Optional, Dict, Any
from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from goiam import new_service
from dotenv import load_dotenv
import uvicorn

# Load environment variables
load_dotenv()

app = FastAPI(
    title="Go IAM Python Example",
    description="FastAPI server with Go IAM authentication",
    version="1.0.0"
)

# Configuration
class Config:
    def __init__(self):
        self.base_url = os.getenv("GO_IAM_BASE_URL", "http://localhost:3000")
        self.client_id = os.getenv("GO_IAM_CLIENT_ID", "abcdef1234567890abcdef1234567890")
        self.client_secret = os.getenv("GO_IAM_CLIENT_SECRET", "abcdef1234567890abcdef1234567890")
        self.port = int(os.getenv("SERVER_PORT", "3004"))

config = Config()

# Initialize Go IAM service
goiam_service = new_service(
    base_url=config.base_url,
    client_id=config.client_id,
    secret=config.client_secret
)

# Security scheme
security = HTTPBearer()

def authenticate_token(credentials: HTTPAuthorizationCredentials = Depends(security)) -> Dict[str, Any]:
    """
    Authentication dependency that validates JWT tokens with Go IAM
    """
    try:
        # Validate token with Go IAM service
        user = goiam_service.me(credentials.credentials)
        # Convert User object to dictionary
        return {
            "id": getattr(user, 'id', None),
            "name": getattr(user, 'name', None),
            "email": getattr(user, 'email', None),
            "roles": getattr(user, 'roles', [])
        }
    except Exception as e:
        print(f"Token validation error: {str(e)}")
        raise HTTPException(
            status_code=401,
            detail="Unauthorized - Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )

@app.get("/")
def root(user: Dict[str, Any] = Depends(authenticate_token)) -> Dict[str, Any]:
    """
    Main protected endpoint that returns a personalized greeting
    """
    return {
        "message": f"Hello, {user.get('name', 'User')}!",
        "user": user
    }

@app.get("/health")
def health_check(user: Dict[str, Any] = Depends(authenticate_token)) -> Dict[str, Any]:
    """
    Health check endpoint with user context
    """
    return {
        "status": "healthy",
        "user": user.get('name', 'Unknown'),
        "timestamp": "2025-01-01T00:00:00Z"  # In real implementation, use datetime.utcnow().isoformat()
    }

@app.get("/profile")
def user_profile(user: Dict[str, Any] = Depends(authenticate_token)) -> Dict[str, Any]:
    """
    User profile endpoint returning full user information
    """
    from datetime import datetime
    return {
        "profile": user,
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }

@app.get("/api/info")
def api_info(user: Dict[str, Any] = Depends(authenticate_token)) -> Dict[str, Any]:
    """
    API information endpoint
    """
    return {
        "api": "Go IAM Python Example",
        "version": "1.0.0",
        "framework": "FastAPI",
        "sdk": "goiam-python",
        "user_id": user.get('id'),
        "authenticated": True
    }

# Error handlers
@app.exception_handler(HTTPException)
def http_exception_handler(request: Request, exc: HTTPException):
    return {
        "error": exc.detail,
        "status_code": exc.status_code
    }

# Startup event
@app.on_event("startup")
def startup_event():
    print(f"Go IAM Python example server starting on http://localhost:{config.port}")
    print(f"Make sure Go IAM server is running on {config.base_url}")
    print(f"Environment: {os.getenv('ENVIRONMENT', 'development')}")

if __name__ == "__main__":
    uvicorn.run(
        "server:app",
        host="0.0.0.0",
        port=config.port,
        reload=True,
        log_level="info"
    )
