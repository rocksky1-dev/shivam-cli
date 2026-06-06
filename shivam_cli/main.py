import os
import sys
from dotenv import load_dotenv
from rich.console import Console
from rich.live import Live
from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style

# Add parent directory to path to allow imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ui.layout import create_layout, get_execution_matrix
from core.agent import ShivamAgent

load_dotenv()

console = Console()

def main():
    # Setup OpenRouter
    api_key = os.getenv("OPENROUTER_API_KEY")
    model_id = os.getenv("MODEL_ID", "anthropic/claude-3.5-sonnet")

    if not api_key:
        console.print("[bold red]Error:[/] OPENROUTER_API_KEY not found in environment or .env file.")
        api_key = console.input("[bold cyan]Enter your OpenRouter API Key: [/]")
        model_id = console.input("[bold cyan]Enter Model ID (default: anthropic/claude-3.5-sonnet): [/]") or model_id
        
        with open(".env", "a") as f:
            f.write(f"\nOPENROUTER_API_KEY={api_key}\nMODEL_ID={model_id}\n")

    agent = ShivamAgent(api_key, model_id)
    layout = create_layout()
    
    # Custom prompt style
    style = Style.from_dict({
        'prompt': 'bold #00ffff',
    })
    session = PromptSession(style=style)

    console.clear()
    
    with Live(layout, refresh_per_second=4, screen=True):
        while True:
            try:
                # In a real CLI, we'd handle the input outside the Live context or use a sub-layout
                # For this demo, we'll exit Live to get input then re-enter or just use standard input
                pass
            except KeyboardInterrupt:
                break
    
    # Interactive loop (simplified for now)
    console.print(create_layout())
    
    while True:
        try:
            user_input = session.prompt("\n> Type '/goal <your idea>' to build something amazing... ")
            
            if user_input.lower() == '/exit':
                console.print("[bold red]Exiting SHIVAM CLI. Goodbye![/]")
                break
            
            if user_input.startswith('/goal '):
                goal = user_input[6:]
                console.print(f"[bold magenta]Initiating build for:[/] {goal}")
                # Logic to update matrix and run agent
                response = agent.chat(f"I want to build: {goal}. Please provide a plan and then execute it.")
                console.print(Panel(response, title="SHIVAM AI RESPONSE", border_style="green"))
            
            elif user_input == '/status':
                console.print(create_layout())
            
            else:
                response = agent.chat(user_input)
                console.print(Panel(response, title="SHIVAM AI RESPONSE", border_style="green"))

        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()
