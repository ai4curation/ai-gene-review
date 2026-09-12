# PN dossier: GTPBP6

- review_batch: proteostasis-batch-2026-06-07c
- review_yaml: genes/human/GTPBP6/GTPBP6-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Translation | Mitochondrial translation | Mitoribosome biogenesis factor | 39S subunit assembly
- UniProt: O43824
- In branches: TR
- PN-node mapping records (path + ancestors):
    - [type] Translation|Mitochondrial translation|Mitoribosome biogenesis factor|39S subunit assembly
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0061668 mitochondrial ribosome assembly]
        rationale: This PN type denotes 39S mitoribosomal subunit assembly factors. Mitochondrial ribosome assembly is the shared process target.
    - [group] Translation|Mitochondrial translation|Mitoribosome biogenesis factor
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0061668 mitochondrial ribosome assembly]
        rationale: This PN group denotes factors for mitoribosome assembly and maturation. Mitochondrial ribosome assembly is the most specific shared process target.
    - [class] Translation|Mitochondrial translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0032543 mitochondrial translation]
        rationale: This PN class is a useful mitochondrial-translation context, but it contains ribosome components, assembly factors, tRNA synthetases, regulatory factors, and translation factors. Direct propagation to mitochondrial translation would over-annotate several adjacent machinery classes, so the relationship is retained as context only.
    - [branch] Translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0006412 translation]
        rationale: The PN Translation branch is organized around the translation apparatus and immediately associated cotranslational quality-control systems. GO translation is the closest high-level process label, but the PN branch also contains adjacent machinery such as ribosome biogenesis and nascent-chain handling. Keeping this relationship is useful for interpretation, but it is too broad to project safely onto every member.

## PN row 2: Translation | Mitochondrial translation | Translation termination | Termination on stalled ribosomes
- UniProt: O43824
- In branches: TR
- PN-node mapping records (path + ancestors):
    - [type] Translation|Mitochondrial translation|Translation termination|Termination on stalled ribosomes
        status=mapped scope=ok_for_propagation_to_go GO=[GO:7770016 rescue of stalled mitochondrial ribosome]
        rationale: This PN type denotes handling of stalled mitochondrial ribosomes. The GO rescue of stalled mitochondrial ribosome process is the best matching target.
    - [group] Translation|Mitochondrial translation|Translation termination
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0070126 mitochondrial translational termination]
        rationale: This PN group denotes mitochondrial translation termination machinery. The matching GO process term is appropriate for propagation.
    - [class] Translation|Mitochondrial translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0032543 mitochondrial translation]
        rationale: This PN class is a useful mitochondrial-translation context, but it contains ribosome components, assembly factors, tRNA synthetases, regulatory factors, and translation factors. Direct propagation to mitochondrial translation would over-annotate several adjacent machinery classes, so the relationship is retained as context only.
    - [branch] Translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0006412 translation]
        rationale: The PN Translation branch is organized around the translation apparatus and immediately associated cotranslational quality-control systems. GO translation is the closest high-level process label, but the PN branch also contains adjacent machinery such as ribosome biogenesis and nascent-chain handling. Keeping this relationship is useful for interpretation, but it is too broad to project safely onto every member.

## Projected GO annotations (4)
- GO:0061668 mitochondrial ribosome assembly | scope=ok_for_propagation_to_go | goa_status=entailed_by_goa_closure | from=Translation|Mitochondrial translation|Mitoribosome biogenesis factor
- GO:0061668 mitochondrial ribosome assembly | scope=ok_for_propagation_to_go | goa_status=entailed_by_goa_closure | from=Translation|Mitochondrial translation|Mitoribosome biogenesis factor|39S subunit assembly
- GO:0070126 mitochondrial translational termination | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Translation|Mitochondrial translation|Translation termination
- GO:7770016 rescue of stalled mitochondrial ribosome | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Translation|Mitochondrial translation|Translation termination|Termination on stalled ribosomes
