---
title: "Plant bioenergy modules"
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

# Plant bioenergy modules

Taxon-neutral modules for cell-wall recalcitrance and seed oil

<span class="small">AI Gene Review · projects/PLANT_BIOENERGY · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- Biofuel yield depends on **cell-wall recalcitrance** (lignin, xylan acetylation, cellulose crystallinity) and, for oilseeds, **triacylglycerol** flux and packaging.
- We curated **three new modules** (lignin, xylan, seed TAG; PR #2066) and grouped them with the existing **cellulose** and **photosynthesis** modules.
- All five validate and are **DRAFT**; together they ground **48 UniProt exemplars**. Feedstock-species gene reviews **have not started**.

---

## The five modules

![h:470](bioenergy-modules.svg)

---

## Why modules first

- The enzymes are well characterized in **Arabidopsis**, but the feedstocks are **poplar, sorghum, maize, rice, soybean**.
- A taxon-neutral module gives each later ortholog review a **shared, verified map** of steps and GO terms.
- Identifiers are grounded **only where verified**; members are exemplars, not species restrictions.

---

## Module inventory

| Module | Scope | UniProt exemplars | Status |
|---|---|---|---|
| Lignin (monolignol) | PAL → CAD grid, export, radical coupling | 14 | DRAFT |
| Xylan | IRX9/10/14 backbone, GUX, GXM, O-acetylation | 10 | DRAFT |
| Seed TAG | Kennedy pathway, PDAT, oleosins | 9 | DRAFT |
| Cellulose | CESA rosettes, KORRIGAN, COBRA | 9 | DRAFT |
| Photosynthesis | light reactions + CBB cycle | 6 | DRAFT |

<span class="small">Distinct UniProtKB ids counted in each modules/*.yaml.</span>

---

## A module page

![h:430](lignin-module-page.jpg)

<span class="small">pages/modules/lignin_monolignol_biosynthesis.html: grounded in GO:0009809 lignin biosynthetic process, with Arabidopsis exemplars such as PAL1 and C4H.</span>

---

## Engineering levers

| Use case | Module(s) | Lever |
|---|---|---|
| Lignocellulosic sugars | lignin, xylan, cellulose | lower lignin, raise S/G, less acetylation, alter crystallinity |
| Fewer fermentation inhibitors | xylan | reduce O-acetylation (acetate) |
| Biodiesel / oleochemicals | seed TAG | DGAT/PDAT flux, oil-body capacity |
| Feedstock productivity | photosynthesis | upstream carbon assimilation |

---

## Status and next steps

- ✅ Five modules curated and validated (all DRAFT).
- ⬜ Grass-specific modules: mixed-linkage glucan (CSLF/CSLH), arabinoxylan arabinosylation / feruloylation.
- ⬜ Suberin and cutin biosynthesis.
- ⬜ Per-gene reviews for poplar / sorghum orthologs of the exemplar enzymes.

**Read more:** `projects/PLANT_BIOENERGY.md` · `modules/{lignin_monolignol,xylan,seed_triacylglycerol,cellulose}_biosynthesis.yaml`
