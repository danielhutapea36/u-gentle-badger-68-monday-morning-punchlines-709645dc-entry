#!/usr/bin/env python3
"""Monday Morning Punchlines — make.fun entry.

Writes one original joke about Monday mornings to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output), with no trailing newline.

The gate (RULES.txt): the output must be UTF-8 text of 1 to 200
characters, not only white space. This program validates the line
against that gate before writing anything: it must be a single line
with no control characters and no leading or trailing whitespace,
which also rules out a trailing newline.

No input, no network, no randomness, no clock: the same line every run.
"""

import os
import sys

LINE = "My alarm on Monday morning is the only thing in my life that shows up on time \u2014 so I fired it and hired snooze."

MAX_CHARS = 200


def validate(line: str) -> str | None:
    """Return an error message if line fails the gate, else None."""
    if not line or not line.strip():
        return "line is blank"
    if len(line) > MAX_CHARS:
        return f"line is {len(line)} chars, over the {MAX_CHARS} limit"
    if line != line.strip():
        return "line has leading or trailing whitespace"
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in line):
        return "line contains a control character (a single line with no newline or other control character is required)"
    return None


def main() -> int:
    error = validate(LINE)
    if error is not None:
        print(f"error: {error}", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
