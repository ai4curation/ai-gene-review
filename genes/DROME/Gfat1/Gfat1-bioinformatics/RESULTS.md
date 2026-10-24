# Gfat1 exact-isoform sequence comparison

A8Y5A1 is the native Gfat1-PF isoform (434 residues; FlyBase FBpp0112413), not the 694-residue PA/PN product Q7PLC7. All 434 target residues match the C-terminal 434 residues of Q7PLC7. Only 40 of 299 residues of the annotated glutamine-amidotransferase domain remain, and its N-terminal catalytic Cys2 is absent. Both SIS domains are fully retained (reference 372–512 and 543–684). The structure supports retained sugar binding, but loss of the glutaminase module contradicts assigning the complete intrinsic glutamine-dependent amidotransferase reaction. Free-ammonia use, trans-complementation and a regulatory role are not demonstrated and are not assumed. Native transcript annotation does not establish actual protein abundance or a prediction-input error.

## Reproducibility

Global BLOSUM62 alignment, gap-open -10, gap-extension -0.5, Biopython 1.85. Inputs, alignment and JSON results are retained; run `just` in this directory. Source feature positions are read from comparator JSON. A separate reference self-alignment verifies indexing and full sequence recovery; the generic script was also run on independent fly gene proteins. The self-control is a computational check, not biological validation. Prediction-time input sequence is not supplied by the release API.

- [x] No biological results or conclusions hardcoded in analysis.
- [x] Same algorithm run on other protein inputs.
- [x] Analysis and control completed successfully.
- [x] Direct inputs/results retained.
- [x] Sequence provenance and inference limitations stated.
