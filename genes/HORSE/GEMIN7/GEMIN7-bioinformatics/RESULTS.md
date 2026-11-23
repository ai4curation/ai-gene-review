# Horse GEMIN7 (A0A9L0T0I7) ortholog comparison

Script: `compare_orthologs.py` (run with `uv run --script compare_orthologs.py`; raw
output in `RESULTS-raw.txt`). Sequences fetched live from UniProt REST; global
Needleman-Wunsch alignment, BLOSUM62, gap open -10, extend -0.5.

## Placement

UniProt assigns A0A9L0T0I7 to PANTHER PTHR14679 (GEM-ASSOCIATED PROTEIN 7) and its only
subfamily PTHR14679:SF1, the same subfamily as human GEMIN7 Q9H840, mouse Gemin7 Q9CWY4,
bovine GEMIN7 Q17QA0 and S. pombe gem7 G2TRR1 (interpro/panther/PTHR14679 entries list).
The family has a single subfamily, so there is no subfamily split to worry about.

## Results

| accession | name | length | identical positions | identity over shorter seq |
|---|---|---|---|---|
| Q9H840 | human GEMIN7 | 131 | 116 | 88.5% |
| Q9CWY4 | mouse Gemin7 | 129 | 106 | 82.2% |
| Q17QA0 | bovine GEMIN7 | 125 | 109 | 87.2% |
| G2TRR1 | S. pombe gem7 | 91 | 25 | 27.5% |

Horse A0A9L0T0I7 is 131 aa, exactly the length of human GEMIN7, and aligns end to end
without internal gaps. Differences are concentrated in the N-terminal disordered,
Pro/Arg-rich segment (residues ~20-50); the C-terminal Sm-fold region (UniProt Sm domain
65-131) differs at only four positions. The RG/arginine-containing N-terminal region
that in human mediates SMN binding (Baccon et al. 2002) is retained
("LRLPRGPDGWSRGFAPDGRRAP").

## Conclusion

A0A9L0T0I7 is a full-length canonical GEMIN7 ortholog, not a fragment or isoform. The
fission yeast protein is a highly divergent family member (27.5% identity, 91 aa).
