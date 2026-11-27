# NOL4 ortholog/paralog comparison

Script: `compare_orthologs.py` (raw output in `results.txt`). Sequences and PANTHER
assignments are fetched live from UniProt REST; identity is over aligned positions of a
global BLOSUM62 alignment (gap open -10, extend -0.5).

| Comparison | PANTHER subfamily of partner | Identity |
|---|---|---|
| human NOL4 (O94818, PTHR12449:SF17) vs mouse Nol4 (P60954) | PTHR12449:SF17 | 93.6% (452/483 aligned positions) |
| human NOL4 vs human NOL4L (Q96MY1) | PTHR12449:SF19 | 62.1% (246/396 aligned positions) |

Interpretation: mouse Nol4 is in the same PANTHER subfamily (SF17) as human NOL4 and is
93.6% identical over its full length, consistent with 1:1 orthology; findings on mouse
Nol4 can be considered for transfer to human NOL4 at ortholog level. NOL4L is a paralog
in a separate subfamily (SF19), so NOL4L-specific findings (e.g. its leukemia fusions or
CtBP interactions) should not be transferred. No phylogenetic tree was built here.
PAN-GO lists 0 GO annotations from evolutionary models for O94818 (no PAINT/IBA node).
