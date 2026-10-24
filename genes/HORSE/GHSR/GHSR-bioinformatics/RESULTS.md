# GHSR: human–horse sequence comparison

Global alignment of cached UniProt sequences gives **348/366 identical paired residues (95.1%)**. Paired coverage is 100.0% of human Q92847 (366 aa) and 100.0% of horse F6QF00 (366 aa).

Reproduce from the repository root with `uv run python genes/HORSE/GHSR/GHSR-bioinformatics/align.py` (Biopython). The full alignment is in `alignment.txt`; sequence hashes and scoring parameters are in `results.json`.

This measures conservation between the identified records. It is not a reciprocal orthology analysis and does not itself validate a functional annotation. Interpret it alongside locus identifiers, domain architecture and primary literature. The sequences are current cached UniProt records, not independently recovered prediction-time inputs.

## Human feature correspondence

These mappings report sequence conservation only; they do not validate targeting, activity or annotation transfer.

| Human feature | Human positions | Paired horse positions | Identical / paired |
|---|---|---|---|
| TRANSMEM | 41–66 | 41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66 | 25/26 |
| TRANSMEM | 73–96 | 73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96 | 23/24 |
| TRANSMEM | 118–139 | 118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139 | 22/22 |
| TRANSMEM | 163–183 | 163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183 | 20/21 |
| TRANSMEM | 212–235 | 212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235 | 23/24 |
| TRANSMEM | 264–285 | 264,265,266,267,268,269,270,271,272,273,274,275,276,277,278,279,280,281,282,283,284,285 | 22/22 |
| TRANSMEM | 303–326 | 303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324,325,326 | 24/24 |
| BINDING | 178–178 | 178 | 1/1 |
| BINDING | 181–181 | 181 | 1/1 |
| BINDING | 213–213 | 213 | 1/1 |
| BINDING | 214–214 | 214 | 1/1 |
| BINDING | 286–286 | 286 | 1/1 |
