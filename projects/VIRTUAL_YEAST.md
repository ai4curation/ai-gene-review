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

## Workstream #3 results (done)

Full write-up + reproduction: [**RESULTS**](VIRTUAL_YEAST/RESULTS.md). Three grounded
benchmarks over the curated yeast (123 genes / 3,926 annotations) and pombe (72 / 2,519)
review sets:

1. **Retention.** Computational annotations (IBA-dominated) are retained by expert review
   more often (92.5%) than experimental ones (76.7%) — GO's conservative IBA/GO-CAM layer
   is a cleaner functional prior than a raw experimental GAF.
2. **Aspect localization.** The over-annotation is almost entirely in **molecular
   function**: experimental MF is 45% flagged in yeast (22% in pombe), while experimental
   **BP and CC are ~96–99% trustworthy** in both organisms. Actionable rule for AIVC priors:
   *trust curated BP/CC; treat the experimental MF layer (esp. `protein binding`) as noisy.*
3. **Novelty + paralog discrimination.** InterPro2GO domain predictions are ~90–94%
   already-in-GOA (CNN / training-data redundancy). The top novel term, `GO:0140662`
   (ATP-dependent protein folding chaperone), is predicted for 9 Hsp70 paralogs — and a
   hand-curated [`SSZ1-interpro2go-predictions-review.yaml`](../genes/yeast/SSZ1/SSZ1-interpro2go-predictions-review.yaml)
   scores it **PLI (paralog over-annotation)** for the atypical, ATPase-dispensable SSZ1
   while it is correct for canonical SSA1/SSQ1 — the exact failure mode foundation-model
   predictors commit.

(See RESULTS.md for caveats: §1–2 measure annotation retention, not novel-prediction
accuracy; the gene sets are non-random.)

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

### 3. Prediction-vs-review benchmark *(DONE)*
- [x] Score computational vs experimental annotation retention across reviewed yeast genes → [RESULTS](VIRTUAL_YEAST/RESULTS.md)
- [x] Extend to predictions **absent** from GOA using `PredictionReview` — InterPro2GO novelty benchmark + hand-curated SSZ1 worked example (PLI paralog over-annotation)
- [x] Stratify over-annotation by GO aspect (MF/BP/CC) — over-annotation localizes to experimental MF
- [x] Compare against `genes/SCHPO/` (pombe) as an independent curated set — pattern replicates
- [ ] Hand-adjudicate the remaining novel InterPro2GO predictions (16 yeast + 21 pombe) into `PredictionReview` files
- [ ] Extend to a predictor with genuinely novel output (PANTHER/IBA propagation, ProtNLM) beyond domain-redundant InterPro2GO

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
