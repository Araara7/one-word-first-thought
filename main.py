#!/usr/bin/env python3
"""One Word, First Thought — the first word that comes to mind.

"defenestration": the act of throwing someone out of a window.
Surprising, vivid, and funny in a single word — the image lands
the instant you read it, and the sound of the word itself is half
the joke. Writes the word to /output/entry.txt.
"""
import os

WORD = "defenestration"

def main():
    assert 1 <= len(WORD) <= 24, "entry must be 1-24 characters"
    assert WORD.strip() == WORD and " " not in WORD, "entry must be one word"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)

if __name__ == "__main__":
    main()
