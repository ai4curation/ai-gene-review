# MT-TM notes

## Identity

- HGNC:7492, "mitochondrially encoded tRNA-Met (AUA/G)"; RNAcentral URS000006E464 (HGNC
  cross-reference, resolved via the HGNC REST API: `curl -H 'Accept: application/json'
  https://rest.genenames.org/fetch/symbol/MT-TM` returns `rna_central_id:
  ["URS000006E464"]`). This is the corroboration for the `id: URS000006E464_9606` in the
  review, whose GOA file is header-only and so carries no cross-reference of its own, and
  whose cached `MT-TM-rnacentral.json` holds publications and `length` but no gene
  cross-reference.
- Gene product type: transfer RNA (no UniProt entry). Cached RNAcentral record length 68 nt.
  Files fetched with `ai-gene-review fetch-ncrna human MT-TM -r URS000006E464_9606`.
- Decodes the methionine codons AUG and AUA (AUR) under the vertebrate mitochondrial genetic
  code. AUA is methionine in this code rather than isoleucine, and reading it depends on
  5-formylcytidine at wobble position 34, installed by NSUN3 and ALKBH1.

## GOA

The GOA file is header-only: RNAcentral/Rfam2GO coverage does not reach this sequence, so the
review proposes the adaptor activity and mitochondrial translation terms as `NEW` rather than
reviewing existing rows. Length alone does not identify a tRNA: among the mt-tRNAs reviewed
here MT-TM's length is shared with MT-TW. So the HGNC cross-reference above, rather than the
cached record, is what ties this id to this gene.

## Why GO:0070124 is not listed

MT-TM is the single methionine tRNA of human mitochondria, so it serves initiation as well as
elongation: it is the species MTFMT formylates and mtIF2 delivers to the ribosomal P site.
`GO:0070124` mitochondrial translational initiation is nonetheless not added to the core
function alongside `GO:0032543` mitochondrial translation, because it is a descendant of it
(`GO:0070124` is_a `GO:0006413` translational initiation and part_of `GO:0032543`, confirmed
with `runoak ancestors -p i,p`). Adding a child of a term the gene already carries is
redundancy rather than coverage, and `GO:0032543` is the one term that spans both roles this
tRNA has - `GO:0070124` on its own would assert only the narrower one.
