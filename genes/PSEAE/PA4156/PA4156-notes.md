# PA4156 / FvbA (Q9HWM5) notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE Q9HWM5 --alias PA4156` (accession fetch). Accession
Q9HWM5 (unreviewed, PE3) matches the worklist. No deep-research keys; literature from the
cached seed paper (PMID:21546589, abstract-only) and the UniProt record.

## Identity

- TonB-dependent outer-membrane receptor. Signal peptide 1-29, plug 56-171, beta-barrel
  270-658. Pfam Plug + TonB_dep_Rec_b-barrel. UniProt places it in PANTHER PTHR32552
  (ferrichrome iron receptor-related); PAINT seeded the GO:0015344 IBD at PTN004738955
  (PTHR30069). Close homologue of the V. cholerae vibriobactin receptor ViuA.

## Literature

- FvbA required for vibriobactin use
  [PMID:21546589 "we identified a P. aeruginosa gene, PA4156 (fvbA), encoding a protein highly homologous to the V. cholerae vibriobactin receptor (ViuA)"];
  [PMID:21546589 "A P. aeruginosa mutant in the two endogenous siderophores (pyoverdine and pyochelin) and in fvbA was unable to utilize vibriobactin as an iron source."].
  Fur- and FvbR-regulated (described as preliminary)
  [PMID:21546589 "preliminary analyses revealed the involvement of vibriobactin, Fur protein and an IclR-type regulator, FvbR (PA4157), in fvbA regulation"].

## Annotation decisions

- Cell outer membrane (IBA, IEA): ACCEPT. Siderophore uptake transmembrane transporter
  activity (IBA, IMP): ACCEPT core. Siderophore-iron import into cell (IEA): ACCEPT.
  Siderophore transmembrane transport (IBA): ACCEPT core process.
- Siderophore transport (IMP, GO:0015891): TOO_GENERAL (GO:0044718 is its is_a descendant).
- Cellular response to iron ion (EXP, GO:0071281, CollecTF, PMID:21546589):
  MARK_AS_OVER_ANNOTATED. The evidence is that fvbA expression is Fur/vibriobactin/FvbR
  controlled, i.e. fvbA is a Fur target, not a participant in the iron response; iron-regulated
  expression of a target gene is not a role in responding to iron (Fur itself carries the
  term). Abstract calls the regulation analysis preliminary.
- Action counts: ACCEPT 5, TOO_GENERAL 1, MARK_AS_OVER_ANNOTATED 1.
- No source defect on the PseudoCAP seed (sound). The GO:0071281 row is CollecTF, not
  PseudoCAP; handled by MARK_AS_OVER_ANNOTATED rather than a source defect.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN004738955 | GO:0015344 siderophore uptake transmembrane transporter activity | 4 | 142 (21 taxa) | GO:0015344, IMP, PMID:21546589 | SOUND | fvbA mutant (in a pvd/pch-null background) cannot use vibriobactin; FvbA is homologous to the V. cholerae vibriobactin receptor ViuA. Direct genetic evidence for ferric-siderophore uptake. | PfeA (Q05098), ChtA (PA4675, Q9HVC0), PirA (Q9I527) — PseudoCAP IMP; E. coli CirA (P17315) at the partner process IBD | Yes |

The node-level assessment of PTN004738955 is recorded once in `PA4675-notes.md` (IBD sound,
node term suits the clade, no GO_CENTRAL defect). FvbA is consistent with it.
