# PA1566 (PauA3, Q9I3F1) notes

PubMed search returned API errors on 2026-11-05. Yao et al. 2011 (PMC3147493)
cached abstract only; the PMC article page was read through a fetch summary
(Table 1 locus map, Table 2 growth phenotypes).

## Literature

- pauA1-pauA7 encode PuuA homologues of the gamma-glutamylation pathway
  [PMID:21622750 "encode enzymes homologous to Escherichia coli PuuABCD of the γ-glutamylation pathway in converting Put into GABA"].
- pauA3B2 participate in DAP catabolism [PMID:21622750 "Mutation analysis led to the conclusion that pauA3B2 participate in catabolism of DAP, which is related to the aminopropyl moiety of Spd"].
- PMC full text (fetch summary): pauA3 = PA1566; the pauA3 mutant's growth on
  DAP is retarded; growth on Put, Cad, Spd normal. No purified-enzyme assay.
- PANTHER PTHR43785 "GAMMA-GLUTAMYLPUTRESCINE SYNTHETASE" (UniProt DR line).

## PseudoCAP IBA-seed assessment

Other seeds' experimental support queried live in QuickGO on 2026-11-05.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN001839150 | GO:0006598 polyamine catabolic process | 4 | 10 (4 taxa) | GO:0006598, IMP, PMID:21622750 (PseudoCAP) | SOUND | pauA3 mutant retarded on 1,3-diaminopropane; GO has no DAP-catabolism term, so the general term is right. | E. coli PuuA P78061 (IMP putrescine catabolism, IDA glutamate-putrescine ligase, PMID:18495664); SpuB Q9I6J3 (SOUND); SpuI Q9I6J5 (WRONG reference) | Yes |

No PSEUDOCAP or GO_CENTRAL defect. Shared node with spuI and spuB (same
batch); the node-level judgment is identical in all three: the IBD stands on
PuuA, PauA3 and PauA2 even though SpuI's seed rows are mis-referenced (defects
recorded on spuI only).

The L-glutamine biosynthetic process IBA (PTN000464978, GlnA seed) and the
glutamine synthetase IEA are marked over-annotated / modified consistently on
all three PauA genes.
