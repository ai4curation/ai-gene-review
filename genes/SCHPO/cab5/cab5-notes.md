# cab5 (SPCC14G10.01, UniProt O74414) notes

Fetch: `just fetch-gene SCHPO cab5` failed (UniProt entry "Uncharacterized protein C14G10.01"). Fetched with `-u O74414`; confirmed YJL1_SCHPO / O74414 (236 aa).

## Evidence
- [UniProt:O74414 "SIMILARITY: Belongs to the CoaE family. {ECO:0000305}."], DPCK domain 3-208, ATP P-loop 8-15 (by similarity).
- Cytoplasmic in GFP library screen [PMID:10759889] and ORFeome YFP screen [PMID:16823372].
- S. cerevisiae CAB5 is DPCK, complemented by E. coli coaE [PMID:19266201 "Null mutants could be complemented by their bacterial counterparts coaBC, coaD and coaE, respectively."]; budding-yeast Cab5 is an extrinsic outer mitochondrial membrane protein (see genes/yeast/CAB5).

## Decisions
- Core MF GO:0004140, BP GO:0015937; locations GO:0031315 (ISO from SGD CAB5, as in PomBase GO-CAM) and GO:0005737 (S. pombe HTP data).
- ATP binding non-core. Consistent with genes/yeast/CAB5.
- No S. pombe biochemical or fractionation data; mitochondrial outer membrane association is by orthology only.
