# K9IWC0 is a C-type natriuretic peptide (NPPC/CNP), not a B-type peptide (NPPB/BNP)

## Question

The UniProt record for K9IWC0 (*Desmodus rotundus*) carries the ARBA-derived
name `RecName: Full=Natriuretic peptides B` together with the alternative names
"Brain natriuretic factor prohormone" and "Gamma-brain natriuretic peptide". The
same record, however, assigns the protein to PANTHER subfamily
`PTHR12167:SF2; C-TYPE NATRIURETIC PEPTIDE`, and the source publication for this
transcript describes the abundant salivary natriuretic peptide of *D. rotundus*
as **C-type** natriuretic peptide (CNP). The GOA annotations propagated from the
BNP reading (notably `GO:0006182 cGMP biosynthetic process` justified by
"binding and stimulating NPR1") depend on which paralogue this actually is,
because BNP signals through NPR1/GC-A whereas CNP signals through NPR2/GC-B.

## Method

`classify_natriuretic_peptide.py` fetches the K9IWC0 precursor and the three
human natriuretic peptide precursors (NPPA/P01160, NPPB/P16860, NPPC/P23582)
from the UniProt REST API at run time and computes, for each human paralogue:

- global pairwise percent identity to K9IWC0 (Biopython `PairwiseAligner`,
  BLASTP scoring), and
- the C-terminal 17-residue disulfide ring (the segment between the last two
  cysteines) plus the number of residues following it.

The residue count after the ring is diagnostic: ANP and BNP precursors carry a
C-terminal tail beyond the ring, whereas CNP terminates exactly at the second
ring cysteine.

Reproduce with:

```bash
uv run python classify_natriuretic_peptide.py
```

Raw output is saved in `results.json`.

## Results

| Sequence | Length | % identity to K9IWC0 | C-terminal ring | Residues after ring |
|---|---|---|---|---|
| K9IWC0 (query) | 119 | — | `CFGQKLDRIGALSGLGC` | 0 |
| human NPPA / ANP (P01160) | 151 | 31.9 | `CFGGRMDRIGAQSGLGC` | 5 |
| human NPPB / BNP (P16860) | 134 | 31.9 | `CFGRKMDRISSSSGLGC` | 6 |
| human NPPC / CNP (P23582) | 126 | **72.3** | `CFGLKLDRIGSMSGLGC` | 0 |

Best match: **human NPPC / CNP**.

## Interpretation

K9IWC0 is a C-type natriuretic peptide (CNP/NPPC) orthologue:

1. It is 72.3% identical to human NPPC over the full precursor, versus 31.9% to
   either NPPB or NPPA — a >2-fold difference that leaves no ambiguity.
2. Its precursor terminates at the ring cysteine (0 trailing residues), matching
   NPPC and excluding NPPA (5 trailing residues) and NPPB (6).
3. The mature ring `CFGQKLDRIGALSGLGC` differs from human CNP
   `CFGLKLDRIGSMSGLGC` at only 3 of 17 positions, whereas it differs from the
   BNP ring at 8 of 17.
4. The N-terminal signal peptide is near-identical to human NPPC
   (`MHLSQLLACALLLTLLSL...` in both).

Consequences for GO annotation:

- The UniProt `FUNCTION` sentence "Acts by specifically binding and stimulating
  NPR1 to produce cGMP" is BNP/ANP biology and does **not** describe this
  protein. CNP is the ligand of NPR2 (guanylate cyclase B) and of the clearance
  receptor NPR3.
- `GO:0007168 receptor guanylyl cyclase signaling pathway` and
  `GO:0006182 cGMP biosynthetic process` remain correct, since CNP also acts
  through a receptor guanylyl cyclase — but the receptor is NPR2, not NPR1.
- `GO:0005179 hormone activity` is retained, as it is for the human NPPC
  orthologue, but with a caveat about the mode of action: unlike ANP/BNP, CNP
  acts as a local paracrine vasodilator rather than a circulating cardiac
  hormone, and in *D. rotundus* the transcript is expressed in the submaxillary
  salivary gland, where it is expected to act on host vasculature at the bite
  site. The orthology assignment made here does not by itself argue for or
  against the term; it is the paracrine/salivary context that should be recorded
  alongside it.

## Limitations

This is a sequence-based orthology assignment only. No *D. rotundus* CNP protein
has been purified or assayed, and receptor usage (NPR2 versus NPR1) is inferred
from mammalian CNP biology rather than measured for the bat protein.
