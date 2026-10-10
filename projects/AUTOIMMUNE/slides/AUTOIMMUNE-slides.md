---
title: "Autoimmune genetics: reviewing GO annotations for 20 risk genes"
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

# Autoimmune genetics: greatest hits

Reviewing every GO annotation on 20 shared autoimmune risk genes

<span class="small">AI Gene Review · projects/AUTOIMMUNE · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- 20 immune-regulation genes carry risk variants for **several autoimmune diseases at once** (T1D, RA, MS, IBD, SLE).
- We reviewed **2,303 GO annotation rows** (2,287 existing plus 16 proposed NEW); every row is actioned and all 20 reviews validate.
- **1,464 accepted**, **180 removed** (150 of them generic `protein binding`, mostly on STAT3 and SMAD3), **16 NEW**. Review files are not all finalised: 10 COMPLETE, 5 DRAFT, 5 IN_PROGRESS.

---

## Where the genes act

![h:500](autoimmune-pathways.svg)

---

## Why these genes

- Chosen as the most strongly replicated, functionally validated autoimmune risk loci (Tier 1: 11 genes) plus well-established risk genes (Tier 2: 9).
- Six pathway groups: T cell activation and inhibition, Th1/Th2 polarisation, Th17/Treg balance, NF-kB/TNF, tolerance, ER sphingolipid control.
- Several are among the most heavily annotated immune genes: **STAT3 456 rows**, **SMAD3 349**, **GATA3 258**.

---

## Actions per gene

![h:500](autoimmune-actions-chart.svg)

---

## What a review looks like

![h:430](ormdl3-review-table.jpg)

<span class="small">ORMDL3 review page: sphingolipid biosynthesis (IBA) accepted as core; ORMDL3 is the ceramide-sensing regulatory subunit of serine palmitoyltransferase.</span>

---

## Findings

1. **`protein binding` IPI removed en masse**: 150 of 180 REMOVEs; STAT3 66, SMAD3 68, GATA3 7.
2. **Propagation errors removed**: IL23R *prolactin receptor activity* (IBA) and *prolactin signaling pathway* (IEA).
3. **ORMDL3 gets its real function** as NEW terms: *enzyme inhibitor activity*, *ceramide binding*, *negative regulation of sphingolipid biosynthetic process*; generic TAS membrane locations removed.
4. **UNDECIDED resolved** for IL4, IL7R, CD28 and IL10 once publications were cached; 11 remain.

---

## Status and next steps

- ✅ 20/20 reviews actioned and validating (0 errors).
- ⬜ Finalise review status: 5 DRAFT, 5 IN_PROGRESS (#4041).
- ⬜ Validator warnings: GO:0005515 policy, Falcon evidence links, BACH2/EGR2 core coverage.
- ✅ The STAT3 deep-research to-do is done (`STAT3-deep-research-falcon.md`).

**Read more:** `projects/AUTOIMMUNE.md` · `genes/human/<GENE>/`
