---
title: "Proteostasis Review Batch 8 — Gene Selection"
---

# Proteostasis Review Batch 8 — Gene Selection

Date: 2026-06-13
Branch: `claude/proteostasis-gene-review-3zv0vt`

## Context

Batches 1–7 are complete (`pr-1217`, `2026-06-03`, `2026-06-06`, `2026-06-07`,
`2026-06-07b`, `2026-06-07c`, `2026-06-11`). Batch 7 covered the **ER
proteostasis branch** (SRP/translocon, EMC/GET insertion, glycoprotein-folding
QC, ERAD ubiquitin machinery). Batch 8 moves into the **Ubiquitin–Proteasome
System (UPS) branch**, selecting 50 unreviewed PN candidates
(`ok_for_propagation_to_go` scope, no prior `*-ai-review.yaml`).

## Theme: Cullin–RING ligase (CRL) substrate-recognition & assembly modules

The UPS branch of the PN workbook is intentionally domain-heavy and inclusive,
built around the E3 ubiquitin/UBL ligase scaffold. This batch walks the largest
and most systematically organized CRL substrate-receptor family — the **F-box
proteins** of the SCF (SKP1–CUL1–F-box / CRL1) complex — plus the **CRL4 core
and CRL assembly/regulation machinery**. It directly exercises the UPS-branch
`E3 ubiquitin and UBL ligases -> CRL family` part of the PN taxonomy.

F-box proteins are grouped by their substrate-recognition module:

- **FBXL** — F-box + leucine-rich repeats
- **FBXW** — F-box + WD40 repeats
- **FBXO** — F-box "other" (diverse/no canonical second domain)

### Selected genes (50)

#### F-box / leucine-rich-repeat receptors — FBXL (14)
1. `FBXL3` — SCF receptor for CRY1/CRY2 (circadian clock)
2. `FBXL5` — iron-sensing receptor for IRP2/IREB2 (FBXL5–SKP1 hemerythrin)
3. `FBXL6`
4. `FBXL7` — receptor for AURKA, survivin
5. `FBXL8`
6. `FBXL12` — receptor for CDKN1B/p27, ALDH3A1
7. `FBXL13`
8. `FBXL14`
9. `FBXL15`
10. `FBXL16`
11. `FBXL17` — receptor for BACH1; SCF dimerization QC
12. `FBXL18`
13. `FBXL20` (SCRAPPER) — synaptic RIM1 turnover
14. `FBXL22`

#### F-box / WD40-repeat receptors — FBXW (8)
15. `FBXW2`
16. `FBXW4` (dactylin)
17. `FBXW5` — receptor for SASS6, TSC2, EPS8
18. `FBXW7` (CDC4) — receptor for MYC, cyclin E, NOTCH, JUN (tumor suppressor)
19. `FBXW8` — CRL7 receptor (with CUL7)
20. `FBXW9`
21. `FBXW10`
22. `FBXW12`

#### F-box / "other" receptors — FBXO (22)
23. `FBXO2` — ER glycoprotein lectin F-box (N-glycan recognition, ERAD)
24. `FBXO5` (EMI1) — APC/C inhibitor (not a canonical SCF receptor)
25. `FBXO6` — ER glycoprotein lectin F-box (ERAD)
26. `FBXO7` (PARK15) — PINK1/Parkin mitophagy; PI31 proteasome regulator
27. `FBXO8`
28. `FBXO10`
29. `FBXO15`
30. `FBXO16`
31. `FBXO17`
32. `FBXO21`
33. `FBXO22` — receptor for KDM4A, PTEN, BACH1
34. `FBXO25`
35. `FBXO27` — ER glycoprotein lectin F-box
36. `FBXO30`
37. `FBXO33`
38. `FBXO34`
39. `FBXO36`
40. `FBXO39`
41. `FBXO40`
42. `FBXO41`
43. `FBXO43` (EMI2/ERP1) — APC/C inhibitor, meiotic CSF
44. `FBXO47`

#### CRL4 core & CRL assembly/regulation (6)
45. `DDB1` — CRL4 adaptor (DDB1–CUL4 scaffold for DCAF receptors)
46. `DDB2` — CRL4 substrate receptor (UV-damaged DNA recognition)
47. `DDA1` — DET1/DDB1-associated, CRL4 stabilizer
48. `DTL` (CDT2) — CRL4 substrate receptor (CDT1, p21, SET8 degradation)
49. `CAND2` — CAND1 paralog; cullin–RBX sequestration / CRL exchange factor
50. `GLMN` (glomulin) — RBX1-binding CRL assembly regulator (FBXW7/CUL7 control)

## Method

Same as batches 5–7: `fetch-gene` scaffolding (uniprot + goa + seeded
`-ai-review.yaml` + cached publications + PANTHER family), per-annotation review
against GO guidelines with verbatim `supported_by`, populated
`description`/`core_functions`/`suggested_questions`/`suggested_experiments`,
reference `reference_review` adjudication, then `uv run linkml-validate` +
`uv run ai-gene-review validate`.

## Curation watch-points

- **F-box = substrate receptor, not the catalytic core.** The catalytic RING
  activity of an SCF complex lives on RBX1/RBX2, not the F-box protein. Prefer
  `GO:1990756 ubiquitin-like ligase-substrate adaptor activity` /
  `GO:0061630 ubiquitin protein ligase activity` in the SCF context plus
  `SCF-dependent proteasomal ubiquitin-dependent protein catabolic process`
  (GO:0031146) and `part_of` the `SCF ubiquitin ligase complex` (GO:0019005).
  Do **not** treat bare `protein binding` (GO:0005515) as a core function —
  replace/supplement with the specific substrate-recognition role.
- **SKP1 binding is the defining F-box feature.** `GO:0019904`/SKP1 binding or
  `F-box domain binding` annotations are mechanistically central and should be
  kept (ACCEPT/non-core), but the *core* statement is substrate-specific
  ubiquitination.
- **Lectin F-box subfamily (FBXO2/FBXO6/FBXO27, and FBXO17/FBXO44).** These bind
  N-linked high-mannose glycans on misfolded glycoproteins and feed ERAD — use
  carbohydrate/`high-mannose oligosaccharide binding` + ERAD/`SCF-dependent…
  catabolic process`, a genuine proteostasis-core function.
- **Non-canonical "F-box" members.** `FBXO5`/EMI1 and `FBXO43`/EMI2 are **APC/C
  inhibitors**, not SCF substrate receptors despite the F-box motif — their core
  biology is cell-cycle/meiotic APC/C regulation; treat SCF/ubiquitin-ligase
  propagations skeptically.
- **Tumor-suppressor / well-studied receptors** (`FBXW7`, `FBXL5`, `FBXL3`,
  `FBXO7`, `FBXO22`) have rich experimental annotations; ground the core
  function in IDA/IMP/IPI literature, keep the many IEA/IBA terms as ACCEPT or
  non-core appropriately.
- **Domain-based / poorly characterized paralogs.** Many FBXL/FBXO/FBXW members
  rest largely on IBA/IEA family propagation with little direct evidence; use
  `KEEP_AS_NON_CORE`/`UNDECIDED` for substrate-specific claims that are not
  supported, and never `REMOVE` an experimental annotation whose full text was
  not read.
- **CRL4 core vs receptor.** `DDB1` is the adaptor/scaffold (not a receptor);
  `DDB2` and `DTL`/CDT2 are DCAF substrate receptors. `DDA1` stabilizes CRL4.
  `CAND2` (CAND1 paralog) and `GLMN` are **regulators** of CRL assembly, not
  ligases — avoid assigning them ubiquitin-ligase catalytic activity.
