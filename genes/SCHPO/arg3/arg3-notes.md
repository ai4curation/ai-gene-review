# arg3 (SPAC4G9.10, UniProt P31317) notes

## Key S. pombe-specific difference
- OTC is mitochondrial in S. pombe (cytosolic in S. cerevisiae): [PMID:1313366 "in contrast to the S. pombe enzyme, more than 95% of the S. cerevisiae enzyme remains in the S. pombe cytoplasm"]; Arg3-GFP mitochondrial [PMID:32896087 "fusion localises to mitochondria"]. So pombe exports citrulline (GO-CAM comment; transporter SPBC365.16).

## Evidence
- Deletion auxotrophy [PMID:32896087 "Strain with arg3 gene deletion"]; library strain was mis-annotated.
- Trx2 dependence (Song et al. 2008, abstract only): [PMID:18849471 "arg3(+) transcript, Arg3 protein, and OCTase activity were all decreased in"]; [PMID:18849471 "we observed a direct interaction between Trx2 and Arg3 in cell extracts"]. No protein-binding GO row present; not proposed.

## Decisions
- Core differs from S. cerevisiae ARG3 in location only (mitochondrial matrix, not cytosol); BPs GO:0006526 + GO:0019240.
- HDA cytoplasm UNDECIDED (conflicts with fractionation/GFP; image not assessable). ARBA cytoplasm MODIFY -> matrix.
- urea cycle IC MARK_AS_OVER_ANNOTATED (consistent across arg3/arg12/arg41 and cerevisiae ARG1).
