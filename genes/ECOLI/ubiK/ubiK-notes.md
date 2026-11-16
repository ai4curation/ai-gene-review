# ubiK (Q46868, E. coli K-12) review notes

## Sources
- No deep-research provider output exists for this gene (provider API keys unavailable in this session);
  the review is built from the UniProt record, the cached publications and the PAINT file for PTHR38040.
- Key papers: Loiseau et al. 2017 (PMID:28559279, abstract cached), Hajj Chehade et al. 2019
  (PMID:30686758, abstract cached, not open access), Lamarche et al. crosslinking MS (PMID:34117231, full
  text), multiscale modelling of UbiJ-UbiK2 (PMID:36142227, abstract).

## Findings
- yqiC renamed ubiK; required for efficient UQ biosynthesis [PMID:28559279 "we report on the identification
  of a bacterial gene, yqiC, which is required for efficient UQ biosynthesis, and which we have renamed ubiK"].
- ubiK mutants accumulate octaprenylphenol and are dispensable anaerobically [PMID:28559279 "both ubiK and
  ubiJ mutants accumulated octaprenylphenol, an early intermediate of the UQ biosynthetic pathway"].
- Component of the soluble Ubi metabolon [PMID:30686758 "seven Ubi proteins form the Ubi complex, a stable
  metabolon that catalyzes the last six reactions of the UQ biosynthetic pathway in Escherichia coli"].
- Modelling places UbiJ-UbiK2 at the membrane [PMID:36142227 "Our data show that UbiJ-UbiK2 interacts
  closely with the membrane"].

## Decisions
- Bare protein binding IPI rows removed per policy; the UbiJ/metabolon association is represented by
  GO:0110142 (ACCEPT).
- Cytoplasm rows MODIFY to cytosol (soluble protein with IDA/IBA cytosol rows), consistent with the queF
  precedent.
- Membrane IDA (EcoCyc, from PMID:30686758 whose full text we could not read) kept as non-core: deferring to
  the curator; modelling supports a peripheral membrane interface.
- No molecular function term is asserted: the biochemical activity of UbiK is unknown.
