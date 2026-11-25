# PA5376 (Q9HTI8) notes

## Identity: CbcV, the ATPase of the Cbc QAC importer

- Q9HTI8, unreviewed, locus PA5376, "Probable ATP-binding component of ABC
  transporter". ABC transporter ATP-binding domain (PF00005, PS50893),
  NCBIfam TIGR03415 (ABC_choXWV_ATP), InterPro IPR022473
  (ABC_trnsptr_Choline_ATP-bd), PANTHER PTHR43869:SF1 (ProV-like glycine
  betaine/proline betaine ATPase). [file:PSEAE/PA5376/PA5376-uniprot.txt "ABC_choXWV_ATP"]
- Operon cbcXWV = PA5378 (CbcX, SBP), PA5377 (CbcW, permease; reviewed in
  genes/PSEAE/PA5377) and PA5376 (CbcV, ATPase, this entry).
  [PMID:19919675 "In addition to the core transporter comprised of a transmembrane protein (CbcW) and an ATPase (CbcV), the Cbc transporter system interacts with at least three SBPs"]

## Literature

**Chen et al. 2010, PMID:19919675 (full text cached).**
- PA14 PA5376::tn fails to grow on choline, betaine and carnitine:
  [PMID:19919675 "The PA5376::tn, PA5377::tn and PA5378::tn mutants all failed to grow on choline (Fig. 3A) and betaine (Fig. S2) as sole C sources"]
  [PMID:19919675 "These transposon mutants also failed to grow on L-carnitine (Fig. S2), suggesting that carnitine is an additional substrate for this transporter."]
- Complementation with PAO1 cbcXWV, and heterologous uptake in E. coli MKH13:
  [PMID:19919675 "the deficiencies in choline uptake by PA14 mutants with insertions in individual cbc loci were complemented by cbcXWV from either PAO1 or B728a"]
  [PMID:19919675 "Interestingly, cells of MKH13 transformed with pME6041 expressing cbcXWV from PAO1, pCbcPAO1, accumulated choline and betaine but little to no carnitine."]
- Carnitine needs the trans-encoded SBP CaiX (PA5388):
  [PMID:19919675 "These findings provide compelling evidence that Psyr_2916 and PA5388, hereafter referred to as CaiX, enable Cbc-mediated carnitine uptake in P. syringae and P. aeruginosa respectively."]

**Malek et al. 2011, PMID:21478341 (abstract only).** CbcXWV supports growth on
choline; CbcXWV and BetT1 dominate under hypo-osmolar conditions, BetT3 under
hyperosmolar ones. [PMID:21478341 "BetT3 and CbcXWV, but not BetT1, were sufficient to support growth on choline."]
No osmoprotective role shown for Cbc, so the ARBA "response to osmotic
stress" row is marked over-annotated.

**Meadows et al. 2018, PMID:29517479 (abstract only).**
[PMID:29517479 "Short-chain acylcarnitines are imported by the ABC transporter CaiX-CbcWV."]

**Chen et al. 2013, PMID:23763788 (abstract only).** P. syringae QAC
bioreporters. The abstract mentions neither sulfate nor PA5376, so the
PseudoCAP "ABC-type sulfate transporter activity" and "sulfur compound
transmembrane transporter activity" IDAs cannot be checked. Inorganic sulfate
is implausible for a ProV/ChoV-type QAC importer; choline-O-sulfate is a
candidate. UNDECIDED, with a SUSPECTED PSEUDOCAP WRONG_TERM (CHECK) on the
sulfate row.

## Ontology notes (same as PA5377)

- GO:0005275 amine transmembrane transporter activity is the wrong branch for
  quaternary ammonium compounds; GO:0015418 ABC-type QAC transporting activity
  is right.
- GO:0031459 (glycine betaine) is_a GO:0015418; GO:0033266 (choline) is_a
  GO:0015220 but not GO:0015418. GO:0015418 is kept (ACCEPT) as the only term
  that covers the CaiX-dependent carnitine mode.
- GO:0055052 (substrate-binding subunit-containing ABC complex) is accepted, so
  the GO:0043190 rows are TOO_GENERAL, although the claim and the IBD are sound.

## PseudoCAP IBA-seed assessment

Seeds from .cache/paint/IBD.gaf (column 8), other seeds' experimental rows
from QuickGO (2026-11-05).

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002466744 | GO:0043190 ATP-binding cassette (ABC) transporter complex | 2 | 14 (12 taxa) | GO:0043190, IDA, PMID:19919675 | SOUND | CbcV is the NBD of the binding protein-dependent CbcWV importer; mutant and complementation data support the complex. Term suits all ABC NBDs in the clade. | E. coli ProV P14175 (ComplexPortal ProU complex GO:1990222 IPI, PMID:23249124) | Yes |
| PTN002466744 | GO:0005275 amine transmembrane transporter activity | 2 | 14 (12 taxa) | GO:0005275, IDA, PMID:19919675 | WRONG | Transport is real, but choline, betaine and carnitine are quaternary ammonium compounds, not amines in GO; correct branch GO:0015418. | E. coli ProV P14175 (EcoCyc GO:0005275 IDA, PMID:23249124; glycine betaine/proline betaine, also QACs) | No: the other seed has the same branch error, so the node term does not suit the clade. GO_CENTRAL REPOINT to GO:0015418 (PROBABLE) recorded on the IBA row. |

Defects: PSEUDOCAP WRONG_TERM GO:0005275 (CONFIRMED, full text read);
GO_CENTRAL WRONG_TERM PTN002466744 GO:0005275 (PROBABLE). Further PSEUDOCAP
CHECKs (not seeds): two catabolic-process rows (PROBABLE, indirect growth
phenotype), sulfate transporter (SUSPECTED), carnitine transport reference
PMID:21478341 (SUSPECTED). These mirror the PA5377 review, whose permease
node PTN000766131 carries the parallel GO:0005275 IBD error.
