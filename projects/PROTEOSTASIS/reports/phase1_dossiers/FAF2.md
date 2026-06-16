# PN dossier: FAF2

- review_batch: proteostasis-batch-2026-06-11
- review_yaml: genes/human/FAF2/FAF2-ai-review.yaml
- PN workbook rows: 5

## PN row 1: ER proteostasis | Organelle-specific protein degradation | ER associated degradation | Retrotranslocation channel complex
- UniProt: Q96CS3
- In branches: ER, MI, UPS
- PN-node mapping records (path + ancestors):
    - [type] ER proteostasis|Organelle-specific protein degradation|ER associated degradation|Retrotranslocation channel complex
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower taxonomy bucket already covered by a curated parent mapping or by gene-level annotations. No additional direct GO mapping is appropriate from this node.
    - [group] ER proteostasis|Organelle-specific protein degradation|ER associated degradation
        status=mapped scope=exact GO=[GO:0036503 ERAD pathway]
        rationale: The PN group "ER associated degradation" is a direct lexical and biological match to the GO ERAD pathway term. The additional branch and class context disambiguates the source string from any broader degradation language.
    - [class] ER proteostasis|Organelle-specific protein degradation
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [branch] ER proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## PN row 2: Mitochondrial proteostasis | Organelle-specific protein degradation | mitoTAD pathway
- UniProt: Q96CS3
- In branches: ER, MI, UPS
- PN-node mapping records (path + ancestors):
    - [group] Mitochondrial proteostasis|Organelle-specific protein degradation|mitoTAD pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower taxonomy bucket that is already covered by a curated parent mapping or by gene-level annotations. No additional direct GO mapping is appropriate from this node.
    - [class] Mitochondrial proteostasis|Organelle-specific protein degradation
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0035694 mitochondrial protein catabolic process]
        rationale: This PN class groups mitochondrial protein-degradation pathways. GO mitochondrial protein catabolic process is the conservative shared target.
    - [branch] Mitochondrial proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## PN row 3: Ubiquitin Proteasome System | Ubiquitin and UBL proteins | UBX domain | VCP adaptors | thioredoxin-like, UBA
- UniProt: Q96CS3
- In branches: ER, MI, UPS
- Signature domains: IPR001012
- Auxiliary domains: IPR054109, IPR036249
- PN references (titles):
    - 18438607 / rev
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|Ubiquitin and UBL proteins|UBX domain|VCP adaptors|thioredoxin-like, UBA
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a UBX-domain/VCP-adaptor architecture subdivision. The domain label does not by itself establish a direct GO annotation beyond gene-level VCP-adaptor evidence.
    - [type] Ubiquitin Proteasome System|Ubiquitin and UBL proteins|UBX domain|VCP adaptors
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a UPS taxonomy container. Its descendants mix catalytic roles, complex membership, binding domains, regulators, adaptors, and substrate-context labels, so a single propagating GO assertion would overstate the shared biology.
    - [group] Ubiquitin Proteasome System|Ubiquitin and UBL proteins|UBX domain
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a UBX-domain protein bucket. UBX domain architecture is useful PN taxonomy but not itself a GO propagation target.
    - [class] Ubiquitin Proteasome System|Ubiquitin and UBL proteins
        status=context_only scope=too_broad_to_propagate GO=[GO:0019787 ubiquitin-like protein transferase activity]
        rationale: This class groups ubiquitin, UBL modifiers, UBX/UBL-domain proteins, and UBL-containing enzymes. The branch is UPS-relevant but too mixed to propagate as a single GO annotation.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## PN row 4: Ubiquitin Proteasome System | VCP and associated proteins | adaptors | UBX | thioredoxin-like, UBA
- UniProt: Q96CS3
- In branches: ER, MI, UPS
- Signature domains: IPR001012
- Auxiliary domains: IPR036249, IPR009060
- PN references (titles):
    - 18775313
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|VCP and associated proteins|adaptors|UBX|thioredoxin-like, UBA
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a VCP-adaptor motif or architecture subdivision. The label is useful taxonomy but too indirect for direct GO propagation without gene-level evidence.
    - [type] Ubiquitin Proteasome System|VCP and associated proteins|adaptors|UBX
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

## PN row 5: Ubiquitin Proteasome System | Ubiquitin and UBL binding | VCP-associated adaptor | with UBX & TRX-like | UBA-like
- UniProt: Q96CS3
- In branches: ER, MI, UPS
- Signature domains: IPR054109
- Auxiliary domains: IPR001012, IPR036249
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|Ubiquitin and UBL binding|VCP-associated adaptor|with UBX & TRX-like|UBA-like
        status=no_mapping scope= GO=[]
        rationale: Reviewed manually as a UPS source node. No single GO term is appropriate for direct propagation from this PN label without narrower context or gene-level evidence.
    - [type] Ubiquitin Proteasome System|Ubiquitin and UBL binding|VCP-associated adaptor|with UBX & TRX-like
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a UPS taxonomy container. Its descendants mix catalytic roles, complex membership, binding domains, regulators, adaptors, and substrate-context labels, so a single propagating GO assertion would overstate the shared biology.
    - [group] Ubiquitin Proteasome System|Ubiquitin and UBL binding|VCP-associated adaptor
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a UPS taxonomy container. Its descendants mix catalytic roles, complex membership, binding domains, regulators, adaptors, and substrate-context labels, so a single propagating GO assertion would overstate the shared biology.
    - [class] Ubiquitin Proteasome System|Ubiquitin and UBL binding
        status=context_only scope=too_broad_to_propagate GO=[GO:0140036 ubiquitin-modified protein reader activity]
        rationale: This class records ubiquitin/UBL-reader context, but the subtree mixes ubiquitin, SUMO, UBL-domain, domain-architecture, catalytic, signaling, trafficking, and nucleic-acid process buckets. It is useful context, not a safe direct propagation.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (2)
- GO:0036503 ERAD pathway | scope=exact | goa_status=already_in_goa_exact | from=ER proteostasis|Organelle-specific protein degradation|ER associated degradation
- GO:0035694 mitochondrial protein catabolic process | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Mitochondrial proteostasis|Organelle-specific protein degradation
