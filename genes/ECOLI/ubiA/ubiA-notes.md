# ubiA (P0AGK1, E. coli K-12) review notes

## Sources
- No deep-research provider output (provider API keys unavailable); built from UniProt, cached abstracts
  (PMID:4552989, PMID:8155731, PMID:15919996) and the PTHR11048 PAINT file and family review.

## Findings
- ubiA mutants lack the activity [PMID:4552989 "The ubiA(-) mutants were found to lack 4-hydroxybenozate
  octaprenyltransferase activity"].
- Integral membrane enzyme [PMID:8155731 "The enzyme is membrane-bound and could not be solubilized by hypotonic
  buffer or detergent treatment."]

## Decisions
- All GO:0008412, GO:0006744 and plasma membrane rows ACCEPT (bacterial inner membrane = GO plasma membrane).
- prenyltransferase activity and both GO:0016765 rows MODIFY to GO:0008412; membrane IEA MODIFY to plasma membrane.
