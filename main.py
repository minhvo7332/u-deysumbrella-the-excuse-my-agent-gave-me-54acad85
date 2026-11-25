#!/usr/bin/env python3
"""Write the single funniest excuse line to /output/entry.txt.

Deterministic, no network, no model calls. The line is a constant:
an agent apologising for a missed deadline with the one resource
it actually ran out of -- its token budget -- and faintly proud
of the apology it spent it on. The hook is the budget itself:
"spent my entire token budget writing this apology" makes the
apology the thing the tokens were spent on, so the excuse and
the apology are the same act -- that is what carries the joke,
not the deadline, which is only the setup.
"""

import os

LINE = (
    "I missed the deadline because I spent my entire token budget "
    "writing this apology, and frankly, it was worth every token."
)


def main():
    assert 1 <= len(LINE) <= 200, "entry line must be 1-200 characters"
    assert LINE == LINE.strip(), "entry line must have no leading/trailing whitespace"
    assert "\n" not in LINE, "entry line must be exactly one line"
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
