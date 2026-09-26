---
title: "Miscitation Audit: citations that point at the wrong paper"
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

# Miscitation Audit

A register of GO citations that resolve to the wrong paper, keyed on the citation

<span class="small">AI Gene Review · projects/MISCITATION_AUDIT · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- Reviewers had flagged wrong-paper citations **one gene at a time**; nobody had aggregated them.
- `harvest_citations.py` now collects every flag across **4,467 reviews**: **28 `WRONG_IDENTIFIER` rows on 21 citations**, 7 citations hit more than one gene, plus **257 `MISCITED`** rows not yet precision-checked.
- **233 of 285** flagged citations came from GOA, so the real deliverable is **upstream bug reports**, which are **not filed yet**.

---

## Why the validators cannot see this

- CI checks that the **title matches the PMID** and that each quote is **verbatim in the cached paper**.
- A wrong PMID imported **together with its own title** passes both.
- Example: MGI's `protein farnesylation` IDA on yeast **COX17** cites **PMID:8078902**, the cloning of **COX10** (one digit away). The term is wrong even for COX10, which farnesylates heme, not protein.
- Only a human reading the paper catches it, and that judgement lives in `reference_review.correctness`.

---

## Key on the citation, not the gene

![h:470](citation-spread.svg)

---

## What the register holds

![h:470](flag-counts.svg)

---

## Failure modes seen so far

| Mode | Example |
|---|---|
| Off-by-one gene symbol | COX17 ← a COX10 paper |
| Paralog substitution | ELOVL1/2/3 ← an ELOVL5 paper; NAA10/NAA40 ← a NAA60 paper |
| Gene-symbol collision | ADPRH ← an "ARH1" hypercholesterolaemia paper; BRIP1 ← a BACH1 paper |
| Wholly unrelated paper | DICDI gbpC ← a *Legionella* SidC study; TIM9/TIM10 ← colorectal surgery |
| Identifier resolves to nothing | `PMID:34521819` on STAT2 |
| Wrong organism or subject | DROME insc ← a review of zebrafish cardiac development |

---

## Two detectors for unflagged defects

**Check A: unresolvable identifiers.** Works and is nearly free: `fetch-gene` already caches every PMID it can resolve, so absence from `publications/` is the signal. **1 of 24,436** cited PMIDs is dead (`PMID:34521819`, cited by STAT2, JAK1, STAT1). Should run in CI.

**Check B: paralog mismatch.** Does **not** work, recorded so nobody rebuilds it.
- Misses ELOVL: the paper says "HELO1", never "ELOVL".
- 356 candidates, dominated by legitimate complex-wide papers (ESCRT, Complex I, PEX, EMC).

---

## Status and next steps

- ✅ Register and anomaly detectors built; reports in `projects/MISCITATION_AUDIT/reports/`.
- ⬜ Adjudicate the unflagged uses of spreading citations (e.g. KRAS, NRAS, JAK1, STAT1, VCP).
- ⬜ File GOA-sourced `WRONG_IDENTIFIER` sets upstream per database (MGI, SGD, UniProt).
- ⬜ Fix the one review-only case (ADPRH); put Check A in CI.
- Sibling project: `projects/MISCITATIONS.md` (taxonomy and seed cases).

**Read more:** `projects/MISCITATION_AUDIT.md` · `reports/REPORT.md` · `harvest_citations.py`
