# Donkey SLC16A11 (A0A8C4PS96) vs human MCT11 (Q8NCK7)

Script: `align_to_human.py` (PEP 723; Biopython PairwiseAligner, global alignment with free end gaps, BLOSUM62, gap open -10, extend -0.5).
Command (repo root): `uv run --script genes/EQUAS/SLC16A11__A0A8C4PS96/SLC16A11__A0A8C4PS96-bioinformatics/align_to_human.py`
Inputs: the cached UniProt flat files `SLC16A11__A0A8C4PS96-uniprot.txt` and `genes/human/SLC16A11/SLC16A11-uniprot.txt`.
Output: `results.json` (all numbers below come from it).

## Results

- All 447 residues of human Q8NCK7 align to the donkey entry, with 90.6% identity over the aligned pairs.
- Human Met1 corresponds to donkey residue 74, also a Met. The donkey model therefore carries a 73-residue N-terminal extension before the position of the human start codon.
- Human UniProt (Q8NCK7) predicts 12 transmembrane helices; the donkey entry has 10 Phobius-predicted helices. Over the 12 human helix segments, 81-95% of positions are identical in donkey, so all twelve helices of the MFS fold are present in the donkey sequence even where Phobius did not call them.

## Interpretation

A0A8C4PS96 encodes a complete MCT11 transporter core. The 73-residue N-terminal extension is probably a gene-model artefact (upstream in-frame start): human UniProt flags three human cDNAs with "Erroneous initiation; Extended N-terminus" for Q8NCK7, and the donkey Met74 aligns with human Met1. This was not tested experimentally. The analysis says nothing about substrate specificity beyond what the high identity and shared PANTHER subfamily (PTHR11360:SF80, MONOCARBOXYLATE TRANSPORTER 11) imply.
