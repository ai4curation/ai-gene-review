# PN dossier: CACUL1

- review_batch: proteostasis-batch-2026-06-07
- review_yaml: genes/human/CACUL1/CACUL1-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | Cullin | degenerate, possible CUL3 inhibitor
- UniProt: Q86Y37
- In branches: UPS
- Signature domains: IPR001373
- Auxiliary domains: (none)
- PN references (titles):
    - 26238671
- PN-node mapping records (path + ancestors):
    - [type] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cullin|degenerate, possible CUL3 inhibitor
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a contextual, regulatory, adaptor, or uncertain UPS bucket. The shared label does not by itself establish a safe gene-level GO propagation.
    - [group] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cullin
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0160072 ubiquitin ligase complex scaffold activity]
        rationale: This PN group captures cullin or cullin-associated scaffold roles in ubiquitin ligase complexes. The shared GO molecular-function target is ubiquitin ligase complex scaffold activity.
    - [class] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases
        status=context_only scope=too_broad_to_propagate GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This class is a genuine E3-ligase context, but its descendants include catalytic ligases, cullin scaffolds, substrate receptors, adaptors, cofactors, regulators, and UBL modifier systems. A class-level propagation would over-annotate.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (1)
- GO:0160072 ubiquitin ligase complex scaffold activity | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cullin
