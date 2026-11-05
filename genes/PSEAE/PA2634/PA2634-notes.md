# PA2634 (aceA, Q9I0K4) notes

## Literature

No deep-research provider was available. PubMed search via the MCP returned an API error on 2026-11-05;
the review rests on the cached abstract of PMID:17319879, the cached full text of PMID:23363478 and the
reviewed UniProt entry (structure PDB 6G1O).

- PA2634 is aceA, the sole ICL [PMID:17319879 "The isocitrate lyase gene (aceA) corresponding to ORF
  PA2634 of the PAO1 strain genome was identified in one of these mutants"].
- Activity in crude extracts, induced by acetate, citronellol, leucine [PMID:17319879 "The ICL enzyme
  activity in crude extracts from cultures of the PAO1 strain was induced by acetate, citronellol and
  leucine"]; complementation [PMID:17319879 "Genetic complementation further confirmed that the aceA gene
  encodes the ICL enzyme"].
- Biofilm phenotype is shared with other TCA/glyoxylate mutants [PMID:23363478 "Biofilm formation under
  anaerobic conditions was significantly enhanced in the aceA mutant as well as in the other mutants that
  showed reduced PcrV expression"].

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000493043 | GO:0004451 isocitrate lyase activity | 9 | 102 (75 taxa) | GO:0004451, IDA, PMID:17319879 (PseudoCAP) | SOUND | Abstract: ICL activity in wild-type extracts plus a complemented aceA mutant; full ICL signature. Strictly an IMP+IDA combination, not a purified-enzyme assay. | E. coli AceA P0A9G6, M. tuberculosis P9WKK7 and O07718, yeast SGD:S000000867, Candida CGD:CAL0000178151, Arabidopsis AT3G21720, rice Q6Z6M4, Q6T267 | Yes. Characterised ICLs from bacteria, fungi and plants; the term suits the ICL clade. |

No PSEUDOCAP or GO_CENTRAL defect.

## Other decisions

- GO:1900232 negative regulation of biofilm formation (PseudoCAP IMP, PMID:23363478, full text read):
  MARK_AS_OVER_ANNOTATED. Indirect metabolic phenotype shared by aceE, aceK, icd-idh and glcB mutants.
  No defect recorded (not a seed).
- GO:0003824: TOO_GENERAL.
