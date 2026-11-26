# PTSG_11235 (Salpingoeca rosetta, F2USU1) - curation notes

**Automated deep research was unavailable** (no deep-research provider key in this
environment), so no `-deep-research-*.md` file exists. These notes were written on
2026-10-02 from the cached publications, the UniProt record and the shared analysis in
`genes/MONBE/MBCDH12/MBCDH12-bioinformatics/`. This protein was reviewed together with
PTSG_05882, PTSG_06458 and MONBE MBCDH12.

## Identity and architecture

- F2USU1, TrEMBL, 8158 aa, ORF PTSG_11235, EMBL EGD81200.1. UniProt name
  "Protein-tyrosine-phosphatase", EC 3.1.3.48.
- Signal peptide 1-29. 56 cadherin repeats. FN3 7342-7450. TM 7478-7502. Cytoplasmic PTP
  7808-8088, with active-site C8029.
- PTP motifs
  [file:MONBE/MBCDH12/MBCDH12-bioinformatics/RESULTS.md "pTyr-recognition KNRY loop, a WPD loop and the catalytic VHCSAGVGRS signature"].
  These are the features of a classical, pTyr-specific PTP. That is why GO:0008138
  (dual-specificity) was modified to GO:0004725.
- The FN3-TM-PTP C-terminus matches the lefftyrin FTY cassette
  [PMID:22837400 "the carboxyl-terminal FTY cassette of lefftyrins is diagnostic of metazoan receptor PTPases"]
  [PMID:22837400 "lefftyrins may have evolved through a domain-shuffling event that brought PTPase and EC domains together in the choanoflagellate/metazoan stem lineage"].
  Pfam does not report the N-terminal Lam-N domain of the LEF cassette, so the lefftyrin
  assignment is likely but not verified. The cached Nichols et al. text does not give
  S. rosetta lefftyrin accessions, so I could not match this protein to them.
- 41 DXNDN-type and 37 LDRE-type calcium motifs, and 30 PROSITE CADHERIN_1 matches.
- No PF01049 (Cadherin_C).

## Track C

- The same 10 TreeGrafter rows from PTN000616280 (Bilateria) are present, with the same
  actions as the other S. rosetta cadherins.
- ARBA rows:
  - apicolateral plasma membrane: REMOVE (epithelial term; no epithelium);
  - positive regulation of hippo signaling: MARK_AS_OVER_ANNOTATED (rule features not
    inspected; FAT-like repeats but no FAT intracellular domain);
  - catalytic activity: KEEP_AS_NON_CORE.
- UniRule: GO:0008138 MODIFY to GO:0004725. Hydrolase: KEEP_AS_NON_CORE.
- PTP activity (combined IEA): ACCEPT, as the core MF.
