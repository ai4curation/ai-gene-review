---
title: "TreeGrafter: how good are automated PANTHER grafts?"
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

# TreeGrafter inference evaluation

How reviewers treated 1,074 automated PANTHER-graft GO annotations

<span class="small">AI Gene Review · projects/TREEGRAFTER · snapshot 2026-10-03 at `f81b9f300`</span>

---

<!-- _class: bluf -->

## Bottom line

- Reviewers **accepted 43%** of uncorroborated TreeGrafter IEA rows as-is; corpus-wide curated PAINT/IBA rows, on a mostly different gene set, were accepted at **73%**.
- When another pipeline reproduced the call (`GO_REF:0000120`), acceptance rose to **77%**, an upper bound because reviewers saw the label.
- In about **three of four** down-grades the graft placement itself was not the defect; the inherited term was too coarse, sibling-level, generic or out of context.

---

## TreeGrafter is not PAINT

| | PAINT / IBA | TreeGrafter |
|---|---|---|
| Applies to | genes **in** the reference tree | sequences **grafted onto** it |
| Made by | curators | fully automated |
| Evidence / reference | IBA, `GO_REF:0000033` | IEA, `GO_REF:0000118` |
| Assigned by | GO_Central | TreeGrafter |

<span class="small">`GO_REF:0000120` is UniProt's merge of identical calls from several pipelines, so `GO_REF:0000118` rows are the TreeGrafter calls no other pipeline reproduced.</span>

---

## How a graft annotation is made

![h:470](treegrafter-graft.svg)

---

## What reviewers did with them

![h:480](treegrafter-results.svg)

---

## Family hotspots: upstream tickets

| Family | n | Down-graded | Problem |
|---|---:|---:|---|
| PTHR24027 cadherin-23 | 30 | 100% | choanoflagellate cadherins on a Bilateria node |
| PTHR10543 beta-carotene dioxygenase | 8 | 100% | stilbene dioxygenases on the carotenoid subfamily |
| PTHR30443 EptA | 8 | 100% | node carries LPS core instead of pEtN transferase (mcr-1..4) |
| PTHR15184 ATP synthase | 5 | 100% | ATP synthase term on FliI/SctN export ATPases |
| PTHR43775 fatty acid synthase | 4 | 100% | FAS term on PKS subfamilies (eryAI-III, Pks1) |

<span class="small">26 of 77 families with at least four reviewed annotations had half or more down-graded. Full table: TREEGRAFTER/treegrafter_family_hotspots.tsv</span>

---

## Caveats

- **65% of rows** come from the ***P. putida* KT2440** batch; rates are directional.
- The PAINT/IBA bar is corpus-wide, not matched; same-file IBA has n=20.
- The reference is the AIGR corpus at `f81b9f300`, and reviews are revised over time.
- Reviewers saw `GO_REF:0000118` vs `GO_REF:0000120`, so the corroboration gap may be inflated.
- `KEEP_AS_NON_CORE` is not an error; accepted + non-core is **69%** for TreeGrafter.

---

## Status and next steps

- ✅ 1,074 annotations tallied; 283 down-grades classified into failure modes; family hotspots listed.
- ⬜ Adjudicate the ten awaiting genes from the 2026-09-20 re-review.
- ⬜ Send the hotspot families to PAINT / PANTHER as tickets.
- ⬜ **Blind the corroboration test** (hide `original_reference_id`).
- ⬜ Second-pass 53 keyword-placed MF/BP rows and 33 mode-0 rows; broaden beyond *P. putida*.

**Read more:** `projects/TREEGRAFTER.md` · `TREEGRAFTER/failure-modes.md` · `analyze_treegrafter.py`
