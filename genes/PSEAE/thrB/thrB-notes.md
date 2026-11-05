# thrB (PA5495, P29364) notes

## Identity

- UniProt P29364 (KHSE_PSEAE), 316 aa, Swiss-Prot reviewed, PE 3 (inferred from
  homology). Homoserine kinase type II (HAMAP MF_00301 Homoser_kinase_2, NCBIfam
  TIGR00938 thrB_alt, InterPro IPR005280, "pseudomonas-type ThrB family"); an
  aminoglycoside phosphotransferase (APH, Pfam PF01636) / protein-kinase-like fold
  enzyme, unrelated to the GHMP-family ThrB of E. coli and B. subtilis.
- Catalytic activity in the entry is the HAMAP reaction (L-homoserine + ATP =
  O-phospho-L-homoserine + ADP), step 4/5 of threonine synthesis from aspartate
  [file:PSEAE/thrB/thrB-uniprot.txt "L-threonine biosynthesis; L-threonine from L-aspartate: step 4/5."].

## Biology (literature)

- Cloning: hom, thrB and thrC cloned and sequenced; thrB lies apart from hom-thrC
  and its product resembles no known ThrB; insertional inactivation gave no
  phenotype, so an isozyme was postulated
  [PMID:1333566 "No phenotype could be detected when the chromosomal thrB gene was inactivated by an insertion."].
- Redundancy with ThrH: only the thrB thrH double mutant is a threonine
  auxotroph [PMID:10220164 "In P. aeruginosa, threonine auxotrophy is observed only when both thrB and thrH are simultaneously inactivated."].
  ThrH is not an ATP-dependent kinase: it is a phosphoserine phosphatase with
  phosphoserine:homoserine phosphotransferase activity
  [PMID:14699121 "ThrH has a novel phosphoserine:homoserine phosphotransferase activity"].
  So ThrB is the ATP-dependent homoserine kinase of PAO1, inferred from family
  membership plus genetics.
- No direct enzyme assay of purified PA5495 was found (PubMed search
  "homoserine kinase Pseudomonas aeruginosa thrB" returns only PMID:1333566,
  PMID:10220164, PMID:14699121). The cited 1999 abstract assays no ThrB activity;
  the full text is not available.
- Consistency with genes/PSEAE/hom: that review found PseudoCAP attached
  PMID:10220164 (all IDA, same date) to hom, thrB and thrH, and judged it the wrong
  paper for hom. For thrB it is the right paper (it is about thrB); the issue here
  is the evidence code, not the reference.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN001464661 | GO:0009088 L-threonine biosynthetic process | 1 (sole seed) | 10 (10 taxa) | GO:0009088 L-threonine biosynthetic process, IDA, PMID:10220164 (PseudoCAP) | SOUND | The paper shows that thrB contributes to threonine synthesis (double thrB thrH mutant is auxotrophic), and ThrB catalyses step 4. This is genetic-interaction evidence, so IGI not IDA. Node breadth is a concern: the node also covers B. subtilis AmiN/YerI (O34640), an experimentally characterised amicoumacin kinase in an organism that has a GHMP ThrB, plus uncharacterised Synechocystis sll1119 and Deinococcus DR_0394. |
| PTN001464661 | GO:0004413 homoserine kinase activity | 1 (sole seed) | 10 (10 taxa) | GO:0004413 homoserine kinase activity, IDA, PMID:10220164 (PseudoCAP) | UNVERIFIABLE | The abstract contains no direct assay of ThrB; it is a genetic study. The activity is very probably right for PA5495 (HAMAP MF_00301, gene redundancy with ThrH, which does the reaction by a different chemistry), so the IBD conclusion is plausible for true type II HSKs. But its only anchor is an IDA whose assay is not visible, and the node includes AmiN, whose characterised activity is antibiotic phosphorylation. |
| PTN001464650 | GO:0019202 amino acid kinase activity | 2 | 53 (34 taxa) | GO:0004413 homoserine kinase activity, IDA, PMID:10220164 (PseudoCAP); second seed human HYKK (A2RU49) | SOUND | Broad term at a node spanning type II HSK and animal hydroxylysine kinases; both seeds are amino acid kinases, and the HYKK seed supports the IBD independently of PseudoCAP. Leaves are mainly metazoan HYKK, for which the general term is correct. |

## Decisions summary

- ACCEPT: homoserine kinase activity (IBA, IEA, IDA), L-threonine biosynthetic
  process (IBA, IEA, IDA).
- PSEUDOCAP: WRONG_EVIDENCE_CODE CHECK on both IDA rows (PROBABLE for the BP,
  which is genetic, IGI; SUSPECTED for the MF, since the full text might contain an
  extract assay).
- GO_CENTRAL: MISSING_NEGATION CHECK (SUSPECTED) for B. subtilis AmiN/YerI under
  PTN001464661.
