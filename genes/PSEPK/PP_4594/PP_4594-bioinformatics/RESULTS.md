# PP_4594 (Q88E72) subfamily placement check

Purpose: independent check of the OpenScientist control-batch report on the
TreeGrafter row GO:0004123 cystathionine gamma-lyase activity (report:
`PP_4594-hypotheses/function-hypothesis-go-0004123/openscientist.md`).

## Method

`placement_identity.py` fetches sequences, EC numbers and PANTHER subfamilies
live from the UniProt REST API, runs a global Needleman-Wunsch alignment
(Biopython, BLOSUM62, gap open -10, extend -0.5) of Q88E72 against each
reference, and reports identity over the shorter sequence. Raw output:
`placement_identity.out`.

```
uv run python placement_identity.py Q88E72 P9WGB7 P18757 P32929 P31373 P13254 P55218 P00935 P06721 Q88NA4 Q88Q39 Q88LD4
```

## Results

| Reference | Activity | EC | PANTHER | Identity to Q88E72 |
|---|---|---|---|---|
| P9WGB7 M. tuberculosis MetB | cystathionine gamma-synthase | 2.5.1.48 | PTHR11808:SF15 | 45.1% |
| P18757 rat Cth | cystathionine gamma-lyase | 4.4.1.1 | PTHR11808:SF15 | 44.5% |
| P32929 human CTH | cystathionine gamma-lyase | 4.4.1.1 | PTHR11808:SF15 | 44.0% |
| P13254 P. putida MdeA | L-methionine gamma-lyase | 4.4.1.11 | PTHR11808:SF80 | 42.5% |
| Q88NA4 KT2440 MdeA (PP_1308) | L-methionine gamma-lyase | 4.4.1.11 | PTHR11808:SF80 | 41.7% |
| P31373 yeast CYS3 | cystathionine gamma-lyase | 4.4.1.1 | PTHR11808:SF15 | 41.0% |
| P55218 P. aeruginosa MetZ | O-succinylhomoserine sulfhydrylase | 2.5.1.- | PTHR11808:SF80 | 40.7% |
| P00935 E. coli MetB | cystathionine gamma-synthase | 2.5.1.48 | PTHR11808:SF75 | 39.1% |
| Q88Q39 KT2440 MetB (PP_0659) | cystathionine gamma-synthase | - | PTHR11808:SF80 | 38.4% |
| Q88LD4 KT2440 MetZ (PP_2001) | O-succinylhomoserine sulfhydrylase | 2.5.1.- | PTHR11808:SF80 | 37.7% |
| P06721 E. coli MetC | cystathionine beta-lyase | 4.4.1.13 | PTHR43500:SF1 | 29.0% |

PLP Schiff-base lysine motif in Q88E72: SASKY, K205.

## Interpretation

- The identities reproduce the report's ranking: the top characterized hit is
  a cystathionine gamma-synthase (Mtb MetB, 45.1%), tied with mammalian
  cystathionine gamma-lyases (44.0-44.5%); all gamma-family activities fall in
  a 38-45% band and only the beta-lyase MetC is clearly more distant (29.0%).
  Sequence identity does not separate the sibling activities.
- PTHR11808:SF15 (official name "CYSTATHIONINE GAMMA-LYASE") is itself mixed:
  it contains the mammalian and yeast cystathionine gamma-lyases and the Mtb
  cystathionine gamma-synthase. PP_4594 is the only KT2440 member of SF15; the
  KT2440 MetB, MetZ and methionine gamma-lyase MdeA are all in SF80.
- The P. putida methionine gamma-lyase P13254 has its KT2440 ortholog in
  MdeA/PP_1308 (82.7% identity in a separate pairwise run, same parameters),
  so PP_4594 is not the methionine gamma-lyase of KT2440, even though P13254
  is one of its closest characterized homologs.
- The catalytic PLP lysine is intact (K205), so this is not a pseudo-enzyme.
