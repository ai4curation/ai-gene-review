# Manual deep research for ACYP1

Automated Perplexity deep research could not run in this checkout: the wrapper
reported `Provider 'perplexity' not available. Available: claude_code`. This
manual note records the literature used to repair the review.

## Key findings

- The erythrocyte/organ-common isozyme was purified from human erythrocytes in
  PMID:3026468. Its abstract reports hydrolytic activity on acyl phosphates,
  higher affinity than the muscle enzyme for some substrates and phosphorylated
  inhibitors, and 44% sequence divergence from the muscle isozyme.
- PMID:7796909 cloned the cDNA coding for the human erythrocyte isozyme and
  expressed recombinant enzyme with kinetic characteristics close to the native
  protein.
- PMID:1645713 tested acylphosphatase purified from human erythrocytes on the
  red-cell membrane Ca2+-ATPase phosphoenzyme. The abstract reports activity at
  physiological enzyme amounts, a 3.41 nM Km for the phosphoenzyme
  intermediate, about twofold stimulation of ATP hydrolysis, and a reduction in
  Ca2+/ATP coupling from 2.04 to 0.9.
- PMID:16511269 crystallized human common-type acylphosphatase and collected
  1.45 A diffraction data for the structure that appears as the PTHR10029
  representative structure.
- PMID:19196981 used human acylphosphatase in a computational surface
  charge-redesign study; its abstract reports that the designed AcPh variants
  retained activity, structure and oligomeric state.

## Curation consequences

- PMID:1645713 belongs with ACYP1 physiology, not as ACYP2-specific evidence.
- The broad ProtInc `GO:0006796` row is true but too general for an
  acylphosphatase and was modified to the verified descendant
  `GO:0016311` dephosphorylation.
- The literature supports several candidate ACYP1 substrates, but not a single
  resolved in-vivo pathway, so the remaining substrate hierarchy was recorded as
  a biology knowledge gap.
