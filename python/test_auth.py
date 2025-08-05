#!/usr/bin/env python3
"""
Test script for authenticate_token function

This script allows you to test the authenticate_token function directly
without starting the full FastAPI server.
"""

import os
import sys
from typing import Dict, Any
from fastapi.security import HTTPAuthorizationCredentials
from dotenv import load_dotenv

# Add current directory to path to import server modules
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Load environment variables
load_dotenv()

def test_authenticate_token(token: str) -> None:
    """
    Test the authenticate_token function with a provided JWT token
    
    Args:
        token: JWT token to test
    """
    print("🔧 Testing authenticate_token function...")
    print(f"Token: {token[:20]}...{token[-10:] if len(token) > 30 else token}")
    print("-" * 50)
    
    try:
        # Import the authentication function from server
        from server import authenticate_token, goiam_service
        
        # Create mock credentials object
        class MockCredentials:
            def __init__(self, token: str):
                self.credentials = token
        
        credentials = MockCredentials(token)
        
        # Test the authentication
        print("🚀 Calling authenticate_token function...")
        user_data = authenticate_token(credentials)
        
        print("✅ Authentication successful!")
        print("👤 User data received:")
        print(f"   ID: {user_data.get('id')}")
        print(f"   Name: {user_data.get('name')}")
        print(f"   Email: {user_data.get('email')}")
        print(f"   Roles: {user_data.get('roles')}")
        
        return user_data
        
    except Exception as e:
        print(f"❌ Authentication failed: {str(e)}")
        print(f"Error type: {type(e).__name__}")
        return None

def test_goiam_service_directly(token: str) -> None:
    """
    Test the goiam service me() method directly
    
    Args:
        token: JWT token to test
    """
    print("\n🔧 Testing goiam service directly...")
    print("-" * 50)
    
    try:
        from server import goiam_service
        
        print("🚀 Calling goiam_service.me() directly...")
        user = goiam_service.me(token)
        
        print("✅ GoIAM service call successful!")
        print("👤 Raw user object:")
        print(f"   Type: {type(user)}")
        print(f"   User: {user}")
        
        # Try to access attributes
        print("\n📋 User attributes:")
        attributes = ['id', 'name', 'email', 'roles', 'username']
        for attr in attributes:
            try:
                value = getattr(user, attr, 'N/A')
                print(f"   {attr}: {value}")
            except Exception as e:
                print(f"   {attr}: Error accessing - {e}")
        
        return user
        
    except Exception as e:
        print(f"❌ GoIAM service call failed: {str(e)}")
        print(f"Error type: {type(e).__name__}")
        return None

def main():
    """Main test function"""
    print("🧪 Go IAM authenticate_token Test")
    print("=" * 50)
    
    # Get token from environment variable or command line
    token = os.getenv("JWT_TOKEN")
    
    if len(sys.argv) > 1:
        token = sys.argv[1]
    
    if not token or token == "your_jwt_token_here":
        print("❌ No JWT token provided!")
        print("\nUsage:")
        print("1. Set JWT_TOKEN environment variable:")
        print("   export JWT_TOKEN='your_actual_token'")
        print("   python test_auth.py")
        print("\n2. Or pass token as argument:")
        print("   python test_auth.py 'your_actual_token'")
        print("\n3. Or add it to your .env file:")
        print("   JWT_TOKEN=your_actual_token")
        sys.exit(1)
    
    print(f"🔑 Using token from: {'environment' if len(sys.argv) == 1 else 'command line'}")
    
    # Test the service directly first
    test_goiam_service_directly(token)
    
    # Test the authentication function
    test_authenticate_token(token)
    
    print("\n" + "=" * 50)
    print("🏁 Test completed!")

if __name__ == "__main__":
    main()
