import argparse
import time
from cliary.core import write_note, read_notes, search_notes
from rich.console import Console
from rich.panel import Panel


console = Console()



def slow_print(text):
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(0.02)
    print()


def main():
    console.print(Panel("cliary ✍️\na quiet place for your thoughts", style="cyan"))
    parser = argparse.ArgumentParser(prog="cliary")
    parser.add_argument(
    "command",
    choices=["write", "read", "search"]
    )
    parser.add_argument("arg", nargs="?")
    args = parser.parse_args()

        
    match args.command:
        case "write": 
            console.print("[bold green]Write your thought:[/bold green]")
            write_note()
        case "read": 
            console.print("[bold yellow]Reading...[/bold yellow]\n")
            read_notes(slow_print)
        case "search": 
            search_notes(args.arg) if args.arg else print('Please provide a keyword')
