# loqs exact-isoform sequence comparison

The selected 464-residue loqs-PF sequence X2J5X6 is identical to reviewed loqs-PB Q9VJY9 except for a single missing lysine at PB position 383. All three annotated DRBM domains are fully retained. The two RNA-binding domains and the third Dcr-1-interaction domain therefore support transfer of the broad PB-like miRNA-processing function to PF, although exact effects on affinity are not measured. This is not Loqs-PD, the alternative two-DRBM Dcr-2 partner; its specific siRNA mechanism cannot be assigned from PB/PF identity. FlyBase independently lists PF as FBpp0309562, 464 aa, X2J5X6, alongside PB as 465 aa Q9VJY9. No sequence-error conclusion is implied.

## Reproducibility

Global BLOSUM62 alignment, gap-open -10, gap-extension -0.5, Biopython 1.85. Inputs, alignment and JSON results are retained; run `just` in this directory. Source feature positions are read from comparator JSON. A separate reference self-alignment verifies indexing and full sequence recovery; the generic script was also run on independent fly gene proteins. The self-control is a computational check, not biological validation. Prediction-time input sequence is not supplied by the release API.

- [x] No biological results or conclusions hardcoded in analysis.
- [x] Same algorithm run on other protein inputs.
- [x] Analysis and control completed successfully.
- [x] Direct inputs/results retained.
- [x] Sequence provenance and inference limitations stated.
