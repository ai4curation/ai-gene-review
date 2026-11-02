# Afap1l2 (mouse, Q5DTU0) sequence mapping

Script: `compare_isoforms.py` (run with `uv run compare_isoforms.py`; raw output in `compare_isoforms.out`).
Sequences are fetched live from UniProt REST and NCBI E-utilities.

## Results

- Mouse canonical isoform Q5DTU0-1 is 825 aa; isoform Q5DTU0-2 is 843 aa (18-residue N-terminal extension).
- The mouse construct used by Yamanaka et al. 2016 (PMID:27462298; GenBank NM_001177796, protein NP_001171267, 843 aa) is identical to UniProt isoform Q5DTU0-2, not to the displayed canonical isoform.
- The F-actin-binding segment that paper maps to construct residues 830-840 (VLQKAKEWEKK) corresponds to residues 812-822 of the canonical isoform Q5DTU0-1, so the actin-binding region is shared by both mouse isoforms.
- Global alignment (BLOSUM62) of human Q8N4X5-1 (818 aa) and mouse Q5DTU0-1: 683 identical positions (83.5% of the human length).
- Human Tyr54, the p85-docking YxxM tyrosine (Y54-I-Y-M57), aligns to mouse Tyr54; the motif SSSDEEYIYMNKV (residues 48-60) is identical in both species. UniProt records large-scale phosphorylation of mouse Tyr56 in brain (PubMed:18034455), the adjacent tyrosine within this motif.

## Interpretation

Mouse and human AFAP1L2 are 1:1 orthologs (same PANTHER subfamily PTHR14338:SF4) with the p85-binding motif and the C-terminal actin-binding segment conserved. This supports transferring the human phosphotyrosine/PI3K adaptor activity to mouse, while the actin-binding and crosslinking data were obtained directly on the mouse protein.
