# Horse NDEL1 (A0A5F5PSW5) vs human NDEL1 (Q9GZM8)

Script: `compare_to_human.py` (PEP 723; run with `uv run --script compare_to_human.py`).
Raw output: `compare_to_human.out`. Sequences are read from the cached UniProt flat files
(`genes/HORSE/NDEL1/NDEL1-uniprot.txt`, `genes/human/NDEL1/NDEL1-uniprot.txt`).
Global alignment: Biopython PairwiseAligner, BLOSUM62, gap open -10, extend -0.5.

## Results

- Horse A0A5F5PSW5 is 481 aa; the human canonical NDEL1 is 345 aa.
- Horse residues 1-338 align to human residues 1-338 without gaps and differ at only 3 positions: horse S228 (human T228), horse M296 (human L296) and horse S298 (human G298).
- Of the 345 human residues, 338 are aligned and 338 are identical (98.0%).
- The human C-terminal tail 339-345 (GMLPLSV, which contains the phosphoserine at human S344) is absent from the horse model. In its place the horse model carries a 143-residue C-terminal extension (horse 339-481, beginning ATSFREPTLHQSW... and ending ...GLVALAQL) with no counterpart in human NDEL1, or in either of the two human alternative C-termini (VAR_SEQ 316-345). The donkey NDEL1 model (A0A9L0IJ72, also 481 aa) carries a near-identical extension, so the two equid models share the same gene-model structure.
- All functionally mapped human residues lie inside the conserved 1-338 block and are retained at identical positions: the self-association coiled coil (56-166), the LIS1-binding segment (114-133), the CDK1/CDK5/MAPK1 phospho-sites S215, T219, S231, S242 and T245, the DISC1-binding region (241-280), the centrosome-localization region (256-291) and the palmitoylated Cys273 (KLAACRNFAK motif at horse 269-278).

## Interpretation

A0A5F5PSW5 is the horse NDEL1 ortholog (PANTHER PTHR10921:SF0, the vertebrate NDEL1
subfamily; VGNC:20610). Its first 338 residues are essentially the human protein. The
C-terminal 143 residues most likely reflect an alternative or erroneous Ensembl gene model
(a different or read-through final exon) rather than a conserved protein region: nothing
comparable is present in human NDEL1 or its annotated isoforms, and no domain signature
matches it (UniProt reports only MobiDB-lite disorder over part of it). Whether horse cells
express this C-terminus is not established. The extension does not remove any mapped
functional site, so NDEL1 functions established in human, mouse and rat transfer to the
conserved 1-338 region.
