# hemH (P23871, Escherichia coli K-12) curation notes

## Sources and deep research

- Deep research was unavailable (the `just deep-research` perplexity route failed in this
  environment). The review rests on UniProt P23871, the GOA-cited publications, and the comparator
  genes/PSEPK/hemH.

## Evidence

- Purified visA product is ferrochelatase [PMID:8458858 "The overexpressed protein was purified to
  near homogeneity and was found to contain ferrochelatase activity."]; renamed hemH.
- Monomer, 35 kDa [PMID:8056770 "suggesting that the enzyme is a monomer"].
- Light sensitivity of visA mutants is caused by protoporphyrin IX accumulation [PMID:1397280 "These
  results confirm the hypothesis that the sensitivity of the visA mutants to light is caused by the
  abnormal accumulation of Proto IX, a substrate of ferrochelatase"].
- OxyR induces hemH during H2O2 stress [PMID:25664592 "OxyR induced synthesis of two members of the
  nine-step heme biosynthetic pathway: ferrochelatase (HemH) and an isozyme of coproporphyrinogen III
  oxidase (HemF)."]. No GOA row; no NEW response term added (regulatory induction, kept to notes).

## Decisions

- GO:0009416 response to light stimulus (two EcoliWiki IMP rows): MARK_AS_OVER_ANNOTATED; the
  phenotype is photosensitisation by accumulated substrate, not a light response.
- Porphyrin biosynthesis IEA: MODIFY to GO:0006785 heme B biosynthetic process.
