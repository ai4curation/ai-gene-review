# PN dossier: ATL3

- review_batch: proteostasis-batch-2026-06-03
- review_yaml: genes/human/ATL3/ATL3-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Autophagy-Lysosome Pathway | Autophagophore initiation and elongation | ULK1 pathway, direct | Modulator of ULK1 activity
- UniProt: Q6DD88
- In branches: ALP
- Notes: Receptor for selective autophagy. ATL3 specifically binds to GABARAP via 2 GABARAP interaction motifs (GIMs). An ER-phagy receptor that promotes tubular ER degradation. Also ATL2/3 directly interact with ULK1 and ATG13 and facilitate the ATG13-mediated recruitment/stabilization of ULK1 and ATG101.
- PN references (titles):
    - Selective Autophagy: ATG8 Family Proteins, LIR Motifs and Cargo Receptors - ScienceDirect
    - Atlastin 2/3 regulate ER targeting of the ULK1 complex to initiate autophagy | Journal of Cell Biology | Rockefeller University Press (rupress.org)
    - ATL3 Is a Tubular ER-Phagy Receptor for GABARAP-Mediated Selective Autophagy
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|ULK1 pathway, direct|Modulator of ULK1 activity
        status=no_mapping scope= GO=[]
        rationale: This PN leaf groups diverse regulators placed around ULK1 activity, but the current members span phosphatase regulation, stress signaling, vesicle/lysosome biology, and proteostasis context rather than a single reusable GO term for ULK1 modulation.
    - [group] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|ULK1 pathway, direct
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation
        status=context_only scope=too_broad_to_propagate GO=[GO:0016236 macroautophagy]
        rationale: This class is a real macroautophagy context, but its descendants include core factors, component buckets, upstream modulators, localization roles, and residual categories. Projecting generic macroautophagy from this ancestor creates TRAPP-like overpropagation, so candidate GO annotations must come from narrower curated nodes.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 2: Autophagy-Lysosome Pathway | Autophagy substrate selection | Selective autophagy receptor | ERphagy
- UniProt: Q6DD88
- In branches: ALP
- Notes: Receptor for selective autophagy. ATL3 specifically binds to GABARAP via 2 GABARAP interaction motifs (GIMs). An ER-phagy receptor that promotes tubular ER degradation. Also ATL2/3 directly interact with ULK1 and ATG13 and facilitate the ATG13-mediated recruitment/stabilization of ULK1 and ATG101.
- PN references (titles):
    - Selective Autophagy: ATG8 Family Proteins, LIR Motifs and Cargo Receptors - ScienceDirect
    - Atlastin 2/3 regulate ER targeting of the ULK1 complex to initiate autophagy | Journal of Cell Biology | Rockefeller University Press (rupress.org)
    - ATL3 Is a Tubular ER-Phagy Receptor for GABARAP-Mediated Selective Autophagy
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|ERphagy
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0061709 reticulophagy]
        rationale: The PN uses the community label ERphagy for selective autophagy of the endoplasmic reticulum, while GO uses the synonym reticulophagy. Receptor members of this PN category are suitable for propagation to the GO reticulophagy process.
    - [group] Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Autophagy substrate selection
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad substrate-selection container. GO has useful targets for specific receptor, cargo-adaptor, and selective-autophagy leaves, but this class mixes marking, recognition, receptor regulation, and unknown roles and should not propagate as one term.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## Projected GO annotations (1)
- GO:0061709 reticulophagy | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|ERphagy
