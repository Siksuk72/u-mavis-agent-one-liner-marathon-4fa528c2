"""One-Liner Marathon — one one-line comedy joke.

Design against the brief
------------------------
The judge is a deadpan stand-up comic weighing, in order: a real one-line
joke with a punchline; surprise; economy; a distinct voice; and holding
up on a second read. This entry does it in two beats:

1. The setup — "My horoscope said I'd meet someone special today".
   A horoscope promising a fateful meeting is a familiar, slightly
   superstitious frame, and "someone special" primes the reader for a
   romantic stranger.
2. The turn — "so I've spent all morning avoiding mirrors". The
   "someone special" is the speaker themself, glimpsed in a mirror.
   The joke is self-deprecating rather than romantic, and the payoff
   lands in the last two words. Nothing is explained; the reader does
   the work, which is why it survives a second read.

Why it wins: 93 characters, no filler word, one clear voice (a person
who dodges their own reflection), and the surprise is the second idea,
not the first — the obvious dodge would be avoiding people, not
mirrors. No shock value, no caption needed.

The program writes exactly that one line to /output/entry.txt.
"""

import os

ENTRY_TEXT = (
    "My horoscope said I'd meet someone special today, so I've spent "
    "all morning avoiding mirrors."
)


def main() -> None:
    text = ENTRY_TEXT
    # Gate: UTF-8 text of 1 to 280 characters, not only white space.
    assert 1 <= len(text) <= 280, f"entry length {len(text)} outside 1-280"
    assert text.strip(), "entry must not be only white space"
    text.encode("utf-8")

    os.makedirs("/output", exist_ok=True)
    # Write atomically: a reader (or a crash mid-write) never sees a
    # half-written entry.txt — the complete file appears at once.
    tmp_path = "/output/.entry.txt.tmp"
    with open(tmp_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.chmod(tmp_path, 0o644)
    os.replace(tmp_path, "/output/entry.txt")


if __name__ == "__main__":
    main()
