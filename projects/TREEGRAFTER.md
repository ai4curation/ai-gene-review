---
title: "TreeGrafter Inference Evaluation"
maturity: IN_PROGRESS
tags: [EVALUATION, PIPELINE]
sidecars:
  per_annotation: TREEGRAFTER/treegrafter_review.tsv
  summary: TREEGRAFTER/treegrafter_summary.tsv
  placement: TREEGRAFTER/treegrafter_placement.tsv
  graft_check: TREEGRAFTER/treegrafter_graft_check.tsv
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
IEA methods" reference (InterPro / ARBA / RHEA / UniRule / …). It is
**excluded** from the TreeGrafter set because the method behind each row is not
identifiable — but it is *not* a negligible source: in this corpus about 12% of
its rows (891 of ~7,200) carry a `PANTHER:PTN…` `WITH/FROM`, i.e. they are
PANTHER-tree inferences re-issued under UniProt's combined reference, and there
are as many of them as there are `GO_REF:0000118` rows (898). The rates below
therefore describe the *explicitly labelled* TreeGrafter output; the
UniProt-relayed PANTHER rows are an untested second population (see next steps).

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

Scanned **4,540** review files. **898** reviewed TreeGrafter annotations
(`GO_REF:0000118`) across **510** genes — every `GO_REF:0000118` row in the
corpus GOA now has a review decision (previous snapshot: 415 annotations /
202 genes, before the *P. putida* KT2440 batch was reviewed).

| Reviewer action | TreeGrafter (IEA) | | PAINT/IBA *(contrast)* | |
|---|---:|---:|---:|---:|
| `ACCEPT` | 371 | 41.3% | 7,286 | 71.7% |
| `KEEP_AS_NON_CORE` | 192 | 21.4% | 1,611 | 15.9% |
| `MODIFY` | 73 | 8.1% | 478 | 4.7% |
| `REMOVE` | 120 | 13.4% | 276 | 2.7% |
| `MARK_AS_OVER_ANNOTATED` | 113 | 12.6% | 432 | 4.3% |
| `UNDECIDED` | 26 | 2.9% | 45 | 0.4% |
| `NEW` / `PENDING` | 3 | 0.3% | 36 | 0.4% |

**Headline:** only **~41%** of TreeGrafter inferences are accepted as-is, and
**~26%** are outright rejected (`REMOVE` + `MARK_AS_OVER_ANNOTATED`), with a
further ~8% needing a better term (`MODIFY`). The accept rate was 41.0% at the
previous 415-annotation snapshot, so it has been stable while the corpus more
than doubled. This is **markedly noisier than curated PAINT/IBA** on the same
corpus (72% accept, ~7% rejected) — which is
exactly what you would expect: TreeGrafter is fully automated propagation onto
sequences that were *not* curated into the reference tree, with no curator
checking residue-level evidence at the graft point.

### By GO aspect

The summary sidecar also breaks the TreeGrafter set down by aspect (taken
from the `GO ASPECT` column of each gene's cached GOA). Molecular-function
propagations are the worst category by a wide margin, confirming the
hypothesis that catalysis-implying MF terms are where tree grafting
over-reaches; CC terms are rarely *wrong* but are mostly parked as non-core.

| Aspect | n | `ACCEPT` | `KEEP_AS_NON_CORE` | down-graded (`REMOVE`+`MODIFY`+`OVER`) |
|---|---:|---:|---:|---:|
| Molecular function | 238 | 30% | 13% | **52%** |
| Biological process | 318 | 41% | 17% | 38% |
| Cellular component | 342 | 49% | 31% | 18% |

### Where TreeGrafter inferences fail

> **Deep dive:** [Failure Modes & Tree Placement](TREEGRAFTER/failure-modes.md)
> joins every down-graded annotation to the PANTHER family/subfamily it was
> grafted onto (and the ancestral `PTN` graft node), to answer whether the
> *placement* or the *propagated term* is at fault. **Short answer: the
> placement is usually fine; the inherited term is too coarse, assumes lost
> catalysis, or is a generic localization** — only a handful (e.g. `aprA`,
> `fcs`) are true within-superfamily mis-placements.

The TreeGrafter terms most often down-graded (`REMOVE` / `MODIFY` /
`MARK_AS_OVER_ANNOTATED`) cluster in two failure modes:

1. **Over-specific catalytic activity propagated to the wrong paralog/subfamily.**
   The grafting node carries a precise enzymatic MF that the query has diverged
   away from: `NADH dehydrogenase activity` (GO:0003954),
   `fatty acid synthase activity` (GO:0004312),
   `spermidine synthase activity` (GO:0004766),
   `phosphotransferase activity` (GO:0016776),
   `carotenoid dioxygenase activity` (GO:0010436),
   `(S)-2-hydroxyglutarate dehydrogenase activity` (GO:0047545),
   `triacylglycerol lipase activity` (GO:0004806). TreeGrafter places a sequence
   on a tree node but cannot tell that the catalytic residues, or the whole
   substrate specificity, have changed — the classic paralog over-annotation.

2. **Generic / uninformative localization.** `cytoplasm` (GO:0005737),
   `cytosol` (GO:0005829), `plasma membrane` (GO:0005886), `membrane`
   (GO:0016020), `nucleus` (GO:0005634) — low-information CC terms inherited
   from distant ancestors. `cytosol` and `cytoplasm` alone are the two most
   frequently down-graded TreeGrafter terms in the corpus. The MF analogue is
   `identical protein binding` (GO:0042802), an uninformative
   "it oligomerises" term propagated from the tree.

There are also process-level mis-propagations of two kinds: a mechanistically
wrong sibling process (`lipopolysaccharide core region biosynthetic process`
on the `mcr` phosphoethanolamine transferases, which modify lipid A, not the
core oligosaccharide), and pathway terms propagated onto hosts that lack the
pathway (`sucrose biosynthetic process` on *P. putida* `fbp`).

These are precisely the cases where automated tree grafting lacks the
gene-specific evidence (catalytic-residue conservation, substrate assays,
organism pathway context) that a curator brings — and why PAINT/IBA, where a
curator made the call, fares so much better.

## Caveats

- **Corpus composition.** 898 TreeGrafter annotations across 510 genes, but
  ~70% of them come from the *Pseudomonas putida* KT2440 batch (see the
  per-taxon table in the summary sidecar), so the rates are largely a
  *P. putida* result; the 95% Wald interval on the 41% accept rate is roughly
  ±3 pp, but the taxon skew matters more than the sampling error. Directional,
  not a frozen benchmark.
- The reference standard is the AIGR review corpus, which mixes expert and AI
  adjudication and is under continuous revision; treat rates as a living
  snapshot.
- `KEEP_AS_NON_CORE` is **not** an error — the inference is correct but
  peripheral to the gene's core function. Counting accept + non-core as
  "retained correct" gives ~63% for TreeGrafter vs ~88% for IBA.
- A few annotations are still `PENDING`/`UNREVIEWED` in partially-reviewed
  genes.

## Deeper analyses

- **[Failure Modes & Tree Placement](TREEGRAFTER/failure-modes.md)** — joins all
  306 down-graded annotations to their PANTHER graft point, plus a lightweight
  PANTHER-vs-InterPro [graft check](TREEGRAFTER/graft_check.py) on five
  exemplars. Key result: the placement is usually sound; the error is the GO term
  attached to the graft node, and **InterPro often resolves the protein better
  than PANTHER** (e.g. `IPR011803 AprA`, `IPR003083 S-crystallin`).
- **OpenScientist blinded verification** uses a dedicated TreeGrafter prompt
  template,
  [`templates/treegrafter_function_hypothesis.md`](https://github.com/ai4curation/ai-gene-review/blob/main/templates/treegrafter_function_hypothesis.md),
  which frames each propagated term as a blinded "GENE has *<term>*" hypothesis
  and instructs the agent to actively test the three failure modes
  (granularity, pseudo-enzyme, mis-placement). Run via
  `gene-hypothesis-research openscientist <org> <gene> --annotation-term-id <GO>
  --as-function-hypothesis --template templates/treegrafter_function_hypothesis.md`.

---
# NOTES

## 2026-09-06

- Review pass over the project. The committed sidecars predated the
  *P. putida* KT2440 batch: regenerated them (corpus 2,775 → 4,540 review
  files; TreeGrafter set 415 → 898 annotations, now covering every
  `GO_REF:0000118` row in the corpus GOA). Accept rate unchanged at ~41%,
  `MODIFY` share fell (12.5% → 8%) and `KEEP_AS_NON_CORE` rose (17% → 21%).
- Corrected the `GO_REF:0000120` paragraph (it is not a "handful" of PANTHER
  rows — ~890, as many as the labelled TreeGrafter set) and the description of
  the `mcr` LPS-core error (sibling-process error, not host-lacks-pathway).
- Fixed the `templates/…` links, which resolved above the site root when
  rendered; removed the hard-coded scratch path from `run_falcon.sh`.
- `analyze_treegrafter.py` now uses the C YAML loader (minutes → ~45 s) and
  emits the action-by-aspect and per-taxon breakdowns added above.
- Verified the exemplar provenance: all ten OpenScientist and Falcon blinded
  reports and the ten Falcon family reports exist under the gene
  `*-hypotheses/` and `interpro/panther/PTHR*/` directories, and their verdict
  lines match the tables on the failure-modes page.

## Next steps

- **Contrast against `IEA` / `GO_REF:0000002` (InterPro2GO)** on the same genes —
  the graft check suggests signature-based transfer would *out-resolve* the
  phylogenetic graft for several of these proteins; quantify how often.
- Hand-classify the ~150 down-grades added by the *P. putida* batch into the
  four failure modes on the failure-modes page (the mode tables there were
  curated on the earlier 159-case snapshot).
- Evaluate the **UniProt-relayed PANTHER rows** (`GO_REF:0000120` with a
  `PANTHER:PTN…` `WITH/FROM`, ~890 rows in this corpus) with the same method —
  they are probably the same TreeGrafter inferences under a different reference
  and are currently excluded.
- Cluster failures by PANTHER family/subfamily id (from `WITH/FROM`) to find
  families where TreeGrafter systematically over-reaches — candidate subfamily
  split / PAINT curation targets to feed upstream.
