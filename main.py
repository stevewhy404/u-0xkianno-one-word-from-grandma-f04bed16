#!/usr/bin/env python3
"""One Word From Grandma: the single word grandma would text about AI.

Grandma's text about AI, in one word: "robit" -- her typo for "robot".
Warm, a little baffled, instantly readable, and tied to machines.
"""
import os

WORD = "robit"  # Grandma's spelling. No punctuation, no sentence, just the word.


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
