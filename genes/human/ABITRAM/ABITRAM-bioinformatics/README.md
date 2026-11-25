# Bioinformatics Analysis: human ABITRAM / PANTHER:PTHR13651

Reproducible global Needleman-Wunsch pairwise sequence identity computation across the eight `PANTHER:PTHR13651` (`PTHR13651:SF0`) orthologs referenced in the `PTHR13651` family review and six metazoan gene reviews.

## Run

```bash
PYTHONPATH=src UV_PROJECT_ENVIRONMENT=/Users/cjm/repos/ai-gene-review/.venv \
  UV_NO_SYNC=1 UV_FROZEN=1 PYTHONDONTWRITEBYTECODE=1 \
  /Users/cjm/repos/ai-gene-review/.venv/bin/python \
  genes/human/ABITRAM/ABITRAM-bioinformatics/pairwise_identity.py
```

Outputs `RESULTS.md` directly from cached `genes/*/*/*-uniprot.txt` records and `inputs/non_chordate_outgroups.fasta` (cross-checked against `.cache/uniprot_seq/`).
