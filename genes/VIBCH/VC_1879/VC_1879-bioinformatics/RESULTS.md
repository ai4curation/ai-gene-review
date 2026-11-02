# VC_1879 (Q9KQW8) ComEC/Rec2: sequence checks

Run: `beril run` id `20261030T213831Z-vc1879-comec-motifs` (projects/hackathon), script
`analyze.py`, Biopython PairwiseAligner (BLOSUM62, gap open -11, extend -1). Inputs are in
`data/`: Q9KQW8, the dashboard sequence NZ_CWQE01000001.1_287, B. subtilis ComEC P39695 and
H. influenzae Rec2 P44408 (UniProt REST, 2026-10-30). Outputs: `results.json`,
`aln_Q9KQW8_vs_*.txt`.

## Dashboard sequence vs Q9KQW8

The dashboard protein (756 aa, including a run of 9 X residues near the N-terminus) aligns
to Q9KQW8 (752 aa) over 747 columns with 747 identities (100.0%) and no mismatches outside
the X positions.

## Domain architecture

Q9KQW8 has the full ComEC architecture: N-terminal ComEC_N (TIGR00360) and DUF4131 (PF13567,
the OB-fold N-terminal domain), the Competence domain (PF03772) with 9 Phobius TM helices in
UniProt (13 by DeepTMHMM on the dashboard page), and a C-terminal metallo-beta-lactamase-like
domain (Lactamase_B PF00753; SMART SM00849, residues 506-689).

## MBL motif conservation

The C-terminal MBL-like domain keeps the metal-binding motif II as HLDNDH at residues 556-561,
the ComEC-type variant of the canonical MBL HxHxDH motif with Asp at the second ligand position.
It aligns to HADQDH in B. subtilis ComEC and HDDNDH in H. influenzae Rec2. Both motif II
aspartates are present. These are the two motif II aspartates whose substitution (D611A/D613A)
in the M. thermoacetica ComEC CTD abolished Mn2+ binding and nuclease activity
(PMID:33772889). M. thermoacetica ComEC was not in the alignment. A motif V-like HH pair
(VPHHGSKTS, residues 663-664) aligns to GHHGSKGS in B. subtilis ComEC.

Over the MBL region (506-689) Q9KQW8 is 33.0% identical to B. subtilis ComEC (182 aligned
columns) and 44.9% identical to H. influenzae Rec2 (178 columns). Global identity is 28.1%
to B. subtilis ComEC (700 columns) and 33.7% to H. influenzae Rec2 (722 columns).

## Interpretation

The C-terminal MBL domain is present, and its metal ligands are conserved, so VC_1879 is
expected to carry the Mn2+-dependent nuclease activity shown for the M. thermoacetica ComEC
CTD and required for efficient transformation in B. subtilis. That activity has not been tested
for any Vibrio ComEC. Neither this analysis nor the literature tests whether ComEC is a passive
channel.
