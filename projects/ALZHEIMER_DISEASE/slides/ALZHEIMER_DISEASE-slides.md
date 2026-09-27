---
title: "Alzheimer disease: reviewing GO annotations for 34 genes"
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

# Alzheimer disease genes

Reviewing every GO annotation on 34 human genes behind amyloid, tau, lipid and microglial biology

<span class="small">AI Gene Review · projects/ALZHEIMER_DISEASE · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- AD genetics converges on **APP processing**, **tau**, **lipid transport**, **endocytosis** and **microglial immunity**.
- We reviewed **4,336 GO annotation rows** (4,332 existing plus 4 proposed NEW) on **34 human genes**; every review is **COMPLETE** and validates.
- **54% accepted as core**, 630 rows marked over-annotated, only **4 REMOVE**: abstract-only experimental rows were left **UNDECIDED** (34) rather than overruled. The proposed pathway modules are **not built yet**.

---

## The core mechanism: two routes for APP

![h:500](app-processing.svg)

---

## Why this gene set

- **Mixed on purpose**: familial genes (APP, PSEN1, PSEN2), GWAS and rare-variant risk genes (APOE, TREM2, SORL1, PLCG2, ABI3), and pathway genes (BACE1, the γ-secretase subunits, MAPT, GSK3B, CDK5).
- Anchored on Open Targets and GWAS Catalog for `MONDO:0004975`, plus Bellenguez 2022, Kunkle 2019 and Sims 2017.
- AD genes carry some of the **largest annotation sets** in human GO: APP 429 rows, GSK3B 390, APOE 293, TREM2 273.
- The test: can review separate each gene's **core molecular function** from pleiotropic and disease-context rows?

---

## Actions per gene

![h:500](ad-actions-chart.svg)

---

## What a review looks like

![h:430](psen1-review-table.jpg)

<span class="small">PSEN1 review page: IBA rows for Notch signalling and intramembrane aspartic endopeptidase activity accepted as core γ-secretase function.</span>

---

## APP: isoforms and cleavage products

![h:430](app-isoforms.jpg)

<span class="small">The APP review separates splice classes and cleavage products (sAPPα, sAPPβ, …) so fragment-specific functions are not pinned on the whole precursor.</span>

---

## Findings

1. **Very few REMOVEs (4)**: APP Notch signalling (IEA keyword), ADAM10 *metallodipeptidase activity* (IEA; ADAM10 is an endopeptidase), PLCG2 Wnt signalling (TAS), INPP5D NKG2A `protein binding` (abstract says SHIP is not associated).
2. **UNDECIDED instead of overruling (34)**: e.g. PSEN1 unusual locations (16), CD33/CD2AP tau-secretion rows from an FRMD4A-centred screen.
3. **4 NEW** terms: APP *cell adhesion mediator activity*, *cell adhesion molecule binding*, *copper ion binding*; INPP5D *phosphotyrosine residue binding*.
4. **MODIFY concentrated in signalling genes**: SPI1 21, PLCG2 19, INPP5D 12.

---

## Status and next steps

- ✅ 34/34 gene reviews COMPLETE, most with a second-pass `reference_review` audit.
- ⬜ Reusable normal-biology modules: APP processing, γ-secretase intramembrane proteolysis, apolipoprotein transport, microglial lipid sensing, tau microtubule biology, endocytic adaptors.
- ⬜ Resolve the 34 UNDECIDED rows with full text.

**Read more:** `projects/ALZHEIMER_DISEASE.md` · `genes/human/<GENE>/`
