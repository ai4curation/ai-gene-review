---
title: "Mevalonate pathway term obsoletion"
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

# Mevalonate pathway terms: obsoletion

GO:1902767 and GO:0010142 → GO:0019287 (to IPP) or GO:0045337 (IPP → FPP)

<span class="small">AI Gene Review · projects/MEVALONATE_PATHWAY_OBSOLETION · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- GO **obsoleted two overlapping mevalonate-route terms**; each old row must go to **GO:0019287** or **GO:0045337** depending on the step the gene catalyses.
- The human pathway is now **reviewed here** (HMGCS1, HMGCR, MVK, PMVK, MVD, IDI1, FDPS; PRs #1998, #2153): MVK, PMVK, MVD accept GO:0019287 and FDPS accepts GO:0045337.
- **Last 3 rows fixed in #3232 (open):** yeast **ERG19** (1 RCA row) KEEP_AS_NON_CORE → **MODIFY to GO:0019287**; rat **Hmgcs2** (2 rows) stays **UNDECIDED** with the obsoletion noted.

---

## Old terms → replacements

![h:480](term-map.svg)

---

## One route, two replacement terms

![h:470](pathway-split.svg)

---

## Why it is a judgement, not a relabel

- Both obsolete terms covered the **whole route** from acetyl-CoA through mevalonate to FPP.
- The replacements split it at **IPP**: GO:0019287 for the upper steps, GO:0045337 for FDPS chemistry.
- A kinase or decarboxylase row belongs on GO:0019287; an FDPS row on GO:0045337; some genes may need both.
- Upstream lists: **2 EXP** on GO:1902767 (1 EcoCyc left), **21 EXP** on GO:0010142 across 16 genes.
- *E. coli* uses the MEP pathway, so the **yajO** row is a removal candidate, not a remap.

---

## What is in the repo

| Gene | Relevant rows | Action |
|---|---|---|
| human MVK, PMVK, MVD | GO:0019287 IBA + IEA | ACCEPT |
| human FDPS | GO:0045337 IBA + IEA | ACCEPT |
| human HMGCS1, HMGCR, IDI1 | reviewed; no row on either replacement | – |
| rat Hmgcs2 | GO:0010142 IBA + IEA | UNDECIDED (obsoletion noted; #3232, open) |
| yeast ERG19 | GO:0010142 RCA; GO:0019287 IEA | MODIFY → GO:0019287 (#3232, open); ACCEPT |

Modules: `modules/mevalonate_pathway.yaml` (grounded on GO:0019287) and `modules/isoprenoid_diphosphate_biosynthesis.yaml`.

---

## Status and next steps

- **2026-06-06:** project created; only rat Hmgcs2 then carried an obsolete-term row.
- **2026-07:** human pathway reviews and modules added (PRs #1998, #2153).
- **2026-09-26:** OLS lists **both terms obsolete**.
- **2026-09-26 (later):** ERG19 and Hmgcs2 rows settled in #3232 (open).
- Next: identify the remaining EcoCyc row (possibly yajO).

**Upstream:** go-annotation#6440, #6439 · go-ontology#32082
**Read more:** `projects/MEVALONATE_PATHWAY_OBSOLETION.md`
