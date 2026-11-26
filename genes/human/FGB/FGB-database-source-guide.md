# FGB database source guide

This guide records what was inspected for the database-derived contexts. Canonical decisions remain in `FGB-ai-review.yaml`. The [source-keyed evidence record](FGB-database-source-evidence.yaml) retains every owned original source object, row index and exact Reactome containment route without duplicating the review text. Publication caches are immutable; reference-only citations do not assert that a quotation was validated.

## InterPro, combined mapping and HPA

- **GO_REF:0000002:** The actual InterPro P02675 response contains six matches. IPR012290 spans residues 90–235 and supplies the receptor-binding, complex, activation and polymerization mappings. IPR037579 spans 230–490 and supplies the coagulation mapping. The other matches are IPR002181, IPR014716, IPR020837 and IPR036056. Entry metadata and target matches were inspected separately; a domain label is not an independent binding assay. Human-chain assembly and structure are scoped under PMID:8910396 and PMID:19296670 in the direct source guide.
- **GO_REF:0000120:** ARBA00027128 genuinely outputs GO:0005576. Its full captured rule contains 280 condition branches. Branch 154 requires positive FunFam identifiers `3.90.215.10:FF:000006` and `4.10.530.10:FF:000004`, both present in the accepted P02675 UniProt record, with no additional taxonomic condition. UniProt SL-0243 is a separate reviewed Secreted assignment. This verifies the prediction's actual source conditions without labeling them as a new secretion experiment.
- **GO_REF:0000052:** [HPA FGB subcellular record](https://www.proteinatlas.org/ENSG00000171564-FGB/subcellular), release 25. The HepG2 assignments and selected images HPA001900/1293_G5_6 and HPA001901/1761_F11_3 were read/viewed. Both antibodies have enhanced ER assignments; no corresponding positive U2OS localization was present in the inspected data. Images support the stated compartment at their resolution, not a processed-product or luminal-topology assignment.

## Ensembl ortholog transfers

Actual protein lookups and human-to-donor one-to-one orthology records join ENSP00000306099 to mouse ENSMUSP00000039472/Q8K0E8 and rat ENSRNOP00000050663/P14480. These establish the source chain, not functional equivalence from sequence similarity alone.

| Source | Operative material inspected | Boundary |
|---|---|---|
| PMID:15914557 | Author-uploaded original: Materials and methods, “Fluorescence imaging of fibrinogen-receptor activation”; Figure 1 caption; first Results section. | Added fibrinogen binds mouse megakaryocyte exteriors. Ligand species is unstated. No intracellular cortex or endogenous mouse Fgb assay; pixels/video unread. |
| PMID:16452087 | Verified abstract and actual indexed publisher Methods for mouse-brain postsynaptic-density proteomics. | Exact Fgb Supplement S1 identification and complete operative supplement were not recovered. Mixed neuronal compartments do not themselves establish contamination. |
| PMID:17521427 | Genuine PMC1890559 original XML: expression Results, Table 1 Fgb entries, Figures 1/3/5 captions, receptor-control Results, relevant Discussion and Methods. | Rat-cell transcript response; mouse receptor constructs/murine leptin and human interleukin-1 are part of that context. No human FGB regulatory measurement or FGB signaling-effector assay; figure pixels/SI unread. |
| PMID:22014850 | Verified abstract and bounded actual publisher original material, DOI 10.1016/j.thromres.2011.09.016. | Rat pulmonary-embolism microparticles; exact target table and full preparation controls remain inaccessible. Earlier incorrect publisher locators are failed requests, not evidence. |

The normal caches for PMID:15914557, PMID:16452087 and PMID:22014850 remain abstract-only. The separately recovered full text of PMID:15914557 is therefore distinguished from its cache status. PMID:17521427 has genuine full XML available.

## PAINT placement

The [phylogeny evidence](FGB-phylogeny-evidence.yaml) records four exact positive IBD joins, actual target-to-node ancestry, the 491-residue ungapped sequence hash, genuine acquisition URLs and source hashes. Current PTHR47221 files call the family “FIBRINOGEN ALPHA CHAIN” and the target subfamily “FIBRINOGEN C-TERMINAL DOMAIN-CONTAINING PROTEIN”; both labels are preserved verbatim. The older API version-19 topology uses PTHR19143, “FIBRINOGEN/TENASCIN/ANGIOPOEITIN,” with target subfamily “FIBRINOGEN BETA CHAIN.” Persistent nodes join these versions. The separate version-19 PTHR47221 tree contains FGA and is not used as FGB ancestry evidence.

The target descends from PTN000441162 and PTN002709771. Self-WITH is valid descendant evidence, not circularity. No conclusion rests on the number of donors. All descendant experimental sources were not independently reread; target structure and the scoped direct evidence determine the biological interpretation.

## Reactome event and product scope

All 44 actual event summations and nested target routes were inspected. The saved graph has 223 genuine objects and reaches P02675 in every assigned event. Unrelated ligand branches were not expanded into an assertion of complete pathway coverage. The [evidence record](FGB-database-source-evidence.yaml) gives each event ID, literal component/member positions, target coordinates and compartment.

| Event group | Actual target role |
|---|---|
| R-HSA-140840, R-HSA-140842, R-HSA-140851 | Thrombin substrate/released peptide/fibrin-chain separation; structural fibrin assembly; factor-XIII cross-linking. Beta is not either enzyme. |
| R-HSA-114560, R-HSA-216069, R-HSA-216082, R-HSA-9921091 | Mature beta-containing fibrin in extracellular integrin complexes or associated with the cell exterior. No transmembrane beta topology. |
| R-HSA-354066, 354073, 354087, 354124, 354149, 354165, 372693, 372697, 372705, 377640, 377641, 377643, 377644, 429415, 429441 | Beta persists in the extracellular fibrin ligand while the receptor-associated machinery undergoes recruitment or signaling. The event title is not transferred as beta-chain enzymatic activity. |
| R-HSA-8870678, 166072, 166082, 166091, 166119, 166284, 166286, 166362, 166363, 2201316, 2201322, 2262775, 2262777, 2559414, 5602353, 5602383, 5602606, 937022, 937059, 937079 | The modeled TLR ligand hierarchy reaches fibrinopeptide B, entity 140876 at 31–44, extracellularly. That model is not independent isolated-peptide agonism evidence; defective MyD88/IRAK4 events are not FGB mutation experiments. |
| R-HSA-481007 | Fibrinogen beta at 31–491 is granule-lumen cargo and released extracellular material. Cargo location does not establish an exocytosis-machine role. |
| R-HSA-9936699 | Extracellular fibrinogen associated with amyloid-beta fibrils and zinc, not an FGB-derived amyloid precursor. |

The source-specific locations can be positive even where the modeled event's mechanistic title belongs to another protein. The event-linked primary bibliography was not comprehensively reread. The [product map](FGB-database-product-evidence.yaml) keeps these literal source coordinates separate from all 113 parent-accession annotations.

## Scope of synthesis

The separately proposed structural core uses human-chain assembly (PMID:8910396), human plasma fibrinogen structure (PMID:19296670) and R-HSA-140842. It covers complex integrity and clot structure. It does not infer an autonomous beta receptor-binding site, alpha-C cofactor activity, a free fibrinopeptide-B activity or a novel process annotation. The single proposed core BP has no redundant parent/child pair.

The genuine provider invocation did not produce a report. Sensitive traces remain private and were not decoded. This authored guide is an evidence journal, not a provider report.
