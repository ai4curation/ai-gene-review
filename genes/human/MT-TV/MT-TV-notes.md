# MT-TV notes

## Identity

- HGNC:7500, "mitochondrially encoded tRNA-Val (GUN)"; RNAcentral URS00002D2D8F (HGNC cross-reference, resolved via the HGNC
  REST API: `curl -H 'Accept: application/json' https://rest.genenames.org/fetch/symbol/MT-TV`
  returns `rna_central_id: ["URS00002D2D8F"]`). This is the corroboration for the
  `id: URS00002D2D8F_9606` in the review, whose GOA file is header-only and so carries no
  cross-reference of its own, and whose cached `MT-TV-rnacentral.json` holds publications
  and `length` but no gene cross-reference.
- Gene product type: transfer RNA (no UniProt entry). Cached RNAcentral record length
  69 nt. Files fetched with `ai-gene-review fetch-ncrna human MT-TV -r URS00002D2D8F_9606`.
- Decodes all four valine GUN codons under the vertebrate mitochondrial genetic code.

## GOA

The GOA file is header-only: RNAcentral/Rfam2GO coverage does not reach this sequence, so
the review proposes the adaptor activity and mitochondrial translation terms as `NEW`
rather than reviewing existing rows. Length alone does not identify a tRNA: among the mt-tRNAs reviewed here MT-TV's length is
shared with MT-TH and MT-TS1. So the HGNC cross-reference above, rather than the cached record, is what
ties this id to this gene.
