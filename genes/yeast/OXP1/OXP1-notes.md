# OXP1 (YKL215C, UniProt P28273) notes

- ATP-dependent 5-oxoprolinase (EC 3.5.2.9), 1286 aa, homodimer. "OXP1/YKL215c ... encodes a functional ATP-dependent 5-oxoprolinase of 1286 amino acids" [PMID:20402795]; in vitro "the enzyme exists and functions as a dimer, and has a K(m) of 159 microM" [PMID:20402795]; actin-like ATPase motif mutations abolish activity [PMID:20402795].
- Metabolomics: ykl215c deletion accumulates 5-oxoproline; "we hypothesized that Ykl215c is an oxoprolinase" and gene named OXP1 [PMID:20349993]. Note this paper is metabolite profiling (an IMP-type inference), although annotated IDA.
- Localization: "SUBCELLULAR LOCATION: Cytoplasm" (Huh GFP) [UniProt:P28273].

## Pathway
- Module glutathione_synthesis_gamma_glutamyl_cycle: exemplar for GO:0017168 (5-oxoprolinase); recovers glutamate from 5-oxoproline produced by Gcg1 (ChaC) from GSH. Consistent.
- YeastCyc does not attach OXP1 to any reaction in the summary; the PWY3O-114 comment still describes 5-oxoprolinase as uncertain in yeast - outdated.
- S. pombe ortholog is split into oxp1/oxp2 (module note); PomBase GO-CAM 68b0f0d000008341 types oxp1 as GO:0017168 in cytosol, part of GO:0006749, consistent with this review.
