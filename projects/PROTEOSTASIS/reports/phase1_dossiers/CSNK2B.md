# PN dossier: CSNK2B

- review_batch: proteostasis-batch-2026-06-07
- review_yaml: genes/human/CSNK2B/CSNK2B-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Translation | Cytosolic translation | Ribosome biogenesis factor | SSU processosome | UTP-C complex
- UniProt: P67870
- In branches: TR, ALP
- PN-node mapping records (path + ancestors):
    - [subtype] Translation|Cytosolic translation|Ribosome biogenesis factor|SSU processosome|UTP-C complex
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower taxonomy bucket already covered by a curated parent mapping or by gene-level annotations. No additional direct GO mapping is appropriate from this node.
    - [type] Translation|Cytosolic translation|Ribosome biogenesis factor|SSU processosome
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0032040 small-subunit processome]
        rationale: This PN type denotes SSU processosome factors. The GO small-subunit processome term is the direct complex target.
    - [group] Translation|Cytosolic translation|Ribosome biogenesis factor
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0042254 ribosome biogenesis]
        rationale: This PN group collects factors assigned through cytosolic ribosome biogenesis, including SSU-processosome and pre-60S maturation machinery. The full PN path resolves the earlier over-annotation problem: these genes are not being placed by core translational elongation or decoding, but by assembly and maturation of ribosomal subunits. GO ribosome biogenesis is therefore the appropriate propagation target.
    - [class] Translation|Cytosolic translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0002181 cytoplasmic translation]
        rationale: The PN class Cytosolic translation is centered on the cytoplasmic translation apparatus and process, but it also houses supporting machinery such as ribosome biogenesis factors. The GO process term is a useful high-level label for the class, but propagating it to all members would over-annotate genes whose PN placement is through assembly or maturation context rather than core cytoplasmic translation.
    - [branch] Translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0006412 translation]
        rationale: The PN Translation branch is organized around the translation apparatus and immediately associated cotranslational quality-control systems. GO translation is the closest high-level process label, but the PN branch also contains adjacent machinery such as ribosome biogenesis and nascent-chain handling. Keeping this relationship is useful for interpretation, but it is too broad to project safely onto every member.

## PN row 2: Autophagy-Lysosome Pathway | Autophagophore initiation and elongation | ATG8 homolog processing, upstream | Preparation of ATG8 homologs for lipidation | Modulation of ATG5-ATG12-ATG16 complex assembly
- UniProt: P67870
- In branches: TR, ALP
- Notes: Member of Casein kinase II complex. Phosphorylates ATG16L1 to increase it's affinity for ATG5-ATG12.
- PN references (titles):
    - Full article: ATG16L1 phosphorylation is oppositely regulated by CSNK2/casein kinase 2 and PPP1/protein phosphatase 1 which determines the fate of cardiomyocytes during hypoxia/reoxygenation (tandfonline.com)
    - Regulation of Autophagy Enzymes by Nutrient Signaling - ScienceDirect
- PN-node mapping records (path + ancestors):
    - [subtype] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|ATG8 homolog processing, upstream|Preparation of ATG8 homologs for lipidation|Modulation of ATG5-ATG12-ATG16 complex assembly
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a contextual PN role. The label is useful for curator triage, but by itself does not support a universal GO assertion for all member genes beyond curated ancestor or child mappings.
    - [type] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|ATG8 homolog processing, upstream|Preparation of ATG8 homologs for lipidation
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a contextual PN role. The label is useful for curator triage, but by itself does not support a universal GO assertion for all member genes beyond curated ancestor or child mappings.
    - [group] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|ATG8 homolog processing, upstream
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation
        status=context_only scope=too_broad_to_propagate GO=[GO:0016236 macroautophagy]
        rationale: This class is a real macroautophagy context, but its descendants include core factors, component buckets, upstream modulators, localization roles, and residual categories. Projecting generic macroautophagy from this ancestor creates TRAPP-like overpropagation, so candidate GO annotations must come from narrower curated nodes.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## Projected GO annotations (2)
- GO:0042254 ribosome biogenesis | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Translation|Cytosolic translation|Ribosome biogenesis factor
- GO:0032040 small-subunit processome | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Translation|Cytosolic translation|Ribosome biogenesis factor|SSU processosome
