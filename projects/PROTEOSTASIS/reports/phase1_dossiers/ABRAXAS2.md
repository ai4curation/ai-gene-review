# PN dossier: ABRAXAS2

- review_batch: proteostasis-batch-2026-06-03
- review_yaml: genes/human/ABRAXAS2/ABRAXAS2-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Ubiquitin Proteasome System | DUBs and UBL demodifiers | BRISC complex | noncatalytic | JAMM / MPN / ubiquitin binding
- UniProt: Q15018
- In branches: UPS
- Signature domains: (none)
- Auxiliary domains: IPR037518
- PN references (titles):
    - 36473924
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|DUBs and UBL demodifiers|BRISC complex|noncatalytic|JAMM / MPN / ubiquitin binding
        status=no_mapping scope= GO=[]
        rationale: Reviewed manually as a UPS source node. No single GO term is appropriate for direct propagation from this PN label without narrower context or gene-level evidence.
    - [type] Ubiquitin Proteasome System|DUBs and UBL demodifiers|BRISC complex|noncatalytic
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0070552 BRISC complex]
        rationale: This PN type covers noncatalytic BRISC subunits, so complex membership is the safe propagation target rather than catalytic DUB activity.
    - [group] Ubiquitin Proteasome System|DUBs and UBL demodifiers|BRISC complex
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0070552 BRISC complex]
        rationale: This PN group denotes BRISC complex members. The matching GO cellular-component term is BRISC complex.
    - [class] Ubiquitin Proteasome System|DUBs and UBL demodifiers
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a UPS taxonomy container. Its descendants mix catalytic roles, complex membership, binding domains, regulators, adaptors, and substrate-context labels, so a single propagating GO assertion would overstate the shared biology.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## PN row 2: Ubiquitin Proteasome System | Ubiquitin and UBL binding | DNA repair | BRISC complex component | idiosyncratic Ub binding / MPN
- UniProt: Q15018
- In branches: UPS
- Signature domains: PMID: 19261749 (IPR037518)
- Auxiliary domains: (none)
- PN references (titles):
    - 19261749
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|Ubiquitin and UBL binding|DNA repair|BRISC complex component|idiosyncratic Ub binding / MPN
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a family, domain, architecture, or residual subdivision. The label is useful for PN taxonomy navigation but is not itself a GO annotation target; any functional assertion should come from a curated parent role or gene-level evidence.
    - [type] Ubiquitin Proteasome System|Ubiquitin and UBL binding|DNA repair|BRISC complex component
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a UPS taxonomy container. Its descendants mix catalytic roles, complex membership, binding domains, regulators, adaptors, and substrate-context labels, so a single propagating GO assertion would overstate the shared biology.
    - [group] Ubiquitin Proteasome System|Ubiquitin and UBL binding|DNA repair
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0006281 DNA repair]
        rationale: This PN group captures ubiquitin/UBL-binding factors assigned to DNA repair contexts. The group is context-defined rather than GO-equivalent, but propagation to DNA repair is appropriate.
    - [class] Ubiquitin Proteasome System|Ubiquitin and UBL binding
        status=context_only scope=too_broad_to_propagate GO=[GO:0140036 ubiquitin-modified protein reader activity]
        rationale: This class records ubiquitin/UBL-reader context, but the subtree mixes ubiquitin, SUMO, UBL-domain, domain-architecture, catalytic, signaling, trafficking, and nucleic-acid process buckets. It is useful context, not a safe direct propagation.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (3)
- GO:0070552 BRISC complex | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Ubiquitin Proteasome System|DUBs and UBL demodifiers|BRISC complex
- GO:0070552 BRISC complex | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Ubiquitin Proteasome System|DUBs and UBL demodifiers|BRISC complex|noncatalytic
- GO:0006281 DNA repair | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Ubiquitin Proteasome System|Ubiquitin and UBL binding|DNA repair
