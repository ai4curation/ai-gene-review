# Publication-Centric Annotation Review (Option 3 scaffold)

This subproject bootstraps an annotation-centric workflow **inside the existing monorepo**.

## Scope

- **Organization**: publication-based (one review file per reference, typically a PMID)
- **Context**: focal annotation + related annotations
  - same publication + same gene
  - same gene + same term across any reference
  - same publication + same term across other genes
- **Review focus**:
  - term correctness
  - supporting text quality

## Quick start

From repository root:

```bash
just pub-review PMID:23991106 PTPN22
```

Output is written to:

- `projects/publication_annotation_review/reviews/PMID_23991106-annotation-review.yaml`

Alternative review entrypoints:

```bash
just pub-review-org PMID:23991106 human
just pub-review-all PMID:23991106
just pub-review-quickgo PMID:23991106 --taxon 9606
```

Use `--max-annotations` for a smaller pilot file:

```bash
just pub-review-org PMID:23991106 human --max-annotations 25
```

For de novo candidate generation when no GOA/QuickGO annotations are available:

```bash
just fetch-pmid 23991106
just pub-denovo PMID:23991106 PTPN22
```

This creates:

- `projects/publication_annotation_review/reviews/PMID_23991106-PTPN22-denovo.yaml`

## Workflow

1. Generate publication-centric review YAML for a target reference.
2. For each `annotations[]` entry, fill in:
   - `review.term_correctness.decision` and rationale
   - `review.supporting_text_quality.*` fields
3. Fetch publication text if needed:
   - `just fetch-pmid 23991106`
4. Iterate and refine decisions.

## Command summary

- `just pub-list-refs <organism>`: list PMIDs found in local GOA files
- `just pub-review <PMID> <GENE>`: generate publication review filtered by gene symbol
- `just pub-review-org <PMID> <organism>`: generate publication review filtered by organism
- `just pub-review-all <PMID>`: generate publication review from all local GOA files
- `just pub-review-quickgo <PMID> [--taxon <id>] [--gene <symbol>]`: use QuickGO API instead of local GOA
- `just pub-denovo <PMID> <GENE>`: build de novo GO candidate assignments from publication text

| If you want to... | Use this command |
|---|---|
| Find candidate PMIDs already present in local GOA for one organism | `just pub-list-refs human` |
| Review one PMID for one known gene | `just pub-review PMID:23991106 PTPN22` |
| Review one PMID across all genes in one organism | `just pub-review-org PMID:23991106 human` |
| Review one PMID across all local GOA data | `just pub-review-all PMID:23991106` |
| Review a PMID without local GOA (query QuickGO directly) | `just pub-review-quickgo PMID:23991106 --taxon 9606` |
| Generate de novo GO candidates from publication text (no GOA/QuickGO annotations) | `just pub-denovo PMID:23991106 PTPN22` |

## Decision values (suggested)

For each review axis (`term_correctness`, `supporting_text_quality`), use one of:

- `ACCEPT`
- `MODIFY`
- `REMOVE`
- `UNDECIDED`

## Migration path to a new repository

When you are ready to split this into a standalone repo:

1. Copy `projects/publication_annotation_review/` as the new repo root.
2. Promote script into a package (`src/<new_pkg>/...`) and add CLI entrypoint.
3. Add dedicated schema + validation for publication review files.
4. Replace broad `genes/` scan with pluggable backends (local GOA cache, QuickGO API, database).
