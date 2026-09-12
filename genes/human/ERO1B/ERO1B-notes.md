# ERO1B (ERO1LB, ERO1-Lbeta) research notes

UniProt Q86YB8. ER oxidoreductin-1 beta; FAD-dependent sulfhydryl oxidase (EC 1.8.3.2), paralog of ERO1A.

## Core molecular function
- Reoxidizes P4HB/PDI to drive disulfide-bond formation; passes electrons to O2 via FAD producing H2O2.
  - [file:human/ERO1B/ERO1B-uniprot.txt "Oxidoreductase involved in disulfide bond formation in the endoplasmic reticulum. Efficiently reoxidizes P4HB/PDI..."]
- More active than ERO1A, looser regulation: [PMID:21091435 "recombinant human Ero1β is twice as active as Ero1α in enzymatic assays. Ero1β oxidizes PDI more efficiently than other PDI family members"]
- FAD cofactor (PMID:21091435); 7 FAD binding residues mapped by similarity to ERO1A.
- Redox-active center Cys90/Cys95 and Cys393/Cys396. Long-range regulatory disulfides; Cys130 critical for feedback.

## Tissue / biology
- Enriched in professional secretory tissues, esp pancreas (islets of Langerhans), digestive tract, stomach chief cells.
  - [file "In the pancreas, expressed in islets of Langerhans"]
- May function in oxidative proinsulin folding -> glucose homeostasis: [file "May be involved in oxidative proinsulin folding in pancreatic cells, hence may play a role in glucose homeostasis."]
- Induced by UPR: [PMID:10818100 "only ERO1-Lbeta transcripts are induced in the course of the unfolded protein response"]
- Primarily ER-localized: [PMID:10818100 "the products of the ERO1-Lbeta gene are primarily localized in the ER of mammalian cells"]
- Homodimer (disulfide-linked); heterodimer with ERO1A.

## Action plan
- Core MF: flavin-dependent sulfhydryl oxidase activity (GO:0016971) EXP - ACCEPT.
- thiol oxidase activity (GO:0016972) EXP/IDA - ACCEPT (parent).
- protein-disulfide reductase activity (GO:0015035) EXP (Reactome) x3 + IEA: ERO1 is an oxidase not reductase. The "reductase" label mislabels directionality. The physical engagement of PDI disulfides is real but the term direction is wrong -> MARK_AS_OVER_ANNOTATED.
- disulfide oxidoreductase activity (GO:0015036) IEA - ACCEPT (correct directionless parent).
- oxidoreductase activity (GO:0016491) NAS - ACCEPT general.
- FAD binding (GO:0071949) - ACCEPT.
- protein binding (PMID:20802462, PDIA3 P30101) - KEEP_AS_NON_CORE.
- ER / ER membrane / ER lumen / membrane localizations - ACCEPT (ER), KEEP_AS_NON_CORE (generic membrane).
- protein folding / protein folding in ER - KEEP_AS_NON_CORE (downstream BP).
- insulin processing (GO:0030070) TAS Reactome - KEEP_AS_NON_CORE (genuine specialized role in pancreas, proinsulin folding).
