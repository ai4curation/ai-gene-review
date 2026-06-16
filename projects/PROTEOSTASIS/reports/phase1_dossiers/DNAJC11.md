# PN dossier: DNAJC11

- review_batch: proteostasis-batch-2026-06-07b
- review_yaml: genes/human/DNAJC11/DNAJC11-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Mitochondrial proteostasis | Chaperone | HSP70 system | J-domain containing HSP70 cochaperone
- UniProt: Q9NVH1
- In branches: MI
- PN-node mapping records (path + ancestors):
    - [type] Mitochondrial proteostasis|Chaperone|HSP70 system|J-domain containing HSP70 cochaperone
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0030544 Hsp70 protein binding]
        rationale: In the PN hierarchy, this type denotes J-domain cochaperones assigned to the HSP70 system. Their shared mechanistic role is direct interaction with HSP70-family chaperones, making Hsp70 protein binding the most defensible GO target in the current cache.
    - [group] Mitochondrial proteostasis|Chaperone|HSP70 system
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a specific GO class. The member genes span multiple activities, complexes, or contexts, so propagation from this node would overstate the shared biology; use narrower child or gene-level curations.
    - [class] Mitochondrial proteostasis|Chaperone
        status=no_mapping scope= GO=[]
        rationale: This PN class is too heterogeneous for a single safe GO mapping. In the workbook it mixes HSP70, HSP60, and HSP90 systems, small intermembrane-space chaperones, membrane-protein chaperones, and other mitochondrial-specific factors.
    - [branch] Mitochondrial proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## Projected GO annotations (1)
- GO:0030544 Hsp70 protein binding | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Mitochondrial proteostasis|Chaperone|HSP70 system|J-domain containing HSP70 cochaperone
