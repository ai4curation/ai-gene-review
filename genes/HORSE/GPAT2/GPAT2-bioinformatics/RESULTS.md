# Horse GPAT2 (A0A3Q2HKJ8) sequence comparison

Script: `compare_sequences.py` (run with `uv run --script compare_sequences.py`);
raw output in `results.txt`. Inputs are UniProt FASTA files downloaded on
2026-10-21: horse A0A3Q2HKJ8, human GPAT2 Q6NUI2, mouse Gpat2 Q14DK4, human
GPAM Q9HCL2. Global alignment, BLOSUM62, gap open -10, extend -0.5, free end gaps.

## Results

| Reference | Length | Aligned | Identity (aligned) |
|---|---|---|---|
| human GPAT2 Q6NUI2 | 795 | 794 | 88.2% |
| mouse Gpat2 Q14DK4 | 801 | 800 | 83.9% |
| human GPAM Q9HCL2 | 828 | 773 | 36.5% |

- Horse A0A3Q2HKJ8 is 800 aa and aligns over the whole length of human GPAT2 (1-795)
  and mouse Gpat2 (1-801); it is a full-length gene model, not a fragment.
- The mouse HXXXXD acyltransferase motif (Q14DK4 205-210, HKSLLD) aligns to horse
  H205-K206-S207-L208-L209-D210, identical in sequence and position.
- The two mouse predicted transmembrane segments (306-332 and 450-472) align to horse
  306-332 and 449-471 without gaps.
- Identity to the GPAT1 paralog (GPAM) is only 36.5%, so the horse protein is a
  GPAT2 ortholog and not a GPAM-like copy; this agrees with UniProt's PANTHER
  assignment PTHR12563:SF15 (GLYCEROL-3-PHOSPHATE ACYLTRANSFERASE 2, MITOCHONDRIAL).

## Limits

Pairwise identity is used only to check gene-model completeness and motif
conservation. The orthology claim rests on the PANTHER subfamily assignment
(SF15, shared with human Q6NUI2, mouse Q14DK4 and rat D3ZI76) and on the
Ensembl Compara orthology to mouse Gpat2 used by the GO_REF:0000107 transfers, not on identity. A conserved
HXXXXD motif does not by itself demonstrate activity of the horse protein.
