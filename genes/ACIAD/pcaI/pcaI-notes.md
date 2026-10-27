# pcaI (Acinetobacter baylyi ADP1, Q43973) notes

## Provenance

- Deep research: `just deep-research ACIAD pcaI --provider falcon` was attempted
  on 2026-10-23 and failed with "Failed to authenticate"; no provider report
  exists. This review was written from the Swiss-Prot record and cached
  publications.
- Added as the non-Pseudomonas exemplar of the PcaI subunit in
  `modules/beta_ketoadipate_lower_pathway.yaml`.

## Evidence

- The A. calcoaceticus (ADP1 lineage) transferase was purified to homogeneity
  and is an alpha2beta2 heteromer [PMID:6780551 "each transferase appears to
  have an alpha 2 beta 2 oligomeric structure formed by association of
  nonidentical subunits"]. The enables GO:0047569 row is therefore reviewed as
  MODIFY to contributes_to, as for PSEPK pcaI/pcaJ.
- pcaI heads the pcaIJFBDKCHG operon [PMID:8063101 "all of the pca structural
  genes are tightly grouped in the order pcaIJFBDKCHG within a single operon"].
- catI (ACIAD1448) encodes a near-identical, isofunctional protein that UniProt
  merges into the same entry [file:ACIAD/pcaI/pcaI-uniprot.txt "Name=catI;
  OrderedLocusNames=ACIAD1448;"]; the catIJF and pcaIJF regions exchange
  sequence [PMID:8125318 "the catIJF region, known to exchange genetic information
  with the pcaIJF region"].
