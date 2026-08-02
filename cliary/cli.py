import argparse
from cliary.core import write_note, read_notes, search_notes

def main():
    parser = argparse.ArgumentParser(prog="cliary", description="cliary is a simple command line diary for your daily use!")
    parser.add_argument("command", nargs="?", help="write | read | search")
    parser.add_argument("arg", nargs="?", help="Write and Read: Relative time | Search: terms")
    args = parser.parse_args()
        
    match args.command:
        case "write": 
            try:
                # Long and quite ugly line of code
                time_dis = int(args.arg) if args.arg != None else 0
            except ValueError:
                print("[bold red] Error: argument must be an integer:[/bold red]")

            write_note(time_dis)

        case "read": 
            try:
                # Long and quite ugly line of code
                time_dis = int(args.arg) if args.arg != None else 0
            except ValueError:
                print("[bold red] Error: argument must be an integer:[/bold red]")

            read_notes(time_dis)

        case "search": 
            search_notes(args.arg) if args.arg else print('Please provide a keyword')
