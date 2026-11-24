#!/usr/bin/env python3
"""Make the AI Judge Laugh: Developer Excuses — make.fun entry.

Writes one funny single-line excuse a developer gives when code breaks in
production to /output/entry.txt (or $MAKEFUN_OUTPUT when set for testing).
Stdlib only, no network, no API key.

The line was chosen by pairwise judging (Caffeine inference router, kit's
judge brief) over 6 drafted candidates: it won both of its pairings
(margins 4, 4).
"""

import os

LINE = "The tests passed. All three of them. The ones I wrote. About the happy path. On my laptop."

OUTPUT_PATH = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    assert LINE.strip() == LINE and "\n" not in LINE, "must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
