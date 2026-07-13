# rapA notes

## 2026-07-10

- `just fetch-gene` could not populate rapA because UniProt REST returned HTTP 500; `rapA-uniprot.txt` is explicitly marked as fallback context [file:PSEPK/rapA/rapA-uniprot.txt "CC   -!- CAUTION: Minimal fallback context assembled from projects/P_PUTIDA/data/psepk_uniprot_metadata.tsv because UniProt REST returned HTTP 500 on 2026-07-10."].
- Routed this gene out of the translation/RNA-processing umbrella into transcription/RNA-polymerase spillover context.
- Core interpretation: rapA encodes an RNA polymerase-associated Swi2/Snf2-family ATPase that stimulates RNA polymerase recycling and transcription regulation under stress conditions. Its translation/RNA-processing bucket placement reflects broad nucleic-acid/transcription keywords rather than a translation role.
- Asta was run as fast retrieval context and is recorded as provenance only [file:PSEPK/rapA/rapA-deep-research-asta.md "  uniprot_accession: Q88NR0"] .
