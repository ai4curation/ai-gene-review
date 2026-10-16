---
title: "P. putida KT2440: module-first review of a bacterial proteome"
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

# *Pseudomonas putida* KT2440

Module-first GO review of a whole bacterial proteome

<span class="small">AI Gene Review · projects/P_PUTIDA · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- KT2440 is a versatile soil bacterium whose GO annotation is **almost entirely automated**.
- Since July 2026 we review it **pathway by pathway**: start from a curated module, ask which steps KT2440 can satisfy, review only the genes each step needs.
- September 2026 snapshot: **921 PSEPK reviews** (5,324 rows) and **138 batch pages**, still growing; unresolved steps are kept as **explicit holes**.

---

## Why a module-first pass

- 5,527 proteins; only ~50 GO annotations cite a paper.
- Gene-by-gene review does not scale to a genome, and treats every gene as equally uncertain.
- A module says **what the organism must do**; review effort goes to steps that are **missing, ambiguous or over-propagated**.
- Early phase: 18 selected genes, then batches of 50 and 16 (TCA, stress, DNA repair, aromatic amino acids).

---

## The workflow

![h:500](module-first-workflow.svg)

---

## A hole kept as a hole

![h:500](d-ala-hole.svg)

---

## What a batch page records

![h:440](ppu00470-batch-page.jpg)

<span class="small">projects/P_PUTIDA/batches/ppu00470_d_amino_acid_cell_wall_precursor_supply.md: selected genes and their module assessment.</span>

---

## Results so far

![h:480](actions-bar.svg)

<span class="small">857 rows marked over-annotated, 243 removed, 85 left undecided.</span>

---

## Status and next steps

- ✅ Whole-proteome metadata, gene list, 161-bucket partition, pathway worklist.
- ✅ 138 pathway batches, from the ppu00400 tryptophan pilot (PR #1874) to the most recent, purine-base oxidation (PR #2643).
- ⬜ The status columns in `data/psepk_pathway_worklist.tsv` and the "Completed Reviews" tables predate most of this work.
- ⬜ 777 of 921 reviews are still `status: DRAFT`. The 1,149 orphan and 825 unknown-function genes have no pathway module to seed them.

**Read more:** `projects/P_PUTIDA.md` · `projects/P_PUTIDA/P_PUTIDA_MODULE_PLAN.md` · `projects/P_PUTIDA/batches/`
