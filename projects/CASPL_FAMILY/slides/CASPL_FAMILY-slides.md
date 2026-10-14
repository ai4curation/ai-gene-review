---
title: "CASP-like (CASPL) family curation"
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

# The CASP-like (CASPL) family

Poplar and Arabidopsis reviews, PANTHER families, and orthology evidence

<span class="small">AI Gene Review · projects/CASPL_FAMILY · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- CASPLs are small **four-span membrane scaffolds**; the true CASPs build the **Casparian strip**, but most CASPLs are uncharacterized.
- We reviewed **21 poplar** and **5 Arabidopsis** CASPLs, described **2 PANTHER families**, and ran orthology and expression analyses.
- Function transfers **at group level**: 20/20 poplar CASPLs hit the same Roppolo group; root-specific **CASPL1B1** and stress-induced **CASPL4C1** fit their Arabidopsis orthologs.

---

## Can function move from Arabidopsis to poplar?

![h:470](caspl-transfer.svg)

---

## Why this family

- A **dark family**: dozens of members per plant genome, a handful characterized.
- Poplar reviews borrow hypotheses from Arabidopsis orthologs; that only works if the **orthology is real**.
- A family-wide view also fixes the PANTHER descriptions that every member inherits.

---

## Expression backs the transfer

![h:470](caspl-expression.svg)

---

## What the annotations show

| Set | Genes | Rows | Outcome |
|---|---|---|---|
| Poplar CASPLs | 21 | 21 | one IEA *plasma membrane* row each, all ACCEPT |
| Arabidopsis orthologs | 5 | 21 | 13 ACCEPT, 1 non-core, **2 REMOVE**, **5 UNDECIDED** |

- **REMOVE**: ISM *extracellular region* (CASPL1B1) and *nucleus* (CASPL1D2).
- **UNDECIDED**: five HDA Golgi / endosome / TGN rows on CASPL1D1.
- **NEW** proposed: CASPL1D1 *defense response to bacterium* (IMP).
- PANTHER: PTHR33573 description now separates CASP1–5 from the CASPL bulk; PTHR36488 (IPR044173) described.

---

## Status and next steps

- ✅ 21 poplar + 5 Arabidopsis reviews; 2 PANTHER families; orthology + expression analyses.
- ⬜ Peanut and watermelon CASPLs are TrEMBL only, so out of scope.
- ⬜ Optional extension: rice (29) and maize (23) reviewed CASPL entries.
- ⬜ CASPL2A1 (poplar) is reviewed but absent from the orthology analysis.

**Read more:** `projects/CASPL_FAMILY.md` · `projects/CASPL_FAMILY/bioinformatics/RESULTS.md` · `genes/POPTR/CASPL*/`
