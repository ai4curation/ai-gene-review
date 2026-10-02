# BMPR1A annotation review notes

Manual source assessment and TMP annotation draft by `/root/bloc_followup`, 2026-10-02 UTC. This is a human P36894/BMPR1A review; it is not a provider-generated deep-research report. The normal falcon/perplexity attempt stopped on dependency resolution before provider execution. The normal publication command found all 31 requested PMID records already cached. Both observations are preserved in the project working evidence.

## Draft scope and decisions

All 140 normal-seed annotation objects are preserved, corresponding to 143 raw source rows after the closed duplicate reconciliation. Only their review sections are authored. The draft has 44 ACCEPT, 77 KEEP_AS_NON_CORE, nine MODIFY and ten UNDECIDED actions; no NEW, REMOVE or MARK_AS_OVER_ANNOTATED rows. Original term identifiers/labels, evidence codes, source references, partners, qualifiers and both negation flags are unchanged. There are no seeded isoforms or alternative products, and none are manufactured from receptor constructs, ligand variants or processed chains.

One core mechanism combines extracellular BMP recognition, receptor-complex assembly and the intracellular serine/threonine kinase step that transmits the signal to R-SMADs. Its primary MF is GO:0098821 BMP receptor activity, with BMP signaling, plasma-membrane location and signaling receptor complex membership. ATP binding and SMAD engagement are parts of that same mechanism, not separate core-function duplicates. The AMH pathway remains a supported developmental use of this receptor machinery, bounded by the conditional mouse evidence in PMID:12368913.

Nine generic-binding assertions are refined to GO:0036122 BMP binding (source rows 31, 33, 34, 35, 37, 38, 43, 47, 49). These preserve the BMP2 or GDF5 partner accessions. The reciprocal ligand activity, BMP receptor binding, is not assigned to the receptor. ProBMP2 binding is not mature-ligand agonism; engineered GDF5 R57A is not a receptor isoform; GDF5 preference for BMPR1B does not eliminate measured lower-affinity BMPR1A binding.

The generic-binding policy normally excludes bare protein binding because it contributes little functional information. The task-specific campaign instruction instead retains supported interactions as non-core where the source does not establish a defensible replacement. Accordingly, eight rows remain KEEP_AS_NON_CORE: ACVR1 association (36), BMP2/BMP4 source-specific assays not independently read in full (39–42), TSC22D1 (44), HFE (48), and SCUBE3 (50). This is an explicit scoped instruction, not a global policy change. The remaining three generic interactions (32, 45, 46) remain UNDECIDED because the exact source experiment could not be adjudicated. No association is upgraded to catalytic, adaptor or scaffolding activity from interaction evidence alone.

Ten unresolved cases are explicit: TGFBRAP1 (32); two PMID:21976273 partner assertions (45, 46); immune response from a polymorphism association (66); two ligand-specific TGF-beta pathway assertions (68, 69); endogenous neuronal receptor participation versus soluble ligand trapping (128); the neural-crest NOT donor chain (136); and two complete HFE–transferrin-receptor complex assertions (139, 140). These are source-access or claim-specific uncertainties, not findings that the gene or reference is wrong.

The two GO:0005025 activity assertions retain curator usage as non-core while the core uses BMP receptor activity. All six cached BMPR1A GO-CAM activities use GO:0005025; that repeated modeling convention is considered explicitly rather than dismissed because the current definition is more ligand-specific. The exact terminology is raised as a question. The models cover BMP2, BMP4, BMP5/dendrite growth, BMP2/BMP6/hepcidin, BMP8A, and AMH contexts (645d887900001795, 66e382fb00001232, 66e382fb00001388, 66e382fb00001786, 66e382fb00002105, 67c10cc400005742).

The cardiac apoptosis NOT is retained only as a bounded source observation: early SM22alpha-Cre experiments show reduced myocardial proliferation without enhanced apoptosis, whereas other deletion timings differ. The neural-crest NOT remains unresolved pending its exact donor chain. Neither negation is edited. The two neuronal-location transfers (81, 98) are from rat Q78EA7/ENSRNOP00000074885, not mouse. Mouse P36895 transfers are not described as direct human developmental assays. PAINT assertions are assessed as ancestral-node judgments; target self-support and short donor lists are not objections.

## Source access and exclusions

All 31 seeded PMID abstracts and nine Reactome records were read. Selected full-text passages were read where documented in the journal below; an available full-text cache is not a claim to have read every figure, supplement or paragraph. Canonical quotations are exact substrings of retained source files. Selected archived text is distinguished from fuller or shorter canonical copies, notably PMID:18326817 (canonical abstract-only) and PMID:18436533 (canonical full text).

PMID:3917437 concerns ecto-galactosyltransferase in intestinal cells and is irrelevant to BMPR1A. It is not a source reference in this 140-row seed and is not added to this review. No citation is imported merely because it was present in a neighboring gene task. Reactome R-HSA-201453 has a title/body mismatch; its source bytes are preserved and the review flags that limitation without denying independently supported receptor membrane localization.

The manual findings and exact read boundaries below precede final candidate authoring and remain an access record, not a substitute for the annotation decisions above.

# BMPR1A source assessment journal

Read-only source assessment by `/root/bloc_followup`, 2026-10-02 UTC. This precedes final candidate authoring and does not authorize source import or overwrite. All 31 archived abstracts and nine Reactome records were read. The complete source-object inventory and curated-model projection were examined; no source fields changed.

## Receptor binding and signaling

[PMID:10881198](https://pubmed.ncbi.nlm.nih.gov/10881198/) and [PMID:15064755](https://pubmed.ncbi.nlm.nih.gov/15064755/) directly support the BMP2–BMPR1A ectodomain interface. [PMID:16672363](https://pubmed.ncbi.nlm.nih.gov/16672363/) describes the ternary ligand/type-I/type-II ectodomain structure and explicitly separates the receptor interfaces. These three archived abstracts were read; no image or coordinate analysis was performed.

[PMID:25938661](https://pmc.ncbi.nlm.nih.gov/articles/PMC4456160/) supplies direct human BMPR1A ectodomain/BMP2 SPR evidence despite its RGM-centered title. Full-text Results, receptor-construct Methods, and SPR Methods were read (archive lines 107, 113, 121, 141, 151, 193; f13a8f). The human receptor construct is reported as residues 49–141. The work distinguishes BMP2 binding by BMPR1A from RGM-mediated scaffolding and a proposed endosomal mechanism. It does not make BMPR1A an RGM scaffold or an endocytic enzyme. Soluble ectodomain inhibition is a ligand-trap experiment, distinct from endogenous signaling.

[PMID:24098149](https://pmc.ncbi.nlm.nih.gov/articles/PMC3789827/) directly compares recombinant wild-type human GDF5 and W414R binding to receptor ectodomains. The selected Results and Methods (archive lines 243, 245, 335; 632a76) confirm measurable wild-type GDF5–BMPR1A binding and reduced mutant affinity. Thus the BMPR1B preference in [PMID:19229295](https://pubmed.ncbi.nlm.nih.gov/19229295/) cannot be read as absolute absence of BMPR1A binding. [PMID:16127465](https://pubmed.ncbi.nlm.nih.gov/16127465/) likewise compares both receptors. Read boundaries for these latter two sources are the complete archived abstracts.

[PMID:21543859](https://pmc.ncbi.nlm.nih.gov/articles/PMC3087638/) uses high-affinity engineered GDF5 R57A. Selected Methods and final Results were read (archive lines 80, 86, 118; 632a76): human BRIA extracellular domain, bacterial expression, purified ligand–receptor complex. The paper reports its own ectodomain numbering; this was not independently remapped to precursor coordinates. Neither R57A nor the truncated receptor is a natural isoform. The crystallization study was still completing structural refinement.

[PMID:19804412](https://pubmed.ncbi.nlm.nih.gov/19804412/) explicitly distinguishes proBMP2 binding to BMPR1A from mature BMP2-like osteogenic activation. A binding refinement must preserve the pro-form context and must not add productive agonism. Complete archived abstract read.

[PMID:18436533](https://pmc.ncbi.nlm.nih.gov/articles/PMC3258927/) has fuller retained canonical text than the archive. Canonical construct, BRET Methods and Results were read (404e35, fdb69b, c5b2f2, 4fa144; lines 213–235, 267–356, 470–605). Human receptor cDNAs and full-length fusion constructs were used in HEK-293 BRET saturation/competition assays. The supported BMPR1A–ACVR1 association and BMPR1A self-association are distinct from the human mesenchymal-cell RNAi experiments. Ligand-induced mineralization was measured separately; receptor perturbations assessed signaling and osteoblast marker outputs. Avoid describing a purified direct-binding experiment, fixed physiological stoichiometry, or a receptor-specific mineralization assay that was not read.

The abstract-only sources PMID:20860622 and PMID:21054789 emphasize ligand antagonists; that does not establish a wrong-receptor annotation. Original curated BMP2/BMP4 partner assertions must retain their identities and explicit access limits. PMID:21976273 similarly does not allow a complete construct inventory from its GDF5/antagonist-focused abstract alone.

## Kinase terminology and curated models

All six target activities in the saved GO-CAM projection use GO:0005025 for human BMPR1A. The complete compact activity/edge view was read in 85c811 after a broader JSON display was truncated. The BMP and AMH contexts establish that this is an existing curator modeling convention. The term definition should not be converted into an accusation that these are wrong-gene annotations. The more specific BMP receptor activity already occurs in source rows 125–127 and remains appropriate for core synthesis.

PMID:12065756 is not disqualified by its ALK4/5/7-focused title: the abstract includes BMP-receptor comparators, and ROOT's saved publisher Methods identify human activated ALK3. PMID:9136927 establishes direct type-I-receptor SMAD1 phosphorylation in its abstract and is the repeated GO-CAM evidence. Full construct-specific kinase assays remain unread. PMID:36641752 includes a human arm; its BMP/TGF-beta-superfamily framing must be distinguished from a specific TGF-beta-ligand claim. No broad wrong-gene inference is justified by these access limits.

The full nine archived Reactome records were read in 33fd1b. R-HSA-201476 describes the intrinsic type-I-receptor kinase step; R-HSA-201443 describes type-II activation of the type-I receptor. R-HSA-201821 makes the receptor the ubiquitination substrate. R-HSA-202604 allows both pre-existing and ligand-induced complexes. R-HSA-201453 has a title/body mismatch, which remains a source limitation; it is not a reason to deny independently supported plasma-membrane location or edit the cache.

## Conditional processes and negative annotations

[PMID:18667463](https://pmc.ncbi.nlm.nih.gov/articles/PMC2653628/) full-text Methods, Results and Discussion were read in 6e35c8. The human pulmonary smooth-muscle experiments distinguish increased basal migration after BMPR1A RNAi from impaired PDGF-BB-directed migration after serum starvation. The original negative-regulation term is compatible with the basal condition. The mouse SM22alpha-Cre E10.5–E11 heart phenotype involves reduced proliferation without enhanced myocardial apoptosis, while the Discussion contrasts later alpha-MHC/Isl1 contexts. Preserve the NOT annotation and limit any inference to the tested model/stage; the original GO_REF donor chain remains unverified. Human proliferation assays and mouse developmental phenotypes must remain separate.

[PMID:11580864](https://pmc.ncbi.nlm.nih.gov/articles/PMC56999/) selected Results and Discussion were read in 6e35c8 (archive lines 108, 132). Soluble BMPR-IA-Fc inhibits BMP5-induced dendrites. The authors explicitly leave endogenous neuronal receptor binding unresolved. This is not an endogenous BMPR1A knockout experiment. The existing GO-CAM preserves a curator-supported downstream process context; any retention must state the source's limit.

[PMID:18326817](https://pmc.ncbi.nlm.nih.gov/articles/PMC2384142/) archive full-text Methods/Results/Discussion paragraphs 78, 98, 102, 146, 150, 152, 154, 156, 182 were read (632a76). ALK3 RNAi reduces BMP/HJV reporter and hepcidin-promoter output in Hep3B and Huh-7 contexts; ALK2/ALK6 utilization depends on cell and ligand. This supports receptor-dependent transcriptional regulation, not DNA binding by BMPR1A. The retained canonical cache is abstract-only, so any final machine-checked quotation must come from its retained bytes; archive-only details can be described in notes with their exact access boundary.

PMID:16886151 reports SNP/bacteremia association, not direct molecular work in immune response. PMID:24882581 reports BMPR1A perturbation in a tumor/angiogenesis context. Neither should silently become an unrestricted defining core function.

The neural-crest NOT donor chain remains unresolved. ROOT's Stottmann 2004 versus earlier-deletion studies are useful timing leads, not proof of the exact original source chain. Mouse and rat transfers must remain distinguishable; the two neuronal-location donors are rat.

## Interaction versus complete complex

[PMID:24904118](https://pmc.ncbi.nlm.nih.gov/articles/PMC4624447/) supports HFE–ALK3 association and surface stabilization. Independently read indexed primary Discussion says TFR2 interaction is weak and the four-component assembly is possible. GO:1990712 requires HFE plus a transferrin receptor; ROOT's saved official definition was read in 2ef7bf. This supports treating assembly uncertainty separately from the positive HFE interaction. No supplemental image was inspected and no absence of a complex was demonstrated.

UniProt's target-specific TSC22D1 and SCUBE3 interaction statements were rechecked (b1485d). Their abstract-centered source access does not justify assigning their adaptor/scaffold or transcriptional activities to BMPR1A. The TRAP1/TGFBRAP1 interaction remains target-assay-unresolved from the accessible abstract.

## Access record

All 31 archived abstracts: 02810b, 851e68, 55b4a9, 1747a8. All nine Reactome bodies: 33fd1b. Selected complete primary passages: 6e35c8, 632a76, f13a8f. Canonical PMID:18436533 selected full-text reading: 404e35, fdb69b, c5b2f2, 4fa144. New primary/ontology web results are saved alongside this journal. Direct PMC access to PMID:21791611 encountered a browser challenge. One unverified JBC URL was inaccessible and supplies no evidence. No figure-image, supplemental-file, coordinate, complete full-text, or original QuickGO JSON read is claimed beyond the explicitly listed scope.
