# PN dossier: GLMN

- review_batch: proteostasis-batch-2026-06-13
- review_yaml: genes/human/GLMN/GLMN-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | CRL regulator | CRL inhibitor
- UniProt: Q92990
- In branches: UPS
- Signature domains: (none)
- Auxiliary domains: (none)
- PN references (titles):
    - 22748924
- PN-node mapping records (path + ancestors):
    - [type] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|CRL regulator|CRL inhibitor
        status=mapped scope=ok_for_propagation_to_go GO=[GO:1904667 negative regulation of ubiquitin protein ligase activity]
        rationale: This PN type captures cullin-RING ligase inhibitors. The matching GO process target is negative regulation of ubiquitin protein ligase activity.
    - [group] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|CRL regulator
        status=context_only scope=too_broad_to_propagate GO=[GO:1904666 regulation of ubiquitin protein ligase activity]
        rationale: This PN group records regulation of cullin-RING ligase systems, but the members include inhibitors, exchange factors, and modulators with different directionality. It is context only.
    - [class] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases
        status=context_only scope=too_broad_to_propagate GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This class is a genuine E3-ligase context, but its descendants include catalytic ligases, cullin scaffolds, substrate receptors, adaptors, cofactors, regulators, and UBL modifier systems. A class-level propagation would over-annotate.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (1)
- GO:1904667 negative regulation of ubiquitin protein ligase activity | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|CRL regulator|CRL inhibitor
