# atpD (B9MS68) sequence comparison with E. coli AtpD

Script: `analyze_atpD.py` (run with `uv run --no-project --with biopython python analyze_atpD.py`).
Outputs: `results.json`, `sequences.fasta` (UniProt sequences retrieved 2026-10-31).

## Catalytic residues

B9MS68 is 70.4% identical to E. coli AtpD (P0ABB4) over 460 aligned positions (global
BLOSUM62 alignment, gap open -11, extend -1).

Every catalytic and coupling residue characterized by mutagenesis in E. coli beta is
conserved in B9MS68. E. coli positions use literature numbering (UniProt P0ABB4 minus 1).

| E. coli beta | B9MS68 | Role |
|---|---|---|
| K155 | K158 | Walker A lysine |
| T156 | T159 | Walker A threonine (Mg2+) |
| E181 | E184 | catalytic base |
| R182 | R185 | catalytic site |
| E185 | E188 | catalytic site |
| D242 | D246 | Walker B aspartate |
| Y331 | Y335 | adenine stacking |
| D380 (DELSEED 380-386) | D384 (DELSEED 384-390) | gamma-contact loop |

The Walker A motif of B9MS68 is GGAGVGKT (residues 152-159) and its gamma-contact loop
is DELSEED (residues 384-390).

## Coupling ion (c subunit)

Beta does not choose the coupling ion; the c subunit does. In a global alignment of the
C. bescii c subunit (B9MS73) with the Na+-binding c subunit of Ilyobacter tartaricus
(Q8KRV3), two of the I. tartaricus Na+ ligands are not kept: Gln32 aligns to Ile20 and
Ser66 aligns to Ala54. Glu65 (Glu53) and Tyr70 (Tyr58) are kept. The H+-coupled E. coli
c subunit (P68699) likewise has Ile and Ala at the Gln32 and Ser66 positions. This is
consistent with H+ rather than Na+ coupling, but the coupling ion of the C. bescii
enzyme has not been measured, and the helix-1 alignment of these short sequences is
less certain than that of helix 2.
