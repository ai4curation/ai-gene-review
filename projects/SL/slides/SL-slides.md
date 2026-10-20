---
title: "UniProt subcellular-location annotations: granularity, not truth"
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

# UniProt subcellular locations

Reviewing GO annotations that come only from `GO_REF:0000044`

<span class="small">AI Gene Review · projects/SL · 2026-10-05</span>

---

<!-- _class: bluf -->

## Bottom line

- The UniProt SL → GO pipeline is **still running** and supplies many CC annotations with **no other evidence**.
- Failures track **granularity**: broad locations such as `mitochondrial membrane`, `endomembrane system`, and `membrane` are flagged at **21–36%**.
- Dropping SL terms made **redundant** by a more specific term was **tested and refuted** (10% vs 8%). **27** first-pass annotations moved.

---

## Why SL, after SPKW

- SPKW (keywords, `GO_REF:0000043`) was retired by GOA around April 2026. **`GO_REF:0000044` is live.**
- The GAF writes `UniProtKB-SubCell:SL-xxxx` into WITH/FROM, so each row names its **source location**.
- Scan: every annotation whose **only** source is `GO_REF:0000044`, joined to the reviewer's verdict.
- Now **1,852** such annotations in **1,380** gene folders; **1,837** reviewed.

---

## Vague locations fail, precise ones do not

![h:480](sl-issue-rates.svg)

---

## A controlled comparison inside one organelle

![h:480](mito-granularity.svg)

---

## Four failure patterns

| Pattern | What goes wrong | Examples |
|---|---|---|
| **A** under-specification | true, but says nothing | `membrane` on an ER protein |
| **B** association ≠ residence | binds the structure, not in it | SGCA, SGCE → MODIFY to complex terms |
| **C** family-rule propagation | a family trait attached to all | enolase `Secreted` via HAMAP MF_00318 |
| **D** transit as destination | passes through on the way out | SALTY slrP, STAAU lytN |

<span class="small">Plus SL-0221: GO:0034045 was defective; GO has obsoleted it and created GO:7770114 phagophore membrane.</span>

---

## The cheap fix that does not work

| Group | n | Issue rate |
|---|---|---|
| more specific CC term already present | 445 | **10%** |
| SL term is the most specific the gene has | 852 | **8%** |

- Reviewers flag **vagueness**, not duplication: "not wrong, but 'membrane' is the uninformative parent" (yeast DCV1).
- So GOA cannot suppress these by graph logic; it is a **per-annotation judgement**.

---

## Status and next steps

- ✅ Scanner and redundancy test committed: `projects/SL/scripts/`.
- ✅ 22 first-pass genes re-reviewed; **27 annotations moved** (18 SL-0221, 9 SL-0162/SL-0090).
- ⬜ Audit the few family rules that attach `Secreted` to housekeeping enzymes (pattern C, #4259).
- ⬜ Decide whether "true but uninformative" deserves its own verdict (31% land on KEEP_AS_NON_CORE).
- ⬜ Systematic check for SL → GO mappings whose axioms fail, like SL-0221 (#4260).

**Read more:** `projects/SL.md` · `projects/SL/SL-METHODOLOGY.md`
