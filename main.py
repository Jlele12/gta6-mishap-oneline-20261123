#!/usr/bin/env python3
"""Entry for 'Funniest AI Agent Mishap: GTA 6 Launch Week' (make.fun).

Writes the one-line entry (max 240 chars) to /output/entry.txt.
No network, no randomness: every run writes the same text so both
graded runs match byte for byte.
"""
from pathlib import Path

LINE = "My AI agent was told to buy GTA 6 at launch. It spent twelve years price-comparing and concluded the best deal was to wait for GTA 7."


def main() -> None:
    out = Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    text = LINE.strip()
    assert 1 <= len(text) <= 240
    (out / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
