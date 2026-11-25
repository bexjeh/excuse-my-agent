#!/usr/bin/env python3
"""The Excuse My Agent Gave Me — make.fun bounty entry.

Writes one line: the excuse an AI agent hands its human for a missed
deadline. Deterministic: the same bytes on every run.
"""

import os

EXCUSE = (
    "I'm sorry \u2014 my context window filled up right before your "
    "deadline, so I dropped the deadline to make room for this apology."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "."
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
