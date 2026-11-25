# ADCY6 curation notes

`just deep-research-falcon human ADCY6 --fallback perplexity-lite` failed in this workspace because the Falcon and Perplexity providers were both unavailable to the `deep-research-client`, so this review is based on the GOA/UniProt seed, cached publications, cached Reactome records, donor-annotation checks in QuickGO, the vasopressin receptor module, and the local GO-CAM review for `gomodel:67e5e74400004286`.

## Core function

ADCY6 is a plasma-membrane type VI adenylyl cyclase. Human ACVI produces cAMP in membranes and in reconstituted GPCR systems: the Gbeta/gamma study directly assayed membranes expressing human hACVI [PMID:17110384, "membranes of Sf9 cells expressing hACV or hACVI showed"], and the baculoviral co-display study reconstituted dopamine D1 receptor, Gs, Gbeta1/gamma2 and ACVI and observed dopamine-stimulated cAMP production [PMID:18403039, "co-expressing DR-D1, Galpha(s), Gbeta(1)gamma(2), and ACVI"]. The natural S674 variant increased ADCY6 activity and beta-adrenergic vascular sensitivity in humans [PMID:17916776, "S674 increased adenylyl cyclase activity"].

The AVPR2 GO-CAM uses ADCY6 for the renal V2 vasopressin branch. Mouse data support that isoform choice: AC6-null kidney had reduced forskolin- and V2-agonist-stimulated adenylyl cyclase activity and a water-homeostasis defect [PMID:20466003, "Activities of AC evoked by forskolin or a selective agonist of"], and an independent knockout study found that AC6 was the dominant inner-medullary cyclase and required for full dDAVP-stimulated cAMP production, AQP2 phosphorylation, apical AQP2 trafficking and urinary concentration [PMID:20864687, "mice lacking AC6 had lower levels of inner medullary cAMP"].

## Non-core contexts

ADCY6 is a shared effector for many receptor systems. Direct human experiments support beta-adrenergic and dopamine D1 receptor contexts, and there is transfer or Reactome support for Gi/o-coupled inhibitory branches. The exact duplicate `GO:0007193` ISS rows in GOA differ only by date and collapse to one review block because the review schema does not carry GAF dates. The serotonin-specific inhibitory ISS rows are left undecided because the donor rows were not exposed locally and the reviewed UniProt text only supports generic GNAI1 inhibition. The generic cyclic-nucleotide biosynthesis, phosphorus-oxygen lyase activity, system process, and intracellular signal-transduction rows are treated as `TOO_GENERAL`, not `MODIFY`, because their own signature or ARBA evidence supports ADCY6's adenylyl-cyclase identity but not the full more-specific physiological branch.

Several rows over-interpret generic GPCR/adenylyl-cyclase placement as pathway-specific biology. The glucagon and laminar-shear Reactome records route a signal through "adenylate cyclase" generically without distinguishing ADCY6 from other membrane isoforms. The PTH/PTHrP bone-resorption paper predates the current ADCY6-specific row and supports a downstream PKA requirement in mouse bone cells, not a cyclase-isoform assignment [PMID:8225186, "PTHrP stimulates bone resorption presumably through"]. Forskolin is a pharmacologic AC activator in the S674 assay, so it supports catalysis rather than a physiological cellular response to forskolin.

The `GO:0007192` serotonin-activating row is left undecided. Its PMID supports isoproterenol-stimulated ACVI activation in the accessible abstract [PMID:17110384, "full activation of hACVI by isoproterenol"], but the full text is unavailable here and the abstract does not identify a serotonin receptor.

## GO-CAM consistency

ADCY6 matches the AVPR2 model as the downstream enzyme in the `GO:0004016` adenylate cyclase activity that produces cAMP in the Gs branch of the V2 receptor cascade. The only local inconsistency is structural rather than biological: activity `gomodel:67e5e74400004286/67e5e74400004291` omits an `occurs_in` assertion. The final GO-CAM consistency PR should add `GO:0005886` plasma membrane to that activity, matching the reviewed ADCY6 location and clearing the existing `MISSING_LOCATION` flag.
