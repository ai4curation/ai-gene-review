# PIKFYVE (horse, A0A3Q2HE51) sequence comparison with human and mouse PIKFYVE

Script: `compare_orthologs.py` (run as `uv run --script compare_orthologs.py .`, 2026-10-21).
Inputs are the UniProt flat files A0A3Q2HE51.txt, Q9Y2I7.txt and Q9Z1T6.txt downloaded by the script into this folder.
Raw output: `results.json`. Global alignment, BLOSUM62, gap open -10, extension -0.5.

## Phylogenetic placement

UniProt places the horse entry in PANTHER PTHR46715:SF1, the single subfamily of the PIKfyve family, which is also the subfamily of human Q9Y2I7 and mouse Q9Z1T6 (interpro/panther/PTHR46715/PTHR46715-entries.csv). The IBA rows on this entry come from PAINT nodes PTN002928511 and PTN002928512 with human Q9Y2I7 and mouse MGI:1335106 as donors. Orthology to human/mouse PIKFYVE rests on this placement, not on the similarity scores below.

## Results

- Human Q9Y2I7 (2098 aa) vs horse (2108 aa): 2095 paired residues, 92.89% identity among paired residues; coverage 99.86% of human and 99.38% of horse.
- Mouse Q9Z1T6 (2097 aa) vs horse: 2094 paired residues, 91.31% identity among paired residues; coverage 99.86% of mouse and 99.34% of horse.
- All eight FYVE zinc-ligand cysteines of human PIKFYVE (Cys-164, 167, 180, 183, 188, 191, 210, 213) are conserved in horse (horse Cys-174, 177, 190, 193, 198, 201, 220, 223).
- Human Lys-1877, whose K1877E mutation abolishes PtdIns3P 5-kinase activity and autophosphorylation (human UniProt MUTAGEN feature, PMID:33098764), aligns to horse Lys-1887.
- Human Ser-2053, the regulatory autophosphorylation site tested by S2053A/S2053E (PMID:33098764), aligns to horse Ser-2063.

## Interpretation

The horse entry is a full-length PIKFYVE gene model: it covers the FYVE finger, DEP domain, chaperonin-like region and the C-terminal PIPK catalytic domain (UniProt domain PIPK 1768-2094), with the conserved catalytic lysine (horse Lys-1887), the regulatory Ser-2063 and the complete FYVE zinc-ligand set. Its 10-residue length excess over human lies N-terminal to the FYVE finger: the horse position of every checked residue, from Cys-164 to Ser-2053, is offset by +10. Nothing in the sequence suggests loss of the catalytic or membrane-targeting machinery.
