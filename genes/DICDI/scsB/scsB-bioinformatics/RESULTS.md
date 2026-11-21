# N-terminal extension of Dictyostelium scsB (Q869S7)

Analysis: `nterm_extension.py`, run on 2026-11-18 with the repository environment (`python nterm_extension.py`). The script carries inline dependency metadata, so `uv run --script nterm_extension.py` also works.
Output: `results.yaml` (all numbers below).
Inputs are fetched at run time from UniProt: the sequence of Q869S7 and of seven reference beta subunits of succinyl-CoA synthetase, with their transit-peptide features.

## Question

UniProt records no transit peptide for Q869S7 and states that none is predicted, although the protein is annotated as mitochondrial.
Does Q869S7 have residues ahead of the conserved start of the mature beta subunit, and what are they like?

## Terms

- Mature start: the first residue after the transit peptide recorded in the reference's UniProt entry. E. coli SucC has no transit peptide, so its mature start is residue 1.
- Extension: the residues of Q869S7 that lie ahead of the residue aligned to a reference's mature start.
- Position 20: residue 20 of the mature beta subunit, counted from the mature start. It is Pro in E. coli SucC and Gln in pig GTP-specific succinyl-CoA synthetase.

## Method

Each reference was aligned to Q869S7 over its full length (global alignment, BLOSUM62, gap open -10, gap extend -0.5, end gaps free; Biopython PairwiseAligner).
The reference's mature start and its position 20 were then mapped onto Q869S7 through the alignment.

## Results

| Reference | Transit peptide in UniProt (evidence) | Reference mature start | Q869S7 residue aligned to it | Q869S7 residue at position 20 |
|---|---|---|---|---|
| Human SUCLG2, Q96I99 | 1..37 (ECO:0007744, proteomics) | 38, LNLQEYQSKK | 27, LNLHEYQSKS | Gln46 (reference Gln) |
| Pig SUCLG2, P53590 | <1..38 (no evidence code) | 39, LNLQEYQSKK | 27, LNLHEYQSKS | Gln46 (reference Gln) |
| Mouse Suclg2, Q9Z2I8 | 1..38 (ECO:0000250, by similarity) | 39, LNLQEYQSKK | 27, LNLHEYQSKS | Gln46 (reference Gln) |
| Human SUCLA2, Q9P2R7 | 1..52 (ECO:0007744, proteomics) | 53, LSLHEYMSME | 27, LNLHEYQSKS | Gln46 (reference Pro) |
| Yeast LSC2, P53312 | 1..30 (ECO:0000255, predicted) | 31, LSIHEYRSAQ | 27, LNLHEYQSKS | Gln46 (reference Pro) |
| E. coli SucC, P0A836 | none | 1, MNLHEYQAKQ | 27, LNLHEYQSKS | Gln46 (reference Pro) |
| Dictyostelium scsC, Q55AI5 | 1..17 (ECO:0000255, predicted) | 18, SLVLNKSTSS | not aligned (gap) | not applicable |

Six of the seven references place their mature start on Leu27 of Q869S7.
The mature start predicted for the Dictyostelium A-type subunit scsC (residue 18) falls in a gap of the alignment, upstream of the conserved start, so that reference does not give a position.
Identity over aligned columns is 57 to 59% to the three animal SUCLG2 proteins, 52.7% to human SUCLA2, 57.9% to the Dictyostelium paralog scsC (Q55AI5), 45.8% to yeast LSC2 and 50.1% to E. coli SucC. Identity therefore does not separate the ortholog from the paralog; the SUCLG2 placement rests on the trees.

The 26 residues of Q869S7 ahead of Leu27 are `MSLFNSANKVIGGVLKFNPSKYQVRY`.
They contain 4 basic residues (Lys or Arg), no acidic residue (Asp or Glu), 3 Ser or Thr and 12 hydrophobic residues (Ala, Ile, Leu, Met, Phe, Val, Trp, Tyr).

The residue of Q869S7 at position 20 is Gln46 with every reference that gives a position. This is the residue UniProt lists as a GTP-binding residue (BINDING 46), and it agrees with the Gln20 state reported for Q869S7 in `genes/yeast/LSC2/LSC2-bioinformatics/results.yaml`.

## Interpretation

- Q869S7 has a 26-residue N-terminal extension ahead of the conserved start of the mature beta subunit. The extension is in the same position as the transit peptides of human SUCLG2 and human SUCLA2, whose removal is recorded in UniProt from proteomics.
- The extension is basic and has no acidic residue, as mitochondrial presequences generally do.
- The extension is evidence that the protein has an N-terminal segment that is not part of the catalytic fold. It is not evidence that the segment is cleaved or that it targets the protein to mitochondria.

## Limitations

- No targeting predictor was run here. TargetP-2.0, as reported in Table S1 and Table S5 of PMID:35602934, classifies Q869S7 as OTHER (no mitochondrial targeting peptide), and the UniProt record says no transit peptide is predicted. The alignment does not overrule those predictions; it shows only where a presequence would be if there is one.
- The mature N-terminus of the Dictyostelium protein has not been determined.
- The mature starts of the pig, mouse, yeast and Dictyostelium scsC references are not experimental in UniProt. Only the human SUCLG2 and SUCLA2 transit peptides carry proteomics evidence, and the bacterial start is the natural N-terminus.
- Pairwise global alignment with one scoring scheme; the conserved start motif (LNLHEYQ) is identical or nearly identical in all references that give a position, so the mapping does not depend on the settings.
