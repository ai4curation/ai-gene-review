# APOOL-bioinformatics

Reproducible analysis supporting the human APOOL/MIC27 gene review.

```bash
UV_NO_WORKSPACE=1 uv run python loop_conservation.py
```

`loop_conservation.py` asks whether human APOOL retains the basic inter-transmembrane
loop of the MIC26/MIC27 family (PANTHER PTHR14564) that has been proposed to recruit
cardiolipin. It fetches the family's representative member sequences plus the
*Drosophila* PAINT seed from UniProt, asserts each length against
`interpro/panther/PTHR14564/PTHR14564-entries.csv`, reads the human transmembrane
boundaries from `../APOOL-uniprot.txt` rather than re-predicting them, aligns with
FAMSA and projects the human loop columns onto every member.

Findings are in `RESULTS.md`; the raw run output is `loop_conservation.out`.

`check_goa_reconciliation.py` is the review's self-audit. It checks that every row in
`../APOOL-goa.tsv` matches exactly one `existing_annotations` entry with identical term,
evidence code, reference, qualifier and normalized `supporting_entities`, that every term label
is GOA's rather than the reviewer's, that no action is
still `PENDING`, and that each `propagation_review` block's `source_entities` source ids are
exactly the row's `supporting_entities` — which is what keeps the two lists from drifting
apart when they are hand-edited. It prints the action and reference counts, so no number
quoted in the review or the PR has to be asserted rather than counted.

```bash
UV_NO_WORKSPACE=1 uv run python check_goa_reconciliation.py
```

This project is deliberately standalone (`UV_NO_WORKSPACE=1`) so that it does not have
to be registered in the repository root `pyproject.toml` workspace member list.
