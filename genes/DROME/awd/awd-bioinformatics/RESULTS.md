# awd exact-isoform sequence comparison

The 168-residue awd-PC/PD protein A0A0B4LHX6 contains the entire 153-residue reviewed P08879 sequence unchanged, preceded by a 15-residue N-terminal extension. Catalytic His119 maps to target His134; all seven annotated nucleotide-binding positions are preserved. FlyBase currently recognizes the 168-residue PC/PD products, whereas reviewed UniProt flags the extended initiation in AAF57188.3 as erroneous. This source disagreement does not remove the complete catalytic core, so broad NDP-kinase function remains a sound transfer. It does not establish which initiation site was used by the original prediction pipeline.

## Reproducibility

Global BLOSUM62 alignment, gap-open -10, gap-extension -0.5, Biopython 1.85. Inputs, alignment and JSON results are retained; run `just` in this directory. Source feature positions are read from comparator JSON. A separate reference self-alignment verifies indexing and full sequence recovery; the generic script was also run on independent fly gene proteins. The self-control is a computational check, not biological validation. Prediction-time input sequence is not supplied by the release API.

- [x] No biological results or conclusions hardcoded in analysis.
- [x] Same algorithm run on other protein inputs.
- [x] Analysis and control completed successfully.
- [x] Direct inputs/results retained.
- [x] Sequence provenance and inference limitations stated.
