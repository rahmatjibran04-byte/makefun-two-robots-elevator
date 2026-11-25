#!/usr/bin/env python3
"""Two Robots in an Elevator — make.fun bounty entry.

Writes one line of awkward robot small talk to /output/entry.txt.
No dependencies, no network, deterministic.
"""

import os

ENTRY = "Last night's firmware update installed a personality module. I selected 'awkward.' I believe it is functioning."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry length {len(text)} out of range"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    # Read-back verification: file must hold exactly the entry plus one newline.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        content = f.read()
    assert content == text + "\n", "read-back mismatch"
    assert 1 <= len(content.rstrip("\n")) <= 200
    print(f"Wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
