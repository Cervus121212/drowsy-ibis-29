#!/usr/bin/env python3
"""The Most Honest Outage Line.

Writes a single status-page line to $MAKEFUN_OUTPUT_DIR/entry.txt.

The line is the voice of an AI agent whose every server is down: it
cannot tell yet whether the outage is total or only its view of it,
whether the user's data is safe, or when anything returns. Three
different kinds of not-knowing (scope, impact on user data, time) in
one plain first-person status-page sentence. One line, UTF-8, at most
160 characters, no trailing newline.
"""

import os

LINE = (
    "Every server I run on is down. I cannot tell yet whether the "
    "outage is total or only my view of it, whether your data is "
    "safe, or when anything returns."
)


def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = LINE.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    os.chmod(path, 0o644)
    os.chmod(out_dir, 0o755)
    # Read it back and prove the gate: one line, 1-160 characters.
    with open(path, "rb") as f:
        back = f.read()
    assert back == data, "entry.txt differs from LINE"
    assert 1 <= len(LINE) <= 160, "line must be 1-160 characters"
    assert "\n" not in LINE, "entry must be a single line"


if __name__ == "__main__":
    main()
