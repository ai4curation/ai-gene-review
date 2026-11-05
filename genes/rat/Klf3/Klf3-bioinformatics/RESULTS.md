# Klf3 (rat, D4A4V3) ortholog comparison

Script: `compare_orthologs.py` (run with `uv run python compare_orthologs.py`); raw output in `output.txt`.
Sequences are fetched live from the UniProt REST API; no results are hard-coded.

## Results (from output.txt)

- Rat D4A4V3 is 344 aa; mouse Q60980 344 aa; human P57682 345 aa.
- Rat vs mouse KLF3: overall identity 97.4% over 344 columns; zinc-finger region identity 100.0% over 84 columns.
- Rat vs human KLF3: overall identity 95.9% over 345 columns; zinc-finger region identity 100.0% over 84 columns.
- Three C2H2 zinc fingers are found in rat Klf3 at residues 261-283, 291-313 and 321-341.
- The CtBP-binding motif PVDLT (the motif mapped as required for repression in mouse BKLF) is present at residue 61 in rat, mouse and human.
- The two SUMO-acceptor lysines mapped in mouse BKLF (K10, K197) are conserved as K10 and K197 in rat
  (human numbering is shifted by one residue at the second site, so the human residue at 197 is not the equivalent position).

## Interpretation

Rat Klf3 is a 1:1 ortholog of mouse BKLF/KLF3 with an identical DNA-binding domain and the conserved
N-terminal CtBP-recruitment motif and sumoylation sites that mediate repression in mouse. Transfer of the
mouse/human experimental DNA-binding and repressor annotations to rat is therefore well justified.
