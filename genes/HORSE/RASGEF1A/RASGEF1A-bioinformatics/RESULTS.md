# RASGEF1A: horse (A0A9L0R5H6) vs human (Q8N9B8) sequence comparison

Script: `align_to_human.py` (PEP 723; run with `uv run --script align_to_human.py`).
Raw output: `alignment_output.txt`. Inputs: `../RASGEF1A-uniprot.txt` (horse, TrEMBL,
Ensembl ENSECAP00000056991.1) and `RASGEF1A-human-Q8N9B8-uniprot.txt` (human Swiss-Prot).

## Results

- Horse A0A9L0R5H6 is 529 residues; human Q8N9B8 is 481 residues.
- Global alignment (BLOSUM62, gap open -10, extend -0.5): 480 aligned pairs, 462 identical,
  96.25% identity; only 1 human residue unaligned.
- Human Met1 aligns to horse position 6; the horse model has a 5-residue N-terminal
  extension (MWEET) before the conserved start.
- The horse model carries a 44-residue insertion (horse 112-155,
  `GDSRGPGPPTVTRSWEEVTSSRHHFPALANLPVTERGQARDSFN`) relative to human,
  falling between human residues 106 and 107, i.e. inside the human N-terminal Ras-GEF (REM)
  domain boundary (41-170). No equivalent segment exists in the human canonical isoform.
  Whether it is a real horse-specific exon or a gene-model artefact cannot be decided from
  these data.
- Human REM domain (41-170): 130/130 residues covered, 94.6% identical.
- Human catalytic Ras-GEF (CDC25) domain (214-461): 248/248 residues covered, 98.0% identical.
- The C-terminus is complete (ends ...LRTTLLNRA, identical to human).

## Interpretation

A0A9L0R5H6 is the full-length horse RASGEF1A ortholog: both GEF domains are complete and the
catalytic domain is nearly identical to human. Both proteins are placed in PANTHER subfamily
PTHR23113:SF172 (RAS-GEF DOMAIN-CONTAINING FAMILY MEMBER 1A) by their UniProt records. The
gene model differs from human by a short N-terminal extension and an internal insertion in the
REM region, neither of which removes any annotated domain.
