# UvrC (Q88FJ7, PP_4098) catalytic-residue conservation versus E. coli UvrC (P0A8G0)

Method: `residue_conservation.py` (Biopython global alignment, BLOSUM62, gap open -10,
extend -0.5) of the P. putida KT2440 UvrC sequence against E. coli UvrC, both read from
the cached UniProt flat files. Checked positions are the E. coli residues whose
substitution abolishes one incision (UniProt MUTAGEN features, PMID:10671556 and
PMID:1387639). The script first verifies that the reference carries the expected residue.
Raw output: `uvrC_vs_ecoli.txt`.

Command:

    python residue_conservation.py ../uvrC-uniprot.txt ../../../ECOLI/uvrC/uvrC-uniprot.txt \
      --site R42 --site D399 --site D438 --site D466 --site H538 \
      --region GIY-YIG:16-94 --region UVR:204-239 --region C-terminal_half:300-610

## Results

- Overall: 325 identical residues over the 610-residue E. coli sequence (53.3%); 601 reference positions aligned.
- 3' incision (GIY-YIG domain) catalytic residue E. coli R42 aligns to Q88FJ7 R42 (conserved).
- 5' incision (RNase H-like domain) catalytic residues E. coli D399, D438, D466, H538 align to Q88FJ7 D398, D437, D466, H534 (all conserved).
- GIY-YIG domain identity 58.2%; UVR (UvrB-interaction) domain identity 47.2%; C-terminal half identity 52.1%.

## Interpretation

Every residue experimentally required in E. coli for either the 3' or the 5' incision is
conserved in P. putida UvrC, so both nuclease active sites are predicted to be intact.
