# PN dossier: HSPA13

- review_batch: proteostasis-batch-2026-06-07b
- review_yaml: genes/human/HSPA13/HSPA13-ai-review.yaml
- PN workbook rows: 1

## PN row 1: ER proteostasis | Chaperone | HSP70 system | HSP70
- UniProt: P48723
- In branches: ER
- PN-node mapping records (path + ancestors):
    - [type] ER proteostasis|Chaperone|HSP70 system|HSP70
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0140662 ATP-dependent protein folding chaperone]
        rationale: In the PN hierarchy, the type label HSP70 within the chaperone/HSP70-system context denotes canonical HSP70 chaperones. Propagation to the GO molecular function ATP-dependent protein folding chaperone is appropriate for curation, but the PN family label is not itself a strict GO-equivalent class.
    - [group] ER proteostasis|Chaperone|HSP70 system
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [class] ER proteostasis|Chaperone
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [branch] ER proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## Projected GO annotations (1)
- GO:0140662 ATP-dependent protein folding chaperone | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=ER proteostasis|Chaperone|HSP70 system|HSP70
