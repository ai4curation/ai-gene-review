# nusB notes

## 2026-07-10

- `just fetch-gene` could not populate nusB because UniProt REST returned HTTP 500; `nusB-uniprot.txt` is explicitly marked as fallback context [file:PSEPK/nusB/nusB-uniprot.txt "CC   -!- CAUTION: Minimal fallback context assembled from projects/P_PUTIDA/data/psepk_uniprot_metadata.tsv because UniProt REST returned HTTP 500 on 2026-07-10."].
- Routed this gene out of the translation/RNA-processing umbrella into transcription/RNA-polymerase spillover context.
- Core interpretation: nusB encodes the NusB transcription antitermination factor in Pseudomonas putida KT2440. It is a soluble RNA-binding transcription factor for ribosomal RNA operon antitermination, not a translation factor.
- Asta was run as fast retrieval context and is recorded as provenance only [file:PSEPK/nusB/nusB-deep-research-asta.md "  uniprot_accession: Q88QH5"] .
