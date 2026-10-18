---
gene: EDAR
annotation_scope:
  imported_annotations: 23
  reviewed_annotations: 23
  new_annotations: 0
  retired_source_contexts: 0
---

# EDAR evidence and source access guide

This guide locates the evidence and distinguishes actual reading from cache availability. It is not an independent study. All 23 source identities and all existing cache bytes are preserved. A source-specific REMOVE is a curation judgment; the retracted source row has not been erased or marked as a retired export context.

## Primary studies and access

| Source | Effective cache | Actual evidence and limits |
| --- | --- | --- |
| [PMID:10431241](https://pubmed.ncbi.nlm.nih.gov/10431241/) | Added, abstract only | Selected author-uploaded original cloning, genetics, predicted topology and Discussion. The EDAR–EDA ligand relationship was explicitly a hypothesis in this 1999 study; later experiments establish it. No figure pixels inspected. |
| [PMID:11035039](https://pubmed.ncbi.nlm.nih.gov/11035039/) | Added, abstract only | Selected original Methods, ligand-binding Results/captions, NF-kappaB experiments and TRAF/NIK association examined separately. Secreted Myc-EDA-A1 and soluble EDAR-Fc were tested in conditioned media with controls, not as a homogeneous purified pair. Cell-based association does not establish direct contact with each signaling adaptor. |
| [PMID:11039935](https://pubmed.ncbi.nlm.nih.gov/11039935/) | Added, abstract only | Complete positive abstract identifies EDA-A1 binding EDAR and EDA-A2 binding EDA2R. Full original recovery failed; unseen construct and organ-culture details are not asserted. |
| [PMID:12270937](https://pubmed.ncbi.nlm.nih.gov/12270937/) | Existing, abstract only | Selected indexed original Introduction, Methods and Results. The Introduction explicitly states prior EDAR disease and ligand findings; new XEDAR assays are kept separate from the EDAR TAS annotation. |
| [PMID:27144394](https://pubmed.ncbi.nlm.nih.gov/27144394/) | Added, full text; retracted | Relevant human constructs, co-IP Methods, binding Results and Fig. 1C caption examined. The later notice questions this same binding panel; the reference is invalidated and the source-specific assertion removed. Independent EDA–EDAR evidence remains positive. |
| [PMID:32822567](https://pubmed.ncbi.nlm.nih.gov/32822567/) | Existing, full text | Human extracellular library, fusion-protein production and controlled retest Methods; actual Data S1, S4 and S5 workbooks. Both EDAR pairs appear in both orientations with triplicate data. No EDAR SPR record was found. Native signaling and physiological contact are not established by this screen. |
| [PMID:42308199](https://pubmed.ncbi.nlm.nih.gov/42308199/) | Added, abstract only | Complete official notice independently recovered and read. It explicitly questions Fig. 1C of PMID:27144394 and retracts the results/conclusions after unresolved concerns. The abstract-only cache flag is unchanged. |
| [PMID:12629675](https://pubmed.ncbi.nlm.nih.gov/12629675/) | Added, abstract only | Complete abstract describes mouse salivary-gland localization and developmental perturbations. Current MGI donor IDAs retain plasma-membrane and apical-part annotations. Detailed microscopy Methods/images were not recovered; positive curator evidence is not treated as a donor error. |
| [PMID:19619491](https://pubmed.ncbi.nlm.nih.gov/19619491/) | Existing, flagged full text | Actual cached content contains Introduction and Discussion but omits detailed Results and Methods. Current mouse donor IMP evidence is traced independently. The stored flag and bytes are preserved; no unseen quantitative experiment is claimed. |

The separately accessed [PMID:10431241 original](https://www.researchgate.net/publication/12868994_Monreal_AW_Ferguson_BM_Headon_DJ_Street_SL_Overbeek_PA_Zonana_JMutations_in_the_human_homologue_of_mouse_dl_cause_autosomal_recessive_and_dominant_hypohidrotic_ectodermal_dysplasia_Nat_Genet_22366-369) supplies the human cloning/genetic context and the explicit prospective ligand hypothesis. The [PMID:11035039 original](https://www.researchgate.net/publication/12289454_The_Ectodermal_Dysplasia_Receptor_Activates_the_Nuclear_Factor-_B_JNK_and_Cell_Death_Pathways_and_Binds_to_Ectodysplasin_A) supplies the selected ligand and signaling experiments. Its original construct coordinates are not silently equated to the deposited IntAct feature ranges or both complete natural products.

The [PMID:12270937 original](https://www.researchgate.net/publication/11139555_Role_of_TRAF3_and_-6_in_the_Activation_of_the_NF-kB_and_JNK_Pathways_by_X-linked_Ectodermal_Dysplasia_Receptor) distinguishes the EDAR background statements from new XEDAR experiments. The [complete retraction notice](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0351787) identifies Fig. 1C concerns and the editorial decision; its [machine-readable XML](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13274892/fullTextXML) contains the same notice. No replacement identifier is substituted for PMID:27144394.

For PMID:32822567, the [original main article](https://pmc.ncbi.nlm.nih.gov/articles/PMC7440162/) and publisher [Data S1](https://ars.els-cdn.com/content/image/1-s2.0-S0092867420309338-mmc1.xlsx), [Data S4](https://ars.els-cdn.com/content/image/1-s2.0-S0092867420309338-mmc4.xlsx) and [Data S5](https://ars.els-cdn.com/content/image/1-s2.0-S0092867420309338-mmc5.xlsx) are the operative screen sources. The portable audit includes exact saved workbooks and checksums; future downloads must match before replay.

## Reproducible source interpretation

The [source audit](EDAR-bioinformatics/source-audit/RESULTS.md) derives four EDAR incident screen records representing two pairs, three exact human library-sequence matches, five selected IntAct source records from 57 total, the three literal PTHR12120 IBDs, matching electronic-rule conditions and four Reactome paths to EDAR. A positive binding class does not transfer a partner's catalytic or signaling activity to EDAR.

[EDA Q92838](https://www.uniprot.org/uniprotkb/Q92838/entry) is an independently established cytokine; [LILRB1 Q8NHL6](https://www.uniprot.org/uniprotkb/Q8NHL6/entry) is an independently established inhibitory signaling receptor. [GO:0019955](https://www.ebi.ac.uk/QuickGO/term/GO:0019955) and [GO:0005102](https://www.ebi.ac.uk/QuickGO/term/GO:0005102) describe binding to those partner classes. The latter term does not require receptor agonism. [GO:0004896](https://www.ebi.ac.uk/QuickGO/term/GO:0004896) captures EDAR's cytokine-receptor function; [GO:0005031](https://www.ebi.ac.uk/QuickGO/term/GO:0005031) specifically names tumor necrosis factor, so TNFR-family membership alone is insufficient.

The exact EDAR sequence and target path were checked in the 125-node PTHR12120 tree and MSA. The root IBDs for receptor activity and cytokine signaling, and the descendant IBD for plasma membrane, all lie on that path. The human target appearing among its own descendant sources is legitimate experimental grounding. Current [mouse Edar Q9R187](https://www.uniprot.org/uniprotkb/Q9R187/entry) and [human EDA2R Q9HAV5](https://www.uniprot.org/uniprotkb/Q9HAV5/entry) donor annotations were inspected separately; their distinct ligand specificity is preserved.

[ARBA00027254](https://www.uniprot.org/arba/ARBA00027254), [ARBA00028236](https://www.uniprot.org/arba/ARBA00028236) and [ARBA00084990](https://www.uniprot.org/arba/ARBA00084990) have explicit condition sets matching the official EDAR FunFam. The epidermis rule also specifies Chordata. The current [IPR047526](https://www.ebi.ac.uk/interpro/entry/InterPro/IPR047526/) family mappings are distinguished from EDAR-specific experimental corroboration.

[Reactome R-HSA-5669012](https://reactome.org/content/detail/R-HSA-5669012) and [R-HSA-5675656](https://reactome.org/content/detail/R-HSA-5675656) both reach [EDAR entity R-HSA-5669001](https://reactome.org/content/detail/R-HSA-5669001), Q9UNE0 residues 27–448 at the plasma membrane. EDARADD's cytosolic location is not transferred to the receptor. These curated models do not establish equivalent activity of the two complete natural EDAR products.

The [official EDAR record](https://www.uniprot.org/uniprotkb/Q9UNE0/entry) supplies two products, 448 and 480 residues. The longer product replaces Ala219 with a 33-residue cytoplasmic segment. The selected extracellular fragments are shared-region reagents; they do not establish equivalent full-product signaling. Signal-peptide cleavage is processing, not a third splice isoform.
