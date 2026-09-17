# CycA exact-isoform sequence comparison

The 490-residue CycA-PC/M9NFR3 sequence matches 490 of 491 residues of PA/P14785, lacking Gln66 in the N-terminal region. The annotated cyclin domain 206–332 is fully retained and maps to target 205–331. The change is outside the cyclin domain, supporting transfer of CDK regulation and broad mitotic cell-cycle function. No exact PC-specific timing or degradation-rate measurement is inferred from this sequence comparison.

## Reproducibility

Global BLOSUM62 alignment, gap-open -10, gap-extension -0.5, Biopython 1.85. Inputs, alignment and JSON results are retained; run `just` in this directory. Source feature positions are read from comparator JSON. A separate reference self-alignment verifies indexing and full sequence recovery; the generic script was also run on independent fly gene proteins. The self-control is a computational check, not biological validation. Prediction-time input sequence is not supplied by the release API.

- [x] No biological results or conclusions hardcoded in analysis.
- [x] Same algorithm run on other protein inputs.
- [x] Analysis and control completed successfully.
- [x] Direct inputs/results retained.
- [x] Sequence provenance and inference limitations stated.
