---
title: "Bacillus subtilis: reviewing 35 model Gram-positive genes"
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

# *Bacillus subtilis*

Reviewing GO annotations on 35 genes of the model Gram-positive bacterium

<span class="small">AI Gene Review · projects/BACSU · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- We reviewed **GOA annotations on 35 genes**: CACAO-curated flagellar/germination genes, key functional genes, the **sporulation sigma cascade**, industrial enzymes, and six follow-up sporulation/cofactor genes.
- **396 rows**: 225 accepted, 37 kept as non-core, 47 modified, 53 NEW, 15 removed, 16 over-annotated, 3 undecided.
- Recurring fixes: **sigma factors are not RNA polymerases**, a fold-based **acyltransferase** call on spoVAD removed, unsupported fliY/swrD rows citing the wrong paper removed.

---

## Why *B. subtilis*

- Model **Gram-positive** bacterium, the counterpart to *E. coli*.
- Model for **cell differentiation**: sporulation runs on a cascade of compartment-specific sigma factors.
- Naturally **competent**, and an industrial secretion host (subtilisin, amylase, levansucrase).
- Round 1 targeted genes where **CACAO** student curation had contributed heavily, to test those rows.

---

## The sporulation sigma cascade

![h:500](sporulation-cascade.svg)

---

## Sigma factors are not polymerases

![h:450](sigG-review-table.jpg)

<span class="small">sigG review: IBA rows for RNA polymerase activity (GO:0003899) and cis-regulatory region binding (GO:0000976) removed; the correct promoter-specificity function is GO:0016987 sigma factor activity.</span>

---

## Results across 35 genes

![h:480](actions-bar.svg)

---

## Notable findings

1. **PMID:25313396** lists the minimal FlgM-secretion components and does not include fliH, fliY or swrD. Unsupported fliY/swrD rows were **removed**; fliH rows remain **UNDECIDED**.
2. **spoVAD**: `acyltransferase activity` came from a thiolase-like fold; it is a Ca-DPA channel component. **Removed**.
3. **yddE** is labelled uncharacterized in UniProt but is **ConE**, the VirB4-like ATPase of the ICEBs1 conjugation system.
4. Generic `metal ion binding` refined to **zinc / calcium binding** (nprE); `hydrolase activity` marked over-annotated where specific terms exist.

---

## Status and next steps

- ✅ 35/35 reviews present and rendered; sporulation cascade pathway summary written.
- ⬜ Finalise YAML statuses: 5 COMPLETE, 26 DRAFT, 4 IN_PROGRESS (#4044).
- ⬜ Work through eight open per-gene re-review issues (#4044).

**Read more:** `projects/BACSU.md` · `projects/BACSU/BACSU_SPORULATION-pathway.md` · `genes/BACSU/<gene>/`
