---
title: "Virtual Yeast: curated causal priors & evaluation layer for AI virtual cells"
maturity: SCOPING
tags: [BIOLOGY_DOMAIN, METHODS, CROSS_CUTTING]
species: [yeast]
---

# Virtual Yeast: curated causal priors & evaluation layer for AI virtual cells

## Overview

The "virtual yeast" / AI virtual cell (AIVC) programme — e.g. *Towards the construction
of a virtual yeast* (Qian, Zhou, Guo et al., **Nature 655, 59–68, 2 July 2026**), and the
broader Bunne et al. (Cell 2024) AIVC agenda — proposes AI agents that simulate
*S. cerevisiae* cellular behaviour from multimodal data. Two of its acknowledged weak
points are **exactly what this repository produces**:

1. **Curated causal priors.** The Perspective asks, verbatim, for *"ontologies and
   knowledge graphs encoding causal relationships among genes, pathways and organelles"* to
   constrain model routing and rewards — but reaches for text-mined KGs (BioGPT, INDRA) and
   never mentions **GO-CAM**, the hand-curated causal-activity ontology that already encodes
   precisely this, with evidence and provenance. This repo holds 2,038 cached GO-CAMs plus a
   `GoCamReview` schema.
2. **Evaluation.** The Perspective benchmarks nothing: its foundation-model function
   predictors (Evo, ESM, PANTHER/IBA) are cited with **no reported accuracy**, and its
   evaluation plan is a vague "expert-defined benchmarks." This repo's reviews are an
   expert-adjudicated gold standard, and its `PredictionReview` framework
   (COR/CNN/LSP/UNC/PLI/NPI/REP biological-validity taxonomy) is a ready-made rubric for
   scoring computational function predictions.

**Goal of this project:** position the AI Gene Review corpus as the *curated causal-prior +
evaluation layer* that an AIVC can consume, and demonstrate it on yeast. The repo already
has **123 reviewed *S. cerevisiae* genes** (`genes/yeast/`) and **72 *S. pombe*** genes to
build on.

## Why this matters (the closed-world trap)

A generic risk in AIVC designs is using a curated KG as a **verifiable-reward oracle**
(reinforcement learning from verifiable rewards). Curated biology is *incomplete*, so a
naive oracle penalizes exactly the **correct novel predictions** the virtual cell exists to
make. What is needed instead is a *typed* prior that distinguishes trusted-core vs
non-core vs over-annotated vs negative (NOT) assertions, each with evidence — which is
what a review action (`ACCEPT` / `KEEP_AS_NON_CORE` / `MARK_AS_OVER_ANNOTATED` / `REMOVE` /
`negated: true`) provides. This repo therefore supplies the belief/provenance layer such a
reward signal actually needs.

## Pilot result (workstream #3, done)

Using the 123 reviewed yeast genes as ground truth, we scored how computational vs
experimental GO annotations survive expert review (n = 3,926 annotations).
Full write-up: [**RESULTS**](VIRTUAL_YEAST/RESULTS.md).

| evidence class | n | retained % | over-annotated / removed % |
|---|---|---|---|
| experimental (IDA/IMP/IPI…) | 2,458 | 76.7 | 22.4 |
| computational (IBA/IEA/ISS…) | 1,342 | 92.5 | 6.9 |

**Finding:** computational annotations — dominated by GO's conservative **IBA** phylogenetic
pipeline — are retained *more* often than experimental ones, which are inflated by
uninformative `IPI` "protein binding" and over-scoped calls. The message for AIVC priors:
**a conservative IBA/GO-CAM layer is a cleaner functional prior than a raw experimental
GAF**, and this repo's review actions are the filter that separates them. (See RESULTS.md
for the important caveats — this is annotation-retention, not novel-prediction accuracy,
and the gene set is non-random.)

---

# STATUS

Last updated: 2026-07-11

## Workstreams

### 1. GO-CAM as the curated causal-prior layer *(strategic, ongoing)*
- [ ] Identify the *S. cerevisiae* subset of the 2,038 cached GO-CAMs (`gocams/`, join via `gocams/index.tsv`)
- [ ] Curate `<id>-review.yaml` (`GoCamReview`) for the highest-value yeast models
- [ ] Export the reviewed set as a typed causal-prior graph (gene → activity → causal relation → gene, with evidence)
- [ ] Write up: "GO-CAM as the causal KG the virtual-yeast Perspective asked for"

### 2. Typed provenance/belief layer for RLVR *(novel contribution)*
- [ ] Export reviewed yeast annotations as typed tiers: trusted-core / non-core / over-annotated / negative
- [ ] Include evidence code + supporting text as provenance per assertion
- [ ] Document how this avoids the closed-world reward trap

### 3. Prediction-vs-review benchmark *(pilot DONE; extend)*
- [x] Score computational vs experimental annotation retention across reviewed yeast genes → [RESULTS](VIRTUAL_YEAST/RESULTS.md)
- [ ] Extend to predictions **absent** from GOA using `PredictionReview` (PANTHER/IBA, ProtNLM already in-repo)
- [ ] Stratify over-annotation by GO aspect (MF/BP/CC) and by paralog family
- [ ] Compare against `genes/SCHPO/` (pombe) as an independent curated set

### 4. Align curation to the paper's 8 functional modules *(prioritization)*
- [ ] Ground each module to a GO-slim term set via the OLS MCP (do **not** hand-guess GO IDs)
- [ ] Map the 123 reviewed yeast genes onto the 8 modules; find coverage gaps
- [ ] Prioritize next yeast reviews to populate under-covered modules (start: metabolic/synthetic-biology prototype)

### The 8 modules (from the Perspective; GO-slim grounding is task 4)
1. Membrane systems — endomembrane trafficking, lipid synthesis
2. Genetic hubs — nuclear organization, genome stability, transcription, cell cycle
3. Mitochondrial energetics — oxidative phosphorylation, redox, ageing
4. Cytosolic metabolism — central carbon, amino-acid/nucleotide biosynthesis, nutrient sensing
5. Biosynthetic networks — translation, folding, PTM, ER–Golgi quality control
6. Cytoskeletal framework — actin, microtubules, cell-wall remodelling
7. Stress processors — stress granules, P-bodies, oxidative-stress detox, RNA QC
8. Degradation machinery — proteasome, vacuole, autophagy, organelle recycling

## Related projects
- [YEAST_METABOLIC_ENGINEERING](YEAST_METABOLIC_ENGINEERING.md) — feeds module 4
- [YEAST_CELL_CYCLE](YEAST_CELL_CYCLE.md) — feeds module 2
- [YEAST_DNA_REPAIR_CHROMATIN](YEAST_DNA_REPAIR_CHROMATIN.md) — feeds module 2
- [YEAST_REPLICATIVE_AGING](YEAST_REPLICATIVE_AGING.md) — feeds module 3
- [FUNCTION_KNOWLEDGE_GAPS](FUNCTION_KNOWLEDGE_GAPS.md) — cross-cutting

## Source
- Qian, L., Zhou, Z., … Guo, T. *Towards the construction of a virtual yeast.* **Nature 655, 59–68 (2026).**
- Bunne, C. et al. *How to build the virtual cell with artificial intelligence.* Cell 187, 7045–7063 (2024).
