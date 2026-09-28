---
title: "Validating E. coli ML enzyme predictions"
marp: true
theme: default
paginate: true
size: 16:9
style: |
  section { font-family: "Source Sans 3", "Helvetica Neue", Arial, sans-serif; font-size: 26px; color: #15201e; background: #f4f7f6; padding: 56px 64px; }
  h1, h2 { font-family: "Literata", Georgia, serif; color: #0e6b66; font-weight: 600; }
  h1 { font-size: 46px; } h2 { font-size: 34px; margin-bottom: 18px; }
  strong { color: #0e6b66; }
  code { font-family: "IBM Plex Mono", Menlo, monospace; font-size: .85em; background: #e3ece9; padding: 0 .25em; border-radius: 3px; }
  table { font-size: 19px; border-collapse: collapse; } th { background: #dcefec; } td, th { padding: 4px 10px; }
  img { border-radius: 4px; }
  section.lead { justify-content: center; }
  section.lead h1 { font-size: 54px; }
  section.bluf { background: #0e6b66; color: #f4f7f6; }
  section.bluf h2, section.bluf strong { color: #ffffff; }
  section.bluf code { background: rgba(255,255,255,.18); color: #ffffff; }
  footer, header { color: #56655f; font-size: 14px; }
  .small { font-size: 18px; color: #56655f; }
  .cols { display: grid; grid-template-columns: 1fr 1fr; gap: 28px; align-items: start; }
---

<!-- _class: lead -->

# Validating *E. coli* ML predictions

Seven gene reviews against an expert audit of DeepECTransformer

<span class="small">AI Gene Review · projects/VALIDATING_ECOLI_PREDICTIONS · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- An expert audit (de Crécy-Lagard et al. 2025, PMID:40703034) found only **3 of 453** DeepECTransformer predictions for *E. coli* unknowns were **correct and novel**.
- We reviewed **7 genes** spanning five error categories; all 7 reviews are **complete** and our verdicts **match** the paper's.
- The same errors sit in **GOA**: yciO's TsaC activity rows and a fepE tyrosine-kinase IBA row were marked **REMOVE**.

---

## Why these seven

- The paper sorted every prediction into a taxonomy: **COR, CNN, LSP, UNC, PLI, NPI, REP**.
- We sampled across it to ask two questions:
  1. Does an agentic gene review reach the same verdict as the experts?
  2. Do the model's logic errors also appear in existing GO annotations?
- Each gene got a full `*-ai-review.yaml` plus a structured `*-det-predictions-review.yaml`.

---

## Prediction vs reality

![h:480](ecoli-predictions.svg)

---

## A paralog error, in GOA too

![h:430](yciO-review-table.jpg)

<span class="small">yciO review, shown: the IEA GO:0061710 threonylcarbamoyladenylate synthase row (GO_REF:0000003, propagated from the EC number) is marked REMOVE. Not in frame: the IDA row for the same term from the DeepECTF validation paper (PMID:37963869) is also REMOVE.</span>

---

## Review actions across the seven genes

![h:470](ecoli-review-actions.svg)

---

## Lessons

- **Paralogs** (yciO, yegV): a weak in vitro activity from a shared fold is not the biological function.
- **Pathway context** (yjhQ, yrhB): a predicted enzyme is wrong if the host lacks the pathway or already has the enzyme (QueD).
- **In vitro vs in vivo** (yjdM): phosphonoacetate hydrolase rows marked over-annotated.
- **Frequency bias** (fepE): "histidine kinase" for a Wzz O-antigen chain-length regulator.

---

## Status

- ✅ 7/7 gene reviews and prediction reviews complete (March 2026).
- The DeepECTF prediction table is browsable with the BioReason comparison material (`BIOREASON_COMPARISON/deepectf-eval.html`).

**Read more:** `projects/VALIDATING_ECOLI_PREDICTIONS.md` · `genes/ECOLI/<gene>/`
