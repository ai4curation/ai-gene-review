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

## Status

- [x] Read and understand issue #31711
- [ ] Deep research on pathway components and nomenclature
- [ ] Identify priority genes for review
- [ ] Begin gene reviews
- [ ] Propose GO term hierarchy
