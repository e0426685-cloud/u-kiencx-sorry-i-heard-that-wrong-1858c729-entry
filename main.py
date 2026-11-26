"""One-line entry program for the make.fun bounty "sorry I heard that wrong".

Running this script produces the competition entry: a joke apology from a
voice assistant that misheard a request for chill music as an order for a
chinchilla. It saves that single line of text to entry.txt (and to
/output/entry.txt when that directory exists), ready for submission.
Only the Python standard library is used.
"""

import os

ENTRY = "Sorry, I heard 'play something chill' as 'buy a chinchilla,' so one is en route. Order cancelled — your playlist is ready."

MAX_CHARS = 140


def main():
    line = ENTRY.strip()
    if not line:
        raise ValueError("entry text must not be empty")
    if "\n" in line:
        raise ValueError("entry must fit on a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry is {len(line)} chars, over the {MAX_CHARS} limit")
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    os.chmod("/output/entry.txt", 0o644)
    with open("entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    os.chmod("entry.txt", 0o644)


if __name__ == "__main__":
    main()
