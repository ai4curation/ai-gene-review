---
title: "PDB structures as GO evidence"
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

# PDB structures as GO evidence

Where deposited structures change a gene's annotation, and where they only confirm it

<span class="small">AI Gene Review · projects/PDB · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- **1,991** pipeline genes have a deposited structure (27,157 PDB entries), yet only **19%** of 1,668 structure-paper and gene pairs are cited in GOA.
- Structures reliably give under-curated proteins their **first experimental-grade evidence** (>12 annotations, **5 NEW** rows across the reviews).
- **New informative function is rare**: 2 structure-unique annotations (both merA); the papers' own hypotheses paid off clearly in 1 of 6.

---

## Why look at structures

- A bound **cofactor, metal, ligand or partner** is direct evidence for MF, binding and complex membership.
- Rank candidates by **richness × sparsity**: a cofactor-bound, full-length structure of an IEA-only enzyme scores high.
- Three cuts (620 genes): **dark_mf** 206 · **euk** 210 · **contested** 340 (a review disputed a catalytic MF).

---

## Structure papers are missing from the evidence trail

![h:460](pdb-citation-gap.svg)

<span class="small">353 of 573 genes cite none of their structure papers. GAP_OPPORTUNITY: the paper predates the gene's latest experimental annotation.</span>

---

## Does structure fill gaps? (H1)

![h:500](pdb-three-layers.svg)

---

## Structure adjudicates contested activities

| Gene | Disputed MF | Action | In the structure |
|---|---|---|---|
| HEN1 (ARATH) | peptidyl-prolyl isomerase | REMOVE | SAH → methyltransferase |
| XYL1 (PICST) | oxidoreductase (generic) | REMOVE | NADP |
| DOT1 (yeast) | methyltransferase (generic) | over-annotated | SAM/SAH |
| SIRT2 (human) | transferase (generic) | over-annotated | NAD, Zn |
| mcrA (METAC) | transferase (generic) | REMOVE | F430, SAM, Fe-S |

<span class="small">Two cases: an over-general parent (cofactor confirms catalysis, points to the specific child) versus a wrong specific activity (structure argues against it).</span>

---

## Caveats we hit

- RCSB **per-entry citations drift**: SPR's are inhibitor screens, cbh1's glycosylation NMR. Verify each PMID before citing.
- A bound ligand is a **clue, not proof**; additives are filtered but adventitious binders remain.
- Round 1 tested genes that were **already curated experimentally**, so structures could only corroborate (4 of 4).

---

## Status and next steps

- ✅ Inventory, RCSB enrichment, citation-gap and H1 ledger
- ✅ Structure-informed reviews: XYL1, IDH3B, COX6B1, psaC, COI1, ATAD1; HSPB3; merA, mcrA, secA; mxaI null
- ⬜ Work down `GAP_WORKLIST.md` (FANCB, PNO1, RCO1, RPS3, AEBP2 …)
- ⬜ Map complex partners to UniProt; consider a PDB-evidence field in the schema

**Read more:** `projects/PDB.md` · `projects/PDB/H1_LEDGER.md` · `projects/PDB/CURATION_GAP.md`
