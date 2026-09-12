# PN dossier: UCHL1

- review_batch: proteostasis-pr-1217
- review_yaml: genes/human/UCHL1/UCHL1-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Autophagy-Lysosome Pathway | Autophagophore initiation and elongation | ATG8 homolog processing, direct | Deubiquitination of ATG8 homologs
- UniProt: P09936
- In branches: ALP, UPS
- Notes: Deubiquitinase that interacts with LC3 proteins to inhibit autophagosome formation
- PN references (titles):
    - Ubiquitin C-Terminal Hydrolase L1 regulates autophagy by inhibiting autophagosome formation through its deubiquitinating enzyme activity - ScienceDirect
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

## PN row 2: Ubiquitin Proteasome System | DUBs and UBL demodifiers | UCH
- UniProt: P09936
- In branches: ALP, UPS
- Signature domains: IPR001578
- Auxiliary domains: (none)
- PN-node mapping records (path + ancestors):
    - [group] Ubiquitin Proteasome System|DUBs and UBL demodifiers|UCH
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0101005 deubiquitinase activity]
        rationale: This PN group is an active deubiquitinase family bucket. The shared molecular-function assertion is deubiquitinase activity.
    - [class] Ubiquitin Proteasome System|DUBs and UBL demodifiers
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a UPS taxonomy container. Its descendants mix catalytic roles, complex membership, binding domains, regulators, adaptors, and substrate-context labels, so a single propagating GO assertion would overstate the shared biology.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (2)
- GO:0016579 protein deubiquitination | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|ATG8 homolog processing, direct|Deubiquitination of ATG8 homologs
- GO:0101005 deubiquitinase activity | scope=ok_for_propagation_to_go | goa_status=entailed_by_goa_closure | from=Ubiquitin Proteasome System|DUBs and UBL demodifiers|UCH
