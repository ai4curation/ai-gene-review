# AVP curation notes

`just deep-research-falcon human AVP --fallback perplexity-lite` failed in this workspace because the Falcon and Perplexity providers were both unavailable to the `deep-research-client`, so this review is based on the GOA/UniProt seed, cached publications, cached Reactome records, the vasopressin receptor module, and the local GO-CAM review for `gomodel:67e5e74400004286`.

## Core function

AVP encodes the preprohormone that yields mature Arg-vasopressin, neurophysin 2 and copeptin. UniProt summarizes mature AVP as an antidiuretic hormone that binds V1A, V1B and V2 vasopressin receptors [file:human/AVP/AVP-uniprot.txt, "Acts by binding to vasopressin receptors"], and the human disease paper establishes that the AVP-neurophysin precursor is the source of the human vasopressin neuropeptide: affected NDI patients had very low or undetectable circulating vasopressin [PMID:1740104, "Affected individuals have very low or undetectable levels of circulating vasopressin"].

The AVPR2 GO-CAM is aligned with the reviewed ligand boundary. It uses the Arg-vasopressin chain as an extracellular `GO:0005179` hormone activity that directly activates AVPR2 and is part of renal water absorption, without assigning the ligand to the GPCR signaling process. The module uses the more specific `GO:0005184` neuropeptide hormone activity [modules/vasopressin_receptor_signaling.yaml, "AVP is given its molecular function only: neuropeptide hormone activity"].

## Over-annotations

The `GO:0004672` protein kinase activity row is a clear mis-annotation: PMID:18402937 shows AVP acting upstream of MAPK/ERK, CaMK and PKC, not catalyzing phosphorylation itself [PMID:18402937, "The signaling pathways mediating the anti-apoptotic effect of VP involve mitogen activated protein (MAP) kinase"].

The Reactome clathrin-coated-vesicle rows place AVP in AVPR2 internalization cargo. These steps are about ADBRK phosphorylation, beta-arrestin and clathrin-mediated endocytosis of the AVPR2 complex; they do not establish the extracellular peptide ligand as a membrane resident of the coated vesicle [Reactome:R-HSA-8866268, "AVPR2 is phosphorylated by ADBRK1 and 2 in an agonist-dependent manner"].

The SARS-CoV-2 row is also over-annotated. The paper reports an extracellular complex among FLAG-tagged vasopressin, soluble ACE2 and spike in transfected cells [PMID:33713620, "successful co-immunoprecipitation of S by pulling down of vasopressin in the absence of ACE2"], which is direct experimental evidence for the paper's cell-entry assay but not an evolved function of vasopressin.

## GO-CAM consistency

No blocking disagreement with `gomodel:67e5e74400004286` remains after this review. The final GO-CAM consistency PR may optionally narrow the AVP molecular function on activity `gomodel:67e5e74400004286/67e5e74400004322` from `GO:0005179` hormone activity to `GO:0005184` neuropeptide hormone activity, matching the reviewed AVP row and the vasopressin receptor signaling module, but the existing GO-CAM term is a correct parent.
