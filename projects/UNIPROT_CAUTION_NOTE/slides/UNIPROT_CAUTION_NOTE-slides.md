---
title: "UniProt CAUTION notes as a GO review worklist"
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

# UniProt CAUTION notes

Using curators' written warnings to find over-annotated GO functions

<span class="small">AI Gene Review · projects/UNIPROT_CAUTION_NOTE · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- **14,830 CAUTION notes** on 14,513 reviewed UniProt entries; **7,219** flag contested, reclassified, pseudoenzyme, retracted or artifact functions.
- Two frozen Query A/B snapshots turn them into GO flags. Locally, strong flags matched curators' actions **8 of 11** times; UniProt-wide they **rediscovered known pseudoenzymes**.
- **13 human genes reviewed**; nine pseudoenzymes (CRMP family, ILK, ROR1, CASP12, AZIN2) each had an inferred catalytic row removed.

---

## What a CAUTION note is

- A free-text `CC -!- CAUTION:` comment in the UniProt flat file: the curator warns the reader.
- Distinct from the structured `SEQUENCE CAUTION` block (gene-model issues), which we exclude.
- Example (S. pombe Epe1): *"lacks the iron catalytic His … has no histone demethylase activity in vitro"*.
- These are exactly the cases where **IEA/IBA domain-to-function** mappings go wrong.

---

## What the notes are about

![h:470](caution-categories.svg)

---

## Query A: positive parent, NOT-ed child

![h:470](query-a-dpysl5.svg)

---

## Query B: the CAUTION paper, cited positively

- A CAUTION cites a PMID; GO uses the **same PMID** for a positive annotation, with no `NOT` from it.
- Frozen counts: 68 flags / 38 local genes; 1,140 UniProt-wide.
- Real catches: **CHMP1A** metallopeptidase from a mistranslated ORF (REMOVE); **ENDOU** serine peptidase from a refuted paper; **HDAC6** histone deacetylase.
- Over-flags: a paper makes several claims and only one is doubted. Needs activity-level matching, not PMID matching.

---

## Pseudoenzymes reviewed

| Gene | Removed inferred catalytic term | Real core role |
|---|---|---|
| DPYSL2/3, CRMP1, DPYSL5 | hydrolase activity (IEA) | cytoskeletal regulators, semaphorin signalling |
| DPYSL4 | cyclic-amide hydrolase (IBA); hydrolase parents UNDECIDED | same family |
| ILK | protein kinase activity | IPP-complex scaffold |
| ROR1 | protein kinase activity | Wnt coreceptor |
| CASP12 | cysteine-type peptidase activity | inflammasome modulator |
| AZIN2 | catalytic activity | antizyme inhibitor |

---

## Status and next steps

- Done: survey, 4,046-candidate worklist, Queries A/B local + UniProt-wide, **13 validated reviews**.
- Pending: report **9 local + 97 UniProt-wide** same-term GOA conflicts (positive and `NOT` on one term) upstream; audit **255** retracted-reference candidates; shrink the 7,605-note "other" bucket.
- Lesson: the GO `NOT` is the curated twin of a CAUTION. **CAUTIONs with no `NOT`** are the best targets.

**Read more:** `projects/UNIPROT_CAUTION_NOTE.md` · `projects/UNIPROT_CAUTION_NOTE/uniprot_wide_queries.md`
