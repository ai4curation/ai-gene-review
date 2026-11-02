# ade1 (SPBC405.01, UniProt P20772) notes

Fetch: correct accession fetched (PUR2_SCHPO, P20772). Naming trap: S. pombe ade1 is the ortholog of S. cerevisiae ADE5,7 (genes/yeast/ADE57), NOT of S. cerevisiae ADE1 (SAICAR synthetase).

## Evidence
- [PMID:967158 "ade1A mutants lack GAR synthetase and ade1B mutants lack AIR synthetase"]; [PMID:967158 "In wild type strains the two activities fractionate together throughout a hundred-fold purification"]; multimer of 4-6 x 40 kDa subunits; AIRS only in the multimer.
- [PMID:3502942 "encodes a bifunctional polypeptide with glycinamide ribotide synthetase (GARSase) and aminoimidazole ribotide synthetase (AIRSase) enzyme activities"]; ~60% identity to S. cerevisiae ade5,7.
- Cytosol (ORFeome, PMID:16823372).

## Decisions
- Two core functions (GO:0004637, GO:0004641), BP GO:0006189, cytosol - identical to genes/yeast/ADE57.
- Nucleobase/adenine BP rows MODIFIED to GO:0006189; ARBA high-level terms marked over-annotated.
- ATP binding and metal ion binding kept non-core (yeast ADE57 review used ACCEPT for both; same biological judgment, different bookkeeping).
