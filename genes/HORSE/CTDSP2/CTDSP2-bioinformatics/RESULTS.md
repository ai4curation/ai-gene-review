# CTDSP2: human–horse sequence comparison

Global alignment of cached UniProt sequences gives **97/170 identical paired residues (57.1%)**. Paired coverage is 62.7% of human O14595 (271 aa) and 97.7% of horse F7A4N8 (174 aa).

Reproduce from the repository root with `uv run python genes/HORSE/CTDSP2/CTDSP2-bioinformatics/align.py` (Biopython). The full alignment is in `alignment.txt`; sequence hashes and scoring parameters are in `results.json`.

This measures conservation between the identified records. It is not a reciprocal orthology analysis and does not itself validate a functional annotation. Interpret it alongside locus identifiers, domain architecture and primary literature. The sequences are current cached UniProt records, not independently recovered prediction-time inputs.

## Human feature correspondence

These mappings report sequence conservation only; they do not validate targeting, activity or annotation transfer.

| Human feature | Human positions | Paired horse positions | Identical / paired |
|---|---|---|---|
| ACT_SITE | 107–107 | unaligned/deleted | 0/0 |
| ACT_SITE | 109–109 | unaligned/deleted | 0/0 |
| BINDING | 107–107 | unaligned/deleted | 0/0 |
| BINDING | 109–109 | unaligned/deleted | 0/0 |
| BINDING | 218–218 | 117 | 0/1 |
