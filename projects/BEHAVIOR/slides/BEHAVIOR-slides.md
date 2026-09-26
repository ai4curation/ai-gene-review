---
title: "Behaviour annotations: core function or distant readout?"
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

# Behaviour annotations

When a knockout changes behaviour, is behaviour the gene's function?

<span class="small">AI Gene Review · projects/BEHAVIOR · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- Behaviour terms (GO:0007610 and children) come mostly from **knockout phenotypes** (IMP, IGI), whatever the gene's molecular job.
- We mined the whole corpus, wrote a **four-step rubric**, and mapped **16 standard behavioural assays** to the GO terms they can support.
- **86%** of adjudicated behaviour rows (169 of 197) are **downgraded**; the 28 accepted are mostly sensory channels and receptors, plus CRY and GCG.

---

## Why behaviour is the hard case

- A behaviour integrates the whole nervous system, plus development, metabolism and basic cell biology.
- So almost any perturbation can move it: a tubulin, a lysosomal peptidase, a ciliary scaffold.
- In the [ASSAY_TO_FUNCTION](../../ASSAY_TO_FUNCTION.md) framing it is the **most distal, most convergent** readout.
- Source surface today: **209** behaviour annotations on **87** genes in GOA files; IMP 84, IEA 39, IGI 30, IDA 3.

---

## The chain and the rubric

![h:520](rubric.svg)

---

## What reviewers decided

![h:520](actions.svg)

---

## Assays as evidence

![h:520](assay-map.svg)

---

## Status and next steps

- ✅ Corpus mined; rubric written; accepted rows spot-checked (9 missed downgrades fixed).
- ✅ IMPReSS ingested; assay→GO map and checker built; `BEHAVIORAL_ASSAY` class added to ASSAY_TO_FUNCTION.
- ⬜ Regenerate `reports/REPORT.md` (committed copy is from June: 146 adjudicated, 87%).
- ⬜ Resolve 9 UNDECIDED rows, including Agtr1a drinking (IMP/IGI).
- ⬜ Record *which assay* drove each behaviour annotation so the check can run automatically.

**Read more:** `projects/BEHAVIOR.md` · `projects/BEHAVIOR/impress/` · `projects/BEHAVIOR/mine_behavior.py`
