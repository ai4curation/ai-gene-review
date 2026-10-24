# APLN-bioinformatics

Reproducible analyses supporting the GO annotation review of human APLN (apelin, Q9ULZ1).
Findings and their interpretation are in [RESULTS.md](RESULTS.md).

```
uv run python cterm_conservation.py       # apelin-13/-17 conservation, ACE2 motif, Phe77
uv run python resolve_withfrom.py         # resolve every GOA WITH/FROM entity
uv run python check_goa_reconciliation.py # GOA rows <-> review YAML entries must be a bijection
```

Everything is fetched live (UniProt, InterPro, RNAcentral) or read from files committed in
this repository (`APLN-goa.tsv`, `APLN-ai-review.yaml`,
`interpro/panther/PTHR15953/PTHR15953-paint.tsv`). HTTP responses are cached under
`cache/`, which is disposable and not committed — delete it and re-run to regenerate every
number in RESULTS.md. No result is hardcoded, and no failure is swallowed: the scripts
raise rather than fall back to a default.
