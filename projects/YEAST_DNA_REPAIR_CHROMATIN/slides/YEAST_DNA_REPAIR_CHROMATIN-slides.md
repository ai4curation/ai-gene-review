---
title: "Yeast DNA repair and chromatin: where the review stands"
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

# Yeast DNA repair and chromatin

Reviewing GO annotations for 26 *S. cerevisiae* repair and chromatin genes

<span class="small">AI Gene Review · projects/YEAST_DNA_REPAIR_CHROMATIN · in progress</span>

---

<!-- _class: bluf -->

## Bottom line

- The plan covers **26 genes**: checkpoint signalling, homologous recombination, FACT and remodelers, mismatch repair, translesion synthesis and dNTP supply.
- **4 of 26 reviewed**, all on the chromatin side: **SPT16, POB3, CHD1, SWI1** (191 existing annotation rows, plus 1 proposed NEW term).
- Almost every row was accepted or kept as non-core; **4 REMOVE**. The recombination, checkpoint and mismatch-repair genes have **no review yet**.

---

## The biology in one picture

![h:500](hr-chromatin.svg)

---

## Why this set

- Repair proteins act on **chromatin, not naked DNA**, so the interesting annotations sit where repair and nucleosome handling meet.
- FACT (SPT16–POB3) and the remodelers CHD1 and SWI/SNF carry both **transcription** and **repair** annotations; the review has to decide which are core.
- The recombination genes (MRX, RAD51, RAD52, RAD54) are some of the best-characterised proteins in yeast, a strong test for over-annotation.

---

## What the four reviews decided

![h:470](actions.svg)

---

## Example rows

- <span style="color:#bd3a30">**REMOVE**</span> CHD1 `GO:0005739` mitochondrion (two HDA rows): CHD1 is a nuclear remodeler.
- **UNDECIDED** CHD1 `GO:0140002` histone H3K4me3 reader activity: conflicting yeast literature.
- <span style="color:#bd3a30">**REMOVE**</span> POB3 `GO:0003677` DNA binding (IEA from the SSRP1/POB3 InterPro domain).
- <span style="color:#1d68b3">**NEW**</span> SWI1 `GO:0031491` nucleosome binding, from cryo-EM structures of SWI/SNF on a nucleosome.

---

## What a review looks like

![h:450](chd1-review-table.jpg)

<span class="small">CHD1 review page: nucleus accepted; the IBA histone binding row kept as non-core, since CHD1 engages nucleosomes mainly through DNA.</span>

---

## Status and next steps

- ✅ Reviewed: `genes/yeast/{SPT16,POB3,CHD1,SWI1}/`
- ⬜ 22 genes with no folder: MRX + SAE2, RAD51/52/54/55/57, RAD9, CHK1, DUN1, MSH2/MSH6/MLH1/PMS1, RAD3, REV3, RNR1–4.
- Fix checklist labels first: yeast 9-1-1 is **Ddc1–Rad17–Mec3**; RAD3 and REV3 are not base excision repair; DUN1 is listed twice.

**Read more:** `projects/YEAST_DNA_REPAIR_CHROMATIN.md`
