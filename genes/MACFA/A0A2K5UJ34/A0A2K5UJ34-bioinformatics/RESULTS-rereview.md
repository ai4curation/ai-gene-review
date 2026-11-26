# A0A2K5UJ34 sequence identity re-review (2026-10-21)

Script: `compare_sequences_rereview.py` (raw output in `compare_sequences_rereview.out`).
Sequences fetched from the UniProt REST API on 2026-10-21.

## Result

- A0A2K5UJ34 (Macaca fascicularis, unreviewed, 545 aa) is a contiguous segment of human TTC39C
  (Q8N584, reviewed, 583 aa): macaque residue 1 aligns to human Met39 and the segment runs to the
  human C-terminus.
- Ungapped identity over the 545 aligned residues is 0.9963 (2 substitutions: macaque 427 / human 465
  F->L; macaque 510 / human 548 A->T).
- Human residues 1-38 (MAGSEQQRPRRRDDGDSDAAAAAAAPLQDAELALAGIN) are absent from the macaque gene model.
  In UniProt Q8N584 residues 1-22 are annotated as a disordered region; the InterPro API places the
  Pfam PF10300 (Iml2-TPR_39) match on Q8N584 at residues 35-498, and the three UniProt TPR repeats at
  315-348, 353-386 and 485-518. The macaque model therefore lacks only the disordered N-terminal
  extension and the first four residues of the Pfam span; all annotated TPR repeats are present.

## Interpretation

A0A2K5UJ34 is the macaque TTC39C ortholog, encoded by an Ensembl gene model (ENSMFAT00000058040.2)
whose start codon corresponds to the internal Met39 of the human protein. It is best treated as an
N-terminally truncated alternative gene model of macaque TTC39C rather than a separate gene or a
fragment lacking the functional domain. No reviewed or longer macaque TTC39C entry exists in UniProt
(the only other macaque TTC39C record, A0A2K5UJ40, is 75 aa).
