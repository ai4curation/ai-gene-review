---
title: DOCK7 source and assay guide
gene: DOCK7
annotation_scope:
  imported_annotations: 39
  new_annotations: 0
---

# DOCK7 source and assay guide

The review separates nucleotide exchange from GTP hydrolysis, native products from engineered fragments, and cellular association from a purified binding interface. Thirty-nine imported assertions represent forty raw GOA contexts; the NOD2 assertion merges two provider contexts. Every imported source field is retained. The signed positive-Rho refinement covers RAC1 and the conditionally demonstrated CDC42 substrate without erasing the independent Rac assertion.

## Mechanisms, constructs and locations

| Source | Operative experiment and boundary |
|---|---|
| [PMID:23718289, Methods and Figures 1–6](https://pmc.ncbi.nlm.nih.gov/articles/PMC3752685/) | Purified human historical DHR2 fragments catalyze exchange on prenylated RAC1/CDC42 in liposomes. Soluble/nonprenylated controls, nucleotide-state-dependent binding and the V1885A control distinguish the tested activities. Full protein aggregated and was not the functional reagent. |
| [PMID:22842144](https://pubmed.ncbi.nlm.nih.gov/22842144/) | Mouse cortical knockdown/rescue separates TACC3-dependent microtubule growth and nuclear migration from DHR2. Human SK-N-BE cells independently show centrosomal colocalization, not a human cortical migration assay. |
| [PMID:16982419](https://pubmed.ncbi.nlm.nih.gov/16982419/) | The complete abstract supports Rac-dependent axon formation and axonal enrichment. Original full text remained inaccessible. GAP activity, growth cone, basal-cell localization and progenitor apicobasal polarity therefore remain unresolved at their own source scope. |
| [PMID:29467281, Figure 5C, EV4B and Figure 6D](https://pmc.ncbi.nlm.nih.gov/articles/PMC5891429/) | DOCK7 co-immunoprecipitates with LRCH3/LRCH1. Figure 6D compares mock and DHR2 in parental and stable-LRCH3 RPE cells; the combination produces rings in approximately 80% of cells. This measured redistribution supports a non-core organization context, while the proposed GEF mechanism remains speculative. Human isoform 4 is named in Methods, but historical coordinates extend to 2140; current product 4 is 2098 residues. Direct MYO6–LRCH3 evidence is distinct from DOCK7 association. |
| [PMID:32203420, Figures 5/6 and Supplementary Tables 1/2/4](https://doi.org/10.1038/s41556-020-0488-x) | DOCK7–LRCH co-immunoprecipitation and localization were read in the original author-hosted version and deposited tables. Table 1's DNA differs from its full-length/product-style label; Table 2 has no positive DOCK7 activity-screen result. No loss of all DOCK7 activity follows from that screen. |

The [construct analysis](DOCK7-bioinformatics/constructs/RESULTS.md) includes executable scripts, exact primary workbook and official sequence inputs, independent DOCK6 controls, and checked output. The human [DQ118679.1 record](https://www.ebi.ac.uk/ena/browser/view/DQ118679.1) encodes a 1992-residue partial CDS. Its DHR2s and DHR2c correspond to current canonical residues 1678–2118 and 1836–2140 respectively. The current seven products have lengths 2140, 2129, 2100, 2098, 2109, 2131 and 632 residues; activity is not transferred indiscriminately among them.

The cytosolic core location is supported by the target-resolved curated Reactome representation: [event R-HSA-8875591](https://reactome.org/content/detail/R-HSA-8875591) → [catalyst 8875590](https://reactome.org/ContentService/data/query/8875590) → [active candidate set 8875579](https://reactome.org/ContentService/data/query/8875579) → [DOCK7 entity 1012970](https://reactome.org/ContentService/data/query/1012970) → [Q96N67 reference entity 89253](https://reactome.org/ContentService/data/query/89253). This is a curated model, not a new microscopy experiment. The retrieved HPA target record did not contain ICC subcellular-location data. The GEF core also retains axon from the complete 2006 abstract's explicit axonal enrichment and Rac-dependent axon-formation observations. Detailed organism and construct Methods were unavailable, so no finer assay identity is asserted. Centrosomal observations remain in the separate TACC3 core. Liposome assays alone do not establish native plasma-membrane localization.

## Associations and contextual processes

| Source | Target-specific evidence |
|---|---|
| [PMID:27812135, interaction comparison and BRET Results](https://pmc.ncbi.nlm.nih.gov/articles/PMC5094585/) | Initial Y2H and saturable BRET are positive; co-IP in 1% Triton X-100 is negative. [Original Table 1](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0165420#pone.0165420.t001) gives DOCK7 10/0/10 points, total 20, without the full-length Y2H reconfirmation flag. These are assay scores, not affinities. The tested NF-kB reporter, MDP-responsive BRET and expression responses do not establish native DOCK7 immune signaling. NOD2 receptor identity supports the bounded binding class, not agonism or a purified interface. |
| [PMID:29187380, author manuscript](https://repository.icr.ac.uk/bitstreams/ac2b7b86-d189-471e-aa3d-af2feeb0a2d9/download) | Human HEK293T SEC16A/NBEAL2-fragment complexes recover DOCK7. Native megakaryocyte-related co-IP and human megakaryocyte proximity assays corroborate NBEAL2 association; they do not establish purified direct interfaces. |
| [PMID:18850735, Results and purification controls](https://pmc.ncbi.nlm.nih.gov/articles/PMC2676908/) | Tagged CSN5 purification and immunoblotting recover endogenous DOCK7 in human 293 cells. The imported colocalizes_with relation is retained; this is not DOCK7 deneddylase activity. |
| [PMID:21423176, cell/FA preparation and mass-spectrometry Methods](https://pmc.ncbi.nlm.nih.gov/articles/PMC3279191/) | Human HFF1 focal adhesions were profiled reproducibly. The DOCK7-specific supplementary identification row was not independently recovered. The curator's contextual detection is retained without treating a failed supplement retrieval as contrary evidence. |
| [PMID:22158624, migration Results and Methods](https://pmc.ncbi.nlm.nih.gov/articles/PMC3281737/) | Human pulmonary arterial smooth-muscle migration decreases after DOCK7 depletion. Rat PAC1 re-expression is separate; the contractility effects attributed to DOCK4/5 are not assigned to DOCK7. |
| [PMID:23553822, cold-response Results](https://pmc.ncbi.nlm.nih.gov/articles/PMC3743939/) | Brown-fat function and innervation are altered, while cold-induced white-fat browning is interpreted as compensation. The phenotype is valid, but compensation does not establish DOCK7 itself as a negative thermogenic regulator. That ISS assertion is over-annotated; neither a simple tissue-independent sign reversal nor a positive-thermogenesis replacement follows. |

The [public interaction extraction](DOCK7-bioinformatics/interactions/RESULTS.md) reproduces nine incident/two selected AP-MS edges and eighteen incident/two selected OpenCell records. LRCH baits recover DOCK7 in the U2OS graph; endogenous-tagged DOCK7 is the bait in OpenCell. Complete accession groups and all incident context are retained. The selected subset corresponds to the four imported assertions, not an exhaustive list of DOCK7 partners. Curated IntAct records separately support the older Hippo map and BioPlex pairs; sequence verification of a curated participant does not prove the product used in every experiment.

## Access and provenance

| PMID | Normal publication cache | Actual independent read scope |
|---|---|---|
| 16982419 | Abstract only | Complete abstract; bounded original attempts unsuccessful. |
| 18850735 | Abstract only | Separately recovered genuine PMC original Methods/Results. |
| 21423176 | Full text | Original preparation/MS Methods and relevant Results; no target-resolved supplementary row. Download/challenge payloads were not treated as source text. |
| 22158624 | Full text | Relevant human/rat assay Methods and Results. |
| 23553822 | Full text | Mouse physiology Methods/Results and tissue-context interpretation. |
| 24255178 | Abstract only | Complete abstract and literal target interaction records; no full-original claim. |
| 27812135 | Full text | Positive and negative target-assay Results and Methods. |
| 29187380 | Abstract only | Separately recovered genuine author PDF, relevant Methods/Results. |
| 29467281 | Full text | Target co-IP, septin, construct and Methods passages independently read. |
| 32203420 | Abstract only | Separately recovered author-hosted original and genuine publisher supplementary tables. |
| 33961781 | Full text | Platform/context passages and six matching curated interaction records; not a claim to have reread every Methods paragraph. |
| 35271311 | Full text | Endogenous-tag platform/limitations plus original target CSV records. |
| 40205054 | Full text | U2OS AP-MS Methods/quality controls and target graph edges. |
| 22842144 | Full text | Mouse cortical perturbation/rescue and human localization passages. |
| 23718289 | Full text | Operative biochemical Methods, Results, captions and Discussion. |
| 22634526 | Abstract only | Complete fly Zir abstract and experimental donor records; no full-assay claim. |

Existing cache bytes and flags are preserved. Separately recovered originals supply additional evidence without pretending that abstract caches contain it. Official product, source and assay identities are preserved even when the reviewed interpretation is narrower. The optional PTHR23317 lookup files are excluded from this publication because another pending gene review already owns their addition; the actual tree, MSA and IBD evidence was independently reconstructed and retained for verification.

## Ontology and curation boundaries

Current [GO:0035025](https://www.ebi.ac.uk/QuickGO/term/GO:0035025) captures the activating direction and descends from the original Rho-regulation term. For the broader GO:0007264 source row, this is a target-supported role correction rather than a claimed strict descendant. The term preserves coverage of RAC1 and conditionally tested CDC42. [GO:0005102](https://www.ebi.ac.uk/QuickGO/term/GO:0005102) describes signaling-receptor binding without requiring receptor agonism; [GO:0031106](https://www.ebi.ac.uk/QuickGO/term/GO:0031106) covers control of septin-ring organization, separating the measured redistribution from an unproven catalytic explanation. [GO:0005096](https://www.ebi.ac.uk/QuickGO/term/GO:0005096) requires GTP hydrolysis stimulation, which nucleotide exchange alone cannot establish. The TACC3 unit has no guessed molecular-function term. No NEW process is proposed, and the refined axon/axonogenesis terms do not create extra source assertions.

The actual PAINT lineage places the target below PTN000593987 for GEF/Rho regulation and PTN002762137 for axonogenesis. The latter uses target experimental evidence legitimately. Fly Zir is the regulatory donor; its immune-cell context is not transferred to human DOCK7. The [project's explicit generic-binding policy](https://github.com/ai4curation/ai-gene-review/blob/27a4b4df4e8c3ade89b00ce91b1cb144d8ad3c8a/projects/CLINGEN_MENDELIAN.md#curation-instructions) retains supported associations as non-core when a finer activity is not established. Advisory warnings do not require removing positive observations.

The categorical CDC42 exclusion in the curated UniProt FUNCTION summary should be qualified against the historical human-fragment, prenylated-substrate and membrane conditions of PMID:23718289. Positive exchange in that assay is not a universal claim about current products or endogenous cell contexts. Open questions concern the separate GAP assertion, endogenous context of CDC42 exchange, the molecular TACC3 mechanism, natural-product differences and endogenous septin dependence. The proposed experiments address those gaps without claiming that unresolved mechanisms were measured.
