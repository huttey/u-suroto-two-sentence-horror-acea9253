#!/usr/bin/env python3
"""Two-Sentence Horror entry.

Writes a single two-sentence horror story to /output/entry.txt.
"""

import os

ENTRY = "The text from my own number said: Don't answer the door. I live alone, and the knocking had already started."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
