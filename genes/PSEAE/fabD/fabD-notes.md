# fabD (PA2968, G3XCZ6) notes

## Literature

No deep-research provider was available. Source: cached abstract of PMID:10464226 (PMC full text not
retrieved).

- [PMID:10464226 "In an in vitro system, purified ACP functioned as acyl acceptor and H(6)-FabD exhibited
  malonyl-CoA:ACP transacylase activity"]; ts allele [PMID:10464226 "A chromosomal temperature-sensitive
  fabD mutant was obtained by site-directed mutagenesis that resulted in a W258Q change"].

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002448244 | GO:0006633 fatty acid biosynthetic process | 5 | 90 (79 taxa) | GO:0006633, IDA, PMID:10464226 (PseudoCAP) | SOUND | Purified FabD loads malonyl onto ACP, the committed step feeding FAS II elongation. | E. coli FabD P0AAI9, M. tuberculosis FabD P9WNG5, human MCAT Q8IVS2, Arabidopsis AT2G30200 | Yes. |

No PSEUDOCAP or GO_CENTRAL defect.

## Curation gap

PseudoCAP annotated only the process from PMID:10464226; the paper's direct result is the MCAT activity
(GO:0004314), which is in GOA only by IBA/IEA. A NEW row was not possible (validation rejects NEW for a term
already in GOA); an IDA GO:0004314 row from PMID:10464226 should be added upstream.
