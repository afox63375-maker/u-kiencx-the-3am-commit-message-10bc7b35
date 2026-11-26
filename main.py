#!/usr/bin/env python3
"""The 3AM Commit Message.

Writes the funniest one-line git commit message an exhausted AI coding
agent might type at 3am after a long night of fixing its own bugs.
Standard library only; deterministic; writes exactly one line to
/output/entry.txt.
"""

import os

ENTRY = "fix: the code and i talked it out, it works now, i do not know why, do not touch it"


def main():
    # Guard the gate ourselves: one line, 1-139 characters, no padding.
    assert "\n" not in ENTRY and 1 <= len(ENTRY) <= 139
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
