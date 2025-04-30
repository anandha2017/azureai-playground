# OpenAI Chat Proof of Concept

A minimal Python-based front-end that calls the OpenAI API's `client.responses.create()` endpoint. This is a throwaway proof-of-concept that can run from the command line.

## Features

- Simple CLI interface for interacting with OpenAI's API
- Uses the `responses.create()` endpoint with GPT-4o
- Secure environment variable management
- Clean virtual environment setup to avoid system clutter

## Project Structure

```
openaichatpoc/
├── app.py            # Main entry-point with CLI interface
├── requirements.txt  # Dependencies with pinned versions
├── setup.sh          # Setup script for virtual environment
├── .env.example      # Template for environment variables
└── .gitignore        # Ensures .env and venv are ignored
```

## Prerequisites

- macOS with Homebrew installed
- Python 3 installed via Homebrew (`/opt/homebrew/bin/python3`)
- OpenAI API key (get one at https://platform.openai.com/api-keys)

## Setup

The setup process creates a virtual environment, installs dependencies, and configures your API key, all while keeping your system clean:

```bash
# Navigate to the project directory
cd openaichatpoc

# Make the setup script executable (if not already)
chmod +x setup.sh

# Run the setup script
./setup.sh
```

The setup script will:
1. Create a virtual environment using Homebrew's Python
2. Install the required dependencies in the virtual environment
3. Create a `.env` file from the template and prompt for your API key

## Usage

To run the application:

```bash
# Navigate to the project directory
cd openaichatpoc

# Activate the virtual environment
source venv/bin/activate

# Run the application
python app.py

# When finished, deactivate the virtual environment
deactivate
```

## Security Notes

- Your API key is stored in the `.env` file, which is excluded from version control via `.gitignore`
- All dependencies are isolated in the virtual environment, keeping your system clean
- The application validates inputs and handles errors gracefully

## Cleanup

To remove the application and all its dependencies:

```bash
# Simply delete the project directory
rm -rf openaichatpoc
```

Since all dependencies are contained in the virtual environment, this will completely remove everything related to the application from your system.
