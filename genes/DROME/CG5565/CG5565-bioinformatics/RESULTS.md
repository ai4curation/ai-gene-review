# CG5565 exact-isoform sequence comparison

The native 240-residue CG5565 protein aligns across 226 of 228 human PUDP/Q08623 residues, with 98 identical aligned positions (43.4% of aligned pairs). Human annotated catalytic Asp14 and Asp16 map to target Asp16 and Asp18. The two catalytic-site assignments in the human record are family-derived; the human enzyme’s substrate specificity is independently measured in PMID:20722631. The near-complete alignment and retained catalytic motif support an intact PUDP-like enzyme and are compatible with the curated ortholog transfer, but do not independently establish a phylogenetic relationship or exact substrate specificity.

The original archaeal structural donor Q9V1B3 aligns over 205 of 238 reference residues, with 55 identical aligned positions (26.8%). This comparison measures sequence correspondence, not a significance-tested substrate classifier. Shared HAD chemistry permits weak side activities; the explicitly in vitro glyceraldehyde-3-phosphate claim remains UNC. The human self-control recovers all 228 residues and both catalytic-site positions correctly.

## Reproducibility

Global BLOSUM62 alignment, gap-open -10, gap-extension -0.5, Biopython 1.85. Inputs, alignment and JSON results are retained; run `just` in this directory. Source feature positions are read from comparator JSON. A separate reference self-alignment verifies indexing and full sequence recovery; the generic script was also run on independent fly gene proteins. The self-control is a computational check, not biological validation. Prediction-time input sequence is not supplied by the release API.

- [x] No biological results or conclusions hardcoded in analysis.
- [x] Same algorithm run on other protein inputs.
- [x] Analysis and control completed successfully.
- [x] Direct inputs/results retained.
- [x] Sequence provenance and inference limitations stated.
