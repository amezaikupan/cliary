import argparse
from rich.console import Console
from rich.panel import Panel
from cliary.core import write_note, read_notes, search_notes, get_display_date
import time

console = Console()

    
def slow_print(text):
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(0.02)
    print()


def main():
    parser = argparse.ArgumentParser(prog="cliary", description="cliary is a simple command line diary for your daily use!")
    parser.add_argument("command", nargs="?", help="write | read | search")
    parser.add_argument("arg", nargs="?", help="Write and Read: Relative time | Search: terms")
    args = parser.parse_args()

    day_offset = 0

    if args.command in ("write", "read"):
        try:
            day_offset = int(args.arg) if args.arg is not None else 0
        except ValueError:
            console.print("[bold red]Error: argument must be an integer.[/bold red]")
            return 
        
    match args.command:
        case "write": 
            console.print("[bold green]Write your thought:[/bold green]")
            write_note(day_offset)
        case "read":
            console.print(f"[bold yellow]Reading {get_display_date(day_offset)}:[/bold yellow]\n")
            read_notes(day_offset, slow_print)
        case "search": 
            search_notes(args.arg) if args.arg else console.print('Please provide a keyword')
        case _:
            console.print(
                Panel(
                    "cliary ✍️\na quiet place for your thoughts",
                    style="cyan",
                )
            )
            parser.print_help()
