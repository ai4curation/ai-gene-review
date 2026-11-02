# aslB (P25550) notes

Deep research was unavailable for this gene (no deep-research provider run; RADICAL_SAM
project Phase 2). Notes are built from cached primary literature, PubMed searches,
the UniProt record and a local sequence analysis.

## Identity and family

- 411 aa radical SAM protein; UniProt name "Anaerobic sulfatase-maturating enzyme homolog
  AslB" [file:ECOLI/aslB/aslB-uniprot.txt "Belongs to the radical SAM superfamily. Anaerobic
  sulfatase-maturating enzyme family."]. Radical SAM core plus a C-terminal SPASM domain
  (Pfam PF13186; NCBIfam TIGR04085 rSAM_more_4Fe4S; TIGR03942 sulfatase_rSAM).
- UniProt cluster and SAM-binding features are all ECO:0000250 transfers from the
  C. perfringens Cys-type anSME (Q0TTH1).
- Gene b3800 is adjacent to aslA (b3801), a putative periplasmic Ser-type sulfatase whose
  catalytic Ser136 is predicted to become formylglycine (UniProt P25549, by similarity).
  No E. coli strain has detectable arylsulfatase activity (UniProt P25549 FUNCTION).

## Literature

- anSME family defined by Berteau et al. 2006: the C. perfringens enzyme converts the
  active-site Cys of a sulfatase to formylglycine anaerobically
  [PMID:16766528 "we have also identified a new Cys-type sulfatase-maturating enzyme that
  catalyzes the conversion of cysteine into FGly"]. This is the reference behind the ISS
  protein maturation row; it is about the Firmicutes enzyme, not E. coli AslB.
- Klebsiella AtsB, the Ser-type anSME, needs SAM and its three FeS centres to make FGly
  from serine [PMID:14749327 "SAM is the critical co-factor for formation of a functional
  AtsB.SAM.sulfatase complex and for FGly formation by AtsB"].
- E. coli K-12 aslB, ydeM and yidF knockouts do not impair Cys-type sulfatase maturation,
  which happens only aerobically [PMID:17303125 "knocking-out of aslB, ydeM and yidF does
  not impair Cys-type sulfatase maturation"]. Ser-type maturation (the presumed AslA
  substrate type) was not tested in that abstract.
- Contrary report in E. coli BL21(DE3): co-expressing AslB with human IDS or GALNS
  raised sulfatase activity 1.5 to 4.6-fold [PMID:28882567 "IDS activity was increased in
  4.6-fold when co-expressed with AslB"]. Activity readout only; FGly formation was not
  reported in the abstract, the strain is B not K-12, and the effect is modest. Treated as
  low-quality, unconfirmed evidence.
- No biochemical study of purified E. coli AslB found (PubMed search 2026-10-19:
  "(aslB OR ydeM OR AtsB) AND Escherichia coli AND (sulfatase OR radical SAM)").

## Bioinformatics (file:ECOLI/aslB/aslB-bioinformatics/RESULTS.md)

- AslB keeps all 11 cysteine ligands of the three anSMEcpe [4Fe-4S] clusters and the
  catalytic base (anSMEcpe D277 = AslB D298); 16 of 17 reference features conserved.
- AslB is 44.7% identical to Ser-type AtsB, 43.2% to YdeM, 34.9% to anSMEcpe.
- Interpretation: catalytic machinery intact, so AslB is probably an active enzyme, but
  its substrate is unknown.

## Curation decisions

- Generic rows per RADICAL_SAM treatment rule: no reaction established, so GO:0003824 and
  GO:0051539 are KEEP_AS_NON_CORE; GO:0051536 MODIFY to GO:0051539.
- GO:0016491 oxidoreductase activity (IPR023867): UNDECIDED; family chemistry, not shown.
- GO:0051604 protein maturation (ISS): UNDECIDED, because the evidence conflicts (K-12
  knockout negative for Cys-type; BL21 overexpression positive) and the Ser-type AslA
  substrate was never tested.
- No NEW rows; no SAM-binding NEW because catalysis is not established.
