# paaF curation notes

- UniProt accession Q88HR9 names PaaF `Enoyl-CoA hydratase-isomerase` and
  assigns EC 4.2.1.17
  [file:PSEPK/paaF/paaF-uniprot.txt,
  "SubName: Full=Enoyl-CoA hydratase-isomerase"].
- The precise enoyl-CoA hydratase molecular-function annotation is accepted;
  its generic catalytic and hydro-lyase parents are replaced by that term.
- `fatty acid beta-oxidation` is marked as over-annotated. It is a
  TreeGrafter family transfer, whereas this protein is the PaaF encoded in the
  phenylacetate catabolic locus and is modeled in the analogous lower
  phenylacetate pathway.

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
