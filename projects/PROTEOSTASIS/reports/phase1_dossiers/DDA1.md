# PN dossier: DDA1

- review_batch: proteostasis-batch-2026-06-13
- review_yaml: genes/human/DDA1/DDA1-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | Cul4A/Cul4B receptor scaffold
- UniProt: Q9BW61
- In branches: UPS
- Signature domains: (none)
- Auxiliary domains: (none)
- PN references (titles):
    - 17452440
- PN-node mapping records (path + ancestors):
    - [group] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul4A/Cul4B receptor scaffold
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0160072 ubiquitin ligase complex scaffold activity]
        rationale: This PN group captures cullin or cullin-associated scaffold roles in ubiquitin ligase complexes. The shared GO molecular-function target is ubiquitin ligase complex scaffold activity.
    - [class] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases
        status=context_only scope=too_broad_to_propagate GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This class is a genuine E3-ligase context, but its descendants include catalytic ligases, cullin scaffolds, substrate receptors, adaptors, cofactors, regulators, and UBL modifier systems. A class-level propagation would over-annotate.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (1)
- GO:0160072 ubiquitin ligase complex scaffold activity | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul4A/Cul4B receptor scaffold
