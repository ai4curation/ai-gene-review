# N-terminal extension of Dictyostelium scsC (Q55AI5)

Analysis: `nterm_extension.py`, run on 2026-11-18 with the repository environment (`python nterm_extension.py`). The script carries inline dependency metadata, so `uv run --script nterm_extension.py` also works.
Output: `results.yaml` (all numbers below).
Inputs are fetched at run time from UniProt: the sequence of Q55AI5 and of eight other beta subunits of succinyl-CoA synthetase, with their transit-peptide features.
The method is the one used for the paralog scsB in `genes/DICDI/scsB/scsB-bioinformatics`.

## Question

UniProt gives Q55AI5 a transit peptide of residues 1..17, taken from a family rule and not from a measurement.
Where does the conserved start of the mature beta subunit fall in Q55AI5, how many residues lie ahead of it, and what are they like?

## Terms

- Mature start: the first residue after the transit peptide recorded in the reference's UniProt entry. E. coli SucC has no transit peptide, so its mature start is residue 1.
- Extension: the residues of Q55AI5 that lie ahead of the residue aligned to a reference's mature start.
- Position 20: residue 20 of the mature beta subunit, counted from the mature start. It is Pro in E. coli SucC and Gln in pig GTP-specific succinyl-CoA synthetase.

## Method

Each reference was aligned to Q55AI5 over its full length (global alignment, BLOSUM62, gap open -10, gap extend -0.5, end gaps free; Biopython PairwiseAligner).
The reference's mature start and its position 20 were then mapped onto Q55AI5 through the alignment.
The paralog scsB (Q869S7) has no transit peptide in UniProt and an unknown mature start, so it is used for percent identity only.

## Results

| Reference | Transit peptide in UniProt (evidence) | Reference mature start | Q55AI5 residue aligned to it | Q55AI5 residue at position 20 | Identity over aligned columns |
|---|---|---|---|---|---|
| Human SUCLA2, Q9P2R7 | 1..52 (ECO:0007744, proteomics) | 53, LSLHEYMSME | 35, LNVHEYQAQK | Pro54 (reference Pro) | 54.6% |
| Human SUCLG2, Q96I99 | 1..37 (ECO:0007744, proteomics) | 38, LNLQEYQSKK | 35, LNVHEYQAQK | Pro54 (reference Gln) | 52.8% |
| Pig SUCLG2, P53590 | <1..38 (no evidence code) | 39, LNLQEYQSKK | 35, LNVHEYQAQK | Pro54 (reference Gln) | 52.7% |
| Mouse Suclg2, Q9Z2I8 | 1..38 (ECO:0000250, by similarity) | 39, LNLQEYQSKK | 35, LNVHEYQAQK | Pro54 (reference Gln) | 52.8% |
| Yeast LSC2, P53312 | 1..30 (ECO:0000255, predicted) | 31, LSIHEYRSAQ | 35, LNVHEYQAQK | Pro54 (reference Pro) | 49.5% |
| S. pombe O94415 | 1..23 (ECO:0000255, predicted) | 24, ALHEYISHDI | 36, NVHEYQAQKM | not used (see below) | 55.5% |
| E. coli SucC, P0A836 | none | 1, MNLHEYQAKQ | 35, LNVHEYQAQK | Pro54 (reference Pro) | 51.0% |
| Dictyostelium scsB, Q869S7 | none recorded | unknown | not used | not used | 57.9% |

Six of the seven references with a mature start place it on Leu35 of Q55AI5.
The seventh, S. pombe O94415, has a predicted transit peptide that ends one residue inside the conserved motif, so its mature start maps to Asn36 and its residue 20 is not the homologous position; it is not used for position 20.

The transit peptide that UniProt records for Q55AI5 itself (1..17) ends 17 residues ahead of Leu35. The 17 residues of that rule-derived transit peptide are `MLSNIVKKTIQSSKNLK` and the next ten are `SLVLNKSTSS`.

The 34 residues of Q55AI5 ahead of Leu35 are `MLSNIVKKTIQSSKNLKSLVLNKSTSSLVYQKRF`.
They contain 7 basic residues (Lys or Arg), no acidic residue (Asp or Glu), 9 Ser or Thr and 13 hydrophobic residues (Ala, Ile, Leu, Met, Phe, Val, Trp, Tyr).

The residue of Q55AI5 at position 20 is Pro54 with every reference that gives a position. This agrees with the Pro20 state reported for Q55AI5 in `genes/yeast/LSC2/LSC2-bioinformatics/results.yaml`.

Q55AI5 is more identical to its Dictyostelium paralog scsB (57.9%) than to human SUCLA2 (54.6%) or human SUCLG2 (52.8%).

## Interpretation

- Q55AI5 has a 34-residue N-terminal extension ahead of the conserved start of the mature beta subunit. The extension is in the same position as the transit peptides of human SUCLA2 and human SUCLG2, whose removal is recorded in UniProt from proteomics.
- The extension is basic, has no acidic residue and is rich in Ser and Thr, as mitochondrial presequences generally are.
- The transit peptide in the UniProt record (1..17) is half the length of the extension. If the mature protein starts at residue 18, it carries 17 residues ahead of the conserved start that the animal and bacterial subunits do not have. If it starts near residue 35, the UniProt feature is too short. The alignment cannot tell these apart.
- Pairwise identity does not show which animal paralog Q55AI5 is orthologous to: the difference between SUCLA2 and SUCLG2 is under two points, and the closest sequence is the Dictyostelium paralog. The A-type placement of Q55AI5 rests on the trees in `genes/yeast/LSC2/LSC2-bioinformatics`, not on identity.

## Limitations

- No targeting predictor was run here. TargetP-2.0, as reported in Table S1 and Table S5 of PMID:35602934, classifies Q55AI5 as mTP (mitochondrial targeting peptide); those tables do not give a cleavage site.
- The mature N-terminus of the Dictyostelium protein has not been determined.
- The mature starts of the pig, mouse, yeast and S. pombe references are not experimental in UniProt. Only the human SUCLA2 and SUCLG2 transit peptides carry proteomics evidence, and the bacterial start is the natural N-terminus.
- Pairwise global alignment with one scoring scheme. The conserved start motif (LNLHEYQ and close variants) is identical or nearly identical in all references that give a position, so the mapping does not depend on the settings.
- Percent identity is over aligned columns of pairwise alignments of different lengths and is not a phylogenetic measure.
