# BRUMA mf1 notes

## 2026-11-22 cross-check

- `genes/BRUMA/mf1/mf1-goa.tsv` has seven rows for UniProtKB P29030:
  chitinase and endochitinase molecular-function rows, a broad O-glycosyl
  hydrolase parent, chitin binding, extracellular region, chitin catabolism, and
  a broad carbohydrate metabolic-process parent.
- UniProtKB identifies P29030 as reviewed B. malayi MF1 antigen/endochitinase,
  with a residues 1-22 signal peptide, mature chain 23-504, a GH18 catalytic
  domain, a C-terminal type-2 chitin-binding domain, EC 3.2.1.14 catalytic
  activity, and predicted chitin-binding residues.
- PMID:1542646 is cached as an abstract only, but directly supports the core
  enzyme function: the MF1 cDNA encodes a chitinase-like protein, and
  chitin-degrading activity from microfilarial extracts and purified MF1
  antigen comigrated with the p70/p75 MF1 antigen.
- PMID:18611418 was added for this review because the initialized description
  and extracellular-region row referred to inner-body storage, secretion during
  transmission, and exsheathment; those are not in the PMID:1542646 abstract.
  Wu et al. used immuno-electron microscopy to place B. malayi MF1/chitinase in
  the microfilarial inner body and pharyngeal thread, showed inner-body
  chitinase only in sheathed microfilarial species, and found that the chitinase
  inhibitor allosamidin reduced in vitro exsheathment.
- `interpro/panther/PTHR11177/PTHR11177-entries.csv` places BRUMA P29030 and
  worm Q11174/cht-1 in the same reviewed PTHR11177:SF400 subfamily. `just
  paint-losses BRUMA mf1` reported no IRD or IKR loss on this gene's lineage,
  with the caveat that P29030 is not a leaf of the local PTHR11177 PAINT tree.
- The local nematode project does not yet have a GH18 chitinase ModuleReview.
  The current module cross-check is therefore to treat MF1 as the parasite
  anchor for a future same-mechanism GH18/chitin-catabolism review with worm
  `cht-1`, not as part of a joint CPI-2/MF1 immune-modulation module.
- This cross-check did not run a remote deep-research provider and did not
  refresh any existing cached publication. It used the existing initialized
  BRUMA review, the local UniProt and GOA snapshots, the cached PMID:1542646
  abstract, the newly added PMID:18611418 full-text cache, and the local
  PTHR11177 member and PAINT tables.
