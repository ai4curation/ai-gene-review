---
title: "Pilot 1 — E. coli genome-wide coherence"
maturity: IN_PROGRESS
tags: [PIPELINE]
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
- **The 17 violations are real, reviewable leads** — and they sort into exactly the three
  categories the project predicts (below), including one likely *genuine biological gap*.
- **It runs on public data with the tooling already here** — GO `has_part` from `go.obo`, the
  EcoCyc GAF, true-path (`is_a`+`part_of`) closure for "present in genome." Numbers are computed
  live by `coherence_pilot.py`; see [RESULTS.md](RESULTS.md) and `violations.tsv`.

## What the leads look like

The 17 violations triage cleanly — this triage is the point, because each class routes to a
different curator action:

| Class | Examples | Likely meaning | Action |
|---|---|---|---|
| **Genuine biological gap** | `denitrification pathway` → missing *nitrous-oxide reductase activity* | E. coli K-12 is not a complete denitrifier (no NosZ); the pathway term is over-reaching | review the `denitrification pathway` annotation; confirm absence with sequence search |
| **Annotation-granularity gap** | `DnaB-DnaC` / `DnaA-DiaA` / `DnaB-DnaG` complexes → missing sub-complex terms; `tRNA CCA addition` → missing its two MF activities; `molybdopterin cofactor biosynthesis` → missing MPT-synthase sulfurtransferase | the gene *is* present; only the finer GO term is unannotated | add the missing MF/CC annotation |
| **Probable over-annotation** | `heterochromatin formation`, `establishment of integrated proviral latency`, `virion attachment to host cell` on E. coli | prophage-gene or electronic propagation of eukaryote/virus-centric terms | candidate `REMOVE` / `MARK_AS_OVER_ANNOTATED`; feeds the over-annotation work |

That a single genome-scale check simultaneously surfaces a metabolic over-reach, a batch of
missing complex/MF annotations, and a set of implausible eukaryote/viral terms — from *nothing
but GO axioms + a GAF* — is the pilot's proof of concept.

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
  bbag336) uses an ELK reasoner to also pull *inferred* `has_part some X` subclasses (~5038
  pairs). So this is a **lower bound** on detectable violations; adding ELK/relation-graph
  inference is the obvious next increment.
- **Set-based, not sequence-based.** A violation cannot by itself distinguish "gene absent"
  from "gene present but unannotated." Genuine-gap candidates (e.g. denitrification) must be
  confirmed with a sequence-level tool (GapMind / Pathway Tools) before any `REMOVE`.
- **Coherence only.** Completeness (a curated minimal-genome essential set) and consistency
  (taxon constraints) are not yet implemented; the small essential-process probe in the output
  is an illustrative sanity check, not the completeness metric.
