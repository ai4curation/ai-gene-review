# PN dossier: ATAD1

- review_batch: proteostasis-batch-2026-06-03
- review_yaml: genes/human/ATAD1/ATAD1-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Mitochondrial proteostasis | Organelle-specific protein degradation | mitoCPR pathway
- UniProt: Q8NBU5
- In branches: MI
- PN-node mapping records (path + ancestors):
    - [group] Mitochondrial proteostasis|Organelle-specific protein degradation|mitoCPR pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower taxonomy bucket that is already covered by a curated parent mapping or by gene-level annotations. No additional direct GO mapping is appropriate from this node.
    - [class] Mitochondrial proteostasis|Organelle-specific protein degradation
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0035694 mitochondrial protein catabolic process]
        rationale: This PN class groups mitochondrial protein-degradation pathways. GO mitochondrial protein catabolic process is the conservative shared target.
    - [branch] Mitochondrial proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## Projected GO annotations (1)
- GO:0035694 mitochondrial protein catabolic process | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Mitochondrial proteostasis|Organelle-specific protein degradation
