# DAB2 (Disabled homolog 2) review notes

UniProt: **P98082** → **DAB2**. Taxon: 9606. Clathrin-associated sorting protein (CLASP) / cargo-specific endocytic adaptor.

## Core function (standalone summary)

DAB2 is a **clathrin-cargo adaptor / autonomous cargo-selective endocytic adaptor**. Its
PTB domain binds NPxY sorting motifs in the cytosolic tails of cell-surface receptors
(LDL receptor family, megalin) and, simultaneously binding clathrin and PtdIns(4,5)P2, it
sorts those receptors into clathrin-coated pits independently of the AP-2 complex. It also
links cargo to the actin motor **myosin VI (MYO6)** for post-endocytic transport and acts
as a **SMAD2/3 adaptor** in TGF-beta signalling.

## Key evidence (provenance)

- [PMID:16984970 abstract]: "The adaptor protein Dab2 sorts LDL receptors into coated pits
  independently of" AP-2 — basis for GO:0035615 clathrin-cargo adaptor activity (core).
- [PMID:11387212]: Dab2 interacts with SMAD2/SMAD3 and TGF-beta receptor; basis for
  GO:0046332 SMAD binding (SMAD2 P84022, SMAD3 P84022/Q15796 rows).
- [PMID:11967127]: Dab2 links to myosin VI (MYO6, Q9UM54) — basis for GO:0017022 myosin binding.
- UniProt P98082: CLASP that can bind and assemble clathrin and recognises non-phosphorylated
  NPxY motifs; AP-2-independent cargo sorting.

## Annotation landscape (GOA, 89 rows)

- Core MF: GO:0035615 clathrin-cargo adaptor activity; GO:0038024 cargo receptor activity.
- Informative binding partners (MODIFY from bare protein binding): SMAD2/3 -> GO:0046332 SMAD
  binding; MYO6 -> GO:0017022 myosin binding.
- Other bare protein-binding IPI rows -> REMOVE per policy; cytoplasm (general) -> TOO_GENERAL.
