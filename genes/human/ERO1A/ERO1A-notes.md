# ERO1A (ERO1L, ERO1-Lalpha) research notes

UniProt Q96HE7. ER membrane-associated FAD-dependent flavoprotein oxidoreductase (sulfhydryl oxidase), EC 1.8.3.2.

## Core molecular function
- Reoxidizes PDI/P4HB to drive disulfide-bond formation in the ER; passes electrons to O2 via FAD generating H2O2.
  - [file:human/ERO1A/ERO1A-uniprot.txt "Oxidoreductase involved in disulfide bond formation in the endoplasmic reticulum. Efficiently reoxidizes P4HB/PDI, the enzyme catalyzing protein disulfide formation, in order to allow P4HB to sustain additional rounds of disulfide formation. Following P4HB reoxidation, passes its electrons to molecular oxygen via FAD, leading to the production of reactive oxygen species (ROS) in the cell."]
- Selectively oxidizes PDI (not ERp57): [PMID:11707400 "both human Ero1-Lalpha and Ero1-Lbeta (hEROs) facilitate disulfide bond formation in immunoglobulin subunits by selectively oxidizing PDI"]
- FAD cofactor and flavin-dependent oxidase: COFACTOR FAD; crystal structures 3AHQ/3AHR with FAD binding sites (PubMed:20834232). EC 1.8.3.2.
- Catalytic reaction: [protein]-dithiol + O2 = [protein]-disulfide + H2O2 (RHEA:59116) -> GO:0016971 flavin-dependent sulfhydryl oxidase activity.

## Localization
- ER membrane, peripheral membrane protein, lumenal side; retained in ER via ERP44 interaction.
  - [file:human/ERO1A/ERO1A-uniprot.txt "SUBCELLULAR LOCATION: Endoplasmic reticulum membrane"]
- Also Golgi lumen and secreted (PubMed:29858230). Dendrite by similarity (mouse).

## Biological roles
- Required for proper folding of immunoglobulins [PMID:29858230].
- ER stress-induced CHOP-dependent apoptosis via IP3R1 (Ca2+ release) — by similarity/ISS from mouse Q8R180.
- Cholera toxin retrotranslocation: oxidizes PDI to release unfolded toxin (PubMed:12403808).
- Hypoxia-induced (HIF pathway): [file "Stimulated by hypoxia; suggesting that it is regulated via the HIF-pathway."]
- Activity tightly regulated by regulatory disulfides (Cys94-Cys131, Cys99-Cys104) to limit ROS.
- FAM20C phosphorylates Ser145 in Golgi, increasing activity [PMID:29858230].

## Interactions (IPI annotations)
- P4HB/PDI (P07237), PDIA3/ERp57 (P30101), ERP44 (Q9BS26). APPBP2 (Q92624), LHX4 (Q969G2) = HT binary interactome, low-confidence/non-core.
- Note: PMID:11707400 shows Ero1a does NOT affect ERp57 redox state, but PDIA3 binding annotated from IntAct (PMID:17170699, 20802462). KEEP_AS_NON_CORE.

## Action plan
- Core MF: flavin-dependent sulfhydryl oxidase activity (GO:0016971) / protein disulfide isomerase reoxidation.
- thiol oxidase activity (GO:0016972) IDA - ACCEPT (parent of more specific flavin-dependent).
- protein-disulfide reductase activity (GO:0015035 IBA) - the family acts as oxidase not reductase; this IBA is misleading -> MARK_AS_OVER_ANNOTATED / MODIFY. Actually ERO1 is an oxidase; "reductase" IBA likely transferred. MARK_AS_OVER_ANNOTATED.
- oxidoreductase activity (GO:0016491) - ACCEPT as parent (non-core/general).
- FAD binding (GO:0071949) - ACCEPT (structural FAD cofactor).
- protein binding x several - KEEP_AS_NON_CORE (P4HB/PDIA3/ERP44 real, HT ones non-core).
- localizations ER/ER membrane - ACCEPT; Golgi lumen/extracellular/dendrite - KEEP_AS_NON_CORE.
- protein folding / protein folding in ER - KEEP_AS_NON_CORE (downstream BP).
- cell redox homeostasis IMP - ACCEPT (core BP).
- ER stress / apoptosis / Ca release ISS/IEA - KEEP_AS_NON_CORE (mouse-transferred).
- response to temperature stimulus TAS - the yeast complementation of ts mutant; weak, MARK_AS_OVER_ANNOTATED.
- intracellular membrane-bounded organelle / membrane - general, KEEP_AS_NON_CORE.
