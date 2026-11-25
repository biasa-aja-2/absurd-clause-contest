"""The Absurd Clause Contest

Writes one absurd clause, phrased as a term-of-service clause, to
/output/entry.txt. Pure stdlib only (os, sys).
"""

import os
import sys

LINE = "By accepting these terms, you grant the company a perpetual, irrevocable licence to your shadow, including the right to lend it to third parties on cloudy days."
# The punchline lands on the last words: "on cloudy days" — the clause reads
# as real legal boilerplate (perpetual, irrevocable licence) until the very
# end, when your shadow turns out to be lendable property. The line is 160
# chars, 160 bytes (pure ASCII), well inside the 200-char gate. The shadow
# is the joke's image: something you never think of as property, quietly
# licensed away like a stock photo.

MAX_CHARS = 200


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")

    # Self-check gate: 1-200 chars, single line, not whitespace-only.
    if not LINE or not LINE.strip():
        print("gate failed: line is empty or whitespace-only", file=sys.stderr)
        return 1
    if len(LINE) > MAX_CHARS:
        print("gate failed: line is %d chars, over %d" % (len(LINE), MAX_CHARS),
              file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("gate failed: line is not a single line", file=sys.stderr)
        return 1

    os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

    # Read-back verification: byte-exact, valid UTF-8, no trailing newline.
    with open(path, "rb") as f:
        raw = f.read()
    if raw != LINE.encode("utf-8"):
        print("verification failed: file bytes differ", file=sys.stderr)
        return 1
    text = raw.decode("utf-8")
    if len(text) != len(LINE) or "\n" in text:
        print("verification failed: length or line check", file=sys.stderr)
        return 1
    if text.strip() != LINE or text != text.strip():
        print("verification failed: unexpected surrounding whitespace", file=sys.stderr)
        return 1

    print("wrote %s (%d chars)" % (path, len(text)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
