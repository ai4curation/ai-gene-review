# PN dossier: CHAF1B

- review_batch: proteostasis-batch-2026-06-07
- review_yaml: genes/human/CHAF1B/CHAF1B-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Nuclear proteostasis | Chaperone | Histone chaperone
- UniProt: Q13112
- In branches: NU
- PN-node mapping records (path + ancestors):
    - [group] Nuclear proteostasis|Chaperone|Histone chaperone
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0140713 histone chaperone activity]
        rationale: This PN group collects nuclear histone-chaperone factors involved in histone handling, deposition, or exchange. The PN bucket is narrower than general nuclear proteostasis and aligns well with the GO molecular function histone chaperone activity.
    - [class] Nuclear proteostasis|Chaperone
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the nuclear chaperone class. The current member set includes histone chaperone and nuclear proteostasis context, but the class is not a single GO-equivalent activity; the histone-chaperone child mapping carries the defensible propagation.
    - [branch] Nuclear proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## Projected GO annotations (1)
- GO:0140713 histone chaperone activity | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Nuclear proteostasis|Chaperone|Histone chaperone
