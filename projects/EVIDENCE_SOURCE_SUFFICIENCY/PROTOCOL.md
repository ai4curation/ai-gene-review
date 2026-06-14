# EVIDENCE_SOURCE_SUFFICIENCY — Study Protocol (pre-registered)

**Version:** 1.0 · **Status:** PRE-REGISTERED (lock before any labeling) · **Scope:** human

Tests whether lower-effort evidence sources are *sufficient* to support an
**ACCEPT** decision for an existing GO annotation. See `../EVIDENCE_SOURCE_SUFFICIENCY.md`
for motivation and the four hypotheses (H-a reviews, H-b abstracts, H-c deep
research, H-d narrative sections).

## Design decisions (locked)

| Decision | Choice |
|---|---|
| Sampling | **Stratified by GO aspect** (MF / BP / CC) |
| Rigor | **Retrospective fill + blind-ablation validation** on a subsample |
| Size | **30 genes**, ~484 labeled ACCEPT annotations (seed `20260614`) |

## Population and frame

- **Frame:** human gene reviews with `status: COMPLETE` (853 available), so ACCEPT
  decisions are final and not mid-review.
- **Unit of analysis:** an ACCEPT annotation (the decision we want to cheapen).
- **Cluster:** gene (annotations within a gene share references and a reviewer).
- **Read unit:** gene (you fetch a gene's papers once), which is why genes, not
  loose annotations, are the selection unit.

## Sampling

Selection and the aspect strata are produced by `sample/sample_genes.py` with a
**fixed seed** (default `20260614`) so the sample is reproducible.

Across COMPLETE human genes, ACCEPT annotations are **CC-dominated** (~CC 12.1k /
BP 6.7k / MF 5.5k). Fixed per-aspect quotas are therefore unnecessary; instead we
balance by taking the scarcer aspects in full and capping the abundant one:

1. Build the frame of all (gene, ACCEPT annotation) pairs from COMPLETE genes;
   attach GO aspect by joining the term id to the gene's `-goa.tsv` `GO ASPECT`.
2. Seeded-shuffle the genes and take the first `--n-genes` (default **30**).
3. In each selected gene, label **all MF and all BP** ACCEPT annotations plus a
   seeded random subset of **CC** capped at `--cc-cap` (default 10), then trim to
   `--per-gene-cap` (default 30) total, dropping CC first then BP. This bounds the
   design effect from gene clustering and keeps CC from swamping the labeled set.

Realized sample (seed 20260614): **30 genes, 484 labeled ACCEPT annotations —
MF 184 / BP 122 / CC 178**, drawn from **916 references**. The script prints the
realized per-aspect counts so any imbalance is visible rather than silent.

## Instrument

### Layer 1 — reference table (one row per reference in selected genes; cheap)

Fill `publication_type` for **every** reference, upgrading the PubMed-PT guess
with journal/MeSH heuristics + human confirmation so review **undertagging is
fixed on the sample**. Columns: `gene, reference_id, publication_type_auto,
publication_type_final, is_review_final, notes`. `publication_type_final` is
written back to the gene YAMLs (reusable schema data, not study-only).

### Layer 2 — ACCEPT annotation table (one row per sampled annotation; the measurement)

Record **observations**, then *derive* sufficiency — do not ask the labeler "is
the abstract enough?".

| Column | Meaning |
|---|---|
| `gene, term_id, term_label, aspect, evidence_code, qualifier` | from the YAML |
| `original_reference_ids` | refs already cited in support |
| `justifying_fact` | the single claim that licenses ACCEPT (one line) |
| `fact_in_abstract` | Y / N / partial — stated or directly derivable from a cited primary's title+abstract |
| `fact_in_review` | Y / N (+ which review reference) |
| `fact_in_deep_research` | Y / N |
| `section_of_fact` | manuscript section where the fact *first* appears (`reference_section_type` vocab) |
| `minimal_sufficient_tier` | **derived**: `ABSTRACT` if `fact_in_abstract=Y`; else `REVIEW`/`DEEP_RESEARCH` if present there; else `FULLTEXT_PRIMARY` |
| `labeler, confidence, notes` | provenance |

Labelers consult, per annotation: the cited primary abstract(s), any review/DR in
the gene's references, and (for `section_of_fact`) the full text. `section_of_fact`
also backfills `reference_section_type` in the YAML.

## Blind-ablation validation (confirmation-bias control)

Pure retrospective labeling is biased: the labeler already knows the annotation was
ACCEPTed. On a **~18% subsample** (stratified by aspect), a *second* reviewer who is
**blinded to the original decision and to the full text** is handed only a restricted
bundle and asked for a verdict:

- Bundles: `ABSTRACT_ONLY`, `REVIEW_ONLY`, `DEEP_RESEARCH_ONLY` (assigned per row).
- Verdict: `ACCEPT` / `UNDECIDED` / `REJECT` + free-text reason.
- **Unbiased sufficiency** = P(blind verdict = ACCEPT) for each bundle. Compare to the
  retrospective `minimal_sufficient_tier` rates to calibrate the cheaper labels.
- The same subsample is **dual-labeled** in Layer 2 for inter-annotator agreement
  (Cohen's κ on `minimal_sufficient_tier` and `is_review_final`).

## Estimands and analysis (declare before labeling)

Primary, each reported overall and **per aspect**, with **gene-clustered** 95% CIs
(cluster bootstrap or GEE):

- **E-b (H-b):** P(`minimal_sufficient_tier = ABSTRACT` | ACCEPT).
- **E-a (H-a):** P(`fact_in_review = Y` | ACCEPT), and blind P(ACCEPT | REVIEW_ONLY);
  pre-specified subgroup: conserved / IBA (`GO_REF:0000033`) functions.
- **E-c (H-c):** P(`fact_in_deep_research = Y` | ACCEPT), and blind P(ACCEPT | DEEP_RESEARCH_ONLY).
- **E-d (H-d):** distribution of `section_of_fact`; fraction whose fact first appears
  in Introduction / Discussion / Conclusions.

Calibration: agreement between retrospective `minimal_tier=ABSTRACT` and blind
`ACCEPT | ABSTRACT_ONLY`. Report κ for dual-labeled rows.

## Validity threats and mitigations

| Threat | Mitigation |
|---|---|
| Confirmation bias (labeler knows the answer) | observations-not-judgments; blind ablation subsample |
| Review undertagging | journal/MeSH heuristics + human confirm in Layer 1 |
| Section-tag sparsity (~5% today) | Layer 2 fills `section_of_fact` for every sampled annotation |
| Clustering by gene | per-gene cap; gene-clustered CIs |
| Circularity (the cited fact defines its own sufficiency) | blind reviewer re-derives the fact from the restricted bundle, not from the original `supported_by` |

## Effort (rough)

30 genes → **484 Layer-2 rows** and **916 reference rows** (Layer 1). Layer-1
(publication_type) is minutes/gene; Layer-2 `section_of_fact` is the cost driver
(needs full text). Blind subsample ≈ **87 rows** across 3 bundles.

## Reproducibility

```bash
uv run python projects/EVIDENCE_SOURCE_SUFFICIENCY/sample/sample_genes.py \
  --seed 20260614 --n-genes 30 --cc-cap 10 --per-gene-cap 30
```

Outputs (committed, with the seed) under `sample/`:
`selected_genes.tsv`, `annotation_instrument.tsv`, `reference_instrument.tsv`,
`blind_ablation_assignments.tsv`.

Once the instruments are filled, score with:

```bash
uv run python projects/EVIDENCE_SOURCE_SUFFICIENCY/score.py
```

which prints each estimand (overall + per aspect) with gene-clustered bootstrap
95% CIs, the conserved/IBA subgroup, the per-bundle blind sufficiency, and the
retrospective-vs-blind calibration gap. It runs safely on partially-filled
instruments (each estimand uses only its filled rows).
