# PN dossier: ATP23

- review_batch: proteostasis-batch-2026-06-03
- review_yaml: genes/human/ATP23/ATP23-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Mitochondrial proteostasis | Organelle-specific protein degradation | Intermembrane space protease
- UniProt: Q9Y6H3
- In branches: MI
- PN-node mapping records (path + ancestors):
    - [group] Mitochondrial proteostasis|Organelle-specific protein degradation|Intermembrane space protease
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0005758 mitochondrial intermembrane space]
        rationale: This PN group captures proteases assigned specifically to the mitochondrial intermembrane space. The source bucket is compartmental and mechanistic rather than a single shared enzymatic GO class, so the mitochondrial intermembrane space cellular-component term is the conservative propagation target.
    - [class] Mitochondrial proteostasis|Organelle-specific protein degradation
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0035694 mitochondrial protein catabolic process]
        rationale: This PN class groups mitochondrial protein-degradation pathways. GO mitochondrial protein catabolic process is the conservative shared target.
    - [branch] Mitochondrial proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## Projected GO annotations (2)
- GO:0035694 mitochondrial protein catabolic process | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Mitochondrial proteostasis|Organelle-specific protein degradation
- GO:0005758 mitochondrial intermembrane space | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Mitochondrial proteostasis|Organelle-specific protein degradation|Intermembrane space protease
