# C. elegans P Granule/Germ Granule Dynamics Project

## Overview

P granules are germline-specific ribonucleoprotein (RNP) condensates in *C. elegans* that are paradigmatic examples of biomolecular condensates formed via liquid-liquid phase separation (LLPS). They are essential for germline development, fertility, and transgenerational epigenetic inheritance. P granules were among the first biological condensates shown to exhibit liquid-like properties.

P granules contain RNA regulatory machinery including Argonaute proteins, RNA helicases, and intrinsically disordered proteins. They associate with nuclear pores in adult germlines and segregate asymmetrically during early embryogenesis to specify germline fate.

## Model Species

**Primary: Caenorhabditis elegans (worm)**
- UniProt species code: CAEEL
- P granules discovered and best characterized in worms
- Excellent live imaging and genetics
- Paradigm for LLPS/condensate biology

## Core Pathway Architecture

### 1. Core Structural Proteins (PGL Family)
RGG-domain proteins that scaffold P granules:
- **pgl-1** - P granule abnormality 1 (core scaffold) [ALREADY REVIEWED]
- **pgl-3** - P granule abnormality 3 (core scaffold) [ALREADY REVIEWED]

### 2. VASA-like RNA Helicases (GLH Family)
DEAD-box helicases essential for P granule integrity:
- **glh-1** - Germline helicase 1 (DDX4/VASA ortholog)
- **glh-2** - Germline helicase 2
- **glh-4** - Germline helicase 4

### 3. MEG Proteins (P Granule Regulators)
Intrinsically disordered proteins regulating P granule dynamics:
- **meg-1** - Maternal-effect germ cell defective 1
- **meg-2** - Maternal-effect germ cell defective 2
- **meg-3** - Key scaffold, phase separation driver
- **meg-4** - Redundant with meg-3

### 4. RNA Regulatory Machinery
Small RNA pathway components enriched in P granules:
- **prg-1** - Piwi-related gene 1 (piRNA pathway)
- **prg-2** - Piwi-related gene 2
- **csr-1** - Chromosome segregation and RNAi deficient
- **wago-1** - Worm-specific Argonaute
- **deps-1** - Defective P granules and sterile (Argonaute scaffold)

### 5. Perinuclear Anchoring
Proteins anchoring P granules to nuclear pores:
- **npp-10** - Nuclear pore protein (anchor)

### 6. Phase Separation Regulators
Kinases and factors controlling condensation:
- **mbk-2** - Minibrain kinase (DYRK ortholog, regulates MEG proteins)
- **mex-5** - Muscle excess 5 (RNA-binding, polarity)
- **mex-6** - Muscle excess 6 (redundant with mex-5)
- **par-1** - Partitioning defective 1 (polarity kinase)

### 7. Z Granule Components
Adjacent condensate for secondary siRNA amplification:
- **znfx-1** - Zinc finger NFX1-type 1 (Z granule marker)
- **wago-4** - Z granule Argonaute

### 8. Mutator Foci Components
Adjacent condensate for siRNA amplification:
- **mut-16** - Mutator 16 (Mutator focus scaffold)
- **rde-2** - RNAi defective 2

### 9. RNA Metabolism
- **car-1** - Cytokinesis, apoptosis, RNA-associated (LSM14)
- **cgh-1** - Conserved germline helicase (DDX6)
- **pab-1** - Poly(A) binding protein

## Genes for Review (Priority Order)

### Priority 1: Core P Granule Proteins (~7 genes)
| Gene | UniProt | Function | Status |
|------|---------|----------|--------|
| pgl-1 | Q9U2C8 | Core scaffold, RGG domain | REVIEWED |
| pgl-2 | P34266 | Core scaffold, RGG domain | REVIEWED |
| pgl-3 | G5EBV6 | Core scaffold, RGG domain | REVIEWED |
| glh-1 | P34689 | VASA helicase, essential | REVIEWED |
| glh-4 | O02123 | Germline helicase | REVIEWED |
| meg-3 | Q9TXM1 | IDR protein, phase separation | REVIEWED |
| meg-4 | Q9TZK8 | meg-3 paralog | REVIEWED |

### Priority 2: RNA Silencing Machinery (~6 genes)
| Gene | UniProt | Function | Status |
|------|---------|----------|--------|
| prg-1 | P90786 | Piwi, piRNA pathway | REVIEWED |
| csr-1 | Q21992 | Argonaute, chromosome segregation | REVIEWED |
| deps-1 | Q9N303 | P granule scaffold for Argonautes | REVIEWED |
| wago-1 | Q21770 | Secondary siRNA pathway | REVIEWED |
| znfx-1 | G5EGT6 | Z granule, siRNA inheritance | REVIEWED |
| mut-16 | O62011 | Mutator focus scaffold | REVIEWED |

### Priority 3: Regulators and Additional Components (~6 genes)
| Gene | UniProt | Function | Status |
|------|---------|----------|--------|
| meg-1 | Q21126 | P granule regulator | REVIEWED |
| meg-2 | Q21127 | P granule regulator | REVIEWED |
| mbk-2 | Q09460 | DYRK kinase, MEG phosphorylation | REVIEWED |
| mex-5 | O44783 | Polarity, RNA binding | REVIEWED |
| car-1 | Q9XW17 | LSM14 ortholog | REVIEWED |
| cgh-1 | P34549 | DDX6 helicase | REVIEWED |

## Key Biological Processes

### Asymmetric Segregation
During the first embryonic cell division, P granules segregate to the posterior P1 blastomere. This requires:
1. PAR polarity proteins
2. MEX-5/MEX-6 RNA-binding proteins
3. MBK-2 kinase regulation of MEG proteins

### Phase Separation Dynamics
P granules exhibit:
- Liquid-like fusion and fission
- Internal rearrangement
- Regulated assembly/disassembly
- Temperature-dependent viscosity

### Transgenerational Epigenetic Inheritance
P granules maintain:
- piRNA-mediated silencing
- RNAi inheritance across generations
- Germline identity

## Key Phenotypes

- **Sterility** - Complete loss of P granules causes sterility
- **Mortal germline (Mrt)** - Progressive sterility over generations
- **Enhanced RNAi (Eri)** - Altered small RNA pathways
- **RNAi defective (Rde)** - Loss of RNAi response

## Key References

- Brangwynne CP et al. (2009) Science - P granules as liquid droplets
- Updike D & Strome S (2010) Dev Dyn - P granule review
- Wang JT et al. (2014) eLife - MEG proteins in phase separation
- Putnam A et al. (2019) Nat Struct Mol Biol - GLH and PGL interactions
- Ouyang JPT & Bharat T (2023) J Mol Biol - Comprehensive review
- Manage KI et al. (2020) Dev Cell - Z granules and ZNFX-1

## Disease Relevance

While *C. elegans* specific, P granule biology informs:
- **Infertility** - Germ cell development defects
- **ALS/FTD** - Stress granule dysfunction parallels
- **Cancer** - Germline tumor biology

## Project Status

### Priority 1: Core P Granule Proteins
- [x] pgl-1 (Q9U2C8) - COMPLETE
- [x] pgl-2 (P34266) - COMPLETE
- [x] pgl-3 (G5EBV6) - COMPLETE
- [x] glh-1 (P34689) - COMPLETE
- [x] glh-4 (O02123) - COMPLETE
- [x] meg-3 (Q9TXM1) - COMPLETE
- [x] meg-4 (Q9TZK8) - COMPLETE

### Priority 2: RNA Silencing Machinery
- [x] prg-1 (P90786) - COMPLETE - Piwi/piRNA pathway
- [x] csr-1 (Q21992) - COMPLETE - Essential Argonaute, chromosome segregation
- [x] deps-1 (Q9N303) - COMPLETE - P granule scaffold
- [x] wago-1 (Q21770) - COMPLETE - Secondary siRNA pathway
- [x] znfx-1 (G5EGT6) - COMPLETE - Z granule marker, RNAi inheritance
- [x] mut-16 (O62011) - COMPLETE - Mutator focus scaffold

### Priority 3: Regulators
- [x] meg-1 (Q21126) - COMPLETE - P granule/germline P-body
- [x] meg-2 (Q21127) - COMPLETE - Highly disordered regulator
- [x] mbk-2 (Q09460) - COMPLETE - DYRK kinase, 51 annotations reviewed
- [x] mex-5 (O44783) - COMPLETE - RNA competition, polarity
- [x] car-1 (Q9XW17) - COMPLETE - LSM14 ortholog
- [x] cgh-1 (P34549) - COMPLETE - DDX6 helicase

---
# STATUS

## 2025-12-27 - PROJECT COMPLETE
- **ALL 19 GENES REVIEWED** - Priority 1, 2, and 3 all complete

### Priority 2 Summary (RNA Silencing Machinery):
- **prg-1**: Piwi/21U-RNA pathway, 28 annotations, removed incorrect nucleus and pole cell annotations
- **csr-1**: NOTE - fetched data was for wrong gene (nhr-47), proposed corrections for actual CSR-1 Argonaute
- **deps-1**: P granule scaffold, added molecular condensate scaffold activity
- **wago-1**: 22G-RNA pathway, removed nuclear localization and RNA endonuclease (lacks catalytic residues)
- **znfx-1**: Z granule marker for transgenerational RNAi inheritance, removed incorrect nuclear annotations
- **mut-16**: Mutator focus scaffold for siRNA amplification, added transposable element silencing

### Priority 3 Summary (Regulators):
- **meg-1**: Germline P-body component with MEG-2, phosphorylation-regulated
- **meg-2**: Most disordered MEG protein (87%), regulates granule dynamics
- **mbk-2**: DYRK kinase with 51 annotations - phosphorylates MEGs for P granule disassembly
- **mex-5**: RNA competition mechanism for P granule dissolution, PAR-1 regulated gradient
- **car-1**: LSM14 ortholog, cytokinesis/apoptosis/RNA functions
- **cgh-1**: DDX6 helicase, protects from germline apoptosis

## 2025-12-27 (continued)
- **Priority 1 COMPLETE** - All 7 core P granule protein reviews finished
- pgl-3: Fixed incorrect stress granule annotation, added protein dimerization activity
- glh-1: 37 annotations reviewed - VASA ortholog, essential for P granule integrity
- glh-4: 17 ACCEPT, 1 REMOVE (SSU-rRNA), 1 MODIFY, 2 NEW annotations
- meg-3: Added GO:0140693 (molecular condensate scaffold activity), GO:0060293 (germ plasm)
- meg-4: Similar to meg-3, marked HT-Y2H protein binding as over-annotated
- Key finding: MEG-3/MEG-4 are paradigmatic IDR scaffold proteins for phase separation

## 2025-12-27
- Project created
- pgl-1, pgl-2 reviews COMPLETE
- pgl-3 review in DRAFT status
- Fetched data for glh-1, glh-4, meg-3, meg-4
- Running deep research for Priority 1 genes

# NOTES

## 2025-12-27
- Building on existing pgl-1/2/3 reviews
- P granules are paradigm for LLPS/condensate biology
- Strong connection to small RNA pathways and transgenerational inheritance
- Related to stress granules project (LLPS theme)

### Key genes to focus on:
- **glh-1**: VASA-like DEAD box helicase, essential for P granule integrity
- **meg-3/meg-4**: IDR proteins that drive phase separation
- These genes are critical for understanding P granule biophysics
