# PN dossier: AMBRA1

- review_batch: proteostasis-batch-2026-06-03
- review_yaml: genes/human/AMBRA1/AMBRA1-ai-review.yaml
- PN workbook rows: 3

## PN row 1: Autophagy-Lysosome Pathway | Autophagophore initiation and elongation | Class 3 PI3K complex 1, direct | Modulator of class 3 PI3K complex 1 activity | Modulator of BECN1 localization
- UniProt: Q9C0C7
- In branches: ALP, UPS
- Notes: Interacts with BECN1 to tether the PI3K complex to the dynein motor complex. CUL4A/B-DDB1-AMBRA1 complex mediates K63 ubiquitination of BECN1, increasing activity of VPS34. Phosphorylation of AMBRA1 by ULK1 releases the PI3K complex to allow autophagy induction. Also an enahncer of chaperone-mediated autophagy by promoting substrate uptake.
- PN references (titles):
    - Full article: Connecting autophagy: AMBRA1 and its network of regulation (tandfonline.com)
    - mTOR inhibits autophagy by controlling ULK1 ubiquitylation, self-association and function through AMBRA1 and TRAF6 | Nature Cell Biology
    - Chaperone-mediated autophagy prevents collapse of the neuronal metastable proteome - ScienceDirect
- PN-node mapping records (path + ancestors):
    - [subtype] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|Class 3 PI3K complex 1, direct|Modulator of class 3 PI3K complex 1 activity|Modulator of BECN1 localization
        status=context_only scope=too_broad_to_propagate GO=[GO:0035032 phosphatidylinositol 3-kinase complex, class III]
        rationale: Reviewed as a class-III PI3K complex context or regulator bucket. This node is useful for curator interpretation, but it should not project cellular-component membership; only explicit complex-component leaves propagate to GO complex terms.
    - [type] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|Class 3 PI3K complex 1, direct|Modulator of class 3 PI3K complex 1 activity
        status=context_only scope=too_broad_to_propagate GO=[GO:0035032 phosphatidylinositol 3-kinase complex, class III]
        rationale: Reviewed as a class-III PI3K complex context or regulator bucket. This node is useful for curator interpretation, but it should not project cellular-component membership; only explicit complex-component leaves propagate to GO complex terms.
    - [group] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|Class 3 PI3K complex 1, direct
        status=context_only scope=too_broad_to_propagate GO=[GO:0035032 phosphatidylinositol 3-kinase complex, class III]
        rationale: Reviewed as a class-III PI3K complex context or regulator bucket. This node is useful for curator interpretation, but it should not project cellular-component membership; only explicit complex-component leaves propagate to GO complex terms.
    - [class] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation
        status=context_only scope=too_broad_to_propagate GO=[GO:0016236 macroautophagy]
        rationale: This class is a real macroautophagy context, but its descendants include core factors, component buckets, upstream modulators, localization roles, and residual categories. Projecting generic macroautophagy from this ancestor creates TRAPP-like overpropagation, so candidate GO annotations must come from narrower curated nodes.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 2: Autophagy-Lysosome Pathway | Chaperone-mediated autophagy | Lysosomal modulator of chaperone-mediated autophagy | Chaperone-mediated autophagy enhancer | Enhancer of substrate uptake
- UniProt: Q9C0C7
- In branches: ALP, UPS
- Notes: Interacts with BECN1 to tether the PI3K complex to the dynein motor complex. CUL4A/B-DDB1-AMBRA1 complex mediates K63 ubiquitination of BECN1, increasing activity of VPS34. Phosphorylation of AMBRA1 by ULK1 releases the PI3K complex to allow autophagy induction. Also an enahncer of chaperone-mediated autophagy by promoting substrate uptake.
- PN references (titles):
    - Full article: Connecting autophagy: AMBRA1 and its network of regulation (tandfonline.com)
    - mTOR inhibits autophagy by controlling ULK1 ubiquitylation, self-association and function through AMBRA1 and TRAF6 | Nature Cell Biology
    - Chaperone-mediated autophagy prevents collapse of the neuronal metastable proteome - ScienceDirect
- PN-node mapping records (path + ancestors):
    - [subtype] Autophagy-Lysosome Pathway|Chaperone-mediated autophagy|Lysosomal modulator of chaperone-mediated autophagy|Chaperone-mediated autophagy enhancer|Enhancer of substrate uptake
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a contextual PN role. The label is useful for curator triage, but by itself does not support a universal GO assertion for all member genes beyond curated ancestor or child mappings.
    - [type] Autophagy-Lysosome Pathway|Chaperone-mediated autophagy|Lysosomal modulator of chaperone-mediated autophagy|Chaperone-mediated autophagy enhancer
        status=mapped scope=ok_for_propagation_to_go GO=[GO:1904716 positive regulation of chaperone-mediated autophagy]
        rationale: This PN type explicitly records enhancer roles for CMA. The directional GO regulation term is more accurate than projecting direct participation in CMA from the class ancestor.
    - [group] Autophagy-Lysosome Pathway|Chaperone-mediated autophagy|Lysosomal modulator of chaperone-mediated autophagy
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Chaperone-mediated autophagy
        status=context_only scope=too_broad_to_propagate GO=[GO:0061684 chaperone-mediated autophagy]
        rationale: The class label matches the GO CMA process, but the subtree includes both effectors and positive or negative modulators. The relation is retained as context so modulators are not projected as direct CMA participants unless a narrower node supports it.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 3: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | Cul4A/Cul4B substrate receptor | WD40 | other
- UniProt: Q9C0C7
- In branches: ALP, UPS
- Signature domains: (none)
- Auxiliary domains: IPR001680
- PN references (titles):
    - 33854239
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul4A/Cul4B substrate receptor|WD40|other
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower substrate-receptor, adaptor, domain, or family subdivision already covered by the curated parent adaptor/receptor mapping. No additional direct GO mapping is needed at this node.
    - [type] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul4A/Cul4B substrate receptor|WD40
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower substrate-receptor, adaptor, domain, or family subdivision already covered by the curated parent adaptor/receptor mapping. No additional direct GO mapping is needed at this node.
    - [group] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul4A/Cul4B substrate receptor
        status=mapped scope=ok_for_propagation_to_go GO=[GO:1990756 ubiquitin-like ligase-substrate adaptor activity]
        rationale: This PN group captures substrate receptors/adaptors for cullin/UBL ligase systems. The shared GO molecular-function target is ubiquitin-like ligase-substrate adaptor activity.
    - [class] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases
        status=context_only scope=too_broad_to_propagate GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This class is a genuine E3-ligase context, but its descendants include catalytic ligases, cullin scaffolds, substrate receptors, adaptors, cofactors, regulators, and UBL modifier systems. A class-level propagation would over-annotate.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (2)
- GO:1904716 positive regulation of chaperone-mediated autophagy | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Autophagy-Lysosome Pathway|Chaperone-mediated autophagy|Lysosomal modulator of chaperone-mediated autophagy|Chaperone-mediated autophagy enhancer
- GO:1990756 ubiquitin-like ligase-substrate adaptor activity | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul4A/Cul4B substrate receptor
