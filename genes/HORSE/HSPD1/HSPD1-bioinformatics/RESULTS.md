# HSPD1: human–horse sequence comparison

Global alignment of cached UniProt sequences gives **527/541 identical paired residues (97.4%)**. Paired coverage is 94.4% of human P10809 (573 aa) and 100.0% of horse F6Z587 (541 aa).

Reproduce from the repository root with `uv run python genes/HORSE/HSPD1/HSPD1-bioinformatics/align.py` (Biopython). The full alignment is in `alignment.txt`; sequence hashes and scoring parameters are in `results.json`.

This measures conservation between the identified records. It is not a reciprocal orthology analysis and does not itself validate a functional annotation. Interpret it alongside locus identifiers, domain architecture and primary literature. The sequences are current cached UniProt records, not independently recovered prediction-time inputs.

## Human feature correspondence

These mappings report sequence conservation only; they do not validate targeting, activity or annotation transfer.

| Human feature | Human positions | Paired horse positions | Identical / paired |
|---|---|---|---|
| TRANSIT | 1–26 | 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26 | 20/26 |
| BINDING | 75–75 | 75 | 1/1 |
| BINDING | 111–115 | 111,112,113,114,115 | 5/5 |
| BINDING | 440–440 | 408 | 1/1 |
| BINDING | 520–520 | 488 | 1/1 |
