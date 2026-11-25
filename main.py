"""One Emoji, One Dream Vacation — entry program.

Writes a single emoji to ``entry.txt`` in the output directory: a surfer
riding a wave. One glyph, no words: a surf trip on a faraway shore, the
postcard a stranger reads at a glance and wants to book.

The output directory comes from MAKEFUN_OUTPUT_DIR when the harness sets it
(local test: ``mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py``),
and defaults to /output in the grader's sandbox. The write is fixed: no
clock, no randomness, no network, so two runs produce byte-identical
output. After writing, the program reads the file back and checks it holds
exactly one non-whitespace character, the sealed gate's own rule, so a
bad write fails loudly here instead of silently at grading time.
"""

import os
import sys

# U+1F3C4 PERSON SURFING — one code point, four UTF-8 bytes, well inside
# the gate's 1-to-8 characters. A surfer is the whole dream in one glyph:
# sun, sea, a faraway beach, and a trip you take for joy, not for work.
# It is specific (one particular dream: a surf trip) rather than any
# holiday, vivid at a glance, and it reads instantly at any size.
EMOJI = "\U0001F3C4"

OUTPUT_FILENAME = "entry.txt"


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, OUTPUT_FILENAME)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(EMOJI)
    with open(path, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if len(written) != 1 or written.isspace():
        raise SystemExit("entry.txt must hold exactly one non-whitespace character")
    print(written)
    return 0


if __name__ == "__main__":
    sys.exit(main())
