---
title: "PANTHER IBA family review: testing IBAs at their source node"
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

# PANTHER IBA family review

Testing 160 fission yeast IBAs at the tree node they came from

<span class="small">AI Gene Review · projects/PANTHER_IBA_REVIEW · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- Each IBA follows from a **PAINT curator's IBD** at an ancestral PANTHER node; we rebuilt that propagation for **all 160 IBAs** on 41 reviewed *S. pombe* genes.
- The per-gene calls **held up**: 148 kept, the 36 cross-subfamily flags were mostly conserved functions, **no new errors** among accepted rows.
- Real over-propagations were **localization terms** and **paralog-specific functions** crossing subfamily lines (pom1, rqh1, mid1).

---

## What an IBA asserts

- A PAINT curator reads the tree, the MSA and the experimental annotations, and places the function at a node (**IBD**). Descendants inherit it as **IBA**.
- So an IBA is a phylogenetic judgment. To challenge one, ask: is the target **inside the clade** that inherited the function, and is there target-specific evidence of **loss or divergence**?
- A short seed list is **not** weak support; one well-characterized descendant can ground a node.

---

## Method: rebuild each propagation from repo data

- `with/from` → source node (`PTN…`) and seed genes.
- Gene and seed **subfamilies** from `*-uniprot.txt` and `interpro/panther/<FAM>/<FAM>-entries.csv`.
- Node-level PAINT annotations and **IRD/IKR losses** from `IBD.gaf`.
- Join our per-gene action; flag `CROSS_SUBFAMILY`, `LOCALIZATION`, `NODE_LOSS`, ...
- `just refresh-panther-iba-project` regenerates all three tables.

---

## Outcomes and flags

![h:470](iba-outcomes.svg)

---

## The two failure patterns

![h:470](iba-cases.svg)

---

## The flag is triage, not a verdict

| Gene | IBA term | Why the cross-subfamily flag is a false positive |
|---|---|---|
| cdc2 | CDK holoenzyme | Cdc2 is the founding CDK |
| plo1 | protein Ser/Thr kinase activity | Polo kinase; conserved family-wide |
| rad3 | DNA damage checkpoint | Rad3/ATR; conserved PIKK function |
| ste11 | dbTF activity | HMG transcription factor |
| cdc18 | replication origin binding | Cdc18/Cdc6 |

<span class="small">Fine-grained PANTHER subfamilies split true orthologs across species. From REVIEW.md.</span>

---

## One term, two correct answers

- `GO:0000165` **MAPK cascade**, IBA on two kinases:
  - **wis1 → ACCEPT**: the MAP2K of the Sty1 stress cascade.
  - **cdc7 → MARK_AS_OVER_ANNOTATED**: SIN initiating kinase; the SIN is a GTPase-regulated relay, not a MAPK cascade.
- **ral2**: PAINT's own IRD losses (peroxidase, cytosol, redox) on node `PTN005166285` keep peroxiredoxin functions off this Kelch subfamily; the one surviving IBA is **ACCEPT**.

---

## Status and next steps

- Done: 160 IBAs analysed; written review in `REVIEW.md`.
- PAINT loss table: **2,129** findings across 549 cached families; **63 IKR** losses fall on a reviewed member, ready for residue reconstruction with `prepare_loss_analysis.py`.

**Read more:** `projects/PANTHER_IBA_REVIEW.md` · `REVIEW.md` · `iba_propagation.tsv` · `projects/IBA_REVIEW.md`
