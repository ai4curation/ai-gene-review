# Scgb3a2 (mouse UGRP1 / PnSP-1, Q920H1) — review notes

Lung-enriched secretoglobin; most UGRP1 biology was done in mouse (Kimura/Niimi lab).

## Identity
- UniProt SG3A2_MOUSE Q920H1; Synonyms Pnsp1, Ugrp1. NKX2-1 (T/EBP) target in lung.
  [PMID:11682631 abstract: "The gene product is a secreted protein, forms a homodimer ... designated Ugrp1
  (uteroglobin-related protein 1)"].
- Disulfide-linked homodimer via Cys68; C68S fails to dimerize (UniProt MUTAGEN; PMID:24213919).

## Function (mouse experimental)
- Phospholipase A2 inhibitor (direct biochemistry, mouse protein):
  [PMID:24213919 "Human SCGB3A2, as well as mouse SCGB3A2, readily formed a dimer in solution and exhibited
  novel phospholipase A2 inhibitory activity"]. UniProt CC:FUNCTION "Strongly inhibits phospholipase A2
  (PLA2G1B) activity". → NEW GO:0019834.
- Anti-inflammatory (gain + loss of function):
  [PMID:16456148 overexpression "markedly reduced the number of infiltrating inflammatory cells, particularly
  eosinophils ... IL-4, IL-5, and IL-13"]; [PMID:25242865 KO "suggest that SCGB3A2 has anti-inflammatory
  property"]; [PMID:26559674 KO -> more severe bleomycin inflammation/fibrosis]. → NEW GO:0050728.
- Lung growth factor:
  [PMID:18535256 "SCGB3A2 is a novel growth factor in lung"]; [PMID:24213919 "human SCGB3A2 exhibited growth
  factor activity by promoting embryonic lung development in both ex vivo and in vivo systems"]. → NEW GO:0008083
  (growth factor activity MF; lung development kept in prose only, not asserted as BP, to avoid developmental
  over-annotation).

## GOA review decisions
- GO:0005515 protein binding (IPI, self PR:Q920H1 = homodimerization) — REMOVE (bare protein-binding policy).
- GO:0005576 extracellular region (IBA, IDA, IEA, ISO) — ACCEPT all (secreted; direct in PMID:11682631).
- GO:0008150 biological_process (ND, 2001) — REMOVE (superseded by experimental BP data above).
