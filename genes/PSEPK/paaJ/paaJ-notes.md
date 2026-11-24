# paaJ curation notes

- UniProt accession Q88HS3 names the target
  `3-oxoadipyl-CoA/3-oxo-5,6-dehydrosuberyl-CoA thiolase`
  [file:PSEPK/paaJ/paaJ-uniprot.txt,
  "SubName: Full=3-oxoadipyl-CoA/3-oxo-5,6-dehydrosuberyl-CoA thiolase"].
- UniProt records the reaction
  `succinyl-CoA + acetyl-CoA = 3-oxoadipyl-CoA + CoA`
  [file:PSEPK/paaJ/paaJ-uniprot.txt,
  "Reaction=succinyl-CoA + acetyl-CoA = 3-oxoadipyl-CoA + CoA;"].
- The exact 3-oxoadipyl-CoA thiolase term is retained. Generic acyltransferase
  parents are replaced by it, while acetyl-CoA C-acetyltransferase is marked
  over-annotated because it specifies the wrong second substrate.
- Phenylacetate catabolism is modeled as the principal paa-locus role.
  The pathway-level paralog analysis identifies the
  3,4-dihydroxybenzoate-process annotation as over-propagation from
  PcaF/PP_1377, so it is marked over-annotated rather than retained as a
  secondary PaaJ role.

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
