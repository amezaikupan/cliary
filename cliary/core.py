from pathlib import Path
from datetime import datetime, timedelta
from rich.console import Console 
import time

LOG_DIR = Path.home() / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)

console = Console()
    
def slow_print(text):
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(0.02)
    print()


def get_date(time_dis):
    if time_dis < 0:
        date = (datetime.now() - timedelta(days=abs(time_dis))).strftime("%Y-%m-%d")
    else:
        date = (datetime.now() + timedelta(days=abs(time_dis))).strftime("%Y-%m-%d")
    return date 


def get_date_file(time_dis):
    date = get_date(time_dis)
    return LOG_DIR / f"{date}.txt"


def write_note(time_dis=0):
    file = get_date_file(time_dis)

    console.print("[bold green]Write your thought:[/bold green]")
    prev_note = ''
    while True:
        note = input(">> ")
        if (note.strip().lower() == 'exit') or (note == prev_note and note == ''): 
            print("Saved. Exiting...")
            break
        with open(file, "a") as f:
            f.write(note + "\n")
        prev_note = note


def read_notes(time_dis=0):
    if time_dis == 0:
        date = 'today'
    elif time_dis == -1:
        date = 'yesterday'
    else:
        date = get_date(time_dis)
    console.print(f"[bold yellow]Reading {date}:[/bold yellow]\n")

    file = get_date_file(time_dis)
    if not file.exists(): 
        slow_print('no notes today')
        return

    with open(file) as f:
        for line in f: slow_print(line)

def search_notes(keyword):
    found = False
    for file in LOG_DIR.glob("*.txt"):
        with open(file) as f:
            for line in f:
                if keyword.lower() in line.lower():
                    print(f"{file.name}: {line.strip()}")
                    found = True
    if found == False:
        console.print(f"Found no file contains [bold red]{keyword}[/bold red]")
