# PN dossier: GBA1

- review_batch: proteostasis-pr-1217
- review_yaml: genes/human/GBA1/GBA1-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Autophagy-Lysosome Pathway | Lysosomal catabolism | Lysosomal lipid catabolism | Lysosomal sphingomyelin/ceramide metabolism | Lysosomal ceramidase
- UniProt: P04062
- In branches: ALP
- Notes: Catabolic enzyme of the lysosome, per Gene ontology. Also autophagic lysosomal reformation is impaired in GBA1 mutants, potentially increasing susceptibility to Parkinson's Disease.
- PN references (titles):
    - Autophagic lysosome reformation dysfunction in glucocerebrosidase deficient cells: relevance to Parkinson disease | Human Molecular Genetics | Oxford Academic (oup.com)
    - The proteome of lysosomes - Schröder - 2010 - PROTEOMICS - Wiley Online Library
    - hLGDB: a database of human lysosomal genes and their regulation | Database | Oxford Academic (oup.com)
- PN-node mapping records (path + ancestors):
    - [subtype] Autophagy-Lysosome Pathway|Lysosomal catabolism|Lysosomal lipid catabolism|Lysosomal sphingomyelin/ceramide metabolism|Lysosomal ceramidase
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a mixed lysosomal ceramide/glycosylceramide hydrolase bucket containing ASAH1, GALC, and GBA1. The current GO cache lacks a non-obsolete ceramidase term that safely covers all members, so no direct universal mapping is made.
    - [type] Autophagy-Lysosome Pathway|Lysosomal catabolism|Lysosomal lipid catabolism|Lysosomal sphingomyelin/ceramide metabolism
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a mixed sphingomyelin/ceramide metabolism container. The child leaves include enzymes and activators with different molecular functions, so direct propagation from the container would lose specificity.
    - [group] Autophagy-Lysosome Pathway|Lysosomal catabolism|Lysosomal lipid catabolism
        status=context_only scope=too_broad_to_propagate GO=[GO:0016042 lipid catabolic process]
        rationale: This group is a lysosomal lipid-catabolism context, but it mixes lipases, phospholipases, sphingolipid enzymes, and activators. Specific molecular functions are mapped at narrower leaves.
    - [class] Autophagy-Lysosome Pathway|Lysosomal catabolism
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad lysosomal-degradation container. The subtree includes carbohydrate, lipid, protein, nuclease, phosphatase, sulfatase, and environment-regulation roles, so mapping should occur at the enzyme or process subtype level.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 2: Autophagy-Lysosome Pathway | Autophagic lysosome reformation | Specific function in autophagic lysosome reformation unknown
- UniProt: P04062
- In branches: ALP
- Notes: Catabolic enzyme of the lysosome, per Gene ontology. Also autophagic lysosomal reformation is impaired in GBA1 mutants, potentially increasing susceptibility to Parkinson's Disease.
- PN references (titles):
    - Autophagic lysosome reformation dysfunction in glucocerebrosidase deficient cells: relevance to Parkinson disease | Human Molecular Genetics | Oxford Academic (oup.com)
    - The proteome of lysosomes - Schröder - 2010 - PROTEOMICS - Wiley Online Library
    - hLGDB: a database of human lysosomal genes and their regulation | Database | Oxford Academic (oup.com)
- PN-node mapping records (path + ancestors):
    - [group] Autophagy-Lysosome Pathway|Autophagic lysosome reformation|Specific function in autophagic lysosome reformation unknown
        status=no_mapping scope= GO=[]
        rationale: This PN group explicitly states that the specific role within autophagic lysosome reformation is unknown. That makes GO propagation unsafe until a narrower mechanistic interpretation is available.
    - [class] Autophagy-Lysosome Pathway|Autophagic lysosome reformation
        status=context_only scope=too_broad_to_propagate GO=[GO:0007040 lysosome organization]
        rationale: Autophagic lysosome reformation is the lysosome-regeneration phase that follows autolysosome formation and cargo degradation. As a class, it is better aligned to lysosome organization than to generic autophagy, but the PN members are mechanistically mixed across membrane remodeling, tubulation, product efflux, and unknown late-stage roles, so class-level propagation would still over-annotate.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.
