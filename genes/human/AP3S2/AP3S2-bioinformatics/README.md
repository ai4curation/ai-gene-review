# AP3S2 bioinformatics

Supporting analyses for the human AP3S2 (P59780) GO annotation review.
Every script fetches live from public REST APIs (UniProt, QuickGO) and caches
responses under `cache/`, which is disposable. Nothing is hardcoded: delete
`cache/` and re-run to regenerate every number in `RESULTS.md`.

```
uv run python sigma_dileucine_pocket.py   # -> sigma_dileucine_pocket.tsv
uv run python resolve_withfrom.py         # -> withfrom_resolved.tsv
uv run python check_goa_reconciliation.py # GOA tsv <-> review YAML reconciliation
```
