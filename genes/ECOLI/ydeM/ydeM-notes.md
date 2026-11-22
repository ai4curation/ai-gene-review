# ydeM (P76134) notes

Deep research was unavailable for this gene (no deep-research provider run; RADICAL_SAM
project Phase 2). Notes are built from cached primary literature, PubMed searches, the
UniProt record and the shared paralog analysis in the aslB folder.

## Identity and family

- 385 aa radical SAM + SPASM protein, anSME family; UniProt "Anaerobic
  sulfatase-maturating enzyme homolog YdeM" [file:ECOLI/ydeM/ydeM-uniprot.txt "Belongs to
  the radical SAM superfamily. Anaerobic sulfatase-maturating enzyme family."].
- All UniProt cluster and SAM features are ECO:0000250 from C. perfringens anSME Q0TTH1.
- ydeM (b1497) is adjacent to ydeN (b1498, UniProt P77318), an uncharacterized
  sulfatase-family protein whose Ser132 is predicted (by similarity) to become
  formylglycine, i.e. a Ser-type sulfatase candidate. The same arrangement holds for aslB
  (b3800) next to aslA (b3801, Ser136). E. coli K-12 sulfatase-family proteins (UniProt
  query 2026-10-19): AslA, YdeN, YidJ, plus the unrelated alkylsulfatase YjcS.

## Literature

- Family definition: [PMID:16766528 "This finding leads to the definition of a new enzyme
  family of sulfatase-maturating enzymes that we have named anSME"]. Firmicutes enzyme;
  GOA reference for the ISS protein maturation row.
- K-12 knockouts of aslB, ydeM and yidF do not impair Cys-type sulfatase maturation
  [PMID:17303125 "these putative anSME are not involved in Cys-type sulfatase maturation"].
- ydeM is among about 30% of E. coli genes whose expression changed after mitomycin C
  [PMID:11967071 "a large number of genes (nearly 30% of all genes) displayed significant
  changes in their expression level"]. This is the IEP DNA damage response row.
- PubMed 2026-10-19: no study of purified YdeM; the BL21 AslB co-expression paper
  (PMID:28882567) did not test YdeM.

## Bioinformatics (file:ECOLI/aslB/aslB-bioinformatics/RESULTS.md)

- YdeM keeps all 17 anSMEcpe reference features (11 cluster cysteines, 5 SAM contacts,
  catalytic D279). 35.0% identical to anSMEcpe, 36.4% to AtsB, 43.2% to AslB.

## Curation decisions

- Generic rows per RADICAL_SAM rule (no reaction established): GO:0003824 and GO:0051539
  KEEP_AS_NON_CORE; GO:0051536 MODIFY to GO:0051539. GO:0016491 UNDECIDED.
- GO:0051604 protein maturation (ISS): UNDECIDED, same as aslB. Cys-type sulfatase
  maturation was tested in ydeM-deleted K-12 and not affected, but the candidate substrate
  next to ydeM, YdeN, is a predicted Ser-type sulfatase and Ser-type maturation was not
  tested. I first leaned to REMOVE before finding the ydeN adjacency.
- GO:0006974 DNA damage response (IEP): MARK_AS_OVER_ANNOTATED (expression change in a
  genome-wide transcriptional response; no evidence YdeM does any work in DNA damage
  responses). Other E. coli reviews in the repo use MARK_AS_OVER_ANNOTATED (glgX, pstA,
  pstS) or REMOVE (glpK) for this paper.
