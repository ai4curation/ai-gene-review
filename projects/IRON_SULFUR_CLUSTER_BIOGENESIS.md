---
title: "Iron-Sulfur Cluster Biogenesis Project"
maturity: IN_PROGRESS
last_reviewed: "2026-10-04"
tags: [BIOLOGY_DOMAIN, FLAGSHIP]
species: [human]
genes: [NFS1, ISCU, FXN, LYRM4, HSPA9, HSCB, GLRX5, ISCA1, ISCA2, IBA57, NFU1, BOLA3, ABCB7, CIAO1, MMS19]
manifest:
  slides:
    - href: IRON_SULFUR_CLUSTER_BIOGENESIS/slides/IRON_SULFUR_CLUSTER_BIOGENESIS-slides.html
      description: AI generated
  artifacts:
    - href: https://claude.ai/artifact/5tZjqRb2tFMCKoamGFVLKA
      title: Project brief
---

# Iron-Sulfur Cluster Biogenesis Project

**Bottom line:** iron-sulfur clusters are built in the mitochondrion by the
ISC machinery (the NFS1-LYRM4-ISCU-FXN core, the HSPA9/HSCB/GLRX5 transfer
chaperones, and late [4Fe-4S] factors), exported via ABCB7, and delivered to
cytosolic and nuclear proteins by the CIA system. All 15 genes in the candidate
table below now have complete reviews. Together they assess 637 review rows:
367 ACCEPT, 93 KEEP_AS_NON_CORE, 90 MARK_AS_OVER_ANNOTATED, 38 MODIFY, 24
REMOVE, 18 NEW and 7
UNDECIDED. The recurring corrections are generic `protein binding` rows
removed on HSCB and GLRX5, heme-transport rows removed from ABCB7, and NEW
Fe-S-specific terms such as `iron-sulfur cluster chaperone activity`
(GO:0140132) for GLRX5 and ISCA1 and `[4Fe-4S] cluster assembly` (GO:0044572)
for ISCA1 and IBA57. FDXR, FDX2, CIAO2A, CIAO2B and CIAO3 are not yet reviewed,
and no integrated human Fe-S biogenesis module has been built.

## Overview

Iron-sulfur (Fe-S) clusters are ancient and essential cofactors required for numerous cellular processes including electron transfer, enzyme catalysis, and gene regulation. The mitochondrial ISC assembly machinery is the primary system in eukaryotes, with cytosolic Fe-S assembly dependent on mitochondrial function.

## Model Species

**Primary: Homo sapiens (human)**
- Current reviews cover 15 ISC, cluster-transfer, export, and CIA genes
- Multiple rare diseases (Friedreich's ataxia, etc.)

## Core Pathway Architecture

### 1. Mitochondrial ISC Assembly
Core machinery for de novo cluster synthesis:
- **NFS1** - Cysteine desulfurase (sulfur donor)
- **ISCU** - Scaffold protein
- **FXN** - Frataxin (iron donor/regulator)
- **LYRM4** (ISD11) - NFS1 stabilizer
- **FDXR/FDX2** - Ferredoxin reductase/ferredoxin

### 2. Cluster Transfer (Chaperone System)
Transfer from scaffold to recipients:
- **HSPA9** - Mitochondrial Hsp70
- **HSCB** - J-domain co-chaperone
- **GLRX5** - Glutaredoxin 5

### 3. [4Fe-4S] Cluster Assembly
Late-acting ISC machinery:
- **ISCA1/ISCA2** - A-type carriers
- **IBA57** - [4Fe-4S] assembly factor
- **NFU1** - Alternative scaffold
- **BOLA3** - [4Fe-4S] maturation

### 4. Mitochondrial Export
- **ABCB7** - ABC transporter (exports unknown sulfur compound)

### 5. Cytosolic Iron-Sulfur Assembly (CIA)
Cytosolic/nuclear Fe-S protein maturation:
- **CIAO1** - CIA targeting complex
- **CIAO2A/2B** - CIA factors
- **CIAO3** (NARFL) - CIA component
- **MMS19** - Late-acting factor

## Candidate Genes (15)

| Gene | UniProt | Function |
|------|---------|----------|
| NFS1 | Q9Y697 | Cysteine desulfurase |
| ISCU | Q9H1K1 | Scaffold |
| FXN | Q16595 | Frataxin |
| LYRM4 | Q9HD34 | NFS1 partner |
| HSPA9 | P38646 | Hsp70 chaperone |
| HSCB | Q8IWL3 | Co-chaperone |
| GLRX5 | Q86SX6 | Glutaredoxin |
| ISCA1 | Q9BUE6 | [4Fe-4S] assembly |
| ISCA2 | Q86U28 | [4Fe-4S] assembly |
| IBA57 | Q5T440 | [4Fe-4S] factor |
| NFU1 | Q9UMS0 | Alternative scaffold |
| BOLA3 | Q53S33 | [4Fe-4S] factor |
| ABCB7 | O75027 | Mitochondrial export |
| CIAO1 | O76071 | CIA complex |
| MMS19 | Q96T76 | CIA factor |

## Disease Relevance

- Friedreich's ataxia (FXN)
- Sideroblastic anemia (GLRX5, ABCB7)
- Multiple mitochondrial dysfunctions (NFU1, BOLA3, IBA57)
- HSCB-related disease (not yet characterized)

## Project Status

- [x] 15/15 candidate-table genes reviewed
- [ ] Review FDXR, FDX2, CIAO2A, CIAO2B, CIAO3
- [ ] Build an integrated human ISC/CIA Fe-S biogenesis module
