import os
from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

console = Console()

def get_header():
    # More compact and professional header for mobile/desktop
    header_text = Text()
    header_text.append("⚡ SHIVAM CLI - ULTRA INSTINCT MODE\n", style="bold magenta italic")
    header_text.append("█▀ █░█ █ █░█ ▄▀█ █▀▄▀█   █▀▀ █░░ █\n", style="bold cyan")
    header_text.append("▄█ █▀█ █ ▀▄▀ █▀█ █░▀░█   █▄▄ █▄▄ █\n", style="bold cyan")
    header_text.append("\n[ AGENTIC IDE | MODEL: OPENROUTER ]", style="bold white on blue")
    return Panel(header_text, border_style="bright_blue", padding=(0, 1))

def get_execution_matrix(tasks=None):
    table = Table(border_style="magenta", expand=True, box=None)
    table.add_column("TYPE", style="yellow", width=8)
    table.add_column("TARGET", style="green")
    table.add_column("DESC", style="white")
    
    if tasks:
        for task in tasks:
            table.add_row(task.get('type', ''), task.get('target', ''), task.get('desc', ''))
    else:
        table.add_row("FILE", "app.py", "Main entry")
        table.add_row("CMD", "pip install", "Deps")
    
    return Panel(table, title="🧠 MATRIX", border_style="magenta")

def get_system_status():
    status_text = Text()
    status_text.append("LINK: ", style="bold cyan")
    status_text.append("OK\n", style="bright_green")
    status_text.append("MODE: ", style="bold cyan")
    status_text.append("ULTRA\n", style="bright_magenta")
    return Panel(status_text, title="💙 STATUS", border_style="blue")

def get_ultra_instinct_stats():
    # Simple bars for mobile
    stats = "CRTV: ████ 100%\nLOGC: ████ 100%"
    return Panel(stats, title="📊 STATS", border_style="magenta")

def get_command_center():
    commands = [
        ("/goal", "Build"),
        ("/chat", "Talk"),
        ("/status", "UI"),
        ("/clear", "Reset"),
        ("/exit", "Quit")
    ]
    
    cmd_text = Text()
    for cmd, desc in commands:
        cmd_text.append(f"{cmd:7} {desc}\n", style="bold cyan")
        
    return Panel(cmd_text, title=">_ CMD", border_style="bright_blue")

def create_layout():
    width = console.width
    layout = Layout()
    
    # Responsive layout based on terminal width
    if width < 60:
        # Mobile view: Stack everything vertically
        layout.split_column(
            Layout(name="header", size=7),
            Layout(name="body")
        )
        layout["body"].split_column(
            Layout(name="matrix", size=6),
            Layout(name="status_row", size=6),
            Layout(name="right", size=8)
        )
        layout["status_row"].split_row(
            Layout(name="status"),
            Layout(name="stats")
        )
    else:
        # Desktop view: Side-by-side
        layout.split_column(
            Layout(name="header", size=8),
            Layout(name="body")
        )
        layout["body"].split_row(
            Layout(name="left", ratio=2),
            Layout(name="right", size=30)
        )
        layout["left"].split_column(
            Layout(name="matrix", size=8),
            Layout(name="status_row", size=6)
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
    console.print(create_layout())
