---
title: "Mechanobiology: scoping a gene review of force sensing"
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

# Mechanobiology

Scoping a GO review of the genes that sense and transmit force

<span class="small">AI Gene Review · projects/MECHANOBIOLOGY · scoping · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- Cells sense stiffness, shear, stretch and membrane tension through **PIEZO channels, integrin adhesions, the nuclear lamina and YAP/TAZ**; GO mixes true sensors with generic adhesion and ECM terms.
- The page defines **inclusion criteria, six modules and 30 candidate genes** in five batches, and a `stimulus → sensor → axis → phenotype` chain for every review.
- **Scoped, not started.** No Batch A–D gene has a review; four matrix genes (FN1, LOX, SPARC, DCN) were reviewed for other purposes.

---

## The landscape to review

![h:520](mechano-chain.svg)

---

## Why scope it this way

- Separate the **few direct sensors** from the many effectors and ECM genes.
- Watch for over-broad terms: `cell adhesion`, `ECM organization`, `actin binding`, `response to mechanical stimulus`.
- Prefer evidence from a **defined mechanical perturbation**, not a generic migration or adhesion assay.
- Use disease anchors (fibrosis, invasion, endothelial flow, kidney cilia) to pick batches, not to make claims.
- Adapted from [cmungall/stuff#671](https://github.com/cmungall/stuff/issues/671), minus the ontology and platform ambitions.

---

## Where the candidates stand

![h:500](batch-status.svg)

---

## Status and next steps

- ⬜ Batch A: PIEZO1, PIEZO2, TRPV4, PKD1, PKD2 (`just fetch-gene human <GENE>` then review).
- ⬜ Re-read FN1, LOX, SPARC, DCN against the mechanical-chain questions.
- ⬜ Batches B–D, then a stimulus / sensor / axis / phenotype summary table.
- ⬜ List recurring GO pain points only after several batches.

**Read more:** `projects/MECHANOBIOLOGY.md`
