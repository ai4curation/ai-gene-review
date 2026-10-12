# CANAL ALO1 notes

## 2026-10-10

- `just fetch-gene CANAL ALO1` seeded 27 GOA rows for UniProtKB:O93852 and
  cached the three publication records directly referenced by GOA:
  PMID:7957197, PMID:11349062, and PMID:19824013.
- Falcon deep research could not run in this environment because no configured
  deep-research provider key was available:
  `OPENAI_API_KEY`, `EDISON_API_KEY`, `ASTA_API_KEY`, or `PERPLEXITY_API_KEY`.
- Manual newer-paper search did not find a later re-characterization of
  C. albicans ALO1 itself. The most directly relevant later paper is
  PMID:18282465, which used `alo1/alo1` and ALO1-overexpression strains to show
  that D-erythroascorbic acid affects alternative oxidase induction and
  cyanide-resistant respiration.
- PMID:39775849 is the source-side budding-yeast study for the SGD
  `myosin V binding` assertion. It supports a S. cerevisiae Alo1-Myo2
  mitochondrial-inheritance interaction, but I found no direct C. albicans
  support for transferring that binding activity.

## Annotation synthesis

- `PANTHER:PTN000356435` carries the ALO1-family
  `GO:0003885 D-arabinono-1,4-lactone oxidase activity` IBD and is seeded by
  the experimentally characterized CGD and SGD ALO1 proteins.
- `PANTHER:PTN001015900` carries only `GO:0005739 mitochondrion`, matching the
  experimentally demonstrated broad mitochondrial localization of the Candida
  enzyme and avoiding the outer-membrane-side specificity from the recent
  budding-yeast Myo2/Alo1 work.
- The 1994 purified-enzyme paper supports EC 1.1.3.37 as the physiological
  reaction and also shows L-galactono-1,4-lactone and L-gulono-1,4-lactone can
  be used as alternate substrates.
- The 2001 ALO1 deletion and overexpression paper establishes the direct
  gene-enzyme connection: deleting both ALO1 alleles eliminates cellular
  D-arabinono-1,4-lactone oxidase activity and D-erythroascorbic acid, while
  extra ALO1 raises both. The oxidative-stress, filamentation, starvation-medium
  growth, detoxification, and virulence annotations are downstream phenotypes of
  losing the antioxidant product rather than separate core functions.
- PMID:19824013 remains unresolved. The abstract describes plasma-membrane
  proteomics, but the cached record has no ALO1-specific peptide or protein
  table. Given the CGD IDA and the abstract-only cache, the review leaves
  `GO:0005886 plasma membrane` as `UNDECIDED`.
