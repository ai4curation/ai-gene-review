---
title: "TreeGrafter Inference Evaluation"
maturity: IN_PROGRESS
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
/ `PANTHER`.)

One more reference matters, and it changes what the `GO_REF:0000118` set *is*.
`GO_REF:0000120` is UniProt's **"Combined Automated Annotation using Multiple
IEA Methods"**: per its GO reference-collection definition it "integrates
identical annotations from multiple electronic pipelines, including UniRule,
ARBA, InterPro2GO, TreeGrafter2GO (GO_REF:0000118), RHEA2GO, KeyWord2GO,
SubCellular2GO, EC2GO and EnsEMBL Compara", listing the contributing pipelines
pipe-separated in `WITH/FROM`. In this corpus **every** `GO_REF:0000120` row
with a `PANTHER:PTN…` in `WITH/FROM` (891 rows) also lists at least one other
pipeline (InterPro in most cases), and **no gene has the same term under both
`GO_REF:0000118` and `GO_REF:0000002`**. So the three electronic references
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

This writes three committed sidecars (no hard-coded numbers):

- [`TREEGRAFTER/treegrafter_review.tsv`](TREEGRAFTER/treegrafter_review.tsv) — one row per reviewed TreeGrafter annotation (gene, taxon, term, aspect, action).
- [`TREEGRAFTER/treegrafter_contrast.tsv`](TREEGRAFTER/treegrafter_contrast.tsv) — one row per reviewed corroborated-PANTHER (`GO_REF:0000120`) and InterPro2GO (`GO_REF:0000002`) annotation on the same genes.
- [`TREEGRAFTER/treegrafter_summary.tsv`](TREEGRAFTER/treegrafter_summary.tsv) — action counts for all populations, by-aspect and by-taxon breakdowns, and the most frequently down-graded TreeGrafter terms.

Two further scripts build on it (see the [failure-modes page](TREEGRAFTER/failure-modes.md)):
`analyze_placement.py` joins each annotation to its PANTHER family / subfamily
/ graft node and writes
[`treegrafter_family_hotspots.tsv`](TREEGRAFTER/treegrafter_family_hotspots.tsv);
`classify_failure_modes.py` assigns every down-graded annotation a failure
mode and writes
[`treegrafter_failure_modes.tsv`](TREEGRAFTER/treegrafter_failure_modes.tsv).

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

### Corroboration: TreeGrafter-only vs multi-method vs InterPro2GO-only

On the same 510 genes, the reviewer treatment of the three electronic
populations defined above:

| Population (same genes) | n | `ACCEPT` | `KEEP_AS_NON_CORE` | down-graded |
|---|---:|---:|---:|---:|
| TreeGrafter, **uncorroborated** (`GO_REF:0000118`) | 898 | 41% | 21% | 34% |
| TreeGrafter **corroborated** by ≥1 other pipeline (`GO_REF:0000120`, `PANTHER:PTN…`) | 637 | **77%** | 9% | **12%** |
| InterPro2GO, **uncorroborated** (`GO_REF:0000002`) | 698 | 26% | 20% | **53%** |

Three things follow:

1. **Corroboration is the strongest single predictor of a good TreeGrafter
   call.** The same algorithm's output is accepted 77% of the time when another
   pipeline reproduces it and 41% when none does — the corroborated set is
   accepted at a higher rate than curated PAINT/IBA on the whole corpus (72%).
   UniProt's `GO_REF:0000120` merge is, in effect, already a QC gate, and the
   `GO_REF:0000118` residue is the part that failed it.

   > **Caveat — the reviewers were not blind to the label.** `original_reference_id`
   > is visible in the review YAML while the annotation is being adjudicated, and
   > "combined multiple IEA methods" (`GO_REF:0000120`) reads as visibly stronger
   > provenance than a lone `GO_REF:0000118`. So the 77%-vs-41% gap may be partly
   > *caused by* the label rather than only *predicted* by it. The direction of the
   > effect is very likely real — corroboration by an independent pipeline is
   > genuine evidence, and this is the same reasoning the repo's IBA guidance
   > applies to propagation provenance — but the magnitude should not be taken at
   > face value from this corpus. Separating the two requires the held-out,
   > provenance-blinded test in the next-steps list below; until that is run, treat
   > 77% vs 41% as an upper bound on the true effect.
2. **Uncorroborated InterPro2GO is worse than uncorroborated TreeGrafter**, not
   better: 53% down-graded, 58% for MF. Its rejected terms are dominated by
   coarse ancestors — `catalytic activity` (47), `oxidoreductase activity` (21),
   `membrane` (17), `nucleotide binding` (15). This qualifies the graft-check
   hypothesis on the failure-modes page: InterPro *does* out-resolve PANTHER for
   particular proteins (AprA, S-crystallin, Mcr1), but the InterPro2GO rows that
   TreeGrafter fails to corroborate are mostly low-information, and the
   informative InterPro2GO calls have already been merged into `GO_REF:0000120`.
3. The **taxon skew cuts both ways**: TreeGrafter is down-graded 31% on the
   *P. putida* rows and 42% elsewhere, while InterPro2GO is down-graded 58% on
   *P. putida* and 37% elsewhere (the *P. putida* reviews were strict about
   generic MF terms).

### Where TreeGrafter inferences fail

> **Deep dive:** [Failure Modes & Tree Placement](TREEGRAFTER/failure-modes.md)
> joins every down-graded annotation to the PANTHER family/subfamily it was
> grafted onto (and the ancestral `PTN` graft node), and assigns each one a
> failure mode. **Short answer: in five cases out of six the placement is
> fine and the inherited term is the problem** — too coarse or a sibling term
> from the family node (47%), or a generic / out-of-context localization or
> process (36%). About one in eight (41 annotations on 27 proteins, e.g. `aprA`,
> `fcs`, `mdh`, `mqo1–3`, `dapE`) is a true within-superfamily mis-placement,
> and genuine pseudo-enzymes are rare (4 annotations, 2 proteins).

| Failure mode | annotations | share | proteins |
|---|---:|---:|---:|
| 1 Granularity — right subfamily, family/node-level or sibling term | 143 | 47% | 109 |
| 3 Generic / out-of-context CC, binding or process term | 109 | 36% | 94 |
| 4 Within-superfamily mis-placement | 41 | 13% | 27 |
| 0 Unclassified — heuristic declines to guess (curation queue) | 9 | 3% | 8 |
| 2 Pseudo-enzyme / co-opted fold | 4 | 1% | 2 |

Protein counts are distinct **review files**, not gene symbols — the corpus has
510 files but only 493 symbols (`mdh`, `ALB`, `dapF` and seven other symbols
span more than one file), so a symbol-keyed count under-reports modes 3 and 4
as 92 and 26.

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

### Family hotspots (upstream targets)

[`treegrafter_family_hotspots.tsv`](TREEGRAFTER/treegrafter_family_hotspots.tsv)
aggregates the reviewer outcome over *all* 898 TreeGrafter annotations per
PANTHER family, subfamily and graft node. Of the 63 families with at least
four reviewed annotations, **29 have half or more of their propagated terms
down-graded** and 19 have none — the errors are concentrated, not diffuse.
The worst families are candidate PAINT subfamily-annotation or node-term
fixes:

| Family | n | proteins | down-graded | Failure | Example genes |
|---|---:|---:|---:|---|---|
| PTHR10543 beta-carotene dioxygenase | 8 | 4 | 100% | stilbene/lignostilbene dioxygenases grafted onto the carotenoid-cleavage subfamily (mode 4) | Q53353, Saro_0802, Saro_2809, lsdB |
| PTHR30443 "inner membrane protein" (EptA) | 8 | 4 | 100% | EptA node carries `LPS core` and `phosphotransferase` instead of pEtN transferase (mode 1) | mcr-1, mcr2, mcr-3, mcr-4 |
| PTHR44169 acyl-DHAP reductase | 6 | 1 | 100% | lipid-enzyme family terms on a secondary-metabolite SDR (mode 1) | fogD |
| PTHR48078 threonine dehydratase | 6 | 2 | 100% | serine-deaminase sibling terms on biosynthetic IlvA (mode 1) | ilvA-I, ilvA-II |
| PTHR11556 FBPase-related | 11 | 2 | 64% | plant cytosolic-isoform processes on chloroplast/bacterial FBPases (mode 4/3) | NCGR_LOCUS1270, fbp |
| PTHR11558 spermidine synthase | 9 | 3 | 67% | family-level spermidine terms on the PMT subfamily (mode 1) | NaPMT3, PMT1, PMT2 |
| PTHR21047 dTDP-sugar epimerase | 10 | 3 | 60% | generic polysaccharide / epimerase parents (mode 1) | eryBVII, rfbC, rmlC |
| PTHR11632 SDH flavoprotein | 7 | 2 | 71% | SDH/FRD/APS-reductase heterogeneity (modes 1 and 4) | aprA, sdhA |
| PTHR43775 fatty acid synthase | 4 | 4 | 100% | family-level FAS term on PKS subfamilies (mode 1) | eryAI–III, Pks1 |
| PTHR43128 L-2-hydroxycarboxylate DH | 4 | 2 | 100% | MDH grafted onto the L-LDH subfamily (mode 4) | METEA/mdh, PSEPK/mdh |
| PTHR21272 catabolic 3-dehydroquinase | 4 | 4 | 100% | catabolic process on biosynthetic type-II DHQases (mode 4) | aroQ, aroQ1, aroQ2, aroQ-III |
| PTHR43808 acetylornithine deacetylase (M20A) | 5 | 3 | 80% | DapE / PepV grafted onto the ArgE branch (mode 4) | dapE, pepV |

## Caveats

- **Corpus composition.** 898 TreeGrafter annotations across 510 reviewed
  proteins (510 review files; only 493 distinct gene symbols), but
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

- **Feed the hotspot list upstream.** The twelve families above are concrete
  PAINT / PANTHER tickets: a stilbene-dioxygenase subfamily split in
  PTHR10543, the EptA node term in PTHR30443, the PMT subfamily in PTHR11558,
  PKS-vs-FAS in PTHR43775, the M20A subfamilies in PTHR43808, and the
  MDH/LDH node in PTHR43128.
- **Test corroboration as a QC gate on a held-out corpus.** Here the
  `GO_REF:0000120` merge predicts acceptance (77% vs 41%); check whether the
  same holds on a non-*P. putida* gene set, and whether family heterogeneity
  (the Falcon family verdicts) predicts *which* TreeGrafter calls fail to be
  corroborated.
- **Second-pass the heuristic failure-mode assignments.** 134 of the 306
  down-grades carry a keyword-derived mode. 68 of those are decided *by
  construction* rather than by reading the reviewer — 61 cellular-component
  rows (mode 3 by aspect) and 7 rows on the low-information binding allowlist —
  leaving **66 genuinely keyword-placed MF/BP rows** that deserve the same
  per-row curation the other 163 received (`failure_mode_curated.tsv`). The
  9 mode-0 rows (`acoA`, `benB`, `davA`, `groES`, `nuoM`, `PP_0094`, `I7J3R9`,
  `NCGR_LOCUS1270` ×2) are the head of that queue: the heuristic deliberately
  declines them rather than guessing.
- **Blind the corroboration test.** Re-adjudicate a sample of `GO_REF:0000118`
  and `GO_REF:0000120` rows with `original_reference_id` withheld, to separate
  the corroboration effect from the reviewer's visibility of the provenance
  label (see the caveat in the Corroboration section).
- **Broaden the taxon base.** ~70% of the reviewed TreeGrafter rows are
  *P. putida* KT2440; a batch of eukaryotic or archaeal non-model genes would
  tell whether the 41% accept rate travels.
