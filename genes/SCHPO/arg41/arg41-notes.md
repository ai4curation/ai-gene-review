# arg41 (SPBC1539.03c, UniProt P50514) notes

## Identity
- UniProt gene name is "argx" (ARLZ_SCHPO); PomBase name arg41. Fetched with `-u P50514`.
- [UniProt:P50514 "RecName: Full=Probable argininosuccinate lyase;"]; ortholog of S. cerevisiae ARG4. Paralog arg7 (SPBC1773.14).

## Evidence
- [PMID:32896087 "arg7 is one of two argininosuccinate lyases (with deletion of the other one, arg41, showing arginine auxotrophy)"] -> arg41 is the paralog needed for prototrophy.
- Cytosol (ORFeome HDA).
- PomBase GO-CAM: both arg7 (IMP PMID:1868575) and arg41 (IBA only) enable GO:0004056 in cytosol.

## Decisions
- urea cycle IC/IEA MARK_AS_OVER_ANNOTATED; catalytic activity MODIFY -> GO:0004056.
- Core = ARG4 core: GO:0004056, GO:0006526, cytosol.
