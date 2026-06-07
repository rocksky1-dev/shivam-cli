import os
from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.align import Align

console = Console()

def get_bot_face():
    # Ultra-compact cute bot for mobile/PC
    bot = Text()
    bot.append("  ^___^\n", style="bold cyan")
    bot.append(" ( o o )\n", style="bold cyan")
    bot.append("  ( - )\n", style="bold cyan")
    bot.append("   -v-", style="bold magenta")
    return Align.center(bot)

def get_header():
    header = Text()
    header.append("⚡ SHIVAM CLI\n", style="bold magenta")
    header.append("─────────────────\n", style="dim white")
    header.append("Made By Shivam Kumar", style="italic cyan")
    return Panel(Align.center(header), border_style="bright_blue", padding=(0, 1))

def get_execution_plan(tasks=None):
    table = Table(box=None, expand=True, padding=(0, 1))
    table.add_column("ST", style="bold yellow", width=3)
    table.add_column("ACTION", style="white")
    
    if tasks:
        for task in tasks:
            status = "✓" if task.get('done') else "○"
            table.add_row(status, task.get('desc', ''))
    else:
        table.add_row("○", "Ready...")
        
    return Panel(table, title="📋 PLAN", border_style="magenta")

def get_system_status(config=None):
    status_text = Text()
    status_text.append("🤖: ", style="bold cyan")
    status_text.append("ON\n", style="bright_green")
    status_text.append("🧠: ", style="bold cyan")
    status_text.append(f"{config.get('active_provider', 'AUTO')[:8]}\n", style="bright_magenta")
    return Panel(status_text, title="💙 SYS", border_style="blue")

def get_command_center():
    commands = [
        ("/goal", "Build"),
        ("/chat", "Talk"),
        ("/api", "Keys"),
        ("/logout", "Reset"),
        ("/exit", "Quit")
    ]
    
    cmd_text = Text()
    for cmd, desc in commands:
        cmd_text.append(f"{cmd:5} {desc}\n", style="bold cyan")
        
    return Panel(cmd_text, title="🎮 CMD", border_style="bright_blue")

def create_layout(tasks=None, config=None):
    width = console.width
    layout = Layout()
    
    if width < 50:
        # Ultra-mobile compact view - No Matrix
        layout.split_column(
            Layout(name="top", size=5),
            Layout(name="plan", ratio=1),
            Layout(name="bottom", size=6)
        )
        layout["top"].split_row(
            Layout(name="bot", size=10),
            Layout(name="header")
        )
        layout["bottom"].split_row(
            Layout(name="status"),
            Layout(name="right")
        )
    else:
        # Standard responsive view - Professional Flow
        layout.split_column(
            Layout(name="top", size=7),
            Layout(name="body")
        )
        layout["top"].split_row(
            Layout(name="bot", size=15),
            Layout(name="header")
        )
        layout["body"].split_row(
            Layout(name="left", ratio=2),
            Layout(name="right", size=25)
        )
        layout["left"].split_column(
            Layout(name="plan", ratio=1),
            Layout(name="status", size=4)
        )
    
    layout["bot"].update(get_bot_face())
    layout["header"].update(get_header())
    layout["plan"].update(get_execution_plan(tasks))
    layout["status"].update(get_system_status(config or {}))
    layout["right"].update(get_command_center())
    
    return layout

if __name__ == "__main__":
    console.print(create_layout())
