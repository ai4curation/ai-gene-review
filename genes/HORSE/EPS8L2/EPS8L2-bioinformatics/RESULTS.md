# EPS8L2 (horse, F7BFV0) ortholog comparison

Script: `compare_orthologs.py` (PEP 723; run with `uv run --script compare_orthologs.py`).
Raw output: `compare_orthologs_output.txt`. Global alignment, BLOSUM62, gap open -10,
extend -0.5, free end gaps.

## Results (from compare_orthologs_output.txt)

| Comparator | Accession | Length | Identity over aligned columns | Horse N-terminal overhang |
|---|---|---|---|---|
| human EPS8L2 | Q9H6S3 | 715 | 626/713 = 87.8% | 91 aa |
| mouse Eps8l2 | Q99K30 | 729 | 615/710 = 86.6% | 91 aa |
| human EPS8 | Q12929 | 822 | 343/672 = 51.0% | 93 aa |
| human EPS8L1 | Q8TE68 | 723 | 296/664 = 44.6% | 101 aa |

The horse model F7BFV0 (806 aa) carries a methionine at position 92 (`...AATEDA M92 SQSGSVSY...`)
that aligns to Met1 of human and mouse EPS8L2. Residues 1-91 of the horse model have no
counterpart in human or mouse EPS8L2, and the UniProt record marks residues 1-75 as a
MobiDB-lite disordered, Pro-rich region. Downstream of Met92 the horse sequence is
collinear with human EPS8L2 over its whole length (806 - 91 = 715 aa, the human length).

## Interpretation

- Horse F7BFV0 is the one-to-one ortholog of human/mouse EPS8L2: its identity to them
  (~87%) is far above its identity to the paralogs EPS8 (51%) and EPS8L1 (45%), and UniProt
  places it in PANTHER subfamily PTHR12287:SF20 (EPS8L2), the same subfamily as Q9H6S3
  and Q99K30 (interpro/panther/PTHR12287/PTHR12287-entries.csv).
- The 91-residue N-terminal extension most likely reflects an Ensembl gene model that
  starts translation at an upstream in-frame codon (or includes 5' UTR sequence) rather than
  a conserved protein region; it is not evidence of a horse-specific domain. All annotated
  domains (PTB, SH3, C-terminal effector/actin-binding region) lie downstream of Met92.
  This is an inference from alignment only; transcript evidence for horse was not examined.
