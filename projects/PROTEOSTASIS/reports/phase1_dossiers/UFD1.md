# PN dossier: UFD1

- review_batch: proteostasis-batch-2026-06-07c
- review_yaml: genes/human/UFD1/UFD1-ai-review.yaml
- PN workbook rows: 4

## PN row 1: ER proteostasis | Organelle-specific protein degradation | ER associated degradation | VCP system for retrotranslocation in ERAD | VCP accessories
- UniProt: Q92890
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

## PN row 2: Translation | Cytosolic translation | Ribosome-associated QC | VCP system for RQC
- UniProt: Q92890
- In branches: ER, TR, UPS
- PN-node mapping records (path + ancestors):
    - [type] Translation|Cytosolic translation|Ribosome-associated QC|VCP system for RQC
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

## PN row 3: Ubiquitin Proteasome System | VCP and associated proteins | adaptors | SHP | UT3
- UniProt: Q92890
- In branches: ER, TR, UPS
- Signature domains: PMID: 28451587 (SHP)
- Auxiliary domains: IPR042299
- PN references (titles):
    - 28451587
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|VCP and associated proteins|adaptors|SHP|UT3
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0034098 VCP-NPL4-UFD1 AAA ATPase complex]
        rationale: This PN subtype identifies UFD1 in the canonical VCP-NPL4-UFD1 adaptor complex. The matching GO cellular-component term is VCP-NPL4-UFD1 AAA ATPase complex.
    - [type] Ubiquitin Proteasome System|VCP and associated proteins|adaptors|SHP
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a VCP-adaptor motif or architecture subdivision. The label is useful taxonomy but too indirect for direct GO propagation without gene-level evidence.
    - [group] Ubiquitin Proteasome System|VCP and associated proteins|adaptors
        status=context_only scope=too_broad_to_propagate GO=[GO:0034098 VCP-NPL4-UFD1 AAA ATPase complex]
        rationale: This PN group records VCP adaptor context, but it mixes UBX, SHP, VIM, VBM, membrane, and other adaptor classes. Direct propagation should come only from narrower complex-specific nodes or gene-level review.
    - [class] Ubiquitin Proteasome System|VCP and associated proteins
        status=context_only scope=too_broad_to_propagate GO=[GO:0043335 protein unfolding]
        rationale: This class records the VCP segregase branch context, but descendants include VCP, substrate adaptors, DUBs, E3 ligases, channels, and unrelated associated enzymes. Direct propagation is restricted to narrower nodes.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## PN row 4: Ubiquitin Proteasome System | Ubiquitin and UBL binding | protein quality control | ERAD cofactor | idiosyncratic Ub binding / UT3
- UniProt: Q92890
- In branches: ER, TR, UPS
- Signature domains: PMID: 36736315 (IPR055417)
- Auxiliary domains: (none)
- PN references (titles):
    - 36736315
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|Ubiquitin and UBL binding|protein quality control|ERAD cofactor|idiosyncratic Ub binding / UT3
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a family, domain, architecture, or residual subdivision. The label is useful for PN taxonomy navigation but is not itself a GO annotation target; any functional assertion should come from a curated parent role or gene-level evidence.
    - [type] Ubiquitin Proteasome System|Ubiquitin and UBL binding|protein quality control|ERAD cofactor
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0097466 ubiquitin-dependent glycoprotein ERAD pathway]
        rationale: This PN type groups ubiquitin/UBL-binding factors that act as ERAD cofactors in protein-quality-control contexts. The best available GO target in the local cache is ubiquitin-dependent glycoprotein ERAD pathway, used here at propagation scope.
    - [group] Ubiquitin Proteasome System|Ubiquitin and UBL binding|protein quality control
        status=context_only scope=too_broad_to_propagate GO=[GO:0043161 proteasome-mediated ubiquitin-dependent protein catabolic process]
        rationale: This PN group is a protein-quality-control context bucket, but its descendants include ERAD cofactors, HSP70 cochaperone context, stalled-chain recognition, and other mixed roles. Direct propagation should come from narrower nodes such as ERAD cofactor.
    - [class] Ubiquitin Proteasome System|Ubiquitin and UBL binding
        status=context_only scope=too_broad_to_propagate GO=[GO:0140036 ubiquitin-modified protein reader activity]
        rationale: This class records ubiquitin/UBL-reader context, but the subtree mixes ubiquitin, SUMO, UBL-domain, domain-architecture, catalytic, signaling, trafficking, and nucleic-acid process buckets. It is useful context, not a safe direct propagation.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (5)
- GO:0036503 ERAD pathway | scope=exact | goa_status=already_in_goa_exact | from=ER proteostasis|Organelle-specific protein degradation|ER associated degradation
- GO:0036503 ERAD pathway | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=ER proteostasis|Organelle-specific protein degradation|ER associated degradation|VCP system for retrotranslocation in ERAD
- GO:0006515 protein quality control for misfolded or incompletely synthesized proteins | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Translation|Cytosolic translation|Ribosome-associated QC
- GO:0034098 VCP-NPL4-UFD1 AAA ATPase complex | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Ubiquitin Proteasome System|VCP and associated proteins|adaptors|SHP|UT3
- GO:0097466 ubiquitin-dependent glycoprotein ERAD pathway | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Ubiquitin Proteasome System|Ubiquitin and UBL binding|protein quality control|ERAD cofactor
