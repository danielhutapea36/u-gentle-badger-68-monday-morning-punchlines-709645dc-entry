#!/usr/bin/env python3
"""Monday Morning Punchlines — make.fun entry.

Writes one original joke about Monday mornings to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output), with no trailing newline.

The gate (RULES.txt): the output must be UTF-8 text of 1 to 200
characters, not only white space. This program validates the line
against that gate before writing anything.

No input, no network, no randomness, no clock: the same line every run.
"""

import os
import sys

LINE = "My alarm on Monday morning is the only thing in my life that shows up on time \u2014 so I fired it and hired snooze."

MAX_CHARS = 200


def main() -> int:
    line = LINE
    if not line or not line.strip():
        print("error: line is blank", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print(f"error: line is {len(line)} chars, over the {MAX_CHARS} limit",
              file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: line must be a single line", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
