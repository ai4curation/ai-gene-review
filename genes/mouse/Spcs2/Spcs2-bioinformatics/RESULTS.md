# Spcs2: A0A140LHW5 product versus canonical Spcs2 (Q9CYN2)

Selected A0A140LHW5 has 74 residues; reference Q9CYN2 has 226 residues.
The two sequences are identical over the first 66 residues; the remaining 8 residues of A0A140LHW5 are a different C-terminal tail.

Biopython PairwiseAligner global BLOSUM62, gap open -10, extension -0.5.

| Reference interval | Selected interval | Identical residues |
|---|---|---|
| 1-66 | 1-66 | 66 |
| 110-112 | 67-69 | 1 |
| 144-147 | 70-73 | 2 |
| 226-226 | 74-74 | 0 |

Reference features of Q9CYN2 and how much of each the selected product covers:

| Reference feature | Interval | Mapped / length | Identical |
|---|---|---|---|
| Topological domain: Cytoplasmic | 2-86 | 65 / 85 | 65 |
| Transmembrane: Helical | 87-107 | 0 / 21 | 0 |
| Topological domain: Lumenal | 108-111 | 2 / 4 | 0 |
| Transmembrane: Helical | 112-132 | 1 / 21 | 1 |
| Topological domain: Cytoplasmic | 133-226 | 5 / 94 | 2 |
| Region: Disordered | 1-37 | 37 / 37 | 37 |

Ensembl exon structures (minus strand, listed 5' to 3'):

- ENSMUST00000208465 (Spcs2-206, protein_coding, 74 aa): 99507971-99508106 (136 nt), 99498183-99498266 (84 nt), 99493907-99493966 (60 nt), 99488635-99489090 (456 nt)
- ENSMUST00000036274 (Spcs2-201, protein_coding, 226 aa): 99507971-99508184 (214 nt), 99498183-99498266 (84 nt), 99497506-99497666 (161 nt), 99493907-99494041 (135 nt), 99486776-99489090 (2315 nt)

Global alignment places isolated tail residues opposite distant reference positions; only the identical prefix is a genuine shared segment. A shared segment does not establish that the short product is expressed, folds, localizes to the ER membrane or joins the signal peptidase complex.

Reproduce with `UV_NO_SYNC=1 uv run python compare_sequences.py` from this directory.
