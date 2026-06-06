import os
from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.live import Live
from rich.columns import Columns
from rich.progress import Progress, BarColumn, TextColumn

console = Console()

def get_header():
    ascii_art = """
   ███████╗██╗  ██╗██╗██╗   ██╗ █████╗ ███╗   ███╗     ██████╗██╗     ██╗
   ██╔════╝██║  ██║██║██║   ██║██╔══██╗████╗ ████║    ██╔════╝██║     ██║
   ███████╗███████║██║██║   ██║███████║██╔████╔██║    ██║     ██║     ██║
   ╚════██║██╔══██║██║╚██╗ ██╔╝██╔══██║██║╚██╔╝██║    ██║     ██║     ██║
   ███████║██║  ██║██║ ╚████╔╝ ██║  ██║██║ ╚═╝ ██║    ╚██████╗███████╗██║
   ╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝  ╚═╝  ╚═╝╚═╝     ╚═╝     ╚═════╝╚══════╝╚═╝
    """
    header_text = Text(ascii_art, style="bold magenta")
    header_text.append("\nULTRA INSTINCT AGENT | Model: OpenRouter LLM", style="cyan")
    return Panel(header_text, border_style="bright_blue")

def get_execution_matrix(tasks=None):
    table = Table(title="🧠 AI EXECUTION MATRIX", border_style="magenta", expand=True)
    table.add_column("TYPE", style="yellow")
    table.add_column("TARGET", style="green")
    table.add_column("DESCRIPTION", style="white")
    
    if tasks:
        for task in tasks:
            table.add_row(task.get('type', ''), task.get('target', ''), task.get('desc', ''))
    else:
        table.add_row("FILE", "app.py", "Main application entry point")
        table.add_row("FILE", "README.md", "Project documentation")
        table.add_row("COMMAND", "pip install -r requirements.txt", "Install dependencies")
    
    return table

def get_system_status(status_info=None):
    if not status_info:
        status_info = {
            "NEURAL LINK": "ESTABLISHED",
            "MODEL": "anthropic/claude-3.5-sonnet",
            "MEMORY": "🧠 ..shivam_memory.json",
            "MODE": "ULTRA INSTINCT",
            "STATUS": "READY FOR AUTONOMOUS EXECUTION"
        }
    
    status_text = Text()
    for key, value in status_info.items():
        status_text.append(f"{key:15}: ", style="bold cyan")
        status_text.append(f"{value}\n", style="bright_green")
        
    return Panel(status_text, title="💙 SYSTEM STATUS", border_style="blue")

def get_ultra_instinct_stats():
    stats = [
        ("CREATIVITY", 100, "blue"),
        ("LOGIC", 100, "magenta"),
        ("SPEED", 100, "red"),
        ("ACCURACY", 100, "green"),
        ("AUTONOMY", 100, "orange3")
    ]
    
    stat_panels = []
    for name, value, color in stats:
        bar = "█" * (value // 10) + "░" * (10 - value // 10)
        stat_panels.append(Text(f"{name:12} {bar} {value}%", style=color))
    
    return Panel("\n".join([str(p) for p in stat_panels]), title="ULTRA INSTINCT", border_style="magenta")

def get_command_center():
    commands = [
        ("/goal <idea>", "Autonomous build mode"),
        ("/chat", "Continue conversation"),
        ("/status", "Check system status"),
        ("/memory", "View memory context"),
        ("/clear", "Clear conversation"),
        ("/exit", "Exit Shivam CLI")
    ]
    
    cmd_text = Text()
    for cmd, desc in commands:
        cmd_text.append(f"{cmd:15}\n", style="bold cyan")
        cmd_text.append(f"{desc}\n", style="white")
        
    return Panel(cmd_text, title=">_ COMMAND CENTER", border_style="bright_blue")

def create_layout():
    layout = Layout()
    layout.split(
        Layout(name="header", size=10),
        Layout(name="body")
    )
    layout["body"].split_row(
        Layout(name="left"),
        Layout(name="right", size=40)
    )
    layout["left"].split_column(
        Layout(name="matrix", size=12),
        Layout(name="status_row")
    )
    layout["status_row"].split_row(
        Layout(name="status"),
        Layout(name="stats")
    )
    
    layout["header"].update(get_header())
    layout["matrix"].update(get_execution_matrix())
    layout["status"].update(get_system_status())
    layout["stats"].update(get_ultra_instinct_stats())
    layout["right"].update(get_command_center())
    
    return layout

if __name__ == "__main__":
    from rich.console import Console
    console = Console()
    console.print(create_layout())
