# ARFGEF2 (BIG2) provenance analyses

Reproducible checks supporting `genes/human/ARFGEF2/ARFGEF2-ai-review.yaml`.
Everything is fetched live from the UniProt and QuickGO REST APIs; nothing is
hardcoded. Responses are cached under `cache/` (git-ignored, disposable).

## Scripts

| script | what it answers |
|---|---|
| `uniprot.py` | shared REST helpers (UniProt entry/search, QuickGO term + annotation search) |
| `resolve_withfrom.py` | resolves every WITH/FROM token in `ARFGEF2-goa.tsv` to a named protein, and builds `supporting_entities` **from the GOA file** rather than by hand |
| `provenance_audit.py` | the rat-donor funnel, the per-reference paralog check, the projection discriminator, and the literature coverage gap |
| `audit_claims.py` | lint: re-checks that the numbers asserted in `RESULTS.md`, `ARFGEF2-notes.md` and the review YAML still match `provenance_audit.json`, and that the review's `supporting_entities` still match the GOA WITH/FROM column |

## Running

```bash
cd genes/human/ARFGEF2/ARFGEF2-bioinformatics
uv run --no-project --with requests --with pyyaml python resolve_withfrom.py
uv run --no-project --with requests --with pyyaml python provenance_audit.py
uv run --no-project --with requests --with pyyaml python audit_claims.py
uv run --no-project --with requests --with pyyaml python audit_claims.py --self-test
```

`--self-test` deliberately breaks each invariant and asserts the guard fires. It
asserts the target string is present **before** mutating, so a guard cannot
"pass" against a mutation that silently no-opped.

## Design notes (each one is a trap this campaign has actually hit)

- **`size>=2` on every identifier lookup.** A `size=1` query turns an ambiguous
  cross-reference into a confident wrong answer. `resolve_mod_id` returns all
  hits and `withfrom_resolved.tsv` reports `n_hits`.
- **`entryType.startswith("UniProtKB reviewed")`**, never `"reviewed" in ...` —
  "reviewed" is a substring of "unreviewed", so the naive test silently promotes
  every TrEMBL entry to Swiss-Prot.
- **Dead-accession guard.** Every resolved accession must return an entry name;
  a deleted UniProt entry returns no annotations and is otherwise
  indistinguishable from an entity that genuinely has none.
- **Anti-truncation compares `numberOfHits` to `len(results)`**, never to a
  page-size constant, because a service that clamps `limit` instead of erroring
  would sail past a constant-based guard.
- **A too-large reference is data, not a missing input.** Three proteome-scale
  screens exceed QuickGO's pagination ceiling; they are reported with
  `entities_available: false` and `n_entities: null` rather than with a number
  derived from one page. Their subject/paralog counts stay exact because those
  come from targeted `geneProductId x reference` queries.
- **Entities are a distinct set of gene-product ids**, never an annotation
  total — one entity can hold several annotations for one term.
