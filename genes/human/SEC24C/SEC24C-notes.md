# SEC24C review notes

UniProt: **P53992** → **SEC24C**. Taxon: 9606. Cargo-selection subunit of COPII.

## Core function (standalone summary)

SEC24C is the **cargo-selection subunit of coat protein complex II (COPII)**, which forms
transport vesicles at ER exit sites for anterograde ER-to-Golgi traffic. In the inner coat it
pairs with a SEC23 subunit and, with SAR1-GTP and the Sec13/31 outer cage, deforms the ER
membrane and concentrates cargo. SEC24C recognises specific sorting signals: IxM motifs in the
SNAREs GOSR2 and STX5, ER-exit motifs in STING1, and GPI-anchored proteins via TMED10. Its cargo
repertoire overlaps SEC24D and differs from SEC24A/B. A structural zinc finger is part of the fold.

## Key evidence (provenance)

- [PMID:18843296 abstract]: structural basis of cargo discrimination; the human genome encodes
  "four forms of Sec24, the cargo selection subunit of the COPII vesicular coat" — basis for
  GO:0140312 cargo adaptor activity (core), GO:0000149 SNARE binding (GOSR2/STX5 via IxM).
- [PMID:20427317]: selective export of GPI-anchored proteins via TMED10 (ER-to-Golgi transport).
- [PMID:41887218]: STING ER-exit motif recognition; cargo adaptor IDA.
- [PMID:10075675, PMID:10329445]: ER membrane / COPII vesicle coat localisation (EXP).

## Annotation landscape (GOA, 87 rows)

- Core MF: GO:0140312 cargo adaptor activity; companion GO:0000149 SNARE binding. part_of
  GO:0030127 COPII vesicle coat. Core processes: GO:0090110 COPII cargo loading, GO:0006888
  ER-to-Golgi transport. Core locations: ER membrane, ER exit site, COPII vesicle membrane, cytosol.
- 15 bare protein-binding IPI -> REMOVE per policy. GO:0008270 zinc ion binding -> KEEP_AS_NON_CORE
  (structural). General protein transport / regulation rows -> KEEP_AS_NON_CORE.
