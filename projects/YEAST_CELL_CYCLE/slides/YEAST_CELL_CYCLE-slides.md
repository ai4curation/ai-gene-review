---
title: "Yeast cell cycle and translation control (scoped)"
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

# Yeast cell cycle and translation control

A scoped review of 23 *S. cerevisiae* genes at the G1/S transition

<span class="small">AI Gene Review · projects/YEAST_CELL_CYCLE · scoping</span>

---

<!-- _class: bluf -->

## Bottom line

- **Scoped, not yet started.** The plan is to review GO annotations for **23 genes** covering Start, the cyclins and CDK, and the translation machinery.
- The question: does GO capture **translational** control of the cell cycle as well as the transcriptional program?
- Status: **1 of 23** has a review (**TOR1**, 67 annotations); the other 22 have no folder yet.

---

## The circuit the project covers

![h:500](start-circuit.svg)

---

## Why this set

- Start is one of the best-understood decision circuits in biology, so GO annotations can be checked against a clear mechanism.
- Recent work proposes that **translation capacity** (TORC1, ribosome biogenesis, initiation factors) helps time Start, a layer GO rarely links to the cell cycle.
- The review would separate **core cell-cycle functions** from **pleiotropic growth effects** that tend to be over-annotated to cell-cycle terms.

---

## Where the list stands

![h:480](gene-status.svg)

---

## Before starting

- **Fix the symbols.** Yeast eIF1 is `SUI1`; `EIF3` is a complex, not a gene; `EIF2A` needs checking. `SHE2` is listed as a ribosome biogenesis factor and its role should be confirmed.
- Run `just fetch-gene yeast <GENE>` for each gene, then deep research and review.
- Reuse the existing **TOR1** review (`genes/yeast/TOR1/`): 52 ACCEPT, 9 KEEP_AS_NON_CORE, 6 MARK_AS_OVER_ANNOTATED.

**Read more:** `projects/YEAST_CELL_CYCLE.md`
