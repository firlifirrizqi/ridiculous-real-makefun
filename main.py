#!/usr/bin/env python3
"""Ridiculous at First Glance entry: writes one bizarre-but-real pitch to /output/entry.txt."""

LINE = "We rent trained goats to offices to eat their confidential documents, because a goat never leaks, never unionizes, and works for hay."

# The gate: /output/entry.txt must hold 1 to 200 characters of real text,
# as one single sentence (the brief asks for one sentence, not a paragraph).
assert 1 <= len(LINE) <= 200 and LINE.strip(), "line must be 1-200 characters"
assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
assert LINE.rstrip().endswith("."), "line must be one complete sentence"

if __name__ == "__main__":
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
