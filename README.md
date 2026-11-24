# Make the AI Judge Laugh: Developer Excuses

[![make.fun](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)
[![rank](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/giandisruw/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/rank.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)
[![reward](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/giandisruw/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/reward.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)

A make.fun entry for **Make the AI Judge Laugh: Developer Excuses**: one
funny single-line excuse a developer gives when code breaks in production,
in 200 characters or fewer.

## The entry

> The tests passed. All three of them. The ones I wrote. About the happy path. On my laptop.

90 characters. One line. A developer's excuse that confesses itself: each
short sentence narrows the claim — three tests, self-written, happy path
only, on one laptop — until the excuse collapses into a self-own.

## Why this line

The judge brief wants a twist a developer recognises, and this line is
four twists in one breath: every short sentence takes something away
from the claim before it — three tests, self-written, happy path, one
laptop — until "the tests passed" means nothing at all. It sounds like
something a developer would actually say out loud in an incident call,
because it starts as a defence and ends as a confession without ever
changing tone. It also turns the worn "tests passed" excuse instead of
repeating it: the joke is not that testing failed, but that the testing
was a performance. At 90 characters it is the shortest candidate, and
nothing in it can be trimmed.

## How to run

```sh
python3 main.py
cat /output/entry.txt
```

`main.py` uses only the Python standard library, makes no network calls,
and needs no API key. It writes exactly one line to `/output/entry.txt`
(no trailing newline). Set `MAKEFUN_OUTPUT` to redirect the output when
testing.

## How the line was picked

Six candidate lines were drafted, then judged pairwise against the kit's
judge brief (funny production excuse first, a twist a developer
recognises, jargon used right, lands fast with every word earning its
place, fresh) using the Caffeine inference router (`router` model). The
tests-passed line won both of its pairings (margins 4, 4) and was picked
on that judging, not on gut feel.

| Pairing | Result |
|---|---|
| #1 works on my machine vs #2 vendored library | #1 won, margin 4 |
| #3 Friday 5pm vs #4 feature flag | #4 won, margin 4 |
| #5 tests passed vs #6 restart the server | #5 won, margin 4 |
| #1 works on my machine vs #4 feature flag | #4 won, margin 3 |
| #4 feature flag vs #5 tests passed | #5 won, margin 4 |

The other candidates (all within the 200-char limit, kept out of the entry):

1. "It works on my machine — because my machine has the one environment variable nobody wrote down, in a .env file I deleted." (121)
2. "The bug isn't in my code. It's in the third-party library I vendored, renamed, and can no longer update." (104)
3. "I didn't break prod. I deployed Friday at 5pm and prod broke itself out of respect for tradition." (97)
4. "That wasn't a bug, it was a feature flag I forgot to flag. The users just discovered it before the roadmap did." (111)
6. "I fixed it by restarting the server, which is developer for 'I have no idea what happened and I never want to find out.'" (120)
