# dksA notes

## 2026-07-10

- `just fetch-gene` could not populate dksA because UniProt REST returned HTTP 500; `dksA-uniprot.txt` is explicitly marked as fallback context [file:PSEPK/dksA/dksA-uniprot.txt "CC   -!- CAUTION: Minimal fallback context assembled from projects/P_PUTIDA/data/psepk_uniprot_metadata.tsv because UniProt REST returned HTTP 500 on 2026-07-10."].
- Routed this gene out of the translation/RNA-processing umbrella into transcription/RNA-polymerase spillover context.
- Core interpretation: dksA encodes an RNA polymerase-binding DksA transcription factor. The supported function is zinc-coordinated transcription regulation through direct RNAP binding, with cytoplasmic localization.
- Asta was run as fast retrieval context and is recorded as provenance only [file:PSEPK/dksA/dksA-deep-research-asta.md "  uniprot_accession: Q88DX5"] .
