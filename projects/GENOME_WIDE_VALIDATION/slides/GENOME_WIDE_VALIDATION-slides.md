---
title: "Genome-wide validation: can this annotation set describe a cell?"
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

# Genome-wide validation

Scoring a whole genome's annotation set for completeness, coherence and consistency

<span class="small">AI Gene Review · projects/GENOME_WIDE_VALIDATION · E. coli pilot rerun 2026-10-04</span>

---

<!-- _class: bluf -->

## Bottom line

- Per-gene review asks if **one annotation** is right; this asks if the **whole set** could coexist in a living cell.
- **Coherence is built:** the *E. coli* EcoCyc GAF satisfies 112 of 129 activated GO `has_part` dependencies (**86.8%**).
- The **17 violations** are curation leads: likely pathway overreach, missing complex/MF terms, viral or heterochromatin over-annotations, and unresolved cases. Completeness and consistency are **still roadmap items**.

---

## Why genome scale

- Prediction and evaluation score one protein at a time, as if annotations were independent facts.
- A method can be accurate per protein yet yield a genome no organism could have: no DNA replication, a late pathway step with no upstream enzymes, photosynthesis next to neuron development.
- Framework: completeness / coherence / consistency (Tawfiq, Kulmanov & Hoehndorf 2026, *Brief. Bioinform.* bbag336), using constraints **already in GO**.

---

## The coherence check

![h:470](coherence-check.svg)

---

## What the 17 violations are

![h:470](coherence-violations.svg)

---

## Limits of the pilot

- **Asserted `has_part` only** (743 pairs); the reference paper reports thousands of additional ELK-inferred pairs, so this is a lower bound.
- **Set-based, not sequence-based:** a violation cannot tell "gene absent" from "gene present but unannotated". Confirm gaps with GapMind or Pathway Tools before any REMOVE.
- The completeness probe in the output (DNA replication, transcription, translation present) is a sanity check, not the metric.

---

## Status and next steps

- Done: *E. coli* coherence pilot, from public data (`pilot-ecoli/coherence_pilot.py`).
- Next: add inferred `has_part` pairs and MetaCyc routes.
- Next: minimal-genome essential-function set for **completeness**; GO taxon constraints for **consistency**.
- Next: predictor sweep (InterPro2GO, DeepGO-family); decide whether to reuse GAEF.

**Read more:** project page · E. coli pilot `RESULTS.md`
