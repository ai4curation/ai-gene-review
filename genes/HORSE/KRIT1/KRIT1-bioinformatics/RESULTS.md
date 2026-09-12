# KRIT1: human–horse sequence comparison

Global alignment of cached UniProt sequences gives **708/719 identical paired residues (98.5%)**. Paired coverage is 97.7% of human O00522 (736 aa) and 100.0% of horse A0A9L0SR44 (719 aa).

Reproduce from the repository root with `uv run python genes/HORSE/KRIT1/KRIT1-bioinformatics/align.py` (Biopython). The full alignment is in `alignment.txt`; sequence hashes and scoring parameters are in `results.json`.

This measures conservation between the identified records. It is not a reciprocal orthology analysis and does not itself validate a functional annotation. Interpret it alongside locus identifiers, domain architecture and primary literature. The sequences are current cached UniProt records, not independently recovered prediction-time inputs.

## Human feature correspondence

These mappings report sequence conservation only; they do not validate targeting, activity or annotation transfer.

| Human feature | Human positions | Paired horse positions | Identical / paired |
|---|---|---|---|
