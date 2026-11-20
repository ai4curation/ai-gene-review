# catA (Acinetobacter baylyi ADP1, P07773) notes

## Provenance

- Deep research was attempted with `just deep-research ACIAD catA --provider falcon`
  (2026-10-23) and failed with "Failed to authenticate"; no other provider key is
  configured in this environment. This review is therefore built from the UniProt
  record and the cached primary literature only.
- Reviewed as an exemplar for `modules/catechol_ortho_cleavage.yaml` (non-Pseudomonas
  gammaproteobacterial CatA) and as the reference protein of the PTHR33711 family review.

## Evidence summary

- Structural gene for catechol 1,2-dioxygenase I [PMID:3170486 "catA, the structural
  gene for catechol 1,2-dioxygenase I, was determined"].
- Crystal structure of the ADP1 enzyme, alone and with catechol or 4-methylcatechol
  [PMID:10801478 "The crystal structure of 1,2-CTD from Acinetobacter sp. ADP1 (Ac
  1,2-CTD) was solved by single isomorphous replacement and refined to 2.0 A
  resolution."]; homodimer with one non-heme Fe(III) per subunit [PMID:10801478
  "a homodimer with one catalytic non-heme ferric ion per monomer"].
- Conserved His/Tyr Fe(III) ligands shared with protocatechuate 3,4-dioxygenase
  [PMID:3170486 "conserved histidyl and tyrosyl residues that are probably involved in
  the ligation of ferric ion in their active sites"].
- Regulation: CatM binds upstream of catA [PMID:7592340 "Gel mobility shift assays
  indicated that CatM also binds to a region upstream of catA."].
- Family: NCBIfam TIGR02439 (proteobacterial catechol 1,2-dioxygenase), PANTHER
  PTHR33711:SF7.

## Review decisions

- GO:0018576 and GO:0008199 accepted (IDA + IEA).
- Broad parents (GO:0003824, GO:0016702, GO:0005506) refined to the specific MF terms.
- Process rows GO:0009712, GO:0019614 (IDA and IEA) and GO:0042952 refined to
  GO:0019615 catechol catabolic process, ortho-cleavage, which is_a both GO:0019614 and
  GO:0042952 (checked with OAK against the local GO build).
