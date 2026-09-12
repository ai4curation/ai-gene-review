# PN dossier: HSPA14

- review_batch: proteostasis-batch-2026-06-07b
- review_yaml: genes/human/HSPA14/HSPA14-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Cytonuclear proteostasis | Chaperone | HSP70 system | HSP70
- UniProt: Q0VDF9
- In branches: CY, TR
- PN-node mapping records (path + ancestors):
    - [type] Cytonuclear proteostasis|Chaperone|HSP70 system|HSP70
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0140662 ATP-dependent protein folding chaperone]
        rationale: In the PN hierarchy, the type label HSP70 within the chaperone/HSP70-system context denotes canonical HSP70 chaperones. Propagation to the GO molecular function ATP-dependent protein folding chaperone is appropriate for curation, but the PN family label is not itself a strict GO-equivalent class.
    - [group] Cytonuclear proteostasis|Chaperone|HSP70 system
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a specific GO class. The member genes span multiple activities, complexes, or contexts, so propagation from this node would overstate the shared biology; use narrower child or gene-level curations.
    - [class] Cytonuclear proteostasis|Chaperone
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a specific GO class. The member genes span multiple activities, complexes, or contexts, so propagation from this node would overstate the shared biology; use narrower child or gene-level curations.
    - [branch] Cytonuclear proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## PN row 2: Translation | Cytosolic translation | Nascent peptide husbandry | Nascent peptide chaperoning | RAC component
- UniProt: Q0VDF9
- In branches: CY, TR
- PN-node mapping records (path + ancestors):
    - [subtype] Translation|Cytosolic translation|Nascent peptide husbandry|Nascent peptide chaperoning|RAC component
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0051083 'de novo' cotranslational protein folding]
        rationale: The ribosome-associated complex is a cotranslational chaperone system for emerging nascent chains. The PN subtype is a specific component class within this mechanism, so propagation to GO 'de novo' cotranslational protein folding is justified but not exact.
    - [type] Translation|Cytosolic translation|Nascent peptide husbandry|Nascent peptide chaperoning
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0051083 'de novo' cotranslational protein folding]
        rationale: This PN type denotes cotranslational chaperoning of nascent peptides. The GO de novo cotranslational protein folding term is the shared process target.
    - [group] Translation|Cytosolic translation|Nascent peptide husbandry
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [class] Translation|Cytosolic translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0002181 cytoplasmic translation]
        rationale: The PN class Cytosolic translation is centered on the cytoplasmic translation apparatus and process, but it also houses supporting machinery such as ribosome biogenesis factors. The GO process term is a useful high-level label for the class, but propagating it to all members would over-annotate genes whose PN placement is through assembly or maturation context rather than core cytoplasmic translation.
    - [branch] Translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0006412 translation]
        rationale: The PN Translation branch is organized around the translation apparatus and immediately associated cotranslational quality-control systems. GO translation is the closest high-level process label, but the PN branch also contains adjacent machinery such as ribosome biogenesis and nascent-chain handling. Keeping this relationship is useful for interpretation, but it is too broad to project safely onto every member.

## Projected GO annotations (3)
- GO:0140662 ATP-dependent protein folding chaperone | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Cytonuclear proteostasis|Chaperone|HSP70 system|HSP70
- GO:0051083 'de novo' cotranslational protein folding | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Translation|Cytosolic translation|Nascent peptide husbandry|Nascent peptide chaperoning
- GO:0051083 'de novo' cotranslational protein folding | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Translation|Cytosolic translation|Nascent peptide husbandry|Nascent peptide chaperoning|RAC component
