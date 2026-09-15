# MYL10: human–horse sequence comparison

Global alignment of cached UniProt sequences gives **166/192 identical paired residues (86.5%)**. Paired coverage is 85.0% of human Q9BUA6 (226 aa) and 90.6% of horse A0A9L0TJE1 (212 aa).

Reproduce from the repository root with `uv run python genes/HORSE/MYL10/MYL10-bioinformatics/align.py` (Biopython). The full alignment is in `alignment.txt`; sequence hashes and scoring parameters are in `results.json`.

This measures conservation between the identified records. It is not a reciprocal orthology analysis and does not itself validate a functional annotation. Interpret it alongside locus identifiers, domain architecture and primary literature. The sequences are current cached UniProt records, not independently recovered prediction-time inputs.

## Human feature correspondence

These mappings report sequence conservation only; they do not validate targeting, activity or annotation transfer.

| Human feature | Human positions | Paired horse positions | Identical / paired |
|---|---|---|---|
| BINDING | 97–97 | 83 | 1/1 |
| BINDING | 99–99 | 85 | 1/1 |
| BINDING | 101–101 | 87 | 1/1 |
| BINDING | 108–108 | 94 | 1/1 |
