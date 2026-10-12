---
title: "Cuproptosis: Copper-Dependent Cell Death"
marp: true
theme: default
paginate: true
backgroundColor: #fff
style: |
  section { font-size: 24px; }
  h1 { color: #2c3e50; }
  h2 { color: #34495e; }
  table { font-size: 18px; }
  section.lead h1 { font-size: 48px; }
---

<!-- _class: lead -->

# Cuproptosis: Copper-Dependent Cell Death

Copper-dependent regulated cell death via lipoylated mitochondrial proteins

**Chris Mungall | AI-Assisted Gene Review**

2026-06-22

---

## Why Cuproptosis?

- A **recently defined** form of regulated cell death, driven by direct binding
  of copper to **lipoylated** mitochondrial proteins.
- Mechanistically **distinct** from apoptosis, necroptosis, ferroptosis, and pyroptosis.
- Sensitivity tracks with **reliance on mitochondrial respiration** — making it a
  fast-growing focus in cancer therapy and copper-overload disease.
- Named and defined only in **2022** (Tsvetkov et al.), so literature and the
  corresponding GO annotations are still **young and incomplete**.
- Parallels the existing **Ferroptosis** project as a metal-dependent
  regulated-cell-death pathway.

---

## Key Biology / Mechanism

1. Copper enters the cell and reaches mitochondria.
2. The ferredoxin **FDX1** reduces **Cu²⁺ → Cu⁺**.
3. Cu⁺ binds **lipoylated DLAT** (E2 of the pyruvate dehydrogenase complex).
4. DLAT undergoes **disulfide-bond–dependent oligomerization / aggregation** —
   a hallmark of cuproptosis.
5. **Fe–S cluster proteins** are destabilized.
6. The resulting **proteotoxic stress** kills the cell.

FDX1 is also required for **protein lipoylation** — the very modification that
serves as the "bait" copper attacks.

---

## The Approach: AI Gene Review

- Systematically review existing **GO annotations** for each pathway gene using
  strict GO guidelines.
- Synthesize with **literature** evidence and **bioinformatic** inference.
- Distinguish **core functions** from over-annotation (e.g. generic "cell death"
  terms with only indirect support).
- Scope **ontology gaps** for this new modality.
- Status: **SCOPING** — eight existing review files are from other campaigns;
  nine candidate genes still need cuproptosis-focused review.

---

## Pathway Architecture

- **Copper delivery & homeostasis** — set the threshold for cuproptosis
  (SLC31A1, ATP7A, ATP7B, ATOX1).
- **Copper reduction (the trigger)** — FDX1 reduces Cu²⁺ → Cu⁺.
- **Lipoate installation and turnover** — builds the lipoyl "bait" and cycles
  it during catalysis (LIAS, LIPT1, LIPT2, GCSH, DLD).
- **PDH complex and lipoylated targets** — DLAT in the copper-attacked PDH
  complex, plus the E1 subunits PDHA1/PDHB.
- **Regulators & specificity controls** — set sensitivity
  (MTF1, GLS, CDKN2A, FDX2).

---

## Priority 1: FDX1, Lipoylation, and PDC Dependencies

| Gene | UniProt | Function |
|------|---------|----------|
| FDX1 | P10109 | Cu²⁺→Cu⁺ reduction; master regulator; promotes lipoylation |
| LIAS | O43766 | Lipoyl synthase |
| LIPT1 | Q9Y234 | Lipoyltransferase 1 |
| DLD | P09622 | Dihydrolipoamide dehydrogenase (E3) |
| DLAT | P10515 | Lipoylated PDH E2; copper-induced aggregation effector |
| PDHA1 | P08559 | Pyruvate dehydrogenase E1 alpha |
| PDHB | P11177 | Pyruvate dehydrogenase E1 beta |

7 genes — the FDX1, lipoylation, and PDH core to review first.

---

## Priority 2: Copper Handling & Regulation

| Gene | UniProt | Function |
|------|---------|----------|
| SLC31A1 | O15431 | Copper importer (CTR1) — raises sensitivity |
| ATP7A | Q04656 | Copper exporter (Menkes) — lowers intracellular Cu |
| ATP7B | P35670 | Copper exporter (Wilson) — lowers intracellular Cu |
| ATOX1 | O00244 | Cytosolic copper chaperone |
| MTF1 | Q14872 | Metal-responsive TF; **protective** regulator |
| GLS | O94925 | Glutaminase; sensitivity modulator |

~6 genes — they set the copper threshold and tune sensitivity.

---

## Priority 3: Supporting / Specificity Genes

| Gene | UniProt | Function |
|------|---------|----------|
| LIPT2 | A6NK58 | Lipoyl/octanoyl transferase 2 |
| GCSH | P23434 | Lipoylated glycine cleavage H protein |
| CDKN2A | P42771 | Sensitivity modulator |
| FDX2 | Q6P4F2 | FDX1 paralog; **non-redundant** specificity control |

~4 genes. Note: **FDX2 does NOT substitute for FDX1** in cuproptosis — a useful
specificity control.

---

## Key Recent Discoveries

1. **FDX1 = target of the copper ionophore elesclomol**
   — Tsvetkov et al., *Nat Chem Biol* 2019 (PMID:31133756). Established the
   FDX1–copper axis in regulated cell death.
2. **Definition of cuproptosis**
   — Tsvetkov et al., *Science* 2022 (PMID:35298263; erratum PMID:36356160).
   Genome-wide CRISPR screens identified FDX1 and the lipoylation pathway;
   showed copper binds lipoylated DLAT → aggregation + Fe–S cluster loss.
3. **Mechanistic / therapeutic syntheses**
   — Tang, Chen & Kang, *Mol Cell* 2022 (PMID:35594843). Placed cuproptosis
   among regulated-cell-death pathways with cancer-therapy implications.

---

## Disease & Therapeutic Relevance

- **Copper-handling disorders** frame the homeostatic thresholds:
  - Wilson disease (ATP7B loss → copper overload)
  - Menkes disease (ATP7A loss → copper deficiency)
- **Cancer therapy:**
  - Copper ionophores (elesclomol, disulfiram–Cu) selectively kill cells
    dependent on mitochondrial respiration / high lipoylation.
  - Copper chelators (e.g. tetrathiomolybdate) **block** cuproptosis.
- **Biomarker biology:** FDX1 and lipoylation status are emerging predictors of
  cuproptosis susceptibility across tumor types.

---

## Challenges: New Modality, GO Term Gaps

- How should **GO:0160119 cuproptosis** be used: direct execution, copper or
  lipoylation supply, or upstream sensitivity modulation?
- Are FDX1's **two roles** (Cu²⁺ reduction vs. promoting lipoylation) captured
  by distinct, appropriately specific MF/BP terms — or over-/under-annotated?
- **DLAT:** distinguish its canonical acetyltransferase MF from its
  cuproptosis-effector behavior (copper-induced aggregation) — the latter is a
  **process** role, not a new MF.
- Watch for **over-annotation** of every lipoate, PDH, or copper-homeostasis
  gene with a generic "cell death" term where support is indirect.

---

## Conclusions & Future Directions

- Cuproptosis: copper-dependent regulated cell death executed via **lipoylated
  mitochondrial proteins** and **Fe–S cluster loss** — a young, fast-moving field.
- Curation target: **17 genes** across 3 priority tiers (FDX1/lipoylation/PDC,
  copper handling, specificity controls).
- **Status: SCOPING.** Next steps:
  - [ ] Fetch FDX1, LIAS, SLC31A1, ATOX1, MTF1, LIPT2, CDKN2A, FDX2
  - [ ] Review Priority 1 genes (4/7), Priority 2 (3/6), Priority 3 (1/4)
  - [ ] Pathway summary + ontology-gap assessment
- Parallels the **Ferroptosis** project as a metal-dependent cell-death pathway.
