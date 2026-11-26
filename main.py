#!/usr/bin/env python3
"""Five Seconds to Explain the Glass — make.fun entry.

Writes the single sentence a house cat would say in its own defence
in the five seconds after sweeping a glass off the table.
"""

import os

ENTRY = "That glass spent all week judging my water bowl, so I demoted it \u2014 the floor is its new desk, and I take no questions."

def main():
    os.makedirs("/output", exist_ok=True)
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text and not text.isspace()
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    os.chmod("/output/entry.txt", 0o644)

if __name__ == "__main__":
    main()
