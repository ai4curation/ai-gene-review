---
title: "TreeGrafter Inference Evaluation"
collections: [HOMOLOGY_PROPAGATION, FUNCTION_PREDICTION]
maturity: MATURE
tags: [EVALUATION, PIPELINE]
# Bare symbols here span many species (aprA is Desulfovibrio, pepV is P. putida,
# "FAS"/"ArgE" are family names), so prose auto-linking mis-targets; keep it off.
autolink_gene_symbols: false
sidecars:
  per_annotation: TREEGRAFTER/treegrafter_review.tsv
  summary: TREEGRAFTER/treegrafter_summary.tsv
  placement: TREEGRAFTER/treegrafter_placement.tsv
  graft_check: TREEGRAFTER/treegrafter_graft_check.tsv
  contrast: TREEGRAFTER/treegrafter_contrast.tsv
  family_hotspots: TREEGRAFTER/treegrafter_family_hotspots.tsv
  failure_modes: TREEGRAFTER/treegrafter_failure_modes.tsv
  failure_mode_curated: TREEGRAFTER/failure_mode_curated.tsv
  snapshot_drift: TREEGRAFTER/treegrafter_snapshot_drift.tsv
  exemplar_independence: TREEGRAFTER/exemplar_independence.tsv
  # Deck images: copied beside the rendered deck so its relative <img> paths resolve.
  slide_images:
    - TREEGRAFTER/slides/treegrafter-graft.svg
    - TREEGRAFTER/slides/treegrafter-results.svg
manifest:
  slides:
    - href: TREEGRAFTER/slides/TREEGRAFTER-slides.html
      description: AI generated
  artifacts:
    - href: https://claude.ai/artifact/Wi9WbyuGcFMPSKNmXX1UoP
      title: Project brief
---

# TreeGrafter Inference Evaluation

**Bottom line:** TreeGrafter grafts a protein that is not in a PANTHER reference
tree onto the best-matching node and copies that node's GO terms to it as IEA
annotations (`GO_REF:0000118`), with no curator in the loop. We took every such
annotation in the review corpus at commit `943b98815` (998 annotations on 560
reviewed proteins) and tallied how reviewers treated them, alongside the
curated PAINT/IBA set as a contrast. Reviewers accepted 44.6% of TreeGrafter
annotations as-is, removed 11.2% outright and down-graded 30.0% in all
(`REMOVE`, `MODIFY` or `MARK_AS_OVER_ANNOTATED`), against 73.0% accepted for
PAINT/IBA; molecular-function terms fared worst, with 49.3% down-graded. When
another pipeline reproduced the same TreeGrafter call (`GO_REF:0000120`)
acceptance rose to 78%, though reviewers could see that label. In about four
of five down-graded cases the tree placement was sound and the inherited term
was the problem (too coarse, a sibling term, or a generic localization). The
errors cluster by family: 27 of the 72 PANTHER families with at least four
reviewed annotations had half or more of their terms down-graded.

We did this because TreeGrafter output is routinely conflated with curated
PAINT/IBA, and knowing where automated grafting over-reaches gives PANTHER and
PAINT curators concrete families to fix. 69% of the rows come from the
*Pseudomonas putida* KT2440 batch, so the rates are directional, and they are
pinned to a commit because the corpus keeps growing.

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
/ `PANTHER`.)

One more reference matters, and it changes what the `GO_REF:0000118` set *is*.
`GO_REF:0000120` is UniProt's **"Combined Automated Annotation using Multiple
IEA Methods"**: per its GO reference-collection definition it "integrates
identical annotations from multiple electronic pipelines, including UniRule,
ARBA, InterPro2GO, TreeGrafter2GO (GO_REF:0000118), RHEA2GO, KeyWord2GO,
SubCellular2GO, EC2GO and EnsEMBL Compara", listing the contributing pipelines
pipe-separated in `WITH/FROM`. In this corpus **every** `GO_REF:0000120` row
with a `PANTHER:PTN…` in `WITH/FROM` (965 rows in the cached GOA files at
`943b98815`; 891 at the 2026-09-06 snapshot) also lists at least one other
pipeline (InterPro in most cases), and **no reviewed protein has the same term
under both `GO_REF:0000118` and `GO_REF:0000002`** (0 shared pairs in the
summary sidecar). So the three electronic references
partition the predictions by corroboration:

| Reference | What the row means |
|---|---|
| `GO_REF:0000118` (TreeGrafter) | a TreeGrafter prediction that **no other pipeline reproduced** |
| `GO_REF:0000120` with `PANTHER:PTN…` | a TreeGrafter prediction **corroborated** by ≥1 other pipeline |
| `GO_REF:0000002` (InterPro2GO) | an InterPro2GO prediction that no other pipeline (TreeGrafter included) reproduced |

The headline rates below are therefore for the **uncorroborated** TreeGrafter
output. The corroborated set and the uncorroborated InterPro2GO set are
evaluated alongside it in [Corroboration](#corroboration-treegrafter-only-vs-multi-method-vs-interpro2go-only).

This project evaluates how good those automated TreeGrafter inferences are when
each is held to standard GO review criteria, using the AIGR corpus of
agent-written gene reviews as the reference standard (see
[Reference standard](#reference-standard)).

## Method

Each `genes/*/*/*-ai-review.yaml` records, per existing annotation, an
`evidence_type`, an `original_reference_id`, and a reviewer `action` from the
AIGR action enum (`ACCEPT`, `KEEP_AS_NON_CORE`, `MODIFY`,
`MARK_AS_OVER_ANNOTATED`, `REMOVE`, `UNDECIDED`, …). We treat the AIGR
adjudication as the reference judgement (see
[Reference standard](#reference-standard)) and ask how the annotations with
`evidence_type: IEA` and `original_reference_id: GO_REF:0000118` (TreeGrafter)
were treated. The PAINT/IBA set (`GO_REF:0000033`) is reported alongside purely
as a **contrast** — it is a different, curator-driven pipeline, on a largely
different set of genes.

Reproduce everything on this page (about three minutes; only `graft_check.py`
needs the network):

```bash
uv run --with pyyaml projects/TREEGRAFTER/analyze_treegrafter.py   # review/contrast/summary
python3 projects/TREEGRAFTER/analyze_placement.py                   # placement + family hotspots
uv run --with pyyaml projects/TREEGRAFTER/classify_failure_modes.py # failure modes
python3 projects/TREEGRAFTER/snapshot_drift.py                      # drift vs the 2026-09-06 snapshot
uv run --with pyyaml projects/TREEGRAFTER/exemplar_independence.py  # exemplar citation check
python3 projects/TREEGRAFTER/graft_check.py                         # live UniProt; or --refresh-actions offline
```

`analyze_treegrafter.py --out-dir DIR` writes its three sidecars elsewhere, so
the numbers can be checked against a newer tree without touching the committed
files. It writes:

- [`TREEGRAFTER/treegrafter_review.tsv`](TREEGRAFTER/treegrafter_review.tsv) — one row per reviewed TreeGrafter annotation (gene, taxon, term, aspect, action).
- [`TREEGRAFTER/treegrafter_contrast.tsv`](TREEGRAFTER/treegrafter_contrast.tsv) — one row per reviewed corroborated-PANTHER (`GO_REF:0000120`) and InterPro2GO (`GO_REF:0000002`) annotation on the review files that carry TreeGrafter rows.
- [`TREEGRAFTER/treegrafter_summary.tsv`](TREEGRAFTER/treegrafter_summary.tsv) — action counts for all populations; a *headline rates* block (accept, retained, `REMOVE`-only, `MODIFY`, `MARK_AS_OVER_ANNOTATED`, down-graded) per population and per aspect; per-taxon breakdown; most frequently down-graded terms.

`analyze_placement.py` joins each annotation to its PANTHER family / subfamily
/ graft node and writes
[`treegrafter_family_hotspots.tsv`](TREEGRAFTER/treegrafter_family_hotspots.tsv);
`classify_failure_modes.py` assigns every down-graded annotation a failure
mode and writes
[`treegrafter_failure_modes.tsv`](TREEGRAFTER/treegrafter_failure_modes.tsv)
(see the [failure-modes page](TREEGRAFTER/failure-modes.md)).

## Results (computed at commit `943b98815`, 2026-10-01)

> **Provenance.** Every number on this page and its sub-page comes from the
> sidecars regenerated on 2026-10-01 at commit **`943b98815`** with the
> commands above (the `genes/` tree was clean at that commit). The corpus keeps
> growing; re-run the commands rather than trusting these figures on a later
> tree, and re-curate `failure_mode_curated.tsv` whenever rows cross into or out
> of the down-graded set.

**5,287** review files were scanned, yielding **998** reviewed TreeGrafter
annotations (`GO_REF:0000118`) across **560** review files (540 distinct gene
symbols). No row is `PENDING`/`NEW`.

Relative to the previous refresh (2026-09-27; 983 annotations / 550 files),
15 annotations were added and 16 actions changed. The additions are 11
*P. putida* rows and the four TreeGrafter `GO:0046933` rows of the new
[rotary-ATPase case study](TREEGRAFTER/rotary-atpase-leak.md) (`fliI` in
CAUVC and HELPJ, `sctN` in SHIFL and YEREN; all `REMOVE`). Together with the
pre-existing PSEPK `fliI` row, all five TreeGrafter rows of that case are now
in every table below. The 16 changed actions are follow-up reviews of
OpenScientist reports on `fogD`, `K9IJK6`, `K9IMD0`, `K9IFT7`, `Cgas` and
`IRE1`; 15 of them were previously `UNDECIDED`.

### Drift since the 2026-09-06 snapshot

An earlier version of this page was frozen at a 2026-09-06 snapshot (898
annotations / 510 files, on `main` at `e3350f43d`).
[`snapshot_drift.py`](TREEGRAFTER/snapshot_drift.py) diffs the two
([`treegrafter_snapshot_drift.tsv`](TREEGRAFTER/treegrafter_snapshot_drift.tsv)):

| | count |
|---|---:|
| annotations added (PSEPK 61, HETGA 29, 9AVES 4, XENLA 2, CAUVC, HELPJ, SHIFL and YEREN 1 each) | 100 |
| annotations dropped | 0 |
| actions changed on already-counted annotations | 62 |
| down-graded (`REMOVE`+`MODIFY`+`OVER`) set | 306 → **299** |
| … rows that **left** the down-graded set | 37 (18 → `ACCEPT`, 13 → `UNDECIDED`, 6 → `KEEP_AS_NON_CORE`) |
| … rows that **entered** it | 30 (28 newly added, 2 changed: PSEPK `pgm`) |

Most of the drift comes from one event: the **2026-09-20 full-gene re-review**
recorded in [`TREEGRAFTER/rereview-2026-09-20/`](#re-review-of-2026-09-20)
(below), plus the follow-up reviews of its awaiting genes. 57 of the 62
changed actions, and all 37 rows that left the down-graded set, are on genes
in that folder. The most common transitions are `MODIFY` → `ACCEPT` (10
rows), `REMOVE` → `MARK_AS_OVER_ANNOTATED` (8) and `MARK_AS_OVER_ANNOTATED`
→ `ACCEPT` (7). `fogD` illustrates the path: the re-review moved its six
`REMOVE` rows to `UNDECIDED` rather than reject on pathway context alone, and
the later follow-up review settled them as `MODIFY` / `MARK_AS_OVER_ANNOTATED`
(four rows) and `KEEP_AS_NON_CORE` (two), so in the snapshot diff those four
stay down-graded.

### Headline

| Reviewer action | TreeGrafter (IEA) | | PAINT/IBA *(corpus-wide contrast; different genes)* | |
|---|---:|---:|---:|---:|
| `ACCEPT` | 445 | 44.6% | 9,096 | 73.0% |
| `KEEP_AS_NON_CORE` | 210 | 21.0% | 1,966 | 15.8% |
| `MODIFY` | 72 | 7.2% | 516 | 4.1% |
| `REMOVE` | 112 | 11.2% | 264 | 2.1% |
| `MARK_AS_OVER_ANNOTATED` | 115 | 11.5% | 353 | 2.8% |
| `UNDECIDED` | 44 | 4.4% | 230 | 1.8% |
| `NEW` / `PENDING` | 0 | 0% | 32 | 0.3% |
| *n* (review files) | 998 (560) | | 12,457 (3,205) | |

Three rates, reported side by side because they answer different questions
(all from the *headline rates* block of the summary sidecar):

| Rate | Definition | TreeGrafter | PAINT/IBA (corpus-wide) |
|---|---|---:|---:|
| accepted | `ACCEPT` | 44.6% | 73.0% |
| **retained** | `ACCEPT` + `KEEP_AS_NON_CORE` + `MARK_AS_OVER_ANNOTATED` — the term stays, possibly flagged | **77.2%** | 91.6% |
| **rejected** | `REMOVE` only | **11.2%** | 2.1% |
| down-graded | `REMOVE` + `MODIFY` + `MARK_AS_OVER_ANNOTATED` | 30.0% | 9.1% |

`MARK_AS_OVER_ANNOTATED` sits in both *retained* and *down-graded* on
purpose: the term is not wrong, but it is flagged as over-reaching. Read
together: roughly one TreeGrafter inference in ten is judged wrong outright,
about three in four survive in some form, and fewer than half are accepted
as-is. The accept rate was 41.0% at an earlier 415-annotation snapshot,
41.3% at the 2026-09-06 snapshot and 45.1% at the 2026-09-27 refresh; the
rise since the snapshot is mostly the 2026-09-20 re-review above, not new
data. The small fall to 44.6% since 2026-09-27 is the 15 added rows (3
accepted, 8 down-graded); the follow-up reviews mostly moved rows out of
`UNDECIDED`, 12 of them into the down-graded set.

**The PAINT/IBA column is not a like-for-like comparison.** It is every IBA row
in the corpus (3,205 review files, dominated by human and model-organism
genes), while TreeGrafter by construction annotates sequences that are *not*
in the PANTHER reference tree — so the two populations barely share genes.
Restricted to the same 560 review files, there are only **20** IBA rows on 9
files (16 `ACCEPT`, 3 `KEEP_AS_NON_CORE`, 1 `UNDECIDED`): too few to say
anything. The contrast shows that curated IBA on well-studied genes fares
better than automated grafting on non-model genes; it does not isolate the
effect of the pipeline from the effect of the gene set. The
[corroboration contrast](#corroboration-treegrafter-only-vs-multi-method-vs-interpro2go-only)
below, which *is* on the same files, is the better-controlled comparison.

### By GO aspect

Molecular-function propagations are the worst category by a wide margin (one
in five MF rows is removed outright); CC terms are rarely *wrong* but are
often parked as non-core.

| Aspect | n | `ACCEPT` | `KEEP_AS_NON_CORE` | `REMOVE` | down-graded (`REMOVE`+`MODIFY`+`OVER`) | retained |
|---|---:|---:|---:|---:|---:|---:|
| Molecular function | 270 | 32.2% | 13.3% | 21.1% | **49.3%** | 59.3% |
| Biological process | 358 | 46.1% | 16.5% | 10.6% | 31.8% | 76.0% |
| Cellular component | 370 | 52.2% | 31.1% | 4.6% | 14.1% | 91.4% |

### Corroboration: TreeGrafter-only vs multi-method vs InterPro2GO-only

Each population below is restricted to the 560 review files that carry
TreeGrafter rows, but covers only the subset of those files that carry it
(403 and 393 files respectively), so the three are close to — not exactly —
the same proteins:

| Population | n (files) | `ACCEPT` | `KEEP_AS_NON_CORE` | `REMOVE` | down-graded | retained |
|---|---:|---:|---:|---:|---:|---:|
| TreeGrafter, **uncorroborated** (`GO_REF:0000118`) | 998 (560) | 45% | 21% | 11.2% | 30% | 77% |
| TreeGrafter **corroborated** by ≥1 other pipeline (`GO_REF:0000120`, `PANTHER:PTN…`) | 695 (403) | **78%** | 9% | 0.7% | **11%** | 92% |
| InterPro2GO, **uncorroborated** (`GO_REF:0000002`) | 796 (393) | 29% | 19% | 6.5% | **50%** | 79% |

Three things follow:

1. **Corroboration is the strongest single predictor of a good TreeGrafter
   call.** The same algorithm's output is accepted 78% of the time when another
   pipeline reproduces it and 45% when none does. UniProt's `GO_REF:0000120`
   merge is, in effect, already a QC gate, and the `GO_REF:0000118` residue is
   the part that failed it.

   > **Caveat — the reviewers were not blind to the label.** `original_reference_id`
   > is visible in the review YAML while the annotation is being adjudicated, and
   > "combined multiple IEA methods" (`GO_REF:0000120`) reads as visibly stronger
   > provenance than a lone `GO_REF:0000118`. So the 78%-vs-45% gap may be partly
   > *caused by* the label rather than only *predicted* by it. The direction of the
   > effect is very likely real — corroboration by an independent pipeline is
   > genuine evidence — but the magnitude should not be taken at face value from
   > this corpus; treat it as an upper bound until the provenance-blinded test in
   > Next steps is run.
2. **Uncorroborated InterPro2GO is down-graded more often than uncorroborated
   TreeGrafter** — 50% (55% for MF) — but mostly by `MARK_AS_OVER_ANNOTATED`
   (31%); its `REMOVE` rate (6.5%) is *lower* than TreeGrafter's (11.2%), and
   its retained rate is similar (79% vs 77%). Its down-graded terms are
   dominated by coarse ancestors — `catalytic activity` (45), `membrane` (23),
   `oxidoreductase activity` (21), `nucleotide binding` (15). So InterPro2GO's
   uncorroborated residue is mostly *uninformative*, while TreeGrafter's is
   more often *wrong*. This qualifies the graft-check hypothesis on the
   failure-modes page: InterPro *does* out-resolve PANTHER for particular
   proteins (AprA, S-crystallin, Mcr1), but the informative InterPro2GO calls
   have mostly already been merged into `GO_REF:0000120`.
3. **Taxon composition.** TreeGrafter's down-grade rate is now similar on the
   *P. putida* KT2440 rows (29.3%, 202/689) and elsewhere (31.4%, 97/309);
   at the 2026-09-06 snapshot it was 31% vs 42%. InterPro2GO is down-graded
   55.9% on *P. putida* and 35.1% elsewhere (the *P. putida* reviews were
   strict about generic MF terms). Computed from the `taxon` column of the
   review and contrast sidecars.

### Where TreeGrafter inferences fail

> **Deep dive:** [Failure Modes & Tree Placement](TREEGRAFTER/failure-modes.md)
> joins every down-graded annotation to the PANTHER family/subfamily it was
> grafted onto (and the ancestral `PTN` graft node), and assigns each one a
> failure mode. **Short answer: in about four cases out of five the placement
> is fine and the inherited term is the problem** — too coarse or a sibling
> term from the family node (50%), or a generic / out-of-context localization
> or process (31%). About one in eight (37 annotations on 24 proteins, e.g.
> `aprA`, `fcs`, `mdh`, `mqo1–3`, `dapE`) is a within-superfamily
> mis-placement, and genuine pseudo-enzymes are rare (4 annotations, 2
> proteins).

| Failure mode | annotations | share | proteins |
|---|---:|---:|---:|
| 1 Granularity — right subfamily, family/node-level or sibling term | 149 | 50% | 122 |
| 3 Generic / out-of-context CC, binding or process term *(informativeness policy)* | 93 | 31% | 85 |
| 4 Within-superfamily mis-placement | 37 | 12% | 24 |
| 0 Unclassified — heuristic declines to guess (curation queue) | 16 | 5% | 14 |
| 2 Pseudo-enzyme / co-opted fold | 4 | 1% | 2 |
| *total down-graded* | *299* | | |

**Mode 3 is not a grafting error.** It records a reviewer *informativeness
policy* — generic CC terms (`cytosol`, `cytoplasm`, `membrane`), uninformative
binding terms and out-of-context process terms are down-graded because the
review standard prefers specific, core terms, not because the graft landed in
the wrong place or the term is false. 51 of the 93 are cellular-component rows
assigned by aspect alone. A different review policy would move most of mode 3
into *retained*; read the mode-1/2/4 counts (190 annotations, 64% of the
down-grades) as the grafting-attributable part.

The five rotary-ATPase rows (`fliI` ×3, `sctN` ×2, `GO:0046933`) are filed as
mode 1 by the operational rule on the sub-page (correct export-ATPase
subfamily, wrong term from a node above it); the
[case study](TREEGRAFTER/rotary-atpase-leak.md) traces that term to a PAINT
IBD placed on a duplication node.

Protein counts are distinct **review files**, not gene symbols — 560 files
carry only 540 symbols (`mdh`, `ALB`, `dapF` and others span more than one
file), so a symbol-keyed count reads modes 3 and 4 as 83 and 23.

The TreeGrafter terms most often down-graded cluster in two patterns:

1. **Over-specific catalytic activity propagated to the wrong paralog/subfamily.**
   The grafting node carries a precise enzymatic MF that the query has diverged
   away from: `NADH dehydrogenase activity` (GO:0003954, 6),
   `proton-transporting ATP synthase activity, rotational mechanism`
   (GO:0046933, 5; the rotary-ATPase case),
   `fatty acid synthase activity` (GO:0004312, 4),
   `phosphotransferase activity, phosphate group as acceptor` (GO:0016776, 4),
   `carotenoid dioxygenase activity` (GO:0010436, 4),
   `spermidine synthase activity` (GO:0004766, 3),
   `(S)-2-hydroxyglutarate dehydrogenase activity` (GO:0047545, 3).
   TreeGrafter places a sequence on a tree node but cannot tell that the
   catalytic residues, or the whole substrate specificity, have changed.
   (`triacylglycerol lipase activity` on `fogD` was re-reviewed to
   `UNDECIDED` on 2026-09-20 — the re-review found that the family source Ayr1
   does have lipase activity — and the later follow-up review marked it
   `MARK_AS_OVER_ANNOTATED`: the source activity is real, but FogD sits in a
   distinct subfamily with no hydrolase assay.)

2. **Generic / uninformative localization.** `cytosol` (GO:0005829, 18) and
   `cytoplasm` (GO:0005737, 9) are the two most frequently down-graded
   TreeGrafter terms; `membrane`, `nucleus` and `plasma membrane` follow. The
   MF analogue is `identical protein binding` (GO:0042802, 5).

There are also process-level mis-propagations of two kinds: a mechanistically
wrong sibling process (`lipopolysaccharide core region biosynthetic process`
on the `mcr` phosphoethanolamine transferases, which modify lipid A, not the
core oligosaccharide), and pathway terms propagated onto hosts that lack the
pathway (`sucrose biosynthetic process` on *P. putida* `fbp`).

### Family hotspots (upstream targets)

[`treegrafter_family_hotspots.tsv`](TREEGRAFTER/treegrafter_family_hotspots.tsv)
aggregates the reviewer outcome over *all* 998 TreeGrafter annotations per
PANTHER family, subfamily and graft node. Of the **72** families with at least
four reviewed annotations, **27 have half or more of their propagated terms
down-graded** and 22 have none — the errors are concentrated, not diffuse.
Families with ≥60% down-graded (modes counted from
`treegrafter_failure_modes.tsv`):

| Family | n | proteins | down-graded | modes of the down-graded rows | Example genes |
|---|---:|---:|---:|---|---|
| PTHR10543 beta-carotene dioxygenase | 8 | 4 | 100% | 4 ×8 — stilbene dioxygenases on the carotenoid-cleavage subfamily | Q53353, Saro_0802, Saro_2809, lsdB |
| PTHR30443 "inner membrane protein" (EptA) | 8 | 4 | 100% | 1 ×8 — EptA node carries `LPS core` and `phosphotransferase` | mcr-1, mcr2, mcr-3, mcr-4 |
| PTHR15184 ATP synthase | 5 | 5 | 100% | 1 ×5 — F-type ATP-synthase term on FliI/SctN export ATPases ([case study](TREEGRAFTER/rotary-atpase-leak.md)) | fliI ×3, sctN ×2 |
| PTHR21272 catabolic 3-dehydroquinase | 4 | 4 | 100% | 1 ×4 | aroQ, aroQ1, aroQ2, aroQ-III |
| PTHR42995 acetyl-CoA carboxylase carboxyl transferase | 4 | 2 | 100% | 1 ×3, 3 ×1 | accD, mdcD |
| PTHR43128 L-2-hydroxycarboxylate DH | 4 | 2 | 100% | 4 ×4 — MDH on the L-LDH subfamily | METEA/mdh, PSEPK/mdh |
| PTHR43775 fatty acid synthase | 4 | 4 | 100% | 1 ×4 — family-level FAS term on PKS subfamilies | eryAI–III, Pks1 |
| PTHR43808 acetylornithine deacetylase (M20A) | 5 | 3 | 80% | 4 ×4 | dapE, pepV |
| PTHR11485 transferrin | 4 | 1 | 75% | 3 ×3 — mammalian receptor-recycling localizations on salivary draculin | K9IMD0 |
| PTHR30435 flagellar protein | 4 | 2 | 75% | 3 ×2, 0 ×1 | flgE, flgG |
| PTHR11558 spermidine synthase | 9 | 3 | 67% | 1 ×6 — spermidine terms on the PMT subfamily | NaPMT3, PMT1, PMT2 |
| PTHR24241 neuropeptide receptor-related GPCR | 6 | 3 | 67% | 1 ×4 (heuristic) | CTR1, CTR2, OPR |
| PTHR44169 1-acyl-DHAP reductase (Ayr1) | 6 | 1 | 67% | 1 ×4 — Ayr1 lipid terms on the SrdE secondary-metabolite subfamily | fogD |
| PTHR21047 dTDP-sugar epimerase | 10 | 3 | 60% | 1 ×6 | eryBVII, rfbC, rmlC |
| PTHR11271 guanine deaminase | 5 | 2 | 60% | 1 ×3 | guaD, hutF |
| PTHR22960 molybdopterin cofactor synthesis | 5 | 3 | 60% | 1 ×3 | PP_1969, PP_2482, moaA |
| PTHR45527 nonribosomal peptide synthetase | 5 | 1 | 60% | 4 ×3 — EntF terms on the PvdD NRPS | pvdD |

Relative to the 2026-09-06 snapshot, three families are **no longer
hotspots**: PTHR48078 (`ilvA-I`/`ilvA-II`, 6/6 → 0/6 down-graded) after the
2026-09-20 re-review; PTHR11556 (FBPase, 7/11 → 1/11) and PTHR11632 (SDH
flavoprotein, 71% → 43%, `aprA` electron-transfer and plasma-membrane rows
now `ACCEPT`). PTHR44169 (`fogD`) went 6/6 → 0/6 at the 2026-09-20
re-review and is back at 4/6 after the follow-up review. PTHR15184
(rotary-ATPase rows) and PTHR11485 (`K9IMD0`, follow-up review) are new to
the table.

### Re-review of 2026-09-20

[`TREEGRAFTER/rereview-2026-09-20/`](https://github.com/ai4curation/ai-gene-review/tree/main/projects/TREEGRAFTER/rereview-2026-09-20)
holds the audit records of a full-gene re-review of **29** genes carrying
TreeGrafter rows (28 of them in the current TreeGrafter set), done by agent
reviewers (three of the seven records name Codex; the others name no
reviewer), which re-examined every annotation on each gene (not only the
`GO_REF:0000118` rows) and wrote the new actions into the gene review YAMLs:

| Record | Genes | Status |
|---|---|---|
| `exemplars.yaml`, `exemplars-2.yaml` | the ten OpenScientist/Falcon exemplars plus `NCGR_LOCUS1270` | all `reviewed` |
| `fogd.yaml` | `fogD` | `awaiting_adjudication` |
| `metabolic-scope.yaml` | `PP_3394`; `alg8`, `purM`, `ilvA-I`, `ilvA-II` | 1 awaiting; 4 reviewed |
| `enzyme-substrate-transfer.yaml` | `K9IJK6`, `mdr`; `ydiJ`, `PoMZ_10221` | 2 awaiting; 2 reviewed |
| `substrate-and-lineage.yaml` | `Cgas`, `K9IFT7`, `K9IMD0`, `pvdD`; `moeB`, `mdcD` | 4 awaiting; 2 reviewed |
| `fusion-and-toll-scope.yaml` | `NCGR_LOCUS10166`, `TOLL9` | both awaiting |

In total 19 genes are `reviewed` and **10 are `awaiting_adjudication`** in
these records. The awaiting genes' new actions are already in the YAMLs and
therefore in every table above: 13 of the 37 rows that left the down-graded
set since the 2026-09-06 snapshot (5 now `UNDECIDED`, 5 `ACCEPT`, 3
`KEEP_AS_NON_CORE`) are on awaiting genes, so those rows are **provisional**
until a curator adjudicates. Five of the awaiting genes (`fogD`, `K9IJK6`,
`K9IMD0`, `K9IFT7`, `Cgas`), and `IRE1`, have since had follow-up reviews of
focused OpenScientist reports, which changed 16 TreeGrafter actions (see
Results); the re-review records themselves were not updated. The
`cache-reports/` subfolder preserves six OpenScientist reports reused as
evidence in that pass (see its README; they are evidence inputs, not accepted
conclusions).

### Reference standard

- **What the reference is.** Every rate on this page measures agreement with
  the AIGR agent review of each gene, written under the repository's curation
  guidelines and fixed at the pinned commit (`943b98815`) before scoring.
  There is no separately human-rated subset, so agreement with expert
  curators is not quoted.
- **Label visibility.** Reviewers saw `original_reference_id` (and hence
  whether a row was TreeGrafter, corroborated or InterPro2GO) while deciding.
  This affects the corroboration contrast (see the caveat there) and possibly
  the TreeGrafter-vs-IBA contrast.
- **Agent reports among the cited evidence.** 197 of the 998 reviewed
  TreeGrafter annotations (68 of the 299 down-graded) cite an OpenScientist or
  Falcon file (blinded hypothesis report or Falcon deep research) in their
  `review.supported_by`, alongside the literature
  ([`exemplar_independence.py`](TREEGRAFTER/exemplar_independence.py)).
- **The ten blinded exemplars.** The ten OpenScientist/Falcon exemplars on the
  [failure-modes page](TREEGRAFTER/failure-modes.md#openscientist-blinded-verification)
  were drawn only from rows that were already down-graded, with no
  accepted-annotation controls, and n = 10, so no claim about the check's
  reliability (sensitivity, specificity or false-positive rate) can be made.
  Their blinded verdicts can be compared fairly with the review actions
  recorded when each exemplar was selected (`aprA` `REMOVE`, `fcs` `MODIFY`,
  `OCTS1` `MARK_AS_OVER_ANNOTATED`, `eryAIII` `MODIFY`, `mcr-1` `MODIFY`,
  `NaPMT3` `REMOVE`, `ADAR2` `REMOVE`, `NaUGT1` `REMOVE`, `aceK` `MODIFY`,
  `ahpC` `MODIFY`), but not with the current actions: some of those reviews
  were later revised with the reports in hand (`aceK` → `ACCEPT`, `NaUGT1` →
  `UNDECIDED`), and 9 of the 10 exemplar annotations now cite the report
  ([`exemplar_independence.tsv`](TREEGRAFTER/exemplar_independence.tsv)).
- **Drift.** The reference is revised over time (62 TreeGrafter actions
  changed since the 2026-09-06 snapshot), which is why results are pinned to
  a commit.

## Caveats

- **Corpus composition.** 69% of the TreeGrafter rows (689 of 998, under two
  taxon labels for KT2440) come from *Pseudomonas putida* KT2440, so the rates
  are largely a *P. putida* result. The 95% Wald interval on the 44.6% accept
  rate is roughly ±3 pp, but the taxon skew and reference drift matter more
  than the sampling error. Directional, not a frozen benchmark.
- The reference standard is the AIGR agent review corpus at the pinned
  commit, which is revised over time (see
  [Reference standard](#reference-standard)).
- `KEEP_AS_NON_CORE` is **not** an error — the inference is correct but
  peripheral. Accept + non-core is 65.6% for TreeGrafter vs 88.8% for
  corpus-wide IBA; adding `MARK_AS_OVER_ANNOTATED` gives the *retained* rates
  in the headline table.
- 44 TreeGrafter rows (4.4%) are `UNDECIDED`, 8 of them on genes still
  `awaiting_adjudication` in the 2026-09-20 re-review records.

## Deeper analyses

- **[Failure Modes & Tree Placement](TREEGRAFTER/failure-modes.md)** — joins all
  299 down-graded annotations to their PANTHER graft point, plus a lightweight
  PANTHER-vs-InterPro [graft check](TREEGRAFTER/graft_check.py) on ten
  exemplars. Key result: the placement is usually sound; the error is the GO term
  attached to the graft node, and InterPro sometimes resolves the protein better
  than PANTHER (e.g. `IPR011803 AprA`, `IPR003083 S-crystallin`).
- **[ATP-synthase terms on flagellar/T3SS export ATPases](TREEGRAFTER/rotary-atpase-leak.md)**
  — a case study of **inherited PAINT over-placement**. The `GO:0046933` /
  `GO:0045259` IBD sits on the duplication node `PTN008558586` in PTHR15184, above
  both the F1-β and the FliI/SctN clades. PAINT IBA and TreeGrafter then label
  nearly every FliI/SctN protein an ATP synthase, and InterPro2GO (IPR013380,
  IPR004100) and `GO_REF:0000108` add further wrong rows. Nine full reviews
  (FliI in *Caulobacter*, *H. pylori*, *P. putida*, *E. coli* and *Salmonella*;
  SctN in *Salmonella* ×2, *Yersinia* and *Shigella*) remove 31 of the 35 affected
  rows and mark the other 4 as over-annotations. The five TreeGrafter rows of
  this case (`fliI` ×3, `sctN` ×2) are in the 2026-10-01 tables, all `REMOVE`.
- **OpenScientist blinded verification** uses a dedicated TreeGrafter prompt
  template,
  [`templates/treegrafter_function_hypothesis.md`](https://github.com/ai4curation/ai-gene-review/blob/main/templates/treegrafter_function_hypothesis.md),
  which frames each propagated term as a blinded "GENE has *<term>*" hypothesis
  and instructs the agent to actively test the failure modes
  (granularity, pseudo-enzyme, mis-placement). Run via
  `gene-hypothesis-research openscientist <org> <gene> --annotation-term-id <GO>
  --as-function-hypothesis --template templates/treegrafter_function_hypothesis.md`.
  See [Reference standard](#reference-standard) for how the ten existing
  runs can be compared with the reviews (against the actions recorded at
  selection, not the current ones).

---
# NOTES

## 2026-10-01

- Refreshed at `943b98815`. The 2026-09-27 numbers were computed at
  `fff7793a6`, which no longer exists on `main` after a rebase; `main` has
  since added reviews (including the rotary-ATPase case study) and follow-up
  reviews of OpenScientist reports on `fogD`, `K9IJK6`, `K9IMD0`, `K9IFT7`,
  `Cgas` and `IRE1`. Re-ran `analyze_treegrafter.py`, `analyze_placement.py`,
  `classify_failure_modes.py`, `snapshot_drift.py`, `exemplar_independence.py`
  and `graft_check.py --refresh-actions` (offline) and rewrote every number on
  both pages from the sidecars: 983 → 998 annotations, 550 → 560 files,
  279 → 299 down-grades, accept 45.1% → 44.6%, retained 76.2% → 77.2%,
  `REMOVE` 10.8% → 11.2%, down-graded 28.4% → 30.0%, `UNDECIDED` 59 → 44;
  MF down-graded 47.7% → 49.3%; hotspot families 24/71 → 27/72. The 15 added
  rows include the five TreeGrafter `GO:0046933` rows of the rotary-ATPase case
  (four new, plus PSEPK `fliI`), now in every table.
- `failure_mode_curated.tsv`: no current override left the down-graded set.
  Six `superseded` rows re-entered it (`fogD` ×4, `IRE1` GO:0070059,
  `K9IJK6` GO:0014909); their new reasons were re-read and they are `current`
  again with the same mode. Seven newly down-graded rows were curated from
  the reviewer's reason: the four new rotary-ATPase rows and `Cgas`
  GO:0071360 (node/sibling term, mode 1), PP_2608 GO:0050661 (mode 1),
  `K9IJK6` GO:0048008 (mode 3). The rest are left to the heuristic, and two
  PP_2608 rows stay mode 0 (16 mode-0 rows now). Superseded-row notes now
  carry the current action. Mode shares barely moved: 1 50%, 3 31%, 4 12%.
- Reframed the "Reference independence" subsection as **Reference standard**:
  the reference is the AIGR agent review fixed at the pinned commit, and the
  scores measure agreement with it. The exemplar caveat now says what can and
  cannot be compared: blinded verdicts against the actions recorded when the
  exemplars were selected (all ten down-graded), not against the current
  actions; with no accepted controls and n = 10, no reliability claim.

## 2026-09-27

- Acted on the TreeGrafter section of
  [REVIEW-2026-09-26](FUNCTION_PREDICTION_EVALUATION/REVIEW-2026-09-26.md).
  Retired the frozen 2026-09-06 snapshot: re-ran `analyze_treegrafter.py`,
  `analyze_placement.py`, `classify_failure_modes.py` and `graft_check.py` at
  `fff7793a6` (a pre-rebase commit no longer on `main`; superseded by the
  2026-10-01 refresh) and rewrote every number on both pages from the sidecars
  (898 → 983 annotations, 510 → 550 files, 306 → 279 down-grades, accept
  41.3% → 45.1%). New `snapshot_drift.py` records the drift (85 added, 63
  changed actions, 48 rows out of / 21 into the down-graded set; 56 of the
  63 changes are the 2026-09-20 re-review), and the page now links and
  summarises `rereview-2026-09-20/` (19 genes reviewed, 10
  `awaiting_adjudication`).
- `failure_mode_curated.tsv` gained a `status` column: 25 overrides whose
  annotation is no longer down-graded are kept but marked `superseded` (the
  classifier ignores them); ADAR2 GO:0008251 re-filed 4 → 1 (its graft node
  PTN000098697 also supplied the accepted ADAR terms); 9 newly down-graded
  PSEPK rows curated to mode 1 from the reviewer's reason. The other 12 new
  down-grades are left to the heuristic or mode 0 (14 mode-0 rows now).
- Reporting: added *retained* and `REMOVE`-only rates next to down-graded
  (summary sidecar *headline rates* block), relabelled mode 3 as an
  informativeness policy, said explicitly that the IBA contrast is
  corpus-wide on different genes and reported the same-file IBA set (20 rows
  on 9 files — too small to use). Added a Reference-independence section; new
  `exemplar_independence.py` shows 9/10 exemplar annotations cite the
  OpenScientist/Falcon report they are scored against, so the exemplar
  agreement claims on the failure-modes page were withdrawn.
- Script hygiene: `analyze_treegrafter.py` docstring no longer contradicts
  itself on `GO_REF:0000120`, and gains `--out-dir` for dry runs;
  `graft_check.py` reads `review_action` from `treegrafter_review.tsv`
  instead of hard-coding it (`--refresh-actions` updates it offline).
- Added the [rotary-ATPase leak](TREEGRAFTER/rotary-atpase-leak.md) case study.
  It began as a first-principles completeness test (F-type ATP synthase across
  15,525 bacterial reference proteomes), whose false positives turned out to be
  FliI/SctN export ATPases annotated as ATP synthases. The TreeGrafter graft points
  are correct here; the error is inherited from a PAINT IBD on a duplication node.
  None of these rows are in the frozen 2026-09-06 tables.

## 2026-09-25

- The snapshot callout's drift note was itself quoting exact merged-tree
  figures that a second `main` merge (`3246edc2`) had already outdated.
  Rewrote it as a dated floor (≥63 annotations / 28 files across HETGA,
  9AVES, PSEPK, XENLA; four changed actions, naming the two `pgm` rows that
  cross into the down-graded set) so it no longer re-stales on every merge.
  Added a snapshot marker to the failure-modes sub-page and a caveat there
  that `K9IMD0` (draculin) and `mdr` are contested mode-4 calls awaiting a
  curator. "genes" → "proteins" in the Corroboration and Results text. The
  Caveats composition bullet, which still quoted the earlier 43-row delta as
  "mostly HETGA", was rewritten as the same floor (≥63, HETGA and *P. putida*
  roughly equal; 656/961 = 68%). Doc-only.

## 2026-09-19

- Froze the sidecars at the 2026-09-06 snapshot (branch `49d8cc0b`, `main`
  `b62182cc`) and said so on the page: the merged `main` adds 15 review files
  / 43 `GO_REF:0000118` annotations (HETGA 29, PSEPK 12, XENLA 2) and one
  action change (PSEPK `fruA` GO:0090563 `ACCEPT` → `KEEP_AS_NON_CORE`) that
  are not in the tables. The completeness clause is now past tense and
  scoped to the snapshot; the *P. putida* composition caveat is marked as a
  snapshot property (~70% then, ~68% on the merged tree). No scripts re-run.

## 2026-09-07

- Worked the four open next steps. (1) `GO_REF:0000120` is UniProt's
  multi-pipeline merge (definition confirmed from the GO reference collection),
  so `GO_REF:0000118` rows are *uncorroborated* TreeGrafter calls; evaluated the
  corroborated PANTHER rows (637, 77% accepted) and uncorroborated InterPro2GO
  rows (698, 26% accepted) on the same genes and added the Corroboration
  section. (2) Classified all 306 down-grades into the four failure modes
  (`classify_failure_modes.py` + `failure_mode_curated.tsv`, 163 rows curated
  by hand, 134 by keyword heuristic, 9 left unclassified): granularity 47%,
  generic/context 36%, mis-placement 13%, pseudo-enzyme 1%. (3) Added per-family / subfamily /
  graft-node hotspot aggregation (`treegrafter_family_hotspots.tsv`) and the
  hotspot table. (4) Moved TFP and IRE1 out of the pseudo-enzyme table on the
  failure-modes page (they are node-term and generic-binding cases) and added
  the newly recognised mis-placements (mdh, mqo1–3, dapE/pepV, ptxD, mupP,
  quiA, kdsC, acoA, stilbene dioxygenases).

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

- **Adjudicate the ten `awaiting_adjudication` genes** of the 2026-09-20
  re-review (`fogD`, `PP_3394`, `K9IJK6`, `mdr`, `Cgas`, `K9IFT7`, `K9IMD0`,
  `pvdD`, `NCGR_LOCUS10166`, `TOLL9`); 13 of the 37 rows that left the
  down-graded set since the snapshot are on them, so the current rates are
  provisional there. Five of them have had follow-up reviews since; update
  the records' status when a curator signs off.
- **A controlled exemplar sample.** Re-run the blinded OpenScientist/Falcon
  check on a fresh sample that includes accepted TreeGrafter rows as
  controls, with the review actions recorded before the reports are read;
  only then quote a sensitivity/specificity.
- **Blind the corroboration test.** Re-adjudicate a sample of `GO_REF:0000118`
  and `GO_REF:0000120` rows with `original_reference_id` withheld, to separate
  the corroboration effect from the reviewer's visibility of the label.
- **Second-pass the heuristic failure-mode assignments.** 123 of the 299
  down-grades carry a heuristic mode; 58 of those are decided by construction
  (51 CC rows, 7 low-information binding terms), leaving **65 keyword-placed
  MF/BP rows**, plus the **16 mode-0 rows** (`acoA`, `ahpC`, `benB`,
  `cbcW` ×2, `Cgas`, `davA`, `flgG`, `groES`, `I7J3R9`, `mfd`, `nuoM`,
  `PP_0094`, `PP_0301`, `PP_2608` ×2).
- **Feed the hotspot list upstream.** Concrete PAINT / PANTHER tickets: a
  stilbene-dioxygenase subfamily in PTHR10543, the `GO:0046933` IBD on the
  PTHR15184 duplication node (see the rotary-ATPase case), the EptA node term in
  PTHR30443, the PMT subfamily in PTHR11558, PKS-vs-FAS in PTHR43775, the
  M20A subfamilies in PTHR43808, and the MDH/LDH node in PTHR43128.
- **Human-rated anchor.** Have a curator rate a small shared subset so that
  agreement between the agent reviews and expert judgement can be quoted.
- **Broaden the taxon base.** 69% of the rows are *P. putida* KT2440; the 29
  HETGA rows (76% accepted) are a first mammalian batch, too small to
  generalise from.
