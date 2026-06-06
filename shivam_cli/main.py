import os
import sys
import time
from dotenv import load_dotenv
from rich.console import Console
from rich.live import Live
from rich.panel import Panel
from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style
from prompt_toolkit.patch_stdout import patch_stdout

# Add parent directory to path to allow imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ui.layout import create_layout
from core.agent import ShivamAgent

load_dotenv()

console = Console()

def main():
    # Setup OpenRouter
    api_key = os.getenv("OPENROUTER_API_KEY")
    model_id = os.getenv("MODEL_ID", "anthropic/claude-3.5-sonnet")

    if not api_key:
        console.print("[bold red]Error:[/] OPENROUTER_API_KEY not found.")
        api_key = console.input("[bold cyan]Enter your OpenRouter API Key: [/]")
        model_id = console.input("[bold cyan]Enter Model ID (default: anthropic/claude-3.5-sonnet): [/]") or model_id
        
        with open(".env", "a") as f:
            f.write(f"\nOPENROUTER_API_KEY={api_key}\nMODEL_ID={model_id}\n")

    agent = ShivamAgent(api_key, model_id)
    
    # Custom prompt style
    style = Style.from_dict({
        'prompt': 'bold #00ffff',
    })
    session = PromptSession(style=style)

    console.clear()
    console.print(create_layout())
    
    while True:
        try:
            with patch_stdout():
                user_input = session.prompt("\nshivam@ultra-instinct:~$ ")
            
            if not user_input:
                continue
                
            if user_input.lower() == '/exit':
                console.print("[bold red]Exiting SHIVAM CLI. Goodbye![/]")
                break
            
            if user_input.startswith('/goal '):
                goal = user_input[6:]
                console.print(f"[bold magenta]Initiating build for:[/] {goal}")
                
                # Show a "Thinking" state in the UI
                with console.status("[bold green]Shivam is planning and building...", spinner="dots"):
                    response = agent.chat(f"I want to build: {goal}. Please provide a plan and then execute it.")
                
                console.print(Panel(response, title="SHIVAM AI RESPONSE", border_style="green"))
            
            elif user_input == '/status':
                console.clear()
                console.print(create_layout())
            
            elif user_input == '/clear':
                console.clear()
                console.print(create_layout())
            
            else:
                with console.status("[bold cyan]Shivam is thinking...", spinner="dots"):
                    response = agent.chat(user_input)
                console.print(Panel(response, title="SHIVAM AI RESPONSE", border_style="green"))

        except KeyboardInterrupt:
            break
        except Exception as e:
            console.print(f"[bold red]An error occurred:[/] {str(e)}")

if __name__ == "__main__":
    main()
