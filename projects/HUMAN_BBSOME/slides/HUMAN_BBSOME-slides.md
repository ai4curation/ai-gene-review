---
title: "Human BBSome: reviewing a ciliary coat complex"
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

# The human BBSome

Reviewing GO annotations for the 14 genes of a ciliary coat complex

<span class="small">AI Gene Review · projects/HUMAN_BBSOME · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- The **BBSome** is an 8-subunit coat that sorts GPCRs and Hedgehog components **into and out of the primary cilium**; its loss causes **Bardet–Biedl syndrome**.
- We reviewed **every GO annotation** on **14 genes** (8 subunits, ARL6 recruiter, 2 regulators, 3 assembly chaperonins) and built a reusable **BBSome module**.
- **Main corrections:** `protein binding` → BBSome membership or specific MF; chaperonins are **assembly factors, not subunits**; two over-propagated BBS2 IEA localizations **removed**.

---

## Who does what inside the complex

![h:500](bbsome-architecture.svg)

---

## Why this complex

- **Well bounded**: one complex, cryo-EM structures (2020), a clear disease.
- A test of whether per-gene review recovers the **division of labour**:
  - cargo recognition and ARL6 binding: **BBS1**
  - membrane recruitment: **ARL6-GTP**
  - assembly: **MKKS / BBS10 / BBS12 + CCT/TRiC**
- The failure mode to avoid: copying one generic "cilium" story onto every subunit.

---

## What a review looks like

![h:440](bbs1-review-table.jpg)

<span class="small">BBS1 review page: each GOA row gets an action and a reason. BBSome membership is accepted; a propagated "patched binding" row is marked over-annotated.</span>

---

## Results across 14 genes

| Gene | Ann. | ACCEPT | Non-core | Over-ann. | MODIFY | REMOVE |
|---|---|---|---|---|---|---|
| BBS1 | 60 | 30 | 18 | 7 | 5 | 0 |
| BBS2 | 67 | 16 | 24 | 25 | 0 | 2 |
| BBS4 | 110 | 42 | 37 | 31 | 0 | 0 |
| MKKS | 61 | 5 | 23 | 30 | 2 | 0 |
| TTC8 | 47 | 23 | 10 | 14 | 0 | 0 |
| BBIP1 | 24 | 13 | 8 | 3 | 0 | 0 |

<span class="small">Six of 14 shown; full table in projects/HUMAN_BBSOME.md.</span>

---

## Cross-cutting findings

1. **`protein binding` (GO:0005515)** IPI rows flagged throughout; biology captured by **GO:0034464 BBSome** or specific MF (BBS1 → *small GTPase binding* for ARL6).
2. **Chaperonins are not subunits**: MKKS, BBS10, BBS12 get GO:0044183 *protein folding chaperone*, replacing obsolete GO:0051082.
3. A **GO:0061629** *RNA Pol II TF binding* row from a BBS7-centric study (PMID:22302990) was flagged as miscited across the scaffold subunits.
4. **BBS2** `microvillus` / `stereocilium` IEA rows **removed** as unsupported.

---

## The BBSome module

![h:440](bbsome-module-page.jpg)

<span class="small">modules/bbsome.yaml: composition, assembly, ARL6 recruitment and cargo trafficking, grounded in GO:0034464.</span>

---

## Status and next steps

- ✅ 14/14 gene reviews validate; module validates.
- ⬜ Pathway/summary integration (optional).
- Out of scope, candidates for their own modules: **IFT** (IFT27/BBS19, IFT172/BBS20) and the **transition zone** (MKS1, CEP290).

**Read more:** `projects/HUMAN_BBSOME.md` · `modules/bbsome.yaml` · `genes/human/<GENE>/`
