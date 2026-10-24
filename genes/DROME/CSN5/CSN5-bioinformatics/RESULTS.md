# CSN5 exact-isoform sequence comparison

The 325-residue CSN5-PB/A0A0B4KHM2 sequence matches 325 of 327 residues of reviewed PA/Q9XZ58, lacking Gly278 and Arg279 outside the MPN domain. The MPN domain 52–189 and JAMM motif 135–148 are completely retained, including His135, His137 and Asp148. This supports transfer of the catalytic-subunit role, without claiming that isolated CSN5 is an autonomous protease or that its participation in neuronal development establishes synaptic-vesicle residence.

## Reproducibility

Global BLOSUM62 alignment, gap-open -10, gap-extension -0.5, Biopython 1.85. Inputs, alignment and JSON results are retained; run `just` in this directory. Source feature positions are read from comparator JSON. A separate reference self-alignment verifies indexing and full sequence recovery; the generic script was also run on independent fly gene proteins. The self-control is a computational check, not biological validation. Prediction-time input sequence is not supplied by the release API.

- [x] No biological results or conclusions hardcoded in analysis.
- [x] Same algorithm run on other protein inputs.
- [x] Analysis and control completed successfully.
- [x] Direct inputs/results retained.
- [x] Sequence provenance and inference limitations stated.
