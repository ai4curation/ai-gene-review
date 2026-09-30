# CAPSL: human–horse sequence comparison

Global alignment of cached UniProt sequences gives **202/208 identical paired residues (97.1%)**. Paired coverage is 100.0% of human Q8WWF8 (208 aa) and 92.4% of horse A0A3Q2I3U9 (225 aa).

Reproduce from the repository root with `uv run python genes/HORSE/CAPSL/CAPSL-bioinformatics/align.py` (Biopython). The full alignment is in `alignment.txt`; sequence hashes and scoring parameters are in `results.json`.

This measures conservation between the identified records. It is not a reciprocal orthology analysis and does not itself validate a functional annotation. Interpret it alongside locus identifiers, domain architecture and primary literature. The sequences are current cached UniProt records, not independently recovered prediction-time inputs.

## Human feature correspondence

These mappings report sequence conservation only; they do not validate targeting, activity or annotation transfer.

| Human feature | Human positions | Paired horse positions | Identical / paired |
|---|---|---|---|
| BINDING | 52–52 | 69 | 1/1 |
| BINDING | 54–54 | 71 | 0/1 |
| BINDING | 56–56 | 73 | 1/1 |
| BINDING | 58–58 | 75 | 1/1 |
| BINDING | 63–63 | 80 | 1/1 |
| BINDING | 88–88 | 105 | 1/1 |
| BINDING | 90–90 | 107 | 1/1 |
| BINDING | 92–92 | 109 | 1/1 |
| BINDING | 94–94 | 111 | 1/1 |
| BINDING | 99–99 | 116 | 1/1 |
