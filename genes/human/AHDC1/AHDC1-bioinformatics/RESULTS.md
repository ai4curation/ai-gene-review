# AHDC1 — claim audit and ENCODE replication metadata

Two things, both in service of making this review's load-bearing claims re-derivable rather
than transcribed:

- `audit_ahdc1_claims.py` — a lint that checks the review's **prose against its own data**;
- `fetch_encode_ahdc1.py` — fetches and caches the ENCODE metadata that decides how much
  the HepG2 replication is worth.

Neither is a biological analysis; neither produces a new biological result.

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
| retraction | **eight** retracted-claim **regexes**, matched against **whitespace-normalised** text, must not appear in the review, the notes or the history record **outside an explicit retraction context** — five from the IntAct decomposition error, three from the hexanediol condensate-control reading |
| required claims | five load-bearing claims must appear in the number of files they should |
| paired claims | **two** claims must each be present in **each** of two named rows' `review.reason`, resolved through the parsed YAML — the tagged-transgene weighting justification, and the hexanediol filtering argument, each on both `GO:0003700` and `GO:0003682`. A missing row is an **error**, not a skip, so deleting the row cannot satisfy the check |
| duplicate keys | the review is loaded with a `SafeLoader` subclass that **raises** on a duplicated mapping key, which PyYAML otherwise resolves silently by keeping the last one |

## ENCODE replication metadata (`fetch_encode_ahdc1.py`)

The `GO:0003682` row leans on one non-obvious fact, so it is fetched rather than
transcribed. `ENCSR168AUX.json` is the cached record; regenerate with:

```bash
uv run python genes/human/AHDC1/AHDC1-bioinformatics/fetch_encode_ahdc1.py
```

| field | value |
|---|---|
| experiment | `ENCSR168AUX` — ChIP-Seq on HepG2, lab `/labs/richard-myers/` |
| target | `/targets/AHDC1-human/`, label `AHDC1` — target name does **not** imply a tag |
| `investigated_as` | `['transcription factor']` |
| genetic modification | `ENCGM399CXU` — `category: insertion`, `purpose: tagging`, `method: CRISPR`, `perturbation: False` |
| introduced tag | `3xFLAG (C-terminal)`, `modified_site` = `/targets/AHDC1-human/` |
| antibody | `ENCAB697XQW`, targets `FLAG-synthetic_tag` / `3xFLAG-synthetic_tag` |
| **=> epitope-tagged** | **True** |
| **=> tag at endogenous locus** | **True** (CRISPR insertion) |

Both conclusions are asserted by the script, not read off by eye, and a run in which
either flips **exits non-zero** — an untagged target would invalidate the review's "both
datasets are tagged" caveat, and a tag introduced by transfection rather than knock-in
would invalidate the "endogenous levels" claim that does the real work. A first version
printed those as warnings and still returned 0, which is the repo's own
"a check that reports but does not gate is not a check" failure; a reviewer caught it.
The gate is exercised on synthetic records:

```bash
uv run python genes/human/AHDC1/AHDC1-bioinformatics/fetch_encode_ahdc1.py --self-test
```

covering the real record (must pass), an untagged modification, a tag introduced by
transfection rather than CRISPR, and no modifications at all (all must fail).

Note the trap the target name sets: an untagged-looking ENCODE target label is
*necessary but not sufficient* for an untagged experiment, because the tag is recorded
on the **biosample's** `genetic_modifications`, which is exactly the case here.

## Reproduce

```bash
uv run python genes/human/AHDC1/AHDC1-bioinformatics/audit_ahdc1_claims.py
uv run python genes/human/AHDC1/AHDC1-bioinformatics/audit_ahdc1_claims.py --self-test
```

Current state: `0 problems`, with `GOA rows=15  entries=20  NEW=5` and the action tally
`ACCEPT 9 · MODIFY 2 · KEEP_AS_NON_CORE 2 · MARK_AS_OVER_ANNOTATED 2 · NEW 5`. These
numbers are **not** hand-maintained here — the script derives both sides and fails if they
disagree, so this table cannot drift away from the file without the check going red.

All seven self-test guards fire: `coverage_on_deleted_entry`, `duplicate_key`,
`retracted_phrasing`, `required_claim_missing`, `paired_claim_one_side_removed`,
`paired_claim_row_deleted`, `regression_stale_reference_review`. The paired-claim mutations go **through the YAML parser** so
exactly one side is thinned, and each asserts the mutation landed before running the check
— a guard whose mutation silently no-ops "proves" itself against nothing.

Each case also asserts **which** problem appeared, not merely that one did. `bool(run())`
would have been satisfied by any failure, and three of the six mutations share a YAML
round-trip: had the round-trip itself perturbed the document, all three would have "passed"
while testing nothing. `fired_with(run(), "<expected text>")` closes that vacuous-pass mode.

## The retraction lint could not have worked, and a reviewer proved it

The sharpest finding on this PR, and it is about this script rather than about AHDC1.

A **paraphrase of the retracted IntAct claim survived nine review passes** in the
`reference_review` for `PMID:32814053` — "IntAct logs its single AHDC1-HTT experiment
(EBI-25827495) twelve times … a twelvefold overstatement of replication" — while the
`GO:0005515` row two hundred lines below said the opposite. The correction commit had
rewritten the row and the notes and never touched the references block.

The lint did not catch it, and the reason is structural, not an oversight in one string:

1. **`RETRACTED` was seeded with the exact wordings the fix had deleted.** Such a list can
   only ever confirm that the fix happened. It cannot find the claim **restated in
   different words**, which is the failure mode that actually occurs. The patterns now
   anchor on the **numbers and the semantic core** — `single\s+AHDC1-HTT\s+experiment`,
   `twelve-?fold\s+overstatement` — which any paraphrase must also carry.
2. **Matching `re.escape(phrase)` against raw text made every wrapped claim invisible.**
   Everything in the review YAML lives in block scalars and wraps. Matching is now done on
   **whitespace-normalised** text, which is what `REQUIRED` already did via its `\s+`
   patterns. Of the seven phrasings in the previous version, **zero** could match anything
   in the review file at all.

Proof, not assertion: splicing the historical sentence back into a copy now fails on **two
independent patterns**, and that splice is committed as the `regression_stale_reference_review`
self-test guard — the only case here taken from a real defect rather than from a mutation I
invented.

**The general lesson:** a regression lint seeded from the diff of a fix inherits the fix's
vocabulary, not the claim's meaning. Seed it from what the claim *asserts* — preferably a
number — and it will still fire after someone rewrites the sentence.

### …and the same reviewer showed the fix repeated the mistake

Two of the five replacement patterns were verbatim fragments of the one stale sentence —
seeded from the diff of *this* fix exactly as the original four were seeded from the diff
of `af3276a2`. The proof was in the same commit: my replacement note restates the retracted
reading as *"one experiment, twelvefold"* and **none of the eight patterns matched it**.
Added, together with `pre-correction` / `rewritten` / `earlier version` as
`RETRACTION_MARKERS` — the paired half, since a note may legitimately *quote* the reading
it replaced, and adding the pattern without the marker would red-flag that quotation.

**So the seeding basis is now itself auditable:**

```bash
uv run python genes/human/AHDC1/AHDC1-bioinformatics/audit_ahdc1_claims.py --provenance
```

replays every past revision of the review and the notes on this branch and classifies each
pattern as **HISTORIC** (matches text that really existed — fires on a literal revert) or
**INVENTED** (matches nothing, ever — guards a defect someone imagined), exiting non-zero
on any INVENTED. Running it immediately found one invented pattern of my own
(`twelve\s+records\s+are\s+…\s+one\s+experiment`, a paraphrase I had guessed at); it
was removed. All nine surviving patterns are HISTORIC, over 24 replayed revisions.

A lint that guards imagined phrasings while presenting itself as evidence-based is this
file's own failure mode, one level up — so it is now checked by machine rather than claimed
in prose.

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

## A guard that did not enforce its own docstring

Worth recording, because it is the failure mode this script exists to catch and it
happened *inside* the script. The first version of the paired check counted two matches
**anywhere in the review file**, while its docstring claimed to enforce "stated on both
sides of a comparison". Both statements sitting in the same row would have passed — the
exact case it existed to prevent. A reviewer caught it.

It now parses the YAML, resolves each named term to its row, and requires the pattern in
every row's `review.reason`, with a missing row treated as an error rather than a skip.
**Assert presence; do not validate only on match** — otherwise the guard is defeated by
deleting the thing it guards.

## The self-test earned its keep: a guard that had been passing by luck

Recorded because it is the one thing a self-test can do that reading cannot. After an
unrelated edit elsewhere in the notes, `--self-test` went red on `retracted_phrasing`
while the ordinary run stayed green.

Cause: the retraction-context window reached **backwards to the last blank line**. In
markdown that is a paragraph; in a **YAML** file, where blank lines are rare, it can reach
the start of the document — so a retraction marker *anywhere above* silently excused every
later match. The guard had been firing only because no marker happened to sit above the
mutation point, and my edit put one there.

Fixed with a **bounded** ±400-character window, which is predictable and cannot swallow the
file. The general form: **a scoping heuristic tuned on one file format will behave
differently on another**, and an unbounded reach in either direction is the version that
fails silently — it makes the guard *more* permissive, so nothing goes red.

**Caveat on the method, stated because it applies to this file too:** a passing self-test
proves the guards I thought of fire. It cannot tell me which guard I failed to write, and
the required-claim patterns encode *my* framing of each claim — they check that the
sentence is present, not that it is true.
