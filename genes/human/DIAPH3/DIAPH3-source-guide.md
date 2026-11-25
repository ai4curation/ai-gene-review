# DIAPH3 source and construct guide

Human DIAPH3 is UniProt [Q9NSV4](https://www.uniprot.org/uniprotkb/Q9NSV4/entry), HGNC:15480. Mouse Diaph3 is [Q9Z207](https://www.uniprot.org/uniprotkb/Q9Z207/entry), historically called mDia2. Mouse mDia3/Diaph2 is a different paralog. This distinction matters for the RhoD-specific study below.

## Two molecular functions

Actin binding and filament assembly form one integrated function. The [PMID:18755006 author manuscript](https://hdl.handle.net/10033/48543), Methods on DNA constructs and Results on filopodia induction, identifies a historical human 1110-residue construct assembled from BX649186 and BC048963. Its active deletion removes residues 1056–1110. Full-length protein is cytosolic in mouse B16-F1 cells; the active construct accumulates at filopodial tips, with human VA-13 cell corroboration. These are cellular experiments rather than purified current-human-product polymerization kinetics.

Microtubule binding is a separate function because it persists in actin-assembly-defective fragments. [PMID:18458159](https://pmc.ncbi.nlm.nih.gov/articles/PMC2364705/) reports controlled cosedimentation, saturable binding and protection from cold or dilution, including actin-defective and dimerization-impaired mutants. Its Methods identify historical Alberts/Wen construct provenance without explicitly resolving the template species. The current experimental donor annotation belongs to mouse Q9Z207; that curated assignment is distinguished from the unresolved exact historical fragment sequence. NIH3T3 host cells or a common construct provider do not establish template identity.

The author-uploaded original Methods for [PMID:16556604](https://doi.org/10.1074/jbc.M510923200) explicitly identify mouse mDia2. The separately inspected Methods for [PMID:15311282](https://doi.org/10.1038/ncb1160) describe residues 521–1040 but do not explicitly close the species link for the later experiment. Neither establishes equivalence to a current natural human splice product.

The full original [PMID:19457867](https://pmc.ncbi.nlm.nih.gov/articles/PMC2740432/), Results and Figure 1, independently localizes endogenous human protein at the HeLa cleavage furrow and central spindle. The engineered-fragment experiments are separate. The [Human Protein Atlas DIAPH3 page](https://www.proteinatlas.org/ENSG00000139734-DIAPH3/subcellular), inspected 17 October 2026, reports supported plasma-membrane and microtubule staining with HPA032151 in A-431, U-251MG and U2OS cells. That localization supports refining the broad microtubule-cytoskeleton annotation to microtubule; the imaging itself is not a binding assay.

## Source-specific location corrections

Three proposed removals concern the interpretation of specific donor evidence, rather than universal absence of a function or location.

| Imported location | Original evidence and interpretation |
| --- | --- |
| ESCRT-I complex, GO:0000813 | [PMID:33036023](https://pmc.ncbi.nlm.nih.gov/articles/PMC7819763/), Results on ESCRT components and Figure 5, places mouse mDia2 upstream of SRF-dependent Chmp5 expression and erythroid remodeling. It does not establish mDia2 as an ESCRT-I subunit. |
| Ribbon synapse, GO:0097470 | [PMID:23441200](https://pmc.ncbi.nlm.nih.gov/articles/PMC3575478/), ribbon-counting Results and immunostaining Methods, uses CtBP2/ribeye as the ribbon marker after mouse Diap3 overexpression. It does not label Diap3 at ribbons; the authors allow a secondary effect. |
| Stereocilia tip-link density, GO:1990427 | The same original uses phalloidin and scanning electron microscopy to assess actin cores and stereociliary morphology. Neither identifies Diap3 at the electron-dense plaque at a tip-link end. |

The exact current definitions are available from [QuickGO ESCRT-I](https://www.ebi.ac.uk/QuickGO/term/GO:0000813), [ribbon synapse](https://www.ebi.ac.uk/QuickGO/term/GO:0097470) and [tip-link density](https://www.ebi.ac.uk/QuickGO/term/GO:1990427). Hearing phenotypes alone do not establish those locations. The human association and Drosophila model in [PMID:20624953](https://pubmed.ncbi.nlm.nih.gov/20624953/) are retained as biological context.

By contrast, [PMID:24069443](https://pmc.ncbi.nlm.nih.gov/articles/PMC3777981/) directly stains endogenous mDia2 and pericentrin in mouse MII oocytes, supporting the specialized spindle-pole and organizing-center locations. [PMID:20660154](https://pmc.ncbi.nlm.nih.gov/articles/PMC2938385/) supports cleavage-furrow recruitment in mouse cells through Rho/anillin perturbation and rescue. These are contextual deployments of the cytoskeletal machinery, not extra molecular functions.

## Ancestral and electronic evidence

The actual PTHR45691 tree places human Q9NSV4 at PTN002509309 and mouse Q9Z207 at PTN000575534 within the DIAPH3 branch. Both descend from the family-root IBD node PTN000575131. The two relevant IBD assertions at that node are actin-filament localization and actin-filament polymerization. Acceptance concerns the ancestral placement and biological agreement, not donor number.

The actin-filament donor WBGene00019030 resolves to worm EXC-6/Q9TYU9 and its filamentous-actin IDA record to [PMID:25771894](https://pubmed.ncbi.nlm.nih.gov/25771894/). Its abstract and curated record were inspected; the original localization assay was not independently recovered. The polymerization donors include mouse Diaph1, Diaph2 and Diaph3. The historical zebrafish identifier was not resolved in the current tree and is not treated as negative biological evidence.

[PMID:14992721](https://pubmed.ncbi.nlm.nih.gov/14992721/) distinguishes monomeric core FH2 fragments from longer oligomerizing constructs. [PMID:23558171](https://pubmed.ncbi.nlm.nih.gov/23558171/) supports nuclear actin assembly, with only its abstract and current donor annotations independently available here. [PMID:23034183](https://pmc.ncbi.nlm.nih.gov/articles/PMC3510025/), Results comparing mDia proteins, assigns RhoD-induced protrusions to mDia3C and includes negative mDia2 controls. That specific response is not counted as positive Diaph3 grounding; independent assembly evidence supports the overall ancestral assertion.

The target has actual [IPR010472](https://www.ebi.ac.uk/interpro/entry/InterPro/IPR010472/) and [IPR010473](https://www.ebi.ac.uk/interpro/entry/InterPro/IPR010473/) matches and current InterPro2GO mappings. Whole-protein actin assembly supports the specific refinements; the mapped regulatory domains are not described as isolated actin-binding sites. Small-GTPase binding remains regulatory engagement, without assigning GTPase, GEF or GAP activity to DIAPH3.

## Reactome locations and proximity evidence

The three cytosol assertions resolve to human Q9NSV4 residues 1–1193, rather than an unrelated candidate effector. The exact public chains are:

- [RHOB recruitment, R-HSA-5666070](https://reactome.org/content/detail/R-HSA-5666070): input [5666066](https://reactome.org/content/detail/5666066), member [DIAPH3 dimer 5666128](https://reactome.org/content/detail/5666128), component [DIAPH3 5666125](https://reactome.org/content/detail/5666125).
- [RHOA effectors, R-HSA-9013009](https://reactome.org/content/detail/R-HSA-9013009): input [9013003](https://reactome.org/content/detail/9013003), member 5666128, component 5666125.
- [RHOB effectors, R-HSA-9690493](https://reactome.org/content/detail/R-HSA-9690493): input [9690490](https://reactome.org/content/detail/9690490), member 5666125.

Each final protein entity explicitly carries cytosol as its compartment. A cytosolic protein pool can be recruited to membrane-associated GTPases; these events do not make DIAPH3 a GTPase catalyst. [PMID:17198702](https://pubmed.ncbi.nlm.nih.gov/17198702/) provides abstract-level RhoB/mDia2 endosomal context.

[PMID:25468996](https://pmc.ncbi.nlm.nih.gov/articles/PMC4972397/), quantitative proteomics Methods, uses E-cadherin-BirA* in human MKN28 cells, parental controls and replicate/enrichment criteria. Proximity labeling includes direct and indirect neighbors. The DIAPH3 supplementary-table row was not independently recovered, so its positive HDA assignment remains curator-supported and non-core, without a claimed purified cadherin-binding interface.

## Product and access boundaries

The official products are Q9NSV4-3 (1193 aa, displayed), -1 (849 aa), -2 (691 aa), -4 (1182 aa), -5 (1147 aa), -6 (1123 aa) and -7 (1112 aa). Sequence differences alone establish neither equivalent activity nor inactivity. No present product is assigned the historical 1110-aa construct by approximate length.

The normal publication caches remain unchanged. In particular, abstract-only flags for 18755006, 19457867, 16556604, 15311282 and 23558171 are preserved even where a separate author manuscript or original Methods was recovered. The first four have the separate access scopes described above; 23558171 remains abstract-only. Claims do not rely on unsuccessful supplementary-file downloads. The review's four short quotations occur once each in the YAML; the surrounding reference assessments and this guide use paraphrase.

Annotation specificity follows the [project curation instructions](https://github.com/ai4curation/ai-gene-review/blob/bff21ea8eb90bc3e07bb2fbedf14c25d37080161/projects/CLINGEN_MENDELIAN.md#curation-instructions). Broad valid terms are refined using MODIFY. Positive contextual associations are retained when a more specific molecular claim is not supported. Existing process coverage supports the two core units; no NEW annotation is proposed.
