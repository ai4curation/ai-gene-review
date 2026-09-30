# ALG5: human–horse sequence comparison

Global alignment of cached UniProt sequences gives **278/294 identical paired residues (94.6%)**. Paired coverage is 90.7% of human Q9Y673 (324 aa) and 100.0% of horse A0A5F5PM72 (294 aa).

Reproduce from the repository root with `uv run python genes/HORSE/ALG5/ALG5-bioinformatics/align.py` (Biopython). The full alignment is in `alignment.txt`; sequence hashes and scoring parameters are in `results.json`.

This measures conservation between the identified records. It is not a reciprocal orthology analysis and does not itself validate a functional annotation. Interpret it alongside locus identifiers, domain architecture and primary literature. The sequences are current cached UniProt records, not independently recovered prediction-time inputs.

## Human feature correspondence

These mappings report sequence conservation only; they do not validate targeting, activity or annotation transfer.

| Human feature | Human positions | Paired horse positions | Identical / paired |
|---|---|---|---|
| TRANSMEM | 8–28 | 8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28 | 16/21 |
