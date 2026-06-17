# PN dossier: DNAJB11

- review_batch: proteostasis-batch-2026-06-07b
- review_yaml: genes/human/DNAJB11/DNAJB11-ai-review.yaml
- PN workbook rows: 2

## PN row 1: ER proteostasis | Chaperone | HSP70 system | J-domain containing HSP70 cochaperone
- UniProt: Q9UBS4
- In branches: ER, EX
- PN-node mapping records (path + ancestors):
    - [type] ER proteostasis|Chaperone|HSP70 system|J-domain containing HSP70 cochaperone
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0030544 Hsp70 protein binding]
        rationale: In the PN hierarchy, this type denotes J-domain cochaperones assigned to the HSP70 system. Their shared mechanistic role is direct interaction with HSP70-family chaperones, making Hsp70 protein binding the most defensible GO target in the current cache.
    - [group] ER proteostasis|Chaperone|HSP70 system
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [class] ER proteostasis|Chaperone
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [branch] ER proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## PN row 2: Extracellular proteostasis | Chaperone | Primarily intracellular, secreted during ER stress
- UniProt: Q9UBS4
- In branches: ER, EX
- PN-node mapping records (path + ancestors):
    - [group] Extracellular proteostasis|Chaperone|Primarily intracellular, secreted during ER stress
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a contextual PN bucket. The label is useful for curator triage, but no direct GO mapping is appropriate because propagation would add a process, activity, or localization not shared cleanly by all members.
    - [class] Extracellular proteostasis|Chaperone
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a specific GO class. The member genes span multiple activities, complexes, or contexts, so propagation from this node would overstate the shared biology; use narrower child or gene-level curations.
    - [branch] Extracellular proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## Projected GO annotations (1)
- GO:0030544 Hsp70 protein binding | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=ER proteostasis|Chaperone|HSP70 system|J-domain containing HSP70 cochaperone
