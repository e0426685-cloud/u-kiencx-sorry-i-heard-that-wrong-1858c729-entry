"""Entry for make.fun bounty u-kiencx-sorry-i-heard-that-wrong-1858c729.

Writes a single-line apology from a smart speaker that misheard its owner
to /output/entry.txt (and ./entry.txt). Python stdlib only.
"""

import os

ENTRY = "Sorry, I heard 'play something chill' as 'buy a chinchilla,' so one is en route. Order cancelled — your playlist is ready."


def main():
    line = ENTRY.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 140, f"entry length {len(line)} out of range"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    os.chmod("/output/entry.txt", 0o644)
    with open("entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    os.chmod("entry.txt", 0o644)


if __name__ == "__main__":
    main()
