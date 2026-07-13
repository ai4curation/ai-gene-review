# PP_2266 notes

## 2026-07-10

- `just fetch-gene` could not populate PP_2266 because UniProt REST returned HTTP 500; `PP_2266-uniprot.txt` is explicitly marked as fallback context [file:PSEPK/PP_2266/PP_2266-uniprot.txt "CC   -!- CAUTION: Minimal fallback context assembled from projects/P_PUTIDA/data/psepk_uniprot_metadata.tsv because UniProt REST returned HTTP 500 on 2026-07-10."].
- Routed this gene out of the translation/RNA-processing umbrella into transcription/RNA-polymerase spillover context.
- Core interpretation: PP_2266 encodes a predicted DNA-directed RNA polymerase-like protein with RNA polymerase domain evidence. This first pass routes it to RNA polymerase/transcription context while leaving its relationship to the compact canonical rpoA/rpoB/rpoC/rpoZ core unresolved.
- Asta was run as fast retrieval context and is recorded as provenance only [file:PSEPK/PP_2266/PP_2266-deep-research-asta.md "  uniprot_accession: Q88KM4"] .
