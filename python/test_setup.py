#!/usr/bin/env python3
"""
Test script for Go IAM Python example
This script tests the basic functionality of the goiam-python package
"""

import sys
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_import():
    """Test if goiam package can be imported"""
    try:
        from goiam import new_service
        print("✅ Successfully imported goiam package")
        return True
    except ImportError as e:
        print(f"❌ Failed to import goiam package: {e}")
        return False

def test_service_creation():
    """Test if GoIAM service can be created"""
    try:
        from goiam import new_service
        
        base_url = os.getenv("GO_IAM_BASE_URL", "http://localhost:3000")
        client_id = os.getenv("GO_IAM_CLIENT_ID", "test")
        client_secret = os.getenv("GO_IAM_CLIENT_SECRET", "test")
        
        service = new_service(
            base_url=base_url,
            client_id=client_id,
            secret=client_secret
        )
        
        print("✅ Successfully created GoIAM service")
        print(f"   Base URL: {base_url}")
        print(f"   Client ID: {client_id[:8]}...")
        return True
    except Exception as e:
        print(f"❌ Failed to create GoIAM service: {e}")
        return False

def test_server_compilation():
    """Test if server.py compiles without errors"""
    try:
        import py_compile
        py_compile.compile('server.py', doraise=True)
        print("✅ server.py compiles successfully")
        return True
    except Exception as e:
        print(f"❌ server.py compilation failed: {e}")
        return False

def main():
    """Run all tests"""
    print("🧪 Testing Go IAM Python Example Setup")
    print("=" * 50)
    
    tests = [
        test_import,
        test_service_creation,
        test_server_compilation
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print("=" * 50)
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Your setup is ready.")
        print("\nNext steps:")
        print("1. Make sure Go IAM server is running")
        print("2. Update .env file with your actual credentials")
        print("3. Run: python server.py")
    else:
        print("⚠️  Some tests failed. Please check the errors above.")
        sys.exit(1)

if __name__ == "__main__":
    main()
