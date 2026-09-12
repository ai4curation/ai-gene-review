# PN dossier: EDEM2

- review_batch: proteostasis-batch-2026-06-11
- review_yaml: genes/human/EDEM2/EDEM2-ai-review.yaml
- PN workbook rows: 1

## PN row 1: ER proteostasis | Glycoproteostasis | N-glycosylation system | N-glycan processing | Mannose trimming
- UniProt: Q9BV94
- In branches: ER
- PN-node mapping records (path + ancestors):
    - [subtype] ER proteostasis|Glycoproteostasis|N-glycosylation system|N-glycan processing|Mannose trimming
        status=mapped scope=ok_for_propagation_to_go GO=[GO:1904382 mannose trimming involved in glycoprotein ERAD pathway]
        rationale: Within the ER proteostasis branch, this PN subtype denotes mannose trimming used in glycoprotein quality control and ERAD triage. That is close enough for propagation to the GO mannose-trimming-in-ERAD process, but the PN subtype is framed as a proteostasis step rather than a formal GO process class.
    - [type] ER proteostasis|Glycoproteostasis|N-glycosylation system|N-glycan processing
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [group] ER proteostasis|Glycoproteostasis|N-glycosylation system
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0006487 protein N-linked glycosylation]
        rationale: This PN group captures the ER N-glycosylation machinery that installs and processes N-linked glycans during proteostasis. GO protein N-linked glycosylation is the best current propagation target in the local cache.
    - [class] ER proteostasis|Glycoproteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [branch] ER proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## Projected GO annotations (2)
- GO:0006487 protein N-linked glycosylation | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=ER proteostasis|Glycoproteostasis|N-glycosylation system
- GO:1904382 mannose trimming involved in glycoprotein ERAD pathway | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=ER proteostasis|Glycoproteostasis|N-glycosylation system|N-glycan processing|Mannose trimming
