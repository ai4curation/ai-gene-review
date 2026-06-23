---
title: "TreeGrafter Inference Evaluation"
maturity: IN_PROGRESS
tags: [EVALUATION, PIPELINE]
sidecars:
  per_annotation: TREEGRAFTER/treegrafter_review.tsv
  summary: TREEGRAFTER/treegrafter_summary.tsv
---

# TreeGrafter Inference Evaluation

## Overview

[TreeGrafter](https://github.com/haimingt/TreeGrafter) (Tang et al. 2019,
[doi:10.1093/bioinformatics/bty625](https://doi.org/10.1093/bioinformatics/bty625))
is the algorithm — bundled into InterProScan — that **grafts** a query protein
onto the most appropriate PANTHER reference phylogenetic tree and then
propagates the GO annotations attached to the grafting node down onto the query.

The critical distinction this project keeps straight is **TreeGrafter vs.
PAINT/IBA**, which are routinely conflated:

| | PAINT / IBA | **TreeGrafter** |
|---|---|---|
| Applies to | genes already **in** the PANTHER reference tree (well-studied "core" species) | sequences **not** in the reference tree — grafted on |
| Made by | **curators**, by hand, on the tree | fully **automated** propagation |
| Evidence code | `IBA` (Inferred from Biological aspect of Ancestor) | `IEA` (Inferred from Electronic Annotation) |
| Reference | `GO_REF:0000033` | **`GO_REF:0000118`** |
| Assigned by | `GO_Central` | **`TreeGrafter`** |
| `WITH/FROM` | `PANTHER:PTN...` | `PANTHER:PTN...` |

So **the TreeGrafter-based inferences are the `IEA` / `GO_REF:0000118` /
assigned-by `TreeGrafter` annotations** — *not* the IBA ones. (We verified this
directly in the corpus GOA: every `GO_REF:0000118` row is `IEA` / `TreeGrafter`
/ `PANTHER`.) Note also that `GO_REF:0000120` is UniProt's "combined multiple
IEA methods" reference (InterPro / ARBA / RHEA / UniRule / …) — only a handful
of its rows are PANTHER-derived — so it is **excluded** from the TreeGrafter set.

This project evaluates how good those automated TreeGrafter inferences are when
each is held to standard GO review criteria, using the AIGR corpus of
expert/AI-adjudicated gene reviews as the gold standard.

## Method

Each `genes/*/*/*-ai-review.yaml` records, per existing annotation, an
`evidence_type`, an `original_reference_id`, and a reviewer `action` from the
AIGR action enum (`ACCEPT`, `KEEP_AS_NON_CORE`, `MODIFY`,
`MARK_AS_OVER_ANNOTATED`, `REMOVE`, `UNDECIDED`, …). We treat the AIGR
adjudication as the reference judgement and ask how the annotations with
`evidence_type: IEA` and `original_reference_id: GO_REF:0000118` (TreeGrafter)
were treated. The PAINT/IBA set (`GO_REF:0000033`) is reported alongside purely
as a **contrast** — it is a different, curator-driven pipeline.

Reproduce with:

```bash
python3 projects/TREEGRAFTER/analyze_treegrafter.py
# or, hermetically:
uv run --with pyyaml projects/TREEGRAFTER/analyze_treegrafter.py
```

This writes two committed sidecars (no hard-coded numbers):

- [`TREEGRAFTER/treegrafter_review.tsv`](TREEGRAFTER/treegrafter_review.tsv) — one row per reviewed TreeGrafter annotation (gene, taxon, term, action).
- [`TREEGRAFTER/treegrafter_summary.tsv`](TREEGRAFTER/treegrafter_summary.tsv) — action counts (TreeGrafter and the IBA contrast) and the most frequently down-graded TreeGrafter terms.

## Results (current corpus snapshot)

Scanned **2,775** review files. **415** reviewed TreeGrafter annotations
(`GO_REF:0000118`) across **202** genes.

| Reviewer action | TreeGrafter (IEA) | | PAINT/IBA *(contrast)* | |
|---|---:|---:|---:|---:|
| `ACCEPT` | 170 | 41.0% | 4,838 | 73.1% |
| `KEEP_AS_NON_CORE` | 72 | 17.3% | 989 | 14.9% |
| `MODIFY` | 52 | 12.5% | 327 | 4.9% |
| `REMOVE` | 69 | 16.6% | 195 | 2.9% |
| `MARK_AS_OVER_ANNOTATED` | 38 | 9.2% | 191 | 2.9% |
| `UNDECIDED` | 10 | 2.4% | 38 | 0.6% |
| `NEW` / `PENDING` | 4 | 1.0% | 39 | 0.6% |

**Headline:** only **~41%** of TreeGrafter inferences are accepted as-is, and
**~26%** are outright rejected (`REMOVE` + `MARK_AS_OVER_ANNOTATED`), with a
further ~12.5% needing a better term (`MODIFY`). This is **markedly noisier than
curated PAINT/IBA** on the same corpus (73% accept, ~6% rejected) — which is
exactly what you would expect: TreeGrafter is fully automated propagation onto
sequences that were *not* curated into the reference tree, with no curator
checking residue-level evidence at the graft point.

### Where TreeGrafter inferences fail

The TreeGrafter terms most often down-graded (`REMOVE` / `MODIFY` /
`MARK_AS_OVER_ANNOTATED`) cluster in two failure modes:

1. **Over-specific catalytic activity propagated to the wrong paralog/subfamily.**
   The grafting node carries a precise enzymatic MF that the query has diverged
   away from: `fatty acid synthase activity` (GO:0004312),
   `spermidine synthase activity` (GO:0004766),
   `phosphotransferase activity` (GO:0016776),
   `L-lactate dehydrogenase (NAD+) activity` (GO:0004459),
   `triacylglycerol lipase activity` (GO:0004806). TreeGrafter places a sequence
   on a tree node but cannot tell that the catalytic residues, or the whole
   substrate specificity, have changed — the classic paralog over-annotation.

2. **Generic / uninformative localization.** `cytoplasm` (GO:0005737),
   `cytosol` (GO:0005829), `plasma membrane` (GO:0005886), `membrane`
   (GO:0016020), `nucleus` (GO:0005634) — low-information CC terms inherited
   from distant ancestors.

There are also organism-mismatched BP propagations (e.g.
`lipopolysaccharide core region biosynthetic process`,
`sucrose biosynthetic process`) onto genes whose host lacks the pathway.

These are precisely the cases where automated tree grafting lacks the
gene-specific evidence (catalytic-residue conservation, substrate assays,
organism pathway context) that a curator brings — and why PAINT/IBA, where a
curator made the call, fares so much better.

## Caveats

- **Small n.** 415 TreeGrafter annotations across 202 genes — directional, not a
  frozen benchmark. The 95% Wald interval on the 41% accept rate is roughly
  ±5 pp.
- The reference standard is the AIGR review corpus, which mixes expert and AI
  adjudication and is under continuous revision; treat rates as a living
  snapshot.
- `KEEP_AS_NON_CORE` is **not** an error — the inference is correct but
  peripheral to the gene's core function. Counting accept + non-core as
  "retained correct" gives ~58% for TreeGrafter vs ~88% for IBA.
- A few annotations are still `PENDING`/`UNREVIEWED` in partially-reviewed
  genes.

## Next steps

- Break the TreeGrafter rates down by GO **aspect** (MF / BP / CC) — hypothesis:
  the over-specific MF propagations are the single worst category.
- Cluster failures by PANTHER family/subfamily id (from `WITH/FROM`) to find
  families where TreeGrafter systematically over-reaches — candidate subfamily
  split / PAINT curation targets to feed upstream.
- Contrast against `IEA` / `GO_REF:0000002` (InterPro2GO) on the same genes:
  phylogenetic grafting vs. signature-based transfer.
