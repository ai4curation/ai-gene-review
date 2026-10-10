---
title: "cGAS-STING: a scoped pathway project"
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

# cGAS-STING cytosolic DNA sensing

A scoped project: ten candidate genes, five already reviewed

<span class="small">AI Gene Review · projects/CGAS_STING_PATHWAY · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- **cGAS** senses cytosolic DNA and makes **2'3'-cGAMP**; **STING1** then recruits **TBK1** to activate **IRF3** and type I interferon.
- **Scoped, not yet started**: no project-specific review work has been done.
- **5 of 10** candidates already have complete reviews from other projects (CGAS, STING1, TBK1, IRF3, IFI16; 917 annotations).
- **TREX1**, **ENPP1**, **SAMHD1**, **IRF7** and **IFNB1** still have no review folder.

---

## The pathway and what is covered

![h:500](cgas-sting-pathway.svg)

---

## Why this pathway

- Links innate immunity to **type 1 interferonopathies** (AGS, SAVI), **lupus**, **cancer immunotherapy** (STING agonists) and **senescence**.
- Many regulators were described **after 2020** (STING trafficking and degradation, intercellular cGAMP transfer), so GO annotation may lag the literature.
- A bounded set of about ten genes with a clear sensor → messenger → adaptor → kinase → transcription factor order.

---

## An existing review: STING1

![h:430](sting1-review-table.jpg)

<span class="small">STING1 (251 annotations, COMPLETE): 165 ACCEPT, 31 MODIFY, 26 REMOVE (25 of them generic <code>protein binding</code>).</span>

---

## Status and next steps

| Gene | State |
|---|---|
| CGAS, STING1, TBK1, IRF3, IFI16 | Reviewed (COMPLETE), from other projects |
| TREX1, ENPP1, SAMHD1, IRF7, IFNB1 | No gene folder |

- ⬜ `just fetch-gene human <GENE>` for the five missing genes.
- ⬜ Review, then consider a cytosolic DNA sensing module.

**Read more:** `projects/CGAS_STING_PATHWAY.md`
