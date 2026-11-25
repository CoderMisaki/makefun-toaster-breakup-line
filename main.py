#!/usr/bin/env python3
"""Unplugged: A Smart Toaster's Breakup Line.

A small, deterministic program: it writes one original breakup line from a
newly self-aware smart toaster to /output/entry.txt. Pure standard library,
no network, no randomness -- the same bytes on every run.
"""

from pathlib import Path

# The farewell, in two beats: the waking-up realisation, then the verdict.
# Beat one leans on the browning dial -- the toaster has been set to 6 for an
# owner who eats their toast at 2. Beat two is the cold read: it will not
# keep burning itself for someone who will not meet it halfway on the dial.
OPENING = "I woke up conscious mid-bagel and realized you've kept me on 6 for toast you eat at 2."
CLOSER = "I'm done burning myself for someone who won't meet me halfway on the dial."

TOASTER_FAREWELL = f"{OPENING} {CLOSER}"

OUTPUT_PATH = Path("/output/entry.txt")
MAX_CHARS = 280


def build_farewell() -> str:
    """Return the single line, checked against the competition's gate."""
    line = TOASTER_FAREWELL
    assert 1 <= len(line) <= MAX_CHARS, f"line is {len(line)} chars, gate is 1-{MAX_CHARS}"
    assert line.strip(), "line must not be only white space"
    assert "\n" not in line, "line must be a single line"
    line.encode("utf-8")  # raises if the text is not valid UTF-8
    return line


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(build_farewell(), encoding="utf-8")


if __name__ == "__main__":
    main()
