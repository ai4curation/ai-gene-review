# atuR (PA2885, Q9HZW2) review notes

## Literature

- atuR lies upstream of atuABCDEFGH and negatively regulates it [PMID:16820476 "A regulatory gene, atuR, was identified upstream of atuABCDEFGH and negatively regulated expression of the atu gene cluster"].
- AtuR is a TetR-family repressor; Atu proteins are constitutive in the atuR mutant, and purified AtuR homodimers bind two 13-bp inverted repeats in the atuA operator [PMID:20487029 "Two 13 bp inverted repeat sequences separated by 40 bp in the atuA operator/promoter region were identified to represent two sites of AtuR binding by EMSA"].

Search: PubMed metadata/abstracts for GOA-cited PMIDs (abstract-only caches).

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN004738546 | GO:0006355 regulation of DNA-templated transcription | 19 | 411 (33 taxa) | GO:0045892, IMP, PMID:20487029 | SOUND | Abstract states constitutive Atu protein expression in the atuR insertion mutant plus EMSA binding to the atuA operator. | 18 other seeds incl. AcrR, RutR, KstR, EthR | Yes |

Node-level verdict for PTN004738546 (all three IBDs stand on many experimentally characterised TetR regulators, no GO_CENTRAL defect) is recorded once in `genes/PSEAE/nfxB/nfxB-notes.md`.

Non-seed PseudoCAP row: GO:0046247 terpene catabolic process IDA (PMID:20487029) is INDIRECT-PHENOTYPE/WRONG for a repressor; REMOVE with a PSEUDOCAP DELETE_ROW defect, PROBABLE (abstract describes only regulatory evidence). Not a seed of PTN004738546, so no node effect.
