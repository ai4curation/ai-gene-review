---
title: "CASPL_FAMILY working directory"
---

# CASPL_FAMILY working directory

Working files for the CASP-like (CASPL) family curation (see `../CASPL_FAMILY.md` for the overview).

- `bioinformatics/` — reproducible orthology/phylogeny analysis (Biopython only).
  - `orthology_analysis.py` — all-vs-all pairwise identity, reciprocal-best-hit orthology, NJ tree.
  - `data/caspl.fasta` — 54 UniProt sequences (20 POPTR + 34 ARATH CASPLs).
  - `data/accessions.tsv` — accession → species → Roppolo code map.
  - `results/` — `rbh_orthology.tsv`, `summary.json`, `caspl_nj_tree.nwk`.
  - `RESULTS.md` — written findings.

Regenerate the analysis:

```bash
cd bioinformatics
uv run orthology_analysis.py
```
