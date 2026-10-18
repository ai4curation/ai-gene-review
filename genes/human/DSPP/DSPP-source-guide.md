---
title: DSPP source and assay guide
gene: DSPP
annotation_scope:
  imported_annotations: 15
  new_annotations: 0
---

# DSPP source and assay guide

This guide identifies the experimental source behind each biological context. Repository cache flags describe stored content; separately accessible original sections and their limits are recorded below. No figure-pixel inspection is claimed for these sources.

| Source | Actual original access and experimental boundary |
|---|---|
| [8995371](https://pubmed.ncbi.nlm.nih.gov/8995371/) — [author original](https://www.researchgate.net/publication/14213696_Dentin_Phosphoprotein_and_Dentin_Sialoprotein_are_Products_Expressed_from_a_Single_Transcript_Coded_by_a_Gene_on_Human-Chromosome-4-Dentin_Phosphoprotein_DNA-Sequence_Determination) | Original Methods, Results, Discussion and captions read. Mouse full cDNA, rat sequence correction and partial human chromosome-mapping probe have different roles. Normal cache: abstract only. |
| [9879917](https://pubmed.ncbi.nlm.nih.gov/9879917/) — [publisher](https://onlinelibrary.wiley.com/doi/10.1046/j.0909-8836..t01-9-.x) | Authentic abstract and indexed original pages 1043/1044/1046, including human molar cloning context. Complete original unavailable; no new direct human binding experiment claimed. Normal cache: abstract only. |
| [16046405](https://pubmed.ncbi.nlm.nih.gov/16046405/) — [author original](https://www.researchgate.net/publication/7700082_Phosphorylation_of_Phosphoryn_Is_Crucial_for_Its_Function_as_a_Mediator_of_Biomineralization) | Operative Methods/Results/Discussion and captions read. Rat native phosphophoryn versus a shorter rat recombinant C-terminal fragment, with calcium, collagen and mineral assays. Normal cache: abstract only. |
| [40640300](https://pmc.ncbi.nlm.nih.gov/articles/PMC12246090/) | Full normal XML; mouse genotype comparisons, histology, matrix/mineral Results and Methods read. The DPP truncation and null resolve later-stage contributions; no supplement or isolated human-product assay claimed. |
| [22615197](https://pmc.ncbi.nlm.nih.gov/articles/PMC3820500/) | Full normal XML; native rat incisor DPP isolation, radiolabeled substrate adsorption and adhesion controls read. Collagen association is directly measured. |
| [11856645](https://pubmed.ncbi.nlm.nih.gov/11856645/) | Complete authentic human-tooth abstract. Full intracellular localization panel and detailed antibody Methods unavailable. Other proteins in the same abstract are not treated as DSPP evidence. |
| [19001636](https://pmc.ncbi.nlm.nih.gov/articles/PMC2664930/) | Indexed original mouse Methods, antisera/controls, Figure 8/9 captions and Discussion read. Normal cache: abstract only. |
| [23525114](https://pmc.ncbi.nlm.nih.gov/articles/PMC3642346/) | Indexed original rat RUB1 localization Results and Figure 5/6 captions/controls read. Normal cache: abstract only. |
| [15763925](https://pmc.ncbi.nlm.nih.gov/articles/PMC2020511/) | Full normal XML; rat M2H4 expression/mineralization and TGFbeta/BMP4 treatment Methods and Results read. This is expression-marker evidence, not a DSPP perturbation. |
| [24502800](https://pubmed.ncbi.nlm.nih.gov/24502800/) | Complete authentic abstract for the rat IEP donor context; no full original or unseen direct perturbation claimed. |
| [25027178](https://pmc.ncbi.nlm.nih.gov/articles/PMC4235594/) | Selected indexed original mouse WT/null Methods, operative lineage-marker Results and Discussion read. Normal cache: abstract only. |
| [22134916](https://pmc.ncbi.nlm.nih.gov/articles/PMC3285302/) — [author original](https://www.researchgate.net/publication/51847217_Dentin_Phosphoprotein_DPP_Activates_Integrin-mediated_Anchorage-dependent_Signals_in_Undifferentiated_Mesenchymal_Cells) | Selected original Methods/Results and captions: mouse C3H10T1/2 and primary mouse pulp cells, recombinant DPP substrate, integrin/FAK/ERK controls and differentiation endpoints. Exact reagent sequence/species unresolved. Normal cache: abstract only. |
| [15308669](https://pubmed.ncbi.nlm.nih.gov/15308669/) — [publisher](https://doi.org/10.1074/jbc.M405031200) | Authentic abstract and selected original promoter-study Methods. Complete paper unavailable; exact attribution of the donor protein-to-process annotation remains unresolved. |
| [36399478](https://pmc.ncbi.nlm.nih.gov/articles/PMC9825471/) | Existing full XML; resource Methods, matrix classes and aggregate coverage Results. No DSPP-specific mass-spectrometry row independently verified. |

## Checkable identity and propagation

The [official human sequence and features](https://rest.uniprot.org/uniprotkb/Q9NZW4.json) distinguish the 1301-residue primary sequence from the signal peptide and processed chains. The [PTHR47819 topology](https://www.pantherdb.org/services/oai/pantherdb/treeinfo?family=PTHR47819&format=json), [family alignment](https://www.pantherdb.org/services/oai/pantherdb/familymsa?family=PTHR47819) and [PAINT IBD file](https://data.pantherdb.org/ftp/downloads/paint/current/IBD.gaf) provide the literal lineage evidence. Select human leaf PTN000789080 and its ancestor PTN002936180, then the five IBD records for GO:0005518, GO:0005634, GO:0005737, GO:0071895 and GO:0097187. The human path has eight nodes including the root and leaf; it is not inferred from donor similarity alone.

Current donor annotations are queryable for [rat Q62598](https://www.ebi.ac.uk/QuickGO/services/annotation/search?geneProductId=UniProtKB:Q62598&limit=200) and [mouse P97399](https://www.ebi.ac.uk/QuickGO/services/annotation/search?geneProductId=UniProtKB:P97399&limit=200). The captured rat record has 49 rows and mouse 39. The annotation references differ by term; the rat marker and regulatory-source limitations are stated in the review. Live services may evolve after this review.

The target-resolved pathway chain is [reaction R-HSA-4086132](https://reactome.org/content/detail/R-HSA-4086132) → [extracellular DPP R-HSA-4086140](https://reactome.org/content/detail/R-HSA-4086140), with [integrin alphaVbeta1 R-HSA-216015](https://reactome.org/content/detail/R-HSA-216015) and [product complex R-HSA-4086137](https://reactome.org/content/detail/R-HSA-4086137). Nonhuman inferred entity coordinates are not substituted for experimentally authenticated rodent sequences. No target activity was present in the inspected GO-CAM index; that absence alone is not an annotation gap.

The more specific core location [GO:0140149](https://www.ebi.ac.uk/QuickGO/term/GO:0140149) is a cellular-component class. It is distinct from the molecular function [GO:0005201](https://www.ebi.ac.uk/QuickGO/term/GO:0005201). Calcium/collagen interactions are integrated in that matrix mechanism; contextual intracellular or developmental assertions do not each require a separate core.
