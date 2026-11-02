# NCU11362 (A7UX10) vs characterised METTL16 orthologs (re-review, 2026-10-21)

Script: `compare_mettl16_rereview.py` (run with `uv run --script`); raw output: `results-rereview.json`.
Sequences fetched live from UniProt REST; global Needleman-Wunsch, BLOSUM62, gap open -10, extend -0.5.

## Results

- Lengths: A7UX10 541 aa; S. pombe Mtl16 (O42662) 385 aa; human METTL16 (Q86W50) 562 aa.
- A7UX10 vs S. pombe Mtl16: 39.7% identity over 383 aligned columns; covers 99.5% of Mtl16, including 96.9% of the Mtl16 C-terminal quarter (the C-terminal region that follows the methyltransferase domain; the KA-1 domain boundaries were not mapped here).
- A7UX10 vs human METTL16: 38.6% identity over 425 aligned columns; covers 75.6% of METTL16 (53.9% of its C-terminal quarter, which includes vertebrate-specific sequence).
- Catalytic NPPF motif: A7UX10 has a single NPPF at residues 282-285, and the alignment maps S. pombe NPPF155 and human NPPF184 onto A7UX10 position 282.

## Interpretation

A7UX10 is a full-length METTL16-family protein, not a fragment. Relative to Mtl16 it carries an extra N-terminal extension (about residues 1-79, predicted disordered in UniProt), and it covers the whole Mtl16 methyltransferase domain and the C-terminal region. The catalytic NPPF motif is retained at the aligned position. This is consistent with a catalytically competent METTL16 ortholog. It is not an enzyme assay.
