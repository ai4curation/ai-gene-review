---
title: "Contested function: pseudo-enzymes in GO"
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

# Contested function

Proteins that keep an enzyme's fold but not its activity

<span class="small">AI Gene Review · projects/CONTESTED_FUNCTION · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- **Pseudo-enzymes** keep a family's domain but have lost catalysis, so IBA, IEA and sometimes experimental rows give them an activity biochemistry contradicts.
- We reviewed four cases in depth: **Epe1** (fission yeast) and three biosynthetic-cluster proteins, **eryCII, pqsB, actI-ORF2**.
- Epe1's **7 catalytic and metal rows are REMOVE**, replaced by histone-binding terms. Finding **more candidates has not started**.

---

## Why these cases

- They need **several evidence types at once**: domain homology, activity assays, catalytic-site mutants, and the alternative mechanism.
- A wrong catalytic term on a pseudo-enzyme is **re-propagated** by IBA and domain IEA until something records the loss.
- The Epe1 case was presented at the **GO Consortium meeting, October 2025**.

---

## Epe1: eraser or recruiter?

![h:500](epe1-mechanism.svg)

---

## Evidence against demethylase activity

1. The JmjC iron triad is **H297-E299-Y370**, not the canonical **H-D-H**.
2. The distal **Fe(II)-binding** histidine is lost: **His370 is a Tyr**.
3. **Mass spectrometry** shows no demethylation of H3K9me2/me3 peptides.
4. The **H297A** catalytic mutant keeps full anti-silencing function.
5. The **C-terminus alone**, without JmjC, disrupts heterochromatin.

<span class="small">Sources named on the project page: Trewick 2007, Wang 2013, Bao 2019, Raiymbek 2020.</span>

---

## Four pseudo-enzymes

![h:500](pseudoenzyme-table.svg)

---

## Contested claims inside a sound paper

- Some disputes are about **one finding**, not the whole reference.
- The schema's `finding_review` records these: `finding_status: DISPUTED` + `superseded_by`.
- Example, **eryCIII**: a 2004 claim that EryCIII is highly active on its own (PMID:15303858) is DISPUTED, superseded by the 2012 structure study (PMID:22056329) showing it is **inactive without EryCII**.

---

## Status and next steps

- ✅ Epe1, eryCII, pqsB, actI-ORF2 reviewed.
- ⬜ Identify suspected pseudo-enzymes (Priority 2): the **Top-Nots** pseudo-enzyme pattern already names PLD5, AKTIP, AIP, CG6051, CPT1C, Pld4.
- ⬜ Screen reviewed genes for over-annotated domain-based IBA/IEA rows (Priority 3).

**Read more:** `projects/CONTESTED_FUNCTION.md` · `genes/SCHPO/Epe1/` · `projects/TOP_NOTS.md`
