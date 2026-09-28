---
title: "Function prediction evaluation: an index"
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

# Function prediction evaluation

Testing protein-function predictors claim by claim against reviewed genes

<span class="small">AI Gene Review · projects/FUNCTION_PREDICTION_EVALUATION · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- Aggregate benchmarks say a field is improving; a curator needs to know whether **one method's predictions** are safe to import.
- We review predictions **one claim at a time** against agent-adjudicated gene reviews, with the **COR/CNN/LSP/UNC/PLI/NPI/REP** taxonomy.
- Errors concentrate in **specificity, paralogs, pseudoenzymes and organism context**; in the larger benchmarks most correct predictions were **already known**.

---

## One review loop, many predictors

![h:470](evaluation-loop.svg)

---

## Why claim by claim

- A CAFA-style score averages over thousands of terms and hides *which* terms are wrong.
- Curators import **individual annotations**; a method that is 95% redundant and 5% wrong is a net cost.
- The same seven-category taxonomy (de Crécy-Lagard et al. 2025, PMID:40703034) makes different tools comparable **within** a cohort.
- Caveat: the reference reviews are AI-assisted and of mixed maturity, not expert-signed ground truth.

---

## Results so far

![h:480](prediction-results.svg)

---

## Headlines by project

| Project | Cohort | Headline |
|---|---|---|
| BioReason-Pro | 139 genes | correctness 4.0/5, completeness 2.9/5; 23 of 955 SFT terms correct and novel |
| ProtNLM2 | 242 targets | 288 GO terms: 53 COR, 83 LSP, 103 UNC, 17 NPI |
| DeepECTransformer | 7 E. coli genes | one gene per error category; paper found 3/453 correct novel |
| Affinage | 42 + 22 + 91 genes | GO layer 1/42 specific; narrative added 13 annotations |
| TreeGrafter | 898 IEA rows | 41% accepted vs 72% for PAINT/IBA |

---

## Recurring failure modes

- **Less precise:** a true parent instead of the specific activity (Affinage `oxidoreductase activity` for GPX4).
- **Pseudoenzymes:** ancestral catalysis assigned to inactive members (BioReason on Epe1, pmp20).
- **Paralogs:** wrong subfamily or interchangeable summaries (DeepECTF on yciO; BioReason on sigF/sigG/sigK).
- **Organism context ignored:** a mycothiol synthase predicted in *E. coli*, which has no mycothiol pathway (yjhQ).
- **Localization default:** cytoplasm when no transmembrane segment is found.

---

## Status and next steps

- ✅ BioReason-Pro, Affinage, TreeGrafter and the E. coli DeepECTF set have results; ProtNLM2 cohorts are in progress.
- ⬜ Provenance-blinded re-test of the TreeGrafter corroboration effect.
- ⬜ Ontology-aware (ancestor-distance) scoring for Affinage.

**Read more:** `projects/FUNCTION_PREDICTION_EVALUATION.md` · shared browser `app/predictions/` · each project's own page
