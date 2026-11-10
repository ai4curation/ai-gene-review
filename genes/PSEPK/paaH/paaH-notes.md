# paaH curation notes

- UniProt accession Q88HS1 names the target
  `3-hydroxyadipyl-CoA dehydrogenase` and assigns EC 1.1.1.35
  [file:PSEPK/paaH/paaH-uniprot.txt,
  "SubName: Full=3-hydroxyadipyl-CoA dehydrogenase"].
- The EC-mapped `(3S)-3-hydroxyacyl-CoA dehydrogenase (NAD+) activity` is the
  best available GO molecular-function term. Broader catalytic and
  oxidoreductase terms are replaced by it.
- The InterPro-derived `3-hydroxybutyryl-CoA dehydrogenase activity` is
  substrate-specific in the wrong direction and is marked over-annotated
  pending direct substrate-range data.
- Fatty-acid metabolism and beta-oxidation annotations are family transfers;
  the exact target's physiological assignment is the analogous lower segment
  of phenylacetate catabolism.

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
