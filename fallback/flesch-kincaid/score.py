# /// script
# requires-python = ">=3.11"
# dependencies = ["textstat"]
# ///
"""Deterministically compute the Flesch Reading Ease score for a markdown file.

Usage:
    uv run score.py <path-to-markdown-file>

Strips markdown markup (fenced code, inline code, URLs, link syntax, headers,
blockquote markers, list markers, emphasis) before feeding the prose to
`textstat.flesch_reading_ease()`. Prints the score rounded to two decimals.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import textstat


def strip_markdown(text: str) -> str:
    """Remove markdown markup so only prose remains."""
    # Fenced code blocks
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    # Inline code
    text = re.sub(r"`[^`]*`", "", text)
    # URLs
    text = re.sub(r"https?://\S+", "", text)
    # Markdown links: keep link text, drop target
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    # Header markers
    text = re.sub(r"^#+\s*", "", text, flags=re.MULTILINE)
    # Blockquote markers
    text = re.sub(r"^>\s*", "", text, flags=re.MULTILINE)
    # Unordered list markers
    text = re.sub(r"^\s*[-*]\s+", "", text, flags=re.MULTILINE)
    # Ordered list markers
    text = re.sub(r"^\s*\d+\.\s+", "", text, flags=re.MULTILINE)
    # Emphasis (*, _, **, __, ***)
    text = re.sub(r"[*_]{1,3}([^*_]+)[*_]{1,3}", r"\1", text)
    return text


def die(msg: str) -> None:
    print(f"Error: {msg}", file=sys.stderr)
    sys.exit(1)


def main() -> None:
    if len(sys.argv) != 2:
        die("exactly one argument required (path to a .md file)")

    path = Path(sys.argv[1])
    if not path.exists():
        die(f"file not found: {path}")
    if path.suffix.lower() != ".md":
        die(f"not a markdown file: {path}")

    prose = strip_markdown(path.read_text())
    score = textstat.flesch_reading_ease(prose)
    print(f"{score:.2f}")


if __name__ == "__main__":
    main()
