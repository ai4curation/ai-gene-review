# Scgb3a1 (mouse UGRP2 / HIN-1 / PnSP-2, Q920D7) — review notes

Paralog of Scgb3a2; secreted cytokine-like secretoglobin. Molecular activity still uncharacterized.

## Identity
- UniProt SG3A1_MOUSE Q920D7; AltNames Cytokine HIN-1 / High in normal 1; Ugrp2; PnSP-2.
- Marks a secretory-cell subset in airway distinct from Scgb3a2/club cells [PMID:12406855].
- UniProt CC:FUNCTION (By similarity to human Q96QR1): "Secreted cytokine-like protein. Inhibits cell growth
  in vitro." Human HIN-1/SCGB3A1 is a growth-suppressive, hypermethylation-silenced gene in epithelial cancers
  [PMID:11481438].

## GOA review decisions
- GO:0003674 molecular_function (ND) — ACCEPT (no specific MF defined; growth-suppressive role is by-similarity
  only, no receptor/mechanism; ND remains honest).
- GO:0005576 extracellular region (IBA, IEA, ISO, ISS) — ACCEPT all (secreted secretoglobin; UniProt Secreted).
- GO:1901741 positive regulation of myoblast fusion (IBA + IMP PMID:23844157) — KEEP_AS_NON_CORE for both.
  The IMP is a single C2C12 RNAi screen of 134 cytokines [PMID:23844157 "Our results have uncovered 29 cytokines
  as strong candidates for novel myogenic regulators"]; the IBA is seeded by Scgb3a1's own IMP (MGI:1915912 in the
  WITH list), so both are consistent and kept, but peripheral to the core airway/uterine secretory function.
