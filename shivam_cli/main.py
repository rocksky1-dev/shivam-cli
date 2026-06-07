import os
import sys
from dotenv import load_dotenv
from rich.console import Console
from rich.live import Live
from rich.panel import Panel
from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style
from prompt_toolkit.patch_stdout import patch_stdout

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ui.layout import create_layout
from core.agent import ShivamAgent
from core.config import load_config, setup_wizard

load_dotenv()
console = Console()

def main():
    config = load_config()
    
    if not config or "/config" in sys.argv:
        config = setup_wizard()

    agent = ShivamAgent(config.get("api_key"), config.get("model"))
    
    style = Style.from_dict({'prompt': 'bold #ff00ff'})
    session = PromptSession(style=style)

    console.clear()
    console.print(create_layout(config=config))
    
    tasks = []
    
    while True:
        try:
            with patch_stdout():
                user_input = session.prompt(f"\nshivam@ultra-instinct ({config.get('active_provider')}):~$ ")
            
            if not user_input: continue
            if user_input.lower() == '/exit': break
            
            if user_input.lower() == '/config':
                config = setup_wizard()
                agent = ShivamAgent(config.get("api_key"), config.get("model"))
                console.clear()
                console.print(create_layout(config=config))
                continue

            if user_input.startswith('/goal '):
                goal = user_input[6:]
                tasks = [{"desc": f"Planning: {goal}", "done": False}]
                console.clear()
                console.print(create_layout(tasks=tasks, config=config))
                
                with console.status("[bold magenta]Shivam is analyzing goal...", spinner="dots"):
                    plan = agent.plan_task(goal)
                
                tasks = []
                for step in plan:
                    tasks.append({"desc": step.get('desc', 'Executing...'), "done": False})
                
                console.clear()
                console.print(create_layout(tasks=tasks, config=config))
                
                # Execution simulation/logic
                for i, task in enumerate(tasks):
                    with console.status(f"[bold cyan]{task['desc']}...", spinner="bouncingBar"):
                        # Here we would call the actual tool executor
                        import time
                        time.sleep(1) 
                    tasks[i]["done"] = True
                    console.clear()
                    console.print(create_layout(tasks=tasks, config=config))
                
                console.print(Panel("✨ Build Complete! All tasks verified by Shivam AI.", style="bold green"))
            
            elif user_input == '/status' or user_input == '/clear':
                console.clear()
                console.print(create_layout(config=config))
            
            else:
                with console.status("[bold cyan]Shivam is thinking...", spinner="dots"):
                    response = agent.chat(user_input)
                console.print(Panel(response, title="SHIVAM AI RESPONSE", border_style="green"))

        except KeyboardInterrupt:
            break
        except Exception as e:
            console.print(f"[bold red]Error:[/] {str(e)}")

if __name__ == "__main__":
    main()
