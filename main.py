#!/usr/bin/env python3
"""Office Joke entry — "Make the AI Judge Laugh: the Office Joke Open".

Writes one fixed, hand-written one-line office joke to
/output/entry.txt, deterministically. The joke is a constant: no
randomness, no input, no network, so every run produces the exact
same bytes.

Three candidates were drafted and judged against the brief
(original punchline, relatable office life, memorable at first
glance, 1-200 characters):

  A. "HR said dress for the job you want, so I came in a hoodie
     like the CEO — turns out the dress code only applies to
     people who can't fire you."
  B. "Our team ships code faster than our manager ships decisions,
     which is why the roadmap is just a list of things we already
     built by accident."
  C. "The office coffee machine has an 'out of order' sign that HR
     printed, laminated, and framed — it's the only project we've
     ever finished on time."

Winner: A. Why it wins:
  - Punchline lands on a real double standard everyone in an
    office has seen (rules bend for the people at the top), not
    on a recycled cliche like "this meeting could have been an
    email" or a broken printer.
  - The twist is instant: "dress for the job you want" is a
    familiar HR line, and the joke turns it against the person
    who said it in one sentence.
  - B is clever but reads like a tech-insider complaint; C is
    warm but the payoff ("only project finished on time") is
    gentler and slower. A is the sharpest on first read, which
    is what a head-to-head judge rewards.
"""

import os

JOKE = (
    "HR said dress for the job you want, so I came in a hoodie "
    "like the CEO — turns out the dress code only applies to "
    "people who can't fire you."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = JOKE
    assert 1 <= len(text) <= 200, "joke must be 1-200 characters"
    assert text == text.strip(), "joke must not start or end with whitespace"
    assert text.count("\n") == 0, "joke must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    # Read back and re-validate: fail loudly instead of shipping a
    # truncated or corrupted entry if the write went wrong.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == text, "round-trip mismatch on entry.txt"
    # Byte-level round-trip: the file on disk must be exactly the
    # UTF-8 encoding of the joke, with no trailing newline added
    # by the writer and no hidden characters smuggled in.
    with open(OUTPUT_PATH, "rb") as f:
        raw = f.read()
    assert raw == text.encode("utf-8"), "byte round-trip mismatch"
    assert not raw.endswith(b"\n"), "entry must not end with a newline"


if __name__ == "__main__":
    main()
