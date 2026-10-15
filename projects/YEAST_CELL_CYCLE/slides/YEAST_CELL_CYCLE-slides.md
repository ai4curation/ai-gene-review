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

- **Scoped, partly reviewed.** The plan spans **23 rows** covering Start, the cyclins and CDK, and the translation machinery.
- The question: does GO capture **translational** control of the cell cycle as well as the transcriptional program?
- Status: **10 of 23** rows have reviews (**493 annotations**); 13 still need review or symbol triage.

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

- **Fix the symbols.** Yeast eIF1 is `SUI1`; `EIF3` is a complex, not a gene; `EIF2A` is the reviewed `SUI2` row.
- Confirm why **SHE2** belongs before treating it as ribosome biogenesis.
- Finish the 13 open rows tracked in #3960.

**Read more:** `projects/YEAST_CELL_CYCLE.md`
