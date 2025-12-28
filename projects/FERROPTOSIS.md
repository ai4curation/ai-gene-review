# Ferroptosis Regulation Project

## Overview

Ferroptosis is a form of regulated cell death characterized by iron-dependent lipid peroxidation. Distinct from apoptosis, necrosis, and autophagy, ferroptosis involves the accumulation of lipid reactive oxygen species (ROS) when glutathione-dependent lipid repair systems are compromised. The field has exploded since 2020 with discoveries of parallel defense pathways.

## Model Species

**Primary: Homo sapiens (human)**
- UniProt species code: HUMAN
- Best characterized system with therapeutic relevance
- Cancer therapy and neurodegeneration applications

## Core Pathway Architecture

### 1. Lipid Peroxidation Substrates
Genes that supply polyunsaturated fatty acids (PUFAs) to phospholipids:
- **ACSL4** - Acyl-CoA synthetase long-chain family member 4 (activates PUFAs)
- **LPCAT3** - Lysophosphatidylcholine acyltransferase 3 (incorporates PUFAs into membranes)

### 2. Iron Metabolism
Iron is essential for lipid peroxidation:
- **TFRC** - Transferrin receptor (iron import)
- **SLC40A1** - Ferroportin (iron export)
- **NCOA4** - Nuclear receptor coactivator 4 (ferritinophagy receptor)
- **FTH1/FTL** - Ferritin heavy/light chains (iron storage)

### 3. GPX4-Dependent Defense (Classical Pathway)
The glutathione peroxidase system:
- **GPX4** - Glutathione peroxidase 4 (THE key ferroptosis suppressor)
- **SLC7A11** - Solute carrier family 7 member 11 / xCT (cystine import)
- **SLC3A2** - 4F2 heavy chain (xCT partner)
- **GSS** - Glutathione synthetase
- **GCLC/GCLM** - Glutamate-cysteine ligase (rate-limiting for GSH synthesis)

### 4. FSP1/CoQ10 Pathway (Discovered 2019-2020)
GPX4-independent ferroptosis suppression:
- **FSP1** (AIFM2) - Ferroptosis suppressor protein 1 (CoQ10 reductase)
- **DHODH** - Dihydroorotate dehydrogenase (mitochondrial CoQ10 reduction)

### 5. GCH1/BH4 Pathway (Discovered 2020-2022)
Tetrahydrobiopterin-mediated protection:
- **GCH1** - GTP cyclohydrolase 1 (rate-limiting for BH4 synthesis)
- **PTS** - 6-pyruvoyltetrahydropterin synthase
- **SPR** - Sepiapterin reductase

### 6. Transcriptional Regulators
- **NFE2L2** (NRF2) - Master antioxidant regulator
- **KEAP1** - NRF2 inhibitor
- **ATF4** - Integrated stress response transcription factor
- **TP53** - p53, context-dependent regulator

### 7. Membrane Lipid Composition
- **ELOVL5** - Fatty acid elongase
- **FADS1/FADS2** - Fatty acid desaturases

## Genes for Review (Priority Order)

### Priority 1: Core Machinery (~8 genes)
| Gene | UniProt | Function |
|------|---------|----------|
| GPX4 | P36969 | Lipid hydroperoxide reduction |
| SLC7A11 | Q9UPY5 | Cystine/glutamate antiporter |
| ACSL4 | O60488 | PUFA-CoA synthesis |
| FSP1/AIFM2 | Q9BRQ8 | CoQ10-dependent lipid repair |
| DHODH | Q02127 | Mitochondrial CoQ10 reduction |
| GCH1 | P30793 | BH4 synthesis |
| LPCAT3 | Q6NVY1 | PUFA incorporation |
| NCOA4 | Q13772 | Ferritinophagy receptor |

### Priority 2: Regulatory Network (~8 genes)
| Gene | UniProt | Function |
|------|---------|----------|
| NFE2L2 | Q16236 | NRF2 - antioxidant response |
| KEAP1 | Q14145 | NRF2 inhibitor |
| TFRC | P02786 | Iron import |
| FTH1 | P02794 | Iron storage |
| ATF4 | P18848 | Stress response TF |
| SLC40A1 | Q9NP59 | Iron export |
| GCLC | P48506 | GSH synthesis |
| TP53 | P04637 | Context-dependent regulator |

### Priority 3: Supporting Genes (~6 genes)
| Gene | UniProt | Function |
|------|---------|----------|
| SLC3A2 | P08195 | xCT partner (4F2hc) |
| GSS | P48637 | GSH synthesis |
| PTS | Q03393 | BH4 pathway |
| SPR | P35270 | BH4 pathway |
| FADS1 | O60427 | PUFA synthesis |
| ELOVL5 | Q9NYP7 | PUFA elongation |

## Key Recent Discoveries (2020+)

1. **FSP1/CoQ10 pathway** (Nature 2019) - GPX4-independent ferroptosis suppression
2. **DHODH in mitochondria** (Nature 2021) - Mitochondrial ferroptosis defense
3. **GCH1/BH4 pathway** (Nature 2022) - Third parallel defense system
4. **MBOAT1/2** (Nature 2023) - Sex hormone-regulated ferroptosis resistance
5. **Membrane lipid remodeling** (Cell 2020+) - Role of specific phospholipids

## Disease Relevance

- **Cancer**: Ferroptosis induction as therapy; resistance mechanisms
- **Neurodegeneration**: Ferroptosis in Parkinson's, Huntington's, ALS
- **Ischemia-reperfusion**: Organ damage
- **Kidney disease**: Acute kidney injury

## Key References

- Stockwell BR et al. (2017) Cell - Foundational review
- Doll S et al. (2019) Nature - FSP1 discovery
- Mao C et al. (2021) Nature - DHODH
- Kraft VAN et al. (2020) ACS Cent Sci - GCH1
- Jiang X et al. (2021) Nat Rev Mol Cell Biol - Comprehensive review
- Chen X et al. (2021) Signal Transduct Target Ther - Mechanisms update

## Project Status

- [x] Create gene folders and fetch UniProt/GOA data
- [x] Priority 1 genes review (8/8 genes)
- [x] Priority 2 genes review (8/8 genes)
- [x] Priority 3 genes review (6/6 genes)
- [x] Pathway summary and integration

---

# STATUS

**All 22 ferroptosis genes reviewed and validated (2025-12-28)**

✓ All gene folders created with UniProt/GOA data
✓ All 22 genes have completed AI reviews
✓ All reviews validated (0 errors)
✓ Pathway summary document created (FERROPTOSIS-pathway.md)
✓ Ready for PR

# NOTES

## 2025-12-28

**Completion Session - Full Project Finished**

### Gene Review Completion Summary

**Priority 1 (Core Machinery) - COMPLETED**
- GPX4 (P36969) ✓
- SLC7A11 (Q9UPY5) ✓
- ACSL4 (O60488) ✓
- FSP1/AIFM2 (Q9BRQ8) ✓
- DHODH (Q02127) ✓
- GCH1 (P30793) ✓
- LPCAT3 (Q6NVY1) ✓
- NCOA4 (Q13772) ✓

**Priority 2 (Regulatory Network) - COMPLETED**
- NFE2L2 (Q16236) ✓
- KEAP1 (Q14145) ✓
- TFRC (P02786) ✓
- FTH1 (P02794) ✓
- ATF4 (P18848) ✓
- SLC40A1 (Q9NP59) ✓
- GCLC (P48506) ✓
- TP53 (P04637) ✓

**Priority 3 (Supporting Genes) - COMPLETED**
- SLC3A2 (P08195) ✓
- GSS (P48637) ✓
- PTS (Q03393) ✓
- SPR (P35270) ✓
- FADS1 (O60427) ✓
- ELOVL5 (Q9NYP7) ✓

### Validation Results

- Total files validated: 592 (across entire codebase)
- Ferroptosis genes: 22/22 validated successfully
- Validation errors: 0
- Validation warnings: Present but manageable (mostly missing supporting text citations in some genes)
- All genes pass core validation

### Deliverables

1. **Gene Reviews**: 22 comprehensive AI gene review YAML files
2. **Pathway Summary**: `genes/human/FERROPTOSIS-pathway.md` created with:
   - Comprehensive ferroptosis mechanism overview
   - Three parallel defense systems documented (GPX4-GSH, FSP1-CoQ10, DHODH-CoQ10)
   - Emerging GCH1-BH4 system
   - Transcriptional regulation (NRF2/ARE pathway)
   - p53 context-dependent roles
   - Disease relevance and therapeutic implications
   - Full mermaid pathway diagram
   - 15+ peer-reviewed citations

### Next Steps

Ready for PR creation with branch `ferroptosis-completion` containing:
- All 22 gene review YAML files
- Supporting publications (PMIDs)
- Pathway summary document
- Updated project status
