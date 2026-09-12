# PN dossier: CAND1

- review_batch: proteostasis-batch-2026-06-06
- review_yaml: genes/human/CAND1/CAND1-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | CRL regulator | F-box exchange factor | Armadillo-like
- UniProt: Q86VP6
- In branches: UPS
- Signature domains: (none)
- Auxiliary domains: IPR011989
- PN references (titles):
    - 23453757
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|CRL regulator|F-box exchange factor|Armadillo-like
        status=mapped scope=ok_for_propagation_to_go GO=[GO:1990757 ubiquitin ligase activator activity]
        rationale: This PN type captures CAND-family exchange factors that activate/remodel cullin-RING ligase assemblies. The closest shared GO activity is ubiquitin ligase activator activity.
    - [type] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|CRL regulator|F-box exchange factor
        status=mapped scope=ok_for_propagation_to_go GO=[GO:1990757 ubiquitin ligase activator activity]
        rationale: This PN type captures CAND-family exchange factors that activate/remodel cullin-RING ligase assemblies. The closest shared GO activity is ubiquitin ligase activator activity.
    - [group] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|CRL regulator
        status=context_only scope=too_broad_to_propagate GO=[GO:1904666 regulation of ubiquitin protein ligase activity]
        rationale: This PN group records regulation of cullin-RING ligase systems, but the members include inhibitors, exchange factors, and modulators with different directionality. It is context only.
    - [class] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases
        status=context_only scope=too_broad_to_propagate GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This class is a genuine E3-ligase context, but its descendants include catalytic ligases, cullin scaffolds, substrate receptors, adaptors, cofactors, regulators, and UBL modifier systems. A class-level propagation would over-annotate.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (2)
- GO:1990757 ubiquitin ligase activator activity | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|CRL regulator|F-box exchange factor
- GO:1990757 ubiquitin ligase activator activity | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|CRL regulator|F-box exchange factor|Armadillo-like
