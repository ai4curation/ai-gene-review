# STX3 (donkey A0A8C4LHZ8): ortholog comparison and motif check

Analysis date: 2026-10-21. Script: `compare_orthologs.py` (run with `uv run --script compare_orthologs.py`).
Sequences are fetched from the UniProt REST API and saved in `sequences.fasta`; numeric output is in
`results.json`. Global alignment with Biopython PairwiseAligner (match 2, mismatch -1, gap open -10,
gap extend -0.5); percent identity is identical aligned columns divided by target length (289).

## Evolutionary placement

UniProt assigns A0A8C4LHZ8 to PANTHER PTHR19957:SF34 (SYNTAXIN-3), the same subfamily as the
experimentally characterised human (Q13277), mouse (Q64704) and rat (Q08849) syntaxin 3 proteins.

## Percent identity of A0A8C4LHZ8 to reference proteins

| accession | protein | length | identity (%) |
|---|---|---|---|
| Q08849 | rat Stx3 (syntaxin 3A) | 289 | 97.9 |
| Q64704 | mouse Stx3 (syntaxin 3A, canonical) | 289 | 97.6 |
| Q13277 | human STX3 (isoform A, canonical) | 289 | 96.5 |
| A0A8C4PQW9 | donkey STX3 syntaxin 3B gene model | 287 | 87.5 |
| Q16623 | human STX1A (paralog) | 288 | 61.6 |
| Q12846 | human STX4 (paralog) | 297 | 40.1 |

The donkey protein is a near-identical ortholog of rodent and human syntaxin 3A, and clearly
distinct from the STX1A and STX4 paralogs. Its lower identity to the donkey 3B gene model reflects
the alternatively spliced exons that encode the C-terminal half of the SNARE motif and the
transmembrane anchor (see `../../STX3/STX3-bioinformatics/RESULTS-rereview.md`, which classifies
A0A8C4LHZ8 as syntaxin 3A by exon-segment comparison).

## Conserved functional motifs in A0A8C4LHZ8

- FMDE apical targeting motif: present at residues 31-34, the same position as the F31, D33 and E34
  residues shown to be required for apical targeting of syntaxin 3 (PMID:16785322).
- N-terminal MKDRL sequence: present at residues 1-5 (N-peptide region used for Munc18 binding in
  syntaxins).
- SNARE motif zero-layer context NQGEML: present at residues 224-229, so the central glutamine of
  this Qa-SNARE is Q225.
- UniProt features: T-SNARE coiled-coil homology domain 191-253 and a C-terminal Phobius
  transmembrane helix 264-288, consistent with a tail-anchored Qa-SNARE.

## Conclusion

A0A8C4LHZ8 is the donkey syntaxin 3A ortholog, with all residues tested here conserved. Functions
established experimentally for mammalian syntaxin 3A (apical plasma membrane Qa-SNARE in polarised
epithelia) can be transferred with high confidence. Functions shown specifically for the retinal
syntaxin 3B splice form (ribbon synapse exocytosis) should not be transferred to this product.
