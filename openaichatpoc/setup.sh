#!/bin/bash
# Setup script for OpenAI Chat Proof of Concept
# This script creates a virtual environment, installs dependencies,
# and sets up the .env file with the OpenAI API key.

# Set the script to exit on error
set -e

# Define colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Print a message with a color
print_message() {
    echo -e "${2}${1}${NC}"
}

# Check if Python is available
if ! command -v /opt/homebrew/bin/python3 &> /dev/null; then
    print_message "Error: /opt/homebrew/bin/python3 not found. Please install Python using Homebrew." "$RED"
    exit 1
fi

# Create a virtual environment
print_message "Creating virtual environment..." "$GREEN"
/opt/homebrew/bin/python3 -m venv venv

# Activate the virtual environment
print_message "Activating virtual environment..." "$GREEN"
source venv/bin/activate

# Install dependencies
print_message "Installing dependencies..." "$GREEN"
pip install -r requirements.txt

# Set up .env file if it doesn't exist
if [ ! -f .env ]; then
    print_message "Setting up .env file..." "$GREEN"
    cp .env.example .env
    
    # Prompt for OpenAI API key
    print_message "Please enter your OpenAI API key:" "$YELLOW"
    read -r api_key
    
    # Replace the placeholder with the actual API key
    if [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS
        sed -i '' "s/your_api_key_here/$api_key/" .env
    else
        # Linux
        sed -i "s/your_api_key_here/$api_key/" .env
    fi
    
    print_message "API key saved to .env file." "$GREEN"
else
    print_message ".env file already exists. Skipping..." "$YELLOW"
fi

# Make the app.py executable
chmod +x app.py

print_message "\nSetup complete! You can now run the application with:" "$GREEN"
print_message "source venv/bin/activate" "$YELLOW"
print_message "python app.py" "$YELLOW"
print_message "deactivate  # When finished" "$YELLOW"
