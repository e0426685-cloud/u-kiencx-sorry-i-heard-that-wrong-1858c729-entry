"""One-line entry program for the make.fun bounty "sorry I heard that wrong".

Running this script produces the competition entry: a joke apology from a
voice assistant that misheard a request for chill music as an order for a
chinchilla. It saves that single line of text to entry.txt in the grader
output directory only (MAKEFUN_OUTPUT_DIR when set, otherwise /output),
creating that directory if needed. The repository directory is never
written to, so the program also runs when the repo is mounted read-only.
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
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    out_path = os.path.join(output_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line)
    os.chmod(out_path, 0o644)


if __name__ == "__main__":
    main()
