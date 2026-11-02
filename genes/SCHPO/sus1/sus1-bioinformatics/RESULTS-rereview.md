# sus1 (Q7LL15) sequence comparison, 2026-10-21 re-review

Script: `compare_sequences_rereview.py` (PEP 723; `uv run --script compare_sequences_rereview.py`).
Raw output: `compare_sequences_rereview.out`. Sequences were fetched live from UniProt.

## Phylogenetic placement

UniProt places Q7LL15, S. cerevisiae SUS1 (Q6WNK7) and human ENY2 (Q9NPA8) in PANTHER family PTHR12514 with no subfamily assignment for any of the three. The PAINT ancestral node PTN000282153, which gives the target its IBA rows, has fission yeast, budding yeast, fly, Arabidopsis and human members among its descendant evidence. Function transfer from budding yeast Sus1 therefore rests on shared descent within one PAINT clade, not only on a best hit.

## Pairwise global alignment (BLOSUM62, gap open -10, extend -0.5)

- Q7LL15 (108 aa) vs S. cerevisiae SUS1 Q6WNK7 (96 aa): 25/96 identical aligned columns (26.0%).
- Q7LL15 (108 aa) vs human ENY2 Q9NPA8 (101 aa): 30/94 identical aligned columns (31.9%).

Q7LL15 is full length relative to both orthologs. Its extra length is a C-terminal extension of about 10 residues (PESANGGNKM) that has no counterpart in either ortholog. It is not a fragment.

## Mapping of budding-yeast Sus1 interaction mutants (PMID:19269973) onto S. pombe

| allele | S. cerevisiae residue | S. pombe residue |
|---|---|---|
| sus1-10 | E18 | E21 |
| sus1-10 | S19 | T22 |
| sus1-10 | G20 | G23 |
| sus1-11 | G37 | G40 |
| sus1-11 | W38 | W41 |
| sus1-12 | V73 | I76 |
| sus1-12 | D75 | D78 |

The sus1-11 residues G37/W38 align to G40/W41 in S. pombe, part of the conserved CGW motif also present in human ENY2. In budding yeast, mutating these residues impairs binding to both Sac3 (TREX-2) and Sgf11 (SAGA). The sus1-10 and sus1-12 positions, which affect only TREX-2 binding, are identical or conservatively substituted in S. pombe (S to T, V to I). This is consistent with fission yeast Sus1 keeping both binding interfaces. It does not show that the fission yeast protein actually binds TREX-2; that has not been tested directly in fission yeast.
