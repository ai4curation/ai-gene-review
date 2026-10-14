# ANKAR transmembrane-segment check

UniProt annotates one helical transmembrane segment, residues 309-329, from sequence prediction (ECO:0000255). It is the basis of the only GOA row (membrane, ECO:0007322). Two analyses ask whether the segment is a real membrane-spanning helix.

## 1. Kyte-Doolittle hydropathy (`hydropathy_check.py`, output `results.tsv`)

Mean hydropathy over 19-residue windows; 1.6 is the classic threshold. The sequence is read from the cached `ANKAR-uniprot.txt`. To reproduce: `uv run python hydropathy_check.py > results.tsv`.

- The two highest-scoring windows in the whole protein start at 312 (1.69) and 311 (1.66), both inside the annotated segment.
- The core of 309-329 (IRRGIGYLKLICFLIPFLLSL) is a 12-residue apolar stretch, with its Arg pair only at the N-terminal edge, consistent with the positive-inside rule.
- Two other windows also pass 1.6:
  - Start 605 (MPIHFAAFYDNVCIIIALC), inside ANK repeat 3, carries Asp-Asn mid-segment.
  - Start 1099 (IKVEVAFSLACIVLGNDVL), inside ARM repeat 6, carries Glu and Asn-Asp.
  - Neither is a credible transmembrane helix.

So hydropathy mildly favours UniProt's call. But a fixed-window mean cannot tell a transmembrane helix from a hydrophobic helix buried in a soluble repeat fold, which is the question here.

## 2. AlphaFold model (`alphafold_tm_check.py`, output `alphafold_results.tsv`)

The script reads AF-Q7Z5J8-F1 (v6) and measures pLDDT, helicity (C-alpha i to i+3 distance) and packing (C-alpha atoms within 10 A, excluding near-sequence neighbours) for 309-329, against the protein-wide distribution. To reproduce: `uv run python alphafold_tm_check.py > alphafold_results.tsv`.

| Measure | 309-329 | Reference |
|---|---|---|
| Mean pLDDT | 95.6 | flanks 289-308: 91.2; 330-349: 88.3 |
| Mean C-alpha i to i+3 | 5.14 A | about 5.0-5.5 A in a helix |
| Mean packing contacts | 11.6 | protein mean (pLDDT 70 or more): 10.0 |
| Share of confident residues with fewer or equal contacts | 0.59 | |

AlphaFold models 309-329 as a confident helix within a well-ordered region, packed about as densely as a typical ordered residue. That looks more like a helix in a folded soluble domain than an isolated membrane-spanning helix. AlphaFold models single proteins without a membrane, however, so this does not exclude insertion.

## Conclusion

The segment is ANKAR's most hydrophobic stretch and has transmembrane-like features. But the structure model places it inside an ordered fold, and no experiment has localized ANKAR. The evidence does not decide between a single-pass membrane protein and a soluble ankyrin/ARM protein.
