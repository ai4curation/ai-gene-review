# ACBD3 claim-consistency audit

`audit_acbd3_claims.py` is a regression test over this review's *claims*, not its quotes.

## Why it exists

`checkquotes.py` and the repo's reference validator verify that each
`supporting_text` is verbatim in its source. Nothing verified that a **claim** is
stated consistently at the five independent sites that can assert it:

| site | audience |
|---|---|
| `description` | a biologist reading standalone |
| `existing_annotations[].review.summary` | a curator judging the row |
| `existing_annotations[].review.reason` | the action justification |
| `references[].findings[].statement` | what a paper shows |
| `ACBD3-notes.md` | the reviewer's own record |

None is generated from the others. Over PR #2232, revising a claim at the flagged
site while leaving it stale elsewhere accounted for review rounds 10, 12, 13, 14
and 15 — after the biology had settled at round 9.

## What it checks

- **29 retracted phrasings** must not appear anywhere in the gene folder. A
  retracted phrasing may legitimately be *quoted inside its own retraction*, so
  matches are suppressed when a retraction marker appears in a narrow look-back
  window (`-170/+140` characters).
- **9 claims must remain positively present, each with a minimum occurrence count.**
  This catches what a forbidden-string list cannot: a regression that *removes a
  qualifier* rather than adding a wrong phrase. `3A-mediated PI4KB recruitment` is
  the case that motivated it — the scoped form was written in `c1ba137`, deleted by
  the round-9 rewrite in `81f46c582`, and the loss was invisible to every other check.

  The **count** is load-bearing, and the first version of this file did not have it.
  An "appears anywhere" check cannot see a claim removed from *one of several* sites
  — which is precisely the failure it was written to prevent. The self-test below
  caught that: deleting the qualifier from one of its two sites still reported zero
  problems. Occurrence counts are asserted instead.
- Matching is whitespace-normalised, so a phrase broken across a line wrap is
  still found. Several regressions survived plain `grep` for exactly this reason.

## Self-test

The window heuristic is the fragile part: written first as a symmetric 320-character
window, it silently suppressed the very regression being hunted. So the intended
verification is:

```bash
uv run python genes/human/ACBD3/ACBD3-bioinformatics/audit_acbd3_claims.py   # expect 0 problems
# reintroduce a known regression, confirm it is caught, restore, confirm clean again
```

A checker that reports zero problems on a file with a known regression is worse
than no checker.

## Result on the current tree

```
29 retracted phrasings checked, 9 required claims checked, 0 problem(s)
```

Run against the round-13 tree it found exactly one regression — `ACBD3-notes.md`
routing all Golgi scaffolding through two domain surfaces, three lines above a
domain map in the same file listing three. That was independently flagged by the
reviewer in the next round.

## Scope and honesty

This is a **per-gene, hand-maintained lexicon**, not a general lint. It cannot find
a claim nobody has yet noticed is wrong; it only stops a *known* correction from
being undone. Generalising it would mean a lint over the four YAML text slots plus
the notes for any gene whose review has been revised — worth doing, but out of
scope for one gene review.
