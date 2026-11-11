# Targeting-signal analysis for Coniophora puteana MDH A0A5M3MRX5 (CONPUDRAFT_136560)

Script: `targeting_analysis.py` (fetches sequences from UniProt REST, Biopython
PairwiseAligner, BLOSUM62, global). Raw output: `targeting_output.txt`.
Run with `uv run python targeting_analysis.py > targeting_output.txt`.

## Question

Is A0A5M3MRX5 the mitochondrial or a non-mitochondrial (cytosolic/peroxisomal)
type-1 malate dehydrogenase of C. puteana?

## Method

The conserved NAD-binding glycine-rich motif of the lactate/malate DH N-terminal
domain (regex `G[AG].GG[IV]G`) was used as a fixed point marking the start of
the conserved catalytic core. The residues before it were compared across the
target, its only other type-1 MDH paralog in the reference proteome
(A0A5M3MC96, CONPUDRAFT_157993) and the three S. cerevisiae isozymes (MDH1
mitochondrial, MDH2 cytosolic, MDH3 peroxisomal). The last three residues were
inspected for a PTS1 signal.

## Results

| Accession | Protein | Residues before motif | Basic (R/K) | Acidic (D/E) | Ser/Thr | C-terminus |
|---|---|---|---|---|---|---|
| A0A5M3MRX5 | C. puteana target | 32 | 5 | 0 | 10 | FVA |
| A0A5M3MC96 | C. puteana paralog | 6 | 1 | 0 | 0 | SKL |
| P17505 | S. cerevisiae MDH1 (mitochondrial) | 23 | 4 | 0 | 5 | ASK |
| P22133 | S. cerevisiae MDH2 (cytosolic) | 19 | 1 | 2 | 4 | ASS |
| P32419 | S. cerevisiae MDH3 (peroxisomal) | 7 | 1 | 0 | 0 | SKL |

Target N-terminal segment: `MLARTALRSVASTSRASAFSTSAARLTRVAVL`.

Global pairwise identity of the target: 0.626 to yeast MDH1 (mitochondrial),
0.633 to the C. puteana paralog, 0.546 to yeast MDH3 (peroxisomal) and 0.484
to yeast MDH2 (cytosolic).

## Interpretation

- The target carries an N-terminal extension of roughly 25 residues beyond the
  short (6-7 residue) start of the peroxisomal-type sequences, rich in Arg,
  Ser/Thr and Ala and devoid of Asp/Glu. This is the composition of a
  mitochondrial matrix-targeting presequence, and it parallels yeast MDH1,
  whose 17-residue N-terminal extension is an experimentally established
  mitochondrial presequence (UniProt P17505 TRANSIT 1..17; PMID:3072021).
  No presequence predictor (TargetP, MitoFates) was run here; the call rests on
  composition and on homology to yeast MDH1.
- The target has no PTS1 (ends in FVA). Its paralog A0A5M3MC96 ends in SKL, a
  canonical PTS1, and lacks the presequence, matching yeast peroxisomal MDH3.
- PANTHER subfamily membership agrees: the target is in PTHR11540:SF73 (UniProt
  PANTHER cross-reference), the subfamily that contains yeast MDH1 (P17505,
  experimentally mitochondrial; `interpro/panther/PTHR11540/PTHR11540-entries.csv`).
  The peroxisomal subfamily is SF72, which holds yeast MDH3 (P32419) and not the
  target. Subfamily names are not localization calls: SF16 is also named
  "MALATE DEHYDROGENASE, MITOCHONDRIAL" yet contains yeast cytosolic MDH2
  (P22133). The paralog A0A5M3MC96 is placed in SF16, not SF72, so its
  peroxisomal call rests on its SKL alone.
- CDD cd01337 (MDH_glyoxysomal_mitochondrial) holds both the target and the
  paralog; it covers glyoxysomal and mitochondrial MDHs and so cannot separate
  the two.
- UniProt's Pfam PF00056 domain feature starts at residue 27 (FT DOMAIN
  27..169), independently corroborating an N-terminal extension of about 26
  residues ahead of the conserved domain.
- Conclusion: A0A5M3MRX5 is most likely the mitochondrial MDH of C. puteana,
  not a cytosolic enzyme. No yeast-MDH2-like cytosolic type-1 MDH, and no
  type-2 (IPR010945/IPR011274) MDH, was found among the UniProt entries of
  proteome UP000053558 queried by EC 1.1.1.37 / Pfam PF00056 / PF02866 /
  name "malate" (October 2026). That is a search of the current UniProt
  proteome only; it does not prove the absence of a cytosolic isozyme.
