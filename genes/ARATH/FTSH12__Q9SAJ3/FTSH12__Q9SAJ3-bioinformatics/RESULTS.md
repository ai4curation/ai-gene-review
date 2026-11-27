# FTSH12 (Q9SAJ3) catalytic motif check

Script: `motif_check.py` (run with `uv run --script motif_check.py`), reading the cached
UniProt record `FTSH12__Q9SAJ3-uniprot.txt` (1008 aa).

## Output

```
length	1008
Walker A (GxxxxGK[TS])	[(533, 'GPPGTGKT')]
Walker B (hhhhDE)	[(587, 'FVFVDE')]
M41 zinc motif (HExxH)	[(769, 'HEAGH')]
residue 769	H
residue 770	E
residue 773	H
residue 849	D
```

## Interpretation

- The AAA+ module retains a canonical Walker A motif (GPPGTGKT, 533-540) and Walker B
  motif (FVFVDE, 587-592), so ATP binding and hydrolysis are sequence-compatible.
- The M41 protease domain retains the HEAGH zinc motif at 769-773 and the third zinc
  ligand D849, matching the UniProt active-site/zinc-binding features.
- This is sequence capacity only. Kikuchi et al. 2018 (PMID:30309901) showed that an
  H769Y substitution in this motif fully complements the embryo-lethal ftsh12 knockout,
  so protease activity is not required for the essential function, and no FtsH12
  proteolytic substrate or ATPase rate has been measured.
