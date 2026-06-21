---
title: "Cuproptosis (Copper-Dependent Cell Death) Project"
maturity: SCOPING
tags: [BIOLOGY_DOMAIN]
species: [human]
---

# Cuproptosis (Copper-Dependent Cell Death) Project

## Overview

Cuproptosis is a recently defined form of regulated cell death driven by the
direct binding of copper to **lipoylated** proteins of the mitochondrial
tricarboxylic acid (TCA) cycle. It is mechanistically distinct from apoptosis,
necroptosis, ferroptosis, and pyroptosis. When intracellular Cu²⁺ is reduced to
Cu⁺ by the ferredoxin **FDX1**, copper binds lipoylated **DLAT** (the E2
component of the pyruvate dehydrogenase complex), triggering its disulfide-bond–
dependent oligomerization/aggregation, alongside destabilization of Fe–S cluster
proteins. The resulting proteotoxic stress kills the cell. Because cuproptosis
sensitivity tracks with reliance on mitochondrial respiration, it has rapidly
become a focus in cancer therapy and copper-overload disease.

The pathway was named and mechanistically defined by Tsvetkov et al. in 2022
(building on their 2019 identification of FDX1 as the target of the copper
ionophore elesclomol), so the literature — and the corresponding GO
annotations — are still young and incomplete. This makes it a good candidate for
focused review, and it parallels the existing **Ferroptosis** project as a
metal-dependent regulated-cell-death pathway.

## Model Species

**Primary: Homo sapiens (human)**
- UniProt species code: HUMAN
- The pathway was defined in human cell lines (genome-wide CRISPR screens)
- Direct disease relevance: Wilson disease / Menkes disease (copper handling),
  and cancer therapy (copper-ionophore strategies)

## Core Pathway Architecture

### 1. Copper Delivery and Homeostasis
Copper must enter the cell and reach mitochondria for cuproptosis to occur;
exporters and chaperones set the threshold:
- **SLC31A1** (CTR1) — high-affinity copper importer; raises cuproptosis sensitivity
- **ATP7A** — copper-exporting P-type ATPase (Menkes disease); lowers intracellular Cu
- **ATP7B** — copper-exporting P-type ATPase (Wilson disease); lowers intracellular Cu
- **ATOX1** — cytosolic copper chaperone delivering Cu to ATP7A/ATP7B

### 2. Copper Reduction — the Trigger
- **FDX1** — reduces Cu²⁺ → Cu⁺ and is the upstream master regulator of
  cuproptosis; also required for protein lipoylation. The single strongest hit
  in the defining CRISPR screens.

### 3. Protein Lipoylation Machinery
The lipoic acid post-translational modification on TCA-cycle E2 enzymes is the
"bait" that copper attacks; loss of this machinery confers resistance:
- **LIAS** — lipoyl synthase (inserts sulfur into the lipoyl moiety)
- **LIPT1** — lipoyl(amido)transferase 1
- **LIPT2** — lipoyl/octanoyl transferase 2
- **DLD** — dihydrolipoamide dehydrogenase (E3; shared component)

### 4. Lipoylated Targets — the Death Effectors
- **DLAT** — dihydrolipoamide S-acetyltransferase (PDH E2); copper-bound
  lipoylated DLAT oligomerizes/aggregates — a hallmark of cuproptosis
- **PDHA1** / **PDHB** — pyruvate dehydrogenase E1 α/β subunits
- **GCSH** — glycine cleavage system H protein (lipoylated)

### 5. Regulators and Specificity Controls
- **MTF1** — metal-regulatory transcription factor 1; induces metallothioneins
  and is **protective** (negative regulator)
- **GLS** — glutaminase; modulates sensitivity (negative regulator hit)
- **CDKN2A** — modulates sensitivity (negative regulator hit)
- **FDX2** — FDX1 paralog that does **not** substitute for FDX1 in cuproptosis;
  useful specificity control

## Genes for Review (Priority Order)

### Priority 1: Core Execution Machinery (~7 genes)
| Gene | UniProt | Function |
|------|---------|----------|
| FDX1 | P10109 | Cu²⁺→Cu⁺ reduction; master regulator; promotes lipoylation |
| LIAS | O43766 | Lipoyl synthase |
| LIPT1 | Q9Y234 | Lipoyltransferase 1 |
| DLD | P09622 | Dihydrolipoamide dehydrogenase (E3) |
| DLAT | P10515 | Lipoylated PDH E2; copper-induced aggregation effector |
| PDHA1 | P08559 | Pyruvate dehydrogenase E1 alpha |
| PDHB | P11177 | Pyruvate dehydrogenase E1 beta |

### Priority 2: Copper Handling and Regulation (~6 genes)
| Gene | UniProt | Function |
|------|---------|----------|
| SLC31A1 | O15431 | Copper importer (CTR1) |
| ATP7A | Q04656 | Copper exporter (Menkes) |
| ATP7B | P35670 | Copper exporter (Wilson) |
| ATOX1 | O00244 | Cytosolic copper chaperone |
| MTF1 | Q14872 | Metal-responsive TF; protective regulator |
| GLS | O94925 | Glutaminase; sensitivity modulator |

### Priority 3: Supporting / Specificity Genes (~4 genes)
| Gene | UniProt | Function |
|------|---------|----------|
| LIPT2 | A6NK58 | Lipoyl/octanoyl transferase 2 |
| GCSH | P23434 | Lipoylated glycine cleavage H protein |
| CDKN2A | P42771 | Sensitivity modulator |
| FDX2 | Q6P4F2 | FDX1 paralog; non-redundant specificity control |

## Key Recent Discoveries

1. **FDX1 as the target of the copper ionophore elesclomol** (Tsvetkov et al.,
   *Nat Chem Biol* 2019, PMID:31133756) — established the FDX1–copper axis in
   regulated cell death.
2. **Definition of cuproptosis** (Tsvetkov et al., *Science* 2022,
   PMID:35298263; erratum PMID:36356160) — genome-wide CRISPR screens identified
   FDX1 and the lipoylation pathway; showed copper binds lipoylated DLAT causing
   aggregation and Fe–S cluster protein loss.
3. **Mechanistic/therapeutic syntheses** (e.g. Tang, Chen & Kang, *Mol Cell*
   2022, PMID:35594843) — placed cuproptosis among regulated-cell-death pathways
   and outlined cancer-therapy implications.

## Disease and Therapeutic Relevance

- **Copper-handling disorders**: Wilson disease (ATP7B loss → copper overload)
  and Menkes disease (ATP7A loss → copper deficiency) frame the homeostatic
  thresholds for cuproptosis.
- **Cancer therapy**: copper ionophores (elesclomol, disulfiram–Cu) selectively
  kill cells dependent on mitochondrial respiration / high lipoylation; copper
  chelators (e.g. tetrathiomolybdate) block cuproptosis.
- **Biomarker biology**: FDX1 and lipoylation status are emerging predictors of
  cuproptosis susceptibility across tumor types.

## Curation Focus / Open Questions

- Is there (or should there be) a GO biological-process term for cuproptosis,
  analogous to GO:0097707 *ferroptosis*? Scope the ontology gap.
- Are FDX1's two roles (Cu²⁺ reduction vs. promoting protein lipoylation)
  captured by distinct, appropriately specific MF/BP terms, or over-/under-annotated?
- DLAT: distinguish its canonical acetyltransferase MF from its
  cuproptosis-effector behavior (copper-induced aggregation) — the latter is a
  process role, not a new MF.
- Watch for over-annotation of every lipoylation/TCA gene with a generic
  "cell death" process term where the experimental support is indirect.

## Key References

- Tsvetkov P et al. (2019) *Nat Chem Biol* — FDX1/elesclomol (PMID:31133756)
- Tsvetkov P et al. (2022) *Science* — Cuproptosis definition (PMID:35298263; erratum PMID:36356160)
- Tang D, Chen X, Kang R (2022) *Mol Cell* — Mechanisms review (PMID:35594843)

## Project Status

- [ ] Stub — needs gene folder setup (`just fetch-gene human <GENE>`)
- [ ] Priority 1 genes reviewed (0/7)
- [ ] Priority 2 genes reviewed (0/6)
- [ ] Priority 3 genes reviewed (0/4)
- [ ] Pathway summary + ontology-gap assessment
