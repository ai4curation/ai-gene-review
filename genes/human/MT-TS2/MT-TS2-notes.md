# MT-TS2 notes

## Identity

- HGNC:7498, "mitochondrially encoded tRNA-Ser (AGU/C) 2"; RNAcentral URS00002C130C (HGNC cross-reference, resolved via the HGNC
  REST API: `curl -H 'Accept: application/json' https://rest.genenames.org/fetch/symbol/MT-TS2`
  returns `rna_central_id: ["URS00002C130C"]`). This is the corroboration for the
  `id: URS00002C130C_9606` in the review, whose GOA file is header-only and so carries no
  cross-reference of its own, and whose cached `MT-TS2-rnacentral.json` holds publications
  and `length` but no gene cross-reference.
- Gene product type: transfer RNA (no UniProt entry). Cached RNAcentral record length
  59 nt. Files fetched with `ai-gene-review fetch-ncrna human MT-TS2 -r URS00002C130C_9606`.
- Decodes the serine AGY (AGU/AGC) codons under the vertebrate mitochondrial genetic code.
  Only AGY: AGA and AGG are stops in the vertebrate mitochondrial code. At 59 nt this is the
  shortest human mt-tRNA, lacking a full D-arm.

## GOA

The GOA file is header-only: RNAcentral/Rfam2GO coverage does not reach this sequence, so
the review proposes the adaptor activity and mitochondrial translation terms as `NEW`
rather than reviewing existing rows. Length alone does not identify a tRNA - it is unique among the mt-tRNAs reviewed here, but
that is a property of this subset rather than of the 22 human mt-tRNAs. So the HGNC
cross-reference above, rather than the cached record, is what ties this id to this gene.
