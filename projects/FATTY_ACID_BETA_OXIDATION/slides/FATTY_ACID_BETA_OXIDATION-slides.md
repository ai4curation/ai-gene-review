---
title: "Mitochondrial fatty acid β-oxidation: a cross-species review"
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

# Mitochondrial fatty acid β-oxidation

Reviewing the GO annotations of the whole enzyme spiral in human, fly and mouse

<span class="small">AI Gene Review · projects/FATTY_ACID_BETA_OXIDATION · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- β-oxidation strips **two carbons per turn** through four steps, each run by **chain-length-specific** enzymes.
- We reviewed **713 GO annotations on 27 genes** (10 human, 16 fly, mouse LCAD) and built a **cross-species module**.
- **389 accepted, 237 non-core, 23 over-annotated, 30 modified, 14 removed, 20 undecided**. Six blinded OpenScientist runs **agreed** with the reviews.

---

## Who runs each step, by chain length

![h:520](fao-spiral.svg)

---

## Why this pathway

- One short, well-understood cycle that still concentrates **five recurring curation problems**:
  - **chain-length specificity**: use the specific MF where GO has one (VLCAD `GO:0017099`, MCAD `GO:0070991`, SCAD `GO:0016937`)
  - **cross-gene transfer**: SOAT cholesterol-esterification rows on the ACAT1 thiolase
  - **moonlighting**: HADH inhibits GLUD1; HADHA remodels cardiolipin
  - **organelle**: mitochondrion vs peroxisome
  - **GO↔RHEA mapping**: `GO:0004300` maps to the (3E) reaction, not the (2E) crotonase

---

## What a review looks like

![h:450](acadvl-review-table.jpg)

<span class="small">ACADVL review page. The IBA very-long-chain ACAD activity is accepted; substrate binding is kept as non-core. Six IEA/ISS lipid-regulation rows transferred from mouse <em>Acadvl</em> (the true ortholog, not LCAD) are left undecided pending the mouse knockout evidence.</span>

---

## Results

| Set | Genes | Ann. | ACCEPT | Non-core | Over-ann. | MODIFY | REMOVE | UNDECIDED |
|---|---|---|---|---|---|---|---|---|
| Human core spiral | 10 | 442 | 251 | 124 | 10 | 24 | 14 | 19 |
| Fly spiral + scully | 11 | 196 | 92 | 88 | 9 | 6 | 0 | 1 |
| Fly auxiliary isomerases | 5 | 33 | 24 | 8 | 1 | 0 | 0 | 0 |
| Mouse Acadl (LCAD) | 1 | 42 | 22 | 17 | 3 | 0 | 0 | 0 |

<span class="small">Counts from the review YAMLs. Human UNDECIDED: ACADVL 6, ACAT1 6, ACADM 4, ACAD9 2, ACADS 1; fly: Egm. No NEW annotations.</span>

---

## Blinded checks agree with the reviews

| Question | OpenScientist verdict |
|---|---|
| fly Acat1 peroxisomal? | Refuted: -EKL is not a PTS1; LOPIT says mitochondrion |
| fly Mtpalpha peroxisomal? | Supported: fly-specific SKL PTS1, isoform-dependent targeting |
| ACAD9 very-long-chain? | No: Thr-139/Ala-143 channel fits C16–C18 → long-chain |
| fly CG4860 short-chain? | Over-specific: pocket Leu→Thr → general ACAD |
| fly Echs1, Mcad substrate range | Conserved pockets; human-like range |
| fly step ③ = scully? | Yes: 100% of 11 catalytic residues conserved |

---

## The cross-species module

![h:440](fao-module-page.jpg)

<span class="small">modules/fatty_acid_beta_oxidation.yaml grounds each step in a human and a fly enzyme; its QC reports every grounded gene reviewed.</span>

---

## Status and next steps

- ✅ Human spiral (10), fly spiral + auxiliary enzymes (16), mouse Acadl; module built; Reactome cross-check done.
- ⬜ Remaining **mouse** orthologs (Acadvl, Acadm, Hadha, …), then rat and worm.
- ⬜ **Fly DECR1**: no ortholog assignable from NCBI, UniProt, Ensembl or OrthoDB.
- ⬜ FlyBase has taken **one** annotation from PMID:40519079; Arc42/CG4860 candidates listed.
- ⬜ Schema: no way to **negate an existing positive** annotation (CG4860 case).

**Read more:** `projects/FATTY_ACID_BETA_OXIDATION.md` · `modules/fatty_acid_beta_oxidation.yaml`
