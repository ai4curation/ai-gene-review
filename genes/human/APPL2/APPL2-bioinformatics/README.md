Sequence analyses supporting the human APPL2 (Q8NEU8) GO annotation review.

- `appl_orthology.py` — fetches APPL1/APPL2 sequences for human and mouse live from
  UniProt, computes pairwise global identities, and checks the residue-level claims
  made in the review (PH-domain basic patch, putative NLS, BAR/PH/PID domain spans).

Run with `uv run python appl_orthology.py`. Results are written to
`appl_orthology.tsv` and summarised in `RESULTS.md`.
