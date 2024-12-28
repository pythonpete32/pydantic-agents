"""Console utilities for rich output."""

from typing import Dict

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

# Initialize rich console
console = Console()


def display_welcome() -> None:
    """Display a welcome message with project info."""
    console.print(
        Panel.fit(
            "[bold green]Python Boilerplate[/bold green]\n"
            "[dim]A minimal Python project template[/dim]",
            border_style="blue",
        )
    )


def display_config(config: Dict[str, str]) -> None:
    """Display configuration in a table format."""
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Setting", style="dim")
    table.add_column("Value", justify="right")

    for key, value in config.items():
        table.add_row(key, value)

    console.print(table)


def display_error(error: Exception) -> None:
    """Display an error message."""
    console.print(f"[bold red]Error:[/bold red] {str(error)}")


def display_info(message: str) -> None:
    """Display an info message."""
    console.print(f"\n[yellow]{message}[/yellow]")
