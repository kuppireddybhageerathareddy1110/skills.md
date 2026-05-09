#!/usr/bin/env python3
"""Demo caveman compressor. Keeps technical tokens, removes common filler."""

from __future__ import annotations

import argparse
import re
import sys


DROP_WORDS = {
    "a",
    "an",
    "the",
    "just",
    "really",
    "basically",
    "actually",
    "simply",
    "very",
    "quite",
    "rather",
    "please",
}

REPLACE = {
    "utilize": "use",
    "utilized": "used",
    "implement": "build",
    "implementation": "build",
    "leverage": "use",
    "approximately": "about",
    "subsequently": "then",
    "prior to": "before",
    "due to the fact that": "because",
    "in order to": "to",
    "demonstrate": "show",
    "facilitate": "help",
    "sufficient": "enough",
    "numerous": "many",
    "configuration": "config",
}


def compress(text: str, ultra: bool = False) -> str:
    lowered = text
    for src, dst in sorted(REPLACE.items(), key=lambda item: len(item[0]), reverse=True):
        lowered = re.sub(rf"(?<!\w){re.escape(src)}(?!\w)", dst, lowered, flags=re.IGNORECASE)

    tokens = re.findall(r"\w+|[^\w\s]", lowered, re.UNICODE)
    kept: list[str] = []
    for token in tokens:
        if token.lower() in DROP_WORDS:
            continue
        if ultra and token.lower() in {"and", "or", "that", "which", "with"}:
            continue
        kept.append(token)

    out = " ".join(kept)
    out = re.sub(r"\s+([.,:;!?])", r"\1", out)
    out = re.sub(r"\s+", " ", out).strip()
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description="Compress prose using simple caveman rules.")
    parser.add_argument("--ultra", action="store_true", help="Drop extra connector words.")
    parser.add_argument("text", nargs="*", help="Text to compress. Reads stdin if omitted.")
    args = parser.parse_args()

    source = " ".join(args.text) if args.text else sys.stdin.read()
    print(compress(source, ultra=args.ultra))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
