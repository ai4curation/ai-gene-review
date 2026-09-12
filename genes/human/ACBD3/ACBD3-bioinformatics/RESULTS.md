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

- **29 retracted phrasings** must not appear in either of the **two** files the
  review authors: `ACBD3-ai-review.yaml` and `ACBD3-notes.md`. It deliberately does
  **not** scan `ACBD3-deep-research-affinage.md` — that is a machine-fetched provider
  record which must not be edited, and `FORBIDDEN[0]` (PI4KB "through its GOLD
  domain") is still live in it, correctly so. The audit governs what this review
  asserts, not what the provider said.
- A retracted phrasing may legitimately be *quoted inside its own retraction*, so a
  match is suppressed when a retraction marker falls in a window weighted backwards
  (`-170/+140` characters): retractions normally introduce the phrasing they retract,
  but some place the marker just after the quote, hence the smaller forward allowance.
- Matching strips **markdown emphasis** as well as collapsing whitespace. Without
  that, `dispensable for **3A-mediated** PI4KB recruitment` in the notes — the most
  explicit statement of that scope anywhere in the review — counted for nothing.
- **9 claims must remain positively present, each with a minimum occurrence count.**
  This catches what a forbidden-string list cannot: a regression that *removes a
  qualifier* rather than adding a wrong phrase. `3A-mediated PI4KB recruitment` is
  the case that motivated it — the scoped form was written in `c1ba137`, deleted by
  the round-9 rewrite in `81f46c582`, and the loss was invisible to every other check.

  The **count** is load-bearing, and the first version of this file did not have it.
  An "appears anywhere" check cannot see a claim removed from *one of several* sites
  — precisely the failure it was written to prevent. The self-test caught that:
  deleting the qualifier from one of its two sites still reported zero problems.

  **Every floor equals the current actual count, with zero slack.** A floor set even
  slightly low silently restores the hole it was meant to close — `3A-mediated PI4KB
  recruitment` was first committed at `5` against an actual `8`, leaving room for
  three assertions of the scope to be deleted unnoticed. Two of the eight are
  `supporting_text` quotes that `checkquotes.py` already protects, so the effective
  prose guard was weaker still. If a claim is legitimately restated more often later,
  raise the floor deliberately rather than leaving headroom.
- Matching is whitespace-normalised, so a phrase broken across a line wrap is
  still found. Several regressions survived plain `grep` for exactly this reason.

## Self-test

The window heuristic is the fragile part: written first as a symmetric 320-character
window, it silently suppressed the very regression being hunted. So the intended
verification is:

```bash
uv run python genes/human/ACBD3/ACBD3-bioinformatics/audit_acbd3_claims.py   # expect 0 problems
# then break it deliberately, three ways, and confirm each is caught:
#   1. reintroduce a retracted phrasing            (round-10 sentence in the notes)
#   2. delete a scope qualifier from ONE of its sites
#   3. remove the emphasis markers from the notes' bolded scope statement
# restore, confirm clean again
```

A checker that reports zero problems on a file with a known regression is worse than
no checker — and this script has hit that state **three** times, each caught only by
trying to break it: the over-wide retraction window, presence-instead-of-count, and a
floor set below the actual count. The script resolves the repository root from its own
path, so it runs from any working directory.

## Result on the current tree

```
29 retracted phrasings checked, 9 required claims checked, 0 problem(s)
```

The counts in this document are the code's: 29 `FORBIDDEN`, 9 `REQUIRED`.

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
