# PN dossier: AGK

- review_batch: proteostasis-batch-2026-06-03
- review_yaml: genes/human/AGK/AGK-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Mitochondrial proteostasis | Protein transport | Inner membrane import | TIMM22 complex
- UniProt: Q53H12
- In branches: MI
- PN-node mapping records (path + ancestors):
    - [type] Mitochondrial proteostasis|Protein transport|Inner membrane import|TIMM22 complex
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0042721 TIM22 mitochondrial import inner membrane insertion complex]
        rationale: This PN type captures TIMM22-complex components responsible for a specific inner-membrane import route. The GO cellular-component term for the TIM22 insertion complex is an appropriate propagation target.
    - [group] Mitochondrial proteostasis|Protein transport|Inner membrane import
        status=context_only scope=too_broad_to_propagate GO=[GO:0044743 protein transmembrane import into intracellular organelle]
        rationale: In `4.3.11`, inner-membrane import is a group that covers TIM22, TIM17/23, PAM-associated matrix import, and related inner-membrane sorting routes. The source is useful context for mitochondrial protein import, but protein insertion into mitochondrial inner membrane is too specific for all descendants because reviewed TIM23/PAM components include matrix-import motor and gatekeeper roles. Propagation should come from narrower child nodes such as TIM22 complex, TIM23 complex, or OXA1L-mediated insertion.
    - [class] Mitochondrial proteostasis|Protein transport
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0015031 protein transport]
        rationale: The PN mitochondrial Protein transport class groups protein-targeting and import pathways into mitochondria. GO protein transport is the appropriate propagation target, while the source class remains mitochondria-specific and broader than any single GO transport subtype.
    - [branch] Mitochondrial proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## Projected GO annotations (2)
- GO:0015031 protein transport | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Mitochondrial proteostasis|Protein transport
- GO:0042721 TIM22 mitochondrial import inner membrane insertion complex | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Mitochondrial proteostasis|Protein transport|Inner membrane import|TIMM22 complex
