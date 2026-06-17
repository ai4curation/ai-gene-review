# PN dossier: NPLOC4

- review_batch: proteostasis-batch-2026-06-07c
- review_yaml: genes/human/NPLOC4/NPLOC4-ai-review.yaml
- PN workbook rows: 6

## PN row 1: ER proteostasis | Organelle-specific protein degradation | ER associated degradation | VCP system for retrotranslocation in ERAD | VCP accessories
- UniProt: Q8TAT6
- In branches: ER, TR, UPS
- PN-node mapping records (path + ancestors):
    - [subtype] ER proteostasis|Organelle-specific protein degradation|ER associated degradation|VCP system for retrotranslocation in ERAD|VCP accessories
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [type] ER proteostasis|Organelle-specific protein degradation|ER associated degradation|VCP system for retrotranslocation in ERAD
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0036503 ERAD pathway]
        rationale: This PN type captures the VCP/p97-dependent retrotranslocation machinery used in ERAD. It is not a separate process from ERAD, but a core mechanistic subsystem within it.
    - [group] ER proteostasis|Organelle-specific protein degradation|ER associated degradation
        status=mapped scope=exact GO=[GO:0036503 ERAD pathway]
        rationale: The PN group "ER associated degradation" is a direct lexical and biological match to the GO ERAD pathway term. The additional branch and class context disambiguates the source string from any broader degradation language.
    - [class] ER proteostasis|Organelle-specific protein degradation
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [branch] ER proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## PN row 2: Translation | Cytosolic translation | Ribosome-associated QC | Ubiquitin recognition
- UniProt: Q8TAT6
- In branches: ER, TR, UPS
- PN-node mapping records (path + ancestors):
    - [type] Translation|Cytosolic translation|Ribosome-associated QC|Ubiquitin recognition
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [group] Translation|Cytosolic translation|Ribosome-associated QC
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0006515 protein quality control for misfolded or incompletely synthesized proteins]
        rationale: The PN ribosome-associated quality-control group covers surveillance and disposal of stalled or defective nascent-chain translation products. GO lacks a dedicated ribosome-associated QC term in the local cache, so the broader protein-quality-control process is the best supported target.
    - [class] Translation|Cytosolic translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0002181 cytoplasmic translation]
        rationale: The PN class Cytosolic translation is centered on the cytoplasmic translation apparatus and process, but it also houses supporting machinery such as ribosome biogenesis factors. The GO process term is a useful high-level label for the class, but propagating it to all members would over-annotate genes whose PN placement is through assembly or maturation context rather than core cytoplasmic translation.
    - [branch] Translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0006412 translation]
        rationale: The PN Translation branch is organized around the translation apparatus and immediately associated cotranslational quality-control systems. GO translation is the closest high-level process label, but the PN branch also contains adjacent machinery such as ribosome biogenesis and nascent-chain handling. Keeping this relationship is useful for interpretation, but it is too broad to project safely onto every member.

## PN row 3: Ubiquitin Proteasome System | Ubiquitin and UBL proteins | UBL domain | DUB | MPN
- UniProt: Q8TAT6
- In branches: ER, TR, UPS
- Signature domains: IPR024682
- Auxiliary domains: IPR037518
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|Ubiquitin and UBL proteins|UBL domain|DUB|MPN
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower UBL-domain DUB subdivision. The domain architecture is not sufficient for propagation because the subtree includes noncatalytic MPN/UBL-domain cases; active DUB mappings are handled elsewhere.
    - [type] Ubiquitin Proteasome System|Ubiquitin and UBL proteins|UBL domain|DUB
        status=context_only scope=too_broad_to_propagate GO=[GO:0101005 deubiquitinase activity]
        rationale: This UBL-domain type is DUB-related context, but the subtree includes noncatalytic MPN/UBL-domain cases. Active DUB propagation is handled from the DUB-family branch.
    - [group] Ubiquitin Proteasome System|Ubiquitin and UBL proteins|UBL domain
        status=context_only scope=too_broad_to_propagate GO=[GO:0043130 ubiquitin binding]
        rationale: This group records UBL-domain protein context, but descendants include enzymes, adaptors, chaperone-related proteins, non-enzymatic proteins, and nucleic-acid factors. Propagation is restricted to narrower nodes.
    - [class] Ubiquitin Proteasome System|Ubiquitin and UBL proteins
        status=context_only scope=too_broad_to_propagate GO=[GO:0019787 ubiquitin-like protein transferase activity]
        rationale: This class groups ubiquitin, UBL modifiers, UBX/UBL-domain proteins, and UBL-containing enzymes. The branch is UPS-relevant but too mixed to propagate as a single GO annotation.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## PN row 4: Ubiquitin Proteasome System | DUBs and UBL demodifiers | JAMM / MPN | VCP-associated
- UniProt: Q8TAT6
- In branches: ER, TR, UPS
- Signature domains: IPR037518
- Auxiliary domains: IPR001876
- PN references (titles):
    - 12370088 / rev
- PN-node mapping records (path + ancestors):
    - [type] Ubiquitin Proteasome System|DUBs and UBL demodifiers|JAMM / MPN|VCP-associated
        status=no_mapping scope= GO=[]
        rationale: Reviewed manually as a UPS source node. No single GO term is appropriate for direct propagation from this PN label without narrower context or gene-level evidence.
    - [group] Ubiquitin Proteasome System|DUBs and UBL demodifiers|JAMM / MPN
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a UPS taxonomy container. Its descendants mix catalytic roles, complex membership, binding domains, regulators, adaptors, and substrate-context labels, so a single propagating GO assertion would overstate the shared biology.
    - [class] Ubiquitin Proteasome System|DUBs and UBL demodifiers
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a UPS taxonomy container. Its descendants mix catalytic roles, complex membership, binding domains, regulators, adaptors, and substrate-context labels, so a single propagating GO assertion would overstate the shared biology.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## PN row 5: Ubiquitin Proteasome System | VCP and associated proteins | associated DUBs | MPN | UBXL
- UniProt: Q8TAT6
- In branches: ER, TR, UPS
- Signature domains: PMID: 28451587 (UBXL)
- Auxiliary domains: IPR037518
- PN references (titles):
    - 28451587
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|VCP and associated proteins|associated DUBs|MPN|UBXL
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0034098 VCP-NPL4-UFD1 AAA ATPase complex]
        rationale: This PN subtype identifies NPLOC4 in the VCP-NPL4-UFD1 complex context. The safe GO target is VCP-NPL4-UFD1 AAA ATPase complex, not DUB activity.
    - [type] Ubiquitin Proteasome System|VCP and associated proteins|associated DUBs|MPN
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower VCP-associated DUB/adaptor subdivision. The VCP context includes both catalytic DUBs and noncatalytic complex members, so no additional direct DUB propagation is made from this node.
    - [group] Ubiquitin Proteasome System|VCP and associated proteins|associated DUBs
        status=context_only scope=too_broad_to_propagate GO=[GO:0101005 deubiquitinase activity]
        rationale: This VCP-associated group is DUB-related context, but it includes NPLOC4 complex membership as well as catalytic DUBs. Direct DUB propagation comes from the DUB-family branch or narrower reviewed nodes.
    - [class] Ubiquitin Proteasome System|VCP and associated proteins
        status=context_only scope=too_broad_to_propagate GO=[GO:0043335 protein unfolding]
        rationale: This class records the VCP segregase branch context, but descendants include VCP, substrate adaptors, DUBs, E3 ligases, channels, and unrelated associated enzymes. Direct propagation is restricted to narrower nodes.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## PN row 6: Ubiquitin Proteasome System | Ubiquitin and UBL binding | DUB | MPN & UBXL | RanBP2-type ZnF
- UniProt: Q8TAT6
- In branches: ER, TR, UPS
- Signature domains: IPR001876
- Auxiliary domains: IPR037518
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|Ubiquitin and UBL binding|DUB|MPN & UBXL|RanBP2-type ZnF
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower UBL-binding DUB-domain subdivision. Because this subtree includes noncatalytic or pseudo-DUB cases, active DUB propagation is handled by the DUB-family branch rather than this binding-domain node.
    - [type] Ubiquitin Proteasome System|Ubiquitin and UBL binding|DUB|MPN & UBXL
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower UBL-binding DUB-domain subdivision. Because this subtree includes noncatalytic or pseudo-DUB cases, active DUB propagation is handled by the DUB-family branch rather than this binding-domain node.
    - [group] Ubiquitin Proteasome System|Ubiquitin and UBL binding|DUB
        status=context_only scope=too_broad_to_propagate GO=[GO:0101005 deubiquitinase activity]
        rationale: This UBL-binding group is DUB-related context, but it includes noncatalytic or pseudo-DUB domain cases such as NPLOC4/USP39-like entries. Active DUB propagation is handled from the DUB-family branch.
    - [class] Ubiquitin Proteasome System|Ubiquitin and UBL binding
        status=context_only scope=too_broad_to_propagate GO=[GO:0140036 ubiquitin-modified protein reader activity]
        rationale: This class records ubiquitin/UBL-reader context, but the subtree mixes ubiquitin, SUMO, UBL-domain, domain-architecture, catalytic, signaling, trafficking, and nucleic-acid process buckets. It is useful context, not a safe direct propagation.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (4)
- GO:0036503 ERAD pathway | scope=exact | goa_status=already_in_goa_exact | from=ER proteostasis|Organelle-specific protein degradation|ER associated degradation
- GO:0036503 ERAD pathway | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=ER proteostasis|Organelle-specific protein degradation|ER associated degradation|VCP system for retrotranslocation in ERAD
- GO:0006515 protein quality control for misfolded or incompletely synthesized proteins | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Translation|Cytosolic translation|Ribosome-associated QC
- GO:0034098 VCP-NPL4-UFD1 AAA ATPase complex | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Ubiquitin Proteasome System|VCP and associated proteins|associated DUBs|MPN|UBXL
