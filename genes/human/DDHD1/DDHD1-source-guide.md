# DDHD1 source guide

## Primary evidence and access

| Source | Evidence inspected | Limits |
| --- | --- | --- |
| [PMID:20359546](https://pubmed.ncbi.nlm.nih.gov/20359546/) | Abstract explicitly reporting recombinant DDHD1 PI hydrolysis, LPI production and PA-dependent activity | Publisher full text inaccessible; construct species and isoform details are not assumed |
| [PMID:22922100](https://pubmed.ncbi.nlm.nih.gov/22922100/) | Abstract explicitly including PA-PLA1/DDHD1 DDHD-domain experiments | DDHD2-focused title does not exclude DDHD1 experiments; residue requirements do not prove metal binding |
| [PMID:24599962](https://pmc.ncbi.nlm.nih.gov/articles/PMC4036285/) | Full original Methods and Results: human FLAG-PA-PLA1, S537A, two HeLa siRNAs, rescue and CCCP fragmentation assays | Cell-type dependence, unchanged bulk mitochondrial PA/LPA, and mouse sperm observations remain distinct |
| [PMID:23176821](https://pmc.ncbi.nlm.nih.gov/articles/PMC3516610/) | Recovered original: DDHD1 cytosolic expression and SPG28 lymphoblast bioenergetics | Initial review cache was abstract-only; merged main now includes full text. Fibroblast/network images concern CYP2U1/SPG49, with SPG28 fibroblasts unavailable |
| [PMID:37189713](https://pubmed.ncbi.nlm.nih.gov/37189713/) | Full original lipid-profile results and limitations | Mouse plasma and one human serum comparison do not establish general diagnostic performance or substrate kinetics |
| [PMID:17428803](https://www.researchgate.net/publication/6399283_Mammalian_Sec16p250_Plays_a_Role_in_Membrane_Traffic_from_the_Endoplasmic_Reticulum) | Indexed original Methods, Results and Figure 7; official p125 identity checked | Direct publisher requests failed; immutable cache is abstract-only. The assayed p125 target is SEC23IP |
| [PMID:15623529](https://www.researchgate.net/publication/8106467_p125_Is_Localized_in_Endoplasmic_Reticulum_Exit_Sites_and_Involved_in_Their_Organization) | Indexed original human PA-PLA1 construct Methods and Figure 5B | Tagged 872-aa protein in Vero cells; length alone does not identify a current isoform. Cache remains abstract-only |
| [PMID:32296183](https://pubmed.ncbi.nlm.nih.gov/32296183/) | Full original study-design/retesting passages and six exact IntAct HuRI records | Three assay stages per pair are not three independent physiological studies; individual orthogonal validation is not inferred |
| [PMID:30085123](https://pmc.ncbi.nlm.nih.gov/articles/PMC6212772/) | Human ZBTB24 ChIP, purified-domain EMSA, expression perturbation and rescue | Establishes the partner's DNA-binding transcription-factor class, not DDHD1 transcriptional activity |

## Annotation and product interpretation

The current PTHR23509 tree places DDHD1 leaf PTN002512372 below IBD root PTN000397232. The saved IBD records contain the phospholipase and cytoplasm assertions and their experimental descendant sources. The ancestral judgment is retained; no objection is based on donor count or a donor's own propagated annotation. Target evidence supports the more informative A1 and cytosol terms.

The two HuRI partner pairs are ZBTB24/O43167–Q8NEL9-2 and CR1L/Q2VPA4–Q8NEL9-2. Both partners and the 872-aa DDHD1 product match the recorded sequence/taxon ROGIDs. Records cover pooled, array and validated two-hybrid stages in yeast. GO:0140297 specifies the established ZBTB24 partner class. CR1L's predicted signal peptide and mammalian processing constrain physiological interpretation, and the receptor-like name does not establish the signaling function required by GO:0005102.

[Reactome R-HSA-6786650](https://reactome.org/content/detail/R-HSA-6786650) connects through [catalyst 6786648](https://reactome.org/ContentService/data/query/6786648) and [grouping 6786649](https://reactome.org/ContentService/data/query/6786649) to [human DDHD1 entity 6786636](https://reactome.org/ContentService/data/query/6786636), Q8NEL9 residues 1–900, explicitly in cytosol. The source represents the DDHD1/2 grouping as a Complex. That data-model class is not used to assert a physiological complex core.

The official isoform changes are preserved: Q8NEL9-2 replaces canonical residues 813–841 with L; Q8NEL9-3 additionally lacks residues 1–418; Q8NEL9-4 additionally replaces D337 with DGSGINYS. Neither retention of an active-site region nor similar length establishes the activity of a shortened or altered product. Historical constructs are not assigned to current isoforms without sequence qualification.

The core uses GO:0008970 with GO:0046488. GO:0036149 describes sequential phosphatidylinositol deacylation/re-acylation and is not justified by PI hydrolysis alone. No NEW process or molecular-function annotation is added. IPR004177 describes a possible metal-binding site; target-specific metal identity, occupancy and stoichiometry remain unresolved.

## Provenance

The source baseline is main `1f2d0f4c42bde7e51deeed7d0486ef015657404b`. All original source fields and normal caches are preserved. Six pre-existing main publication caches were protected; independently fetched variants were archived separately before fixing the source boundary. The pending DARS2 branch shares PMID23186163; its bytes were not adopted. After the CYP2U1 merge at main `e32937e9a43d197137f795d76417027d318843f0`, the newly present full-text PMID23176821 cache was qualified and preserved. Its original abstract-only review snapshot remains archived. The normal provider attempt and its fallback both failed, so no provider-labelled report exists. Source recovery and read scopes were recorded separately from the immutable cache flags.

The review follows the user's [CLINGEN_MENDELIAN curation instructions](https://github.com/ai4curation/ai-gene-review/blob/1f2d0f4c42bde7e51deeed7d0486ef015657404b/projects/CLINGEN_MENDELIAN.md#curation-instructions). This is project policy, not a claim of repository-wide policy or human scientific sign-off.

## Tissue, disease and oligomerization context

The [human UniProt Q8NEL9 record](https://www.uniprot.org/uniprotkb/Q8NEL9/entry), also preserved in [the local source record](DDHD1-uniprot.txt), contains the tissue-specificity, SPG28 disease and experimental subunit annotations. The SUBUNIT statement attributes homooligomerization and weaker DDHD2 association to PMID:22922100. These are curated statements; the oligomerization Methods, product assignments, stoichiometry and physiological role were not independently recovered from the abstract-only cache. They are documented in the notes and an expert question without proposing a new GO annotation.

The full PMID:23176821 Results on SPG28/DDHD1 identify truncating/splice variants in recessive disease families, and the Discussion describes expression in human brain and testis. The separate CYP2U1 experiments remain distinct. UniProt’s testis-rich expression statement is retained as human-record curation; the PMID:9488669 abstract alone does not resolve all tissue-panel species.

The two corrected COPII source assertions are anchored in the original experimental Methods/Results, with identity cross-checks in the cached abstracts and [PTHR23509 member table](../../../interpro/panther/PTHR23509/PTHR23509-entries.csv): SEC23IP/Q9Y6Y8 belongs to SF4, whereas DDHD1/Q8NEL9 belongs to SF32. Abstract prominence or PANTHER membership alone would not justify overruling an experimental annotation. Cytosol denotes the observed protein pool; transient action at membrane interfaces remains compatible with the mitochondrial-surface phosphatidate model and is not a newly demonstrated localization mechanism.
