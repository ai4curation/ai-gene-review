---
title: "Peroxisome Biogenesis Project"
maturity: MATURE
last_reviewed: "2026-10-05"
tags: [BIOLOGY_DOMAIN]
species: [human]
genes: [PEX1, PEX2, PEX3, PEX5, PEX6, PEX7, PEX10, PEX11A, PEX11B, PEX11G, PEX12, PEX13, PEX14, PEX16, PEX19, PEX26]
manifest:
  slides:
    - href: PEROXISOME/slides/PEROXISOME-slides.html
      description: AI generated
---

# Peroxisome Biogenesis Project

**Bottom line:** peroxisomes are built and maintained by the PEX proteins
(peroxins), which insert membrane proteins, import matrix enzymes through a
receptor-docking-recycling cycle, and divide the organelle; their loss causes
Zellweger spectrum disorders. We reviewed every existing GO annotation on the
16 human peroxins, in three phases: import and recycling, the RING ligases and
docking complex, then membrane biogenesis and proliferation. All 16 reviews
are in the repo (828 annotations: 561 accepted, 51 kept as non-core, 94 marked
over-annotated, 44 modified, 65 removed, 11 NEW, 2 undecided). PEX39, a
recently characterized PTS2-import factor that binds PEX7, has its own review
but is outside this set. Generic `protein binding` was
the dominant problem: 35 of PEX19's 37 removals and 18 of PEX5's 20
over-annotations are `protein binding` IPI rows. The other recurring pattern
was guilt by cargo or phenotype, where a peroxin is annotated to the metabolic
process of the enzymes it imports or to a downstream knockout phenotype; these
rows were mostly kept as non-core (PEX7 ether lipid biosynthesis, PEX13 neuron
migration) rather than removed. The
conserved machinery is modelled in the
[peroxisome lifecycle module](../modules/peroxisome-lifecycle.html), and the
targeting-signal binding obsoletion has already been folded into the PEX5,
PEX7 and PEX19 reviews. The two remaining `UNDECIDED` rows are tracked in
[#4242](https://github.com/ai4curation/ai-gene-review/issues/4242).

## Overview

Peroxisomes are single-membrane-bound organelles found in virtually all eukaryotic cells.
They perform essential metabolic functions including fatty acid beta-oxidation (especially
very long-chain fatty acids), ether lipid (plasmalogen) synthesis, bile acid synthesis,
and reactive oxygen species metabolism. The peroxisome biogenesis machinery is encoded by
PEX (peroxin) genes, mutations in which cause Zellweger spectrum disorders (ZSD) and
other peroxisomal biogenesis disorders (PBDs).

## Model Species

**Primary: Homo sapiens (human)**

- Zellweger spectrum disorders provide clinical relevance
- Comprehensive proteomics data available
- Well-characterized import pathways

## Functional Architecture of the PEX Machinery

### 1. Membrane Protein Insertion (Class I)
- **PEX3** - Membrane anchor for PEX19-cargo complexes
- **PEX19** - Cytosolic chaperone/receptor for peroxisomal membrane proteins (PMPs)
- **PEX16** - Membrane receptor, recruits PEX3 to peroxisomes

### 2. Matrix Protein Import - Receptors (Class II)
- **PEX5** - PTS1 (C-terminal -SKL) receptor, cycling receptor
- **PEX7** - PTS2 (N-terminal nonapeptide) receptor

### 3. Docking Complex (Class III)
- **PEX13** - Docking complex component, SH3 domain
- **PEX14** - Central docking component, forms transient pore

### 4. RING Complex / Ubiquitination (Class IV)
- **PEX2** - E3 ubiquitin ligase (RING domain)
- **PEX10** - E3 ubiquitin ligase (RING domain)
- **PEX12** - E3 ubiquitin ligase (RING domain)

### 5. Receptor Recycling / AAA ATPase Complex (Class V)
- **PEX1** - AAA+ ATPase, receptor export
- **PEX6** - AAA+ ATPase, receptor export
- **PEX26** - Membrane anchor for PEX1-PEX6 complex

### 6. Peroxisome Proliferation / Division (Class VI)
- **PEX11A** - Peroxisome elongation/proliferation (inducible)
- **PEX11B** - Peroxisome elongation/proliferation (constitutive)
- **PEX11G** - Peroxisome elongation/proliferation (tissue-specific)

## Evolutionary Conservation

The PEX machinery shows tiered conservation:

- **Deeply conserved (yeast to human)**: PEX1, 2, 3, 5, 6, 7, 10, 12, 13, 14, 19
- **Metazoan innovations**: PEX11 family expansion (1 in yeast -> 3 in human)
- **Vertebrate-specific**: PEX26 (replaces yeast PEX15, convergent evolution)
- **Recently characterized**: PEX5L (PEX5-related), PEX39

Key reference: Jansen et al. (2021) "Comparative Genomics of Peroxisome Biogenesis Proteins:
Making Sense of the PEX Proteins" Front Cell Dev Biol 9:654163.

## Disease Relevance

| Disease | OMIM | Key Genes |
|---------|------|-----------|
| Zellweger syndrome (most severe) | 214100 | PEX1, PEX2, PEX3, PEX5, PEX6, PEX10, PEX12, PEX13, PEX14, PEX16, PEX19, PEX26 |
| Neonatal adrenoleukodystrophy | 202370 | PEX1, PEX5, PEX10, PEX13, PEX26 |
| Infantile Refsum disease | 266510 | PEX1, PEX2, PEX26 |
| Rhizomelic chondrodysplasia punctata type 1 | 215100 | PEX7 |
| Heimler syndrome | 234580 | PEX1, PEX6 |

PEX1 is the most commonly mutated gene (~65% of ZSD cases), followed by PEX6 (~16%) and PEX26 (~5%).

## Candidate Genes - Priority Order

Priority is based on: (1) disease prevalence in ZSD, (2) functional centrality,
(3) evolutionary conservation depth.

### Phase 1: Core Import/Recycling (highest priority)

| Gene | UniProt | Function | ZSD Frequency |
|------|---------|----------|---------------|
| PEX1 | O43933 | AAA+ ATPase, receptor recycling | ~65% |
| PEX5 | P50542 | PTS1 receptor | ~4% |
| PEX6 | Q13608 | AAA+ ATPase, receptor recycling | ~16% |
| PEX7 | O00628 | PTS2 receptor | RCDP1 |
| PEX14 | O75381 | Docking complex | Rare |
| PEX26 | Q7Z412 | PEX1/PEX6 anchor | ~5% |

### Phase 2: RING Complex & Docking

| Gene | UniProt | Function | ZSD Frequency |
|------|---------|----------|---------------|
| PEX2 | P28328 | RING E3 ligase | ~3% |
| PEX10 | O60683 | RING E3 ligase | ~3% |
| PEX12 | O00623 | RING E3 ligase | ~4% |
| PEX13 | Q92968 | Docking complex, SH3 | Rare |

### Phase 3: Membrane Biogenesis & Proliferation

| Gene | UniProt | Function |
|------|---------|----------|
| PEX3 | P56589 | PMP membrane anchor |
| PEX16 | Q9Y5Y5 | PMP membrane receptor |
| PEX19 | P40855 | PMP chaperone/receptor |
| PEX11A | O75192 | Proliferation (inducible) |
| PEX11B | O96011 | Proliferation (constitutive) |
| PEX11G | Q96HA9 | Proliferation (tissue-specific) |

---
# STATUS

## Phase 1 Genes
- **Done:** PEX1 (O43933)
- **Done:** PEX5 (P50542)
- **Done:** PEX6 (Q13608)
- **Done:** PEX7 (O00628)
- **Done:** PEX14 (O75381)
- **Done:** PEX26 (Q7Z412)

## Phase 2 Genes
- **Done:** PEX2 (P28328)
- **Done:** PEX10 (O60683)
- **Done:** PEX12 (O00623)
- **Done:** PEX13 (Q92968)

## Phase 3 Genes
- **Done:** PEX3 (P56589)
- **Done:** PEX16 (Q9Y5Y5)
- **Done:** PEX19 (P40855)
- **Done:** PEX11A (O75192)
- **Done:** PEX11B (O96011)
- **Done:** PEX11G (Q96HA9)

# NOTES

## 2026-03-05

Original completion notes from the first pass over the 16-gene set. Exact
per-gene action counts in this March snapshot were superseded by later
receptor-term obsoletion and RING-complex follow-up edits; use the current
YAMLs and the 2026-10-05 aggregate above for live counts.

- Phase 3 annotation reviews complete (all 6 genes: PEX3, PEX16, PEX19, PEX11A, PEX11B, PEX11G)
- Key findings across Phase 3:
    - PEX19 had the largest removal set, driven mostly by generic protein-binding rows from high-throughput interactome studies
    - PEX3 and PEX11B carried many downstream metabolic-process or knockout-phenotype over-annotations
    - PEX11G was the smallest Phase 3 review; its tissue-specific role was confirmed
    - PEX16: 3 annotations removed; well-characterized ER-to-peroxisome pathway annotations retained
    - Several NEW annotations proposed across Phase 3 genes (PEX16, PEX19, PEX11A, PEX11G)

- Phase 2 annotation reviews complete (all 4 genes: PEX2, PEX10, PEX12, PEX13)
- Key findings across Phase 2:
    - RING complex (PEX2/PEX10/PEX12) shows cleaner annotations than Phase 1 receptors — fewer over-annotations
    - PEX2: 5 annotations removed, including generic protein binding; 9 non-core (downstream metabolic processes)
    - PEX10 had strong ISS evidence from the cryo-EM channel paper (PMID:35768507)
    - PEX12: 4 modify actions, mostly refining E3 ligase specificity; bridges RING complex to docking via PEX5/PEX10 interactions
    - PEX13 downstream metabolic annotations were flagged, and its SH3-domain scaffold function was confirmed

- Phase 1 annotation reviews complete (all 6 genes)
- Key findings across Phase 1:
    - Pervasive over-annotation of generic "protein binding" (GO:0005515) across all genes (25+ instances)
    - PEX7: homodimerization annotation (GO:0042803) contradicted by cited paper PMID:11931631 which shows WD40 repeat mediates PTS2 binding, not dimerization
    - PEX14: phase separation behavior emerging as new paradigm for import pore (PMID:34551879)
    - PEX14: beta-tubulin binding (GO:0048487) is a validated core function, connecting peroxisomes to cytoskeleton
    - PEX5 had the highest annotation count in the set
    - PEX26: convergent evolution with yeast PEX15 visible in annotation evidence patterns
    - Guilt-by-cargo pattern: several genes annotated with cargo metabolic processes (e.g. ether lipid biosynthesis for PEX7)

## 2026-05-01

- Tracking upstream obsoletion of GO:0005052/GO:0005053/GO:0033328 (peroxisome
  matrix/membrane targeting signal binding) → merged into renamed parent
  "peroxisome signal sequence receptor activity". Affects PEX5, PEX7, PEX19
  reviews. See [PEROXISOME_TARGETING_SIGNAL_OBSOLETION.md](PEROXISOME_TARGETING_SIGNAL_OBSOLETION.md).

## 2026-03-05 (initial)

- Project created, focusing on human peroxisome biogenesis (PEX) genes
- Prioritized Phase 1 as core import/recycling machinery (PEX1, PEX5, PEX6, PEX7, PEX14, PEX26)
- PEX1 is highest priority: most commonly mutated in Zellweger spectrum disorders
- Will start with Phase 1 genes, fetching data and performing annotation review
