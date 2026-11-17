# PA4675 / ChtA (Q9HVC0) notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE Q9HVC0 --alias PA4675` (accession fetch). Accession
Q9HVC0 (unreviewed, PE3) matches the worklist. No deep-research keys; literature from the
cached seed paper (PMID:16549659, abstract-only, no PMC full text) and the UniProt record.

## Identity

- TonB-dependent outer-membrane receptor (TBDR). Signal peptide 1-28, plug domain 47-150,
  TonB-dependent beta-barrel 244-699. PTHR30069:SF42 "FERRIC AEROBACTIN RECEPTOR"; Pfam
  Plug + TonB_dep_Rec_b-barrel. No N-terminal signalling extension before the plug, so a
  receptor-transporter, not a TonB-dependent transducer.

## Literature

- ChtA is the outer-membrane receptor for the citrate-hydroxamate xenosiderophores
  [PMID:16549659 "it was demonstrated that ChtA is the outer-membrane receptor for aerobactin."];
  [PMID:16549659 "ChtA also mediated the utilization of rhizobactin 1021 and schizokinen, which are structurally similar to aerobactin."];
  no redundancy [PMID:16549659 "there was no apparent redundancy in the utilization of aerobactin, rhizobactin 1021 and schizokinen"];
  TonB1-dependent [PMID:16549659 "The utilization of citrate hydroxamate siderophores by P. aeruginosa was demonstrated to be TonB1 dependent."]. Fur-regulated.

## Annotation decisions

- Cell outer membrane (IBA, IEA): ACCEPT. Siderophore uptake transmembrane transporter
  activity (IBA, IMP): ACCEPT core. Siderophore-iron import into cell (IEA): ACCEPT.
  Siderophore transmembrane transport (IBA): ACCEPT core process.
- Siderophore-iron transmembrane transporter activity (IEA, GO:0015343): TOO_GENERAL
  (GO:0015344 is its is_a descendant). Siderophore transport (IEA, IMP, GO:0015891):
  TOO_GENERAL (GO:0044718 is its is_a descendant).
- Signaling receptor activity (IEA, GO:0038023): REMOVE. The InterPro2GO mapping is wrong
  for this member: ChtA has only a signal peptide then the plug, no signalling extension,
  so it is not a TonB-dependent transducer. (Same decision as PfeA.)
- Action counts: ACCEPT 6, TOO_GENERAL 3, REMOVE 1. Defects: none recorded (the signaling
  row is an InterPro2GO electronic over-mapping handled by REMOVE, not a PseudoCAP/GO_CENTRAL
  source defect; it is noted here and for the whole family).

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN004738955 | GO:0015344 siderophore uptake transmembrane transporter activity | 4 | 142 (21 taxa) | GO:0015344, IMP, PMID:16549659 | SOUND | chtA mutant cannot use aerobactin, rhizobactin 1021 or schizokinen (no redundancy), TonB1-dependent; ChtA is the outer-membrane receptor for these ferric siderophores. | PfeA (Q05098), FvbA (PA4156, Q9HWM5), PirA (Q9I527) — all PseudoCAP IMP; GO:0044718 at the same node seeded by E. coli CirA (P17315, IMP/IDA) | Yes |

### Node-level assessment, PTN004738955 (recorded here; cross-referenced from PA4156, pirA)

The GO:0015344 IBD at PTN004738955 (PTHR30069 TonB-dependent siderophore receptor clade,
142 leaves in 21 taxa) is seeded by four PAO1 receptors: PfeA (ferric enterobactin,
PMID:8419284), ChtA (this gene), FvbA (vibriobactin) and PirA (ferric enterobactin /
catecholamines). PfeA is independently reviewed (SOUND). The partner process IBD GO:0044718
at the same node is seeded by E. coli CirA (P17315), which carries experimental
GO:0015343/GO:0044718 (EcoCyc). Each seed is a characterized ferric-siderophore receptor, so
the IBD stands and the node term (siderophore uptake transmembrane transporter activity)
suits the clade; no GO_CENTRAL defect. The only caveat is the GO term itself: GO:0015344 is
defined by a proton-coupled ferrioxamine symport reaction (TC 2.A.1.16), which does not
describe a TonB-dependent outer-membrane receptor, yet it is the conventional term for them;
raised as a suggested question.

## PANTHER note

UniProt currently assigns PA4675 to PTHR30069:SF42; the cell-outer-membrane IBA is on the
separate node PTN002824128 (seeded by E. coli FepA/BtuB/CirA/YncD), which is a general TBDR
localization node and is appropriate.
