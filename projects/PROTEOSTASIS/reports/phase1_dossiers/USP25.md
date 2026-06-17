# PN dossier: USP25

- review_batch: proteostasis-batch-2026-06-07c
- review_yaml: genes/human/USP25/USP25-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Ubiquitin Proteasome System | DUBs and UBL demodifiers | USP | other | UBA, UIM
- UniProt: Q9UHP3
- In branches: UPS
- Signature domains: IPR028889
- Auxiliary domains: IPR009060, IPR003903
- PN references (titles):
    - 19734957 / rev
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|DUBs and UBL demodifiers|USP|other|UBA, UIM
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower active DUB family/domain subdivision already covered by the curated parent DUB-family mapping. No additional direct GO mapping is needed at this node.
    - [type] Ubiquitin Proteasome System|DUBs and UBL demodifiers|USP|other
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

## PN row 2: Ubiquitin Proteasome System | Ubiquitin and UBL binding | DUB | USP / with UBD | UIM, UBA-like, SIM
- UniProt: Q9UHP3
- In branches: UPS
- Signature domains: IPR003903, IPR054109, PMID: 18538659
- Auxiliary domains: IPR028889
- PN references (titles):
    - 18538659
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|Ubiquitin and UBL binding|DUB|USP / with UBD|UIM, UBA-like, SIM
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower UBL-binding DUB-domain subdivision. Because this subtree includes noncatalytic or pseudo-DUB cases, active DUB propagation is handled by the DUB-family branch rather than this binding-domain node.
    - [type] Ubiquitin Proteasome System|Ubiquitin and UBL binding|DUB|USP / with UBD
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

## Projected GO annotations (1)
- GO:0101005 deubiquitinase activity | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Ubiquitin Proteasome System|DUBs and UBL demodifiers|USP
