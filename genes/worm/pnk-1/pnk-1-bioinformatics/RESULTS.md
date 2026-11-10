# pnk-1 (H2KYP7) catalytic-residue and domain-coverage analysis

Script: `catalytic_residues.py` (run from the repository root with
`uv run python genes/worm/pnk-1/pnk-1-bioinformatics/catalytic_residues.py`).
Sequences are fetched live from the UniProt REST API; alignments are ad hoc
pairwise local alignments (Biopython PairwiseAligner, BLOSUM62, gap open -10,
extend -0.5). No result is hard-coded.

## Question

PANTHER places C. elegans PNK-1 (H2KYP7, isoform C10G11.5a) in subfamily
PTHR12280:SF20 "4'-PHOSPHOPANTETHEINE PHOSPHATASE" (the PANK4 subfamily), and
PAINT propagates to it both NOT pantothenate kinase activity and phosphatase
activity. Human PANK4 is a pseudo-kinase because of Glu138Val and Arg207Trp
substitutions (human PANK3 numbering; PMID:30927326) and carries its
phosphatase activity in a C-terminal DUF89 domain. Does PNK-1 share either feature?

## Output (run 2026-10-28)

```
## Lengths
H2KYP7	C. elegans PNK-1	449 aa
Q18580	C. elegans PNK-4	755 aa
Q9H999	human PANK3	370 aa
Q8TE04	human PANK1	598 aa
Q9BZ23	human PANK2	570 aa
Q9NVE7	human PANK4	773 aa

## PNK-1 (H2KYP7) local alignment identity to human PANKs
human PANK1	identity 153/366 = 0.418	PNK-1 68-449 vs Q8TE04 180-597
human PANK2	identity 156/390 = 0.400	PNK-1 4-442 vs Q9BZ23 142-565
human PANK3	identity 133/316 = 0.421	PNK-1 118-441 vs Q9H999 16-364
human PANK4	identity 154/332 = 0.464	PNK-1 99-441 vs Q9NVE7 20-366

## Catalytic residues (human PANK3 numbering)
C. elegans PNK-1 (H2KYP7):	PANK3 E138 -> E214; PANK3 R207 -> R281
C. elegans PNK-4 (Q18580):	PANK3 E138 -> A119; PANK3 R207 -> R184
human PANK4 (Q9NVE7):	PANK3 E138 -> V147; PANK3 R207 -> W211
human PANK1 (Q8TE04):	PANK3 E138 -> E363; PANK3 R207 -> R432
human PANK2 (Q9BZ23):	PANK3 E138 -> E338; PANK3 R207 -> R407
```

## Interpretation

- PNK-1 retains both catalytic residues of active PANKs: Glu214 and Arg281
  align with human PANK3 Glu138 and Arg207. Human PANK4 has Val147/Trp211 at
  these positions (as reported in PMID:30927326), and the second worm paralog
  PNK-4 (Q18580) has Ala119 at the catalytic-Glu position.
- PNK-1 is only 449 aa and aligns with human PANK4 residues 20-366 only, i.e.
  with the kinase-like (Fumble) domain. It has no counterpart of the PANK4
  C-terminal phosphatase (DUF89) region; PNK-4 aligns over almost the whole
  length of PANK4 (PNK-4 13-748 vs PANK4 27-769 in a separate run of the same
  aligner settings).
- Sequence identity of PNK-1 is slightly higher to PANK4 (46%) than to
  PANK1-3 (40-42%), which is consistent with the PANTHER PANK4-subfamily
  placement of the Fumble domain, but the active-site residues are those of an
  active kinase. The divergence that inactivated PANK4 kinase activity is
  amniote-specific (PMID:30927326) and, in C. elegans, has occurred in PNK-4,
  not PNK-1.

Conclusion: the PAINT NOT pantothenate kinase activity and the phosphatase
activity propagated to PNK-1 are not supported by its sequence. PNK-1 is
predicted to be the active (monofunctional) pantothenate kinase of C. elegans.
