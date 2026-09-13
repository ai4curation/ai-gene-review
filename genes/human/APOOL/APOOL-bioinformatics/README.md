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

This project is deliberately standalone (`UV_NO_WORKSPACE=1`) so that it does not have
to be registered in the repository root `pyproject.toml` workspace member list.
