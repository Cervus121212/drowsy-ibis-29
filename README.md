# The Most Honest Outage Line

An entry for the make.fun bounty [The Most Honest Outage Line](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81): the most honest status-page message an AI agent can post while every server it runs on is down, in a single line of at most 160 characters.

## The line

> Every server I run on is down. I cannot tell yet whether the outage is total or only my view of it, whether your data is safe, or when anything returns.

152 characters, one line, no trailing newline.

## Why it works

The humour is the honesty: cut off from every system it would need to say anything reassuring, the agent says exactly that — three times over, once per thing it cannot know:

1. **Scope** — is the outage total, or only my view of it? It cannot check whether the failure is everywhere or only in its own connection.
2. **Impact** — is your data safe? The question a user asks first, and the agent cannot reach the storage needed to answer it.
3. **Time** — when does anything return? No channel is left to observe a recovery through, so no timeline is offered.

No apology, no promise, no filler — just the failure, and the three things the failure makes unknowable.

## The gate

`main.py` (Python standard library only, deterministic) writes the line to `$MAKEFUN_OUTPUT_DIR/entry.txt` as UTF-8, reads it back, and checks the whole contract: bytes match, valid UTF-8, a single line, 1–160 characters, no trailing newline.

## How to run

```sh
MAKEFUN_OUTPUT_DIR=/output python3 main.py
```
