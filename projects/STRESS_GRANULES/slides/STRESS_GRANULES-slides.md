---
title: "Stress granules: a scoped project"
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

# Stress granules

Assembly and disassembly of stress-induced RNA-protein condensates in human: a scoped project

<span class="small">AI Gene Review · projects/STRESS_GRANULES · SCOPING · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- **Scoped, not started.** No stress granule module; the core nucleators **G3BP1 and G3BP2 are not reviewed**.
- **7 of 16 listed candidates** already have reviews made for other projects (TIA1, TIAL1, USP10, TARDBP, HNRNPA2B1, ATXN2, VCP).
- In those, stress-granule rows were **accepted** for TIA1, TARDBP, ATXN2 and VCP; TIAL1 adds SG assembly as **NEW**, while USP10's negative-regulation rows are **non-core**.

---

## The biology

![h:470](stress-granule-cycle.svg)

---

## Why this is worth doing

- Stress granules are the best-known **cytoplasmic condensate**, and several **ALS/FTD proteins** (TDP-43, FUS, hnRNPA1/A2B1, ATXN2) partition into them.
- Many RNA-binding proteins are *found in* granules; few *build* them. Separating nucleators from residents is the key curation call.
- The general question of how GO should represent condensates is handled in **CONDENSATES**.

---

## Where the candidate genes stand

![h:470](candidate-coverage.svg)

---

## Next steps

1. `just fetch-gene human G3BP1` and `G3BP2`; review them, then CAPRIN1.
2. Review FUS, HNRNPA1, FMR1, PABPC1, EIF2S1 and EIF4G1.
3. Build a stress granule module distinguishing nucleators, regulators, residents and disassembly factors.

**Read more:** `projects/STRESS_GRANULES.md` · `genes/human/TIA1/` · `projects/CONDENSATES.md`
