# spuB (PA0298, PauA2, Q9I6J3) notes

PubMed search returned API errors on 2026-11-05. Lu et al. 2002 full text is
cached; Yao et al. 2011 (PMC3147493) was read through a fetch summary of the
PMC page.

## Literature

- spuB mutants are defective in spermidine utilization [PMID:12081945 "Although spuA and spuB mutants showed an apparent defect in spermidine utilization, the biochemical functions of the gene products have yet to be elucidated."].
- PMC full text (fetch summary): pauA2 = PA0298; a single pauA2 knockout
  completely blocks growth on Spd; growth on diamines normal; pauA2 also in the
  pauA1A2A4 putrescine-null combination.
- No purified-enzyme assay.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN001839150 | GO:0006598 polyamine catabolic process | 4 | 10 (4 taxa) | GO:0046203, IMP, PMID:21622750 (PseudoCAP) | SOUND | Single pauA2 knockout abolishes growth on spermidine; independently seen in PMID:12081945. | PuuA P78061 (IMP, IDA); PA1566 Q9I3F1 (SOUND); SpuI Q9I6J5 (WRONG reference) | Yes |

No PSEUDOCAP or GO_CENTRAL defect. Node shared with PA1566 and spuI; spuI's
mis-referenced rows carry the defects (see spuI notes).
