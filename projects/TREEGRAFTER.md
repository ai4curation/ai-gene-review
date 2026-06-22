---
title: "TreeGrafter / PANTHER (IBA) Inference Evaluation"
maturity: IN_PROGRESS
tags: [EVALUATION, PIPELINE]
sidecars:
  per_annotation: TREEGRAFTER/treegrafter_iba_review.tsv
  summary: TREEGRAFTER/treegrafter_summary.tsv
---

# TreeGrafter / PANTHER (IBA) Inference Evaluation

## Overview

[TreeGrafter](https://github.com/haimingt/TreeGrafter) (Tang et al. 2019,
[doi:10.1093/bioinformatics/bty625](https://doi.org/10.1093/bioinformatics/bty625))
is the algorithm — bundled into InterProScan — that **grafts** a query protein
onto the most appropriate PANTHER reference phylogenetic tree and then
propagates the GO annotations attached to ancestral nodes of that tree. Those
ancestral annotations are themselves produced by the GO Consortium's
phylogenetic annotation pipeline (PAINT / GO_Central). In GOA the resulting
inferences surface with:

- **Evidence code `IBA`** — *Inferred from Biological aspect of Ancestor*
- **Reference `GO_REF:0000033`**
- **Assigned by `GO_Central`**
- a `WITH/FROM` of the form `PANTHER:PTNxxxxxxxxx`

This project evaluates how good those TreeGrafter-style phylogenetic inferences
are when each one is held to standard GO review criteria, using the AIGR
corpus of expert/AI-adjudicated gene reviews as the gold standard. The key
question: **when an IBA annotation lands on a gene, how often does it survive
review unchanged, and what kinds of IBA annotations systematically fail?**

## Method

Every `genes/*/*/*-ai-review.yaml` review records, per existing annotation, an
`evidence_type` and a reviewer `action` drawn from the AIGR action enum
(`ACCEPT`, `KEEP_AS_NON_CORE`, `MODIFY`, `MARK_AS_OVER_ANNOTATED`, `REMOVE`,
`UNDECIDED`, …). We treat the AIGR adjudication as the reference judgement and
ask how the subset of annotations with `evidence_type: IBA` and
`original_reference_id: GO_REF:0000033` was treated.

Reproduce with:

```bash
python3 projects/TREEGRAFTER/analyze_treegrafter.py
# or, hermetically:
uv run --with pyyaml projects/TREEGRAFTER/analyze_treegrafter.py
```

This writes two committed sidecars (no hard-coded numbers):

- [`TREEGRAFTER/treegrafter_iba_review.tsv`](TREEGRAFTER/treegrafter_iba_review.tsv) — one row per reviewed IBA annotation (gene, taxon, term, action).
- [`TREEGRAFTER/treegrafter_summary.tsv`](TREEGRAFTER/treegrafter_summary.tsv) — action counts and the most frequently down-graded terms.

## Results (current corpus snapshot)

Scanned **2,775** review files; **1,667** genes carry at least one
TreeGrafter/PANTHER IBA annotation, for **6,617** reviewed IBA annotations
total.

| Reviewer action | Count | Share | Interpretation |
|---|---:|---:|---|
| `ACCEPT` | 4,838 | 73.1% | Inference correct and core |
| `KEEP_AS_NON_CORE` | 989 | 14.9% | Correct but peripheral to the gene's core role |
| `MODIFY` | 327 | 4.9% | Right idea, wrong granularity/term |
| `REMOVE` | 195 | 2.9% | Inference unsupported / wrong |
| `MARK_AS_OVER_ANNOTATED` | 191 | 2.9% | Over-propagated |
| `UNDECIDED` | 38 | 0.6% | Could not adjudicate |
| `NEW` / `PENDING` | 39 | 0.6% | Bookkeeping, not a judgement |

**Headline:** ~73% of TreeGrafter IBA inferences are accepted as-is, and ~88%
are retained in some form (`ACCEPT` + `KEEP_AS_NON_CORE`). Only ~5.8% are
outright rejected (`REMOVE` + `MARK_AS_OVER_ANNOTATED`), with another ~4.9%
needing a better term (`MODIFY`). This is a respectable signal-to-noise ratio
for a fully automated phylogenetic pipeline, and notably better than the
generic-domain narrative methods evaluated in
[BIOREASON_COMPARISON](BIOREASON_COMPARISON.md).

### Where TreeGrafter inferences fail

The terms most often down-graded (`REMOVE` / `MODIFY` / `MARK_AS_OVER_ANNOTATED`)
fall into recognizable failure modes:

1. **Generic localization over-propagation.** `membrane` (GO:0016020),
   `cytoplasm` (GO:0005737), `nucleus` (GO:0005634), `plasma membrane`
   (GO:0005886), `cytosol` (GO:0005829), `mitochondrion` (GO:0005739) are
   repeatedly flagged — uninformative or wrong CC terms inherited from
   distant ancestors.

2. **Obsoletion-candidate / superseded MF terms.** `unfolded protein binding`
   (GO:0051082, 67 down-grades) and `protein refolding` (GO:0042026) dominate —
   partly reflecting the ongoing obsoletion of these chaperone terms; IBA keeps
   propagating them onto specialized chaperones that are not general unfolded-protein
   binders.

3. **Pseudo-enzyme / lost-residue over-annotation.** Catalytic activity
   inherited from an enzyme ancestor by a degenerate paralog that has lost the
   active site — e.g. *N*-acetylmuramoyl-L-alanine amidase activity (GO:0008745)
   propagated onto recognition-only PGRPs (PGRPLC, PGRPS1 in *Anopheles*).
   TreeGrafter cannot detect catalytic-residue loss.

4. **Subfamily / context mis-propagation.** Whole-family annotations applied to
   members that have diverged in function — e.g. `sensory perception of smell`
   (GO:0007608) propagated onto *Anopheles* D7 salivary proteins, or
   `photosystem I assembly` (GO:0048564) onto an *Arabidopsis* PSII subunit.

These are exactly the cases where tree-level propagation lacks the
gene-specific evidence (catalytic-residue conservation, organism-specific
biology, fold-level localization signals) that a curator brings.

## Caveats

- The reference standard is the AIGR review corpus, which mixes expert and AI
  adjudication and is itself under continuous revision; treat the rates as a
  living snapshot, not a frozen benchmark.
- `KEEP_AS_NON_CORE` is not an error — it means the inference is *correct* but
  not the gene's core function. Counting it as a "success" for correctness but
  separating it for core-function purposes is deliberate.
- Some IBA annotations were left `PENDING`/`UNREVIEWED` in partially-reviewed
  genes; these are excluded from rate denominators where noted.

## Next steps

- Break the action rates down by GO **aspect** (MF / BP / CC) — the hypothesis
  is that CC IBA is the noisiest aspect.
- Cross-reference the `WITH/FROM` PANTHER family ids to see whether failures
  cluster in specific PANTHER families/subfamilies (candidate PAINT curation
  targets to feed back upstream).
- Compare IBA acceptance against `IEA` (InterPro2GO) on the same genes to
  contrast phylogenetic vs. signature-based transfer.
