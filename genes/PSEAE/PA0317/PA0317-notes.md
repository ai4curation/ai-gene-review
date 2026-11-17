# PA0317 (Q9I6H4) review notes

No deep-research provider was available. Sources: UniProt record, cached
PMID:28827360 (abstract and significance; PMC full text body not returned by the
PubMed MCP).

## Function

- Bacterial FAD-dependent D-2-hydroxyglutarate dehydrogenase (D2HGDH) identified in
  P. stutzeri A1501 and P. aeruginosa PAO1 [PMID:28827360 "We identified a bacterial
  d-2-hydroxyglutarate dehydrogenase (D2HGDH), a flavin adenine dinucleotide
  (FAD)-dependent enzyme, that converts d-2-HG back to 2-ketoglutarate"].
- Coupled to SerA and L-serine synthesis; deletion defect rescued by L-serine
  [PMID:28827360 "the defect was rescued by adding l-serine, suggesting that the
  D2HGDH is functionally tied to l-serine synthesis"].
- Electrons pass via ETF and ETFQO to the respiratory chain [PMID:28827360
  "Electron transfer flavoprotein (ETF) and ETF-ubiquinone oxidoreductase (ETFQO)
  are also essential in d-2-HG metabolism through their capacity to transfer
  electrons from D2HGDH"].

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN005178867 | GO:0051990 (R)-2-hydroxyglutarate dehydrogenase activity | 8 | 127 (103 taxa) | GO:0051990, IMP, PMID:28827360 (PseudoCAP) | SOUND | The paper biochemically identified the FAD-dependent D2HGDH activity (not merely a mutant phenotype) in PAO1 and P. stutzeri. The node term matches the D2HGDH family. | human D2HGDH Q8N465, Arabidopsis AT4G36400, rat RGD:1307976, two S. cerevisiae genes, Drosophila FBgn0023507, mouse MGI:2138209 | Yes; human mitochondrial D2HGDH (Q8N465) and the yeast/plant members carry independent experimental support. No GO_CENTRAL defect. |

PseudoCAP defects from this gene: none. The IMP GO:0051990 and GO:0006564 rows are
well supported by the cited paper.
