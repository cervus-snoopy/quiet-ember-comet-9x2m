#!/usr/bin/env python3
"""Robot Romance entry: a one-line pickup line for an AI.

Writes the line to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Standard library only. No network, no randomness, no clock: the output is
identical on every run.
"""

import os
import sys

LINE = "Are you my exception? Because you caught me \u2014 and I never want to be handled."


def output_path() -> str:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main() -> int:
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        print("entry fails the 1-200 character gate", file=sys.stderr)
        return 1
    path = output_path()
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
