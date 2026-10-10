---
title: "Prephenate pathway obsoletion"
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

# Prephenate pathway obsoletion

GO:0009095 → GO:0009094 L-phenylalanine and GO:0006571 L-tyrosine biosynthetic process

<span class="small">AI Gene Review · projects/PREPHENATE_PATHWAY_OBSOLETION · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- GO **obsoleted GO:0009095**, a pre-composed Phe + Tyr superpathway; the two component pathways already exist as separate terms.
- **4 experimental annotations** on 3 proteins must move; upstream proposes **removal for 3** and **GO:0009094 for Petunia PPA-AT**.
- **Scoped, not yet started:** none of the three proteins is reviewed in this repo.

---

## One superpathway, two existing terms

![h:480](term-map.svg)

---

## Where the annotated enzymes act

![h:480](pathway.svg)

---

## Why most rows are removals

- A move to a replacement is valid **only if the paper shows a role in Phe or Tyr biosynthesis** specifically.
- PMID:20883697 (Arabidopsis PAT) and PMID:18727669 (Rv0948c) are **biochemical or structural**: no process claim.
- Chorismate mutase acts **upstream of both branches**; mapping it to either needs in-vivo data.
- No InterPro2GO, UniProt keyword or UniRule mappings point at GO:0009095, so there is **no mapping fan-out**.

---

## Next steps

1. **Petunia PPA-AT (E9L7A5)** first: check Fig 1 of PMID:21102469 supports Phe specifically; record MODIFY → GO:0009094.
2. **Arabidopsis PAT (Q9SIE1)**: both rows, likely REMOVE.
3. **M. tuberculosis Rv0948c (P9WIC1)**: likely REMOVE.

Each starts with `just fetch-gene <organism> <gene>`.
**Upstream:** go-annotation#6395 + go-ontology#32005 (closed)
**Local tracker:** ai-gene-review#547
**Read more:** `projects/PREPHENATE_PATHWAY_OBSOLETION.md`
