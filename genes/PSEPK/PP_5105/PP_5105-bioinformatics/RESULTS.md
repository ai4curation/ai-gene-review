# PP_5105 (Q88CS5) ThiS gene-model check

Script: `this_start_site.py` (Biopython local alignment, BLOSUM62). Input: the cached
`PP_5105-uniprot.txt`; comparison sets fetched from UniProt REST on 2026-11-12
(E. coli ThiS O32583; all genus Pseudomonas, taxon 286, entries with InterPro IPR010035).
Raw output: `this_start_site.out`.

## Results

- Q88CS5 is 92 aa and ends in the C-terminal Gly-Gly that ThiS-family carriers
  thiocarboxylate (output line: "Q88CS5 length 92; C-terminal dipeptide GG").
- The local alignment with E. coli ThiS (66 aa) begins at Q88CS5 residue 27 and
  O32583 residue 1 and runs to the C-terminal GG of both proteins (E. coli ThiS residues 1-66
  aligned with Q88CS5 27-92).
- 355 Pseudomonas IPR010035 entries; length distribution
  {66: 301, 67: 2, 71: 38, 72: 4, 77: 3, 82: 1, 83: 1, 90: 1, 92: 2, 95: 1, 97: 1};
  all 355 end in GG.
- For orthologs whose own residue 1 falls inside the alignment, ortholog Met1 aligns to
  Q88CS5 residue 27 in 301 cases (all 66-aa entries) and residue 22 in 38 cases (all 71-aa
  entries); only one other entry (92 aa) aligns from Q88CS5 residue 1.
  Output line: "(ortholog length, Q88CS5 residue aligned to ortholog Met1): {(66, np.int64(27)): 301, (71, np.int64(22)): 38, (92, np.int64(1)): 1}"
- Q88CS5 residue 22 is Met (segment 22-30 = MVAVRMRIK); residue 27 is also Met.

## Interpretation

The ThiS beta-grasp core and C-terminal GG of Q88CS5 are intact. Residues 1-21 have
no counterpart in 339 of 340 Pseudomonas ThiS orthologs whose N-terminus could be placed,
so the annotated start codon of PP_5105 is probably upstream of the real one (Met22
or Met27). This is an inference from ortholog comparison, not a measured start site.
The family assignment and functional inference are unaffected.
