# metZ (Q88LD4) subfamily placement check

Purpose: independent check of the OpenScientist control-batch report on the
TreeGrafter row GO:0016846 carbon-sulfur lyase activity (report:
`metZ-hypotheses/function-hypothesis-go-0016846/openscientist.md`).

## Method

`placement_identity.py` fetches sequences, EC numbers and PANTHER subfamilies
live from the UniProt REST API, runs a global Needleman-Wunsch alignment
(Biopython, BLOSUM62, gap open -10, extend -0.5) of Q88LD4 against each
reference, and reports identity over the shorter sequence. Raw output:
`placement_identity.out`.

```
uv run python placement_identity.py Q88LD4 P55218 P00935 P32929 P06721 P13254 Q88NA4 Q88Q39 Q88E72
```

## Results

| Reference | Activity | EC | PANTHER | Identity to Q88LD4 |
|---|---|---|---|---|
| P55218 P. aeruginosa MetZ | O-succinylhomoserine sulfhydrylase | 2.5.1.- | PTHR11808:SF80 | 82.1% |
| Q88NA4 KT2440 MdeA (PP_1308) | L-methionine gamma-lyase | 4.4.1.11 | PTHR11808:SF80 | 40.2% |
| P13254 P. putida MdeA | L-methionine gamma-lyase | 4.4.1.11 | PTHR11808:SF80 | 39.9% |
| Q88Q39 KT2440 MetB (PP_0659) | cystathionine gamma-synthase | - | PTHR11808:SF80 | 39.5% |
| Q88E72 KT2440 PP_4594 | unresolved gamma-family paralog | - | PTHR11808:SF15 | 37.7% |
| P00935 E. coli MetB | cystathionine gamma-synthase | 2.5.1.48 | PTHR11808:SF75 | 37.0% |
| P32929 human CTH | cystathionine gamma-lyase | 4.4.1.1 | PTHR11808:SF15 | 35.5% |
| P06721 E. coli MetC | cystathionine beta-lyase | 4.4.1.13 | PTHR43500:SF1 | 29.1% |

PLP Schiff-base lysine motif in Q88LD4: SATKF, K219 (matches the UniProt
N6-(pyridoxal phosphate)lysine position).

## Interpretation

- Q88LD4 is the ortholog of the P. aeruginosa O-succinylhomoserine
  sulfhydrylase P55218 (82.1% identity); every other characterized member of
  the family is at 29-40%. This agrees with the report's 82.1% value.
- The catalytic PLP lysine is intact, so this is an active enzyme, not a
  pseudo-enzyme.
- Correction to the report: human CTH (P32929) is in PTHR11808:SF15, not SF80.
  PTHR11808:SF80 (official name "CYSTATHIONINE GAMMA-LYASE") holds metZ
  together with methionine gamma-lyases (MdeA, EC 4.4.1.11, true C-S lyases)
  and the KT2440 cystathionine gamma-synthase MetB. The TreeGrafter node
  therefore spans both gamma-elimination (lyase) and gamma-replacement
  (transferase) activities; the carbon-sulfur lyase term is correct for some
  descendants and not for the MetZ clade.
- UniProt P55218 cites PubMed 7704274 with experimental evidence
  (ECO:0000269) for the O-succinyl-L-homoserine + hydrogen sulfide reaction
  (RHEA:27826). That paper is not cached in `publications/`, so it is a lead
  rather than a quotable source here.
