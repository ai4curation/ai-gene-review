# ASPFU exgA notes

## 2026-10-24

- `exgA` / `AFUA_1G03600` encodes A. fumigatus Af293 Q4WK60, a reviewed
  Swiss-Prot "Probable glucan 1,3-beta-glucosidase A" with EC 3.2.1.58,
  a predicted N-terminal signal peptide, inferred secretion, and PANTHER
  `PTHR31297:SF1` placement.
- The cached A. fumigatus review of beta-1,3-glucan modifying enzymes lists
  `AFUA_1G03600` as `EXG1`, a 416-aa GH5 candidate exo-beta-1,3-glucanase with
  a signal peptide, and notes the then-current limitation that none of the
  A. fumigatus `EXG1`-`EXG4` genes had been deleted or otherwise characterized
  [PMID:23616783, "AfExg1p and AfExg4p have a signal peptide in contrast to the others AfExg2p and AfExg3p."].
- Direct A. fumigatus Af293 `exgA` biochemical papers were not found in the
  cached references or in a targeted web search for `Q4WK60`, `AFUA_1G03600`,
  `Afu1g03600`, and `exgA Aspergillus fumigatus glucan beta-glucosidase`.
  The exact EC 3.2.1.58 call therefore rests on homology, especially to
  Candida albicans XOG1/Exg, whose disruption removes the major C. albicans
  exoglucanase activity [PMID:9308184, "gene is responsible for the major exoglucanase activity in C. albicans"] and whose purified enzyme has beta-1,3
  specificity [PMID:10469155, "The exo-beta-1,3-glucanase of Candida albicans (Exg) has a marked specificity"].
- PAINT `PTHR31297` has a broad extracellular/wall-glucan node
  `PTN001262686` and a glucan-catabolism node `PTN001262628`. Both are suitable
  for `exgA`: the target is a secreted PTHR31297:SF1 GH5 enzyme, and the
  propagated terms are broad enough to cover extracellular exo-glucanase
  action.
- The EnsemblFungi rows that come from PomBase `SPBC1105.05` need splitting by
  granularity. Generic extracellular region and fungal-type cell-wall
  beta-glucan metabolism remain biologically plausible, but
  `glucan endo-1,6-beta-glucosidase activity`, `division septum`,
  `mating projection tip cell wall disassembly`, and
  `mating projection actin fusion focus` are fission-yeast-specific imports.
  The full-text S. pombe paper explicitly contrasts S. pombe Exg1 with
  ScExg1/CaXog1: fission Exg1 and Exg3 are beta-1,6-specific and cannot
  degrade beta-1,3 glucans [PMID:20852022, "In contrast to ScExg1 and CaXog1, the S. pombe Exg1 and Exg3 were highly specific for β(1,6)-glucans"].
  The mating-projection localization comes from a separate fission-yeast actin
  fusion focus study [PMID:25825517, "Type V myosins are essential for fusion and concentrate cell wall hydrolases"].
