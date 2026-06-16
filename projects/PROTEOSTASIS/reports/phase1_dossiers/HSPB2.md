# PN dossier: HSPB2

- review_batch: proteostasis-batch-2026-06-07b
- review_yaml: genes/human/HSPB2/HSPB2-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Cytonuclear proteostasis | Chaperone | small HSP system | small HSP
- UniProt: Q16082
- In branches: CY, MI
- PN-node mapping records (path + ancestors):
    - [type] Cytonuclear proteostasis|Chaperone|small HSP system|small HSP
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0044183 protein folding chaperone]
        rationale: This PN type denotes small heat-shock chaperones. Protein folding chaperone is the appropriate shared molecular-function term.
    - [group] Cytonuclear proteostasis|Chaperone|small HSP system
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower taxonomy bucket that is already covered by a curated parent mapping or by gene-level annotations. No additional direct GO mapping is appropriate from this node.
    - [class] Cytonuclear proteostasis|Chaperone
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a specific GO class. The member genes span multiple activities, complexes, or contexts, so propagation from this node would overstate the shared biology; use narrower child or gene-level curations.
    - [branch] Cytonuclear proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## PN row 2: Mitochondrial proteostasis | Chaperone | small HSP
- UniProt: Q16082
- In branches: CY, MI
- PN-node mapping records (path + ancestors):
    - [group] Mitochondrial proteostasis|Chaperone|small HSP
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0044183 protein folding chaperone]
        rationale: This PN group denotes mitochondrial small heat-shock chaperones. Protein folding chaperone is the appropriate shared molecular-function term.
    - [class] Mitochondrial proteostasis|Chaperone
        status=no_mapping scope= GO=[]
        rationale: This PN class is too heterogeneous for a single safe GO mapping. In the workbook it mixes HSP70, HSP60, and HSP90 systems, small intermembrane-space chaperones, membrane-protein chaperones, and other mitochondrial-specific factors.
    - [branch] Mitochondrial proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## Projected GO annotations (2)
- GO:0044183 protein folding chaperone | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Cytonuclear proteostasis|Chaperone|small HSP system|small HSP
- GO:0044183 protein folding chaperone | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Mitochondrial proteostasis|Chaperone|small HSP
