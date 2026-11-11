# PIKFYVE (donkey, A0A8C4L106) sequence comparison with human, mouse and horse PIKFYVE

Analysis date: 2026-10-21. Reproduce from this folder with:

    uv run --script compare_orthologs.py .

The script (adapted from genes/HORSE/PIKFYVE/PIKFYVE-bioinformatics/compare_orthologs.py) downloads the UniProt flat
files for donkey A0A8C4L106, horse A0A3Q2HE51, human Q9Y2I7 and mouse Q9Z1T6 into this folder, runs global
alignments (BLOSUM62, gap open -10, extend -0.5) of each reference against the donkey entry, and reports identity
among paired residues, coverage, and the donkey residue aligned to selected human positions. Raw output: results.json.

## Evolutionary placement (the basis for transfer)

UniProt places the donkey entry in PANTHER PTHR46715:SF1, the single subfamily of the PIKfyve family, the same
subfamily as human Q9Y2I7, mouse Q9Z1T6 and horse A0A3Q2HE51 (DR PANTHER lines of the four downloaded flat files;
interpro/panther/PTHR46715/PTHR46715-entries.csv lists Q9Y2I7 and Q9Z1T6 in PTHR46715:SF1). A0A8C4L106 is the product
of the Ensembl canonical transcript ENSEAST00005004444 of donkey gene ENSEASG00005003072. Pairwise similarity below is
used only to check the gene model and conserved residues, not to establish orthology.

## Results

| Reference | Ref length | Paired | Identity (of paired) | Ref coverage | Donkey coverage |
|---|---|---|---|---|---|
| human Q9Y2I7 | 2098 | 2095 | 92.94% | 99.86% | 99.38% |
| mouse Q9Z1T6 | 2097 | 2094 | 91.36% | 99.86% | 99.34% |
| horse A0A3Q2HE51 | 2108 | 2108 | 99.72% | 100.00% | 100.00% |

The donkey entry is a full-length PIKFYVE gene model, covering 99.86% of human PIKFYVE.

All eight FYVE zinc-ligand cysteines of human PIKFYVE (Cys-164, 167, 180, 183, 188, 191, 210, 213) are conserved in
donkey (donkey Cys-174, 177, 190, 193, 198, 201, 220, 223).

Human Lys-1877, whose K1877E substitution abolishes lipid kinase activity and autophosphorylation (PMID:33098764),
aligns to donkey Lys-1887. Human Ser-2053, the regulatory autophosphorylation site (PMID:33098764), aligns to donkey
Ser-2063.

## Limits

No experiment has been done on donkey PIKFYVE. Conservation of these residues is consistent with, but does not
demonstrate, catalytic activity of the donkey protein.
