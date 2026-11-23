# U5TVQ7 (Thiobacillus thioparus SoxB fragment): mapping onto full-length SoxB

Script: `map_fragment.py` (run with `uv run --no-project --with biopython python map_fragment.py`).
It downloads the sequences and features live from the UniProt REST API, runs a local
(Smith-Waterman) BLOSUM62 alignment (gap open -10, extend -0.5) of U5TVQ7 against two
full-length SoxB sequences, and maps the PDB-derived Mn(2+) ligand positions of
Thermus thermophilus HB27 SoxB (Q72IT0; PDB 2WDC/2WDD/2WDE/2WDF, the structures of
Sauvé et al. 2009, PMID:19535341) onto the fragment.

## Output (run 2026-10-28)

```
U5TVQ7: length 325

Reference Q72IT0 (Thermus thermophilus (strain ATCC BAA-163 / DSM 7039 / HB27)), length 573
  fragment aligns to reference residues 148-465
  aligned columns 314; identity 122/314 = 38.9%
  PDB-derived Mn(2+) ligand positions in Q72IT0: [47, 49, 143, 174, 274, 297, 299]
    Q72IT0 D47 -> outside fragment / gap
    Q72IT0 H49 -> outside fragment / gap
    Q72IT0 D143 -> outside fragment / gap
    Q72IT0 H174 -> U5TVQ7 H27 conserved
    Q72IT0 H274 -> U5TVQ7 H131 conserved
    Q72IT0 H297 -> U5TVQ7 H154 conserved
    Q72IT0 H299 -> U5TVQ7 H156 conserved

Reference A0AAE6TS95 (Paracoccus pantotrophus), length 564
  fragment aligns to reference residues 153-470
  aligned columns 318; identity 160/318 = 50.3%
```

## Interpretation

- U5TVQ7 is an internal PCR-amplicon fragment (UniProt NON_TER at residues 1 and 325)
  covering roughly residues 150-470 of a ~565-575-residue SoxB. It lacks the N-terminal
  ~150 residues, which carry the twin-arginine signal peptide reported for
  P. pantotrophus SoxB (PMID:10940005), and the C-terminal ~100 residues.
- The fragment is clearly SoxB-like (50% identical over 318 columns to P. pantotrophus
  SoxB, 39% to T. thermophilus SoxB), consistent with its PANTHER placement in
  PTHR11575:SF42 "SULFUR OXIDATION PROTEIN SOXB".
- All four Mn(2+) ligands of the structural reference that fall inside the fragment
  are conserved histidines (U5TVQ7 H27, H131, H154, H156). The other three ligands
  (D47, H49, D143 in Q72IT0) are N-terminal to the fragment, so their conservation
  cannot be assessed from this sequence.
- The sequence is therefore consistent with a dimanganese SoxB thiosulfohydrolase, but
  nothing here is experimental for the T. thioparus protein; the inference rests on
  homology to characterized SoxB proteins.
