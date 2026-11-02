# MT-TC notes

## Identity

- HGNC:7477, "mitochondrially encoded tRNA-Cys (UGU/C)"; RNAcentral URS000018E119 (HGNC cross-reference, resolved via the HGNC
  REST API: `curl -H 'Accept: application/json' https://rest.genenames.org/fetch/symbol/MT-TC`
  returns `rna_central_id: ["URS000018E119"]`). This is the corroboration for the
  `id: URS000018E119_9606` in the review, whose GOA file is header-only and so carries no
  cross-reference of its own, and whose cached `MT-TC-rnacentral.json` holds publications
  and `length` but no gene cross-reference.
- Gene product type: transfer RNA (no UniProt entry). Cached RNAcentral record length
  66 nt. Files fetched with `ai-gene-review fetch-ncrna human MT-TC -r URS000018E119_9606`.
- Decodes the cysteine UGY (UGU/UGC) codons under the vertebrate mitochondrial genetic code.

## GOA

The GOA file is header-only: RNAcentral/Rfam2GO coverage does not reach this sequence, so
the review proposes the adaptor activity and mitochondrial translation terms as `NEW`
rather than reviewing existing rows. Length alone does not identify a tRNA - it is unique among the mt-tRNAs reviewed here, but
that is a property of this subset rather than of the 22 human mt-tRNAs. So the HGNC
cross-reference above, rather than the cached record, is what ties this id to this gene.
