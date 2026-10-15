---
title: "Regulation of X: Consistency and Meaning"
maturity: SCOPING
tags: [PIPELINE, EVALUATION]
species: [human]
---

# Regulation of X: Consistency and Meaning

**Bottom line:** a third of GO biological-process terms and 31% of human BP
annotation rows are "regulation of X". This project audits how consistently
they are used. The first pass covers GOA human and the 7,168 existing reviews.
It finds three recurring patterns that are worth triaging:

- a gene annotated both to X and to regulation of X (5,167 gene–process pairs);
- a gene annotated to both positive and negative regulation of the same X
  (1,242 pairs);
- unsigned "regulation of X" sitting alongside a signed term for the same X
  (2,220 pairs).

Can we work out after the fact what a "regulation of X" row means? Partly.
Reviewers' MODIFY replacements tell us directly in about 1,000 cases. Simple
rules flag likely misfiled participants: rows the rules put in the
misfiled-participant bucket were modified to the participant term 8% of the
time, against at most 0.5% for rows with no participant co-annotation. Most rows
are still kept as they are, so the rules can rank a review queue but cannot
rewrite annotations automatically. The companion enrichment eval in
`monarch-initiative/genesets`
([`evals/regulation_closure`](https://github.com/monarch-initiative/genesets/tree/main/evals/regulation_closure))
asks what the same choices cost in enrichment analysis.

## Why regulation terms are noisy

GO separates participating in X from regulating X. Real annotation does not
always keep them apart:

- **Participant misfiled as regulator.** A core component of a pathway is
  annotated to *positive regulation of* that pathway because knocking it down
  lowers the output. Necessity evidence cannot tell a component from an
  upstream activator (see "Do not add what curators deliberately declined to
  add" in `CLAUDE.md`).
- **Readout-driven sign.** IMP/IGI rows record the sign of a phenotype
  readout, which depends on cell type, dose and the assay window. Both signs for
  the same X often mean two papers measured different contexts, not that the
  gene has two activities. The Drosophila LKB1–AMPK reviews contain the
  reverse case: *positive regulation of TORC1 signaling* (IMP) corrected to
  *negative* by the reviewer.
- **Indirect, via gene expression.** A transcription factor gets "regulation of
  X" for every X its targets affect.
- **Ontology structure.** GO places *signal transduction*, and so every
  signaling pathway, `is_a` *regulation of cellular process*. Tools that treat
  `is_a regulation` as "is a regulation term" will count all signaling as
  regulation. The script below avoids this by keying on explicit `regulates`
  edges.

## Method

[`regulation_triage.py`](REGULATION_CONSISTENCY/regulation_triage.py) is
deterministic. It takes the full `go.obo` (go-basic lacks the regulates
relations), a GAF and the `genes/` tree:

```bash
uv run python projects/REGULATION_CONSISTENCY/regulation_triage.py \
  --obo go.obo --gaf goa_human.gaf.gz --genes-dir genes \
  --out-dir projects/REGULATION_CONSISTENCY/results
```

1. **GOA triage.** For each gene and each process X targeted by a
   `regulates` / `positively_regulates` / `negatively_regulates` edge, the
   script records the signs annotated, whether the gene also participates in X
   (X itself, or a non-regulation is_a/part_of descendant), and the evidence.
   For broad grouping targets (more than 500 descendants, e.g.
   *biological_process*) only a direct annotation to X counts as
   participation.
2. **Meaning heuristics.** Each regulation row gets an ordered rule-based
   guess: `upstream_effect_qualifier` (an `acts_upstream_of*` qualifier),
   `participant_misfiled_as_regulator` (co-annotated participant, + or
   unsigned, no regulator MF), `participant_with_feedback_or_modulation`,
   `indirect_via_gene_expression` (TF, X not transcription),
   `perturbation_readout` (IMP/IGI/IEP only), `direct_regulator_candidate`
   (regulator-type MF), `propagated_unclassified`, `unclassified`.
3. **Review mine.** For every review, the script tallies the action on each
   regulation row. Each MODIFY is classified by where its replacement points:
   the participant term, the opposite sign, a signed child of an unsigned term,
   a more specific X with the same sign, a broader term, or something else.
4. **Calibration.** Reviewer decisions on human rows are cross-tabulated
   against the heuristic bucket of the same (gene, term) row.

Outputs in [`results/`](REGULATION_CONSISTENCY/results/):
`summary.yaml` (all counts), `triage_queue.tsv` (the 7,630 flagged
gene–process pairs), `review_regulation_modifications.tsv` (972 reviewer
MODIFY replacements on regulation terms) and
`review_participant_and_regulator_pairs.tsv`. The full per-row tables
(`goa_pairs.tsv`, `goa_regulation_rows.tsv`) are regenerated, not committed.

## Findings (GO 2026-07-26, goa_human 2026-05-21)

### The scale

| | count |
|---|---|
| BP terms / of which regulation terms | 23,974 / 8,342 (35%) |
| human BP annotation rows / regulation rows | 204,224 / 62,719 (31%) |
| genes with any regulation annotation | 12,280 |
| gene–process (X) pairs with a regulation annotation | 41,708 |
| … also annotated as participant in X | 5,167 |
| … both + and − regulation of X | 1,242 |
| … unsigned alongside signed | 2,220 |
| regulation rows carrying an `acts_upstream_of*` qualifier | about 4% |

The sign conflicts are concentrated in a few targets. Most are biologically
expected and only a minority are noise. *Transcription by RNA polymerase II*
(336 genes), *DNA-templated transcription* (187) and *gene expression* (127)
are dual-function transcription regulators. *Apoptotic process* (46) and
*cell population proliferation* (45) are mostly context-dependent readouts.
The genes with the most sign-conflicted targets are pleiotropic signaling
hubs: APOE (9), TGFB1 (8), SFRP1 (7), TNF (6), and miRNAs.

### What reviewers do with regulation terms

Across all reviews, reviewers treat regulation rows differently from other BP
rows. They rarely remove them; they demote them:

| action | regulation rows (21,233) | other BP rows (56,372) |
|---|---|---|
| ACCEPT | 35.6% | 47.5% |
| KEEP_AS_NON_CORE | 46.7% | 32.9% |
| MARK_AS_OVER_ANNOTATED | 6.9% | 6.8% |
| MODIFY | 4.4% | 5.5% |
| REMOVE | 1.1% | 2.1% |

Where a reviewer changed a regulation term, the replacement records what they
decided the row meant:

| replacement points to | MODIFYs |
|---|---|
| same sign, more specific X | 242 |
| signed child of an unsigned term | 239 |
| **the participant term X** (row meant participation) | 205 |
| a non-regulation process other than X | 104 |
| a different regulation term | 102 |
| **opposite sign** | 37 |
| broader term | 33 |

Examples of participant re-filing: BAK1 *positive regulation of apoptotic
process* → *mitochondrial outer membrane permeabilization*; RBX1 *positive
regulation of protein catabolic process* → *proteasome-mediated
ubiquitin-dependent protein catabolic process*; AP2S1 *regulation of
endocytosis* → *clathrin-dependent endocytosis*; ZSWIM8 *positive regulation
of miRNA catabolic process* → *target-directed miRNA degradation*.

### Can the meaning be recovered after the fact?

The calibration below covers 8,802 human rows that have both a GOA record and a
reviewer decision:

| heuristic bucket | n | ACCEPT | NON_CORE | OVER_ANN | MODIFY→participant |
|---|---|---|---|---|---|
| participant_misfiled_as_regulator | 570 | 43% | 34% | 5% | **8.2%** |
| participant_with_feedback_or_modulation | 863 | 41% | 43% | 4% | 1.9% |
| direct_regulator_candidate | 2,181 | 33% | 48% | 10% | 0% |
| unclassified | 1,092 | 28% | 55% | 7% | 0.4% |
| propagated_unclassified | 1,303 | 18% | 56% | **14%** | 0.1% |
| indirect_via_gene_expression | 975 | 20% | **63%** | 9% | 0% |
| perturbation_readout | 1,435 | 22% | **62%** | 9% | 0.1% |
| upstream_effect_qualifier | 383 | 30% | 57% | 6% | 0.5% |

1. **The buckets carry signal.** Co-annotation as a participant is the
   strongest predictor of a participant re-filing: 8% in the misfiled bucket,
   2% for other co-annotated rows, and at most 0.5% elsewhere. Perturbation-only and indirect-via-TF rows are the most often
   demoted to non-core. Propagated rows are the most often marked
   over-annotated.
2. **The signal is not strong enough to automate.** Even in the
   participant-misfiled bucket, 77% of rows were accepted or kept. In many
   cases both readings hold: a component that also limits flux through its
   pathway. Use the buckets to order work, not to rewrite annotations.
3. **GAF already has the right vocabulary but rarely uses it.**
   `acts_upstream_of_positive_effect` / `_negative_effect` record a signed
   causal effect without claiming the gene regulates X. Fewer than 0.2% of
   regulation rows use them. Many perturbation-only "positive/negative
   regulation of X" rows are what those qualifiers were designed for.

## Regulation terms versus extensions, across annotation sources

Could a "regulation of X" annotation instead be a more precise statement
about *which gene* is regulated? GO already supports that through annotation
extensions. For a TF, the precise form is DNA-binding TF activity
`has_input(target gene)`, or a regulation term with a gene-product extension.
[`regulation_by_species.py`](REGULATION_CONSISTENCY/regulation_by_species.py)
compares human GOA with six MOD GAFs from the same GO release
([`results/regulation_by_species.yaml`](REGULATION_CONSISTENCY/results/regulation_by_species.yaml)):

| | human | pombe | yeast | mouse | fly | worm | Arabidopsis |
|---|---|---|---|---|---|---|---|
| regulation share of BP rows | 31% | **12%** | 14% | 31% | 18% | 21% | 15% |
| … of which transcriptional | 29% | 45% | 50% | 26% | 35% | 35% | 50% |
| … perturbation-only evidence | 18% | 41% | 55% | 21% | 56% | 55% | 36% |
| … with a gene-product extension | 5% | 5% | 7% | 3% | 1% | 7% | 0% |
| TF rows on a *non*-transcriptional regulation term | 2,922 | **45** | 219 | 5,212 | 585 | 420 | 1,036 |
| … with a gene-product extension | 1% | 2% | 0% | 0% | 0% | 1% | 0% |
| TF activity (MF) rows naming a target gene | 5% | **75%** | 9% | 5% | 3% | 1% | 0% |

**Pombe uses regulation terms sparingly, and models TF targets on the MF.**
Regulation terms make up 12% of PomBase BP rows, against 31% for human and
mouse. Half of PomBase's regulation rows are transcriptional, and almost none
put a TF on regulation of a downstream process (45 rows). Instead, 75% of
PomBase's DNA-binding TF activity rows name the target gene with `has_input`.
Human GOA does that for 5% of TF activity rows. Its 2,922 rows placing TFs on
"regulation of" a non-transcriptional process carry a target gene in 1% of
cases.

**So in human, a TF on "regulation of X" is usually a weaker, higher-level
stand-in for "this TF controls gene(s) Y that act in X".** The target gene is
almost never recorded. These rows correspond to the
`indirect_via_gene_expression` bucket above, which reviewers most often demote
to non-core. Converting them to the pombe pattern would mean finding the
targets in the source papers, which is a curation task rather than a
relabelling.

**For enrichment, though, TFs are not where the valid regulation signal
comes from.** In the genesets recuration, 145 of the 149 regulation terms
judged core or supporting regulate non-transcriptional processes:
proliferation, cell death, immune activation, the MAPK cascade, muscle
contraction. Only 8% of the contributing genes are TFs, the same rate as in
rejected regulation terms. Most of that signal comes from signaling components
and effectors. GO-CAM would express it as causal links between activities,
and a GAF can express it only with `causally_upstream_of` or
`has_regulation_target` extensions. Those are rare everywhere: under 0.5% of
human regulation rows.

Two other contrasts to follow up:

- **Pombe and yeast lean on perturbation evidence for regulation** (41% and
  55% of rows, against 18% for human). So a low regulation share does not
  mean PomBase has stricter evidence standards for these rows.
- **MGI and TAIR use `acts_upstream_of*` qualifiers** on 20% and 30% of
  regulation rows, against 3.5% for human and none for pombe. Those rows are
  the explicit form of the "perturbation readout" reading.

## Proposed triage rules

These are draft rules for review practice. They are not yet enforced.

| pattern | default action |
|---|---|
| X and positive/unsigned regulation of X, gene is a pathway component (no regulator MF) | review: likely `MODIFY` → X, or `KEEP_AS_NON_CORE` if a flux-limiting role is documented |
| unsigned regulation of X alongside signed regulation of X | the unsigned row is entailed: `TOO_GENERAL` only if the signed row is kept in the same review |
| + and − regulation of X | check each source; keep both only if the papers show context-specific opposite effects, otherwise sign-check (37 reviewer sign flips so far) |
| perturbation-only regulation of a broad readout (proliferation, apoptosis, migration) | `KEEP_AS_NON_CORE` unless the mechanism is shown |
| TF annotated to regulation of a non-transcription process | `KEEP_AS_NON_CORE`; core function is the transcription regulator activity |

## Enrichment consequences (genesets)

The genesets benchmark was first scored as it stood (126 sets, 394 CORE
terms). On that gold, dropping regulation terms looked free, because it lost
only the gold's own regulation terms. That gold had rarely been offered
regulation-only hits, so the contested region was recurated. Candidates were
pooled symmetrically from all four variants (884 terms) and judged blind to
which variant proposed them:

| variant | recall, recurated gold (481 CORE) | precision on judged contested hits |
|---|---|---|
| current is_a/part_of | 0.549 | 0.458 |
| drop regulation terms | 0.459 | 0.356 |
| regulates closure | **0.653** | **0.462** |
| collapse regulation onto X | 0.555 | 0.400 |

- **Regulation terms are not the noise for enrichment.** Judges called 50% of
  contested regulation-term hits core or supporting, against 40% of
  participant-term hits.
- **Regulates closure gives the best recall** at unchanged precision. Collapse
  is the compact option: it matches closure on participant recall with 27%
  less output.
- This sits alongside the annotation-level noise documented above. GOA's
  regulation rows are internally inconsistent, but in aggregate they still
  carry real signal about what a gene set does. Regulates closure also
  propagates the inconsistent rows triaged here, so cleaning them should
  improve it further.

## Next steps

1. Work the `triage_queue.tsv` participant-and-regulator pairs for genes that
   already have reviews, starting with signaling-pathway targets.
2. Add GO-CAM evidence (`gocams/index.tsv`): when a model places the gene as
   an activity *part of* X, that should settle the participant reading. When it
   places the gene *causally upstream of* X, the regulation reading stands.
3. Extend to the MOD GAFs (mouse, fly, worm, yeast, Arabidopsis), where many
   of the sign flips above came from.
4. Write the triage rules into the review guidelines, and possibly into
   `action_consistency.yaml` for the unsigned/signed redundancy case.
