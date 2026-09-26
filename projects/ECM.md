---
title: "Extracellular Matrix (ECM) Project"
maturity: IN_PROGRESS
tags: [BIOLOGY_DOMAIN, FLAGSHIP]
species: [human]
genes: [AGRN, HSPG2, EPYC, SPOCK1, SPOCK2, SPOCK3, NID1, FN1, DCN, SPARC]
---

# Extracellular Matrix (ECM) Project

**Bottom line:** the extracellular matrix is the protein and proteoglycan
network that holds tissues together and signals to the cells within it. We
reviewed ten human ECM genes in three phases: the basement-membrane
proteoglycans AGRN and HSPG2 plus EPYC, the testican family SPOCK1-3, and a
diverse set (NID1, FN1, DCN, SPARC). All ten reviews are complete, although
the task list below still shows Phase 3 as open and AGRN/HSPG2 as in progress.
They assess 639 GOA rows: 284 ACCEPT, 193 KEEP_AS_NON_CORE, 73 REMOVE, 63
MODIFY, 17 NEW, 7 MARK_AS_OVER_ANNOTATED and 2 UNDECIDED. FN1 accounts for most
of the corrections: 52 generic `protein binding` rows removed and 38
`extracellular region` rows modified to `extracellular matrix`. The SPOCK2
metalloendopeptidase-inhibitor rows were modified to reflect its role as a
counter-inhibitor of SPOCK1/3, and EPYC gained NEW collagen-binding and matrix
terms. DCN still has no `core_functions` block, and no ECM module exists.

## Overview

This project focuses on reviewing genes involved in the extracellular matrix (ECM), a complex network of proteins and polysaccharides that provides structural and biochemical support to surrounding cells.

## Tasks

### Phase 1: Core ECM Components

- [x] Review human AGRN (Agrin) - IN_PROGRESS
- [x] Review human HSPG2 (Perlecan) - IN_PROGRESS
- [x] Review human EPYC (Epiphycan) - COMPLETE

### Phase 2: SPARC/Osteonectin Family (Testican/SPOCK proteins)

- [x] Review human SPOCK1 (Testican-1) - IN_PROGRESS
- [x] Review human SPOCK2 (Testican-2) - IN_PROGRESS
- [x] Review human SPOCK3 (Testican-3) - IN_PROGRESS

### Phase 3: Diverse ECM Components

- [ ] Review human NID1 (Nidogen-1) - Basement membrane linker
- [ ] Review human FN1 (Fibronectin) - Major ECM glycoprotein
- [ ] Review human DCN (Decorin) - Small leucine-rich proteoglycan
- [ ] Review human SPARC (Osteonectin/SPARC) - Matricellular protein

## Status

Started: 2025-11-10
- Phase 1: AGRN and HSPG2 in progress, EPYC complete
- Phase 2 Added: 2025-11-11 - All three SPOCK genes reviewed and validated
- Phase 3 Added: 2025-11-11 - Expanding to diverse ECM protein classes

## Notes

**SPOCK proteins (Testican family):**
- Proteoglycans belonging to the SPARC/osteonectin family
- Modular structure with follistatin-like and extracellular calcium-binding domains
- Chondroitin/heparan sulfate chains
- **Key finding**: SPOCK2 uniquely acts as counter-inhibitor, blocking SPOCK1/3 MMP inhibition
- Roles in ECM assembly, neurogenesis, angiogenesis, and cancer

**Phase 3 rationale:**
- **NID1**: Bridges laminin to collagen IV networks in basement membranes
- **FN1**: Cell adhesion, migration, wound healing
- **DCN**: Collagen fibrillogenesis, TGF-β regulation
- **SPARC**: Parent family member, Ca²⁺ binding, collagen binding, anti-adhesive

