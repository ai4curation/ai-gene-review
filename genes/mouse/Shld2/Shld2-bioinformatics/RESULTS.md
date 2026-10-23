# Mouse Shld2 (Q3UEN2) vs human SHLD2 (Q86V20): sequence comparison

Script: `compare_to_human.py` (BLOSUM62 global alignment, Biopython). Raw output: `compare_to_human.out`.
Inputs are the local UniProt files `genes/mouse/Shld2/Shld2-uniprot.txt`, `genes/human/SHLD2/SHLD2-uniprot.txt`
(835-aa displayed form, Q86V20-1) and `genes/human/SHLD2/SHLD2-isoform2.fasta` (904-aa long form, Q86V20-2).

## Results

- Mouse Shld2 is 891 aa. Against the human 904-aa long form, identity over aligned pairs is 0.672 (587/873).
- The N-terminal segment that binds SHLD3-REV7 in human (residues 1-60) is 41/60 identical (0.683).
- The C-terminal OB-fold region (human long-form 421-904) is 381/484 identical (0.787), the most conserved part of the protein.
- The human long form carries 69 residues (655-723) that the 835-aa displayed form lacks (the OB fold B exon). Mouse has all 69 aligned positions, 56/69 identical (0.812). The canonical mouse sequence therefore corresponds to the human long form used in the biochemical and rescue studies, not the short splice form that fails to suppress HR.

## Interpretation and limits

Orthology itself rests on PANTHER, not on this alignment. Q3UEN2 is a member of PTHR14495:SF2, the family's only subfamily, which descends from PAINT node PTN001025652 (Eumetazoa). The alignment adds two things. The two functional modules mapped in human (the N-terminal recruitment segment and the C-terminal OB-fold region) are both conserved in mouse. Mouse also encodes the OB fold B exon that the human ssDNA-binding and HR-suppression experiments need. These are sequence observations. No ssDNA-binding assay has been done on mouse Shld2 protein.
