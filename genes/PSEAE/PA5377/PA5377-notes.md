# PA5377 (Q9HTI7) notes

## Identity: CbcW, the permease, not the ATPase

- Q9HTI7, unreviewed, 279 aa, locus PA5377. Six predicted TM helices and an
  ABC transmembrane type-1 domain (PS50928). NCBIfam TIGR03416
  (ABC_choXWV_perm), InterPro IPR017784 (ABC_transptr_choline_permease),
  PANTHER PTHR47737:SF1 (ProW-like glycine betaine/proline betaine permease).
  [file:PSEAE/PA5377/PA5377-uniprot.txt "ABC_transptr_choline_permease"]
- The operon is PA5378 (CbcX, SBP, Q9HTI6), PA5377 (CbcW, permease, this entry)
  and PA5376 (CbcV, ATPase, Q9HTI8, "Probable ATP-binding component of ABC
  transporter"; UniProt REST, 2026-10-28). The task brief called PA5377
  "CbcV/ATP-binding subunit". That is wrong: PA5377 is the integral membrane
  permease CbcW, and PA5376 is the ATPase CbcV.

## Literature

**Chen et al. 2010, PMID:19919675 (full text cached).** Defines Cbc
(choline/betaine/carnitine) in P. syringae and P. aeruginosa.
- PA14 transposon mutants in each cbc gene, including PA5377, fail to grow on
  choline, betaine and carnitine as sole carbon sources:
  [PMID:19919675 "The PA5376::tn, PA5377::tn and PA5378::tn mutants all failed to grow on choline (Fig. 3A) and betaine (Fig. S2) as sole C sources"]
  [PMID:19919675 "These transposon mutants also failed to grow on L-carnitine (Fig. S2), suggesting that carnitine is an additional substrate for this transporter."]
- Choline uptake by the PA14 cbc mutants is complemented by PAO1 cbcXWV:
  [PMID:19919675 "the deficiencies in choline uptake by PA14 mutants with insertions in individual cbc loci were complemented by cbcXWV from either PAO1 or B728a"]
- PAO1 CbcXWV in E. coli MKH13 takes up choline and betaine but not carnitine:
  [PMID:19919675 "Interestingly, cells of MKH13 transformed with pME6041 expressing cbcXWV from PAO1, pCbcPAO1, accumulated choline and betaine but little to no carnitine."]
- Carnitine needs the separately encoded SBP CaiX (PA5388). The PAO1 core
  CbcWV alone restored carnitine uptake in a P. syringae host that has CaiX:
  [PMID:19919675 "A plasmid expressing only the core transporter, pNcbcWV, was constructed by deleting cbcX from pNcb-cXWV; it restored carnitine uptake to BT (Fig. 5), consistent with an association between the native CaiX SBP and the core transporter."]
  [PMID:19919675 "These findings provide compelling evidence that Psyr_2916 and PA5388, hereafter referred to as CaiX, enable Cbc-mediated carnitine uptake in P. syringae and P. aeruginosa respectively."]
- Substrate specificity sits in the SBPs (CbcX choline > betaine; BetX
  betaine; CaiX carnitine), not in the core CbcWV. P. syringae DC3000 has a
  98-100% identical Cbc core but no caiX, and does not take up carnitine:
  [PMID:19919675 "yet B728a transports carnitine and DC3000 does not"]

**Malek et al. 2011, PMID:21478341 (abstract only; PMC3133218 returned no
body text).** CbcXWV is one of three choline transporters (with BetT1 and
BetT3) supporting growth on choline. cbcXWV is induced by GbdR and glycine
betaine. [PMID:21478341 "BetT3 and CbcXWV, but not BetT1, were sufficient to support growth on choline."]
The abstract does not mention carnitine or betaine uptake. The PseudoCAP rows
citing it for carnitine transmembrane transport and glycine betaine transport
cannot be checked against the text I can read.

**Meadows et al. 2018, PMID:29517479 (abstract only, fetched).** CaiX-CbcWV
imports carnitine and short-chain acylcarnitines:
[PMID:29517479 "Short-chain acylcarnitines are imported by the ABC transporter CaiX-CbcWV."]

**Chen et al. 2013, PMID:23763788 (abstract only).** P. syringae
QAC bioreporters and plant choline. The abstract does not mention sulfur
compounds or PA5377. The basis of the PseudoCAP "sulfur compound
transmembrane transporter activity" IDA cannot be seen (choline-O-sulfate is a
candidate, but unverified).

## Ontology notes

- GO:0005275 amine transmembrane transporter activity is defined for amines
  ("weakly basic ... amino or substituted amino group"). Choline, glycine
  betaine and carnitine are quaternary ammonium compounds, and GO places them
  under GO:0015651 quaternary ammonium group transmembrane transporter
  activity and GO:0015418 ABC-type quaternary ammonium compound transporting
  activity, not under amine transporter (runoak ancestors, go.db). The amine
  term is therefore the wrong branch for Cbc.
- GO:0015871 choline transport is not under GO:0015697 quaternary ammonium
  group transport in the current ontology. GO:0031460 and GO:1902603 are.
- A permease subunit does not hydrolyse ATP, so "enables" an ABC-type
  transporter activity is a complex-level claim. In core_functions I use
  contributes_to GO:0015418, which covers all three SBP-dependent substrates.

## PseudoCAP IBA-seed assessment

All six IBDs sit on one node, PTN000766131 (PTHR47737, taxon Bacteria, 13
leaf IBAs in 11 taxa). Three are co-seeded with E. coli ProW (P14176, the
ProU glycine betaine/proline betaine permease).

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN000766131 | GO:0005275 amine transmembrane transporter activity | 2 (PA5377, ProW) | 13 | GO:0005275, IDA, PMID:19919675 | WRONG | The transport is real, but the substrates (choline, glycine betaine, carnitine; for ProW, betaine and proline betaine) are quaternary ammonium compounds, which GO does not class as amines. The correct branch is GO:0015418/GO:0015651. |
| PTN000766131 | GO:0031460 glycine betaine transport | 2 (PA5377, ProW) | 13 | GO:0031460, IDA, PMID:19919675 and PMID:21478341 | SOUND | PA5377::tn fails to grow on betaine, and PAO1 CbcXWV confers betaine uptake on E. coli MKH13. ProW is a betaine permease. The term suits the ProW/ChoW clade. |
| PTN000766131 | GO:1902603 carnitine transmembrane transport | 1 (sole) | 13 | GO:1902603, IDA, PMID:21478341 | OVER-SPECIFIC | True for PA5377 (PMID:19919675; PMID:29517479), but the cited paper's abstract is about choline. More importantly, carnitine transport depends on the separate SBP CaiX, not the permease: the 98-100% identical DC3000 Cbc does not move carnitine, and ProW in the same node is not a carnitine transporter. Clade-wide propagation is unjustified. |
| PTN000766131 | GO:0015871 choline transport | 1 (sole) | 13 | GO:0015871, IMP, PMID:19919675 | SOUND | Direct mutant and complementation evidence for PA5377, and TIGR03416 is the ChoXWV permease family. For the ProW members of the node, choline is at most a low-affinity substrate, so some leaves may be over-annotated. Acceptable. |
| PTN000766131 | GO:0015226 carnitine transmembrane transporter activity | 1 (sole) | 13 | GO:0015226, IDA, PMID:19919675 | OVER-SPECIFIC | Same SBP-dependence argument as the carnitine process term. For a permease subunit the activity is also complex-level (contributes_to). |
| PTN000766131 | GO:0043190 ATP-binding cassette (ABC) transporter complex | 2 (PA5377, ProW) | 13 | GO:0043190, IDA, PMID:19919675 | SOUND | A TMD of a binding-protein-dependent ABC importer. Complex membership is functionally supported by the operon-dependent uptake. Not purified, but the claim is safe for the whole clade. |

GO_CENTRAL defects are recorded on the IBA rows for GO:0005275 (REPOINT to
GO:0015418) and for the two carnitine IBDs (CHECK, restrict or remove). A
PSEUDOCAP WRONG_TERM defect is on the GO:0005275 IDA row, and WRONG_TERM (CHECK)
defects are on the catabolic-process IDA rows (indirect growth phenotype). A
WRONG_REFERENCE (CHECK) defect is on the carnitine-transport row citing
PMID:21478341.

## Review decisions (summary)

- ACCEPT: ABC transporter complex (IBA, IDA, IEA); plasma membrane; glycine
  betaine transport (IBA, IDA x2, IEA); choline transport (IBA, IMP); carnitine
  transmembrane transport (IBA, IDA), true for PA5377 with CaiX.
- MODIFY: amine transmembrane transporter activity (IBA, IDA) -> GO:0015418;
  carnitine transmembrane transporter activity (IBA, IDA) -> GO:0015418; amine
  transport -> GO:0015697 quaternary ammonium group transport; amino-acid
  betaine transport -> glycine betaine transport + carnitine transmembrane
  transport; membrane -> plasma membrane; transmembrane transporter complex ->
  ABC transporter complex.
- TOO_GENERAL: transmembrane transport.
- MARK_AS_OVER_ANNOTATED: glycine betaine catabolic process; choline catabolic
  process (x2). These are indirect: the transporter is needed for growth on
  these compounds but does not catabolise them.
- UNDECIDED: sulfur compound transmembrane transporter activity (PMID:23763788,
  abstract only, basis unknown).
