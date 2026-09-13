# CG33453 exact-isoform sequence comparison

The selected CG33453-PB A0A0B4LFV5 protein has 174 residues, compared with 175 for same-gene PA/A1ZBI2. Global alignment finds 173 identical aligned residues, with different short N termini and otherwise retained sequence. Both are native FlyBase gene products; a one-residue length difference is not a sequence-error diagnosis. This alignment establishes isoform relatedness but not functional equivalence to mammalian GM2 activator proteins. No experimental native ligand, enzyme partner or lysosomal localization was established.

## Reproducibility

Global BLOSUM62 alignment, gap-open -10, gap-extension -0.5, Biopython 1.85. Inputs, alignment and JSON results are retained; run `just` in this directory. Source feature positions are read from comparator JSON. A separate reference self-alignment verifies indexing and full sequence recovery; the generic script was also run on independent fly gene proteins. The self-control is a computational check, not biological validation. Prediction-time input sequence is not supplied by the release API.

- [x] No biological results or conclusions hardcoded in analysis.
- [x] Same algorithm run on other protein inputs.
- [x] Analysis and control completed successfully.
- [x] Direct inputs/results retained.
- [x] Sequence provenance and inference limitations stated.
