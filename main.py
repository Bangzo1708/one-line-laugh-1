#!/usr/bin/env python3
"""One Line, One Laugh -- entry program.

Writes a single funny line (<=200 chars, one line, no trailing newline)
to /output/entry.txt. Deterministic: the line is a fixed constant.

Three candidate variants considered (all original, none copied from RULES.txt):

  A. "I gave my houseplant a pep talk; it died anyway, but at least
     it died feeling supported."
     - Twist: a pep talk is supposed to save something, and the plant
       dies anyway; the consolation prize ("feeling supported") is
       absurdly useless. Laugh lands in the second clause, fast.
     - Fresh: plants-as-patients is familiar, but the "support"
       double meaning (emotional support vs. a plant support stake)
       is not a stock pun.

  B. "My smoke alarm only goes off when I cook -- its polite way of
     saying I'm banned from the kitchen."
     - Relatable and tight, but the punchline is predictable: the
       reader guesses "I'm a bad cook" halfway through. Weaker on
       criterion (3) freshness.

  C. "I told my GPS I needed space, so it recalculated and now it
     follows me everywhere out of spite."
     - Good double meaning on "space" and a snappy ending, but the
       "GPS with feelings" angle is a well-worn gag; the twist is
       telegraphed by the setup.

Selection: A wins. It is the funniest on first read (the dead-plant
punchline arrives as a surprise, not a payoff the reader saw coming),
the most original (the "support" wordplay is buried, not the joke
itself), and the most retellable: one sentence, one image, one twist.
Every word earns its place -- "pep talk", "died anyway", "feeling
supported" each carry the joke.
"""

import os
import sys

LINE = "I gave my houseplant a pep talk; it died anyway, but at least it died feeling supported."

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    # Gate self-check: 1-200 chars, not only whitespace, single line.
    if not (1 <= len(LINE) <= 200):
        print(f"line length {len(LINE)} out of gate range", file=sys.stderr)
        return 1
    if not LINE.strip():
        print("line is only whitespace", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("line must be a single line", file=sys.stderr)
        return 1

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # No trailing newline: write the exact bytes of the line only.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Round-trip check: what landed on disk must be byte-identical to
    # the chosen line, so a silent write failure can never pass.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        if f.read() != LINE:
            print("written file does not match the chosen line", file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
