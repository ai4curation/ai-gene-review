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

- Behaviour-label terms come mostly from **knockout phenotypes** (IMP, IGI), whatever the gene's molecular job.
- We mined the whole corpus, wrote a **four-step rubric**, and mapped **16 standard behavioural assays** to the GO terms they can support.
- **89%** of adjudicated behaviour rows (219 of 247) are **downgraded**; the 28 accepted are mostly sensory channels and receptors, plus CRY and GCG.

---

## Why behaviour is the hard case

- A behaviour integrates the whole nervous system, plus development, metabolism and basic cell biology.
- So almost any perturbation can move it: a tubulin, a lysosomal peptidase, a ciliary scaffold.
- In the [ASSAY_TO_FUNCTION](../../ASSAY_TO_FUNCTION.html) framing it is the **most distal, most convergent** readout.
- 2026-10-04 lexical snapshot: **268** behaviour-label annotations on **110** genes in GOA files; IMP 113, IEA 56, IGI 37, IDA 3.

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
- ✅ `reports/REPORT.md` regenerated (2026-10-04 lexical snapshot: 247 adjudicated, 89%).
- ⬜ Resolve 12 UNDECIDED rows in AKT1, BLOC1S6, Pde4, Agtr1a and GHSR; replace the lexical miner with a behavior-branch closure (#4046).
- ⬜ Record *which assay* drove each behaviour annotation so the check can run automatically.

**Read more:** `projects/BEHAVIOR.md` · `projects/BEHAVIOR/impress/` · `projects/BEHAVIOR/mine_behavior.py`
