#!/usr/bin/env python3
"""
Interactive JWT Token Tester for Go IAM

This script provides an interactive way to test JWT tokens with the Go IAM service.
"""

import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def interactive_test():
    """Interactive token testing"""
    print("🔐 Go IAM Interactive Token Tester")
    print("=" * 40)
    
    # Check if token is in environment
    env_token = os.getenv("JWT_TOKEN")
    if env_token and env_token != "your_jwt_token_here":
        print(f"📋 Found JWT_TOKEN in environment: {env_token[:20]}...")
        use_env = input("Use this token? (y/n): ").lower().strip()
        if use_env == 'y':
            token = env_token
        else:
            token = input("Enter your JWT token: ").strip()
    else:
        print("🔑 Please enter your JWT token:")
        token = input("Token: ").strip()
    
    if not token:
        print("❌ No token provided. Exiting.")
        return
    
    print(f"\n🧪 Testing token: {token[:20]}...")
    print("-" * 40)
    
    try:
        # Import and test
        from goiam import new_service
        
        # Get configuration
        base_url = os.getenv("GO_IAM_BASE_URL", "http://localhost:3000")
        client_id = os.getenv("GO_IAM_CLIENT_ID", "abcdef1234567890abcdef1234567890")
        client_secret = os.getenv("GO_IAM_CLIENT_SECRET", "abcdef1234567890abcdef1234567890")
        
        print(f"🌐 Go IAM Base URL: {base_url}")
        print(f"🆔 Client ID: {client_id[:8]}...")
        
        # Create service
        service = new_service(
            base_url=base_url,
            client_id=client_id,
            secret=client_secret
        )
        
        print("✅ Go IAM service created successfully")
        
        # Test the token
        print("🚀 Validating token with Go IAM...")
        user = service.me(token)
        
        print("✅ Token validation successful!")
        print("\n👤 User Information:")
        print(f"   Raw object: {user}")
        print(f"   Type: {type(user)}")
        
        # Try to extract common attributes
        attributes = ['id', 'name', 'email', 'username', 'roles']
        for attr in attributes:
            try:
                value = getattr(user, attr, None)
                if value is not None:
                    print(f"   {attr}: {value}")
            except:
                pass
        
        # Test the authenticate_token function
        print("\n🔧 Testing authenticate_token function...")
        try:
            from server import authenticate_token
            
            class MockCredentials:
                def __init__(self, token):
                    self.credentials = token
            
            mock_creds = MockCredentials(token)
            user_dict = authenticate_token(mock_creds)
            
            print("✅ authenticate_token function successful!")
            print("📊 Processed user data:")
            for key, value in user_dict.items():
                print(f"   {key}: {value}")
                
        except Exception as e:
            print(f"❌ authenticate_token failed: {e}")
        
    except Exception as e:
        print(f"❌ Token validation failed: {str(e)}")
        print(f"Error type: {type(e).__name__}")
        
        if "401" in str(e) or "Unauthorized" in str(e):
            print("\n💡 Possible issues:")
            print("   - Token might be expired")
            print("   - Token might be invalid")
            print("   - Go IAM server might not be running")
        elif "Connection" in str(e) or "timeout" in str(e).lower():
            print("\n💡 Possible issues:")
            print("   - Go IAM server is not running")
            print("   - Check if Go IAM is accessible at:", base_url)
        else:
            print("\n💡 Check your Go IAM server configuration")

if __name__ == "__main__":
    try:
        interactive_test()
    except KeyboardInterrupt:
        print("\n\n👋 Test cancelled by user")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
    
    print("\n🏁 Done!")
