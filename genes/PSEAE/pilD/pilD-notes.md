# pilD (PA4528, P22610) notes

No deep-research provider was available; this is my own literature review
(PubMed MCP plus cached publications).

## Identity

- UniProt P22610 (LEP4_PSEAE), 290 aa, Swiss-Prot reviewed; locus PA4528;
  synonym xcpA. Matches the worklist accession.
- Peptidase A24 family (MEROPS A24.001; Pfam PF01478 Peptidase_A24 and
  PF06750 A24_N_bact; PANTHER PTHR30487:SF0). Six predicted TM helices,
  cytoplasmic N-terminal domain with four conserved Cys (Zn ligands).
- EC 3.4.23.43 (prepilin peptidase) plus an N-methyltransferase activity.

## Function

- Bifunctional: cleaves the short basic leader peptide of type IV prepilin
  and then N-methylates the new N-terminal Phe using SAM [PMID:8096341 "Here
  we demonstrate that PilD, in addition to cleaving the amino-terminal leader
  sequences of prepilin, also catalyzes N-methylation of the amino-terminal
  phenylalanine of the mature pilin, using S-adenosyl-L-methionine as a methyl
  donor"].
- The four conserved cytoplasmic Cys are needed for full peptidase and
  methylase activity [PMID:8340405 "the 4 conserved cysteines in the
  cytoplasmic domain are required for full peptidase activity in vivo and for
  complete peptidase and methyltransferase activities in vitro"].
- Gly95/Lys96 substitutions separate methylation from cleavage; loss of
  methylation does not prevent pilus assembly [PMID:9668097 "Absence of
  N-methyltransferase activity did not appear to interfere with the ability of
  P. aeruginosa to assemble functional pili"].
- Purified PilD, made cell-free into liposomes, cleaves PilA and methylates
  mature pilin; it binds zinc, which is needed for methylation but not
  cleavage [PMID:23255525 "Zinc is required for the N-terminal methylation of
  the mature pilin, but not for signal peptide cleavage"].
- Type 4 prepilin peptidases are aspartic proteases with an invariant Asp
  pair [PMID:10625704 "In this report we show that the TFPPs represent a
  novel family of bilobed aspartate proteases that is unlike any other
  protease"; "Corresponding aspartate residues are completely conserved
  throughout this extensive peptidase family"]. (Shown for V. cholerae TcpJ
  and VcpD; for PilD the aspartic assignment is by family conservation.)
- Also processes the T2SS pseudopilins XcpT-W, and pilD mutants fail to
  secrete exoproteins (accumulate them in the periplasm) [PMID:1671384
  "pilD mutants accumulate these proteins in the periplasmic space"];
  [PMID:8331069 "This bifunctional enzyme, acting in the inner membrane,
  cleaves the leader peptides from precursors of pilins and XcpT-W"];
  [PMID:1588814 "The N-termini of four of the encoded Xcp proteins display
  similarity to the N-termini of type IV pili, suggesting that XcpA is
  involved in the processing of these Xcp proteins. This could indeed be
  demonstrated in vivo."].
- Inner (cytoplasmic) membrane location [PMID:1898929 "This is consistent with
  a localization in the cytoplasmic membrane in P. aeruginosa, determined
  after specific expression of the xcpA gene"].

## GO term checks

- GO:0004190 aspartic-type endopeptidase activity: correct genus for EC
  3.4.23.43 (under EC 3.4.23 aspartic endopeptidases). The specific term
  GO:0008978 prepilin peptidase activity is obsolete; GO:0042500 (intramembrane
  cleaving) not used: the cleavage site of prepilin is at the cytoplasmic face,
  not clearly within the bilayer.
- GO:0008170 N-methyltransferase activity is general; GO:0071885 N-terminal
  protein N-methyltransferase activity ("transfer of a methyl group from
  S-adenosyl-L-methionine (AdoMet) to the alpha-amino group of the N-terminal
  amino or imino acid residue of a protein substrate") fits exactly.
- GO:0015627 type II protein secretion system complex (part_of, PseudoCAP
  IDA, PMID:1588814). The abstract shows in vivo processing of Xcp
  pseudopilins by XcpA/PilD, not membership of the secretion complex. PilD is
  shared with the T4P system and is a maturation enzyme. Comparator check
  (UniProt reviewed members of PTHR30487, incl. PulO, OutO, E. coli GspO,
  Vibrio TcpJ/VvpD): none carries GO:0015627 or GO:0015628; PilD is the only
  family member with GO:0015627 in QuickGO experimental rows.

## PseudoCAP IBA-seed assessment

PTN000766410 is a Bacteria-level (taxon:2) node of PTHR30487 with 33 leaf IBAs
in 29 taxa (worklist).

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN000766410 | GO:0004190 aspartic-type endopeptidase activity | 1 (sole: P22610) | 33 (29 taxa) | GO:0004190, IDA, PMID:23255525 (PseudoCAP); also UniProt EXP PMID:8096341 | SOUND | Purified PilD cleaves the PilA leader peptide in vitro (23255525) and PilD was the first prepilin peptidase characterised biochemically (8096341). The aspartic mechanism is a family property with invariant Asp pairs (10625704). Endopeptidase activity on prepilin-like substrates is the defining property of A24 prepilin peptidases, so the term suits a Bacteria-level node. |
| PTN000766410 | GO:0005886 plasma membrane | 3 (P22610, E. coli GspO P25960, PppA Q46836) | 33 (29 taxa) | GO:0005886, IDA, PMID:9466269 (PseudoCAP); also UniProt EXP PMID:8331069 | UNVERIFIABLE (PseudoCAP row); IBD SOUND | The claim is right (six TM polytopic inner-membrane protein; PMID:1898929, PMID:8331069), and the IBD has two other seeds plus the UniProt EXP row. But the abstract of PMID:9466269 (xcpT ts mutants and xcpR suppressors) reports no PilD localization; full text not available. Row accepted, reference queried (SUSPECTED). |

## Other PseudoCAP rows

- GO:0008170 N-methyltransferase activity (IDA 8096341): sound, MODIFY to
  GO:0071885.
- GO:0006480 N-terminal protein amino acid methylation (IDA 23255525): sound.
- GO:0009297 pilus assembly (IDA 9668097): MODIFY to type IV pilus assembly;
  the pilus-assembly part of this paper is an in vivo mutant analysis (IMP
  rather than IDA, SUSPECTED defect).
- GO:0043683 type IV pilus assembly (IMP 1671384): sound (restates Nunn et al.
  1990 pilD mutant phenotype).
- GO:0015627 T2SS complex (IDA 1588814): MARK_AS_OVER_ANNOTATED, PSEUDOCAP
  defect PROBABLE.

## Decisions summary

- ACCEPT: aspartic-type endopeptidase activity (EXP, IBA, IDA, IEA); plasma
  membrane (EXP, IBA, IDA, IEA); N-terminal protein amino acid methylation
  (IDA); type IV pilus assembly (IMP).
- MODIFY: N-methyltransferase activity -> N-terminal protein
  N-methyltransferase activity; pilus assembly -> type IV pilus assembly;
  membrane -> plasma membrane.
- MARK_AS_OVER_ANNOTATED: type II protein secretion system complex.
