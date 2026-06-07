import os
import json
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, IntPrompt
from rich.table import Table

console = Console()

CONFIG_FILE = os.path.expanduser("~/.shivam_config.json")

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    return {}

def save_config(config):
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=4)

def setup_wizard():
    console.clear()
    console.print(Panel.fit("🛠️ SHIVAM CLI SETUP WIZARD", style="bold magenta"))
    
    config = load_config()
    
    providers = {
        "1": ("OpenRouter", "OPENROUTER_API_KEY"),
        "2": ("Gemini", "GEMINI_API_KEY"),
        "3": ("OpenAI", "OPENAI_API_KEY"),
        "4": ("Anthropic", "ANTHROPIC_API_KEY"),
        "5": ("HuggingFace", "HF_API_KEY"),
        "6": ("Nvidia", "NVIDIA_API_KEY")
    }
    
    table = Table(title="Select AI Provider")
    table.add_column("ID", style="cyan")
    table.add_column("Provider", style="white")
    
    for k, v in providers.items():
        table.add_row(k, v[0])
    
    console.print(table)
    choice = Prompt.ask("Choose a provider", choices=list(providers.keys()), default="1")
    
    provider_name, env_var = providers[choice]
    api_key = Prompt.ask(f"Enter your {provider_name} API Key", password=True)
    model_id = Prompt.ask(f"Enter Model ID for {provider_name}", default="anthropic/claude-3.5-sonnet" if choice == "1" else "gemini-1.5-pro")
    
    config["active_provider"] = provider_name
    config["api_key"] = api_key
    config["model"] = model_id
    config["env_var"] = env_var
    
    save_config(config)
    console.print(f"[bold green]Success![/] Configured {provider_name} with model {model_id}")
    return config
