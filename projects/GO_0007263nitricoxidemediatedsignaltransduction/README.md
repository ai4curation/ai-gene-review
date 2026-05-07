# GO:0007263 Nitric Oxide Mediated Signal Transduction Review

This is a **parallel project** under `projects/` for migrating annotations away from:

- `GO:0007263` nitric oxide mediated signal transduction
- `GO:0010749` regulation of nitric oxide mediated signal transduction
- `GO:0010750` positive regulation of nitric oxide mediated signal transduction
- `GO:0010751` negative regulation of nitric oxide mediated signal transduction

## Goal

Review experimental annotations currently using these terms and decide whether to:

- transfer to an existing GO term,
- remove as unsupported/over-annotated, or
- record an ontology gap / NTR request.

Experimental evidence filter is restricted to:

- `EXP`, `IDA`, `IPI`, `IMP`, `IGI`, `IEP`

## Quick start

From repository root:

```bash
just go7263-seed
```

This is cross-species by default (all organisms in local `genes/**/**-goa.tsv`).

This creates:

- `projects/GO_0007263nitricoxidemediatedsignaltransduction/reviews/GO_0007263-transfer-review.yaml`

Useful filters:

```bash
just go7263-seed --organism human
just go7263-seed --organism human --gene NOS2
just go7263-seed --all-evidence
```

To avoid dependence on locally fetched genes and run truly cross-species from QuickGO:

```bash
just go7263-seed-quickgo
just go7263-seed-quickgo --taxon 9606
just go7263-seed-quickgo --taxon 9606 --gene NOS2
```

## Output model

Each focal annotation includes:

- source GOA row fields,
- context from same gene (other references/terms),
- review fields for action + replacement term.

Review actions:

- `TRANSFER`
- `REMOVE`
- `MARK_AS_OVER_ANNOTATED`
- `UNDECIDED`
- `NTR`

## Notes

- Filesystem-safe project folder uses `_` instead of `:`.
- Scope here is annotation migration for one obsolete term, not whole-gene curation.
