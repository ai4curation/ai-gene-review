# MT-TW notes

## Identity

- HGNC:7501, "mitochondrially encoded tRNA-Trp (UGA/G)"; RNAcentral URS000012396D (HGNC cross-reference, resolved via the HGNC
  REST API: `curl -H 'Accept: application/json' https://rest.genenames.org/fetch/symbol/MT-TW`
  returns `rna_central_id: ["URS000012396D"]`). This is the corroboration for the
  `id: URS000012396D_9606` in the review, whose GOA file is header-only and so carries no
  cross-reference of its own, and whose cached `MT-TW-rnacentral.json` holds publications
  and `length` but no gene cross-reference.
- Gene product type: transfer RNA (no UniProt entry). Cached RNAcentral record length
  68 nt. Files fetched with `ai-gene-review fetch-ncrna human MT-TW -r URS000012396D_9606`.
- Decodes the tryptophan codons UGA and UGG under the vertebrate mitochondrial genetic code.
  UGA is tryptophan in the vertebrate mitochondrial code, not a stop codon as in the standard
  code, so this tRNA reads both UGR codons.

## GOA

The GOA file is header-only: RNAcentral/Rfam2GO coverage does not reach this sequence, so
the review proposes the adaptor activity and mitochondrial translation terms as `NEW`
rather than reviewing existing rows. Length alone does not identify a tRNA: among the mt-tRNAs reviewed here MT-TW's length is
shared with MT-TM. So the HGNC cross-reference above, rather than the cached record, is what
ties this id to this gene.
