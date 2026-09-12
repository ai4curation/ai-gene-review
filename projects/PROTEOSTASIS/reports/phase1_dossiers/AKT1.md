# PN dossier: AKT1

- review_batch: proteostasis-batch-2026-06-03
- review_yaml: genes/human/AKT1/AKT1-ai-review.yaml
- PN workbook rows: 3

## PN row 1: Autophagy-Lysosome Pathway | Pre-initiation autophagy signaling | mTORC1 pathway, upstream | Insulin signaling pathway | TSC complex deactivator
- UniProt: P31749
- In branches: ALP
- Notes: Inhibits TSC1-TSC2 complex by phosphorylating TSC2. Also phosphorylates GFAP to prevent it from interacting with and stabilizing the LAMP2 translocation pore in chaperone-mediated autophagy. AKT1 also phosphorylates FOXO1 and FOXO3 which prevents their nuclear translocation and the transcription of autophagy-related genes by FOXO1 and FOXO3. Also inhibits chaperone-mediated autophagy by modulating LAMP2A multimerization.
- PN references (titles):
    - p53 Regulation of the IGF-1/AKT/mTOR Pathways and the Endosomal Compartment (cshlp.org)
    - Lysosomal mTORC2/PHLPP1/Akt Regulate Chaperone-Mediated Autophagy - ScienceDirect
    - Nuclear Trapping of the Forkhead Transcription Factor FoxO1 via Sirt-dependent Deacetylation Promotes Expression of Glucogenetic Genes* - Journal of Biological Chemistry (jbc.org)
    - Akt Promotes Cell Survival by Phosphorylating and Inhibiting a Forkhead Transcription Factor - ScienceDirect
    - Chaperone-mediated autophagy prevents collapse of the neuronal metastable proteome - ScienceDirect
    - Proteome-wide analysis of chaperone-mediated autophagy targeting motifs | PLOS Biology
- PN-node mapping records (path + ancestors):
    - [subtype] Autophagy-Lysosome Pathway|Pre-initiation autophagy signaling|mTORC1 pathway, upstream|Insulin signaling pathway|TSC complex deactivator
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a contextual PN role. The label is useful for curator triage, but by itself does not support a universal GO assertion for all member genes beyond curated ancestor or child mappings.
    - [type] Autophagy-Lysosome Pathway|Pre-initiation autophagy signaling|mTORC1 pathway, upstream|Insulin signaling pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a contextual PN role. The label is useful for curator triage, but by itself does not support a universal GO assertion for all member genes beyond curated ancestor or child mappings.
    - [group] Autophagy-Lysosome Pathway|Pre-initiation autophagy signaling|mTORC1 pathway, upstream
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Pre-initiation autophagy signaling
        status=context_only scope=too_broad_to_propagate GO=[GO:0010506 regulation of autophagy]
        rationale: This class organizes upstream signaling inputs to autophagy initiation. Because the subtree contains generic insulin, AMPK, mTORC1, nutrient-sensing, and miscellaneous signaling components, class-level propagation to regulation of autophagy would over-annotate many genes.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 2: Autophagy-Lysosome Pathway | Autophagy gene expression | FOXO transcriptional program | Modulator of FOXO1 and FOXO3 activity
- UniProt: P31749
- In branches: ALP
- Notes: Inhibits TSC1-TSC2 complex by phosphorylating TSC2. Also phosphorylates GFAP to prevent it from interacting with and stabilizing the LAMP2 translocation pore in chaperone-mediated autophagy. AKT1 also phosphorylates FOXO1 and FOXO3 which prevents their nuclear translocation and the transcription of autophagy-related genes by FOXO1 and FOXO3. Also inhibits chaperone-mediated autophagy by modulating LAMP2A multimerization.
- PN references (titles):
    - p53 Regulation of the IGF-1/AKT/mTOR Pathways and the Endosomal Compartment (cshlp.org)
    - Lysosomal mTORC2/PHLPP1/Akt Regulate Chaperone-Mediated Autophagy - ScienceDirect
    - Nuclear Trapping of the Forkhead Transcription Factor FoxO1 via Sirt-dependent Deacetylation Promotes Expression of Glucogenetic Genes* - Journal of Biological Chemistry (jbc.org)
    - Akt Promotes Cell Survival by Phosphorylating and Inhibiting a Forkhead Transcription Factor - ScienceDirect
    - Chaperone-mediated autophagy prevents collapse of the neuronal metastable proteome - ScienceDirect
    - Proteome-wide analysis of chaperone-mediated autophagy targeting motifs | PLOS Biology
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Autophagy gene expression|FOXO transcriptional program|Modulator of FOXO1 and FOXO3 activity
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a contextual PN role. The label is useful for curator triage, but by itself does not support a universal GO assertion for all member genes beyond curated ancestor or child mappings.
    - [group] Autophagy-Lysosome Pathway|Autophagy gene expression|FOXO transcriptional program
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Autophagy gene expression
        status=context_only scope=too_broad_to_propagate GO=[GO:0010506 regulation of autophagy]
        rationale: This class records autophagy-linked gene-expression programs, but many nodes are transcription program names or upstream modulators rather than direct GO regulation assertions. It is kept as context only; transcription factor or cofactor activities are mapped at narrower nodes.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 3: Autophagy-Lysosome Pathway | Chaperone-mediated autophagy | Lysosomal modulator of chaperone-mediated autophagy | Chaperone-mediated autophagy inhibitor | Modulator of LAMP2A multimerization
- UniProt: P31749
- In branches: ALP
- Notes: Inhibits TSC1-TSC2 complex by phosphorylating TSC2. Also phosphorylates GFAP to prevent it from interacting with and stabilizing the LAMP2 translocation pore in chaperone-mediated autophagy. AKT1 also phosphorylates FOXO1 and FOXO3 which prevents their nuclear translocation and the transcription of autophagy-related genes by FOXO1 and FOXO3. Also inhibits chaperone-mediated autophagy by modulating LAMP2A multimerization.
- PN references (titles):
    - p53 Regulation of the IGF-1/AKT/mTOR Pathways and the Endosomal Compartment (cshlp.org)
    - Lysosomal mTORC2/PHLPP1/Akt Regulate Chaperone-Mediated Autophagy - ScienceDirect
    - Nuclear Trapping of the Forkhead Transcription Factor FoxO1 via Sirt-dependent Deacetylation Promotes Expression of Glucogenetic Genes* - Journal of Biological Chemistry (jbc.org)
    - Akt Promotes Cell Survival by Phosphorylating and Inhibiting a Forkhead Transcription Factor - ScienceDirect
    - Chaperone-mediated autophagy prevents collapse of the neuronal metastable proteome - ScienceDirect
    - Proteome-wide analysis of chaperone-mediated autophagy targeting motifs | PLOS Biology
- PN-node mapping records (path + ancestors):
    - [subtype] Autophagy-Lysosome Pathway|Chaperone-mediated autophagy|Lysosomal modulator of chaperone-mediated autophagy|Chaperone-mediated autophagy inhibitor|Modulator of LAMP2A multimerization
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a contextual PN role. The label is useful for curator triage, but by itself does not support a universal GO assertion for all member genes beyond curated ancestor or child mappings.
    - [type] Autophagy-Lysosome Pathway|Chaperone-mediated autophagy|Lysosomal modulator of chaperone-mediated autophagy|Chaperone-mediated autophagy inhibitor
        status=mapped scope=ok_for_propagation_to_go GO=[GO:1904715 negative regulation of chaperone-mediated autophagy]
        rationale: This PN type explicitly records inhibitory roles for CMA. The directional GO regulation term is more accurate than projecting direct participation in CMA from the class ancestor.
    - [group] Autophagy-Lysosome Pathway|Chaperone-mediated autophagy|Lysosomal modulator of chaperone-mediated autophagy
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Chaperone-mediated autophagy
        status=context_only scope=too_broad_to_propagate GO=[GO:0061684 chaperone-mediated autophagy]
        rationale: The class label matches the GO CMA process, but the subtree includes both effectors and positive or negative modulators. The relation is retained as context so modulators are not projected as direct CMA participants unless a narrower node supports it.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## Projected GO annotations (1)
- GO:1904715 negative regulation of chaperone-mediated autophagy | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Autophagy-Lysosome Pathway|Chaperone-mediated autophagy|Lysosomal modulator of chaperone-mediated autophagy|Chaperone-mediated autophagy inhibitor
