# des (Bacillus subtilis 168, O34653) curation notes

## 2026-11-13

- Des is the cold-induced membrane phospholipid Delta5 desaturase
  [PMID:9555904 "indicating that the B. subtilis des gene product is a delta5 acyl-lipid desaturase"];
  des null mutants make no unsaturated fatty acids after a cold shift
  [PMID:9555904 "the resulting null mutant strains were unable to synthesize UFAs upon a shift to low growth temperatures"].
- GO has no Delta5 acyl-lipid desaturase term, so the core MF is the
  oxygen-dependent desaturase class GO:0016717. A new term is proposed in the
  review.
- Broad PAINT rows (lipid metabolic process, membrane) are refined to
  GO:0006636 and the plasma membrane.
- **Aerobic desaturase exemplar choice.** Des is the oxygen-dependent
  exemplar in `modules/bacterial_unsaturated_fatty_acid_biosynthesis.yaml`.
  Pseudomonas aeruginosa DesA (Q9I6K4, PA0286, Delta9 desaturase) and DesB
  (Q9HUS5, PA4888, acyl-CoA Delta9 desaturase) also act aerobically, but
  their UniProt entries are unreviewed and have no gene reviews here, so
  they were not used as module exemplars.
- Regulation by the DesK/DesR two-component system is upstream context, not
  part of Des function.
