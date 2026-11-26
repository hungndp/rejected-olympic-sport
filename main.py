#!/usr/bin/env python3
"""Rejected Olympic Sports — one funny single-line sport the Olympics rejected.

The entry is a single line: a made-up event, real enough to sound like a
broadcast, absurd enough to be funny. Running this program writes the line
deterministically to /output/entry.txt (or $ENTRY_OUTPUT) and prints it.
"""

import os
import sys

# The setup: names the invented event and stages the incident. Broadcast-flat,
# no joke yet — the punch does all the work.
SETUP = "Competitive Fitted-Sheet Folding: athletes race to fold a fitted sheet neatly; "


def check_line(line):
    """The gate, in miniature: 1-200 chars, one line, nothing but the line."""
    if not isinstance(line, str):
        raise TypeError("entry must be text")
    if not 1 <= len(line) <= 200:
        raise ValueError("entry must be 1 to 200 characters, got %d" % len(line))
    if line != line.strip() or "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line with no surrounding space")
    return line

# The punch: one incident, twist word last, then stop. The first finisher is
# not celebrated — they are disqualified, for the one thing nobody can prove
# about a folded fitted sheet.
PUNCH = "the first to finish is disqualified for lying."


def build_line():
    """Join setup and punch, then enforce the gate before anything is written."""
    return check_line(SETUP + PUNCH)


def main():
    line = build_line()
    out = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(line)
    print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
