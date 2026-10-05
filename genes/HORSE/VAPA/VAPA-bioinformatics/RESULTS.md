# VAPA: human–horse sequence comparison

Global alignment of cached UniProt sequences gives **245/249 identical paired residues (98.4%)**. Paired coverage is 100.0% of human Q9P0L0 (249 aa) and 84.7% of horse A0A3Q2H1L9 (294 aa).

Reproduce from the repository root with `uv run python genes/HORSE/VAPA/VAPA-bioinformatics/align.py` (Biopython). The full alignment is in `alignment.txt`; sequence hashes and scoring parameters are in `results.json`.

This measures conservation between the identified records. It is not a reciprocal orthology analysis and does not itself validate a functional annotation. Interpret it alongside locus identifiers, domain architecture and primary literature. The sequences are current cached UniProt records, not independently recovered prediction-time inputs.

## Human feature correspondence

These mappings report sequence conservation only; they do not validate targeting, activity or annotation transfer.

| Human feature | Human positions | Paired horse positions | Identical / paired |
|---|---|---|---|
| TRANSMEM | 228–248 | 273,274,275,276,277,278,279,280,281,282,283,284,285,286,287,288,289,290,291,292,293 | 21/21 |
