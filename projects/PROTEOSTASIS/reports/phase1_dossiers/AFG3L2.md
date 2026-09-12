# PN dossier: AFG3L2

- review_batch: proteostasis-batch-2026-06-03
- review_yaml: genes/human/AFG3L2/AFG3L2-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Mitochondrial proteostasis | Organelle-specific protein degradation | Matrix protease
- UniProt: Q9Y4W6
- In branches: MI
- PN-node mapping records (path + ancestors):
    - [group] Mitochondrial proteostasis|Organelle-specific protein degradation|Matrix protease
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0005759 mitochondrial matrix]
        rationale: This PN group identifies matrix-local protease systems. The source is a compartmental proteostasis bucket, so the mitochondrial matrix cellular-component term is the conservative propagation target.
    - [class] Mitochondrial proteostasis|Organelle-specific protein degradation
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0035694 mitochondrial protein catabolic process]
        rationale: This PN class groups mitochondrial protein-degradation pathways. GO mitochondrial protein catabolic process is the conservative shared target.
    - [branch] Mitochondrial proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## Projected GO annotations (2)
- GO:0035694 mitochondrial protein catabolic process | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Mitochondrial proteostasis|Organelle-specific protein degradation
- GO:0005759 mitochondrial matrix | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Mitochondrial proteostasis|Organelle-specific protein degradation|Matrix protease
