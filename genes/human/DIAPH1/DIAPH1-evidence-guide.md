# DIAPH1 evidence scope and source tracing

This guide distinguishes human target evidence, homolog evidence and the exact scope of the existing annotations. It accompanies the [DIAPH1 review](DIAPH1-ai-review.yaml). All 60 imported annotation identities are retained; refinements occur only in their review fields. No additional annotation is proposed.

## Identity and products

[HGNC:2876](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2876) identifies human DIAPH1; the reviewed [UniProt O60610 record](https://www.uniprot.org/uniprotkb/O60610/entry) gives three products: O60610-1, 1,272 residues; O60610-2, 1,248 residues; and O60610-3, 1,263 residues. The alternative sequences were reconstructed from the official variant features and checked against the corresponding official FASTA sequences. The review retains the genuine fetched product objects.

The older names mDia1, hDia1, DIAP1 and DFNA1 require species and construct checks. A historical construct ending at residue 1263 does not alone establish that the experiment used current O60610-3. Gene-level mass-spectrometry assignments likewise do not distinguish these three products. The 80-kDa band in the platelet study was discussed as possible limited proteolysis, not established as an additional splice product.

## Direct actin and cytoskeletal evidence

[Higashi et al., PMID:18218625](https://doi.org/10.1074/jbc.M707839200) used human bone-marrow cDNA for mDia1 N-terminal residues 69–450 and C-terminal residues 753–1263. The original Methods and Results were read from the public author-posted article. Purified regulatory fragments were studied alongside platelet-cytosol actin assembly, rather than an entirely purified actin reconstruction. Figure 6A explicitly includes weak RhoD/RhoF binding. The assembly-rescue result concerns RhoA/B/C; the thrombin-dependent co-immunoprecipitation result concerns DAAM1. Those distinctions govern the pair reviews.

[Stritt et al., PMID:26912466](https://doi.org/10.1182/blood-2015-10-675629) was read in the public Cambridge accepted manuscript. Human platelet phenotypes and wild-type/R1213* comparisons in human cell lines support DIAPH1-dependent actin and microtubule organization. The cell experiments controlled DIAPH2/3 expression. The FH2 inhibitor reduced the excess F-actin phenotype while not reversing microtubule stabilization. This supports one integrated actin-assembly core without assigning a separate microtubule catalytic activity.

[Zaoui et al., PMID:20937854](https://pmc.ncbi.nlm.nih.gov/articles/PMC2972954/) was read in the separately recovered PMC original, including the mDia1 knockdown and GSK3B phosphorylation experiment in human SKBr3 cells. The mechanism includes MEMO1, RHOA, APC, CLASPs and ACF7; their activities are not assigned to DIAPH1. The exact supplemental mDia1 siRNA sequence was not independently recovered.

[Ercan-Sencicek et al., PMID:24781755](https://pubmed.ncbi.nlm.nih.gov/24781755/) was read in the separately recovered PMC original. Human ReNcell CX cells show DIAPH1/pericentrin colocalization at centrosomes and mitotic spindles. Human fetal-brain expression, human loss-of-function cases and targeted mouse observations support the developmental context. The mouse knockout retained cortical organization and apical actin belts despite ventricular dilation; this does not establish an equivalent human spindle-perturbation experiment.

## Binding evidence and its limits

Specific binding refinements require evidence for the corresponding recognition. Co-complex association alone does not establish a narrower partner-class molecular function. None of these annotations assigns the partner’s enzymatic activity, physiological stoichiometry or equal behavior of all DIAPH1 products.

| Source | Evidence inspected | Review scope |
| --- | --- | --- |
| [PMID:18230650](https://doi.org/10.1242/jcs.013557) | Public author-posted original: cellular co-immunoprecipitation and GST-POPX2/His-mDia1 261–571 overlay | [PPM1F/P49593](https://www.uniprot.org/uniprotkb/P49593/entry) supports protein phosphatase binding. The host cell does not establish the species of an otherwise unspecified construct. |
| [PMID:18922799](https://pmc.ncbi.nlm.nih.gov/articles/PMC2590709/) | Human RAGE tail and human lung DIAPH1 library/constructs; two-hybrid, pull-down and cellular co-immunoprecipitation | [AGER/Q15109](https://www.uniprot.org/uniprotkb/Q15109/entry) supports signaling receptor binding. Rat C6 signaling results remain distinct. The pull-down used an in-vitro-translated DIAPH1 fragment, not two purified proteins. |
| [PMID:22190034](https://pmc.ncbi.nlm.nih.gov/articles/PMC3310911/) | Original AP-MS Methods and exact IntAct records EBI-6176962 and EBI-6178643 for O60610/Q9Q2G4 | Retain the supported association as non-core protein binding. The bait carries a catalytic-site D25 mutation; AP-MS/pull-down does not establish direct protease recognition or a native proteolytic or antiviral mechanism. |
| [PMID:33961781](https://pmc.ncbi.nlm.nih.gov/articles/PMC8165030/) | Genuine PMC original Methods and exact records EBI-54908625 (RHOD) and EBI-54651993 (RHOC) | Small GTPase binding. BioPlex uses tagged baits and gene-level aggregation; the AP-MS associations do not independently prove direct contact. |
| [PMID:22658674](https://doi.org/10.1016/j.cell.2012.04.031) | Institutional original plus supplement and Table S1: DIAPH1, ENSG00000131504, in the HeLa mRNA interactome | UV crosslinking and stringent oligo(dT) capture support RNA contact. Protein groups were aggregated by gene; specific RNA targets, domains and product differences remain unresolved. |

The [PKD2 paper, PMID:15123714](https://doi.org/10.1074/jbc.M400544200), was read from its public author-posted original. Its initial two-hybrid prey library was mouse; native human HEK293 co-immunoprecipitation independently supports the interaction. Human HeLa knockdown affects spindle PKD2 and histamine-evoked calcium release in mitosis, with unchanged interphase responsiveness. The endogenous double-staining image is porcine; human spindle isolation and independent human neural-progenitor imaging support the retained location. No DIAPH1 calcium-channel activity is inferred.

[PMID:9360932](https://doi.org/10.1126/science.278.5341.1315) was read in its author-posted original. It establishes human genetic segregation and cochlear expression. Its proposed hair-cell mechanisms remain hypotheses. The original receptor-binding NAS row is retained on independent RAGE evidence, not presented as a direct receptor assay in this genetics paper.

## Inherited evidence

The exact PAINT IBD node is PANTHER:PTN000575131 in PTHR45691. Human DIAPH1 leaf PTN002509308 lies below it. The worm EXC-6 leaf and the three named mouse Diaph leaves were reconstructed in the actual tree. Current EXC-6/Q9TYU9 has experimental GO:0031941 evidence to [PMID:25771894](https://pubmed.ncbi.nlm.nih.gov/25771894/), which grounds the broader filament location. Mouse polymerization assertions are experimentally grounded. The historical ZFIN:ZDB-GENE-090115-1 seed was not resolved in the current tree; no replacement identity is guessed. This bounded identifier gap does not negate the independently supported ancestral assertion.

InterPro target matches were verified for IPR010472 (274–466) and IPR010473 (84–268), together with the official entries and current InterPro2GO mappings. Domain mappings are assessed against the whole protein and the direct human experiments. Broad organizational terms are refined to the supported polymerization step; broad cytoskeleton and spindle locations are refined to actin filament and mitotic spindle.

Mouse Diaph1/O08808 and its Ensembl product were traced in the official record. Direct donor evidence supports profilin binding and membrane recruitment ([PMID:9214622](https://pubmed.ncbi.nlm.nih.gov/9214622/)), nuclear actin ([PMID:23558171](https://pubmed.ncbi.nlm.nih.gov/23558171/)), neuronal contexts ([PMID:18572016](https://pubmed.ncbi.nlm.nih.gov/18572016/)) and synaptic-vesicle retrieval ([PMID:28231467](https://pubmed.ncbi.nlm.nih.gov/28231467/)). Those caches are abstract-only, and no unobserved Methods are claimed. The conserved contextual annotations are retained with their donor grounding and explicit limits.

The full cached original for [PMID:22114352](https://pmc.ncbi.nlm.nih.gov/articles/PMC3258176/) identifies mDia1 in isolated adult-mouse intestinal brush-border proteomics and describes isolation and immunoblotting. The inherited brush-border location is supported; the proposed microvillar-tip role was not established by that detection.

## Reactome location tracing

The 12 cited events were followed through actual input/output, component and member relationships to an O60610 protein reference. Cytosolic protein 5665970 is reached directly or through dimer 5665967. RHOA/RHOC/RHOD/RHOF effector sets contain DIAPH1 as an explicit member. The expression event R-HSA-9857585 produces DIAPH1; it does not make DIAPH1 the transcriptional regulator.

For granule exocytosis, input sets 6800420 and 6800437 contain DIAPH1 entities 6801368 (secretory-granule membrane) and 6801388 (ficolin-1-rich granule membrane). Output sets 6806534 and 6806514 contain DIAPH1 entity 6801557 (plasma membrane). Each resolves to O60610. These location annotations do not depend on a generic set-name match and do not create a new exocytosis-process assertion.

## Access and quotations

Original recovery does not change a publication cache’s literal `full_text_available` flag. Short exact excerpts occur once in the review; other supported-by entries refer back to the same sources without repeating quotations. The scope above, rather than quote count, determines what was inspected. The project’s [explicit curation instruction](https://github.com/ai4curation/ai-gene-review/blob/298fede2212a4d540865542e5e8b396bec69107c/projects/CLINGEN_MENDELIAN.md#curation-instructions) governs retention of supported interactions and source-specific refinements.
