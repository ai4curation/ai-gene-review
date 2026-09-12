# PN dossier: BAG2

- review_batch: proteostasis-batch-2026-06-06
- review_yaml: genes/human/BAG2/BAG2-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Cytonuclear proteostasis | Chaperone | HSP70 system | HSP70 nucleotide exchange factor | BAG domain subtype
- UniProt: O95816
- In branches: CY, UPS
- PN-node mapping records (path + ancestors):
    - [subtype] Cytonuclear proteostasis|Chaperone|HSP70 system|HSP70 nucleotide exchange factor|BAG domain subtype
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower taxonomy bucket that is already covered by a curated parent mapping or by gene-level annotations. No additional direct GO mapping is appropriate from this node.
    - [type] Cytonuclear proteostasis|Chaperone|HSP70 system|HSP70 nucleotide exchange factor
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0000774 adenyl-nucleotide exchange factor activity]
        rationale: These PN entries denote nucleotide exchange factors that reset HSP70 chaperones by promoting ADP release. The current validated GO cache does not expose a more HSP70-specific exchange-factor term, so adenyl-nucleotide exchange factor activity is the best supported target.
    - [group] Cytonuclear proteostasis|Chaperone|HSP70 system
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a specific GO class. The member genes span multiple activities, complexes, or contexts, so propagation from this node would overstate the shared biology; use narrower child or gene-level curations.
    - [class] Cytonuclear proteostasis|Chaperone
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a specific GO class. The member genes span multiple activities, complexes, or contexts, so propagation from this node would overstate the shared biology; use narrower child or gene-level curations.
    - [branch] Cytonuclear proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## PN row 2: Ubiquitin Proteasome System | Proteasome and associated proteins | adaptors | BAG
- UniProt: O95816
- In branches: CY, UPS
- Signature domains: IPR037689
- Auxiliary domains: IPR003103, IPR037689
- PN-node mapping records (path + ancestors):
    - [type] Ubiquitin Proteasome System|Proteasome and associated proteins|adaptors|BAG
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

## Projected GO annotations (2)
- GO:0000774 adenyl-nucleotide exchange factor activity | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Cytonuclear proteostasis|Chaperone|HSP70 system|HSP70 nucleotide exchange factor
- GO:0070628 proteasome binding | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Ubiquitin Proteasome System|Proteasome and associated proteins|adaptors
