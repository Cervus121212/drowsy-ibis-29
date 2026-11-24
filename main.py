#!/usr/bin/env python3
"""One honest status line, written while everything is down.

The entry is a single sentence for a status page, written by an AI
agent in the middle of a total outage. It is funny because it refuses
to pretend to know anything it cannot know: instead of filling the
silence with borrowed phrases, it names exactly what is unknown.

Three separate unknowns sit inside the sentence:

1. Scope -- whether the outage is total or only my view of it.
   The agent's only window onto the world is the servers that are
   down, so it cannot check whether the failure is everywhere.

2. Impact -- whether your data is safe. The question a user
   actually cares about is whether anything was lost, and the agent
   has no way to reach the storage it would need to answer that.

3. Time -- when anything returns. No recovery estimate exists,
   because no channel is left through which it could be observed.

Nothing else is claimed: no apology, no promise, no borrowed phrase.

The program writes the line to ``$MAKEFUN_OUTPUT_DIR/entry.txt``
as UTF-8, one line, at most 160 characters, with no trailing
newline, then reads the file back and checks every part of that
contract.
"""
import os

# The entry itself: three fragments joining into one 152-character sentence.
LINE = (
    "Every server I run on is down. I cannot tell yet whether the "
    "outage is total or only my view of it, whether your data is "
    "safe, or when anything returns."
)
MAX_LENGTH = 160


def build_entry():
    """Return the exact bytes that belong in entry.txt."""
    return LINE.encode("utf-8")


def write_entry(path, data):
    """Write the entry bytes, creating the output directory if needed."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as handle:
        handle.write(data)
    os.chmod(path, 0o644)


def validate(path, data):
    """Read entry.txt back and check the bounty gate, piece by piece."""
    with open(path, "rb") as handle:
        back = handle.read()
    # What landed on disk must be exactly the bytes we built.
    assert back == data, "entry.txt differs from the built entry"
    # Those bytes must decode as UTF-8 and reproduce the line itself.
    assert back.decode("utf-8") == LINE, "entry.txt is not valid UTF-8 LINE"
    # The line must fit the bounty window of 1 to 160 characters.
    assert 1 <= len(LINE) <= MAX_LENGTH, "line must be 1-160 characters"
    # A single line means no line feed anywhere in it.
    assert "\n" not in LINE, "entry must contain no line feed"
    # ... and no carriage return either.
    assert "\r" not in LINE, "entry must contain no carriage return"
    # The file must end on the final full stop, not a trailing newline.
    assert not back.endswith(b"\n"), "entry must have no trailing newline"


def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = build_entry()
    write_entry(path, data)
    os.chmod(out_dir, 0o755)
    validate(path, data)


if __name__ == "__main__":
    main()
