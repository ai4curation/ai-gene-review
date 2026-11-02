# ATG3 (donkey A0A9L0J149): comparison to characterised ATG3 orthologs

Reproduce from this folder with:

    uv run --script compare_to_orthologs.py > compare_to_orthologs_output.txt

The script fetches the UniProt records of donkey A0A9L0J149, human Q9NT62, mouse Q9CPX6 and yeast P40344 (UniProt REST, run 2026-10-21), makes global BLOSUM62 pairwise alignments of each against the donkey protein, and maps the human Swiss-Prot functional features onto the donkey sequence. Raw output is in `compare_to_orthologs_output.txt`.

## Results

- Evolutionary placement: donkey A0A9L0J149, human Q9NT62, mouse Q9CPX6 and yeast P40344 are all classified by UniProt in PANTHER subfamily PTHR12866:SF2 (UBIQUITIN-LIKE-CONJUGATING ENZYME ATG3). The donkey protein is therefore in the same subfamily as the experimentally characterised ATG3 proteins, not in the ATG10 subfamily (PTHR12866:SF5).
- Identity: A0A9L0J149 is 314 residues, the same length as human ATG3, with 309 identical aligned residues to human Q9NT62 (98.4%) and 309 to mouse Q9CPX6 (98.4%); identity to yeast Atg3 is 112 residues (36.1% of the shorter sequence).
- Functional residues mapped from human ATG3 are all conserved in the donkey protein at the same positions: the N-terminal membrane-curvature-sensing amphipathic helix (4-19) including Lys9 and Lys11; the LIR motif (104-110, DGGWVDT); the caspase-8 LETD motif (166-169); the ATG12-acceptor Lys243; and the catalytic Cys264 that forms the glycyl thioester intermediate.
- The ATG12-interacting acidic region (human 140-170) differs at one position (human D148 vs donkey E148 in the acidic stretch EEEEDEDE/EEEEEEDE); it is a conservative acidic-to-acidic substitution.

## Limitations

This is sequence-level conservation only. It supports transfer of the E2 activity from mammalian orthologs in the same PANTHER subfamily, but no donkey ATG3 protein has been assayed experimentally.
