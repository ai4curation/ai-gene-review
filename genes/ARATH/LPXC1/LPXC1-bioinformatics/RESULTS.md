# Results: LPXC1-5 paralog check

Produced by `lpxc_paralog_check.py` (numbers in `results.json`).

## Paralog identity

The canonical UniProt sequences of LPXC1 (F4IAT8), LPXC2 (P0DKB7), LPXC3 (P0DKB8),
LPXC4 (P0DKB9) and LPXC5 (F4IAW1) are all 326 aa and are identical to each other:
every pairwise comparison reports identical_sequence = true, 100.0% identity.
At the protein level the five loci therefore encode the same canonical product, and
no protein-level experiment (GFP fusion, antibody, peptide mass spectrometry) can
distinguish them.

## Comparison with E. coli LpxC (P0A725)

Each canonical sequence aligns to E. coli LpxC with 36.2% identity over 260 aligned
columns (local alignment). All five inspected E. coli active-site residues are
conserved: H79 -> H109, H238 -> H281, D242 -> D285, D246 -> D289, H265 -> H313.
The Zn(2+) ligand positions (109, 281, 285) coincide with the UniProt BINDING features
of the Arabidopsis entries.

## Alternative isoforms (LPXC1 entry)

- F4IAT8 isoform 2 (266 aa; matches the length of AtLpxC1.2 in Li et al. 2011) keeps
  H109 but lacks H281, D285, D289 and H313 (1/5 sites), consistent with the authors'
  statement that AtLpxC1.2 lacks the C-terminal catalytic residues and is probably
  inactive.
- F4IAT8 isoform 3 (156 aa, residues 1-170 missing) lacks the N-terminal Zn ligand
  H109 (4/5 sites) and the transit peptide.

## Limitations

- Expression of the individual loci cannot be resolved here: with identical coding
  sequences, short-read or EST evidence cannot be assigned unambiguously to one locus.
- Nucleotide-level (UTR/intron) differences were not examined.
