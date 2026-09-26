---
title: "Mitochondrial import pathways: one GO term per route"
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

# Mitochondrial import pathways

One GO process term per import route, and a review of the human import machinery

<span class="small">AI Gene Review · projects/MITOCHONDRIAL_IMPORT_PATHWAYS · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- Mitochondrial proteins reach their compartment by **six import routes**, but GO grouped them inconsistently; **GO issue #31711** proposed one term per route.
- GO has **added the route terms** (`GO:7770058`–`GO:7770063`) and reworded `GO:0030150` and `GO:0160203`.
- We reviewed **670 annotations on 23 human genes** of the machinery; only **MTCH2** yet carries a new route term.

---

## Six routes, six terms

![h:520](import-routes.svg)

---

## Why this project

- GO-CAM models of import need **one process per route**, so that TOM → SAM and TOM → TIM23 → PAM are not the same step.
- Old terms mixed **destination** and **machinery**, and grouping terms (e.g. `GO:0070585` protein localization to mitochondrion) collected annotations that belong to a specific route.
- Reviewing the machinery shows which annotations would move to the new terms.

---

## Actions per gene

![h:520](import-actions.svg)

---

## Findings

1. **`protein binding` IPI** rows removed on TOMM70 (11), CHCHD4 (5), TOMM40 (3), MTCH2 (3).
2. **Localization refined**: SAMM50 *mitochondrion* → *mitochondrial outer membrane*; PMPCA → *mitochondrial matrix*.
3. **Wrong route**: SAMM50 *protein import into mitochondrial matrix* → *protein insertion into mitochondrial outer membrane*.
4. **CHCHD4** *protein-disulfide reductase* → *disulfide oxidoreductase activity*: MIA40 oxidises its substrates.
5. **MTCH2** gains NEW `GO:7770059` α-helical OM insertion, matching MTCH1 and yeast MIM1.

---

## What a review looks like

![h:430](mtch2-review-table.jpg)

<span class="small">MTCH2 review: the IBA <em>mitochondrion</em> row is marked over-annotated because the direct outer-membrane annotation says more; the propagation review records why.</span>

---

## Status and next steps

- ✅ Issue #31711 read; 23 priority genes fetched and reviewed (the page checklist predated most of them).
- ✅ GO added the route terms and reworded the matrix and IMS terms.
- ⬜ Move reviews onto the new terms: TIMM22 → `GO:7770061`, SAMM50/MTX → `GO:7770063`, TIMM21 → `GO:7770060`.
- ⬜ Two grouping terms proposed for obsoletion, `GO:0070585` and `GO:0072656`, are still live in GO.

**Read more:** `projects/MITOCHONDRIAL_IMPORT_PATHWAYS.md` · `genes/human/<GENE>/`
