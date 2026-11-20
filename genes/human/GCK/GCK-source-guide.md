# GCK source and context guide

## Biological scope

The review centers on glucose phosphorylation and its coupling to insulin secretion and glucose homeostasis. Alternative-sugar assays remain positive evidence, while their physiological contribution is unresolved. The three official amino-terminal products are retained; translation efficiency does not establish catalytic inactivity. Individual experimental constructs are not assigned to a natural product without source support.

## Source access

Reference assessments distinguish authentic abstract evidence from selected original text. The table below identifies the original sources used beyond the normal caches. An abstract-only cache is not described as full text. The original genuine native import contains 74 source paths. The follow-up adds one independently qualified, unchanged main-cache record (PMID:12931191), for 75 current sources. Newly available functional full text was inspected before transfer; source-specific access limits remain explicit.

| Reference | Inspected source and locator | Access limit |
| --- | --- | --- |
| PMID:7742312 | [PubMed abstract](https://pubmed.ncbi.nlm.nih.gov/7742312/) and [UniProt record](GCK-uniprot.txt), BIOPHYSICOCHEMICAL PROPERTIES / CATALYTIC ACTIVITY | Original tables were not accessed. The separately inspected curated record provides explicitly attributed numerical kinetics, summarized below. |
| PMID:11522786 | [Original reprint](https://www.researchgate.net/publication/232315692_Characterization_of_Glucokinase-binding_Protein_Epitopes_by_a_Phage-displayed_Peptide_Library), Methods p43916, Results p43917–19, captions 2/3/8 | Text and captions read; no figure-pixel analysis. Human GCK target and rat partner constructs remain distinct. |
| PMID:8132752 | [JCI original](https://www.jci.org/articles/view/117064), Methods and glucose–secretion Results | Selected original text, not every endpoint or raw trace. |
| PMID:8878425 | [JCI original](https://www.jci.org/articles/view/118974), Methods and hepatic-glycogen Results | Relative pathway fractions are not absolute gluconeogenic-flux measurements. |
| PMID:16173921 | [Original article](https://doi.org/10.1042/BJ20051137), selected Methods/Results | Purified islet GST-GCK kinetics and stability were distinguished; engineered variants are not natural products. |
| PMID:12931191 | [PubMed abstract](https://pubmed.ncbi.nlm.nih.gov/12931191/) and unchanged normal cache | Mouse BAD-containing GCK mitochondrial complex; original full text was not recovered. No direct human topology or GCK–VDAC assay is inferred. |
| PMID:16542652 | [Publisher original](https://febs.onlinelibrary.wiley.com/doi/10.1016/j.febslet.2006.03.009), Methods 2.1–2.4, Results 3.1–3.4, Discussion 4 | Rat fractionation is positive localization evidence with stated activity and topology limits; no figure-pixel reassessment. |
| PMID:10456334 | [PubMed abstract](https://pubmed.ncbi.nlm.nih.gov/10456334/) | Full publisher text unavailable. Recipient cell species is not construct species. |
| PMID:24187134 | [PMC original](https://pmc.ncbi.nlm.nih.gov/articles/PMC3861633/), Methods and Results, especially localization and purified-ULD experiments | Selected text; no supplement or image analysis. Cellular and purified-enzyme inhibition differ. |
| PMID:12086933 | [PubMed abstract](https://pubmed.ncbi.nlm.nih.gov/12086933/) | Donor neuronal experiments; full inhibitor controls not inspected. |
| PMID:17470517 | [PubMed abstract](https://pubmed.ncbi.nlm.nih.gov/17470517/) and limited indexed Results | Complete leptin-specific GT1-7 evidence remains unresolved; slice nonsignificance is not a whole-paper negative. |
| PMID:19884385 | [PMC original](https://pmc.ncbi.nlm.nih.gov/articles/PMC5419125/), kinetic Results, Discussion and mutagenesis/kinetic Methods | Human pancreatic GST-GCK constructs; secretion thresholds are modeled. No figure or raw-data reanalysis. |
| PMID:23957911 | [PMC original](https://pmc.ncbi.nlm.nih.gov/articles/PMC3859847/), selected structural/functional Methods and Results | Human pancreatic GCK and rat GKRP; no figure/supplement reading or new nuclear-localization assay. |
| PMID:18477811 | [Europe PMC original](https://europepmc.org/article/MED/18477811), Methods, Results and Figures 6–7 captions | Gck and Sox4 perturbations are distinct; figure images and supplements uninspected. |

Five records (PMID:11372010, PMID:16965331, PMID:20375417, PMID:21604084 and PMID:9435328) have verified bibliographic identities but no inspected abstract or original. Their assessments remain UNVERIFIED for scientific content. Other abstract-based reference notes explicitly limit their scope.

## Sugar kinetics and annotation scope

The native [UniProt P35557 record](GCK-uniprot.txt), BIOPHYSICOCHEMICAL PROPERTIES, attributes the following values to PMID:7742312. Values for these three sugars were reported at 30 °C and pH 7.5. The final column is calculated from the reported values; it is not a cellular flux measurement or a replacement for GCK’s cooperative glucose-response curve.

| Substrate | Km (mM) | kcat (s−1) | Approximate kcat/Km (mM−1 s−1) |
| --- | ---: | ---: | ---: |
| Glucose | 6.03 | 66.4 | 11.0 |
| Mannose | 4.35 | 56.4 | 13.0 |
| Fructose | 240 | 116.9 | 0.49 |

Mannose phosphorylation is substantial; fructose phosphorylation is also real. Their physiological contribution by human GCK remains unresolved. The record’s reaction-direction annotation does not quantify that contribution, so measured sugar specificity alone is not presented as a complete explanation of cellular substrate use. No human physiological fructose concentration or same-reaction comparison with KHK is inferred.

GO:0004340 glucokinase activity is an actual is_a child of GO:0004396 hexokinase activity. The generic parent is therefore true and entailed by the accepted glucose reaction; it does not require activity on every member of the D-hexose class. Its TOO_GENERAL judgment neither rejects the experimental evidence nor deletes the measured substrate range. In contrast, glucose homeostasis adds an informative systemic regulatory scope to the catalytic step. The glucose-sensor annotation remains core and explicitly described in the same mechanistic core: binding and catalytic conformational response couple glucose concentration to downstream physiology, rather than constituting an unrelated second enzyme function.

The current QuickGO name for GO:0006096 is glycolysis, with glycolytic process as an exact synonym. Both authored locations use the latter spelling to match the validated ontology snapshot; incoming GOA labels remain unchanged.

## Interactions, products and phylogeny

The retained [HuRI study](https://pubmed.ncbi.nlm.nih.gov/32296183/) contains P35557-1/ORF3689 pairs with A6NLX3/ORF70835 and A0A0C4DFN2/ORF54784. A retained gene-level crosswalk links the latter to GCKR/Q14397; full clone-to-modern-product equivalence is not established. The six literal assay records are preserved separately from biological interpretations.

Actual PTHR19443 tree/MIA/FASTA records place human GCK at AN118/PTN002500356. Ten current IBA contexts match their IBD assertions and donor sets at AN0, AN2 or AN108. The target's appearance as its own descendant evidence is legitimate. The 24 family negative records fall outside the target lineage. The target alignment matches the canonical 465-residue sequence; this does not identify study constructs. The mitochondrial-side IBA at AN2 remains non-core. Its term includes peripheral association and does not prescribe an HK1/HK2 binding-peptide mechanism. GCK’s amino terminus differs, but the assertion spans the single-domain plant donor as well as HK2; this is not a direct HK2-to-GCK similarity transfer. The plant donor itself has a hydrophobic amino terminus, so size alone does not settle the mechanism. Mouse BAD-dependent mitochondrial-complex evidence is compatible with association, while neither its abstract nor the rat fractionation establishes direct human sidedness (PMID:12931191; PMID:16542652).

## Reactome roles

The normal [glucose-phosphorylation reaction](https://reactome.org/content/detail/R-HSA-70420) reaches GCK through catalyst set450097 and entity450094 (P35557, chain 1–465, cytosol). GCKR complex formation, import, dissociation and export preserve their distinct roles. In [beta-cell gene regulation](https://reactome.org/content/detail/R-HSA-210745) and [FOXO repression](https://reactome.org/content/detail/R-HSA-9615017), GCK is a regulated output. Defective GCK or NPC events are assessed as disease context; they do not establish wild-type activity or transfer TPR disease biology to GCK.

## Conservation and native obligations

The evidence archive preserves all 86 original contexts, the 16-column export, forecast indices, three products, the literal raw 38 part_of GO:0009749 atom, and all 89 inherited annotations with 96 historical quote associations. The single atom projects to BFO:0000050; its original text and source remain unchanged. All 86 actual-native indices are reconciled, and the one flat extension is restored. Default validation passed without target advisories, strict GOA matched all 86 originals, and computed COMPLETE status retains one scientific UNDECIDED. Native codex EDIT history, private rendering, local links and authored whitespace checks passed; these describe the original native pass. The follow-up passed default validation without target advisories, strict matching of all 86 contexts, COMPLETE-status verification, new EDIT-history validation, private rendering, local links and scoped whitespace. Publication and integration remain separate. Historical observations and earlier judgments are explicitly distinguished from the current review.

Six current excerpts occur only in assessed-reference findings. The archive retains their source hashes, byte offsets and aggregate word budgets. All six now match genuine normal-cache bytes. Original retained-cache and article-scoped abstract locators remain archived; the two new-cache snippets differ only in line wrapping. All 74 original normal source paths have recorded native byte/hash/blob identities. The old notes prefix and existing history remain append-only.
