# Itpr3 (rat) review notes

- Fetched with `just fetch-gene rat Itpr3`; UniProt Q63269 (ITPR3_RAT, Swiss-Prot), RGD:2934, GeneID 25679. 95 GOA rows.
- No deep-research provider available; manual synthesis in `Itpr3-deep-research-manual.md`.
- Modelled decisions on the completed rat Itpr1 review for consistency.

## Key decisions
- Core MF GO:0005220 accepted on all rows; general channel/transport MF terms (GO:0005216, GO:0005262, GO:0015085, GO:0015278) MODIFY to GO:0005220.
- Transport BP rows (GO:0006811, GO:0006816, GO:0055085, GO:0070588, GO:0051209, GO:0007204) MODIFY to GO:1903514 (ER-specific release; descendant of GO:0051209 verified in OLS).
- GO:0035091 phosphatidylinositol binding MODIFY to GO:0070679 IP3 binding with a source_defects entry (IP3 is soluble, not a PI lipid).
- GO:0005903 brush border (PMID:8288584): abstract says staining is *adjacent to* the brush border -> MARK_AS_OVER_ANNOTATED plus suspected source defect; apical part of cell kept. Paper is mainly human (HT29 cDNA); species of stained tissue not stated in abstract [PMID:8288584 "cDNA clones encoding InsP3Rs were isolated from a human colon adenocarcinoma cell line, HT29"].
- Dendrite (PMID:17471556) and neuronal cell body (PMID:17091480) UNDECIDED: abstract-only, abstracts foreground IP3R1 / Schwann cells.
- Nucleoplasm / nucleolus ISO MARK_AS_OVER_ANNOTATED; nucleus ISO MODIFY to nuclear envelope.
- Memory/LTP ISO (mouse phenotype) MARK_AS_OVER_ANNOTATED; taste ISO rows kept non-core (IP3R3 performs the Ca2+-release step in type II taste cells).
- Two bare protein-binding rows removed (policy).
- No NEW rows proposed.
