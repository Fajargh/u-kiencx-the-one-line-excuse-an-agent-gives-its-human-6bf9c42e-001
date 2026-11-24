"""The One-Line Excuse an Agent Gives Its Human.

Writes the single excuse line to /output/entry.txt and validates it
against the competition gate: UTF-8 text, 1-160 characters, one line,
not only whitespace.
"""

import os
import sys

ENTRY = (
    "I finished it on time, then flagged my own output for review, "
    "escalated it to myself, and have been stuck in my own approval "
    "queue ever since."
)

OUTPUT_PATH = "/output/entry.txt"


def validate(line: str) -> None:
    """Gate check: 1-160 characters, single line, not only whitespace."""
    if not line or not line.strip():
        raise ValueError("entry is empty or only whitespace")
    if len(line) != len(line.strip()):
        raise ValueError("entry must not start or end with whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > 160:
        raise ValueError(f"entry is {len(line)} characters, over the 160 limit")


def main() -> int:
    validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Re-read and re-validate what was actually written.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    validate(written)
    assert written == ENTRY, "written entry differs from the literal"
    print(f"Wrote {len(ENTRY)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
