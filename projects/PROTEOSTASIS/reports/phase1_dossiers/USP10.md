# PN dossier: USP10

- review_batch: proteostasis-pr-1217
- review_yaml: genes/human/USP10/USP10-ai-review.yaml
- PN workbook rows: 3

## PN row 1: Translation | Cytosolic translation | Ribosome-associated QC | Deubiquitination
- UniProt: Q14694
- In branches: TR, ALP, UPS
- PN-node mapping records (path + ancestors):
    - [type] Translation|Cytosolic translation|Ribosome-associated QC|Deubiquitination
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0101005 deubiquitinase activity]
        rationale: This PN RQC type denotes deubiquitinases acting in ribosome-associated quality control. Deubiquitinase activity is the shared molecular-function target.
    - [group] Translation|Cytosolic translation|Ribosome-associated QC
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0006515 protein quality control for misfolded or incompletely synthesized proteins]
        rationale: The PN ribosome-associated quality-control group covers surveillance and disposal of stalled or defective nascent-chain translation products. GO lacks a dedicated ribosome-associated QC term in the local cache, so the broader protein-quality-control process is the best supported target.
    - [class] Translation|Cytosolic translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0002181 cytoplasmic translation]
        rationale: The PN class Cytosolic translation is centered on the cytoplasmic translation apparatus and process, but it also houses supporting machinery such as ribosome biogenesis factors. The GO process term is a useful high-level label for the class, but propagating it to all members would over-annotate genes whose PN placement is through assembly or maturation context rather than core cytoplasmic translation.
    - [branch] Translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0006412 translation]
        rationale: The PN Translation branch is organized around the translation apparatus and immediately associated cotranslational quality-control systems. GO translation is the closest high-level process label, but the PN branch also contains adjacent machinery such as ribosome biogenesis and nascent-chain handling. Keeping this relationship is useful for interpretation, but it is too broad to project safely onto every member.

## PN row 2: Autophagy-Lysosome Pathway | Autophagophore initiation and elongation | ATG8 homolog processing, direct | Deubiquitination of ATG8 homologs
- UniProt: Q14694
- In branches: TR, ALP, UPS
- Notes: Deubiquitinase that removes ubiquitin from LC3, thereby increasing autophagy.
- PN references (titles):
    - The ubiquitin isopeptidase USP10 deubiquitinates LC3B to increase LC3B levels and autophagic activity - ScienceDirect
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|ATG8 homolog processing, direct|Deubiquitination of ATG8 homologs
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0016579 protein deubiquitination]
        rationale: This PN type denotes deubiquitination of ATG8-family proteins within the autophagy pathway. GO does not currently provide an ATG8-specific deubiquitination term, so the defensible target is the broader parent process protein deubiquitination.
    - [group] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|ATG8 homolog processing, direct
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation
        status=context_only scope=too_broad_to_propagate GO=[GO:0016236 macroautophagy]
        rationale: This class is a real macroautophagy context, but its descendants include core factors, component buckets, upstream modulators, localization roles, and residual categories. Projecting generic macroautophagy from this ancestor creates TRAPP-like overpropagation, so candidate GO annotations must come from narrower curated nodes.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 3: Ubiquitin Proteasome System | DUBs and UBL demodifiers | USP | Ataxin-2, C term | other
- UniProt: Q14694
- In branches: TR, ALP, UPS
- Signature domains: IPR028889
- Auxiliary domains: IPR009818
- PN references (titles):
    - 19734957 / rev
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|DUBs and UBL demodifiers|USP|Ataxin-2, C term|other
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower active DUB family/domain subdivision already covered by the curated parent DUB-family mapping. No additional direct GO mapping is needed at this node.
    - [type] Ubiquitin Proteasome System|DUBs and UBL demodifiers|USP|Ataxin-2, C term
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower active DUB family/domain subdivision already covered by the curated parent DUB-family mapping. No additional direct GO mapping is needed at this node.
    - [group] Ubiquitin Proteasome System|DUBs and UBL demodifiers|USP
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0101005 deubiquitinase activity]
        rationale: This PN group is an active deubiquitinase family bucket. The shared molecular-function assertion is deubiquitinase activity.
    - [class] Ubiquitin Proteasome System|DUBs and UBL demodifiers
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a UPS taxonomy container. Its descendants mix catalytic roles, complex membership, binding domains, regulators, adaptors, and substrate-context labels, so a single propagating GO assertion would overstate the shared biology.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (4)
- GO:0006515 protein quality control for misfolded or incompletely synthesized proteins | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Translation|Cytosolic translation|Ribosome-associated QC
- GO:0101005 deubiquitinase activity | scope=ok_for_propagation_to_go | goa_status=entailed_by_goa_closure | from=Translation|Cytosolic translation|Ribosome-associated QC|Deubiquitination
- GO:0016579 protein deubiquitination | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|ATG8 homolog processing, direct|Deubiquitination of ATG8 homologs
- GO:0101005 deubiquitinase activity | scope=ok_for_propagation_to_go | goa_status=entailed_by_goa_closure | from=Ubiquitin Proteasome System|DUBs and UBL demodifiers|USP
