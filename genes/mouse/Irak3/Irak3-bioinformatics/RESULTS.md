# Mouse Irak3 (Q8K4B2): pseudokinase motif comparison with human IRAK3 (Q9Y616)

Script: `pseudokinase_motifs.py` (run with `uv run --no-project --with biopython python pseudokinase_motifs.py`).
Output: `pseudokinase_motifs.json`. Sequences are read from the UniProt flat files in the repository
(`genes/mouse/Irak3/Irak3-uniprot.txt`, `genes/human/IRAK3/IRAK3-uniprot.txt`); global alignment with
BLOSUM62 (gap open -10, extend -0.5).

## Results

- Global alignment: 454 identical positions over 609 alignment columns (74.5% identity).
- Catalytic loop (HRD in active kinases): human CGS 291-293 aligns to mouse CGN 304-306. The catalytic
  aspartate is absent in mouse Irak3 (Asn-306), consistent with the UniProt CAUTION note.
- Mg-binding loop (DFG in active kinases): human DFA 311-313 aligns to mouse DFA 324-326. The glycine is
  replaced by alanine in both species.
- VAIK lysine: human K192 aligns to mouse K205 (retained).
- Death-domain IRAK4-binding residue: human W74 aligns to mouse W74 (retained; the residue mutated in the
  mouse IRAK-M W74A experiments of PMID:23376919).
- PIN1 site: human S110-P111 aligns to mouse T110-P111 (phosphoacceptor is Thr in mouse; the proline
  needed for a pS/pT-Pro PIN1 motif is retained).

## Interpretation

Mouse Irak3 shares the noncanonical active-site configuration of human IRAK3: no catalytic HRD aspartate and
a DFA Mg-binding loop. Both proteins are classified in PANTHER 19.0 subfamily PTHR24419:SF7 (IRAK3), per
the PANTHER 19.0 mouse and human classification files in `.cache/panther/`. (The UniProt Q8K4B2 entry's
own PANTHER cross-reference lists PTHR27001:SF929; the 19.0 HMM classification places it in PTHR24419:SF7
with the human protein.) Catalytic kinase activity is therefore not expected for mouse Irak3, while the death
domain residue used for IRAK4 binding and the PIN1 Pro-directed site are conserved.
