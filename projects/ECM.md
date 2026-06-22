---
title: "Extracellular Matrix (ECM) Project"
maturity: SCOPING
tags: [BIOLOGY_DOMAIN, FLAGSHIP]
species: [human]
---

# Extracellular Matrix (ECM) Project

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

## Relationship to the Matrisome project (evaluation: low yield)

We evaluated whether the [Matrisome project](https://sites.google.com/uic.edu/matrisome) /
[MatrisomeDB](https://matrisomedb.org) (Naba/Hynes) is a useful source of GO annotations for ECM gene
review. **Conclusion: it adds little**, recorded here so we don't re-investigate it.

- **It is a membership lookup list, not a GO source.** The matrisome assigns each gene to one of six
  families (core: Collagens, ECM Glycoproteins, Proteoglycans; associated: ECM-affiliated Proteins,
  ECM Regulators, Secreted Factors). MatrisomeDB reprocesses public ECM proteomics; it does **not**
  deposit GO annotations. The `GO:0031012` HDA annotations in GOA are made independently by GO
  curators (GO_Central, BHF-UCL) citing the underlying proteomics papers.
- **No molecular function, and it collapses to one generic CC term.** The families are
  localization/membership labels — "Secreted Factor" is at most `GO:0005576 extracellular region` (a
  cellular component, not a function). As an annotation generator the whole resource yields at most
  `GO:0031012 extracellular matrix` (a location), shared by all three core families.
- **GOA already has it.** Cross-checking the matrisome masterlist against our reviewed genes: of 24
  mappable core-matrisome genes, **19 already carry GO:0031012**, 1 was subsumed by a more specific
  term, and only **4** lacked it (GAS6, IGFBP3, NTN3, mouse Gas6) — and those are the borderline "is
  this really ECM-localized?" cases, not confident additions.
- **The one modest nugget**: the **core vs matrisome-associated** split is a useful *soft prior on the
  core/non-core decision* for ECM-localization annotations we already review — not a generator of new
  ones. E.g. SERPINH1/HSP47 carries `GO:0031012` HDA annotations but the matrisome classes it as
  *associated / ECM Regulator*, consistent with our `KEEP_AS_NON_CORE` call (peripheral
  co-purification, not true ECM residence).
- **Side finding**: `GO:0062023` "collagen-containing extracellular matrix" is **obsolete**
  (`replaced_by GO:0031012`; go-ontology#29475, *"not clearly defined and usage has been
  inconsistent"*), so the earlier GO push to reannotate metazoan ECM annotations to GO:0062023 has
  been reversed — `GO:0031012` is the current term.

(The throwaway family→GO mapping and gap-finder script used for this check are not retained; see git
history if needed.)


