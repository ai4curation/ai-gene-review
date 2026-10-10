---
title: "PINK1-Parkin mitophagy: a scoped project"
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

# PINK1-Parkin mitophagy

Selective autophagy of damaged mitochondria in human: a scoped project

<span class="small">AI Gene Review · projects/MITOPHAGY · SCOPING · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- **Scoped; kinase/E3 center still missing.** No mitophagy module; **PINK1 and PRKN are not reviewed**.
- **8 of 14 listed candidates** already have reviews made for other projects (mostly Proteostasis).
- Those reviews make mitophagy **core** for OPTN, CALCOCO2, BNIP3L and VCP and **non-core** for SQSTM1.

---

## The pathway

![h:470](pink1-parkin-pathway.svg)

<span class="small">Schematic from the pathway architecture on the project page.</span>

---

## Why this is worth doing

- The best-characterised mitophagy pathway, with **Parkinson's disease** (PINK1, PRKN) and **ALS** (OPTN, TBK1) genetics.
- Receptors are shared with xenophagy and aggrephagy, so **which selective-autophagy process is core** is the real curation question.
- A worm counterpart, **CAEEL_MITOPHAGY**, is already mature and could be compared ortholog by ortholog.

---

## Where the candidate genes stand

![h:470](candidate-coverage.svg)

---

## What the existing reviews say about mitophagy

| Gene | Mitophagy row | Evidence | Action |
|---|---|---|---|
| OPTN | GO:0061734 type 2 mitophagy | IMP | ACCEPT |
| CALCOCO2 | GO:0000423 mitophagy | IMP | NEW |
| SQSTM1 | GO:0000423 mitophagy | IGI, IBA | KEEP_AS_NON_CORE |
| BNIP3L | GO:1901524 regulation of mitophagy | IEA | ACCEPT |
| VCP | GO:0000423 mitophagy | IDA | ACCEPT |

---

## Next steps

1. `just fetch-gene human PINK1` and `PRKN`; review them first.
2. Review BNIP3, FUNDC1, PHB2 and MFN2.
3. Build a PINK1-Parkin mitophagy module from the reviewed genes, checking against the worm project.

**Read more:** `projects/MITOPHAGY.md` · `genes/human/OPTN/` · `projects/CAEEL_MITOPHAGY.md`
