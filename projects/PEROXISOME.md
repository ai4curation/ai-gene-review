# Peroxisome Biogenesis Project

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
- [ ] PEX1 (O43933)
- [ ] PEX5 (P50542)
- [ ] PEX6 (Q13608)
- [ ] PEX7 (O00628)
- [ ] PEX14 (O75381)
- [ ] PEX26 (Q7Z412)

## Phase 2 Genes
- [ ] PEX2 (P28328)
- [ ] PEX10 (O60683)
- [ ] PEX12 (O00623)
- [ ] PEX13 (Q92968)

## Phase 3 Genes
- [ ] PEX3 (P56589)
- [ ] PEX16 (Q9Y5Y5)
- [ ] PEX19 (P40855)
- [ ] PEX11A (O75192)
- [ ] PEX11B (O96011)
- [ ] PEX11G (Q96HA9)

# NOTES

## 2026-03-05

- Project created, focusing on human peroxisome biogenesis (PEX) genes
- Prioritized Phase 1 as core import/recycling machinery (PEX1, PEX5, PEX6, PEX7, PEX14, PEX26)
- PEX1 is highest priority: most commonly mutated in Zellweger spectrum disorders
- Will start with Phase 1 genes, fetching data and performing annotation review
