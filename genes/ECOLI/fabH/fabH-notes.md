# fabH (Escherichia coli K-12, UniProtKB:P0A6R0) — curation notes

Reviewed for `modules/type_ii_fatty_acid_synthesis.yaml` as the E. coli
representative of KAS III chain initiation. Note the family split: E. coli FabH is
in PANTHER PTHR43091 while the P. putida FabH enzymes are in PTHR34069, so this
review is the grounding for the new PTHR43091 family review.

FabH condenses an acetyl-CoA primer with malonyl-ACP (Km 40 uM and 5 uM)
[PMID:8631920 "FabH exhibited a Km of 40 microM for acetyl-CoA and 5 microM for malonyl-ACP."]
and rejects medium-chain and branched primers, which is why E. coli makes
straight-chain fatty acids
[PMID:10629181 "Reconstitution of a complete round of fatty acid synthesis in vitro with purified E. coli proteins showed that eFabH was the only E. coli enzyme incapable of using branched-chain substrates."].
It is feedback-inhibited by long-chain acyl-ACPs
[PMID:8631920 "Acyl-ACPs suppressed Fabh activity, and their potency increased with increasing acyl chain length between 12 and 20 carbon atoms."].

The one substantive correction is the `GO:0004315` row: that term names the
elongation condensation of acyl-ACP with malonyl-ACP, the FabB/FabF reaction, while
FabH uses an acyl-CoA primer. `GO:0033818` is not a descendant of `GO:0004315`, so
this is MODIFY as a lateral substrate correction, not a refinement.

## Annotation decisions (15 GOA rows)

| GO term | Evidence | Action | Rationale in brief |
|---|---|---|---|
| GO:0004315 3-oxoacyl-[acyl-carrier-protein] synthase activity | IEA | MODIFY -> GO:0033818 | Condensing activity assigned from domain signatures, but with the wrong substrate: the KAS III reaction uses an acyl-CoA primer, not acyl-ACP. |
| GO:0005737 cytoplasm | IEA | ACCEPT | Cytoplasmic location of a soluble FAS-II condensing enzyme. |
| GO:0005829 cytosol | IDA | ACCEPT | Cytosolic localization from fractionation-based proteomic assignment of the E. coli proteome. |
| GO:0005829 cytosol | IDA | ACCEPT | Cytosolic localization from abundance profiling of the E. coli cytosolic fraction. |
| GO:0006631 fatty acid metabolic process | IMP | TOO_GENERAL | Correct but uninformative process: the specific biosynthetic terms are asserted elsewhere in this review. |
| GO:0006633 fatty acid biosynthetic process | IEA | ACCEPT | Fatty-acid biosynthesis is the pathway FabH initiates. |
| GO:0016746 acyltransferase activity | IEA | TOO_GENERAL | Correct but uninformative parent activity; the exact KAS III term is asserted on seven other rows. |
| GO:0030497 fatty acid elongation | IBA | ACCEPT | Phylogenetic assignment of fatty-acid elongation across the KAS III clade; the process FabH's condensation belongs to. |
| GO:0033818 beta-ketoacyl-acyl-carrier-protein synthase III activity | EXP | ACCEPT | KAS III activity in the reconstitution that also showed FabH is the enzyme that excludes branched primers in E. coli. |
| GO:0033818 beta-ketoacyl-acyl-carrier-protein synthase III activity | EXP | ACCEPT | KAS III activity in the study that placed FabI as the rate-determining FAS-II step. |
| GO:0033818 beta-ketoacyl-acyl-carrier-protein synthase III activity | EXP | ACCEPT | KAS III activity measured on the purified enzyme, with kinetic constants for both substrates. |
| GO:0033818 beta-ketoacyl-acyl-carrier-protein synthase III activity | EXP | ACCEPT | KAS III activity in the comparative study of the FabA and FabZ dehydratases. |
| GO:0033818 beta-ketoacyl-acyl-carrier-protein synthase III activity | IBA | ACCEPT | Phylogenetic assignment of KAS III activity across the FabH clade. |
| GO:0033818 beta-ketoacyl-acyl-carrier-protein synthase III activity | IDA | ACCEPT | KAS III activity of the purified gene product, in the study that cloned fabH and showed the protein has both condensing and transacylase activity. |
| GO:0033818 beta-ketoacyl-acyl-carrier-protein synthase III activity | IEA | ACCEPT | Electronic assignment of the core KAS III activity from Rhea, EC and UniRule mappings. |

**Core function:** enables GO:0033818 beta-ketoacyl-acyl-carrier-protein synthase III activity; in GO:0006633, GO:0030497; located in GO:0005829

