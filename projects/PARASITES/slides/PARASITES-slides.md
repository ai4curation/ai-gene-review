---
title: "Parasites: GO review of genes at the host interface"
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

# Parasites

GO review of nematode genes that work at the host interface

<span class="small">AI Gene Review · projects/PARASITES · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- Parasites invade hosts, evade immunity and steal nutrients; these functions are **thinly covered by GO**, and parasite species have **few reviewed UniProt entries**.
- We anchored on *S. carpocapsae* **nas-8** (the genus's only Swiss-Prot entry) and **five *Brugia malayi*** secreted or surface proteins.
- **All 6 reviewed: 35 GOA rows**, 21 ACCEPT. Key fix: a CPI-2 **aspartic-type** inhibitor row → **cysteine-type**, since legumain is a cysteine protease.

---

## Why these species

![h:470](reviewed-entries.svg)

---

## What the six proteins do at the host interface

![h:500](host-interface.svg)

---

## Review outcomes

| Gene | Species | Rows | ACCEPT | Non-core | Over-ann. | MODIFY | REMOVE |
|---|---|---|---|---|---|---|---|
| nas-8 | *S. carpocapsae* | 6 | 4 | 1 | 1 | 0 | 0 |
| cpi-2 | *B. malayi* | 6 | 3 | 1 | 0 | 1 | 1 |
| far-1 | *B. malayi* | 5 | 4 | 0 | 1 | 0 | 0 |
| dpy-31 | *B. malayi* | 6 | 4 | 1 | 1 | 0 | 0 |
| gp29 | *B. malayi* | 5 | 3 | 1 | 1 | 0 | 0 |
| mf1 | *B. malayi* | 7 | 3 | 2 | 0 | 2 | 0 |

<span class="small">From <code>genes/{STECR,BRUMA}/&lt;gene&gt;/&lt;gene&gt;-ai-review.yaml</code>. Over-annotations are generic parents (metallopeptidase, peroxidase, lipid binding); mf1 MODIFYs move to chitinase and chitin catabolism.</span>

---

## A mis-typed protease inhibitor

![h:420](cpi-2-review-table.jpg)

<span class="small">cpi-2: the IDA row from PMID:15664654 said <em>aspartic-type</em>; the target (AEP/legumain) is a cysteine peptidase, so it becomes GO:0004869. Above it, the TreeGrafter <em>cytoplasm</em> row is removed for a secreted protein.</span>

---

## Status and next steps

- ✅ 6/6 seed genes reviewed and rendered (the project page's "PENDING" labels are out of date).
- ⬜ No deep research or notes files yet; reviews rest on UniProt and cached papers.
- ⬜ *S. hermaphroditum* (`9BILA`): no seed chosen, no reviewed entries; will need literature + bioinformatics.
- ⬜ Fold in the host-modulator candidates from [PARASITE_IMMUNE_MODULATORS](../../PARASITE_IMMUNE_MODULATORS.md).

**Read more:** `projects/PARASITES.md` · `genes/BRUMA/` · `genes/STECR/nas-8/`
