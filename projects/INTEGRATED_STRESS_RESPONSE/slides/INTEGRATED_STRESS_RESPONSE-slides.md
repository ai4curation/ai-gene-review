---
title: "Integrated stress response: a scoped pathway project"
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

# The integrated stress response

A scoped project: about 18 candidate genes, five already reviewed

<span class="small">AI Gene Review · projects/INTEGRATED_STRESS_RESPONSE · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- Four kinases (**HRI, PKR, PERK, GCN2**) each sense a different stress and phosphorylate **eIF2α**, which blocks **eIF2B**, dampens translation and lets **ATF4** through.
- **Scoped, not yet started**: no project-specific review work has been done.
- **5 of 18** candidates already have reviews from other work (EIF2AK3, ATF4, ATF3, EIF2B4 COMPLETE; OMA1 IN_PROGRESS; 490 annotations). **EIF2S1**, three kinases and DELE1 have no gene folder.

---

## Four sensors, one switch

![h:500](isr-pathway.svg)

---

## Why this pathway

- A drug target: **ISRIB** binds a cleft in the eIF2B decamer (cryo-EM structure cited in the EIF2B4 review).
- **eIF2B mutations** cause vanishing white matter disease.
- The **DELE1-HRI** route from mitochondrial stress was described only in 2020, so GO may not yet reflect it.
- Clear convergence: four kinases → one substrate → one exchange factor → one transcription factor.

---

## An existing review: EIF2AK3 (PERK)

![h:430](eif2ak3-review-table.jpg)

<span class="small">Generic kinase rows are <b>MODIFY</b>'d to <em>eukaryotic translation initiation factor 2alpha kinase activity</em>; the review also proposes <em>integrated stress response signaling</em> (GO:0140467) as NEW.</span>

---

## Status and next steps

| Genes | State |
|---|---|
| EIF2AK3 (96 ann.), ATF4 (216), ATF3 (80), EIF2B4 (44) | COMPLETE |
| OMA1 (54) | IN_PROGRESS |
| EIF2AK1, EIF2AK2, EIF2AK4, EIF2S1, DELE1, DDIT3, PPP1R15A, PPP1R15B, EIF2B1/2/3/5, ASNS | No gene folder |

- ⬜ `just fetch-gene human <GENE>`, starting with **EIF2S1**, the other three kinases and **DELE1**.
- ⬜ An ISR module once the core is reviewed.

**Read more:** `projects/INTEGRATED_STRESS_RESPONSE.md`
