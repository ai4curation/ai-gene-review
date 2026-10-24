# paaZ curation notes

- UniProt accession Q88HT3 names the target
  `Oxepin-CoA hydrolase/3-oxo-5,6-dehydrosuberyl-CoA semialdehyde dehydrogenase`
  [file:PSEPK/paaZ/paaZ-uniprot.txt,
  "SubName: Full=Oxepin-CoA hydrolase/3-oxo-5,6-dehydrosuberyl-CoA semialdehyde dehydrogenase"].
- The record assigns EC 3.3.2.12 and EC 1.2.1.91, but has prediction-level
  protein evidence. The review therefore models both catalytic roles while
  explicitly retaining the need for target-specific biochemical confirmation.
- The existing generic oxidoreductase term is replaced by the
  aldehyde/oxo-group oxidoreductase child term. A hydrolase annotation is added
  for the second domain; GO currently offers only a broad hydrolase term in the
  local record.

## 2026-10-24 completion pass

- Replaced UniProt quotes that were submitter-imported protein names/EC
  numbers (ECO:0000313) or ARBA-only CATALYTIC ACTIVITY/COFACTOR comments with
  family/domain classification lines from the KT2440 record (NCBIfam,
  PANTHER, PIRSF, PROSITE, CDD, InterPro) plus verbatim quotes from cached
  ortholog literature: Teufel et al. 2010 [PMID:20660314, full text; the
  PaaABC(D)E, PaaG, PaaJ and PaaF enzymes used were from Pseudomonas sp.
  strain Y2, "strain Y2 (PaaABC(D)E, PaaG, PaaJ, PaaF)"], Grishin et al. 2011
  [PMID:21247899, E. coli PaaABCDE], and where relevant PMID:21296885,
  PMID:31511507 (PaaZ), PMID:22961985 (PaaFG), PMID:17259607 (terminal
  thiolysis), PMID:9748275 (PaaK).
- Molecular-function terms aligned with the completed E. coli paa reviews
  (genes/ECOLI/paa*): PaaA enables the epoxidase activity (catalytic diiron
  subunit); PaaB/C/E contribute to it; PaaE GO:0016651; PaaG GO:0016863;
  PaaZ GO:0016803 + GO:0033721. Broad parent terms that a supported specific
  term already covers were changed to MODIFY toward that term.
- No KT2440-specific biochemistry exists for this protein; all functional
  assignments rest on family classification plus orthology. Status set to
  COMPLETE.
