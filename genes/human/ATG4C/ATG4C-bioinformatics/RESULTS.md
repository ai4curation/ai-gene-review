# ATG4C (human, Q96DT6) catalytic triad and subfamily check

Script: `catalytic_residues.py` (run with `uv run --script catalytic_residues.py`).
Sequences fetched from UniProt REST on 2026-10-21; global BLOSUM62 alignment
(gap open -10, extend -0.5) of each subject against human ATG4C.

## Output

```
query Q96DT6 length 458; triad residues: C111, D345, H347
subject	label	length	identity_over_aligned_cols	triad_in_subject
Q9Y4P1	human ATG4B	393	34.9% (125/358)	C74,D278,H280
Q8WYN0	human ATG4A	398	37.4% (134/358)	C77,D279,H281
Q86TL0	human ATG4D	474	53.7% (218/406)	C144,D356,H358
Q811C2	mouse Atg4c	458	90.4% (414/458)	C111,D345,H347
A0A9L0IIU3	donkey ATG4C (TrEMBL)	458	95.0% (435/458)	C111,D345,H347
```

## PANTHER subfamily assignments (UniProt DR PANTHER lines, 2026-10-21)

| Accession | Protein | PANTHER subfamily |
|---|---|---|
| Q96DT6 | human ATG4C | PTHR22624:SF38 (CYSTEINE PROTEASE ATG4C) |
| Q811C2 | mouse Atg4c | PTHR22624:SF38 |
| A0A9L0IIU3 | donkey ATG4C | PTHR22624:SF38 |
| Q86TL0 | human ATG4D | PTHR22624:SF36 (CYSTEINE PROTEASE ATG4D) |
| Q9Y4P1 | human ATG4B | PTHR22624:SF39 (CYSTEINE PROTEASE ATG4B) |
| Q8WYN0 | human ATG4A | PTHR22624:SF35 (CYSTEINE PROTEASE ATG4A) |

## Interpretation

- The Cys/Asp/His catalytic triad of the papain-like C54 fold, defined
  experimentally in ATG4B (Cys74, Asp278, His280), aligns to Cys111, Asp345 and
  His347 of ATG4C, matching UniProt's by-similarity ACT_SITE features. ATG4C is
  therefore not a pseudo-protease by sequence, consistent with its measured
  (weak) priming activity and its delipidation activity.
- ATG4C is closest within the human family to ATG4D (about 54% identity over the
  aligned columns) and distant from ATG4A/ATG4B (about 35-37%), each of which
  sits in a separate PANTHER subfamily. Subfamily-specific properties of ATG4B
  (fast, broad-spectrum priming) or ATG4D (preferential ATG8-PS delipidation) are
  not transferable to ATG4C on this basis.
- Mouse Atg4c and donkey ATG4C are in the same subfamily (SF38) and align end to
  end (458/458 columns) at 90% and 95% identity with conserved triad positions,
  supporting 1:1 orthology.
- A retained catalytic triad shows the residues are present; it does not by
  itself establish activity. Activity of human ATG4C rests on the biochemical
  and cellular papers cited in the review.
