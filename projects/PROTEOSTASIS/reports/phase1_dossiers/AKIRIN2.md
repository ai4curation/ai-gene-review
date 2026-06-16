# PN dossier: AKIRIN2

- review_batch: proteostasis-batch-2026-06-03
- review_yaml: genes/human/AKIRIN2/AKIRIN2-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Ubiquitin Proteasome System | Proteasome and associated proteins | adaptors | Akirin
- UniProt: Q53H80
- In branches: UPS
- Signature domains: IPR024132
- Auxiliary domains: (none)
- PN references (titles):
    - 34711951
- PN-node mapping records (path + ancestors):
    - [type] Ubiquitin Proteasome System|Proteasome and associated proteins|adaptors|Akirin
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower proteasome component, chaperone, adaptor, domain, or isoform subdivision already covered by a curated parent proteasome mapping. No additional direct GO mapping is needed at this node.
    - [group] Ubiquitin Proteasome System|Proteasome and associated proteins|adaptors
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0070628 proteasome binding]
        rationale: This PN group captures proteasome adaptors and shuttle factors. Proteasome binding is the safe shared molecular-function target.
    - [class] Ubiquitin Proteasome System|Proteasome and associated proteins
        status=context_only scope=too_broad_to_propagate GO=[GO:0000502 proteasome complex]
        rationale: This class records the proteasome branch context, but descendants include core and regulatory particle subunits, activators, assembly chaperones, adaptors, DUBs, E3 ligases, enzymes, and transcriptional regulators. Propagation should come from narrower nodes.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (1)
- GO:0070628 proteasome binding | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Ubiquitin Proteasome System|Proteasome and associated proteins|adaptors
