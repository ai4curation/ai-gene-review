# Hierarchical annotation facets

The annotation browser has Species and GO generic slim facets with **Hierarchy**
and **Most used** views. Expand arrows navigate independently of checkboxes.
Selecting a category matches the annotation terms or species underneath it,
including detailed GO terms that are not displayed in the slim. Category search
reveals matching nodes and their parent paths, with branches automatically open
and expand/collapse buttons hidden until the search is cleared. The existing
exact GO term facet is still available. The Species hierarchy replaces the flat
species-label facet; individual species remain selectable within it.

Selections within a facet use OR; different facets and text search use AND.
Counts show distinct annotation rows matching the other active filters, ignoring
that hierarchy's own selection so siblings remain available for further selection.
They are annotation counts, not unique gene counts. A child can appear under
multiple parents: those appearances share selection, and reaching an ancestor by
two paths never counts a row twice. Sibling counts consequently need not add up to
their parent's count. Selections survive URL sharing, reload, and back/forward;
TSV export uses the filtered rows.

This is navigation over the *terms in reviewed annotations*, not an assertion of
gene function. It includes negated and rejected annotations unless the user
filters them out with the existing Negated and Review Action facets.

## Build and sources

`just deploy-browser` and `just update-browser-data` generate hierarchical metadata
after exporting the rows and schema. The existing payload size target still
applies (`just deploy-browser pages` for an artifact build). Metadata is appended
to `app/schema.js`, so it works over `file://` and follows existing Pages staging
without a new runtime API or additional asset. `app/data.js` is not expanded with
per-row ancestry arrays.

To rebuild just the metadata from an existing JSON export:

```sh
uv run python -m ai_gene_review.tools.build_browser_hierarchies \
  --data exports/exported_annotations.json --schema app/schema.js
```

The first build downloads full `go-basic.obo` from the GO release service and
UniProt taxonomy records for the observed taxon IDs. Later builds reuse
`.cache/browser-hierarchies/`. The daily Pages workflow restores this directory
with `actions/cache` and saves newly encountered taxa under a fresh run key.
Bump the workflow's `browser-hierarchies-v1` prefix to refresh its source snapshot.
Downloads retry connection failures and HTTP 429/500/502/503/504 responses up to
three times with exponential backoff; permanent errors fail immediately. The
emitted provenance records the GO release,
SHA-256, subset (`goslim_generic`), traversed predicates, and source URLs. To use
a pinned GO release, provide `--go-obo /path/to/go-basic.obo`; to refresh the
sources, use a new `--cache-dir` (or remove the old cached sources).

The GO subset is read from actual `subset: goslim_generic` tags. The builder uses
the full ontology's `is_a` and `part_of` ancestry to project edges between nearest
displayed slim ancestors, preserving multiple parentage. It excludes `regulates`
and `has_part`. The three aspect roots are included; unused nodes are pruned.
Alternative IDs resolve to their active primary IDs. Unknown and obsolete IDs
remain visible as **Unmapped / obsolete GO terms**, without assuming replacements.
See the [GO subset guide](https://geneontology.org/docs/go-subset-guide/) and
[relation guidance](https://geneontology.org/docs/ontology-relations/).

Species grouping uses selected clade names from authoritative UniProt lineages;
the source supplies their IDs and parentage. All observed taxa remain selectable
leaves (or intermediate nodes if an observed taxon contains another). The selected
groups include Eukaryota, Opisthokonta, Metazoa, Fungi, Viridiplantae, Bacteria and
Archaea. Malformed existing identifiers are retained under **Unmapped taxa** and
produce a build warning. Their original identifiers are preserved verbatim, so
bare or wrongly prefixed IDs cannot overwrite the ancestry of valid taxa.
Network failures after the bounded retries, or unexpected ID redirects, fail the
build rather than silently emitting incomplete ancestry.

If a separately refreshed data payload contains source values absent from the
hierarchy metadata, the browser warns and groups those values under an explicit
unmapped category. They remain selectable and counted without inferred ancestry.

The component lives in `src/ai_gene_review/browser/index.html`. Hierarchies are
optional schema metadata; other consumers of this shared template retain their
flat facets. This first integration supplies data for the annotation browser.

## Verification

```sh
uv run pytest tests/test_browser_hierarchies.py
uv run pytest tests/test_browser_hierarchy_downloads.py
uv run pytest tests/test_browser_hierarchies_frontend.py -m integration
```

The browser tests use Chromium and local static files. They cover multiple-parent
selection, deduplicated counts, sibling counts, combined filters, URL state,
category search, view switching, filtered export, and mobile width.
Retry tests use a real local HTTP server with transient and persistent failures.
