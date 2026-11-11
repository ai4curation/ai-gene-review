# BICDL1 (horse, F6SAQ3): ortholog comparison

Script: `compare_orthologs.py` (run with `uv run --script compare_orthologs.py`).
Sequences fetched live from UniProt REST; global pairwise alignment (BLOSUM62,
gap open -10, extend -0.5). Raw output: `results.json`; alignments:
`alignment_horse_human.txt`, `alignment_horse_mouse.txt`.

## Family placement

UniProt places F6SAQ3 in PANTHER PTHR32123:SF12 (BICD FAMILY-LIKE CARGO ADAPTER 1),
the same subfamily as human BICDL1 Q6ZP65, mouse Bicdl1 A0JNT9 and zebrafish bicdl1
P0CF95 (interpro/panther/PTHR32123/PTHR32123-entries.csv). BICDL2 sits in SF11 and
Spindly (SPDL1) in SF9. The two IBA rows come from PAINT node PTN001281025
(taxon:33511, Deuterostomia), seeded by mouse Bicdl1 (MGI:1922915) and zebrafish
bicdl1 (ZFIN:ZDB-GENE-091204-439).

## Results

| Comparison | Length (other) | Paired | Identity over paired | Horse covered |
|---|---|---|---|---|
| human BICDL1 Q6ZP65 (canonical) | 573 | 573 | 96.51% | 99.83% |
| mouse Bicdl1 A0JNT9 | 577 | 574 | 95.12% | 100.0% |
| zebrafish bicdl1 P0CF95 | 569 | 548 | 61.5% | 95.47% |
| human BICDL2 A1A5D9 (paralog, SF11) | 508 | 492 | 38.41% | 85.71% |

Horse F6SAQ3 (574 aa) aligns end to end with the human canonical product with no
unpaired segment of 5 or more residues in either sequence, and end to end with mouse
A0JNT9. It is a full-length product of the canonical gene model, not a fragment or
an alternative-exon isoform. (The current human isoform Q6ZP65-2 is a 270-residue
C-terminal form; horse residues 1-352 have no counterpart in it.)

Functionally characterised mouse residues map to identical horse residues:

- mouse K512 (required for Rab6 binding, Schlager et al. 2010) -> horse K510
- mouse W166 (coiled-coil registry marker in the dynein-dynactin-BICDR1 cryo-EM
  structure, Chaaban & Carter 2022) -> horse W164

## Interpretation

Orthology to the characterised mouse and human BICDL1 is supported by shared SF12
subfamily membership and the deuterostome PAINT node, not only by sequence
similarity. Identity of 95-97% over the full length, conservation of the Rab6-binding
lysine, and conservation of the N-terminal coiled-coil support transfer of the mouse
activating-adaptor and Rab6-binding functions to the horse protein.
