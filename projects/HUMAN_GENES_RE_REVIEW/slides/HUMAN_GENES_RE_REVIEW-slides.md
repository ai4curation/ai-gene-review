---
title: "Human genes re-review: a second reader for 1,323 reviews"
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

# Human genes re-review

A second reader for every curation action in 1,323 human reviews

<span class="small">AI Gene Review · projects/HUMAN_GENES_RE_REVIEW · reviewed 2026-10-04</span>

---

<!-- _class: bluf -->

## Bottom line

- We re-read the action on every existing annotation in **1,323 human reviews** (AAAS → ZSWIM8, ~55k actions) and asked "do I agree?"
- **~99.7% agreement**: only **3 actions changed** (ABL1, ADRM1, BRCA2); all 143 **NOT** annotations adjudicated.
- Sweep **complete** (July 2026). The human set has since grown to **2,812** files, so 1,489 newer reviews have not had a second pass.

---

## Why a second pass

- Actions (ACCEPT, REMOVE, MODIFY …) are what summaries and modules are built on.
- A single reviewer can be wrong in systematic ways: over-removal, removing experimental rows it cannot see, mishandling NOT rows.
- Rules: judge from the YAML and cached papers only; **edit only on confident disagreement**; log everything else as a fence case or literature question.

---

## What changed

![h:500](sweep-funnel.svg)

---

## The NOT audit

![h:500](not-audit.svg)

---

## What the first pass got right

- **Pseudo-enzymes**: ancestral activity removed when catalytic residues are lost (CRMP1, ILK, ROR1, UBAC2).
- **Wrong enzyme or direction**: phosphatase ≠ kinase (CDC25B, PTPN6); TXN vs TXNRD; CPS1 vs CPS2.
- **Name collisions**: HAP1 (huntingtin-associated ≠ APE1), GNAS locus, AARSD1 vs AARS1.
- **Legacy TF labels** removed from ESCRT/Golgi machinery: TSG101, TMF1, USO1.

---

## Flagged for a curator, not edited

| Case | Tension |
|---|---|
| **GAPDH** | ~43 REMOVEs include documented moonlighting (GAIT complex) |
| **HSPA1B** | removes own IDA chaperone rows that twin HSPA1A keeps |
| **ATP23** | DSB-repair rows from its former KUB3 identity removed |
| **AGO3 / AGR2** | NOT rows removed as superseded |
| **ASCL1, ATF3** | REMOVE on IDA; need the source papers |

---

## Status and next steps

- Done: A→Z sweep over 1,323 files; 3 edits, all present in the current YAMLs.
- Done: TRA2B, flagged as never reviewed, has since been reviewed with no PENDING rows.
- Next: resolve the fence cases and the ASCL1 / ATF3 literature questions.
- Next: second pass for the 1,489 human reviews added after July 2026.
- Tracker: #4097.

**Read more:** `projects/HUMAN_GENES_RE_REVIEW.md`
