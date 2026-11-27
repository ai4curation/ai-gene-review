# DOK7 source and assay guide

The review preserves 16 imported source assertions and four official products. Their actions are four ACCEPT, five KEEP_AS_NON_CORE and seven MODIFY. One additional proposed molecular-function annotation uses ISS evidence from the mouse ortholog. This guide distinguishes underlying observations from their interpretation.

| Source | Actual access and decisive scope | Limits |
|---|---|---|
| [PMID:20603078](https://pmc.ncbi.nlm.nih.gov/articles/PMC2917201/) | Genuine full XML cache; Results on PH–PTB/MUSK binding, dimerization and kinase stimulation; Experimental Procedures for protein purification, crystallography, lipid binding and kinase assay. | Human PH–PTB 1–220 supplies solution binding/oligomerization; mouse PH–PTB supplies the ligand-bound structure, lipid and direct kinase assays; MUSK 529–868 is rat. Mouse full-length Dok7 is used in NIH3T3. |
| [PMID:16794080](https://pubmed.ncbi.nlm.nih.gov/16794080/) | Verified complete abstract; exact mouse GO annotations provide additional curator-grounded process/location assertions. | Publisher retrieval failed. Detailed full Methods and source-specific donor assays were not independently recovered. |
| [PMID:21041412](https://pmc.ncbi.nlm.nih.gov/articles/PMC2964755/) | Full PMC original separately recovered; Figures 1–5, Discussion and Methods on DNA constructs, cell culture, affinity purification, biochemical analyses and MS. | Normal cache remains abstract-only. Murine BAE96740 was cloned from C2 cells; peptide pull-down is from lysate. Rac/Rho GEF linkage is proposed in Discussion. |
| [PMID:32296183](https://pubmed.ncbi.nlm.nih.gov/32296183/) | Protected full main cache, Generation and characterization of HuRI; IntAct pair records listed below. | General orthogonal-assay performance is not claimed as individual-pair validation or a native DOK7–EFEMP2 function. |
| [HPA DOK7](https://www.proteinatlas.org/ENSG00000175920-DOK7/subcellular) | Official [target XML](https://www.proteinatlas.org/ENSG00000175920.xml), ICC/IF summary and HPA059449/HPA062780 subassays. | Actual annotations were read; image pixels were not independently scored. No natural product identity is assigned. |
| [UniProt Q18PE1](https://www.uniprot.org/uniprotkb/Q18PE1/entry) | Official sequence, alternative products, PH/PTB and alternative-sequence features; all four official FASTAs independently reconstructed. | By-similarity evidence remains labeled. Retaining a domain does not prove functional equivalence. |
| [Mouse Q18PE0](https://www.uniprot.org/uniprotkb/Q18PE0/entry) | Complete current QuickGO response, 36 of 36 records; literal donor identity and primary source attribution. | Orthology is not a direct human assay. The original imported identifiers remain unchanged. |
| [InterPro IPR037746](https://www.ebi.ac.uk/interpro/entry/InterPro/IPR037746/) | Protein Dok-7 family, target match at residues 1–495, kinase-binding/kinase-regulation mappings. | The current ARBA00028598 rule emits kinase binding but its historical triggering condition was not reconstructed. |

## Binary interaction record

The exact EFEMP2–DOK7 pair is in [IntAct EBI-24557174](https://www.ebi.ac.uk/intact/interaction/EBI-24557174), EBI-23490963 and EBI-25046471, under PMID:32296183 and IM-25472. Methods are validated two-hybrid, two-hybrid array and prey pooling. Both interactors are human; the assay host is yeast. The ROGIDs are `L8jMp8rFYb6DRRusfWgyd9zN2KI9606` for EFEMP2 and `RNSUGsyQVitqfrm+mTmzf0fZHR49606` for DOK7, matching the canonical official sequences. These records preserve a positive binary result without assigning a specific physiological function.

## Inherited assertions and specificity

[PANTHER PTHR21636](https://www.pantherdb.org/panther/family.do?clsAccession=PTHR21636) places human leaf PTN002502548 below PTN001092033. The actual PAINT IBD records for GO:0007528 and GO:0019901 were joined to that node, rather than treating a short donor list as weak evidence. The saved IBD source is dated 2026-08-28 for development and 2020-04-21 for binding. It includes mouse development evidence and mouse plus human binding evidence. The imported development assertion also lists zebrafish; this dated-list difference does not justify altering its source fields.

Receptor tyrosine kinase binding GO:0030971 is a verified descendant of protein kinase binding. GO:0005068 adds coordinated receptor/adaptor recruitment and is supported independently by the tail experiments. GO:0030296 describes activation of kinase activity; DOK7 does not supply kinase catalysis. GO:0007169 is the current cell-surface receptor tyrosine-kinase signaling term. Postsynaptic membrane GO:0045211 is a typed descendant of both plasma membrane and synapse. Neuromuscular junction is retained as the broader anatomical setting; no presynaptic DOK7 localization is inferred.

## Supporting clinical and sequence references

PMIDs [16917026](https://pubmed.ncbi.nlm.nih.gov/16917026/), [17439981](https://pubmed.ncbi.nlm.nih.gov/17439981/), [19261599](https://pubmed.ncbi.nlm.nih.gov/19261599/), [20012313](https://pubmed.ncbi.nlm.nih.gov/20012313/) and [22661499](https://pubmed.ncbi.nlm.nih.gov/22661499/) were verified and read at abstract level. They support human synaptopathy, variable severity and reported variant assays; detailed constructs or Methods are not invented. PMIDs 14702039, 15489334 and 15815621 are sequence-resource context, assessed through their abstracts and official UniProt provenance. Available full caches were not treated as fully read simply because their metadata says full text.

The only newly reproduced publication excerpts are in the review YAML: eight words from PMID:32296183, nine from PMID:20603078 and eight from PMID:21041412, each used once. Reference-only support elsewhere reuses the same underlying evidence without repeating quotation text.


## Review follow-up

The review proposes GO:0030296 protein tyrosine kinase activator activity by ISS from the verified mouse ortholog Q18PE0. The direct activation assay and the human binding/oligomerization experiments retain their distinct construct species. This adds the annotation recommendation already represented by the first core function; it does not claim direct human kinase-rate measurements or equal activity for all four products. The 16 imported assertions and their source fields remain unchanged.
