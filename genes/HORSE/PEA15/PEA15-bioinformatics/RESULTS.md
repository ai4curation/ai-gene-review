# PEA15: human–horse sequence comparison

Global alignment of cached UniProt sequences gives **130/130 identical paired residues (100.0%)**. Paired coverage is 100.0% of human Q15121 (130 aa) and 73.9% of horse A0A9L0RWM8 (176 aa).

Reproduce from the repository root with `uv run python genes/HORSE/PEA15/PEA15-bioinformatics/align.py` (Biopython). The full alignment is in `alignment.txt`; sequence hashes and scoring parameters are in `results.json`.

This measures conservation between the identified records. It is not a reciprocal orthology analysis and does not itself validate a functional annotation. Interpret it alongside locus identifiers, domain architecture and primary literature. The sequences are current cached UniProt records, not independently recovered prediction-time inputs.

## Human feature correspondence

These mappings report sequence conservation only; they do not validate targeting, activity or annotation transfer.

| Human feature | Human positions | Paired horse positions | Identical / paired |
|---|---|---|---|
