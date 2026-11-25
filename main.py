#!/usr/bin/env python3
"""Write one original roast of a smart fridge to /output/entry.txt.

Deterministic: the same bytes on every run, from any working directory.
Standard library only; no network, no input files.
"""

from pathlib import Path

LINE = (
    "My smart fridge's firmware update locked the ice maker behind new "
    "terms \u2014 I traded my grocery data for a cold drink."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    text = LINE.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(f"line is {len(text)} chars, must be 1-200")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
