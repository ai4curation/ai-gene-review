---
title: "BIOREASON_COMPARISON / article"
---

# BIOREASON_COMPARISON / article

Paper drafts and supporting material for the **BioReason-Pro / AIGR** manuscript, intended for **ISMB 2026 Function-COSI**.

## Files

- `manuscript.tex` — **canonical full manuscript source** (title, abstract, introduction, background, methods, results, discussion, limitations, conclusions, figure/table callouts, and BibTeX references). Start here.
- `references.bib` — BibTeX bibliography for `manuscript.tex`.
- `manuscript.md` — lightweight website bridge that points readers to the LaTeX source and local PDF build command.
- `supplemental-benchmark-details.md` — source-availability and denominator details moved out of the main manuscript.
- `abstract.md` — 2-page long-form conference abstract (earlier draft; largely superseded by the manuscript but kept as a source for the short version).
- `short-abstract.md` — 250-word short-form abstract (based on Google-Doc edits).
- `slides.md` / `slides.html` — **ISMB 2026 Function-COSI slide deck** (Marp source + rendered HTML; embeds `figures/`). Render: `npx @marp-team/marp-cli@latest slides.md --html --allow-local-files`.
- `README.md` — this file.
- `bioreason-pro-biorxiv.pdf` — *(not committed)* reference PDF: Fallahpour *et al.* (2026) *BioReason-Pro: Advancing Protein Function Prediction with Multimodal Biological Reasoning*, bioRxiv 10.64898/2026.03.19.712954. Local reference only; excluded via `.gitignore` due to third-party rights.

## Thesis

Annotation databases face a practical deployment question — *when is a new function-prediction method good enough to trust in production?* — that CAFA-style aggregate metrics ($F_{\max}$, $S_{\min}$) cannot fully answer. AIGR (AI Gene Review) is an agentic curation pipeline that complements CAFA-style evaluation by:

1. **Reading the narrative.** Modern agentic predictors such as BioReason-Pro emit free-text functional summaries and chain-of-thought reasoning traces that sit outside bag-of-GO-terms scoring.
2. **Surfacing systematic failure modes.** Pseudoenzyme blind spots, localisation defaults, paralog indistinguishability, missing organism-specific biology, neo-functionalisation, narrative–GO disconnect, and cross-kingdom fold bias — not visible in aggregate scores, decisive for deployment.
3. **Distinguishing novel insight from restatement.** Most BioReason-Pro summaries narratively restate InterPro2GO. An aggregate score cannot see this; an agentic review can.

## Evidence base

- **ARGO139 BioReason-Pro evaluation** (see `../BIOREASON_COMPARISON.md`): fixed 139-gene benchmark used for both RL narrative review and SFT GO-term review, with overall RL correctness 3.7/5, completeness 2.9/5, a seven-mode failure-mode taxonomy, and source-stratified SFT term assessments.
- **`ESR-ECOLI-DET-Mini` 7-gene *E. coli* positive control and recap** against de Crécy-Lagard *et al.* (2025, *G3*) expert error taxonomy (see `../../VALIDATING_ECOLI_PREDICTIONS.md` and `../recapitulation-experiment/claude-expt-1/`; dataset ID `10.5281/zenodo.20751016`): AIGR reproduces all 7 classes when labels/rationales are present as a positive control. An answer-key-withheld, literature/bioinformatics-assisted recapitulation recovers 4/7 exact labels, enough for useful triage but not expert-equivalent.
- **Supplemental SFT source checks** on the public HuggingFace `wanglab/protein_catalogue` dataset: retained for reproducibility in `supplemental-benchmark-details.md`.

## How to read this directory

For a reviewer coming in cold, read in this order:

1. `manuscript.tex` — the full story.
2. `supplemental-benchmark-details.md` — source availability and supplemental denominator checks.
3. `../BIOREASON_COMPARISON.md` — the underlying experimental log with per-organism breakdown, top performers, critical failures, and full failure-mode taxonomy.
4. `../VALIDATING_ECOLI_PREDICTIONS.md` — the de Crécy-Lagard positive-control experimental log.
5. `../recapitulation-experiment/claude-expt-1/README.md` — archived `ESR-ECOLI-DET-Mini` answer-key-withheld recap results.
6. `short-abstract.md` — a 250-word pitch.

## PDF build

Build the manuscript PDF directly in this project workspace:

```bash
cd projects/BIOREASON_COMPARISON
just pdf
```

The recipe runs `latexmk` in `article/` and writes `article/manuscript.pdf`.
Generated PDFs and LaTeX build outputs are intentionally ignored here.
