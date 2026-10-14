---
title: "ISOFORMS: when one gene makes opposite products"
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

# ISOFORMS

Genes whose splice isoforms or cleavage products do different, sometimes opposite, things

<span class="small">AI Gene Review · projects/ISOFORMS · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- Most GO annotation is **gene-level**, but Bcl-xL/Bcl-xS and α-MSH/β-endorphin come from one gene with **opposite effects**.
- We reviewed **2,786 annotations on 16 paradigm genes** and added `isoform`, `negated` and `functional_isoforms` to the data model.
- Conflation is common: **258 rows marked over-annotated**, e.g. 8 in BCL2L1, 21 in VEGFA, 63 in mouse App.

---

## The problem

![h:470](isoform-conflation.svg)

---

## The gene set

| Tier | Genes | Contrast |
|---|---|---|
| 1 · paradigms | AGRN, WT1, BCL2L1, FAS, VEGFA, CASP9 | antagonistic or dominant-negative isoforms |
| 2 · tissue / development | FN1, TPM1, TPM3, DSCAM | EDA/EDB, muscle vs cytoskeletal |
| 3 · further cases | FGFR2, PKM, STAT3 | IIIb/IIIc ligands, PKM1/PKM2, STAT3α/β |
| Polyproteins | POMC, APP (human), App (mouse) | cleavage products |

<span class="small">DSCAM caveat: human DSCAM has 2 isoforms, not the 38,016 of fly Dscam1.</span>

---

## Recording distinct products: POMC

![h:470](pomc-functional-isoforms.jpg)

<span class="small">`functional_isoforms` on the POMC review: each cleavage product with its UniProt chain (PRO_…, not the PRO ontology) and its own terms. Two of five products shown.</span>

---

## Over-annotation by gene

![h:470](overannotated-by-gene.svg)

---

## Findings

1. **BCL2L1**: pro-apoptotic Bcl-xS function attached to the gene whose main product is anti-apoptotic.
2. **FAS**: GOA carries both positive and negative regulation of apoptosis; membrane vs soluble decoy isoforms explain it.
3. **VEGFA**: VEGF165B is anti-angiogenic while canonical isoforms are pro-angiogenic.
4. **App/APP**: splicing (KPI domain) *and* cleavage (sAPPα vs Aβ) in one gene.
5. An `isoform` tag records **what was tested**, not necessarily what is unique to that isoform.

---

## Status and next steps

- 12/16 paradigm reviews COMPLETE.
- Finish **WT1**, **VEGFA**, **AGRN** and **DSCAM**.
- Decide whether to review PTBP1, PTBP2 and MST1R.
- 16 reviews repo-wide use `functional_isoforms` so far.

**Read more:** `projects/ISOFORMS.md` · `projects/ISOFORMS/genes.csv` · `src/ai_gene_review/schema/gene_review.yaml`
