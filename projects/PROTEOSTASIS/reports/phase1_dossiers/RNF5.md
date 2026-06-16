# PN dossier: RNF5

- review_batch: proteostasis-batch-2026-06-11
- review_yaml: genes/human/RNF5/RNF5-ai-review.yaml
- PN workbook rows: 3

## PN row 1: ER proteostasis | Organelle-specific protein degradation | ER associated degradation | Cytosolic handling of ERAD substrates | ERAD-associated RING E3 ligase
- UniProt: Q99942
- In branches: ER, ALP, UPS
- PN-node mapping records (path + ancestors):
    - [subtype] ER proteostasis|Organelle-specific protein degradation|ER associated degradation|Cytosolic handling of ERAD substrates|ERAD-associated RING E3 ligase
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This PN subtype denotes ERAD-associated RING E3 ligases. Ubiquitin protein ligase activity is the appropriate shared catalytic target.
    - [type] ER proteostasis|Organelle-specific protein degradation|ER associated degradation|Cytosolic handling of ERAD substrates
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0036503 ERAD pathway]
        rationale: This PN type covers the cytosolic processing steps that receive ERAD substrates after retrotranslocation. These activities remain part of the ERAD pathway, but the source category is a specific mechanistic slice.
    - [group] ER proteostasis|Organelle-specific protein degradation|ER associated degradation
        status=mapped scope=exact GO=[GO:0036503 ERAD pathway]
        rationale: The PN group "ER associated degradation" is a direct lexical and biological match to the GO ERAD pathway term. The additional branch and class context disambiguates the source string from any broader degradation language.
    - [class] ER proteostasis|Organelle-specific protein degradation
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [branch] ER proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## PN row 2: Autophagy-Lysosome Pathway | Autophagophore initiation and elongation | ATG8 homolog processing, upstream | Preparation of ATG8 homologs for lipidation | Modulation of ATG4 activity
- UniProt: Q99942
- In branches: ER, ALP, UPS
- Notes: Annotated by homology with mouse. Regulates basal levels of autophagy by controlling the stability of ATG4B
- PN references (titles):
    - Regulation of ATG4B Stability by RNF5 Limits Basal Levels of Autophagy and Influences Susceptibility to Bacterial Infection (plos.org)
- PN-node mapping records (path + ancestors):
    - [subtype] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|ATG8 homolog processing, upstream|Preparation of ATG8 homologs for lipidation|Modulation of ATG4 activity
        status=mapped scope=ok_for_propagation_to_go GO=[GO:2000785 regulation of autophagosome assembly]
        rationale: This PN leaf denotes factors that alter ATG4 function upstream of ATG8 processing. The cleanest GO-level consequence captured in the current ontology is regulation of autophagosome assembly.
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

## PN row 3: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | RING | with transmembrane domain | ER, mitochondria, cell membrane
- UniProt: Q99942
- In branches: ER, ALP, UPS
- Signature domains: IPR001841
- Auxiliary domains: (none)
- PN references (titles):
    - 19489725 / rev
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING|with transmembrane domain|ER, mitochondria, cell membrane
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower E3-ligase architecture, component, or domain subdivision already covered by the curated parent E3 mapping. No additional direct GO mapping is needed at this node.
    - [type] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING|with transmembrane domain
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower E3-ligase architecture, component, or domain subdivision already covered by the curated parent E3 mapping. No additional direct GO mapping is needed at this node.
    - [group] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This PN group is a catalytic ubiquitin E3 ligase bucket. The shared GO molecular-function target is ubiquitin protein ligase activity.
    - [class] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases
        status=context_only scope=too_broad_to_propagate GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This class is a genuine E3-ligase context, but its descendants include catalytic ligases, cullin scaffolds, substrate receptors, adaptors, cofactors, regulators, and UBL modifier systems. A class-level propagation would over-annotate.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (5)
- GO:0036503 ERAD pathway | scope=exact | goa_status=already_in_goa_exact | from=ER proteostasis|Organelle-specific protein degradation|ER associated degradation
- GO:0036503 ERAD pathway | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=ER proteostasis|Organelle-specific protein degradation|ER associated degradation|Cytosolic handling of ERAD substrates
- GO:0061630 ubiquitin protein ligase activity | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=ER proteostasis|Organelle-specific protein degradation|ER associated degradation|Cytosolic handling of ERAD substrates|ERAD-associated RING E3 ligase
- GO:2000785 regulation of autophagosome assembly | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|ATG8 homolog processing, upstream|Preparation of ATG8 homologs for lipidation|Modulation of ATG4 activity
- GO:0061630 ubiquitin protein ligase activity | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING
