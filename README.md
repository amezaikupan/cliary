# cliary

![Python](https://img.shields.io/badge/python-3.12-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Type](https://img.shields.io/badge/type-CLI-lightgrey)

A minimal command-line journal for writing, reading, and searching notes.

Notes are automatically grouped by day — each day gets its own file.

---

## Installation

```id="z9r3xk"
uv tool install cliary
```

Or you can also install locally with `pip`

```
pip install -e cliary
```
---

## Quick Example

1. You can write about **today**
```id="f2v6ny"
$ cliary write
>> today I learned about pathlib
>> built my first CLI tool
>> exit
Saved. Exiting...
```

and read what you have written about **today**
```id="3r5yhl"
$ cliary read

today I learned about pathlib
built my first CLI tool
```

2. You can also write and search about **yesterday** (-1 from today)
```id="f2v6ny"
$ cliary write -1
>> yesterday I install Linux
>> and learn about vim
>> exit
Saved. Exiting...
```

```id="3r5yhl"
$ cliary read -1

yesterday I install Linux
and learn about vim
```

and you can also do that with **tomorrow** (1 from today).

3. You can exact search 
```id="6x8pqm"
$ cliary search good

2026-04-23.txt: weather is good today

```

---

## Usage

Write notes:

```id="h1k9vb"
cliary write
```
**Note**: You can exit writing by writing 'exit' or tapping 2 times. 

Read today’s notes:

```id="q7n2dj"
cliary read
```

Search notes:

```id="m4w8rs"
cliary search <keyword>
```

---

## Storage

Notes are stored in a `logs/` directory in the home directory.   

Example:

```id="b2k6lm"
/home/me/
 ├── logs/
 │    ├── 2026-04-23.txt
```

Each day creates a new file.

---

## Requirements

* Python 3.8+

---

## License

MIT

