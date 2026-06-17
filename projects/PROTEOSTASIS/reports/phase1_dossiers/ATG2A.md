# PN dossier: ATG2A

- review_batch: proteostasis-batch-2026-06-03
- review_yaml: genes/human/ATG2A/ATG2A-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Autophagy-Lysosome Pathway | Autophagophore initiation and elongation | Regulation of autophagophore membrane composition | ATG2-WIPI complex component
- UniProt: Q2TAZ0
- In branches: ALP
- Notes: Component of ATG2-WIPI complex, which recruits ATG9 to the autophagosome. ATG2A and ATG2B are lipid transporters, carry phospholipids to the phagophore
- PN references (titles):
    - Mammalian Autophagy: How Does It Work? | Annual Review of Biochemistry (annualreviews.org)
    - Insights into autophagosome biogenesis from structural and biochemical analyses of the ATG2A-WIPI4 complex | PNAS
    - Mammalian Atg2 proteins are essential for autophagosome formation and important for regulation of size and distribution of lipid droplets | Molecular Biology of the Cell (molbiolcell.org)
    - Lipid droplet and early autophagosomal membrane targeting of Atg2A and Atg14L in human tumor cells[S] - Journal of Lipid Research (jlr.org)
    - Autophagosome biogenesis comes out of the black box | Nature Cell Biology
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|Regulation of autophagophore membrane composition|ATG2-WIPI complex component
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0062079 ATG2-ATG18 complex]
        rationale: This PN component bucket corresponds to the ATG2-WIPI/ATG18 lipid-transfer complex used during autophagophore membrane expansion. The GO ATG2-ATG18 complex term is the closest component-level target.
    - [group] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|Regulation of autophagophore membrane composition
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation
        status=context_only scope=too_broad_to_propagate GO=[GO:0016236 macroautophagy]
        rationale: This class is a real macroautophagy context, but its descendants include core factors, component buckets, upstream modulators, localization roles, and residual categories. Projecting generic macroautophagy from this ancestor creates TRAPP-like overpropagation, so candidate GO annotations must come from narrower curated nodes.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## Projected GO annotations (1)
- GO:0062079 ATG2-ATG18 complex | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|Regulation of autophagophore membrane composition|ATG2-WIPI complex component
