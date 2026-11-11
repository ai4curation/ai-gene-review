# sptl-1 (P91079) bioinformatics results

Script: `align_plp_lysine.py` (Biopython PairwiseAligner, global, BLOSUM62, gap open -10, extend -0.5).
Inputs: UniProt FASTA for P91079 (C. elegans SPTL-1), O15269 (human SPTLC1), O15270 (human SPTLC2),
downloaded from rest.uniprot.org.

Output (verbatim):

```
P91079 vs O15270: identity 132/439 aligned = 30.1%
  O15270 residue 379 = K; window MGTFTKSFGAS
  aligned P91079 residue 297 = N; window MASLENALAST
P91079 vs O15269: identity 227/451 aligned = 50.3%
  O15269 residue 133 = C; window YGVGTCGPRGF
  aligned P91079 residue 121 = C; window YGVGSCGPRGF
```

## Interpretation

- SPTL-1 is far closer to human SPTLC1 (50.3% identity over the aligned region) than to SPTLC2 (30.1%),
  consistent with it being the LCB1-type (SPTLC1-like) subunit of the SPT heterodimer.
- At the position aligned to the SPTLC2 PLP Schiff-base lysine (K379), SPTL-1 has Asn297, not Lys.
  SPTL-1 therefore lacks the catalytic PLP-binding lysine, as do the LCB1/SPTLC1 subunits of other
  eukaryotes; the PLP cofactor is expected to be bound by the LCB2-type partner (SPTL-2 or SPTL-3).
- SPTL-1 Cys121 aligns with human SPTLC1 Cys133 (HSAN1 C133W site), matching the residue engineered
  as SPTL-1(C121W) by Cui et al. 2019 (PMID:31138658).
