---
title: "TreeGrafter Inference Evaluation"
maturity: IN_PROGRESS
tags: [EVALUATION, PIPELINE]
sidecars:
  per_annotation: TREEGRAFTER/treegrafter_review.tsv
  summary: TREEGRAFTER/treegrafter_summary.tsv
  placement: TREEGRAFTER/treegrafter_placement.tsv
  graft_check: TREEGRAFTER/treegrafter_graft_check.tsv
  rejection_rereview: TREEGRAFTER/rereview-2026-09-24/summary.tsv
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

Scanned **4,974** review files. **968** reviewed TreeGrafter annotations
(`GO_REF:0000118`) across **540** genes. These numbers are *after* the
2026-09-24 rejection re-review below; the first-pass snapshot (415 rows, 202
genes, 41% accept, 26% rejected) is preserved in the git history of the
sidecars.

| Reviewer action | TreeGrafter (IEA) | | PAINT/IBA *(contrast)* | |
|---|---:|---:|---:|---:|
| `ACCEPT` | 466 | 48.1% | 8,087 | 73.1% |
| `KEEP_AS_NON_CORE` | 229 | 23.7% | 1,754 | 15.8% |
| `MODIFY` | 76 | 7.9% | 458 | 4.1% |
| `REMOVE` | 88 | 9.1% | 191 | 1.7% |
| `MARK_AS_OVER_ANNOTATED` | 47 | 4.9% | 329 | 3.0% |
| `UNDECIDED` | 62 | 6.4% | 217 | 2.0% |
| `NEW` / `PENDING` | 0 | 0.0% | 33 | 0.3% |

**Headline:** **~48%** of TreeGrafter inferences are accepted as-is and a
further ~24% are correct but peripheral (`KEEP_AS_NON_CORE`), so ~72% are
retained as correct; **~14%** are rejected (`REMOVE` +
`MARK_AS_OVER_ANNOTATED`) and ~8% need a better term (`MODIFY`). That is still
**noisier than curated PAINT/IBA** on the same corpus (73% accept, 89%
retained, ~5% rejected) — as expected for fully automated propagation onto
sequences that were *not* curated into the reference tree, with no curator
checking residue-level evidence at the graft point — but the gap is
substantially smaller than the first pass suggested, because a large share of
the first-pass rejections did not survive re-examination (see below).

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
   away from: `fatty acid synthase activity` (GO:0004312),
   `spermidine synthase activity` (GO:0004766),
   `phosphotransferase activity` (GO:0016776),
   `L-lactate dehydrogenase (NAD+) activity` (GO:0004459),
   `triacylglycerol lipase activity` (GO:0004806). TreeGrafter places a sequence
   on a tree node but cannot tell that the catalytic residues, or the whole
   substrate specificity, have changed — the classic paralog over-annotation.
   This is the failure mode that survives scrutiny intact.

2. **Whole-complex activity on a single subunit.** `NADH dehydrogenase
   activity` (GO:0003954) on six complex I subunits that lack the NADH site is
   now the single most down-graded term; the right fix is `MODIFY` to the
   complex activity with a `contributes_to` qualifier, not removal.

3. **Generic / uninformative localization** — `cytoplasm` (GO:0005737),
   `cytosol` (GO:0005829), `membrane` (GO:0016020), `nucleus` (GO:0005634).
   The re-review found most of these are *true* and had been rejected only for
   redundancy; they are a real failure only where the location is incompatible
   with the protein (a secreted or exported product).

There are also organism-mismatched BP propagations (e.g.
`lipopolysaccharide core region biosynthetic process`,
`polysaccharide biosynthetic process` on epimerases that form no glycosidic
bond) onto genes whose host lacks the pathway or whose product merely feeds it.

These are precisely the cases where automated tree grafting lacks the
gene-specific evidence (catalytic-residue conservation, substrate assays,
organism pathway context) that a curator brings — and why PAINT/IBA, where a
curator made the call, fares better.

## Caveats

- **Moderate n.** 968 TreeGrafter annotations across 540 genes — directional,
  not a frozen benchmark. The 95% Wald interval on the 48% accept rate is
  roughly ±3 pp.
- The reference standard is the AIGR review corpus, which mixes expert and AI
  adjudication and is under continuous revision; treat rates as a living
  snapshot. The first-pass reviews over-rejected (see the re-review), so the
  rates for *unaudited* actions should be read with that bias in mind.
- `KEEP_AS_NON_CORE` is **not** an error — the inference is correct but
  peripheral to the gene's core function. Counting accept + non-core as
  "retained correct" gives ~72% for TreeGrafter vs ~89% for IBA.
- `UNDECIDED` (6%) is honest uncertainty, mostly on proteins with no
  substrate assay; it counts neither for nor against TreeGrafter.

## Rejection re-review (2026-09-24)

The rejection rate above is only meaningful if the rejections themselves hold
up, so every TreeGrafter row marked `REMOVE` or `MARK_AS_OVER_ANNOTATED` was
re-examined against a fixed rule set (positive contrary evidence required for
`REMOVE`; broad-but-true terms are not over-annotations; too-coarse ancestors
are `MODIFY`, not `REMOVE`; term definitions checked in QuickGO). Records,
rules, and a generated summary live in
[`TREEGRAFTER/rereview-2026-09-24/`](TREEGRAFTER/rereview-2026-09-24/README.md);
the nine genes already re-audited on 2026-09-20 were left as recorded there.

**192 rejected rows across 165 genes: 114 (59%) stand, 78 (41%) were relaxed.**

| Previous → new action | n |
|---|---:|
| `REMOVE` → `REMOVE` | 76 |
| `MARK_AS_OVER_ANNOTATED` → `MARK_AS_OVER_ANNOTATED` | 38 |
| `MARK_AS_OVER_ANNOTATED` → `ACCEPT` | 30 |
| `MARK_AS_OVER_ANNOTATED` → `KEEP_AS_NON_CORE` | 25 |
| `REMOVE` → `MARK_AS_OVER_ANNOTATED` | 7 |
| `MARK_AS_OVER_ANNOTATED` → `MODIFY` | 6 |
| `REMOVE` → `UNDECIDED` | 4 |
| `REMOVE` → `MODIFY` | 3 |
| `REMOVE` → `KEEP_AS_NON_CORE` / `ACCEPT` | 3 |

The relaxations are concentrated, and they say more about the *first-pass
reviews* than about TreeGrafter:

- **Redundant locations (24 of 78).** `cytosol`/`cytoplasm` on soluble
  bacterial enzymes had been marked over-annotated purely because a sibling
  location row existed. A broad true term is not an error; these are now
  `ACCEPT` or `KEEP_AS_NON_CORE`. The generic-localization "failure mode"
  listed above therefore shrinks: it is real only where the location is
  *incompatible* with the protein (secreted cystatin `cpi-2`, exported
  flagellar hook `flgE`, periplasmic `alr`), and those rejections stand.
- **True ancestors of an accepted term (~20).** `oxidoreductase activity` on
  betA, `glycosyltransferase activity` on murG, `protein transport` on
  secD/secF, `deaminase activity` on guaD, and the like; verified by QuickGO
  ancestry and restored. The six complex I subunits carrying `NADH
  dehydrogenase activity` became `MODIFY` → `GO:0008137` (contributes_to).
- **Rejections resting only on "no target-specific assay" (~12).** Absence of
  a target experiment does not refute a supported phylogenetic inference;
  these moved to `MARK_AS_OVER_ANNOTATED` or, where the substrate is
  genuinely unknown (ptxD, retS, TFP nucleus), `UNDECIDED`.
- **Label read instead of definition (1, but instructive).** `GO:0009329
  "acetate CoA-transferase complex"` on PSEPK/accD was removed as a different
  enzyme; its definition is the AccA/AccD carboxyltransferase component of
  acetyl-CoA carboxylase, so the TreeGrafter call was *more* specific than the
  term the gene already carried. The term's label and its `capable_of` axiom
  contradict its own definition — worth raising with GO.

The 114 retained rejections all rest on stated chemistry, architecture, or
organism evidence, and about a third had their `reason` strengthened with the
specific evidence (EC numbers, PANTHER subfamily vs. graft node, cached
substrate-panel quotes). That leaves the **paralog / wrong-subfamily
catalytic-activity transfers as the one failure mode that survives scrutiny
intact** — e.g. spermidine synthase on the PMT methyltransferases, carotenoid
dioxygenase on the lignostilbene dioxygenases, lactate dehydrogenase on
malate dehydrogenases, cysteine synthase vs. O-acetylhomoserine sulfhydrylase.

Follow-ups surfaced by the re-review: the duplicate `aroQ` / `aroQ-III`
folders (both Q88IJ6 / PP_3003) have since been merged into `PSEPK/aroQ-III`,
the name UniProt gives the locus. Still open — benB carries an `IC`
annotation to the obsolete `GO:0043640`, and a few relaxed ancestors now sit
beside sibling rows (ubiA `GO:0004659`/`GO:0016765`, zwf `GO:0006098`) that
were out of scope and may warrant harmonizing.

## Deeper analyses

- **[Failure Modes & Tree Placement](TREEGRAFTER/failure-modes.md)** — joins all
  159 down-graded annotations to their PANTHER graft point, plus a lightweight
  PANTHER-vs-InterPro [graft check](TREEGRAFTER/graft_check.py) on five
  exemplars. Key result: the placement is usually sound; the error is the GO term
  attached to the graft node, and **InterPro often resolves the protein better
  than PANTHER** (e.g. `IPR011803 AprA`, `IPR003083 S-crystallin`).
- **OpenScientist blinded verification** uses a dedicated TreeGrafter prompt
  template,
  [`templates/treegrafter_function_hypothesis.md`](../../templates/treegrafter_function_hypothesis.md),
  which frames each propagated term as a blinded "GENE has *<term>*" hypothesis
  and instructs the agent to actively test the three failure modes
  (granularity, pseudo-enzyme, mis-placement). Run via
  `gene-hypothesis-research openscientist <org> <gene> --annotation-term-id <GO>
  --as-function-hypothesis --template templates/treegrafter_function_hypothesis.md`.

## Next steps

- Fold in the OpenScientist verdicts for the five exemplars once the runs
  complete (see failure-modes page).
- **Contrast against `IEA` / `GO_REF:0000002` (InterPro2GO)** on the same genes —
  the graft check suggests signature-based transfer would *out-resolve* the
  phylogenetic graft for several of these proteins; quantify how often.
- Break the TreeGrafter rates down by GO **aspect** (MF / BP / CC) — hypothesis:
  the over-specific MF propagations are the single worst category.
- Cluster failures by PANTHER family/subfamily id (from `WITH/FROM`) to find
  families where TreeGrafter systematically over-reaches — candidate subfamily
  split / PAINT curation targets to feed upstream. The 2026-09-24 re-review
  narrows this to the retained paralog-transfer set, which is the right input.
- Harmonize the out-of-scope sibling rows and the remaining data hygiene item
  listed under the rejection re-review (benB obsolete `GO:0043640` IC row).
