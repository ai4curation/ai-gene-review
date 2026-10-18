# Drosophila BNIP3 (Q9VPD6) motif mapping against human BNIP3/BNIP3L and worm DCT-1

Script: `align_motifs.py` (run from the repo root with
`uv run python genes/DROME/BNIP3/BNIP3-bioinformatics/align_motifs.py`).
Raw output: `align_motifs_output.txt`.

Method: global pairwise alignment (Biopython PairwiseAligner, BLOSUM62, gap open -10,
extend -0.5) of fly BNIP3 against human BNIP3 (Q12983), human BNIP3L (O60238) and
C. elegans DCT-1, with sequences parsed from the cached UniProt files in this
repository. Human BNIP3 regions (UniProt Q12983 FT lines: BH3 motif 100-125, TM 164-184;
canonical LIR core WVEL 18-21) were projected onto the fly sequence.

## Results

- Overall identity to human BNIP3 is modest: 62 identical aligned residues, 30.8% over the
  201-residue fly protein (BNIP3L: 54 identities, 26.9%; DCT-1: 54 identities, 26.9%).
- LIR: human WVEL (18-21) aligns without gaps to fly WIEL at residues 16-19. These are
  the residues mutated (W16A/L19A) in the fly LIR mutant of Taoka et al. 2025 (PMID:40801807).
  The N-terminal LIR is the best-conserved functional motif.
- MER: the fly MER defined experimentally by Taoka et al. (G42-Q53, GEEYLRLLREAQ) sits in
  the conserved N-terminal block that aligns with human "DMEKILLDAQHESG".
- Transmembrane domain: human TM 164-184 aligns gaplessly to fly 169-189
  (SLLVTNVLSLLLGAGFGLWLS). The fly TM keeps a GxxxG-like glycine pattern (LGAGFG), which in
  human BNIP3 mediates homodimerisation; this is a sequence observation, not a test of dimerisation.
- BH3: the human BH3 motif region (100-125, IERRKEVESILKKNSDWIWDWSSRPE) aligns only
  partially (81% of columns, with gaps) to fly 93-120 (ELRNVYINYWTKGGDKQNAGNEDWLKNW).
  The only shared feature is the tryptophan-containing DW-x-x-x-W segment (human DWIWDW,
  fly DWLKNW; worm DCT-1 DWIWDW). The hydrophobic N-terminal half of the human BH3
  (ESILKK) is not conserved in fly. This alignment shows no recognisable BH3 consensus in
  fly BNIP3. It does not rule out a degenerate BH3-like element.

## Interpretation (limits)

These pairwise alignments support conservation of the mitophagy-receptor architecture
(LIR, MER, C-terminal tail anchor) in fly BNIP3. Support for a conserved BH3 domain is weak.
No structural or functional test of BH3 activity was done here.
