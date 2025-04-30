#!/opt/homebrew/bin/python3
"""
OpenAI Chat Proof of Concept

A minimal CLI application that demonstrates the use of OpenAI's responses.create() endpoint.
This is a throwaway proof-of-concept that can run from the command line.
"""

import os
import sys
from typing import Dict, Any, List

# Third-party imports
from dotenv import load_dotenv
from openai import OpenAI
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown

# Initialize Rich console for better output formatting
console = Console()

def load_environment() -> None:
    """Load environment variables from .env file."""
    load_dotenv()
    
    # Check if the API key is available
    if not os.getenv("OPENAI_API_KEY"):
        console.print(
            Panel(
                "[bold red]Error:[/bold red] OPENAI_API_KEY not found in environment variables.\n"
                "Please make sure you have created a .env file with your API key.",
                title="Environment Error"
            )
        )
        sys.exit(1)

def initialize_client() -> OpenAI:
    """Initialize and return an OpenAI client."""
    return OpenAI()

def create_response(client: OpenAI, user_input: str) -> Dict[str, Any]:
    """
    Call the OpenAI API to generate a response.
    
    Args:
        client: OpenAI client instance
        user_input: Text input from the user
        
    Returns:
        The API response
    """
    try:
        # Format the input as required by the API
        formatted_input = [
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_text",
                        "text": user_input
                    }
                ]
            }
        ]
        
        # Call the API with the parameters from the reference snippet
        response = client.responses.create(
            model="gpt-4o",
            input=formatted_input,
            text={"format": {"type": "text"}},
            reasoning={},
            tools=[],
            temperature=1,
            max_output_tokens=1024,
            top_p=1,
            store=True
        )
        
        return response
    except Exception as e:
        console.print(
            Panel(
                f"[bold red]Error:[/bold red] {str(e)}",
                title="API Error"
            )
        )
        sys.exit(1)

def get_user_input() -> str:
    """Prompt the user for input and return it."""
    console.print(Panel("[bold blue]Enter your message:[/bold blue]", title="User Input"))
    return input("> ")

def display_response(response: Dict[str, Any]) -> None:
    """
    Display the API response in a formatted way.
    
    Args:
        response: The API response from OpenAI
    """
    try:
        # Debug the response structure
        console.print(f"Response type: {type(response)}")
        console.print(f"Response structure: {response}")
        
        # Extract the output text from the response
        # The structure might be different than expected, so let's handle it properly
        if hasattr(response, 'output') and hasattr(response.output, 'text'):
            # Original expected structure
            output_text = response.output.text
        elif hasattr(response, 'content') and isinstance(response.content, list):
            # Try to find text content in the response
            for item in response.content:
                if isinstance(item, dict) and item.get('type') == 'output_text':
                    output_text = item.get('text', 'No text found in response')
                    break
            else:
                output_text = "Could not find text content in response"
        else:
            # Fallback: convert the entire response to a string
            output_text = f"Response format changed. Raw response: {str(response)}"
        
        # Display the response in a panel with markdown formatting
        console.print(
            Panel(
                Markdown(output_text),
                title="[bold green]Assistant Response[/bold green]"
            )
        )
    except Exception as e:
        console.print(
            Panel(
                f"[bold red]Error displaying response:[/bold red] {str(e)}\n\n"
                f"Raw response: {str(response)}",
                title="Display Error"
            )
        )

def main() -> None:
    """Main entry point for the application."""
    # Display welcome message
    console.print(
        Panel(
            "[bold]OpenAI Chat Proof of Concept[/bold]\n"
            "A minimal CLI application that demonstrates the use of OpenAI's responses.create() endpoint.",
            title="Welcome"
        )
    )
    
    # Load environment variables
    load_environment()
    
    # Initialize the OpenAI client
    client = initialize_client()
    
    # Get user input
    user_input = get_user_input()
    
    # Show loading message
    with console.status("[bold blue]Generating response...[/bold blue]"):
        # Call the API
        response = create_response(client, user_input)
    
    # Display the response
    display_response(response)

if __name__ == "__main__":
    main()
