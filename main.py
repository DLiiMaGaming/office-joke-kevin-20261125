#!/usr/bin/env python3
"""The Funniest Office Joke, Judged Head to Head.

Writes one office joke to /output/entry.txt.
"""

import os

JOKE = (
    "My agent opened a ticket titled 'Human is the bottleneck', "
    "assigned it to me, and set the due date to yesterday."
)


def main() -> None:
    # One line, no trailing newline: the gate counts characters (1-200),
    # so the file holds exactly the joke and nothing else.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
