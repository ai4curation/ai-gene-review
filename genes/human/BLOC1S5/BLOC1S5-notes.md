# BLOC1S5 (MUTED) review notes

## 2026-10-01 — Initial manual synthesis

MUTED is an integral subunit of the eight-protein BLOC-1 assembly. The most specific established role is support of endosomal membrane-cargo delivery to melanosomes. This is an assembly contribution: the evidence does not identify MUTED as a motor, membrane-spanning transporter, or enzyme. Human MUTED re-expression in muted mouse melanocytes restores other complex subunits, pigmentation and Tyrp1 cargo routing. Its three normal UniProt alternative products remain unchanged; the source annotations do not isolate isoform-specific effects.

The early pallidin study explicitly includes Muted in a heterooligomer and finds reduced pallidin in muted mouse fibroblasts [PMID:12191018, *Pallidin is a component of a multi-protein complex involved in the biogenesis of lysosome-related organelles*]. The endogenous complex study establishes the full BLOC-1 membership through co-immunoprecipitation, fractionation and a two-hybrid network [PMID:15102850]. Reconstitution with eight human proteins includes MUTED, while the two isolated stable trimers exclude it. Whole-octamer association with AP-3 does not resolve an isolated MUTED–AP-3 interface [PMID:22203680]. The normal UniProt entry states, “Component of the BLOC-1 complex” [UniProt:Q8TDH9]. This is the only new verbatim quotation in this draft: six words from this accession, zero new quoted words from the shared publications.

### Cargo sorting, carrier localization and pigment-cell interpretation

The human MuHA construct is a relevant distinction from work on other BLOC-1 subunits. PMID:17182842 uses human HA-tagged MUTED in mutant mouse melanocytes, restores pigmentation and BLOC-1 stability, and follows Tyrp1 delivery and surface cycling. Its text reports the reconstituted complex on tubulovesicular endosomes in MuHA cells (Supplementary Figure S3b/c). This supports the existing carrier association without claiming that every individual complex subunit was separately localized. The supplementary images and captions were not inspected in this review.

Two annotations remain more uncertain. Directed movement of an entire melanosome is different from transport of its membrane cargo: the selected assays resolve the latter. Likewise, pigment recovery in an established melanocyte line does not by itself show regulation of differentiation from an unspecialized cell. The existing experimental GO:0032402 and GO:0050942 assertions are therefore provisionally UNDECIDED, with the original source objects retained. Neither is removed on the basis of an abstract or an uninspected supplement. Official definitions of transport vesicle, pigment-cell differentiation and its positive regulation were read in the saved AmiGO/ontology results.

The 2017 correction to PMID:17182842 is material. The original transferrin-FITC preparation did not contain the expected protein, invalidating that recycling control. Repetition with Alexa488-transferrin supported a mild early recycling defect; the authors retained the central cargo-sorting conclusions [PMID:28137951, PMC5341732, official correction read separately]. The obsolete control is not used as decisive evidence here. The correction is discussed from the saved official primary record; no correction cache was fabricated or fetched in this lane.

### Neuronal evidence

PMID:21998198 is not merely a dysbindin-only source. Selected Results and Figure 1 captions directly include FLAG-muted in human SH-SY5Y cells, and Figure 2 includes muted-null mouse dentate-gyrus PI4KIIalpha depletion. Later localization and trafficking experiments also use other BLOC-1 or AP-3 mutants. Together these support selected neuronal cargo-sorting roles but do not make MUTED an autonomous axonal motor. The existing axonal and synaptic transport inferences are retained as non-core specializations. The detailed mouse-to-human inference remains explicit.

The neurite-extension work in PMID:19546860 tests primary pallid mouse hippocampal neurons. It supports a BLOC-1 assembly role rather than an isolated human MUTED morphogenesis mechanism. Its selected results and discussion were read, and this context supports retaining the existing developmental annotation as non-core.

### Physical associations and unresolved donor annotations

All seventeen generic protein-binding annotations are retained as non-core. The source-specific reasons distinguish older BLOC-1 interaction studies, human binary interactome screens, and AP-MS/multimodal co-complex data. The target partner records are also represented in the normal UniProt interaction section. Exact supplementary pair tables were not independently reproduced, and co-complex association is not described as a resolved direct binary interface. Supported experimental binding is not removed solely because it is generic.

Four mouse-derived electronic annotations — gene expression, swimming behavior, otolith development and microvesicle localization — await a bounded donor-provenance consultation. The provisional UNDECIDED decisions acknowledge this evidence gap. A phenotype need not be a core molecular function, and intracellular small-vesicle fractions must not be confused with extracellular microvesicles. No propagation error, wrong organism or false donor annotation is asserted without the actual evidence.

The IBA annotations are treated as ancestral PAINT inferences, not pairwise transfers. The full family tree was not available for independent reconstruction. Direct MUTED/BLOC-1 evidence is concordant with the retained core claims; neither a short donor list nor the target appearing among its own experimental descendants is treated as weak or circular evidence.

### Human disease corroboration and source limits

The official abstract of PMID:32565547 (*BLOC1S5 pathogenic variants cause a new type of Hermansky-Pudlak syndrome*, DOI:10.1038/s41436-020-0867-5; PMC7529931) reports two unrelated affected individuals, platelet dense-granule deficiency and BLOC-1 destabilization in patient platelets, and defective complementation by a patient deletion construct in muted melanocytes. Official PubMed metadata/abstract and the publisher preview were read. The preview identifies Figure 3 as the platelet complex comparison and Figures 4–5 as rescue/cargo experiments. These figure images and the complete primary paper were not yet inspected. Direct PMC and PubMed page opens returned challenges. This source is useful independent human corroboration, but its normal cache is absent after B3's single DNS-failed fetch (d246f7 to d3e640). It is not a formal review reference or a validated quotation in this draft; no cache or recovery output was fabricated.

Canonical source reading: all eight seed PMID abstracts were read. The caches for PMID:12191018, PMID:15102850, PMID:17182842 and PMID:22203680 are abstract-only. The authenticated Seed55 full-text variants of the latter two were read separately through selected methods/results/discussion, preserving the different canonical bytes. The four large interaction-source bodies were not read in full; their abstracts and assay scope were inspected, without pair-table claims. The additional normal canonical sources PMID:21998198 and PMID:19546860 were read in the selected sections stated above. Figure images were not independently evaluated.

### Provenance and draft boundary

The exact normal seed imported by B3 contains 44 annotations and three alternative products. Every source field, source row and product is preserved in this TMP draft; no new GO annotation is added. All eight seed publication caches already existed with different bytes, and the two family files remain absent. None is overwritten. The normal provider command was attempted once with writable UV cache/tool directories and the documented fallback. It failed before provider execution because the offline dependency deep-research-client[cyberian]==0.2.7rc1 was unavailable (actual 8aa836). No research output was created and the three primary files remained unchanged (67918c). These are manual notes, not provider-generated research.

This draft awaits the donor consultation, independent whole-science review and any separately authorized cache recovery. Later canonical notes must append new entries rather than rewrite this journal. Canonical application, history and publication have not been performed by this preparation.

### 2026-10-01 — Multimodal-map correction checked

The official Nature publisher correction to PMID:40205054 (PMID:41039152; DOI:10.1038/s41586-025-09648-x) was read after the source assessment flagged it. It corrects a duplicated loss-function equation and its x/y notation. The notice does not identify a change to the BLOC-1 interaction records. The original protein-association annotations remain non-core; this correction does not turn them into evidence for a distinct MUTED molecular mechanism. No additional quotation or cache was created. The pre-notice draft is preserved in TMP.

### 2026-10-01 — Preliminary focused validation

The TMP draft passed normal schema, ontology-term and reference validation (5d22dd to ad8637, exit 0). All 17 warnings concern retained generic protein-binding rows; the user's action definitions support keeping established physical associations as non-core when no evidence-backed finer molecular function is established. TMP GOA lookup was disabled, with all 44 complete source objects and three products separately checked equal to the canonical normal seed. The canonical primary files and ten cited normal publication caches were observed unchanged afterward. This is a preliminary check; donor consultation and independently reviewed final integration remain pending.

### 2026-10-01 — Quote-count clarification

The short UniProt snippet counted above as six words contains five whitespace-delimited words. Counting its occurrence in both findings and notes conservatively gives ten words from this accession, below the source budget. The quoted text is unchanged; no new publication quotation was added.


## Mouse donor reassessment, 2026-10-01

The bounded independent consultation and the owner's reread resolve two of the earlier pending donor questions. Rows 37 (swimming behavior) and 41 (otolith development) are retained as noncore consequences inferred from mouse MUTED, while rows 20 (gene expression) and 44 (microvesicle) remain undecided. These decisions supersede the earlier four-row pending status; all 44 source objects and all three `alternative_products` remain exact.

The [official MGI muted genotype record](https://www.informatics.jax.org/allele/genoview/MGI:3587678) assigns variable swimming impairment to J:89392 and otolith abnormalities to J:89392/J:5145. The complete [2004 primary abstract via MouseMine](https://www.mousemine.org/mousemine/report.do?id=74011257) includes muted mice among the vestibular and swimming comparisons; it supports a phenotype, not a direct locomotor mechanism or uniform inability to swim. The selected [1969 publisher description](https://doi.org/10.1017/S0016672300002007) documents variable otolith loss in muted homozygotes. The [MGI comparative GO graph](https://www.informatics.jax.org/homology/GOGraph/Bloc1s5) was generated in March 2023 and supplies historical otolith-morphogenesis provenance, not the current exact developmental GO transfer. No complete 1969/2004 paper, figure images, or current donor GO graph is claimed as read.

The current gene-expression donor experiment remains unverified. For microvesicle, the official GO definition is extracellular, while the PC12 preparation in canonical PMID:21998198 starts with cell homogenization. The latter cannot establish extracellular release, but it also does not identify the curator's actual source; no misattribution or REMOVE is inferred. No new formal citation, NEW annotation, core function or publication quotation is introduced by this reassessment. The existing own-UniProt snippet is five words, conservatively ten across its two occurrences; its wording is unchanged. The normal PMID:32565547 cache remains pending separate recovery, so this is still a TMP proposal and the earlier preliminary validation is not represented as validation of these revised bytes.


## Final normal-source integration, 2026-10-01

The separately verified Source100 create-only import and postverification now provide the exact normal XML cache for [PMID:32565547](https://pubmed.ncbi.nlm.nih.gov/32565547/). This dated entry supersedes the pending-cache and donor-consult statements above. The earlier statements describe the evidence available at those stages; they are preserved as journal history.

The complete abstract and selected Methods, Results and Discussion paragraphs were read from the recovered normal text. Patient 1 platelet lysates show reduction or absence of pallidin and dysbindin. Available antibodies did not detect a specific MUTED band even in control platelets, so this is evidence for complex destabilization rather than a direct measurement of absent MUTED protein. The two patients had platelet dense-granule deficits and bleeding phenotypes; the second patient's frameshift allele was not tested in complementation experiments.

The mechanistic rescue assay uses HA-tagged human constructs in muted mouse melanocytes. Full-length wild-type and donor202 constructs restore BLOC-1 subunit stability, pigmentation and TYRP1 distribution relative to the transferrin receptor, whereas patientdel1/del2 and the truncated control205 construct do not. Selected Results referring to Figures 4–5 were read; the actual figure images and supplementary experiments were not independently inspected. These experiments support the existing BLOC-1 assembly and endosomal cargo-sorting core. They do not resolve directed movement of whole melanosomes or pigment-cell differentiation, so rows 31 and 42 remain undecided. No new GO assertion is added, and transcript-construct experiments do not authorize rewriting the three original UniProt alternative_products.

All 44 original source objects remain exact: eleven ACCEPT, twenty-nine KEEP_AS_NON_CORE and four UNDECIDED decisions, one core function and zero NEW rows. The donor consultation already resolved swimming behavior and otolith development as noncore; gene-expression and extracellular-microvesicle donor assays remain unresolved. The seventeen generic protein-binding annotations remain noncore under the user's action definitions. The two new short supporting snippets occur only in the proposed YAML and total thirteen words from PMID:32565547; the previous UniProt snippet remains five words, conservatively ten across its two occurrences. No provider-generated file, source cache, canonical review or notes were authored by this TMP integration. Focused validation and the independent science decision are recorded separately before any canonical application.


## Axon-cytoplasm evidence reassessment, 2026-10-01

This dated reassessment supersedes only the earlier decision to retain row 43, GO:1904115 axon cytoplasm, as noncore. The combined electronic source uses the process terms axonal transport and synaptic vesicle transport. Independent selected reading of the canonical PMID:21998198 Results and captions (lines 92, 96, 98, 128 and 130) and Discussion (line 136) distinguishes Muted-containing complexes in human SH-SY5Y extracts and cargo depletion in muted-null mouse neuropil from localization of MUTED itself. The paper identifies the cell body as the most upstream sorting site. Its positive discussion of BLOC-1 subunits in axons supports the general neuronal context, but the selected evidence does not identify MUTED-specific occupancy of axon cytoplasm. Figure images and earlier studies cited by that paragraph were not newly assessed. No absence from axons is inferred.

Row 43 is therefore UNDECIDED while the existing neuronal transport process decisions remain unchanged. The superseding totals are eleven ACCEPT, twenty-eight KEEP_AS_NON_CORE and five UNDECIDED, with all 44 source objects, three alternative_products, absent products field, one core function and zero NEW annotations preserved. References, supporting snippets and quotation allocations are unchanged; this appendix adds no quotation. The full earlier proposal and its owner record remain unchanged in their original TMP directory.


2026-10-01 — Canonical review completed. Distinct scientific peer d25756 preceded application 78bdb7. Focused schema, GOA, reference and term validation passed (fa52af) with 17 generic-binding non-core advisories under the supplied ActionEnum. Rendering 8f3654 and history validation 6cc22d passed. The page embeds the exact reviewed YAML. All 44 source objects, three alternative products and 13 protected source files are preserved. No successful external research-provider report, complete figure/supplement reading or global validation is claimed.


## First review followup — biological summary and decision rationale, 2026-10-01

MUTED contributes to BLOC-1 assembly, endosomal cargo delivery and melanosome organization. The human-gene rescue in mutant mouse melanocytes restores pigmentation, complex stability and TYRP1 distribution [PMID:17182842; PMID:32565547]. Melanosome organization is now included explicitly in the core-function summary. The general vesicle-mediated transport annotation is refined to the already-supported endosome-to-melanosome transport term; no NEW annotation is introduced. Its structured term-scoping category records this difference in granularity only. The PAINT phylogeny and IBD node were not inspected, and no source-annotation or propagation error is alleged. Restored pigment and cargo delivery do not, by themselves, prove movement of whole melanosomes or acquisition of pigment-cell identity. Those two experimental annotations remain undecided, with their more specific cargo/organization alternatives stated.

The AP-3 result is present in the full text of [PMID:22203680], although its canonical cache contains only the abstract. Selected Results describe recombinant BLOC-1 pulling down endogenous AP-3 from MNT1 and melan-a cells, with GST and GST-AP-2 controls (Figure 1D). The separately retrieved full-text variant was inspected; the original cache remains unchanged. [PMID:21998198] adds Muted-containing neuronal-complex evidence. These results support the intact complex association; they do not identify a binary MUTED–AP-3 binding surface. The suggested attribution error is therefore not adopted.

### Durable action-policy exception for this review

The explicit user-supplied AGENTS.md instruction defines REMOVE as removal when an annotation is likely incorrect based on combined evidence. It defines KEEP_AS_NON_CORE as retaining an annotation while marking it non-core. These explicit definitions take precedence in this task over the annotation-reviewer skill's default to remove uninformative generic protein binding. All 17 existing experimental protein-binding assertions therefore remain KEEP_AS_NON_CORE, with their source partners preserved, because the interactions are supported and no evidence-backed finer MUTED molecular function has been established. Eight describe partners within BLOC-1; the existing complex-membership annotations capture the assembly's biological significance. Redundancy is not treated as evidence that these interactions are false. This is an explicit task-specific override, not a proposed repository-wide generic-binding convention. No MF term is invented from co-complex membership or a binding partner's function.

### Mouse vestibular evidence and remaining uncertainty

The existing canonical abstract for [PMID:15109702, Gravity receptor function in mice with graded otoconial deficiencies] was read and is now a structured reference supporting swimming behavior. It explicitly includes muted mice; the official MGI genotype record attributes the swimming phenotype to the same study through J:89392. The evidence supports an existing non-core vestibular consequence inferred to human, not a human swimming assay or an intrinsic locomotor mechanism. The abstract records adaptation in some mice. Its PubMed metadata lists an erratum in Hearing Research 194:143 (2004); the correction text was not verified, and no assurance about unchanged numerical results is inferred.

The 1969 otolith study is [PMID:5367369, Muted, a new mutant affecting coat colour and otoliths of the mouse, and its position in linkage group XIV; DOI:10.1017/s0016672300002007]. Official PubMed metadata and the publisher's selected first-page description establish the identity and variable mouse otolith loss. PubMed has no indexed abstract. The normal retrieval has now completed through Source105 and its exact 877-byte citation-only cache is imported unchanged. It supplies verified bibliographic metadata, not an indexed abstract or full paper. The formal PMID reference is now attached to the existing otolith-development annotation. The variable otolith-loss assessment continues to rely on the previously read selected publisher first page and independently checked mouse identity; it does not reconstruct the current exact donor-reference edge.

The gene-expression and extracellular-microvesicle donor experiments remain unidentified. A direct QuickGO lookup did not return accessible annotation data. Changes in cargo abundance or expression of MUTED itself do not establish participation in gene expression; intracellular vesicle fractionation does not establish extracellular microvesicle localization. These limits support retaining UNDECIDED while preserving the original donor fields, rather than alleging an unverified propagation error. No unjoined gene-expression paper is added.

### Open mechanisms and review status

The unresolved molecular activity is represented as a knowledge gap, with questions and experiments that distinguish octamer destabilization from a specific cargo-sorting defect. Platelet dense-granule deficiency in HPS11 motivates an isogenic megakaryocyte rescue experiment to resolve the affected cargo-delivery step; a new process annotation is not inferred from the clinical phenotype alone [PMID:32565547].

DRAFT follows the schema definition for a review with no PENDING rows but remaining validation advisories. It does not mean that the 44 source annotations are unreviewed. This provisional followup has ten ACCEPT, one MODIFY, twenty-eight KEEP_AS_NON_CORE and five UNDECIDED decisions, one core function and no NEW rows. All original source fields and three alternative products are preserved. Earlier entries above are historical journal records; their operational identifiers and superseded counts do not describe the current biological conclusions. No source cache or canonical review was edited in preparing this followup.


### Final source integration, 2026-10-01 UTC

PMID5367369 is now a structured reference with the exact normal-cache title and an explicit citation-only reading limit. No abstract or full-text excerpt was manufactured from its title, and no supporting quotation is added: the reviewed first-page observation is cited through the verified reference identifier. The source identifies the 1969 mouse study, not a new human experiment. The whole paper remains uninspected.

This final integration changes no annotation action, source object, core-function assignment or prior reference. The 44 annotations retain ten ACCEPT, one MODIFY, twenty-eight KEEP_AS_NON_CORE and five UNDECIDED decisions; three alternative products, the absent products field and zero NEW annotations are preserved. The previous v2 validation passed with 17 documented generic-binding advisories; no validation of this final integration is claimed yet. Distinct final scientific peer, canonical application, validation, rendering and history remain subsequent steps. No ordinary source fetch was repeated and no cache bytes were edited.


## Follow-up verification

Independent scientific review approved the final follow-up and its source-reading limits. Canonical validation passed with the same 17 generic-binding advisories retained under the supplied action policy. History validation passed, and the rendered HTML reproduces the review YAML. All 44 source assertions and three alternative products remain unchanged; the follow-up has ten ACCEPT, one MODIFY, twenty-eight KEEP_AS_NON_CORE and five UNDECIDED decisions. The two added bibliographic sources were reused unchanged. No new annotation, molecular activity or source-cache edit was introduced.

## Generic binding follow-up - 2026-10-10

The 17 experimental `GO:0005515` rows are now `REMOVE` under the default generic-binding policy. This changes the BLOC-1 assembly-associated rows from PMID:12191018, PMID:15102850, PMID:22203680, PMID:33961781, and PMID:40205054, plus the human binary-interaction rows from PMID:25416956 and PMID:32296183. The source partners and evidence are preserved, and several interactions remain useful support for MUTED-containing BLOC-1, but GO:0005515 itself does not name a specific MUTED molecular activity. Current totals are 10 `ACCEPT`, 11 `KEEP_AS_NON_CORE`, 17 `REMOVE`, 5 `UNDECIDED`, and 1 `MODIFY`.

## Status refresh, 2026-10-10

After the generic-binding rows were switched to `REMOVE`, focused status recomputation reported no
validation warnings and derived `COMPLETE`. The status field is updated from `DRAFT` to `COMPLETE`; earlier
entries that attribute `DRAFT` to retained generic-binding warnings are historical.
