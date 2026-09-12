# PIGG (Q5H8A4) review notes

Human PIGG = GPI ethanolamine phosphate transferase 2, catalytic subunit (aka GPI7 homolog / hGPI7 / PIG-G).
Falcon deep research OUT OF CREDITS (HTTP 402) at time of review; grounded in UniProt, seeded GOA, and cached publications.

## Core biology
- PIGG is the catalytic subunit of the GPI-ethanolamine-phosphate transferase II (GPI-ETII) complex.
  It transfers ethanolamine phosphate (EtNP), donated from phosphatidylethanolamine (PE), onto the
  6-OH of the **second** mannose of the GPI intermediate (H7 -> H8 conversion). This is a side-branch
  EtNP that is normally shortly removed from the GPI-anchored protein after anchoring.
  [PMID:15632136 "By attachment of an additional ethanolamine phosphate (EtNP) to the second mannose"]
  [PMID:34113002 "PIGG is involved in transfer of EtNP to the second mannose before attachment of proteins"]
- Works with the accessory/regulatory subunit **PIGF**, which stabilizes it; PIGG competes with PIGO
  (GPI-ETIII, EtNP on 3rd mannose) for the shared stabilizer PIGF.
  [PMID:15632136 "associated with and stabilized by PIG-F"]
  [PMID:32156170 "Both PIGO and PIGG are stabilized by association with PIGF"]
- Multi-pass ER membrane protein (12 predicted TM helices; large N-terminal lumenal domain harboring
  the alkaline-phosphatase-like catalytic core); acts in the ER during GPI-anchor biosynthesis
  (step 11 of the pathway). [UniProt SUBCELLULAR LOCATION / PATHWAY]

## Disease
- Biallelic LoF variants cause an inherited GPI-deficiency disorder: neurodevelopmental disorder with/without
  hypotonia, seizures, and cerebellar atrophy (NEDHSCA; MIM:616917) -> DD/ID, hypotonia, early-onset (mostly
  febrile) seizures, cerebellar atrophy, ataxia. Unusually for IGDs, alkaline phosphatase and granulocyte
  GPI-AP surface levels are often normal (fibroblast CD73 is the sensitive readout).
  [PMID:34113002] [PMID:26996948 - not cached; UniProt DISEASE]
- Genetic variation in PIGG also defines the Emm blood group system (Emm-null phenotype). [UniProt POLYMORPHISM; PMID:34535746]

## GOA MF term
- GOA carries **GO:0051377 mannose-ethanolamine phosphotransferase activity** for the IBA/IEA/IDA MF rows.
- The UniProt DR line lists GO:0051267 "CP2 mannose-ethanolamine phosphotransferase activity" for the IDA (MGI),
  but GO:0051267 is now **OBSOLETE** (QuickGO). The current/valid term to use is GO:0051377.

## Annotation decisions summary
- MF GO:0051377 (IBA, IEA, IDA): ACCEPT - core enzymatic activity.
- BP GO:0006506 GPI anchor biosynthetic process (IBA, IEA, TAS, IDA/acts_upstream): ACCEPT - core process.
- CC GO:0005789 ER membrane (IBA is_active_in, IEA, EXP, NAS, TAS): ACCEPT - correct location of action.
- CC GO:0005783 ER (IDA): ACCEPT (broader parent of ER membrane; consistent).
- CC GO:0016020 membrane (HDA, NK-cell membrane proteome MS): MARK_AS_OVER_ANNOTATED - uninformative parent; ER membrane is the specific/correct term.
- MF GO:0016740 transferase activity (IMP, PMID:34113002): MODIFY -> GO:0051377 (the IMP variant assay measures EtNP-transferase activity; the generic parent should be replaced by the specific MF).
- MF GO:0016780 phosphotransferase activity, for other substituted phosphate groups (TAS Reactome): ACCEPT (correct broader parent, TAS from Reactome; kept as-is, non-core-ish parent but sound).
- MF GO:0005515 protein binding (IPI, PMID:23864651, with GLP1R): MARK_AS_OVER_ANNOTATED - bare protein binding from a high-throughput GLP1R interactome screen; not the informative catalytic function.
