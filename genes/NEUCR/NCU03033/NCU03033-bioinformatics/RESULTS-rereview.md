# NCU03033 (Q7SGY4) NF-YA/Hap2 core comparison (re-review, 2026-10-21)

Script: `compare_core_rereview.py` (PEP 723; `uv run --script compare_core_rereview.py`).
Raw output: `compare_core_rereview.out`. Sequences fetched live from UniProt REST.

## Method

The Q7SGY4 segment 190-255, which spans the UniProt/PROSITE-annotated subunit
association domain (194-217) and the NFYA/HAP2-type DNA-binding region (225-250),
was locally aligned (BLOSUM62) to three experimentally characterised members of
PANTHER PTHR12632: S. cerevisiae HAP2 (P06774), S. pombe php2 (P24488) and human
NFYA (P23511). This is a domain-conservation check, not a phylogeny; the
evolutionary placement comes from the PAINT IBA nodes (PTN000290575,
PTN000290576) under which Q7SGY4 receives its IBA annotations.

## Results

- Q7SGY4 is 314 aa, the only UniProt entry in N. crassa OR74A carrying
  PTHR12632/IPR001289 (UniProt query organism_id:367110), so there is no NF-YA
  paralog in this genome.
- Core identity: S. pombe php2 77.8% (49/63, php2 10-72); S. cerevisiae HAP2
  76.2% (48/63, HAP2 158-220); human NFYA 66.1% (41/62, NFYA 262-323).
- The "YVNAKQ(F/Y)(H/Y)RILKRR" subunit-association segment and the
  "YLHESRH(N/K/R)HAMRRPRG(P/E)GGRF" DNA-recognition segment are intact in
  Q7SGY4; no indel in the core relative to the yeast proteins.

## Interpretation

The full essential core of the NF-YA/Hap2 family is present and highly conserved.
The protein is a full-length gene product (not a fragment); its N-terminal
Q/P-rich disordered region (1-185) is typical of fungal Hap2 proteins, and its
C-terminal region after the core is disordered and acidic/basic. Nothing in the
sequence suggests loss of the subunit-association or CCAAT-recognition function.
