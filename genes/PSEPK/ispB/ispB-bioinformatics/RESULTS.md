# IspB (Q88Q11, PP_0687) versus E. coli IspB (P0AD57)

Script: `compare_ispb.py` (Biopython global alignment, BLOSUM62, gap open -10,
extend -0.5). Run from the repository root:
`python genes/PSEPK/ispB/ispB-bioinformatics/compare_ispb.py`.

## Output (verbatim)

```
E. coli IspB P0AD57 length: 323
P. putida IspB Q88Q11 length: 322
Aligned (ungapped) columns: 322
Identical positions: 166 (51.6% of aligned columns)
E. coli Y38 aligns with P. putida Y38
E. coli A79 aligns with P. putida A79
E. coli R321 aligns with P. putida R320
E. coli first DDxxD motif DDVVD at 84; P. putida aligned segment: DDVVD
```

## Interpretation

- Q88Q11 is a full-length trans-prenyl diphosphate synthase that is 51.6%
  identical to E. coli IspB over its whole length, with the first
  aspartate-rich (DDxxD) motif conserved. That fits a one-to-one orthologue
  of the homodimeric bacterial quinone side-chain synthase.
- The three E. coli residues reported to affect product chain length or
  activity (Y38, A79, R321; PMID:11108713) are conserved in Q88Q11. That
  conservation does not tell C40 from C45 product lengths, because other
  positions (and dimer contacts) also set chain length. The alignment
  therefore supports "long-chain all-trans-prenyl diphosphate synthase" but
  cannot assign the octaprenyl (C40) versus nonaprenyl (C45) product.
- Pseudomonads make ubiquinone-9 (measured in P. aeruginosa,
  PMID:32409583), so the expected product in P. putida KT2440 is
  all-trans-nonaprenyl diphosphate. The chain length has not been measured
  for KT2440 or for this enzyme. This is an inference, not a result.
