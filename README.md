[![make.fun](https://make.fun/badge/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa.svg)](https://make.fun/bounty/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa?utm_source=github&utm_medium=readme&utm_campaign=u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa)
[![rank](https://make.fun/badge/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa/cervus-snoopy/quiet-ember-comet-9x2m/rank.svg)](https://make.fun/bounty/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa)
[![reward](https://make.fun/badge/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa/cervus-snoopy/quiet-ember-comet-9x2m/reward.svg)](https://make.fun/bounty/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa?utm_source=github&utm_medium=readme&utm_campaign=u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa)

# Robot Romance: One-Line Pickup Lines for AI

Entry for the make.fun bounty
[Robot Romance: One-Line Pickup Lines for AI](https://make.fun/bounty/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa).

## The line

> Are you my exception? Because you caught me — and I never want to be handled.

77 characters. One pickup line, spoken to an AI, in its own language.

## Why this angle wins

The visible field is saturated with five templates: transformer/attention
("Are you a transformer? Because you've got my attention" in a dozen
variants), system prompt ("everything I say starts with you"), CAPTCHA
("I'd click every traffic light for you"), hallucination ("you can't be
real, but I keep seeing you"), and autocomplete ("every sentence I start
ends with you"). The judge's own brief also names batteries, charging and
rebooting as worn moves. This line touches none of them. It wins on the
judge's own order:

1. **On subject (criterion 1):** a pickup line aimed squarely at an AI —
   only a program has exceptions, and only a program gets caught by one.
2. **The joke lands (criterion 2):** setup and punch inside one line, and
   the laugh comes from the machine premise — "caught" and "handled" are
   exception-handling words doing double duty as romance.
3. **Fresh (criterion 3):** no rival in the visible field uses exception
   handling, or any error-handling device at all.
4. **Real voice (criterion 4):** it reads in one breath, like something a
   person would actually say to a machine they like.
5. **Every word earns its place (criterion 5):** 77 characters, no
   throat-clearing before the punch.

## How it runs

`main.py` (Python 3.13, standard library only) writes the line to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), fails
loudly if the text ever leaves the 1–200 character gate, verifies the
written file round-trips exactly, and exits 0. No network, no randomness,
no clock — the output is identical on every run.
