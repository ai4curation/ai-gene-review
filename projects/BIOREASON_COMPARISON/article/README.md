---
title: "BIOREASON_COMPARISON / article"
---

# BIOREASON_COMPARISON / article

Paper drafts and supporting material for the **BioReason-Pro / AIGR** manuscript, intended for **ISMB 2026 Function-COSI**.

## Files

- `manuscript.md` — **full manuscript draft** (title, abstract, introduction, background, methods, results, discussion, limitations, conclusions, figure/table callouts, references). Start here.
- `supplemental-benchmark-details.md` — source-availability and denominator details moved out of the main manuscript.
- `abstract.md` — 2-page long-form conference abstract (earlier draft; largely superseded by the manuscript but kept as a source for the short version).
- `short-abstract.md` — 250-word short-form abstract (based on Google-Doc edits).
- `slides.md` / `slides.html` — **ISMB 2026 Function-COSI slide deck** (Marp source + rendered HTML; embeds `figures/`). Render: `npx @marp-team/marp-cli@latest slides.md --html --allow-local-files`.
- `README.md` — this file.
- `bioreason-pro-biorxiv.pdf` — *(not committed)* reference PDF: Fallahpour *et al.* (2026) *BioReason-Pro: Advancing Protein Function Prediction with Multimodal Biological Reasoning*, bioRxiv 10.64898/2026.03.19.712954. Local reference only; excluded via `.gitignore` due to third-party rights.

## Thesis

Annotation databases face a practical deployment question — *when is a new function-prediction method good enough to trust in production?* — that CAFA-style aggregate metrics ($F_{\max}$, $S_{\min}$) cannot fully answer. AIGR (AI Gene Review) is an agentic curation pipeline that complements CAFA-style evaluation by:

1. **Reading the narrative.** Modern agentic predictors such as BioReason-Pro emit free-text functional summaries and chain-of-thought reasoning traces that bag-of-GO-terms metrics cannot grade.
2. **Surfacing systematic failure modes.** Pseudoenzyme blind spots, localisation defaults, paralog indistinguishability, missing organism-specific biology, neo-functionalisation, narrative–GO disconnect, and cross-kingdom fold bias — invisible to aggregate metrics, decisive for deployment.
3. **Distinguishing novel insight from restatement.** Most BioReason-Pro summaries narratively restate InterPro2GO. An aggregate score cannot see this; an agentic review can.

## Evidence base

- **ARGO139 BioReason-Pro evaluation** (see `../BIOREASON_COMPARISON.md`): fixed 139-gene benchmark used for both RL narrative review and SFT GO-term review, with overall RL correctness 3.7/5, completeness 2.9/5, a seven-mode failure-mode taxonomy, and source-stratified SFT term assessments.
- **7-gene *E. coli* VDCL positive control** against de Crécy-Lagard *et al.* (2025, *G3*) expert error taxonomy (see `../../VALIDATING_ECOLI_PREDICTIONS.md`): AIGR reproduces all 7 error classifications (COR / PLI / NPI / UNC / REP) along with the underlying mechanistic rationales. This is retrospective and not blinded.
- **Supplemental SFT source checks** on the public HuggingFace `wanglab/protein_catalogue` dataset: retained for auditability in `supplemental-benchmark-details.md`.

## How to read this directory

For a reviewer coming in cold, read in this order:

1. `manuscript.md` — the full story.
2. `supplemental-benchmark-details.md` — source availability and supplemental denominator checks.
3. `../BIOREASON_COMPARISON.md` — the underlying experimental log with per-organism breakdown, top performers, critical failures, and full failure-mode taxonomy.
4. `../VALIDATING_ECOLI_PREDICTIONS.md` — the de Crécy-Lagard positive-control experimental log.
5. `short-abstract.md` — a 250-word pitch.
