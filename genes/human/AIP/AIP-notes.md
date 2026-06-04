# AIP notes

## 2026-06-02

PITA context: AIP corresponds to PITA1 / AIP-related pituitary adenoma predisposition. UniProt frames PITA1 as multiple pituitary adenoma types rather than GH-only, listing "growth hormone (GH)-secreting, prolactin (PRL)-secreting, adrenocorticotropin (ACTH)-secreting, thyroid- stimulating hormone (TSH)-secreting, and plurihormonal" tumors [file:human/AIP/AIP-uniprot.txt "Functional pituitary adenomas are further classified by the type of hormone they secrete"].

Local review status: `AIP-ai-review.yaml` was already marked COMPLETE before this batch review. I treated it as an existing review and did not rewrite it. The review's core functional picture is AIP as an HSP90/AHR co-chaperone/scaffold and cytosolic chaperone-like factor for mitochondrial preprotein import, supported by direct AIP/Tom20/preprotein evidence [PMID:14557246 "AIP functions as a cytosolic factor that mediates preprotein import into mitochondria"] and AIP/HSP90/AHR-complex evidence in the existing YAML.

Follow-up on GO:0051082: the `projects/UNFOLDED_PROTEIN_BINDING.md` project explicitly classifies AIP as `MODIFY -> GO:0051879 Hsp90 protein binding`, not as a `GO:0044183 protein folding chaperone` replacement. I aligned the review to treat PMID:14557246 as support for mitochondrial preprotein import and a holdase-like assay result, but not as evidence that AIP's core MF should be broad protein-folding chaperone activity.

## 2026-06-03

Proteostasis PN re-review: Falcon deep research is already present (`AIP-deep-research-falcon.md`), so I did not rerun deep research. The PN projection has two AIP-relevant outputs: `GO:0031072 heat shock protein binding` as a candidate addition from the HSP70-HSP90 joint co-chaperone branch, and `GO:0003755 peptidyl-prolyl cis-trans isomerase activity` as already in GOA from the FKBP-type PPIase branch [file:projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv "AIP GO:0031072 heat shock protein binding more_specific_than_existing_goa"; file:projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv "AIP GO:0003755 peptidyl-prolyl cis-trans isomerase activity already_in_goa_exact"].

Conservative PN decision: do not accept or retain the PPIase projection for AIP. AIP has an FKBP-like/PPIase-like domain, but direct biochemical evidence states that the PPIase-like region is enzymatically inactive [PMID:19375531 "The PPIase-like region turned out to be enzymatically inactive"]. I updated both `GO:0003755` annotation reviews to record that the PN FKBP/PPIase classification is over-broad for AIP at gene level.

For the co-chaperone projection, the biology supports heat-shock-protein binding in a broad sense because AIP binds HSP90 through its TPR motif [PMID:19375531 "The effect of XAP2 on GR requires its interaction with Hsp90 through the TPR motif"] and binds Hsc70 in the mitochondrial preprotein import context [PMID:14557246 "Hsc70 was also found to bind to AIP"]. However, the existing review already uses the more specific `GO:0051879 Hsp90 protein binding` as the preferred replacement for obsolete `GO:0051082`, so I did not add a broad `GO:0031072` assertion. I added a curator question asking whether PN should propagate the broad heat-shock-protein binding term for AIP or prefer the more specific HSP90-binding recommendation.
