#!/usr/bin/env python3
"""Rough overlap estimator for common academic phrasing.

This is not a plagiarism or detector substitute. It highlights repeated stock phrases
so writers can review originality, attribution, and sentence structure manually.
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path


COMMON_PHRASES = {
    "it is important to note",
    "in conclusion",
    "this study aims to",
    "the results show that",
    "furthermore",
    "moreover",
    "this suggests that",
    "there is a significant",
    "plays a crucial role",
    "in recent years",
    "a growing body of literature",
    "future research should",
}


def words(text: str) -> list[str]:
    return re.findall(r"[a-zA-Z][a-zA-Z'-]*", text.lower())


def ngrams(tokens: list[str], n: int) -> Counter[str]:
    return Counter(" ".join(tokens[i : i + n]) for i in range(max(0, len(tokens) - n + 1)))


def estimate(text: str, n: int) -> tuple[float, list[str]]:
    tokens = words(text)
    if len(tokens) < n:
        return 0.0, []

    grams = ngrams(tokens, n)
    repeated = [gram for gram, count in grams.items() if count > 1]
    phrase_hits = sorted(phrase for phrase in COMMON_PHRASES if phrase in text.lower())
    risk_score = min(1.0, (len(repeated) * 0.04) + (len(phrase_hits) * 0.08))
    return risk_score, phrase_hits + repeated[:20]


def label(score: float) -> str:
    if score >= 0.55:
        return "high"
    if score >= 0.25:
        return "medium"
    return "low"


def main() -> int:
    parser = argparse.ArgumentParser(description="Estimate stock-phrase overlap risk.")
    parser.add_argument("file", nargs="?", type=Path, help="Text file to inspect. Reads stdin if omitted.")
    parser.add_argument("--ngram", type=int, default=4, help="Repeated n-gram size. Default: 4.")
    args = parser.parse_args()

    text = args.file.read_text(encoding="utf-8") if args.file else sys.stdin.read()
    score, hits = estimate(text, args.ngram)

    print(f"risk: {label(score)} ({score:.2f})")
    if hits:
        print("review phrases:")
        for hit in hits:
            print(f"- {hit}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
