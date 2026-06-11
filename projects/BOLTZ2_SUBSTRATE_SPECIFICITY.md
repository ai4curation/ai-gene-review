# Boltz-2 for Enzyme Substrate Specificity

## Overview

This project explores whether **Boltz-2** — the 2025 open-source structure + binding-affinity
foundation model from the MIT Jameel Clinic / Recursion — can provide a *structure-grounded prior*
on **enzyme substrate specificity** to support GO curation decisions.

It is a methods/feasibility companion to three existing projects:

- [`ENZYME_SPECIFICITY.md`](ENZYME_SPECIFICITY.md) — genes where GO terms get the substrate wrong
  (too narrow, too broad, wrong reaction). These are exactly the questions Boltz-2 might inform.
- [`STRUCTURE_FUNCTION.md`](STRUCTURE_FUNCTION.md) — the broader "what does structure add over HMMs"
  landscape (Foldseek, M-CSA/EnzyMM, PARSE, DPFunc, …). Boltz-2 is a new, **ligand-aware** layer
  that none of those tools cover.
- [`VALIDATING_ECOLI_PREDICTIONS.md`](VALIDATING_ECOLI_PREDICTIONS.md) — the de Crécy-Lagard et al.
  (PMID:40703034) taxonomy of ML enzyme-prediction failures, several of which (PLI = "wrong paralog
  subfamily", "correct first 3 EC digits, wrong substrate") are **substrate-specificity** errors.

**Source for Boltz-2:** Passaro, Wohlwend et al., *Boltz-2: Towards Accurate and Efficient Binding
Affinity Prediction* (2025), [PMC12262699](https://pmc.ncbi.nlm.nih.gov/articles/PMC12262699/);
code: https://github.com/jwohlwend/boltz (MIT license).

## The idea in one sentence

For an enzyme of uncertain specificity, **co-fold the protein with each of a panel of candidate
substrates (as SMILES) and rank them by Boltz-2's predicted binding affinity and binding-pocket
plausibility** — then ask whether the top-ranked candidate matches (or contradicts) the existing GO
substrate annotation.

## What Boltz-2 actually provides

| Capability | Output | Relevance to specificity |
|---|---|---|
| Protein–ligand **co-folding** | predicted 3D complex (CIF) + confidence (pLDDT, iPTM, PAE) | Does the candidate dock in a pocket near the catalytic residues at all? |
| **Affinity value** | `affinity_pred_value` = `log10(IC50 [µM])`; **lower = tighter** | Rank candidate substrates against each other |
| **Binder probability** | `affinity_probability_binary` ∈ [0,1]; **higher = more binder-like** | Binder-vs-decoy gate; filter non-binders |

Key reported numbers (from the paper):
- Pearson r ≈ **0.66** on the FEP+ benchmark, **>1000× faster** than FEP free-energy simulations.
- Outperformed all CASP16 affinity-challenge participants out-of-the-box (no fine-tuning).
- Affinity is **a relative ranking signal**, not a calibrated absolute Kd/IC50.

## Why "substrate specificity" is *not* the same problem Boltz-2 was trained on

This is the crux, and it must frame any conclusion drawn from the model.

1. **Trained on binders/inhibitors, not catalytic substrates.** Affinity labels come from
   Ki/Kd/IC50/EC50 datasets (largely medicinal-chemistry inhibitors). Tight binding ≠ productive
   turnover. A good *inhibitor* binds tightly; a good *substrate* binds productively and is released
   after catalysis. Boltz-2 scores **binding**, which is a *necessary but not sufficient* proxy for
   being a substrate.
2. **No reaction/transition-state modelling.** It cannot tell a hydrolase from a transferase, nor
   capture the PHYKPL-style "aminotransferase fold but actually a phospho-lyase" error — that is a
   *mechanism* question, not a *binding* question.
3. **Cofactors, metals, ions, water are not handled by the affinity module.** Many specificity
   determinants are metal- or PLP/NAD(P)-dependent. The COX2 copper work in
   [`PROTEIN_COMPLEX_FUNCTIONS`](PROTEIN_COMPLEX_FUNCTIONS.md) already flags this limitation.
4. **Affinity is relative, not absolute, and "performance varies strongly between assays."** Use it
   to *rank within one enzyme's candidate panel*, never to compare across enzymes.
5. **Structure-dependent.** "If the model fails to identify the correct pocket … downstream affinity
   predictions are unlikely to be reliable." Large substrate-induced conformational changes are
   often missed.

**Conclusion on scope:** Boltz-2 is best treated as a **hypothesis-generating / triage** tool for
*relative substrate ranking within a single enzyme* and a **binder-vs-decoy filter** — not as
curation-grade evidence on its own. It complements, and does not replace, M-CSA catalytic-motif
detection (which addresses mechanism) and the literature.

## Where it plausibly adds value for this repo

1. **Substrate-range questions (too narrow / too broad).** e.g. LPL1 (CANAL) is annotated
   phosphatidylcholine-specific but acts on *all* glycerophospholipids. Co-folding a lipid panel and
   seeing flat/uniform affinity across head-groups would be consistent with broad specificity;
   strong preference for one head-group would not.
2. **Paralog "wrong substrate" errors (PLI).** e.g. yegV (E. coli) — DeepECTF predicted
   "dehydro-2-deoxygluconokinase"; paper says correct EC first-three (a sugar kinase) but wrong
   substrate. Ranking a panel of candidate sugar substrates could indicate which sugar the pocket
   prefers, supporting/refuting the prediction.
3. **Discriminating closely related candidate substrates** for a kinase/transferase where the fold
   is clear but the acceptor is ambiguous.

## Where it will *not* help (be explicit)

- Reaction-mechanism / EC-class errors (PHYKPL phospho-lyase vs transaminase).
- Pseudoenzymes (Epe1) — binding without catalysis is exactly what it cannot distinguish.
- Metal/cofactor-determined specificity (lanmodulin Ln³⁺ vs Ca²⁺).
- Anything requiring absolute affinity or cross-enzyme comparison.

## Proposed reproducible workflow

Implemented as a scaffold in [`boltz2-substrate-specificity/`](boltz2-substrate-specificity/):

1. **Inputs:** one protein sequence (UniProt) + a curated **candidate substrate panel** of
   `name,SMILES` (include the annotated substrate, plausible alternatives, and 1–2 negative-control
   decoys that *should not* bind).
2. **Generate** one Boltz-2 YAML per candidate with an `affinity` block (`generate_inputs.py`).
3. **Run** `boltz predict` (GPU required) over the panel.
4. **Parse & rank** affinity outputs into a table (`rank_affinity.py`): rank by
   `affinity_pred_value` (ascending) and report `affinity_probability_binary`.
5. **Sanity gate (recommended, manual or scripted):** check the predicted pose places the substrate's
   reactive group near the known catalytic residues (M-CSA / literature); a high-affinity pose in the
   *wrong* pocket is not evidence of specificity.
6. **Interpret** against the existing GO annotation; record as **hypothesis-generating** evidence in
   the gene's `-notes.md` and, if it motivates a change, in the relevant annotation `review.reason`
   (never cite a Boltz-2 score as standalone justification for `REMOVE`/`MODIFY`).

### Critical validation step (do this first)

Before trusting *any* ranking, run the pipeline on **enzymes with experimentally known specificity
and known non-substrates** (positive + negative controls) and confirm Boltz-2 recovers the known
ordering. Candidate benchmark sets: the ENZYME_SPECIFICITY completed cases (LPL1, PHYKPL as a
*negative* test where it *should* fail), and well-characterised kinases with measured substrate
panels. **If it cannot recover known orderings, it should not be used to question curated
annotations.** Never hardcode or assume results — let the benchmark come back inconclusive if it does.

## Practical / cost notes

- **GPU required** (this analysis was scaffolded in a CPU-only container; inference was *not* run
  here). A single protein+ligand prediction is on the order of seconds–minutes on a modern GPU;
  a panel of N substrates is N independent jobs (embarrassingly parallel).
- Install: `pip install boltz` (or `uv add boltz`). First run downloads model weights (~GBs).
- Use `--use_msa_server` for automatic MSA, or precompute MSAs for reproducibility/offline use.

## Status

- [x] Capability review + scope/limitations analysis (this document)
- [x] Reproducible input-generation + ranking scaffold (`boltz2-substrate-specificity/`)
- [ ] Run control/benchmark panel on a GPU (known-specificity enzymes) — **gating step**
- [ ] First demonstrator on a real ENZYME_SPECIFICITY case (candidate: yegV PLI, or LPL1 lipid panel)
- [ ] Decide whether Boltz-2 ranking earns a place in the gene-review bioinformatics toolkit

## Open questions

1. Does inhibitor-trained affinity transfer to *substrate* ranking well enough to be useful?
2. Can the binder-vs-decoy probability reliably flag non-substrates (cleaner signal than the value)?
3. Is pose-based active-site proximity a better specificity signal than the affinity scalar?
4. How does it compare head-to-head with cheaper alternatives (docking, M-CSA, simple pocket analysis)?

Last updated: 2026-06-11
