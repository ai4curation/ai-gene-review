# FGD1 database source guide

The canonical review holds the decisions. [The source table](FGD1-database-source-evidence.yaml) joins each of the 27 database contexts to its unchanged source tuple, exact annotation index and evidence locator. [The phylogeny proof](FGD1-phylogeny-evidence.yaml), [ontology relations](FGD1-ontology-evidence.yaml) and [product boundaries](FGD1-product-evidence.yaml) provide separate reproducible source facts.

| Source | Actual evidence inspected | Limit |
|---|---|---|
| PMID:12913069 | Author-uploaded original Methods; localization and altered-targeting Results; Figures 3–7 captions; Table 1; relevant Discussion | Mouse Fgd1 constructs, principally in COS-7 cells; no figure-pixel or supplement read; endogenous coimmunoprecipitation unavailable in the paper |
| PMID:8969170 | Saved original exchange Results and Figures 1–2 discussion; complete source assessment owned by the direct lane | Human DH–PH fragment, not a natural splice product; exchange is distinct from hydrolysis |
| PTHR12673 / GO_REF:0000033 | Actual version-19 target tree path and MSA; exact four literal positive IBD joins; current family entries and names | Every descendant experiment was not independently reread |
| Mouse P52734 / Ensembl | Official identity, complete manual annotation response, exact ENSMUSP00000026296 lookup and human/mouse one-to-one homology | Orthology is not a new human localization assay |
| HPA / GO_REF:0000052 | FGD1 XML and antibody-specific cell assignments; actual U2OS HPA000911 and A-431 HPA076516 sample images | No integral-membrane topology or quantitative colocalization claim |
| InterPro | P98174 target matches and official IPR000219/IPR000306 mappings | Fold-level inference distinguished from target biochemical measurements |
| ARBA | Exact condition branches 1298, 103 and 4 in the three cited rules, matched to target FunFam/lineage fields | Rule matching is not an additional experiment |
| Reactome | Actual root summations, catalysts, member sets and canonical P98174 entity 194935 | Complete target routes only; unrelated branches and every cited primary were not exhaustively reviewed |

The original donor article is available at [the author-uploaded source](https://www.researchgate.net/publication/10618353_Fgd1_the_Cdc42_GEF_responsible_for_Faciogenital_Dysplasia_directly_interacts_with_cortactin_and_mAbp1_to_modulate_cell_shape). Public database evidence is reproducible through [PANTHER treeinfo](https://www.pantherdb.org/services/oai/pantherdb/treeinfo?family=PTHR12673), [familymsa](https://www.pantherdb.org/services/oai/pantherdb/familymsa?family=PTHR12673), [Reactome FGD1 entity](https://reactome.org/ContentService/data/query/194935), [HPA XML](https://www.proteinatlas.org/ENSG00000102302.xml) and [target InterPro matches](https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P98174/).

The generic HPA selected-thumbnail URL returned 404; genuine sample-image URLs succeeded. An exploratory Golgi-paper lookup encountered a PMC challenge page and Europe PMC 500 response; it was not adopted as an additional normal or used to create a process assertion. Failed access remains separate from positive source evidence. The 19 accepted normal files remain byte-for-byte preserved privately; the ten referenced publication/Reactome/PAINT dependencies form the proposed installation subset.
