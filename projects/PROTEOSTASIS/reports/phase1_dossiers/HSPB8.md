# PN dossier: HSPB8

- review_batch: proteostasis-batch-2026-06-07b
- review_yaml: genes/human/HSPB8/HSPB8-ai-review.yaml
- PN workbook rows: 3

## PN row 1: Cytonuclear proteostasis | Chaperone | small HSP system | small HSP
- UniProt: Q9UJY1
- In branches: CY, MI, ALP
- PN-node mapping records (path + ancestors):
    - [type] Cytonuclear proteostasis|Chaperone|small HSP system|small HSP
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0044183 protein folding chaperone]
        rationale: This PN type denotes small heat-shock chaperones. Protein folding chaperone is the appropriate shared molecular-function term.
    - [group] Cytonuclear proteostasis|Chaperone|small HSP system
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower taxonomy bucket that is already covered by a curated parent mapping or by gene-level annotations. No additional direct GO mapping is appropriate from this node.
    - [class] Cytonuclear proteostasis|Chaperone
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a specific GO class. The member genes span multiple activities, complexes, or contexts, so propagation from this node would overstate the shared biology; use narrower child or gene-level curations.
    - [branch] Cytonuclear proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## PN row 2: Mitochondrial proteostasis | Chaperone | small HSP
- UniProt: Q9UJY1
- In branches: CY, MI, ALP
- PN-node mapping records (path + ancestors):
    - [group] Mitochondrial proteostasis|Chaperone|small HSP
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0044183 protein folding chaperone]
        rationale: This PN group denotes mitochondrial small heat-shock chaperones. Protein folding chaperone is the appropriate shared molecular-function term.
    - [class] Mitochondrial proteostasis|Chaperone
        status=no_mapping scope= GO=[]
        rationale: This PN class is too heterogeneous for a single safe GO mapping. In the workbook it mixes HSP70, HSP60, and HSP90 systems, small intermembrane-space chaperones, membrane-protein chaperones, and other mitochondrial-specific factors.
    - [branch] Mitochondrial proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## PN row 3: Autophagy-Lysosome Pathway | Autophagy substrate selection | Selective autophagy receptor | Chaperone assisted selective autophagy | CASA complex component
- UniProt: Q9UJY1
- In branches: CY, MI, ALP
- Notes: Small heat shock protein. Participates in chaperone-assisted selective autophagy by forming the CASA complex (HSPA8, BAG3, HSPB8, and STUB1) that delivers ubiquitinated substrates to the to the autophagosome
- PN references (titles):
    - Full article: The chaperone-assisted selective autophagy complex dynamics and dysfunctions (tandfonline.com)
    - small heat shock protein B8 (HspB8) promotes autophagic removal of misfolded proteins involved in amyotrophic lateral sclerosis (ALS) | Human Molecular Genetics | Oxford Academic (oup.com)
    - A Surveillance Function of the HSPB8-BAG3-HSP70 Chaperone Complex Ensures Stress Granule Integrity and Dynamism - ScienceDirect
- PN-node mapping records (path + ancestors):
    - [subtype] Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|Chaperone assisted selective autophagy|CASA complex component
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0035973 aggrephagy]
        rationale: The PN CASA subtype covers BAG3-HSPB8-HSP70-system machinery that directs damaged or aggregation-prone substrates into selective autophagic clearance. GO lacks a dedicated CASA term in the current cache, and this subtype includes chaperones and cofactors beyond pure cargo adaptors, so aggrephagy is the closest available process target.
    - [type] Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|Chaperone assisted selective autophagy
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a contextual PN role. The label is useful for curator triage, but by itself does not support a universal GO assertion for all member genes beyond curated ancestor or child mappings.
    - [group] Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Autophagy substrate selection
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad substrate-selection container. GO has useful targets for specific receptor, cargo-adaptor, and selective-autophagy leaves, but this class mixes marking, recognition, receptor regulation, and unknown roles and should not propagate as one term.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## Projected GO annotations (3)
- GO:0044183 protein folding chaperone | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Cytonuclear proteostasis|Chaperone|small HSP system|small HSP
- GO:0044183 protein folding chaperone | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Mitochondrial proteostasis|Chaperone|small HSP
- GO:0035973 aggrephagy | scope=ok_for_propagation_to_go | goa_status=supported_by_goa_regulation | from=Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|Chaperone assisted selective autophagy|CASA complex component
