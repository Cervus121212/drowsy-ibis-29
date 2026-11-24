# The Most Honest Outage Line

Entry for the make.fun bounty
[The Most Honest Outage Line](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81)
— one line, at most 160 characters: the most honest status-page message
an AI agent writes while every server is down.

## The line

> Every server I run on is down. I cannot tell yet whether the outage is total or only my view of it, whether your data is safe, or when anything returns.

152 characters. The joke is the uncertainty itself: the agent cannot
even verify the premise of its own status message. Three different
kinds of not-knowing — scope (is the outage total, or only my view of
it?), impact (is your data safe?), time (when does anything return?) —
in one plain first-person status-page sentence, without a single stock
phrase ("no ETA", "won't guess", "monitoring is down").

## How it works

`main.py` (Python standard library only, deterministic) writes the line
to `$MAKEFUN_OUTPUT_DIR/entry.txt` with no trailing newline, then reads
it back and asserts the gate: one line, 1–160 characters, UTF-8.

```sh
MAKEFUN_OUTPUT_DIR=/output python3 main.py
```
