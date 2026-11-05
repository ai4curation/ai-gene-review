# spuI (PA0296, PauA1, Q9I6J5) notes

PubMed search returned API errors on 2026-11-05. Lu et al. 2002 full text is
cached; Yao et al. 2011 (PMC3147493) was read through a fetch summary of the
PMC page.

## Literature

- spuI mutants show no growth defect on polyamines [PMID:12081945 "While mutations on spuI did not show any growth defect on agmatine and polyamines, the contiguous spuABC genes are all related to polyamine catabolism."].
- SpuB and SpuI are glutamine synthetase homologues [PMID:12081945 "One interesting feature of these spu genes is the presence of two putative glutamine synthetase homologues encoded by spuB and spuI ."].
- pauA knockouts act in combinations [PMID:21622750 "it requires specific combinations of pauA knockouts to abolish utilization of different polyamines"].
- PMC full text (fetch summary): pauA1 = PA0296. pauA1 single mutant normal on
  all polyamines; pauA1A4 severely retarded on Put; pauA1A2A4 cannot grow on
  Put; pauA1A4A5 cannot grow on Cad. Spd growth needs pauA2 alone.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN001839150 | GO:0006598 polyamine catabolic process | 4 | 10 (4 taxa) | GO:0009447, IMP, PMID:12081945 (PseudoCAP) | WRONG (reference) | Cited paper reports no spuI growth defect; the term is true from PMID:21622750 (pauA1A4, pauA1A2A4). | PuuA P78061 (IMP, IDA); PA1566 Q9I3F1 (SOUND); SpuB Q9I6J3 (SOUND) | Yes |
| PTN001839150 | GO:0006598 polyamine catabolic process | 4 | 10 (4 taxa) | GO:0046203, IMP, PMID:12081945 (PseudoCAP) | WRONG | Cited paper reports no defect; spermidine growth depends on pauA2 (spuB), not pauA1. | as above | Yes |

PSEUDOCAP defects: 2, both CONFIRMED (full text of PMID:12081945 read):
WRONG_REFERENCE REPOINT to PMID:21622750 (GO:0009447) and WRONG_REFERENCE
DELETE_ROW (GO:0046203; possibly meant for spuB). No GO_CENTRAL defect: the IBD
stands without SpuI and the term is true for it. Node shared with PA1566 and
spuB (see their notes).
