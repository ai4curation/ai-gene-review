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

## What the union represents

For a review that opts into a snapshot manifest, the `existing_annotations` array audits source assertions that were actually observed. A historical assertion may still be assessed even when it is absent from the newest source response. The union is therefore not a claim that all rows remain in live GOA, and it is not a count of distinct biological functions. Each retained assertion still needs a scientific disposition; source retention does not turn its action into ACCEPT.

Record which review contexts occur in each snapshot. In FN1, the context companion identifies 223 typed current contexts from 222 raw records and eleven historical-only source contexts. The older and current heart-development donor groups represent the same ancestral function, and obsolete/current term identifiers can converge on the same replacement. Their distinct source tuples remain auditable; they are not independent replication or new biological assertions.

Only the ordinary review-validation paths described above load this manifest. Existing ETL, comparison and projection consumers that open GENE-goa.tsv directly retain their single-file behavior. Do not present their output as a union-aware export. The FN1 JSON companion is a local provenance aid for its complex reconciliation, not a repository-wide archive requirement or a new machine schema.

## Refreshing sources without losing the original

1. Run normal `fetch-gene` without `--force` when checking for updates. The fetcher preserves an existing GOA file and reports differences; it seeds GOA-derived annotations from that preserved file rather than silently replacing it with the new response. The command is not entirely read-only: fetched UniProt data can still add or repair alternative-product records.
2. Keep the original and every already declared snapshot byte-for-byte. Acquire a new genuine response and its repository TSV projection under a new dated sibling filename, recording the retrieval source, time, exact raw contexts and projection method. Do not generate source rows from the authored review.
3. Compare the new source assertions with the existing reviewed contexts, including complete support lists and the separately preserved qualifiers, isoforms and extension branches. Review genuinely distinct contexts individually. Add the new filename, its actual SHA256 and provenance to the manifest, and update the context-to-review mapping. A source-backed addition is not an authored NEW annotation.
4. Run ordinary validate and default validate-goa --strict for the complete review. Also check the fields outside the matcher's scope and the original-source/product/quotation conservation. For a source-only change, run these explicitly because current CI path selection is not guaranteed to select the gene.

A SHA mismatch is an integrity failure to investigate, not a request to replace the expected hash with whatever bytes are now on disk. If an explicit --force, manual edit or other operation overwrote a pinned snapshot, first preserve those new bytes and their real acquisition provenance under a separate filename. Recover the original bytes from the manifest's known source commit or preserved exact archive, verify the expected SHA256, and restore that original file. For example, after preserving the overwritten file and confirming the desired source commit, the following command restores the committed snapshot:

    git restore --source <accepted-commit> --worktree -- genes/<organism>/<gene>/<gene>-goa.tsv

Then process the genuine new data as an additive snapshot and rerun full review validation. Do not change an old manifest hash merely to make validation pass.

This refresh procedure deliberately leaves the original cache intact. Consumers needing a current-only or union export require an explicit separately reviewed output; neither view should be inferred from the presence of this manifest.
