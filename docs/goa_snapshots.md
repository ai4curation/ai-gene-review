# Validating retained GOA snapshots

A review can retain historical source assertions while adding current ones. When their source tuples differ, replacing the fetched `GENE-goa.tsv` would lose provenance and validating against only that older file would reject genuine additions.

The ordinary gene validator can opt in to multiple immutable snapshots through a sibling `GENE-goa-snapshots.yaml`. The original `GENE-goa.tsv` remains mandatory and must be the first entry. Additional TSVs contain authentic source projections, never rows generated from the review itself.

```yaml
version: 1
gene_product_db: UniProtKB
gene_product_id: P02751
taxon_id: NCBITaxon:9606
snapshots:
  - path: FN1-goa.tsv
    sha256: 7e0023a7148b26931db494d46d04c6ae0be3c7c9e8259fe4cbb7fd135c254ed5
    role: original
    provenance: Original fetched repository snapshot; retain its exact bytes.
  - path: FN1-goa-20261031.tsv
    sha256: c622a2e533c8e864b96488997c16b0e2e0a50e6dbf6225a1fe3029896a693c53
    role: additive
    provenance: Repository TSV projection of the separately preserved current QuickGO response.
```

The manifest accepts exactly these keys. Version must be the integer `1`; hashes must be lowercase SHA256 strings. Duplicate mapping keys, duplicate source paths, unknown keys, missing provenance, invalid roles and missing files fail validation. Paths must be sibling TSV filenames; symlinks escaping the gene directory are rejected. Each nonempty snapshot must use the repository's 16-column GOA header and complete rows, with the declared database namespace, accession and taxon. Target isoform accessions may occur under a canonical target accession. The manifest accession and taxon must match the review. Both numeric and `NCBITaxon:`-prefixed taxon values are accepted in the TSV.

Hashes verify integrity, not authenticity. Keep the original response, retrieval/projection provenance and any historical source evidence available for review. The FN1 context archive preserves both complete TSV texts and their parsed headers/rows as well as the original QuickGO contexts. The manifest does not fetch or rewrite anything.

The loader concatenates source records in memory and uses the existing strict matcher. Every source tuple must be represented, and every ordinary reviewed tuple must have a source. Exact duplicate source records can share one review decision; different complete WITH/FROM lists remain distinct. For example, FN1's older heart-development IBA has four donors and its current source has three. Both authenticated contexts are retained separately, without widening the current record, exploiting a wildcard or calling either `NEW`. Source paths and physical line numbers accompany missing-source diagnostics from `validate-goa`.

The matcher retains its existing scope: GO term, evidence, reference, polarity and WITH/FROM coverage, including legacy empty-support compatibility and lossless whole-list unions. This is not a new check of all qualifiers, isoforms, extension conjunctions or source identity fields. Separate conservation checks remain necessary. A manifest also does not make an unsupported `NEW` assertion valid or weaken retirement semantics.

Without a manifest, single-file validation behaves as before. An explicit `validate-goa --goa PATH` remains a diagnostic against that single file and does not load a manifest. The default `validate` and `validate-goa` paths discover the sibling manifest automatically, so no `--no-goa` bypass is needed.

Existing CI path selection has a limitation: a change only to source TSVs or their manifest is not guaranteed to select the gene review for validation. This change does not alter workflow filters. Run ordinary validation explicitly for a source-only update; combined review and validation-code changes exercise the normal validation path and infrastructure checks.
