# Mitochondrial Import Pathways Project

## Overview

Reorganization of GO terms for mitochondrial protein import pathways, driven by GO-CAM modelling work.

Based on: https://github.com/geneontology/go-ontology/issues/31711

## Background

Mitochondrial protein import involves multiple distinct pathways for different classes of precursor proteins:

1. **MIM/MTCH pathway** — α-helical outer membrane protein insertion (via Tom70 → MIM complex)
2. **TOM-TIM23-PAM pathway** — presequence-bearing proteins imported into the matrix
3. **TOM-TIM23-SORT pathway** — lateral insertion of proteins into the inner membrane via TIM23
4. **TOM-SAM pathway** — β-barrel outer membrane protein insertion
5. **TOM-TIM22 pathway** — inner membrane metabolite carrier import (carrier pathway)
6. **TOM-MIA pathway** — IMS protein import via the disulfide relay system (CX₃C/CX₉C motifs)
7. **OXA pathway** — inner membrane insertion of mitochondrial-encoded proteins (not import per se)

## Proposed GO Term Changes (from issue #31711)

### New terms proposed
- Mitochondrial protein import pathway (parent term)
- Mitochondrial outer membrane alpha helical protein insertion (MIM/MTCH pathway)
- TOM-TIM23-SORT protein import and lateral insertion into inner membrane
- Mitochondrial beta barrel outer membrane protein insertion (TOM-SAM pathway)
- TOM-TIM22 inner membrane protein import (carrier pathway)

### Modifications proposed
- Rename GO:0030150 → clarify as "protein import into mitochondrial matrix" via TOM-TIM23-PAM
- Rename GO:0160203 → "protein import into intermembrane space via disulfide relay system"

### Terms proposed for obsoletion
- GO:0070585, GO:0072656, GO:1903637 and others — unnecessary groupings that can be annotated to more specific pathways

## Genes to Review

The project should review key components of each import pathway. Priority genes TBD based on which organisms/complexes are being modelled.

### Key complexes and representative subunits
- **TOM complex**: TOMM40, TOMM20, TOMM22, TOMM70, TOMM5, TOMM6, TOMM7
- **TIM23 complex**: TIMM23, TIMM17A/B, TIMM50, TIMM21
- **PAM complex**: HSPA9 (mortalin/mtHsp70), TIMM44, GRPEL1/2, PAM16/TIMM16, PAM18/TIMM14
- **TIM22 complex**: TIMM22, TIMM29, TIMM10, AGK
- **SAM/TOB complex**: SAMM50, metaxin-1/2/3
- **MIA/CHCHD4 pathway**: CHCHD4 (Mia40), ALR/GFER (Erv1)
- **MIM complex**: MIM1, MIM2 (yeast); MTCH2 (metazoan equivalent)
- **Processing**: PMPCB, PMPCA (MPP), XPNPEP3 (Icp55), MIP/MIPEP (Oct1)
- **Folding**: HSPD1 (Hsp60), HSPE1 (Hsp10)

## Priority Genes (fetched)

### Tier 1 — Core channel/pathway subunits
| Gene | Complex/Pathway | Annotations |
|------|----------------|-------------|
| TOMM40 | TOM complex central channel | 30 |
| TIMM23 | TIM23 complex channel | 29 |
| TIMM22 | TIM22 complex channel | 27 |
| SAMM50 | SAM complex channel | 31 |
| CHCHD4 | MIA40/disulfide relay | 31 |
| GFER | Erv1/ALR, disulfide relay partner | 26 |
| MTCH2 | Metazoan MIM equivalent | 22 |

### Tier 2 — Receptors, regulators, and accessory subunits
| Gene | Complex/Pathway | Annotations |
|------|----------------|-------------|
| TOMM20 | TOM receptor (presequence) | pre-existing |
| TOMM22 | TOM receptor (cis-binding) | 27 |
| TOMM70 | TOM receptor (carrier proteins) | 60 |
| TOMM5 | Small TOM subunit | 11 |
| TOMM6 | Small TOM subunit | 10 |
| TOMM7 | Small TOM subunit (quality control) | 20 |
| TIMM50 | TIM23 receptor | 32 |
| TIMM44 | PAM complex (tethers mtHsp70) | 24 |
| TIMM17A | TIM23 core channel | 17 |
| TIMM21 | TIM23-SORT pathway | 23 |
| PAM16 | PAM complex (J-protein regulator) | 27 |
| MTX1 | Metaxin-1, SAM complex partner | 16 |
| MTX2 | Metaxin-2, SAM complex partner | 20 |
| HSPA9 | Mortalin/mtHsp70 (PAM motor) | pre-existing |

### Tier 3 — Processing enzymes
| Gene | Function | Annotations |
|------|----------|-------------|
| PMPCA | MPP alpha subunit | 24 |
| PMPCB | MPP beta subunit (catalytic) | 21 |

## Status

- [x] Read and understand issue #31711
- [x] Identify priority genes for review
- [x] Fetch gene data for all priority genes
- [x] Deep research on pathway components and nomenclature
- [ ] Begin gene reviews
  - [x] TOMM40 — TOM complex central channel (30 annotations reviewed)
  - [x] CHCHD4 — MIA40/disulfide relay (31 annotations reviewed)
  - [x] MTCH2 — metazoan MIM insertase (22 annotations reviewed)
  - [ ] Remaining genes (TIMM23, TIMM22, SAMM50, GFER, TOMM22, TOMM70, etc.)
- [ ] Propose GO term hierarchy
