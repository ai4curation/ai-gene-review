---
title: "Conidiation regulatory cascade"
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

# The conidiation regulatory cascade

A reusable module for fungal asexual spore formation, with 30 reviewed genes

<span class="small">AI Gene Review · projects/CONIDIATION · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- Fungi make conidia through a **TF relay**: FluG/Flb → **BrlA** → AbaA → WetA/velvet, held back by **G-protein/PKA** signalling that FlbA damps.
- We built an **ABSTRACT module** with two taxon variants (*Aspergillus*, *Neurospora*) and reviewed **all 30 member genes**.
- **382 annotations:** 288 accepted, 63 non-core, 25 over-annotated, 1 modified, **5 removed** (4 plant ARBA rows on FlbD, a mis-attributed laccase on wA).

---

## Same logic, different genes

![h:480](conidiation-variants.svg)

---

## Why conidiation

- One of the **best-dissected** fungal developmental programs.
- *Aspergillus* and *Neurospora* reach the same outcome with **largely non-orthologous** regulators.
- Tests whether a module can hold one developmental logic with **taxon variants**, not a species gene list.
- Grounded in **GO:0048315** *conidium formation* and **GO:0070787** *conidiophore development* (GO:0061794 is being obsoleted).

---

## The module

![h:440](conidiation-module-page.jpg)

<span class="small">modules/conidiation_regulatory_cascade.yaml (DRAFT): tiers, typed connections, per-annoton MFs, PANTHER PTN grounding.</span>

---

## Notable curation calls

- **REMOVE** FlbD: 4 plant-specific ARBA IEA rows (stomatal patterning, water homeostasis, salt and water-deprivation responses).
- **REMOVE** wA *laccase activity*: the cited paper (PMID:7050088) assigns the laccase to **yA**; reference marked MISCITED.
- **Over-annotated**: *sterigmatocystin biosynthetic process* on regulators BrlA, VelB, FluG; biosynthesis terms on Gα FadA.
- **MODIFY** FadA *conidium formation* → *negative regulation of conidium formation* (GO:0075308).

---

## A review page

![h:440](flbD-review-table.jpg)

<span class="small">FlbD (Myb TF) review: family TF terms accepted; a propagated cell-cycle Myb row marked over-annotated.</span>

---

## Status and next steps

- ✅ Module built; 30/30 member genes reviewed (21 EMENI, 9 NEUCR); module deep research cached and checkable.
- ⬜ Cite (or drop) the ACON-3 → *con* gene step in the Neurospora variant.
- ⬜ Track the GO:0061794 obsoletion (go-ontology #32315); check `gocams/index.tsv` for conidiation models.
- ⬜ Consider spinning out structural output as a `conidial_wall_assembly` module.

**Read more:** `projects/CONIDIATION.md` · `modules/conidiation_regulatory_cascade.yaml` · `genes/EMENI/`, `genes/NEUCR/`
