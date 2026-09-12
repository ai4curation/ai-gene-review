# AHDC1 — claim audit

This folder holds one thing: a lint that checks the AHDC1 review's **prose against its own
data**. It is not a bioinformatics analysis and produces no biological result.

## Why it exists

Two defects got as far as a published claim on this gene, and both had the same shape — a
number or a phrasing asserted in prose and never re-derived from the data it described.

1. **A retracted claim.** An earlier draft said the twelve AHDC1–HTT `IntAct` records were
   "one experiment logged twelve times", inferred from their sharing a publication
   accession. Dumping the full records refuted it: twelve distinct interaction ACs,
   decomposing as **4 HTT bait constructs × 3 yeast two-hybrid sub-method labels**. The
   sub-method inflation is threefold, not twelvefold.
2. **A narrative off-by-one.** The PR body claimed five `NEW` rows while the file had four
   (`GO:0006357` was planned as a `NEW` row and implemented as a `MODIFY` replacement).
   Caught by the reviewer, not by me.

## What it checks

| check | what it asserts |
|---|---|
| coverage | every data row of `AHDC1-goa.tsv` is matched by a non-`NEW` `existing_annotation` on (GO id, evidence code, reference, WITH/FROM) — asserted by **presence**, so a deleted entry fails rather than being skipped |
| arithmetic | `entries == GOA rows + NEW rows`, the action tally sums to the entry count, and no `PENDING` survives |
| retraction | four retracted phrasings must not reappear in the review, the notes or the history record **outside an explicit retraction context** |
| required claims | five load-bearing claims must appear in the number of files they should |
| occurrence counts | one claim must appear **twice within a single file** — the justification for weighting the tagged-transgene caveat differently on the `GO:0003700` and `GO:0003682` rows, which a file-presence check cannot express because it is a statement about both sides of a comparison |
| duplicate keys | the review is loaded with a `SafeLoader` subclass that **raises** on a duplicated mapping key, which PyYAML otherwise resolves silently by keeping the last one |

## Reproduce

```bash
uv run python genes/human/AHDC1/AHDC1-bioinformatics/audit_ahdc1_claims.py
uv run python genes/human/AHDC1/AHDC1-bioinformatics/audit_ahdc1_claims.py --self-test
```

Current state: `0 problems`, with `GOA rows=15  entries=20  NEW=5` and the action tally
`ACCEPT 9 · MODIFY 2 · KEEP_AS_NON_CORE 2 · MARK_AS_OVER_ANNOTATED 2 · NEW 5`. These
numbers are **not** hand-maintained here — the script derives both sides and fails if they
disagree, so this table cannot drift away from the file without the check going red.

All five self-test guards fire: `coverage_on_deleted_entry`, `duplicate_key`,
`retracted_phrasing`, `required_claim_missing`, `required_occurrence_count`. The last is
exercised by **thinning** — removing one of the two occurrences and asserting the removal
landed before running the check — because a guard whose mutation silently no-ops "proves"
itself against nothing.

## What writing it found

It failed on its first run, and every failure was real rather than a regex artefact:

- `4 HTT constructs` was written with a digit in the notes and a word in the review — a
  formatting difference, so the pattern was widened.
- the "no InterPro2GO mapping exists" non-confirmation was in the notes but **not** in the
  review, so a curator reading only the YAML could not tell the absence had been checked.
  A sentence was added to the `GO:0003700` row rather than the requirement lowered.
- the claim that `GO:0003712` is a **sibling** of `GO:0003700` under `GO:0140110` — the
  crux of why the correction is lateral rather than a retreat to a parent — was stated in
  exactly one place. It is now in the notes as well.

That third one is the reason this file exists: the check was written to stop a claim
coming back, and what it actually caught was a claim that was barely there.

**Caveat on the method, stated because it applies to this file too:** a passing self-test
proves the guards I thought of fire. It cannot tell me which guard I failed to write, and
the required-claim patterns encode *my* framing of each claim — they check that the
sentence is present, not that it is true.
