#!/bin/bash

# Quick setup script for Go IAM Python example
echo "🚀 Setting up Go IAM Python Example..."

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
else
    echo "✅ Virtual environment already exists"
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📥 Installing dependencies..."
pip install -r requirements.txt

# Copy environment file if it doesn't exist
if [ ! -f ".env" ]; then
    echo "📋 Creating .env file from template..."
    cp .env.example .env
    echo "⚠️  Please edit .env file with your actual Go IAM credentials"
else
    echo "✅ .env file already exists"
fi

# Run setup test
echo "🧪 Testing setup..."
python test_setup.py

echo ""
echo "🎉 Setup complete! Next steps:"
echo "1. Edit .env file with your Go IAM credentials"
echo "2. Obtain JWT token from Go IAM"
echo "3. Run: python server.py"
echo ""
echo "To activate the virtual environment later, run:"
echo "source venv/bin/activate"
