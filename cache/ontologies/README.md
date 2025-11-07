# Ontology Term Cache

This directory contains cached ontology term metadata (ID → label mappings) used for fast, offline validation of gene review YAML files.

## Purpose

When ontologies evolve (labels change, terms become obsolete), YAML files with hardcoded labels can become invalid. This cache system provides:

1. **Stability**: YAML files don't break when ontologies update upstream
2. **Performance**: Fast validation (TSV lookup, no API calls)
3. **Offline capability**: Works without internet connection
4. **Reproducibility**: Old commits validate correctly (cache is versioned with them)

## Files

- `go.tsv` - Gene Ontology terms (id, label, is_obsolete, fetched_date)
- `go.meta.json` - Metadata about the GO cache (version, date, source)
- Additional ontology caches (chebi, uberon) as needed

## Workflow

### 1. Normal Development (Uses Cache)

```bash
# Validate files using cache (fast, offline)
just validate human TP53

# Validate all files
just validate-all
```

### 2. Update Cache (Monthly or as needed)

```bash
# Update GO cache
just update-cache go

# Update all ontology caches
just update-cache all
```

This scans all YAML files for term IDs, fetches current labels from OLS/OAK, and updates the cache TSVs.

### 3. Fix Labels After Cache Update

```bash
# Dry run - see what would change
just fix-labels

# Actually fix the labels
just fix-labels --write

# Fix specific file
just fix-labels genes/human/TP53/TP53-ai-review.yaml --write
```

## Cache Format

### TSV Format
```tsv
term_id	label	is_obsolete	fetched_date
GO:0007156	homophilic cell-cell adhesion	false	2025-10-29T12:00:00
GO:0098742	obsolete cell-cell adhesion via plasma-membrane adhesion molecules	true	2025-10-29T12:00:00
```

### Metadata Format
```json
{
  "ontology_id": "go",
  "version": null,
  "cache_date": "2025-10-29T12:00:00Z",
  "source": "OAK (sqlite:obo)",
  "term_count": 1986,
  "notes": "Only terms used in annotations"
}
```

## Design Principles

- **Sparse caching**: Only cache terms actually used in our annotations (~1,000s not ~100,000s)
- **Incremental updates**: Only fetch new terms when cache is updated
- **Multi-tier validation**: Cache → OAK → OLS API (fallback chain)
- **Version control**: Cache files are committed, ensuring reproducibility

## Maintenance

- Update cache monthly or when ontology updates are needed
- Review cache diffs in PRs to see what changed upstream
- Cache updates should be separate commits from label fixes
