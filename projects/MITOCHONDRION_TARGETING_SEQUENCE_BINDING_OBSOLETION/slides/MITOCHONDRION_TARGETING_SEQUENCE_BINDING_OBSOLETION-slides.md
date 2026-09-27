---
title: "Mitochondrion targeting sequence binding obsoletion"
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

# Mitochondrion targeting sequence binding: obsoletion

GO:0030943 → GO:0140436 mitochondrial signal sequence receptor activity, row by row

<span class="small">AI Gene Review · projects/MITOCHONDRION_TARGETING_SEQUENCE_BINDING_OBSOLETION · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- GO **obsoleted GO:0030943**; the receptor term the project waited for now exists as **GO:0140436** (OLS, 2026-09-26).
- Only some of the **18 curated rows** are true presequence receptors (TOM20/22, likely TIM50); channels, a plant protein and the TIM23 complex need individual calls.
- **10 reviews** here touch the old term, **5 in `core_functions`**. All fixed in **#3234 (open)**: receptors → **GO:0140436**, channels TOMM40 and TIM22 → **GO:0008320**.

---

## Old term → replacement, by class

![h:480](term-map.svg)

---

## Receptors versus channels

![h:470](import-route.svg)

---

## Why no blanket replaced_by

- **TOM20 / TOM22** read the amphipathic presequence on the cytosolic face: a receptor, a clean fit.
- **TIM50** hands the presequence to TIM23 in the intermembrane space: receptor-like.
- **TIM23** is the channel: receptor MF, or a transporter feeding the import process?
- **TIM22** imports carriers with **internal** signals, not presequences.
- **PAP2** (Arabidopsis, IPI) and the **TIM23 complex** records need case-by-case calls.
- About **12,091** IEA/IBA rows sit on the term; pipelines will need reseeding.

---

## The 10 reviews that touch GO:0030943 (fixed in #3234, open)

| Review | Rows on GO:0030943 | Action before → after #3234 (open) | core_functions |
|---|---|---|---|
| human TOMM20 | IDA, IBA; replacement target | ACCEPT → MODIFY to GO:0140436 | → GO:0140436 |
| human TOMM22 | IDA | ACCEPT → MODIFY to GO:0140436 | → GO:0140436 |
| human TOMM70 | IBA, ISS | ACCEPT → MODIFY to GO:0140436 | no |
| human TIMM50 | NAS | NEW row → GO:0140436 | → GO:0140436 |
| worm tomm-22 | ISS | NEW row → GO:0140436 | → GO:0140436 |
| yeast TOM22 | none | | → GO:0140436 |
| human TOMM40 | IBA | ACCEPT → MODIFY to GO:0008320 (channel) | no |
| yeast TIM22 | IDA, IBA | ACCEPT → MODIFY to GO:0008320 (channel) | no |
| human TIMM22 | IBA | MARK_AS_OVER_ANNOTATED (kept, note added) | no |
| yeast ACL4 | IBA | UNDECIDED (kept, note added) | no |

---

## Status and next steps

- **2026-05-28:** project created; the replacement term was not yet in OLS.
- **2026-09-26:** GO:0030943 obsolete, **GO:0140436 live**. Local `cache/ontologies/go.tsv` still lists the old term as live, so validation is quiet.
- **2026-09-26 (later):** MODIFY pass fixed in **#3234 (open)**: 8 GOA rows ACCEPT → MODIFY; every author-supplied GO:0030943 now GO:0140436, so **TOMM20** no longer proposes the obsolete id for its GO:0051082 row. TIMM22 and ACL4 keep their actions with a note.
- Next: merge #3234; upstream PAP2 and TIM23-complex rows are for GO curators.
- Coordinate with the **MITOCHONDRIAL_IMPORT_PATHWAYS** project.

**Upstream:** go-annotation#6437 · go-ontology#32142 · #31711
**Read more:** `projects/MITOCHONDRION_TARGETING_SEQUENCE_BINDING_OBSOLETION.md`
