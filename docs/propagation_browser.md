# Homology propagation browser

Open [the propagation browser](../app/propagation/index.html) to explore GO
annotations that a gene received from *other* gene products. It is the browser
for the [Propagation by Homology](../projects/HOMOLOGY_PROPAGATION.md) collection.

## What a row is

One row per GOA annotation whose evidence is a transfer:

| Included | Evidence · reference |
|---|---|
| Orthology transfers | ISO (GO_REF:0000119, 0000096, 0000121, 0000008, 0000024, or a PMID) |
| Curator similarity transfers | ISS / ISA (GO_REF:0000024, 0000113, 0000114, or a PMID) |
| Phylogenetic inference | IBA (GO_REF:0000033) |
| Electronic orthology | IEA via Ensembl Compara (GO_REF:0000107), TreeGrafter (GO_REF:0000118), and Combined IEA (GO_REF:0000120) rows whose WITH/FROM carries an Ensembl or PANTHER source |

Each row is read as **donor(s) → intermediate → target**:

- **Donor** — the gene product(s) named in WITH/FROM. For ISO/ISS/ISA and
  Compara the donor is resolved to a symbol and species (UniProt, or RGD's own
  API for non-rat RGD genes). For IBA the donors are the PAINT seed genes; they
  are listed but not individually resolved.
- **Intermediate** — the PANTHER node (`PTN…`) for IBA and TreeGrafter; for
  the other methods the orthology call itself, named by the method.
- **Target** — the annotated gene, linked to its review page.

## Columns and facets

- **Donor support** — what the donor carries *today* for the exact term, from
  QuickGO at the donor-cache date: `EXPERIMENTAL`; `INFERRED_ONLY` (the donor's
  own support is inferred, typically a transfer of a transfer); `ABSENT` (checked,
  the donor no longer has the term — a stale transfer); `NOT_CHECKED`.
- **Donor vs target symbol** — `DIFFERENT_SYMBOL` flags a donor that is not the
  target's namesake, which is where paralog sourcing shows up (rat Calm1 donating
  to mouse Calm3; human ANG donating to mouse Ang2). It is a prompt to check,
  not a verdict: nomenclature can differ between true orthologs.
- **IBA on target / Experimental on target** — the closest annotation of that
  kind on the same target, using the GO is_a/part_of closure: `SAME`,
  `MORE_SPECIFIC` (already entails this row), `MORE_GENERAL` (this row adds
  specificity), or `NONE` (this row is a new assertion). Filter ISO with
  `IBA on target = NONE` to see what ISO adds beyond PAINT.
- **Review** — the matching `existing_annotations` entry's action, summary,
  reason, and any `propagation_review` root cause and failure modes.

Search, filters, and page state are kept in the URL, so a selection can be
linked from a project page. Examples:

- [ISO rows sourced from a differently named donor](../app/propagation/index.html?evidence=ISO&symbol_match=DIFFERENT_SYMBOL)
- [ISO rows whose donor no longer carries the term](../app/propagation/index.html?evidence=ISO&donor_support=ABSENT)
- [ISO rows with no related IBA on the target](../app/propagation/index.html?evidence=ISO&iba_on_target=NONE)
- [Transfers reviewed as `PROPAGATION_BAD`](../app/propagation/index.html?root_cause=PROPAGATION_BAD)

**Download TSV** exports the filtered rows.

## Rebuilding

```bash
just refresh-propagation-sources   # network; updates projects/HOMOLOGY_PROPAGATION/data/
just deploy-propagation-browser    # offline; writes app/propagation/
just propagation-stats             # offline; writes projects/HOMOLOGY_PROPAGATION/propagation-stats.md
```

The refresh step caches donor identities (`donor-entities.tsv`), the donor's
current annotations for each transferred term (`donor-annotations.tsv`, with the
checked pairs in `donor-annotations-checked.tsv`), and the GO ancestor closure
restricted to terms in the corpus (`term-ancestors.tsv`). It reuses existing
cache rows; `--force` refetches everything. The build step reads only local
files. `just build-pages` rebuilds the browser, and Pages staging copies the
gene review pages the rows link to (`source-files.json`).

Strings are interned and donor records deduplicated in `data.js`, so the
payload is roughly 17 MB uncompressed and about 3.5 MB gzipped, similar to the
prediction browser.
