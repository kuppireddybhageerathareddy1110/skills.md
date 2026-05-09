#!/usr/bin/env python3
"""Validate Apex prompt templates contain all required fields."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


REQUIRED_FIELDS = [
    "Role",
    "Context",
    "Task",
    "Constraints",
    "Process Hints",
    "Output Format",
    "Quality Checks",
]


def validate(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    missing = []
    for field in REQUIRED_FIELDS:
        if f"## {field}" not in text and f"# {field}" not in text:
            missing.append(field)
    return missing


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Apex prompt template fields.")
    parser.add_argument("template", type=Path, help="Path to a prompt template markdown file.")
    args = parser.parse_args()

    if not args.template.exists():
        print(f"missing file: {args.template}", file=sys.stderr)
        return 2

    missing = validate(args.template)
    if missing:
        print("missing fields:")
        for field in missing:
            print(f"- {field}")
        return 1

    print("ok: all 7 prompt fields present")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
