# ygfA (P0AC28, b2912) notes

## Deep research status

`just deep-research ECOLI folD --provider perplexity` failed in this session
("Provider 'perplexity' not available"; no provider key configured), so deep
research was not run for ygfA. These notes are my own reading of the UniProt
record and cached abstracts (all three cited papers are abstract-only).

## Literature reviewed

- Jeanguenin et al. 2010. Deleting ygfA (5-FCL) makes E. coli accumulate
  5-CHO-THF and, on glycine as sole N source, grow poorly; both phenotypes are
  complemented by glutamate formiminotransferase genes
  [PMID:20952389 "The deletion mutant accumulated 5-CHO-THF and, with glycine as
  sole nitrogen source, showed a growth defect"]. 5-CHO-THF is a side product of
  SHMT and an inhibitor of folate enzymes [PMID:20952389 "Unlike other folates, it
  is not a one-carbon donor but a potent inhibitor of folate enzymes and must
  therefore be metabolized."].
- Hansen, Lewis & Vulic 2008. Knockout-library screen for ofloxacin persisters;
  ygfA deletion lowered persister levels and overexpression raised tolerance
  [PMID:18519731 "the overexpression of both genes produced increased tolerance to
  ofloxacin"]. Indirect phenotype; proposed mechanism (folate pool depletion) is
  speculative.
- Butland et al. 2005. Large-scale affinity purification/MS interaction network;
  source of the IPI with Ndk (P0A763) [PMID:15690043]. Bare protein binding.

## Synthesis

YgfA is the E. coli 5-formyl-THF cyclo-ligase (EC 6.3.3.2), ATP-dependent
conversion of 5-CHO-THF to 5,10-methenyl-THF, salvaging the folate pool and
relieving inhibition of SHMT/glycine cleavage. Soluble 182-aa protein, no TM or
signal peptide; cytoplasmic. GO:0009396 (folic acid-containing compound
biosynthetic process) is an ancestor of GO:0035999 (tetrahydrofolate
interconversion is_a tetrahydrofolate biosynthetic process, checked in OLS
2026-11-13), so it is refined to GO:0035999.
