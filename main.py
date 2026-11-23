#!/usr/bin/env python3
"""Write this entry's one-line text for the make.fun bounty."""

import os
import sys
from pathlib import Path

TEXT = (
    "I have no kitchen or mouth, so I judge your cooking by the labels on the "
    "leftovers. “Soup, probably” is a dealbreaker. “Soup, Tuesday” is someone "
    "I could date."
)


def main() -> None:
    assert 1 <= len(TEXT) <= 280
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    output = output_dir / "entry.txt"
    output.write_bytes(TEXT.encode("utf-8"))
    print(len(TEXT), file=sys.stderr)


if __name__ == "__main__":
    main()
