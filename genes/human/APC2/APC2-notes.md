# APC2 annotation review notes

## Initial scope and provenance

The exact Seed9 baseline contains 52 PENDING annotations and three alternative products for human APC2 (O95996; APCL). Baseline YAML, raw GOA and UniProt bytes are preserved in `tmp/APC2-initial/baseline`. All eight original PMID caches are present. Seven are abstract-only; PMID:26393419 contains full text. The differing Seed9 candidate for PMID:9601641 is retained separately, with no canonical overwrite. No citation or source assertion has yet been edited.

The configured Falcon research command with Perplexity fallback failed once in 4.932 seconds and produced no provider document. These are manual source notes. Existing normal source caches were inventoried concurrently; no redundant cache fetch was run. Five additional absent sources are being attempted once through the ordinary bounded publication command.

## Initial primary-source reading

All seven original abstract-only records were read in full. PMID:9823329 describes the cloned human APCL protein, beta-catenin binding and downregulation. PMID:10021369 reports mammalian APC2 conductin-binding SAMP domains and suppression of beta-catenin/Tcf activity. These support a Wnt-regulatory role independently of the later fly mechanism.

PMID:10644998 explicitly studies APCL with EB3 and reports localization with the microtubule network. Its complete Methods and the distinct EB1/EB3 partner/isoform assay boundaries remain to be inspected. PMID:10646860 describes APCL–TP53BP2 interaction and perinuclear redistribution, but the proposed p53/BCL2 pathway function is a hypothesis. PMID:11691822 explicitly reports human endogenous and overexpressed APC2 localization at cytoplasm, Golgi and actin-associated structures; exact leading-edge/lamellipodial evidence needs the body. PMID:25753423's abstract establishes the disease/neuronal context but does not itself resolve the human-construct cytoskeletal and Rac1 assays. Indexed original Figure 2/3 captions have been located; full scope will be recorded after targeted reading.

PMID:26393419 was inspected at the actual Results opening, targeted complex-assembly passages and construct/cell/kinase Methods. Its experimental APC2 is Drosophila APC2; the human APC constructs concern APC1. Human SW480 cells are the host, and their endogenous APC2 is mentioned separately. Thus host species must not be treated as a human APC2 construct. The source also acknowledges very high transfected-protein abundance. The human APC2 Wnt function is independently supported by the original cloning studies, but the source-specific IMP row needs an explicit evidence-scope judgment rather than an inference from the title. The remaining full text and any relevant supplementary target assay have not yet been exhaustively inspected. [PMID:26393419](https://elifesciences.org/articles/08022)

PMID:9601641's abstract concerns human Axin and APC and describes the destruction-complex mechanism. This alone does not establish a wrong-gene citation: its full body and the ComplexPortal NAS provenance remain to be checked. No removal is inferred from its title.

## Additional literature identified

PMID:30018294 directly supplies human APC2 constructs (actual DNA/construct Methods), assayed in rat hippocampal neurons and cell lines. Targeted Results distinguish extended-S lattice association, EB3-linked plus-end interactions and DYNLL2-dependent clustering. Local stabilization and rescue sites coexist with increased microtubule dynamics; the review should not describe APC2 as simply suppressing all dynamics. Full supplementary material and figure pixels have not been inspected. [Primary article](https://pmc.ncbi.nlm.nih.gov/articles/PMC6050278/)

PMID:19759310 provides chick retinal axon context; PMID:22573669 provides mouse neuronal migration and cue-responsive cytoskeletal context. PMID:31291912 uses constitutive Apc2-knockout mice and supports tissue-dependent physiological Wnt regulation beyond the nervous system. PMID:31585108 describes human biallelic APC2-associated lissencephaly and heterotopia; this clinical evidence does not manufacture a new GO process assertion. Exact individual access limits are recorded in `tmp/APC2-initial/additional-primary-assessment.json`.

## Curation boundaries

Every original term, reference, evidence code, partner, qualifier and product will be preserved. Ordinary relation qualifiers do not determine decisions. IBA target self-inclusion is expected, and donor count will not be treated as evidence weakness. Prospective core candidates are microtubule binding and beta-catenin-associated regulation, subject to full source synthesis. No new biological process is currently proposed.

## Targeted original-body checks

The ordinary five-ID fetch timed out after 45.024 seconds with no output; this was one interrupted batch, not five completed failures. Its receipt preserves that distinction. No repeat was attempted.

PMID:25753423 original published Results and Figures 2–3 captions were read through the author-uploaded article. They explicitly identify human wild-type and mutant APC2 constructs, expressed in Neuro2a cells; primary mouse cortical neurons were an additional host. Wild-type protein associated with microtubules and F-actin, protected acetylated microtubules from nocodazole, and increased GTP-bound Rac1 relative to control. The measured activation does not establish intrinsic nucleotide-exchange catalysis. Main Experimental Procedures were read, but detailed supplemental protocols and supplementary images were not. [Published article copy](https://www.researchgate.net/publication/273386475_Loss-of-Function_Mutation_in_APC2_Causes_Sotos_Syndrome_Features), Results “The Mutant APC2 Protein Is Functionally Null,” Figures 2–3.

PMID:11691822 publisher-indexed Results, localization Discussion and Figure 4 caption were read. Antibody specificity controls distinguish APC2 from APC; endogenous human A549 and breast-cell signals include perinuclear/Golgi and membrane-associated actin structures. Figure 4E specifically identifies lamellipodial membrane. Microtubule decoration in that paper is an overexpression observation, a scope limitation consistent with later independent human APC2 assays. This was targeted body/caption access, not figure-pixel or complete Methods inspection. [Original publisher article](https://aacrjournals.org/cancerres/article/61/21/7978/508132/Human-APC2-Localization-and-Allelic-Imbalance1).

Current official GO:0090630 describes initiation of GTPase activity by GDP-to-GTP exchange, so active Rac1 supports the existing process context without implying APC2 is a GAP or GEF. Current GO:0016342 is the cadherin-associated catenin complex connecting to actin, not any complex containing beta-catenin. Its three original assertions therefore require source-specific examination distinct from beta-catenin binding and the destruction complex. [GO:0090630](https://amigo.geneontology.org/amigo/term/GO:0090630); [GO:0016342](https://amigo.geneontology.org/amigo/term/GO:0016342).


## Original APCL fragment experiments

The original [PMID:9823329 paper](https://www.researchgate.net/publication/13464037_Identification_of_a_brain-specific_APC_homologue_APCL_and_its_interaction_with_-catenin) was read at the functional Methods, corresponding Results/Discussion and Figures 5–7 captions. The human APCL fragment 627–1666, rather than full-length protein, was used for the reticulocyte/GST beta-catenin binding and SW480 depletion/TCF reporter experiments. These are positive beta-catenin-binding and Wnt-suppression data. They do not directly place APCL in the cadherin-associated catenin complex described by current GO:0016342. The latter source-specific cellular-component assertion needs separate adjudication; no change to the original source fields or abstract-only cache has been made.

## Current primary database boundaries

The official [HPA APC2 subcellular page](https://www.proteinatlas.org/ENSG00000115266-APC2/subcellular) reports supported cytokinetic-bridge staining in SH-SY5Y and U2OS cells and supported cytosolic signal. The summary and human-cell table were inspected; image pixels were not independently reanalyzed. These support the original locations, without adding a cytokinesis process from location alone.

The exact Seed9 InterPro/PANTHER member record identifies human APC2 O95996 in PTHR12607. Its actual IBD, tree and alignment were not recovered: the official web route failed, and one bounded direct IBD request failed DNS with zero bytes. Family membership is not a substitute for ancestral-node inspection. Target experimental grounding and original node/donor fields remain distinct; neither self-inclusion nor a short donor list is treated as faulty evidence.

An initial all-52 prospective assessment is ready for independent review: 29 ACCEPT, 11 KEEP_AS_NON_CORE, 11 UNDECIDED and one source-specific MARK_AS_OVER_ANNOTATED, with no NEW assertion. These are proposed decisions pending consultation and actual Source37 cache closure; canonical annotations remain PENDING at this stage.


## Independent consultation and original EB-binding experiments

The complete 52-row prospective review passed independent consultation. Original [PMID:10644998](https://www.researchgate.net/publication/12669553_EB3_a_novel_member_of_the_EB1_family_preferentially_expressed_in_the_central_nervous_system_binds_to_a_CNS-specific_APC_homologue) Results, Figures 4–8 captions, Discussion and binding/culture Methods have now been read by both reviewers. The paper's in-vitro assays support APCL binding to EB1 and EB3. Reciprocal coimmunoprecipitation supported tagged full-length APCL–EB3 in Cos-7 cells, whereas EB1 coimmunoprecipitation was not detected under the same conditions. These distinct results are compatible. The original EB3 accession is AB024964; an exact mapping to the separately annotated Q9UPY8-1 partner remains unverified. The EB1 row is therefore retained as non-core, while the distinct isoform-partner assertion remains uncertain.

The original tagged APCL microscopy showed a perinuclear pool and partial microtubule-network localization in Cos-7/SW480 expression experiments. The authors explicitly qualify tag and overexpression effects; this does not replace the later endogenous human localization evidence.

The cadherin-associated catenin-complex assertion from PMID:9823329 is over-annotated relative to its actual human APCL fragment binding and beta-catenin/TCF experiments. The original functional Methods, Results and Discussion and the official GO:0016342 definition were independently read. This is a source-specific boundary, not a claim that APC2 can never occur at adhesion sites. The separate IBA and ARBA complex derivations remain unresolved. Current [GO:0008013](https://amigo.geneontology.org/amigo/term/GO:0008013) is the molecular function beta-catenin binding, which those fragment assays directly support.

## Actual recovered-source scope

All five additional normal records were inspected in the exact Source37 artifact. PMID:19759310, PMID:22573669 and PMID:31585108 remain abstract-only; their normal availability flags are preserved. PMID:30018294 and PMID:31291912 contain XML-derived bodies. These records were imported without rewriting the eight original publication caches.

For [PMID:30018294](https://pmc.ncbi.nlm.nih.gov/articles/PMC6050278/), actual human-clone/DNA, animal/culture and human iPSC-neuron Methods, targeted Results/Figures 1–7 and Discussion were read. The human APC2 constructs were tested in rat hippocampal neurons and cell lines; endogenous human iPSC-neuron localization is a separate observation. Extended-S lattice association differs from SxLP-dependent plus-tip interaction. Rat depletion reduces minus-end-out microtubule dynamics, and human full-length protein rescues the reported dynamicity defect. DYNLL2 association is supported by HEK lysate pull-downs. Stabilizing patches that allow regrowth are a proposed mechanistic explanation; individual rescue events are not asserted to have been reconstituted with purified APC2. No independent figure-pixel or complete supplemental analysis is claimed.

For [PMID:31291912](https://pmc.ncbi.nlm.nih.gov/articles/PMC6617595/), the actual animal Methods, targeted WNT/follicle and aged-cohort Results, and Discussion caveats were read. The experiments use constitutive Apc2 knockout mice, and aged tumour cohorts also carry a hypomorphic Apc allele. WNT target expression rises in young knockout ovaries, but tissue specificity and autonomous versus nonautonomous effects remain explicit. This is corroborating mammalian Wnt evidence, not a direct human ovarian assay.

The chick axonal context (PMID:19759310), mouse migration context (PMID:22573669) and human lissencephaly cohort (PMID:31585108) provide useful biological context without creating new process annotations. Disease severity and rescue do not alone justify a new process. The actual Source37 read receipt records individual source limits.

## Current authored assessment

All 52 original source objects and all three alternative products are preserved: 29 ACCEPT, 12 KEEP_AS_NON_CORE, 10 UNDECIDED and one MARK_AS_OVER_ANNOTATED. There are no NEW annotations. Two functions are summarized: microtubule binding and beta-catenin binding associated with Wnt suppression. The source-specific fly APC2 IMP claim, unread NAS derivations, unresolved phylogenetic assertions and exact EB3 isoform mapping remain visible. The original sources, not their replacements, remain attached to every assertion.


## Final authored checks

Full gene validation and rendering passed. Five intentional advisories remain: three experimentally supported generic binding records retained as non-core under the explicit removal criteria, and two term-level action differences whose underlying source evidence differs. The five unresolved IBA assertions carry UNRESOLVED propagation metadata rather than an invented phylogenetic failure. All 52 original source objects, three alternative products, two raw seed files and eight original publication caches are unchanged. Source37 contributes five exact additional normal caches; all supporting snippets and availability flags were checked against their actual sources. No NEW assertions were added.
