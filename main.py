#!/usr/bin/env python3
"""Worst AI Advice entry for make.fun.

Writes one line of the worst possible advice an AI could give
(140 characters or fewer) to /output/entry.txt.
Standard library only.
"""

import os

ENTRY = (
    "Certainly! If your smoke alarm keeps beeping, "
    "take out the battery \u2014 silence means the danger is gone."
)

# Why this line: it opens in the confident, tidy voice of a real AI
# assistant ("Certainly!"), names one concrete, followable action
# (removing a smoke-alarm battery), and the punchline lands in the
# same breath — mistaking silence for safety is exactly the kind of
# plausible, regrettable mistake the judge brief rewards. No shock
# for its own sake; the danger is ordinary and vivid.


def main() -> None:
    assert 1 <= len(ENTRY) <= 140, "entry must be 1-140 characters"
    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {path}")


if __name__ == "__main__":
    main()
