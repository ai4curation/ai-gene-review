# CcmC heme-binding site conservation: Q8EK42 (S. oneidensis MR-1) vs P0ABM1 (E. coli K-12)

## Question

The heme-binding site of CcmC is defined experimentally in *Escherichia coli*: the
tryptophan-rich WWD domain in the second periplasmic loop, flanked by two external
histidines (His60 and His184 in the *E. coli* numbering) that serve as the axial
ligands to the heme iron (PMID:20599545, PMID:19721088). The gene review needs to
know whether that site is present *in the sequence of the protein under review*
(UniProtKB:Q8EK42), rather than only inferring it from family membership.

## Method

`align_wwd_domain.py` fetches both sequences from the UniProt REST API, cross-checks
the fetched Q8EK42 sequence against the `SQ` block of the committed
`../ccmC-uniprot.txt` (aborting if they differ), performs a global Needleman-Wunsch
alignment (Biopython `PairwiseAligner`, BLOSUM62, gap open -11 / extend -1), and then
reads the Q8EK42 residue and position that each *E. coli* landmark aligns to directly
off the computed alignment. No position or residue identity is hardcoded; a landmark
that aligned to a gap or to a non-histidine would be reported as `NOT CONSERVED`.

```
uv run python align_wwd_domain.py
```

Raw output of the run behind this file is in `align_wwd_domain.out`.

## Result

```
Flat-file cross-check: fetched Q8EK42 matches ../ccmC-uniprot.txt SQ block
P0ABM1 (CCMC_ECOLI): 245 aa
Q8EK42 (CCMC_SHEON): 248 aa
Global alignment: score 758.0, 144/245 identical in aligned columns (58.8% identity)

Axial histidine landmarks (E. coli numbering -> Q8EK42):
  H60 -> H60 in Q8EK42: conserved
  H184 -> H184 in Q8EK42: conserved

WWD motif:
  P0ABM1: WWVWD at 122-126
  Q8EK42: WWVWD at 122-126
  E. coli 122-126 aligns to Q8EK42 positions [122, 123, 124, 125, 126]

Alignment around each landmark (E. coli / Q8EK42, aligned columns):
  His60   NSYRIIYLHVPAAIWSM
          DSYRIIFIHVPAASMSM
  WWD     WGKPMWGTWWVWDARLT
          WGKPMWGTWWVWDARLT
  His184  SVEWWNTLHQGST---R
          SVEWWSSLHQPSTIRIT
```

## Interpretation

The two proteins are 58.8% identical over the aligned length, and the alignment is
ungapped from the N-terminus through residue 184, so the *E. coli* numbering maps
one-to-one onto Q8EK42 across the whole heme-binding region:

- Both axial histidines are conserved and fall at the **same positions in Q8EK42**,
  His60 and His184. (These are Q8EK42 positions established by this alignment, not
  the *E. coli* numbers carried over by assumption.)
- The WWD motif is intact and identical in sequence, `WWVWD` at Q8EK42 122-126, in a
  17-residue window that is identical between the two proteins.

This is positional, sequence-level evidence that the characterised heme-binding site
of CcmC is present in the *S. oneidensis* MR-1 protein, which is a stronger basis for
the `GO:0020037` heme binding assignment than family membership plus the maturation
mutant phenotype alone. It does **not** demonstrate heme binding by Q8EK42
experimentally, and it says nothing about the catalytic or transport questions the
review discusses separately; the heme-attachment chemistry itself has not been assayed
for this protein.

## Caveats

- Pairwise global alignment, not a curated family MSA. The conclusion rests on an
  unambiguous, gap-free, high-identity region, which is the favourable case for this
  method; a borderline alignment would need a profile approach.
- The *E. coli* landmark positions are taken from the published *E. coli* work and are
  the input to the mapping, not a result of it.
- Sequences are fetched live, so a future UniProt sequence revision would change the
  run; the flat-file cross-check against `../ccmC-uniprot.txt` is what pins the
  reviewed sequence.
