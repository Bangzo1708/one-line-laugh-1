"""One Line, One Laugh -- entry program.

Writes a single funny line to /output/entry.txt (or $ENTRY_OUTPUT).

Three hand-written candidate jokes are scored 0-5 on each judge
criterion, in the judge's own order of importance:

  1. it is a funny one-line joke
  2. the laugh comes from the line itself (a turn / surprise / one exact word)
  3. it is one short line, readable in a single breath
  4. the wording is fresh, in plain words that sound like a person talking
  5. it lands on a single read, with no footnote, context or shared knowledge

The winner is chosen deterministically: highest total score, ties broken
by the criteria in order (criterion 1 first, then 2, and so on), then by
shorter text. No randomness, no clock, no network, no file reads.

As scored here the winner is the self-help book line: total 24, ahead of
the houseplants line on 21 and the gym line on 19, and it also leads on
the first criterion, so no tie-break is even needed.
"""

import os

# Each candidate: the joke line, its score per judge criterion (in order),
# and a short reason per criterion.
CANDIDATES = [
    {
        "text": "I bought a self-help book, but it keeps asking me for advice.",
        "scores": [5, 5, 5, 4, 5],
        "reasons": [
            "a real joke with a clear punchline, not a stray thought",
            "the twist lands on one exact word: the book needs the advice",
            "one short sentence, read in a single breath",
            "fresh angle on self-help books, plain everyday words",
            "needs nothing explained; the reversal is instant",
        ],
    },
    {
        "text": "My houseplants formed a union and their first demand was sunlight, not apologies.",
        "scores": [4, 4, 4, 4, 5],
        "reasons": [
            "a joke with a punchline, though the setup takes a beat longer",
            "the surprise is the union's demand, but 'union' does some of the work",
            "one line, still short, but a touch longer to say aloud",
            "plants forming a union is an unusual image in plain words",
            "lands on one read; houseplants and apologies need no context",
        ],
    },
    {
        "text": "I joined a gym to get fit, so now the treadmill and I just wave at each other.",
        "scores": [4, 3, 4, 3, 5],
        "reasons": [
            "a joke, though gentler: recognition more than a laugh",
            "the wave is a small turn, not a sharp surprise",
            "one line and short enough to read in a breath",
            "gym-avoidance jokes are well-worn; the wave saves it a little",
            "instantly clear, no context needed",
        ],
    },
]


def pick_winner(candidates):
    """Deterministic pick: highest total, ties broken by criteria in order,
    then by shorter text."""
    def key(candidate):
        scores = candidate["scores"]
        return (sum(scores), tuple(scores), -len(candidate["text"]))

    return max(candidates, key=key)


def main():
    winner = pick_winner(CANDIDATES)
    line = winner["text"]

    # The gate: UTF-8 text, 1-140 characters, not only whitespace,
    # a single line, no leading or trailing whitespace.
    assert isinstance(line, str)
    assert 1 <= len(line) <= 140, "line must be 1-140 characters"
    assert line.strip() == line, "line must have no leading/trailing space"
    assert line.strip() != "", "line must not be only whitespace"
    assert "\n" not in line and "\r" not in line, "line must be a single line"
    line.encode("utf-8")  # must be valid UTF-8 text

    out_path = os.environ.get("ENTRY_OUTPUT") or "/output/entry.txt"
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
