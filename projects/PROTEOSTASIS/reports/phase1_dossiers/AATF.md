# PN dossier: AATF

- review_batch: proteostasis-batch-2026-06-03
- review_yaml: genes/human/AATF/AATF-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Translation | Cytosolic translation | Ribosome biogenesis factor | pre-60S complex | ANN complex
- UniProt: Q9NY61
- In branches: TR
- PN-node mapping records (path + ancestors):
    - [subtype] Translation|Cytosolic translation|Ribosome biogenesis factor|pre-60S complex|ANN complex
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower taxonomy bucket already covered by a curated parent mapping or by gene-level annotations. No additional direct GO mapping is appropriate from this node.
    - [type] Translation|Cytosolic translation|Ribosome biogenesis factor|pre-60S complex
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0030687 preribosome, large subunit precursor]
        rationale: This PN type denotes pre-60S particles. The GO preribosome large-subunit precursor term is the direct complex target.
    - [group] Translation|Cytosolic translation|Ribosome biogenesis factor
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0042254 ribosome biogenesis]
        rationale: This PN group collects factors assigned through cytosolic ribosome biogenesis, including SSU-processosome and pre-60S maturation machinery. The full PN path resolves the earlier over-annotation problem: these genes are not being placed by core translational elongation or decoding, but by assembly and maturation of ribosomal subunits. GO ribosome biogenesis is therefore the appropriate propagation target.
    - [class] Translation|Cytosolic translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0002181 cytoplasmic translation]
        rationale: The PN class Cytosolic translation is centered on the cytoplasmic translation apparatus and process, but it also houses supporting machinery such as ribosome biogenesis factors. The GO process term is a useful high-level label for the class, but propagating it to all members would over-annotate genes whose PN placement is through assembly or maturation context rather than core cytoplasmic translation.
    - [branch] Translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0006412 translation]
        rationale: The PN Translation branch is organized around the translation apparatus and immediately associated cotranslational quality-control systems. GO translation is the closest high-level process label, but the PN branch also contains adjacent machinery such as ribosome biogenesis and nascent-chain handling. Keeping this relationship is useful for interpretation, but it is too broad to project safely onto every member.

## Projected GO annotations (2)
- GO:0042254 ribosome biogenesis | scope=ok_for_propagation_to_go | goa_status=entailed_by_goa_closure | from=Translation|Cytosolic translation|Ribosome biogenesis factor
- GO:0030687 preribosome, large subunit precursor | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Translation|Cytosolic translation|Ribosome biogenesis factor|pre-60S complex
