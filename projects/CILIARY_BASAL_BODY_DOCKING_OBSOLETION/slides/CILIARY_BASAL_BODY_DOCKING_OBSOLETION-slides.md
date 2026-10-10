---
title: "Ciliary basal body docking obsoletion"
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

# Ciliary basal body docking obsoletion

GO:0097711 and GO:1905353 → GO:1905349 ciliary transition zone assembly

<span class="small">AI Gene Review · projects/CILIARY_BASAL_BODY_DOCKING_OBSOLETION · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- GO **obsoleted** basal body-plasma membrane docking and transition fiber assembly; both merge into **GO:1905349** ciliary transition zone assembly.
- **7 experimental rows** were affected: FlyBase, MGI, Reactome, UniProt and Xenbase reported fixes; ZFIN remains for upstream error reports.
- **Scoped, not yet started:** no affected gene is reviewed here; **CEP290** and **RAB3IP** are queued.

---

## Why docking was retired

- Upstream (go-ontology #31882): the "docking" term described the **whole multi-step build** of the transition zone, not one docking event.
- The mother centriole first docks to vesicles; transition zone assembly **begins with that step** (PMID:27646273).
- GO:1905353 transition fiber assembly had **no experimental annotations** and sat inside the same process.
- Fix type: terminological. The biology is unchanged.

---

## One process, not a separate docking event

![h:470](docking-steps.svg)

---

## Old terms → replacement, and where the rows go

![h:480](term-map.svg)

---

## What this means for the repo

- `grep` over `genes/`: **no GOA or review YAML uses GO:0097711 / GO:1905353.**
- CEP290, RAB3IP, FOXJ1 and pam have **no review folders** yet.
- Worm `mks-1` and `mks-3` (from `CAEEL_CILIOPATHY`) already propose **NEW GO:1905349** for the MKS transition-zone module (IMP / IGI, PMID:21422230).
- The anticipated tether MF now exists: **GO:7770062** vesicle membrane tethering activity (sibling `VESICLE_TETHERING_OBSOLETION`).

---

## Status and next steps

1. Review **human CEP290** (O15078) as the anchor: most-annotated gene under the old term, multi-ciliopathy gene.
2. Review **RAB3IP** (Q96QF0), Rab8 GEF for ciliary vesicle delivery.
3. Defer FOXJ1, fly Cep290 and zebrafish pam.

**Upstream:** go-annotation#6405 · go-ontology#31882
**Siblings:** `VESICLE_DOCKING_OBSOLETION` (#6379) · `VESICLE_TETHERING_OBSOLETION` (#6375)
**Page:** `projects/CILIARY_BASAL_BODY_DOCKING_OBSOLETION.md`
