# pgoX / hemY (P56601, Myxococcus xanthus) curation notes

## Folder and naming

- UniProt gene name is pgoX (synonym hemY), so the folder is genes/MYXXA/pgoX; hemY is an alias.

## Sources and deep research

- Deep research was unavailable (the `just deep-research` perplexity route failed in this
  environment). The review rests on UniProt P56601, PMID:8621504 (abstract) and PMID:17046834
  (full text), and the PANTHER PTHR42923 PAINT file (no IBA rows reach this protein in GOA).

## Evidence

- Enzymology [PMID:8621504 "The M. xanthus enzyme utilizes protoporphyrinogen IX, but not
  coproporphyrinogen III, as substrate and produces 3 mol of H2O2/mol of protoporphyrin."]; FAD
  [PMID:8621504 "The purified protein contains a non-covalently bound FAD but no detectable redox
  active metal."].
- Membrane association [PMID:17046834 "mxPPOX is a membrane-associated enzyme that requires the
  presence of detergent for solubilization and purification."]; contrast with the cytoplasmic B.
  subtilis HemY [PMID:17046834 "This is in contrast to the PPOX from Bacillus subtilis, which is
  monomeric, cytoplasmic"].

## Decisions

- GO:0004729 (oxygen as acceptor; "3 O2 + protoporphyrinogen IX = 3 H2O2 + protoporphyrin IX"):
  ACCEPT; matches the measured H2O2 stoichiometry (contrast E. coli HemG, quinone acceptor GO:0070819).
- Cytoplasm (EXP PMID:17046834 and SubCell IEA): MARK_AS_OVER_ANNOTATED, source defect recorded
  against the UniProt Cytoplasm statement.
- Plasma membrane rows: ACCEPT; membrane face not shown, so not refined to GO:0009898.
- Oxidoreductase activity IEA: MODIFY to GO:0004729. Porphyrin biosynthesis IEA: MODIFY to GO:0006785.
- NEW GO:0071949 FAD binding (IDA PMID:8621504).
