# BIOREASON_COMPARISON / article

Paper drafts and supporting material for the **BioReason-Pro / AIGR** manuscript, intended for **ISMB 2026 Function-COSI**.

## Files

- `manuscript.md` — **full manuscript draft** (title, abstract, introduction, background, methods, results, discussion, limitations, conclusions, figure/table callouts, references). ~7,800 words. Start here.
- `abstract.md` — 2-page long-form conference abstract (earlier draft; largely superseded by the manuscript but kept as a source for the short version).
- `short-abstract.md` — 250-word short-form abstract (based on Google-Doc edits).
- `README.md` — this file.
- `bioreason-pro-biorxiv.pdf` — *(not committed)* reference PDF: Fallahpour *et al.* (2026) *BioReason-Pro: Advancing Protein Function Prediction with Multimodal Biological Reasoning*, bioRxiv 10.64898/2026.03.19.712954. Local reference only; excluded via `.gitignore` due to third-party rights.

## Thesis

Annotation databases face a practical deployment question — *when is a new function-prediction method good enough to trust in production?* — that CAFA-style aggregate metrics ($F_{\max}$, $S_{\min}$) cannot fully answer. AIGR (AI Gene Review) is an agentic curation pipeline that complements CAFA-style evaluation by:

1. **Reading the narrative.** Modern agentic predictors such as BioReason-Pro emit free-text functional summaries and chain-of-thought reasoning traces that bag-of-GO-terms metrics cannot grade.
2. **Surfacing systematic failure modes.** Pseudoenzyme blind spots, localisation defaults, paralog indistinguishability, missing organism-specific biology, neo-functionalisation, narrative–GO disconnect, and cross-kingdom fold bias — invisible to aggregate metrics, decisive for deployment.
3. **Distinguishing novel insight from restatement.** Most BioReason-Pro summaries narratively restate InterPro2GO. An aggregate score cannot see this; an agentic review can.

## Evidence base

- **139-gene BioReason-Pro evaluation** across 11 eukaryotic and bacterial clades (see `../BIOREASON_COMPARISON.md`): overall correctness 3.7/5, completeness 2.9/5, with a seven-mode failure-mode taxonomy and an InterPro2GO baseline comparison per gene.
- **7-gene *E. coli* blinded cross-validation** against de Crécy-Lagard *et al.* (2025, *G3*) expert error taxonomy (see `../../VALIDATING_ECOLI_PREDICTIONS.md`): AIGR independently recovers all 7 error classifications (COR / PLI / NPI / UNC / REP) along with the underlying mechanistic rationales.
- **SFT vs RL cross-check** on the public HuggingFace `wanglab/protein_catalogue` dataset (45 proteins, 15 clades): SFT scores lower (correctness 2.9/5, completeness 2.7/5) and fabricates UniProt summary text in 16% of cases.

## How to read this directory

For a reviewer coming in cold, read in this order:

1. `manuscript.md` — the full story.
2. `../BIOREASON_COMPARISON.md` — the underlying experimental log with per-organism breakdown, top performers, critical failures, and full failure-mode taxonomy.
3. `../VALIDATING_ECOLI_PREDICTIONS.md` — the de Crécy-Lagard replication experimental log.
4. `short-abstract.md` — a 250-word pitch.
