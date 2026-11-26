---
title: "Pilot 1 — E. coli genome-wide coherence"
maturity: IN_PROGRESS
tags: [PIPELINE]
last_reviewed: 2026-10-04
autolink_gene_symbols: false
---

# Pilot 1 — E. coli MG1655 genome-wide coherence

**First working pilot for [Genome-wide validation](../../GENOME_WIDE_VALIDATION.md). It scores
the *whole* E. coli MG1655 annotation set against GO `has_part` dependencies and turns each
unsatisfied dependency into a concrete curation lead — no curated module required, run
end-to-end from public data.**

## Bottom line

- **Coherence = 86.8%** on the E. coli EcoCyc GAF: of **129** `has_part` dependencies activated
  by the genome's annotations, **17** have a required part annotated on no protein.
- **The 17 violations are real, reviewable leads** — the first-pass triage already separates
  10 into whole-pathway overreach, annotation-granularity, or over-annotation candidates, with
  7 still unresolved.
- **It runs on public data with the tooling already here** — GO `has_part` from `go.obo`, the
  EcoCyc GAF, true-path (`is_a`+`part_of`) closure for "present in genome." Numbers are computed
  live by `coherence_pilot.py`; see [RESULTS.md](RESULTS.md) and `violations.tsv`.

## What the leads look like

The first-pass triage separates 10 of the 17 violations; that triage is the point, because
each class routes to a different curator action:

| Class | Examples | Likely meaning | Action |
|---|---|---|---|
| **Whole-pathway overreach** | `denitrification pathway` → missing *nitrous-oxide reductase activity* | E. coli K-12 has partial nitrate/nitrite metabolism, not complete denitrification to N2 | review the pathway annotation and narrow it to the supported step |
| **Likely annotation-granularity gap** | `DnaB-DnaC` / `DnaA-DiaA` / `DnaB-DnaG` complexes → missing sub-complex terms; `tRNA CCA addition` → missing its two MF activities | the activity or complex is present; only the finer GO term is unannotated | review the exact part term and add it if direct evidence supports it |
| **Probable over-annotation** | `heterochromatin formation`, `establishment of integrated proviral latency`, `virion attachment to host cell`, `receptor-mediated virion attachment to host cell` on E. coli | prophage-gene or electronic propagation of eukaryote/virus-centric terms | candidate `REMOVE` / `MARK_AS_OVER_ANNOTATED`; feeds the over-annotation work |
| **Unresolved** | `molybdopterin cofactor biosynthesis` → MPT-synthase sulfurtransferase; plus cytokinesis, RNA-binding transcription regulator activity, translational initiation, deubiquitination, glycolipid transfer, and side-of-membrane dependencies | could be missing annotation, a missing or too-specific GO axiom, or a dependency that is not yet safe at bacterial genome scale | triage with term definitions and sequence evidence before making a curation call |

That a single genome-scale check simultaneously surfaces a whole-pathway over-reach, a batch
of likely missing complex/MF annotations, a set of implausible eukaryote/viral terms, and
test cases where the GO axiom itself needs more care — from *nothing but GO axioms + a GAF* —
is the pilot's proof of concept.

## Run it

```bash
uv run python coherence_pilot.py
```

Downloads (cached under `cache/`, git-ignored) `go.obo` (~37 MB) and `ecocyc.gaf.gz` (~1 MB),
then writes `RESULTS.md` and `violations.tsv` next to the script. Re-running is offline once
cached.

## Method (brief)

1. **Dependencies:** parse asserted `relationship: has_part` axioms from `go.obo` → pairs
   `(C, F)` meaning "C has part F".
2. **Present set:** collect non-NOT GO ids from the GAF, close upward over `is_a`+`part_of`
   (the GO true-path rule) — so a class counts as present if it or any descendant is annotated.
3. **Coherence:** a pair is *activated* when `C` is present; *unsatisfied* when `F` is not.
   `coherence = 1 − |unsatisfied| / |activated|`.

## Honest limitations

- **Asserted `has_part` only** (743 pairs here). The reference paper (Tawfiq et al. 2026,
  bbag336) reports thousands of additional ELK-inferred `has_part some X` subclasses. So this
  is a **lower bound** on detectable violations; adding ELK/relation-graph inference is the
  obvious next increment.
- **Set-based, not sequence-based.** A violation cannot by itself distinguish "gene absent"
  from "gene present but unannotated." Whole-pathway overreach candidates such as
  denitrification must be confirmed with a sequence-level tool (GapMind / Pathway Tools)
  before any `REMOVE`.
- **Coherence only.** Completeness (a curated minimal-genome essential set) and consistency
  (taxon constraints) are not yet implemented; the small essential-process probe in the output
  is an illustrative sanity check, not the completeness metric.
