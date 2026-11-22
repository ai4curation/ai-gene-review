# fabG (Escherichia coli K-12, UniProtKB:P0AEK2) — curation notes

Reviewed for `modules/type_ii_fatty_acid_synthesis.yaml` as the E. coli
representative of the FabG ketoreduction step. FabG reduces beta-ketoacyl-ACP with
NADPH
[PMID:14996818 "FabG, beta-ketoacyl-acyl carrier protein (ACP) reductase, performs the NADPH-dependent reduction of beta-ketoacyl-ACP substrates to beta-hydroxyacyl-ACP products, the first reductive step in the elongation cycle of fatty acid biosynthesis."]
and is essential and non-redundant: conditional mutants stop making acyl-ACP
intermediates at the non-permissive temperature
[PMID:14996818 "Moreover, synthesis of the acyl-ACP intermediates of the pathway was inhibited upon shift of mutant cultures to the nonpermissive temperature, indicating blockage of the synthetic cycle."].

Two decisions worth recording. The `GO:0051287` NAD-binding row is MODIFYed to
`GO:0050661` NADP binding: the enzyme is NADPH-specific and NADP(H) binding is shown
structurally
[PMID:15016358 "Biochemical data confirm that FabG[Y151F] is defective in NADPH binding."],
so the InterPro mapping names the wrong nucleotide — recorded as a `WRONG_TERM`
source defect against InterPro, the same correction made for the NADH row of
B. subtilis fabL in this batch. The `GO:0016616` IBA is TOO_GENERAL rather than
removed, because unlike FabL (a C=C reductase in the same SDR superfamily) FabG
really does act on a CH-OH group; the node PTN002449287 is in fact seeded by FabG
itself, which is expected, not circular.

## Annotation decisions (20 GOA rows)

| GO term | Evidence | Action | Rationale in brief |
|---|---|---|---|
| GO:0004316 3-oxoacyl-[acyl-carrier-protein] reductase (NADPH) activity | EXP | ACCEPT | The core NADPH-dependent ketoreductase activity, from the reconstitution of a complete round of E. coli fatty-acid synthesis with purified enzymes. |
| GO:0004316 3-oxoacyl-[acyl-carrier-protein] reductase (NADPH) activity | EXP | ACCEPT | Core ketoreductase activity, from the study of the FAS-II elongation cycle in vitro. |
| GO:0004316 3-oxoacyl-[acyl-carrier-protein] reductase (NADPH) activity | EXP | ACCEPT | Core ketoreductase activity, assayed in the reconstituted synthase used to study FabH. |
| GO:0004316 3-oxoacyl-[acyl-carrier-protein] reductase (NADPH) activity | EXP | ACCEPT | Core ketoreductase activity, in the reconstituted elongation cycles used to compare FabA and FabZ. |
| GO:0004316 3-oxoacyl-[acyl-carrier-protein] reductase (NADPH) activity | IDA | ACCEPT | Ketoreductase activity measured directly, in the study that mapped the ACP-binding surface of FabG. |
| GO:0004316 3-oxoacyl-[acyl-carrier-protein] reductase (NADPH) activity | IEA | ACCEPT | Electronic assignment of the core activity from the FabG family signature, Rhea and EC. |
| GO:0004316 3-oxoacyl-[acyl-carrier-protein] reductase (NADPH) activity | IMP | ACCEPT | Loss-of-function evidence for the activity: conditional fabG mutants have thermolabile ketoreductase activity and stop making fatty acids. |
| GO:0005829 cytosol | IDA | ACCEPT | Cytosolic localization from fractionation-based proteomic assignment. |
| GO:0005829 cytosol | IDA | ACCEPT | Cytosolic localization from abundance profiling of the cytosolic fraction. |
| GO:0006633 fatty acid biosynthetic process | IEA | ACCEPT | Fatty-acid biosynthesis is the pathway the FabG reduction serves. |
| GO:0006633 fatty acid biosynthetic process | IMP | ACCEPT | Mutant evidence that FabG is required for, and acts in, fatty-acid biosynthesis. |
| GO:0008610 lipid biosynthetic process | IMP | TOO_GENERAL | Correct but uninformative process: the fatty-acid biosynthesis and elongation terms asserted in this review entail it. |
| GO:0009102 biotin biosynthetic process | IMP | KEEP_AS_NON_CORE | The pimeloyl moiety of biotin is built by a diverted round of fatty-acid elongation that uses FabG; a real secondary use of the core activity. |
| GO:0016616 oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor | IBA | TOO_GENERAL | Correct but uninformative parent activity; the exact NADPH ketoreductase term is asserted on seven rows of this review. |
| GO:0030497 fatty acid elongation | IBA | ACCEPT | Phylogenetic assignment of fatty-acid elongation across the FabG clade. |
| GO:0030497 fatty acid elongation | IEA | ACCEPT | Electronic assignment of fatty-acid elongation. |
| GO:0030497 fatty acid elongation | IMP | ACCEPT | Mutant evidence that elongation stops without FabG: acyl-ACP intermediates are not made at the non-permissive temperature. |
| GO:0042802 identical protein binding | IDA | KEEP_AS_NON_CORE | Self-association: FabG is a homotetramer whose subunits communicate allosterically. |
| GO:0050661 NADP binding | IDA | KEEP_AS_NON_CORE | NADP binding, shown by the FabG-NADP(H) complex structures. |
| GO:0051287 NAD binding | IEA | MODIFY -> GO:0050661 | NAD binding, mapped from the FabG family signature, but the enzyme's cofactor is NADP(H). |

**Core function:** enables GO:0004316 3-oxoacyl-[acyl-carrier-protein] reductase (NADPH) activity; in GO:0006633, GO:0030497; located in GO:0005829

