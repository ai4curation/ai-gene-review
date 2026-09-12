# PN dossier: ADRM1

- review_batch: proteostasis-batch-2026-06-03
- review_yaml: genes/human/ADRM1/ADRM1-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Ubiquitin Proteasome System | Proteasome and associated proteins | proteasome regulatory particle subunit | base, nonATPase | PRU, DEUBAD
- UniProt: Q16186
- In branches: UPS
- Signature domains: (none)
- Auxiliary domains: IPR044868, IPR044867
- PN references (titles):
    - 19145068 / rev
    - 19489727 / rev
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|Proteasome and associated proteins|proteasome regulatory particle subunit|base, nonATPase|PRU, DEUBAD
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower proteasome component, chaperone, adaptor, domain, or isoform subdivision already covered by a curated parent proteasome mapping. No additional direct GO mapping is needed at this node.
    - [type] Ubiquitin Proteasome System|Proteasome and associated proteins|proteasome regulatory particle subunit|base, nonATPase
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0008540 proteasome regulatory particle, base subcomplex]
        rationale: This PN type captures base subunits of the proteasome regulatory particle. The matching GO cellular-component term is proteasome regulatory particle, base subcomplex.
    - [group] Ubiquitin Proteasome System|Proteasome and associated proteins|proteasome regulatory particle subunit
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0005838 proteasome regulatory particle]
        rationale: This PN group captures proteasome regulatory particle subunits. The matching GO cellular-component term is proteasome regulatory particle.
    - [class] Ubiquitin Proteasome System|Proteasome and associated proteins
        status=context_only scope=too_broad_to_propagate GO=[GO:0000502 proteasome complex]
        rationale: This class records the proteasome branch context, but descendants include core and regulatory particle subunits, activators, assembly chaperones, adaptors, DUBs, E3 ligases, enzymes, and transcriptional regulators. Propagation should come from narrower nodes.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## PN row 2: Ubiquitin Proteasome System | Ubiquitin and UBL binding | proteasomal subunits | regulatory particle | idiosyncratic Ub binding / PRU
- UniProt: Q16186
- In branches: UPS
- Signature domains: PMID: 18497827, PMID: 32160516 (IPR044868)
- Auxiliary domains: IPR044867
- PN references (titles):
    - 18497827
    - 32160516
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|Ubiquitin and UBL binding|proteasomal subunits|regulatory particle|idiosyncratic Ub binding / PRU
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0005838 proteasome regulatory particle]
        rationale: This PN type/subtype is a ubiquitin-binding regulatory-particle subunit bucket. The safe GO target is proteasome regulatory particle.
    - [type] Ubiquitin Proteasome System|Ubiquitin and UBL binding|proteasomal subunits|regulatory particle
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0005838 proteasome regulatory particle]
        rationale: This PN type/subtype is a ubiquitin-binding regulatory-particle subunit bucket. The safe GO target is proteasome regulatory particle.
    - [group] Ubiquitin Proteasome System|Ubiquitin and UBL binding|proteasomal subunits
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0000502 proteasome complex]
        rationale: This PN group captures ubiquitin/UBL-binding proteasomal subunits. The shared GO target is proteasome complex.
    - [class] Ubiquitin Proteasome System|Ubiquitin and UBL binding
        status=context_only scope=too_broad_to_propagate GO=[GO:0140036 ubiquitin-modified protein reader activity]
        rationale: This class records ubiquitin/UBL-reader context, but the subtree mixes ubiquitin, SUMO, UBL-domain, domain-architecture, catalytic, signaling, trafficking, and nucleic-acid process buckets. It is useful context, not a safe direct propagation.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (5)
- GO:0005838 proteasome regulatory particle | scope=ok_for_propagation_to_go | goa_status=entailed_by_goa_closure | from=Ubiquitin Proteasome System|Proteasome and associated proteins|proteasome regulatory particle subunit
- GO:0008540 proteasome regulatory particle, base subcomplex | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Ubiquitin Proteasome System|Proteasome and associated proteins|proteasome regulatory particle subunit|base, nonATPase
- GO:0000502 proteasome complex | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Ubiquitin Proteasome System|Ubiquitin and UBL binding|proteasomal subunits
- GO:0005838 proteasome regulatory particle | scope=ok_for_propagation_to_go | goa_status=entailed_by_goa_closure | from=Ubiquitin Proteasome System|Ubiquitin and UBL binding|proteasomal subunits|regulatory particle
- GO:0005838 proteasome regulatory particle | scope=ok_for_propagation_to_go | goa_status=entailed_by_goa_closure | from=Ubiquitin Proteasome System|Ubiquitin and UBL binding|proteasomal subunits|regulatory particle|idiosyncratic Ub binding / PRU
