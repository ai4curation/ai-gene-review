# Manual deep research for ACYP2

Automated Perplexity deep research was unavailable in this runtime; the wrapper
reported `Provider 'perplexity' not available. Available: claude_code`. This
manual note records the literature used to repair the review.

## Key findings

- PMID:8268218 synthesized the human muscle acylphosphatase coding sequence,
  expressed it in E. coli and Saccharomyces cerevisiae, and found that the
  recombinant enzymes maintained the kinetic properties of natural muscle
  acylphosphatase against benzoylphosphate.
- PMID:1645713 assayed acylphosphatase purified from human erythrocytes and
  therefore supports ACYP1 physiology rather than the ACYP2 GOA row that cites
  it.
- PMID:8702578 reports that acylphosphatase purified from heart muscle
  actively hydrolyzes the cardiac sarcoplasmic-reticulum Ca2+ pump
  phosphoenzyme at concentrations within the physiological range.
- PMID:12374855 and PMID:16084386 use human muscle acylphosphatase as an
  in-vitro amyloid aggregation model. They establish experimentally observed
  aggregation, but under non-native or mutational conditions rather than a
  physiological homodimerization function.

## Curation consequences

- The PMID:1645713 row is retained as a true ACYP2 activity claim only because
  PMID:8268218 independently supports ACYP2 acylphosphatase activity; its
  upstream problem is now a suspected wrong-gene-product defect.
- The broad ProtInc `GO:0006796` row was modified to the verified descendant
  `GO:0016311` dephosphorylation rather than marked over-annotated.
- Cardiac SR Ca2+-ATPase phosphoenzyme is a plausible physiological substrate
  for muscle/heart ACYP2, but the dominant intact-cell substrate set remains a
  biology knowledge gap.
