---
title: "MicroRNA degradation: the TDMD machinery"
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

# Target-directed microRNA degradation

Reviewing the ZSWIM8 ligase axis and its Argonaute substrates

<span class="small">AI Gene Review · projects/MIRNA_DEGRADATION · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- In **TDMD**, the **ZSWIM8–CUL3** ligase recognizes AGO-miRNA complexes bound to a highly complementary **trigger RNA** and ubiquitylates AGO, which leads to loss of the miRNA.
- We reviewed the **9 human proteins** of that layer (ZSWIM8, CUL3, ARIH1, ELOB, ELOC, AGO1–4): **1,106 annotations**.
- ZSWIM8 now points at **`GO:0140958` target-directed miRNA degradation** and a **Cul3**-RING complex; 139 of 143 removals are bare `protein binding` rows.

---

## The mechanism

![h:490](tdmd-ligase.svg)

---

## Scope: the dedicated protein layer only

- **In:** ZSWIM8, CUL3, ARIH1, ELOB, ELOC (the ligase) and AGO1–4 (the substrate layer).
- **Context, not reviewed:** trigger RNAs and trigger-bearing transcripts (CYRANO, NREP, SERPINE1, HSUR1, fly AGO1 mRNA).
- **Out:** miRNA biogenesis (DROSHA, DICER1…), effector repression (TNRC6, CCR4-NOT), generic CRL/proteasome parts, and the TUT4/7–DIS3L2 tailing branch.
- Aim: keep **core TDMD function** separate from generic silencing and ubiquitin biology.

---

## What the reviews concluded

![h:480](actions-per-gene.svg)

---

## A TDMD-specific correction

![h:430](zswim8-review-table.jpg)

<span class="small">ZSWIM8: the IBA Cul2-RING complex row is modified to Cul3-RING, because CUL3, not CUL2, was required in the TDMD screen follow-up (PMID:33184234).</span>

---

## Key changes

- **ZSWIM8**: `positive regulation of miRNA catabolic process` (IDA ×2) → **`GO:0140958`** target-directed miRNA degradation; core MF `GO:1990756` ligase-substrate adaptor.
- **CUL3**: ligase and transferase activity rows → **`GO:0160072`** ubiquitin ligase complex scaffold activity; 78 rows over-annotated.
- **AGO4**: IBA **RNA endonuclease activity removed**, not supported as a physiological activity.
- **ELOB / ELOC**: 58 `protein binding` IPIs and two Pol II transcription-initiation rows, one per gene, removed.

---

## Status and next steps

- ✅ 9/9 human reviews exist; all are fully actioned; 6 are `COMPLETE`.
- ⬜ Finalize CUL3, AGO1 and AGO2 statuses.
- ⬜ Comparative fly / worm / mouse TDMD machinery.
- ⬜ Deferred: TUT4/TUT7–DIS3L2 branch; viral trigger subproject.
- ⬜ Track phase-2 decisions in ai4curation/ai-gene-review#4224.

**Read more:** `projects/MIRNA_DEGRADATION.md` · `projects/MIRNA_DEGRADATION/sources.md` · `genes/human/ZSWIM8/`
