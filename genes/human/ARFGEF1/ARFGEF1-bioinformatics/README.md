# ARFGEF1 bioinformatics

Five scripts, all run from the **repo root** with the repo's own environment:

```bash
uv run python genes/human/ARFGEF1/ARFGEF1-bioinformatics/<script>.py
```

Nothing is hardcoded. Every number comes from a live UniProt / QuickGO / IntAct
call, or from a committed input file in the gene folder (`ARFGEF1-goa.tsv`,
`ARFGEF1-uniprot.txt`, `ARFGEF1-deep-research-affinage.md`,
`ARFGEF1-ai-review.yaml`). HTTP responses are cached under `cache/`, which is
gitignored and disposable — delete it and every figure is re-derived.

| script | what it answers | outputs |
|---|---|---|
| `uniprot.py` | shared REST helpers | — (imported) |
| `resolve_withfrom.py` | who is behind every WITH/FROM token, and what evidence does that donor itself carry for the propagated term? | `withfrom_resolved.tsv`, `supporting_entities.json`, `donor_evidence.tsv` |
| `check_terms.py` | is each term this review argues about current, merged, or absent — and what are the relevant children? | `term_status.json` |
| `partner_checks.py` | are the `GO:0005515` partners the canonical proteins, and how many *distinct* experiments support each? | `partner_checks.tsv` |
| `reference_scope.py` | how many entities does each supporting reference annotate, and with what? | `reference_scope.tsv`, `reference_annotations.tsv` |
| `literature_coverage.py` | which of ARFGEF1's primary papers have produced any GO annotation at all? | `literature_coverage.tsv` |
| `arfgef1_quotes.py` | is every quotation in the review YAML and the notes verbatim in its source? | — (exit status) |
| `check_goa_reconciliation.py` | does every GOA row map to exactly one review entry, with `supporting_entities` copied from the GOA field? | — (exit status) |

## Self-tests

Two scripts can silently return a plausible wrong answer if an upstream format
changes, so both carry a `--self-test` that breaks them on purpose:

```bash
uv run python genes/human/ARFGEF1/ARFGEF1-bioinformatics/partner_checks.py --self-test
uv run python genes/human/ARFGEF1/ARFGEF1-bioinformatics/arfgef1_quotes.py --self-test
```

`partner_checks.py`'s invariant is the one that matters: IntAct writes ids as
`"P05919 (uniprotkb)"`, not as bare accessions, so a naive equality test matches
nothing and every partner then reports "1 distinct experiment" — a number that
looks like an answer. The script asserts that grouping the subject's records by
partner accounts for *every* record, and raises on any record it cannot place.
That assertion fired on the first run and turned up four mRNA/miRNA CLASH rows
and a PI(3)P small-molecule pull-down that are not protein–protein interactions
at all.

`arfgef1_quotes.py` derives the repo root by walking up for a directory holding
both `src/` and `publications/`; it never asserts a path. A checker with a
hardcoded worktree path resolves quotes against the wrong cache and reports mass
false failures on clean work, which is worse than crashing.

## Reproducing the headline numbers

See `RESULTS.md`.
