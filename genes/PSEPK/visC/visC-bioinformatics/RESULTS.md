# Pairwise identity of P. putida KT2440 ring hydroxylases to E. coli UbiI, UbiH and UbiF

Question: which of the three E. coli flavin monooxygenases (UbiI/VisC, UbiH, UbiF)
do the two KT2440 UbiH/COQ6-family proteins, PP_5197 (Q88CI4, *visC*) and PP_5199
(Q88CI2, *ubiH*), correspond to?

Method: `hydroxylase_identity.py` reads the sequences from the cached UniProt flat
files and runs global Needleman-Wunsch alignments with Biopython `PairwiseAligner`
(BLOSUM62, gap open -10, gap extend -0.5). Percent identity is identical positions
divided by aligned (non-gap) columns. Command (from the repository root):

```
python genes/PSEPK/visC/visC-bioinformatics/hydroxylase_identity.py \
  genes/PSEPK/visC/visC-uniprot.txt genes/PSEPK/ubiH/ubiH-uniprot.txt \
  genes/ECOLI/ubiI/ubiI-uniprot.txt genes/ECOLI/ubiH/ubiH-uniprot.txt \
  genes/ECOLI/ubiF/ubiF-uniprot.txt genes/yeast/COQ6/COQ6-uniprot.txt
```

Raw output: `hydroxylase_identity.tsv`.

## Results

| KT2440 protein | vs E. coli UbiI (P25535) | vs E. coli UbiH (P25534) | vs E. coli UbiF (P75728) | vs yeast Coq6 (P53318) |
|---|---|---|---|---|
| Q88CI4 (PP_5197, visC) | 46.7 | 35.3 | 42.1 | 31.0 |
| Q88CI2 (PP_5199, ubiH) | 34.4 | 40.5 | 36.2 | 29.8 |

The two KT2440 proteins are 35.6% identical to each other.

## Interpretation

- Q88CI4 (PP_5197) is most similar to E. coli UbiI, then UbiF. UbiI and UbiF are
  sister clades (E. coli UbiI vs UbiF here: 39.4%), so pairwise identity alone
  separates them by only about 5 points. The UbiI assignment also rests on the
  PANTHER placement: the TreeGrafter row on Q88CI4 transfers GO:0019168 from the
  gammaproteobacterial UbiI node PTN000350245 (seeded by E. coli UbiI), not the
  UbiF node PTN001789718.
- Q88CI2 (PP_5199) is most similar to E. coli UbiH, consistent with its UbiH-specific
  NCBIfam (TIGR01984) and PANTHER subfamily (PTHR43876:SF8) assignments.
- Neither protein is closest to UbiF. With no UbiF-type third flavin monooxygenase,
  the late hydroxylation in KT2440 falls to the Coq7-family di-iron enzyme PP_0427
  (Q88QR1), the UbiH + UbiI + Coq7 combination described for *P. aeruginosa*.
- Identities computed this way differ from the values in the OpenScientist reports
  (e.g. 51% for Q88CI2 vs UbiH there), which used a different identity denominator;
  the ranking is the same.

Limitations: pairwise identity is not a phylogeny; no complementation or enzyme
assay of either KT2440 protein exists.
