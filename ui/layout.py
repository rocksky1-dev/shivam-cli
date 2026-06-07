import os
from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.align import Align

console = Console()

def get_bot_face():
    # Cute AI Bot Face with gradients
    face = """
      .---.
     /     \\
    | (o)(o) |
    |   ▲   |
     \\  -  /
      '---'
    """
    bot = Text()
    bot.append("    ╭─────────────╮\n", style="bold magenta")
    bot.append("    │   ^ ___ ^   │\n", style="bold cyan")
    bot.append("    │  ( o   o )  │\n", style="bold cyan")
    bot.append("    │   (  -  )   │\n", style="bold cyan")
    bot.append("    ╰─────┬───────╯\n", style="bold magenta")
    bot.append("          ▼", style="bold magenta")
    return Align.center(bot)

def get_header():
    header = Text()
    header.append("🚀 SHIVAM CLI v2.0 - ULTRA INSTINCT\n", style="bold italic magenta")
    header.append("───────────────────────────────────\n", style="dim white")
    header.append("   [ ADVANCED AGENTIC IDE ]\n", style="bold white on blue")
    header.append("   Made By Shivam Kumar 🇮🇳", style="italic cyan")
    return Panel(Align.center(header), border_style="bright_blue", padding=(1, 2))

def get_execution_plan(tasks=None):
    # Professional execution plan instead of matrix
    table = Table(box=None, expand=True)
    table.add_column("STATUS", style="bold yellow", width=12)
    table.add_column("ACTION", style="white")
    
    if tasks:
        for task in tasks:
            status = "✓ DONE" if task.get('done') else "● PENDING"
            table.add_row(status, task.get('desc', ''))
    else:
        table.add_row("● READY", "Waiting for your command...")
        table.add_row("● IDLE", "Systems at 100% capacity")
        
    return Panel(table, title="📋 EXECUTION PLAN", border_style="magenta")

def get_system_status(config=None):
    status_text = Text()
    status_text.append("🤖 AGENT   : ", style="bold cyan")
    status_text.append("ACTIVE\n", style="bright_green")
    status_text.append("🧠 MODEL   : ", style="bold cyan")
    status_text.append(f"{config.get('model', 'Claude-3.5') if config else 'AUTO'}\n", style="bright_magenta")
    status_text.append("🌐 NETWORK : ", style="bold cyan")
    status_text.append("SECURE\n", style="bright_blue")
    return Panel(status_text, title="💙 SYSTEM", border_style="blue")

def get_command_center():
    commands = [
        ("/goal", "Autonomous Build"),
        ("/chat", "AI Interaction"),
        ("/config", "API Settings"),
        ("/clear", "Reset Terminal"),
        ("/exit", "Shutdown")
    ]
    
    cmd_text = Text()
    for cmd, desc in commands:
        cmd_text.append(f"{cmd:8}", style="bold cyan")
        cmd_text.append(f" {desc}\n", style="dim white")
        
    return Panel(cmd_text, title="🎮 COMMANDS", border_style="bright_blue")

def create_layout(tasks=None, config=None):
    width = console.width
    layout = Layout()
    
    if width < 60:
        layout.split_column(
            Layout(name="bot", size=8),
            Layout(name="header", size=8),
            Layout(name="body")
        )
        layout["body"].split_column(
            Layout(name="plan", size=10),
            Layout(name="footer", size=8)
        )
        layout["footer"].split_row(
            Layout(name="status"),
            Layout(name="right")
        )
    else:
        layout.split_column(
            Layout(name="top", size=10),
            Layout(name="body")
        )
        layout["top"].split_row(
            Layout(name="bot", size=25),
            Layout(name="header")
        )
        layout["body"].split_row(
            Layout(name="left", ratio=2),
            Layout(name="right", size=30)
        )
        layout["left"].split_column(
            Layout(name="plan", size=12),
            Layout(name="status", size=8)
        )
    
    layout["bot"].update(get_bot_face())
    layout["header"].update(get_header())
    layout["plan"].update(get_execution_plan(tasks))
    layout["status"].update(get_system_status(config))
    layout["right"].update(get_command_center())
    
    return layout

if __name__ == "__main__":
    console.print(create_layout())
