# AIP notes

## 2026-06-02

PITA context: AIP corresponds to PITA1 / AIP-related pituitary adenoma predisposition. UniProt frames PITA1 as multiple pituitary adenoma types rather than GH-only, listing "growth hormone (GH)-secreting, prolactin (PRL)-secreting, adrenocorticotropin (ACTH)-secreting, thyroid- stimulating hormone (TSH)-secreting, and plurihormonal" tumors [file:human/AIP/AIP-uniprot.txt "Functional pituitary adenomas are further classified by the type of hormone they secrete"].

Local review status: `AIP-ai-review.yaml` was already marked COMPLETE before this batch review. I treated it as an existing review and did not rewrite it. The review's core functional picture is AIP as an HSP90/AHR co-chaperone/scaffold and cytosolic chaperone-like factor for mitochondrial preprotein import, supported by direct AIP/Tom20/preprotein evidence [PMID:14557246 "AIP functions as a cytosolic factor that mediates preprotein import into mitochondria"] and AIP/HSP90/AHR-complex evidence in the existing YAML.

Follow-up on GO:0051082: the `projects/UNFOLDED_PROTEIN_BINDING.md` project explicitly classifies AIP as `MODIFY -> GO:0051879 Hsp90 protein binding`, not as a `GO:0044183 protein folding chaperone` replacement. I aligned the review to treat PMID:14557246 as support for mitochondrial preprotein import and a holdase-like assay result, but not as evidence that AIP's core MF should be broad protein-folding chaperone activity.
