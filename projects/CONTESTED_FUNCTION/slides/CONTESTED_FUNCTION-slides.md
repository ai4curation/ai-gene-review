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
- Epe1's **4 electronic catalytic rows are REMOVE** (only the IBA demethylase row gets a replacement, chromo shadow domain binding); the **2 IDA/EXP rows and metal ion binding are UNDECIDED**. Finding **more candidates has not started**.

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

1. The JmjC iron triad is **H297-E299-Y370**: position 370 is a **Tyr** where canonical JmjC demethylases have the third iron-ligating His. Yet **Y370A loses function** (Raiymbek 2020): the Tyr is required, though required is not catalytic.
2. **Mass spectrometry** shows no demethylation of H3K9me2/me3 peptides.
3. **H297A keeps prevention** of de novo H3K9me (nearly fully), so part of the anti-silencing activity does not need H297 (Sorida 2019). *One experiment read two ways*: its other arm, lost removal of established H3K9me, is on the next slide.
4. The **C-terminus alone**, without JmjC, disrupts heterochromatin.

<span class="small">Sources named on the project page: Ayoub 2003, Trewick 2007, Wang 2013 (Bdf2, PMID:24013502), Audergon 2015, Bao 2019, Sorida 2019, Raiymbek 2020.</span>

---

## Evidence for a catalytic contribution (not excluded)

- The **JmjC domain is essential** for Epe1 activity (Ayoub 2003) and for its effect on Pol II accessibility (Zofall & Grewal 2006, who note the mechanism may differ from demethylases).
- **Y307A** is recorded as loss of function, but from the same Ayoub paper, possibly the same experiment. Y307 is a 2-oxoglutarate-site residue, not an Fe ligand (Raiymbek; Sorida): cofactor pocket implicated, catalysis not isolated.
- **Sorida 2019**, independent of Ayoub: under H297A, **removal of established H3K9me is lost**, read out in vivo. *One experiment read two ways*: its other arm, retained prevention, is on the previous slide.
- **Wang 2015** (Mst2/Epe1): epe1-H374A and epe1-Y307A read as enzymatically dead, redundant with Mst2 (residue 374 of O94603 is Thr, so the His cannot be identified).
- Against: **no study has measured demethylation directly**, and the same mutations weaken Swi6 binding and localization.

<span class="small">Sources: Ayoub 2003 (PMID:12773576), Zofall & Grewal 2006 (PMID:16762840), Sorida 2019 (PMID:31206516), Wang 2015 (Mst2/Epe1, PMID:25774602), Raiymbek 2020 (PMID:32195666).</span>

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
