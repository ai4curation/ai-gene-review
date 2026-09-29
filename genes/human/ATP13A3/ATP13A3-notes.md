# ATP13A3 review notes

## 2026-09-29 — source-grounded initial review

ATP13A3 is a human P5B-type ATPase associated with cellular polyamine uptake. The normal seed supplies 24 GO assertions and two named products (Q9H7F0-1 and Q9H7F0-2). Preserve every original annotation ID, evidence code, qualifier and supporting entity. UniProt flags the second product as a dubious splice isoform; no product-specific activity is inferred here, and the source sequence-note text is retained verbatim.

### Primary transport evidence

[PMID:33310703, ATP13A3 is a major component of the enigmatic mammalian polyamine transport system](https://pubmed.ncbi.nlm.nih.gov/33310703/) directly studies human WT and D498N ATP13A3 expressed in hamster CHO hosts. WT restored BODIPY-putrescine uptake in mutant CHO-MG cells; comparable expression of D498N did not. Knockdown provided a complementary cellular phenotype. Polyamine competition and probe-uptake experiments support broader substrate scope. The human construct and hamster host must be distinguished.

Endocytosis inhibitors reduced uptake. Mutant cells retained the probe in endosomal structures despite increased transferrin endocytosis, supporting a two-step uptake model involving endosomal delivery to the cytosol. These are cellular uptake and localization experiments. They do not measure purified ATP13A3 translocation, exact ATP/substrate stoichiometry, or direct plasma-membrane flux. The paper explicitly leaves purified-protein characterization for future work.

Root read the complete abstract and selected WT/D498N rescue, knockdown, competition and endocytosis Results, with the relevant vector/cell-culture/uptake Methods. Figure pixels and the complete supplement were not inspected. The normal XML cache was imported unchanged through the verified Seed27 auxiliary workflow; preexisting source caches and raw gene files were preserved.

### Localization and catalytic mechanism

[PMID:29505581, Parkinson disease related ATP13A2 evolved early in animal evolution](https://pubmed.ncbi.nlm.nih.gov/29505581/) includes direct ATP13A3 experiments despite its ATP13A2-focused title. The human ATP13A3 construct came from DNASU. In HeLa overexpression experiments, ATP13A3 overlapped most strongly with RAB11-positive recycling endosomes, with lesser early and late endosomal pools. N- and C-terminal tags showed comparable localization. The text reports similar patterns in Neuro2a and MEF cells as data not shown. Overexpression may broaden the distribution, so the results do not establish identical endogenous localization in all tissues.

Human ATP13A3 autophosphorylation was observed in four of eight membrane preparations. That variability limited additional hydroxylamine analysis. The stronger Asp-site controls and biochemical measurements on ATP13A1/ATP13A2, and purified yeast Ypk9 experiments, must not be relabeled as ATP13A3 experiments. The architecture, autophosphorylation observation and human WT/D498N cellular phenotype together support the P-type transport mechanism.

Root read selected construct/culture/imaging Methods, ATP13A3 autophosphorylation Results/Figure 3 text, and localization Results/Figure 5 text. The available [PMID:19946888](https://pubmed.ncbi.nlm.nih.gov/19946888/) cache was read completely but contains only an abstract describing YTS membrane proteomics. Its ATP13A3 target entry was not verified. The broad membrane assignment has independent target-specific support from PMID29505581.

### Annotation and ontology distinctions

The current [GO:0015594](https://amigo.geneontology.org/amigo/term/GO:0015594) putrescine term and [GO:0015417](https://amigo.geneontology.org/amigo/term/GO:0015417) polyamine term descend from [ABC-type transporter activity, GO:0140359](https://amigo.geneontology.org/amigo/term/GO:0140359). The ancestor definition specifies ABC architecture. A reaction mentioning ATP and putrescine does not make the P5B-type ATP13A3 an ABC transporter. The substrate-transport evidence can be retained while replacing that mechanistic classification. This is an objection to the current ontology mapping, not a claim that the experiment was on the wrong gene.

[P-type ion transporter activity, GO:0015662](https://amigo.geneontology.org/amigo/term/GO:0015662), has a broader ion target and is not restricted to single-atom ions. Transport of charged polyamines is compatible with that term. Conversely, [GO:0019829](https://amigo.geneontology.org/amigo/term/GO:0019829) has explicit monoatomic-cation ancestors. ATP13A3 polyamine uptake does not establish monoatomic substrate specificity; the linked electronic process GO:0098655 inherits the same problem. ATP13A2 potassium-associated experiments cannot serve as direct ATP13A3 evidence. These distinctions do not imply that every possible additional ATP13A3 substrate has been excluded experimentally.

The local PAINT file records a calcium-homeostasis IBD at PTN000643505, dated 20170228, and separate later polyamine and endosomal assertions. The full phylogeny and node placement have not been reconstructed. A small donor list is not evidence against an IBA, and the target appearing among its own experimental sources is expected. No ATP13A3-specific loss of an ancestral calcium-homeostatic role has been demonstrated here; the calcium assertion therefore remains an explicit uncertainty, outside the concise core.

### Core function and remaining biological questions

One polyamine transport activity accounts for the supported core. ATP binding, ATP hydrolysis and the P-type mechanism are aspects of the same transport cycle. The core uses the existing polyamine transporter activity (GO:0015203), polyamine transmembrane transport process (GO:1902047) and recycling endosome membrane location (GO:0055038). Early and late endosomal pools remain in the reviewed source annotations. No disease process or new annotation is manufactured from necessity evidence, and no second ATPase core is added.

The molecular-function definition was checked in the [FlyBase GO display](https://flybase.org/cgi-bin/cvreport.pl?cvterm=GO%3A0015203&rel=is_a) after AmiGO timed out. The [process](https://amigo.geneontology.org/amigo/term/GO:1902047) and [location](https://amigo.geneontology.org/amigo/term/GO:0055038) definitions and parents were checked in AmiGO. No ATP13A3/Q9H7F0 match was found in the local GO-CAM index; that is not a claim of global absence.

Useful unresolved questions are the purified protein's substrate selectivity and coupling ratio, the compartment-specific flux under endogenous expression, and whether the inherited calcium-homeostasis assertion reflects an additional conserved role. They are questions, not new GO assertions.

### Research provenance

The requested Falcon research attempt with perplexity-lite fallback did not launch either provider because the pinned deep-research-client dependency was unavailable in the offline environment. No provider-named report was authored. Manual primary-source reading and the independent annotation/core consultations are the basis of this review.

Additional orientation reads of PMID35260637 and PMID38626311 were kept separate from the minimum three cached citations. PMID35260637 uses an in-frame ATP13A3 deletion in human L3.6pl cells, not a complete protein-null knockout; its cell-context substrate results and proposed plasma-membrane model should not be generalized into universal substrate exclusion or direct flux. These additional papers are not required evidence for the core presented here.

### Independent all-annotation consultation and final synthesis

The independent annotation consultation covered every one of the 24 original assertions. The final review retains all source fields and both products, with 12 ACCEPT, 8 MODIFY, 3 KEEP_AS_NON_CORE and 1 UNDECIDED decisions. The unresolved row is the calcium-homeostasis IBA. No NEW annotation is added.

The putrescine-specific ABC annotations are refined to [non-ABC putrescine transporter activity, GO:0015489](https://amigo.geneontology.org/amigo/term/GO:0015489), preserving their experimentally supported substrate detail. Root independently checked that term's definition and parents. The monoatomic-cation molecular function is refined to broad P-type ion transporter activity; the existing polyamine term supplies substrate specificity. General nucleotide and membrane terms are refined to more informative existing terms, with explicit independent-source attribution for the abstract-only proteomics reference.

ATP hydrolysis and early endosomal locations are accepted as biochemical and spatial facets of the same transport activity. The single core remains centered on polyamine transport and the predominant recycling-endosomal pool. The lesser late-endosomal distributions are retained as non-core. Neither a second ATPase core nor a product-specific assignment is introduced.


## 2026-09-29 — First-review response

This entry supersedes only the initial choices described here. The broad membrane HDA from PMID19946888 is retained as non-core with explicit curatorial deference; a membrane-proteomics assignment is not refined to an endosomal compartment using another paper. The general electronic membrane inference still uses independent target-specific imaging for its existing refinement. All original source objects and both alternative products remain intact.

The monoatomic-cation molecular-function mapping and its automatic process inference are removed as over-specific electronic classifications. The correct P-type annotation already has the same InterPro evidence, and the polyamine process has its own IBA, so no redundant replacement is proposed. The reviewer-suggested GO:0034220 also specifies monoatomic ions. This is not a claim that all untested additional ATP13A3 substrates are experimentally excluded. Other substrate-preserving ABC-to-non-ABC refinements remain; repeated GO terms with distinct evidence are permitted.

The PAINT export verifies the calcium-homeostasis IBD and its recorded descendant evidence, but does not contain the phylogenetic tree or alignment. A 2017 date, two ATP13A2 donor entries or the absence of a direct ATP13A3 calcium experiment do not establish a bad ancestral placement. The row remains UNDECIDED with explicit source metadata rather than being demoted or accepted solely from donor composition. Its actual placement and retention remain a biological question.

Short exact quotes are allocated to four evidence-bearing source reviews. Together they use 17 words from PMID33310703 and 18 words from PMID29505581, including every occurrence in this draft. The core retains both references and its unchanged biological terms without repeating those quotations. Source descriptions and additional references carry the other supporting context; no target-specific claim is manufactured from a short fragment alone.

PMID33310703's protein-localization statement cites PMID29505581. Its new confocal assay follows BODIPY-putrescine cargo and endosomal markers. It is complementary evidence for the uptake model, not a second independent ATP13A3 protein-localization experiment. Human constructs in hamster CHO hosts, tagged human ATP13A3 localization, variable autophosphorylation and unmeasured purified flux/stoichiometry remain distinguished. The follow-up read the complete PMID19946888 abstract, selected cached localization/autophosphorylation Results in PMID29505581, and selected rescue/endocytosis Results plus relevant Methods in PMID33310703. Figure pixels and complete supplements were not inspected.

Official ontology checks: [P-type ion transporter GO:0015662](https://amigo.geneontology.org/amigo/term/GO:0015662) targets ions and descends from P-type transmembrane transporter activity; [GO:0019829](https://amigo.geneontology.org/amigo/term/GO:0019829) has explicit monoatomic-cation parents; [GO:0034220](https://amigo.geneontology.org/amigo/term/GO:0034220) likewise requires monoatomic ions. The source annotation IDs remain unchanged.

The revised totals are 12 ACCEPT, five MODIFY, four KEEP_AS_NON_CORE, one UNDECIDED and two REMOVE, with one unchanged core and no NEW annotation. Questions and proposed experiments make the unresolved phylogenetic and transport issues explicit. Independent source and PAINT consultations informed the revision. The final source anchors name the observed activity or cellular result; incomplete early/late localization fragments were omitted. Focused validation and rendering follow canonical application.
