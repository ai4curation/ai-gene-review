---
title: "Protein localization to ER exit site obsoletion"
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

# Protein localization to ER exit site obsoletion

GO:0070973 → five destinations, chosen per annotation

<span class="small">AI Gene Review · projects/ER_EXIT_SITE_LOCALIZATION_OBSOLETION · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- GO **obsoleted GO:0070973** because curators used it for four different roles; there is **no single replacement**.
- The **10 curated annotations** each get their own term: COPII coat assembly, ER→Golgi transport, its regulation, ER stress, or deletion.
- In this repo, **BCAP31 is already aligned** and yeast **YET2** only has the same IBA in its cached UniProt record; **LRRK2's two ACCEPT rows now MODIFY to GO:0060628**, fixed in #3241 (open).

---

## Why the term went

- The name says **where a protein ends up**, not what process it takes part in.
- It was applied to COPII scaffolds, cargo receptors, a kinase regulator and ER quality-control chaperones.
- OLS obsoletion note: replacements "depend on the specific biological context".
- One UniRule mapping (`UR001349783`) propagated it to **~14,414 annotations**, mostly IEA and IBA.

---

## Four roles at the ER exit site

![h:470](eres-roles.svg)

---

## One term, five destinations

![h:480](term-split.svg)

---

## Curated rows to move

| Gene | Organism | Evidence | Destination |
|---|---|---|---|
| SEC16A · sec-16A.1 · SEC16 | human · worm · yeast | IMP | GO:0048208 |
| MIA3 · GBF1 | human | IMP | GO:0006888 / vesicle transport |
| LRRK2 | human | IMP (PMID:25201882) | GO:0060628 |
| Bcap29 · Bcap31 | mouse | IGI | GO:0034976 or child |
| Lrrk2 · Tb03.28C22.610 | mouse · *T. brucei* | IMP | delete (redundant) |

<span class="small">From QuickGO (2026-05-29) and the go-ontology#19122 plan.</span>

---

## Repo impact

| Review | GO:0070973 rows | Current action | Needed |
|---|---|---|---|
| `genes/human/LRRK2` | IEA (GO_REF:0000120), IMP (PMID:25201882) | ACCEPT → MODIFY ×2 | **→ GO:0060628**, fixed in #3241 (open) |
| `genes/human/BCAP31` | IBA (GO_REF:0000033) | MARK_AS_OVER_ANNOTATED | none |
| `genes/yeast/YET2` | IBA, cached UniProt record only (not in GOA file) | not reviewed | none; same PTN000294723 node |

- SEC16A, MIA3 and GBF1 have **no review** here yet.

---

## Next steps

1. Merge #3241 (open): both LRRK2 GO:0070973 rows already MODIFY to **GO:0060628**.
2. Optional: review **SEC16A**, **MIA3**, **GBF1** as clean cases for the three main replacement terms.
3. Flag UniRule **UR001349783** for retargeting so the IEA tail does not re-propagate.

**Upstream:** go-annotation#6434 · go-ontology#19122 · go-annotation#6172
**Read more:** `projects/ER_EXIT_SITE_LOCALIZATION_OBSOLETION.md`
