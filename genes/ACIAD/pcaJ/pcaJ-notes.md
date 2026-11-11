# pcaJ (Acinetobacter baylyi ADP1, Q59091) notes

## Provenance

- Deep research: `just deep-research ACIAD pcaJ --provider falcon` was attempted
  on 2026-10-23 and failed with "Failed to authenticate"; no provider report
  exists. This review was written from the Swiss-Prot record and cached
  publications.
- Added as the non-Pseudomonas exemplar of the PcaJ subunit in
  `modules/beta_ketoadipate_lower_pathway.yaml`.

## Evidence

- PcaJ is subunit B of the alpha2beta2 transferase purified from
  A. calcoaceticus [PMID:6780551 "each transferase appears to have an alpha 2
  beta 2 oligomeric structure formed by association of nonidentical
  subunits"]; GO:0047569 is therefore contributes_to.
- catJ (ACIAD1449) encodes a near-identical, isofunctional protein that UniProt
  merges into the same entry [file:ACIAD/pcaJ/pcaJ-uniprot.txt "Name=catJ;
  OrderedLocusNames=ACIAD1449;"; PMID:8125318].
