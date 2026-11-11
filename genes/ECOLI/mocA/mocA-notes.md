# mocA (Q46810) notes, E. coli K-12

Deep research providers were unavailable for this session (no API keys), so no
`-deep-research-<provider>.md` file exists. The review is built from the UniProt record
and the cached publications (abstract-only; PMC full text exists for both papers).

## Identity

- UniProt Q46810, molybdenum cofactor cytidylyltransferase, EC 2.7.7.76; synonym ygfJ;
  b2877. PANTHER PTHR43777; NCBIfam TIGR03310 (matur_MocA_YgfJ).

## Evidence

- Defined in vitro MCD synthesis [PMID:19542235 "MocA, Mo-MPT, CTP, and MgCl2 are required and sufficient for MCD biosynthesis in vitro"];
  CTP-specific [PMID:19542235 "The activity of MocA is specific for CTP; other nucleotides such as ATP and GTP were not utilized."].
- Essential for PaoABC (YagTSR), XdhABC and XdhD activity (PMID:19542235).
- Domain swaps with MobA: N-terminal domain sets nucleotide specificity, C-terminal domain the
  acceptor protein (PaoD) [PMID:21081498 "the C-terminal domain of either MocA or MobA determines the specific binding to the respective acceptor protein"].

## Curation decisions

- GO:0006777 IMP MODIFY to GO:1902760 (the phenotype is loss of MCD); GO:0016740 ARBA MODIFY
  to GO:0061602.
- Bare protein binding with PaoD removed per policy.
- Mg ion binding kept as non-core (cofactor), matching MobA.
