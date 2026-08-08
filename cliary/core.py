from pathlib import Path
from datetime import datetime, timedelta

LOG_DIR = Path.home() / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)


def get_date(day_offset):
    return (datetime.now() + timedelta(days=day_offset)).strftime("%Y-%m-%d")

def get_date_file(day_offset):
    return LOG_DIR / f"{get_date(day_offset)}.txt"

def get_display_date(day_offset):
    if day_offset == 0:
        return "today"
    elif day_offset == -1:
        return "yesterday"
    return get_date(day_offset)

def write_note(day_offset=0):
    file = get_date_file(day_offset)

    prev_note = ''
    while True:
        note = input(">> ")
        if (note.strip().lower() == 'exit') or (note == prev_note and note == ''): 
            print("Saved. Exiting...")
            break
        with open(file, "a") as f:
            f.write(note + "\n")
        prev_note = note


def read_notes(day_offset=0, display_fn=print):
    file = get_date_file(day_offset)
    if not file.exists(): 
        display_fn('No notes for this date.\n')
        return

    with open(file) as f:
        for line in f: display_fn(line)

def search_notes(keyword):
    found = False
    for file in LOG_DIR.glob("*.txt"):
        with open(file) as f:
            for line in f:
                if keyword.lower() in line.lower():
                    print(f"{file.name}: {line.strip()}")
                    found = True

    if not found:
        print(f'No notes found containing "{keyword}".')
