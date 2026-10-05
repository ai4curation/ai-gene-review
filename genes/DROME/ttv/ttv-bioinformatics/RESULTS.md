# ttv exact-isoform sequence comparison

D5SHU8 is the native 299-residue ttv-PC product (FlyBase FBpp0305368) and matches residues 462–760 of full-length Q9V730. The C-terminal glycosyltransferase-region active-site Asp670 maps to target Asp209, and the source-record nucleotide-sugar/metal-binding residues in this region are retained. The N-terminal membrane anchor and N-terminal glycosyltransferase region are absent. Mammalian EXT structures distinguish N-terminal GT-B and C-terminal GT-A domains; the retained C-terminal domain is not intrinsically devoid of catalytic potential. However, experimental isolated-domain expression/activity limitations and missing targeting information prevent assigning full physiological catalytic competence to this native short isoform.

## Reproducibility

Global BLOSUM62 alignment, gap-open -10, gap-extension -0.5, Biopython 1.85. Inputs, alignment and JSON results are retained; run `just` in this directory. Source feature positions are read from comparator JSON. A separate reference self-alignment verifies indexing and full sequence recovery; the generic script was also run on independent fly gene proteins. The self-control is a computational check, not biological validation. Prediction-time input sequence is not supplied by the release API.

- [x] No biological results or conclusions hardcoded in analysis.
- [x] Same algorithm run on other protein inputs.
- [x] Analysis and control completed successfully.
- [x] Direct inputs/results retained.
- [x] Sequence provenance and inference limitations stated.
