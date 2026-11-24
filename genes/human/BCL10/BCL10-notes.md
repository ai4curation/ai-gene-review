# BCL10 evidence review, 2026-09-30

Research before canonical import used the authenticated Seed46 archive (`8fa1efcff2c9694bbdd924c9b33898993adeafbdae3ebefd11a38bd77f34c7d7`). This is a reviewer log, not a generated provider report. No source cache was edited.

All 58 normally fetched PMID records were inspected at the abstract/metadata level (1040062 has no abstract): initial batches cf5830/d12b10, then e369db, b00e0b, 1ac036, dee841, bc5f01. The full 178 source assertion tuples were read as 876e14. Source assertions include two contributes_to kinase-activator entries; preserve those qualifiers. Source products and alternative_products are null, not an invented isoform list.

PMID:24074955, *Structural architecture of the CARMA1/Bcl10/MALT1 signalosome: nucleation-induced filamentous assembly*: selected complete Results and Methods paragraphs 11–13,20–22,43–44,47,50,64 read as 43e9ee. Human recombinant CARD11/BCL10 forms CARD filaments; the reconstituted ternary complex incorporates MALT1, enhances MALT1 activity, and filament-interface mutations impair NF-kappaB signaling. Endogenous HBL-1 immunoprecipitates also contain CBM components with filamentous morphology. This supports BCL10 as a signaling adaptor, not an enzyme. The initial overly broad display 8548d6 was truncated and is not a full-text read claim.

PMID:28628108, *Germline hypomorphic CARD11 mutations in severe atopic disease*: selected complete Results and Methods paragraphs 15,71 read as 43e9ee. BCL10 co-immunoprecipitation directly assays mutant-dependent impairment of CARD11/MALT1 assembly in human T-cell lines. The CARD11-focused title is not a reason to reject BCL10 complex membership.

PMID:25365219, *Inherited BCL10 deficiency impairs hematopoietic and nonhematopoietic immunity*: primary JCI Results/captions previously read at lines331–394. The BCL10-deficient patient has strong lymphocyte and fibroblast defects, while tested myeloid cytokine responses are preserved. Human innate dependence is cell-type specific; do not describe universal dependence of all human innate responses on BCL10.

PMID:15125833, *The TRAF6 ubiquitin ligase and TAK1 kinase mediate IKK activation by BCL10 and MALT1 in T lymphocytes*: abstract explicitly describes purified biochemical reconstitution. Oligomeric BCL10/MALT1 promotes TRAF6/TAK1/IKK activation. Retain contributes_to kinase activator and use signaling adaptor as the principal molecular function.

PMID:15207693, *Characterization of Bcl10 as a potential transcriptional activator that interacts with general transcription factor TFIIB*: normally fetched abstract and independently indexed PubMed source (turn7061search1) describe mammalian Gal4-DBD fusion assays and TFIIB interaction, with activity mapped to the N-terminal13 residues. This supports contextual non-core coactivation/TFIIB binding; it does not establish constitutive sequence-specific DNA binding. No full-paper read claimed.

PMID:16280327, *A pathway for tumor necrosis factor-alpha-induced Bcl10 nuclear translocation*: normal abstract and indexed PubMed identity read. MCF7 TNFalpha induces Akt phosphorylation and BCL3-associated nuclear translocation. The abstract's NF-kappaB-binding site is in BCL10 regulatory DNA; the existing protein-binding annotation needs full-paper verification. DOI full-text open failed; keep uncertainty, do not claim wrong-gene or misattribution from abstract alone.

PMID:22267217, *Dectin-1 is an extracellular pathogen sensor for the induction and processing of IL-1beta via a noncanonical caspase-8 inflammasome*: normal abstract/publisher abstract+figure captions establish CARD9/BCL10/MALT1/caspase8/ASC assembly and IL1B induction/processing. Do not equate caspase8 inflammasome activity with apoptosis without reading the relevant experiment. Publisher full body is restricted. Existing IMP apoptosis should remain unresolved pending evidence, rather than being removed from its title.

PMID:1040062 resolves to *[Nurses replies to expectations of the nursing profession]*, an unrelated nursing article. GOA generic interaction partner Q15628 was independently verified as TRADD. PMID:10400625, *c-E10 is a caspase-recruiting domain-containing protein that interacts with components of death receptors signaling pathway and activates nuclear factor-kappaB*, has independently verified PubMed identity and an abstract explicitly describing TRADD co-precipitation (turn7060search0). Preserve original_reference_id1040062, record a formal reference replacement10400625, and use that paper under its own identifier as support. This correction follows content, not simply a guessed missing digit.

PMID:19593445, *Expression of the Bcl-2 protein BAD promotes prostate cancer growth*: full unique narrative Introduction, Methods, Results, figure captions and Discussion read as9a19eb; raw text search79ddfe found no BCL10, Bcl-10, mechanical or stress mentions. Experiments manipulate BAD in prostate cancer cells and mouse xenografts. This paper does not substantiate BCL10's mechanical-stimulus IEP; no intended replacement established. Flag the citation as MISCITED and the process as UNDECIDED rather than claiming the biological process is disproven.

PMID:23264731 has a MTR120-focused abstract and normally cached full text unavailable. PMC open returned a browser challenge. Cytoplasmic microtubule localization therefore requires target-specific evidence inspection; do not infer wrong-gene annotation from the title. Similar caution applies to CARD8-focused PMID11821383.

The IPI screen papers25416956,25910212,27107012,32296183,33961781,40205054 were read at abstract level. Preserve curated partner assertions as non-core when supported by the source record; do not claim supplementary pairs, constructs or isoforms were independently reproduced. PMID27071417 provides explicit BCL10/MALT1-dependent CARD14 signaling; CARD14-1 and CARD14-2 are partner isoforms, not BCL10 isoforms.

GO:0035591 current official definition and parentage verified at AmiGO (turn7061search0): signaling adaptor is a child of protein-macromolecule adaptor. Refine the existing broad adaptor assertion to this specific existing term; no NEW term is needed. GO:0038061 current definition explicitly requires NIK/IKKalpha/p100→p52 processing (turn7062view3), which is not interchangeable with general CBM-driven canonical signaling. GO:0071260 definition checked (turn7062view1). NF-kappaB-binding and apoptotic-signaling official opens failed in that batch; no substituted unofficial term definition used.

No new quotations have yet been committed for this gene. No full PAINT tree/node placement review has been performed; target in WITH/FROM is valid descendant evidence, not circularity. Existing GO-CAM65d7e4ac00000022 models BCL10 as adaptor, consistent with the central molecular role. No new process proposal is justified by absence alone.


## Retained cache comparison and focused consultation

The canonical source import is complete. All 58 PMID titles and 30 Reactome records agree with the draft's declared identities. Five publication availability flags differ from the archived candidates and were corrected to the retained normal caches: PMID21157432, PMID22528498, PMID23264731, PMID27071417 and PMID28628108. Full-text availability is not a claim that a complete paper was supplied or read: the retained 22528498 and 23264731 bodies contain Introduction and Discussion after the abstract. The BCL10-specific microtubule image/list in 23264731 remains uninspected.

The independent 13-assertion consultation was integrated without changing actions. It identifies actual BCL10 comparator experiments in the CARD8 paper, the ORFeome screen in the MTR120 paper, and the distinction between NF-kappaB binding to regulatory DNA and an unresolved BCL10/protein interaction. The original incorrectly indexed nursing citation remains preserved with its independently verified reference replacement. The BAD/prostate-cancer mechanical-stimulus mismatch remains MISCITED and the biological assertion UNDECIDED.

The 13-word PMID15125833 quote now preserves the canonical cache's literal space before its line break. No new quoted words or annotations were added. The remaining new primary citation PMID19897484 is awaiting the one normal recovery job; no canonical review application or final validation is claimed here.


## Independent whole-review correction

The high-throughput reporter qualification is now limited to the PMID12761501 assertion; it has been removed from six adjacent mechanistic or orthology rows. Actions and all original source objects are unchanged. PMID17287217 is added as source-only support for the membrane-raft core location: its complete normal abstract reports recruitment of the CD26/CARMA1/BCL10/IKK complex to lipid rafts after CD26 ligation. No new quote or annotation is introduced. Final PMID19897484 normal-cache integration remains pending.


## Normal PMID19897484 source reassessment

The authenticated normal source contains HTML-derived full text (PMCID PMC2804200; DOI 10.1074/jbc.M109.050815). The complete cached abstract, Introduction, Experimental Procedures, Results and Discussion were read; this does not include visual inspection of the figures or supplements. BCL10 siRNA reduced carrageenan-induced nuclear p52/RelB responses in human NCM460 cells and mouse embryonic fibroblasts. Reduced NIK phosphorylation supports an upstream requirement in that stimulus context and does not establish BCL10 as the phosphorylating enzyme. Row135 remains non-core, now with a formal supplemental reference and source link. No source object, action, core, product or supporting quotation changed. Canonical application remains conditional on exclusive import of the exact normal cache bytes.


## Final integration and validation, 2026-10-01 UTC

The exact normal PMID19897484 record is now imported and verified; the source-import condition above is closed. All 178 distinct source assertions from 180 raw GOA rows remain intact, including qualifiers and supporting entities. The complete review passes focused validation, rendering and history validation. Fifty-one advisories concern supported generic protein interactions retained as non-core under the supplied action definitions. One advisory concerns missing structured propagation metadata for an unresolved IBA; the donor/node evidence was not reconstructed and no failure cause is invented. The seven explicit UNDECIDED decisions remain visible. No new global validation pass or whole-paper coverage beyond the recorded reading scopes is claimed.


## Focused first follow-up: specific binding and evidence scope

Eight generic binding assertions are refined where the identified partner and source context support a more informative term: CARD9, CARD10, CARD11 and CARD14 contacts become CARD domain binding; the AKT1 assertion becomes protein kinase B binding; one MALT1 assertion becomes protease binding. These are refinements of existing source assertions, not new annotations. The original accessions are preserved: Q9BXL6 is CARD14 and Q9BXL7 is CARD11. Other supported generic interactions retain the established non-core policy rather than being removed by a blanket rule.

The CARD refinements are grounded in [PMID:11053425](https://pubmed.ncbi.nlm.nih.gov/11053425/), [PMID:11259443](https://pubmed.ncbi.nlm.nih.gov/11259443/), [PMID:11278692](https://pubmed.ncbi.nlm.nih.gov/11278692/) and selected human-protein/engineered-cell experiments in [PMID:31296852](https://pubmed.ncbi.nlm.nih.gov/31296852/). The [AKT1 paper](https://pubmed.ncbi.nlm.nih.gov/16280327/) concerns phosphorylation and localization of BCL10 in TNFalpha-treated MCF7 cells; it does not make BCL10 an AKT activator. The MALT1 refinement preserves the curated IPI interaction in [PMID:14695475](https://pubmed.ncbi.nlm.nih.gov/14695475/) and uses independently read CBM reconstitution in [PMID:24074955](https://pubmed.ncbi.nlm.nih.gov/24074955/) as corroboration. The original abstract alone was not treated as a new pairwise interaction assay.

Short exact anchors now accompany the four earlier MODIFY decisions, the eight binding refinements, and selected core ACCEPT decisions. They remain tied to explicit assay descriptions: the reporter-screen anchor in [PMID:12761501](https://pubmed.ncbi.nlm.nih.gov/12761501/) establishes assay scope, not independent inspection of a BCL10-specific screen entry. The [CARD11-variant abstract](https://pubmed.ncbi.nlm.nih.gov/28628108/) does not expose its BCL10 complex assay; the retained CBM membership has independent direct support. Existing quotations are unchanged; aggregate quotation counts include repeated snippets and remain at most 25 words per source.

The kinase-activator IDA and IBA retain their original contributes_to qualifiers. [PMID:15125833](https://pubmed.ncbi.nlm.nih.gov/15125833/) supports an oligomeric BCL10/MALT1 signaling assembly, and [PMID:18287044](https://pubmed.ncbi.nlm.nih.gov/18287044/) distinguishes CBM formation from ubiquitin-dependent NEMO recruitment. The core remains signaling-adaptor activity: the available experiments do not require an additional authored assertion that BCL10 itself binds a kinase as an activator. This does not reject the curator-qualified complex contribution. MALT1, ubiquitin enzymes and kinases retain their own catalytic roles. BCL10's positive pathway role follows its assembling platform, not necessity or ubiquitination alone.

The normal cache abstracts were read completely for the fourteen abstract-only sources considered in this follow-up; four full-text caches were consulted in the selected Results/Methods/Discussion scope recorded in the proposal. No figures or supplementary files were visually reviewed. [PMID:11163238](https://pubmed.ncbi.nlm.nih.gov/11163238/) is now explicitly recognized as high-relevance foundational mouse evidence. All 178 source objects, products, core terms and seven unresolved decisions are preserved. No new process annotation or reconstructed PAINT failure mechanism is introduced.


The follow-up passed independent science review, focused gene validation, rendering and history validation. Validation retained 43 retained generic-binding policy warnings and one unchanged unresolved-IBA metadata advisory; these are documented unresolved issues, not a claim of warning-free review. No full-repository validation was run.


## Binding follow-up, 2026-10-01 UTC

Twenty-six additional generic interaction assertions now have an evidence-backed specific refinement: eight CARD11, three CARD9, two CARD14 partner-isoform, one viral E10 and one CLAN/NLRC4 association become CARD domain binding; eleven MALT1 associations become protease binding. These are refinements of existing curated interactions. All 178 source assertions from 180 raw GOA rows, their qualifiers and supporting entities, products, all seven unresolved decisions, and the signaling-adaptor core remain unchanged. No new annotation is proposed. The action totals are 80 ACCEPT, 53 KEEP_AS_NON_CORE, 38 MODIFY and 7 UNDECIDED; seventeen generic binding assertions retain the established non-core policy where a more specific assignment was not established.

The reciprocal CARD contact is explicit for viral E10 and CLAN in the complete [PMID:10187771](https://pubmed.ncbi.nlm.nih.gov/10187771/) and [PMID:11472070](https://pubmed.ncbi.nlm.nih.gov/11472070/) abstracts. For CARD9 and CARD11, independently read human recombinant templating experiments in [PMID:31296852](https://pubmed.ncbi.nlm.nih.gov/31296852/) corroborate the interface separately from the original curated partner assertions. These experiments use defined CARD-containing constructs and include engineered yeast nucleation assays; they do not imply that every full-length conformational state binds equally. The original [CaMKII study](https://pubmed.ncbi.nlm.nih.gov/16809782/) used human CARMA1 with mouse Bcl10 cDNA in the selected Methods. The [PKCdelta study](https://pubmed.ncbi.nlm.nih.gov/22528498/) distinguishes inhibition of MALT1-TRAF6 recruitment from preserved CARD11-BCL10/MALT1 association.

The CARD14 refinements combine the reciprocal CARD interface in [PMID:11278692](https://pubmed.ncbi.nlm.nih.gov/11278692/) with the curated mutant-context associations in [PMID:27071417](https://pubmed.ncbi.nlm.nih.gov/27071417/). Official [UniProt Q9BXL6](https://www.uniprot.org/uniprotkb/Q9BXL6/entry) places its CARD at residues 15-107; the annotated partner isoform 2 lacks residues 741-1004 and retains that domain. It is not the cardless isoform 3. These remain partner-isoform supporting entities, not BCL10 isoform annotations. The exact original isoform-specific construct assays were not independently inspected.

For MALT1, selected human recombinant CBM assembly and activation experiments in [PMID:24074955](https://pubmed.ncbi.nlm.nih.gov/24074955/) corroborate recognition of a protease partner. This does not give BCL10 MALT1's catalytic activity. The exact supplementary pairs in the human interactome [PMID:25416956](https://pubmed.ncbi.nlm.nih.gov/25416956/), glioma [PMID:31774199](https://pubmed.ncbi.nlm.nih.gov/31774199/), BioPlex [PMID:33961781](https://pubmed.ncbi.nlm.nih.gov/33961781/) and U2OS [PMID:40205054](https://pubmed.ncbi.nlm.nih.gov/40205054/) sources remain uninspected. Their curated associations and original experimental contexts are preserved, while independent domain or partner evidence is cited separately; affinity purification is not recast as a new binary-affinity measurement.

The official GO definitions and parents place [CARD domain binding](https://amigo.geneontology.org/amigo/term/GO:0050700) under protein domain specific binding and [protease binding](https://amigo.geneontology.org/amigo/term/GO:0002020) under enzyme binding. They describe recognition of a domain or enzyme, not acquisition of the partner's catalytic function. No new process claim or PAINT failure mechanism is introduced.

The current formal reference list contains 59 PMIDs; the earlier 58-reference count and no-new-quotation statements describe historical stages and are superseded by the integrated normal cache and subsequent follow-ups. The CARD14 complex anchor now states the mutant association instead of naming only the two partners. Three short PMID24074955 excerpts are consolidated into one structural Results anchor while preserving the CBM-membership and reporter-assay source links, experimental descriptions, and existing core activity excerpt. Aggregate quoted words, including repeated excerpts, stay at most 25 per source; this is an authoring constraint, not a claim about a repository validator limit.

This follow-up independently read nineteen complete cached abstracts and selected Results, Discussion and Methods passages from six full-text caches. The source-specific limits are stated in the affected reasons. No figure images or supplementary files were inspected, and no complete-paper or full-review audit is claimed. All source-cache bytes remain unchanged. Independent science review and canonical application/validation are pending at this proposal stage.


Independent science review passed for this binding follow-up, and the exact approved YAML and appended notes have been applied after verifying their canonical preimages. All 178 original source objects, 89 normal reference caches, raw GOA/UniProt files, prior history and the existing core are preserved. Focused validation, rendering and a new history record follow this application.


The binding follow-up passed focused canonical validation, HTML rendering and history validation. The rendered page embeds the exact reviewed YAML. Eighteen advisories remain: seventeen retained generic-binding decisions under the supplied action definitions and one unchanged unresolved IBA propagation-metadata advisory. No failure mechanism was invented and no full-repository validation is claimed. All normal source caches, raw GOA/UniProt bytes and prior history remain unchanged.


## Partner-class follow-up, 2026-10-01 UTC

Ten additional generic-binding reviews are refined using their source partners and available evidence: UBE2N/UBC13 to ubiquitin conjugating enzyme binding; IRAK1 and CAMK2A to protein kinase binding; the colorectal-screen AKT1 row to protein kinase B binding; PKCzeta to protein kinase C binding; and five TRAF2 rows to ubiquitin protein ligase binding. These identify binding partner classes without transferring catalysis, asserting purified direct affinity, or changing original source identifiers and isoforms. Kinase-substrate cases retain BCL10 as substrate. The UBC13 association comes from the curated IPI record, not merely from pathway necessity.

TRAF2 E3 activity is supported by cofactor-dependent biochemical experiments in [PMID:20577214](https://pubmed.ncbi.nlm.nih.gov/20577214/) and by a separate MLST8 substrate context in [PMID:28489822](https://pubmed.ncbi.nlm.nih.gov/28489822/). Earlier negative results in [PMID:19810754](https://pubmed.ncbi.nlm.nih.gov/19810754/) concern the tested biochemical conditions. GO:0031625 identifies an E3 binding partner; it does not require catalysis in the original BCL10 interaction experiment. An initial TMP draft imposed that unnecessary requirement; independent review identified the error and this proposal corrects it. Source-specific variant, screen, construct and coassociation limits remain explicit. No E3 activity or activation of TRAF2 is assigned to BCL10. The existing cIAP2 annotation has separate partner provenance and does not exclude the same binding class for TRAF2.

Generic TRADD, BCL3, NEMO and COG6 associations retain non-core decisions under the supplied ActionEnum. A missing informative replacement does not establish that an experimental association is false. Current totals are 80 ACCEPT, 43 KEEP_AS_NON_CORE, 48 MODIFY and 7 UNDECIDED over 178 source rows, with seven generic-binding advisories. No NEW annotation or core function is added. The formal PMID count is 62. Existing quotes and the prior PMID:24074955 assessment are unchanged. Earlier note hashes and search-turn strings are internal execution artifacts, not public source identifiers; PubMed links and cached publications supply scientific references. Historical notes remain append-only.

Follow-up reading covered complete abstracts of PMID:11466612, 14695475, 16831874, 17052756, 25011391, 16280327, 24412244, 19810754, 20577214 and 28489822. Selected primary passages were read from 19810754 (paragraphs 49, 50, 53, 55), 20577214 (14–16) and 28489822 (12–17). Original images, full supplements and constructs were not newly audited. All three added reference caches already exist and are reused unchanged. Official AmiGO pages confirm the kinase and E3 binding terms; GO:0031624's label occurs in the local ontology and official GO:0044390 parent hierarchy, while direct access to its own page timed out. This corrected TMP proposal awaits independent peer review and canonical validation.


This follow-up passed independent science review (875943), focused gene validation (74e36d), rendering (f65ecc) and generated-history validation (3c85f0). These checks close the pending validation described above. Seven generic-binding advisories and one unchanged unresolved-IBA metadata advisory remain; no full-repository validation or warning-free claim is made.


## Evidence-context follow-up, 2026-10-01 UTC

The negative [TRAF2 RING study](https://pubmed.ncbi.nlm.nih.gov/19810754/) is removed from the positive supported_by lists of the five TRAF2-binding refinements. It remains in their additional_reference_ids and contextual reasons. Its tested lack of E2 engagement/activity is not erased or labeled universally overturned. The positive [S1P-dependent biochemical study](https://pubmed.ncbi.nlm.nih.gov/20577214/) and the separate [MLST8 substrate study](https://pubmed.ncbi.nlm.nih.gov/28489822/) remain supporting evidence for the partner class. The binding annotation does not require the original BCL10 interaction assay to measure the partner's catalytic activity. For the four screen-derived TRAF2 records, the original curator-assigned partner identity is retained and the enzyme-class evidence is supplied separately; this does not claim new inspection of each screen pair, mutant construct or endogenous interaction.

The S1P paper's reference review is now DISPUTED for the scope of its cellular SPHK1-dependence claim. A [later primary mouse knockout study](https://pmc.ncbi.nlm.nih.gov/articles/PMC4769158/) reports TNF responses in Sphk1-deficient fibroblasts and keratinocytes that remain impaired after Traf2 deletion. The read abstract and selected Results challenge a general cellular SPHK1 requirement; they do not directly repeat or refute the purified S1P-dependent TRAF2 reaction. This external primary source is linked as context only: its normal cache is absent, no source fetch occurred, and the formal PMID list stays at 62 (99 references overall). No formal superseding finding is invented from experiments performed under different conditions. The original assay details and the separate MLST8 evidence remain relevant to the E3 partner classification.

The three NEMO reasons now describe actual experiments. [The CARMA1 study](https://pubmed.ncbi.nlm.nih.gov/17363905/) detects endogenous NEMO coassociation with BCL10 after stimulation of CARMA1-reconstituted cells. [The Jurkat study](https://pubmed.ncbi.nlm.nih.gov/18287044/) shows pull-down and co-IP of ubiquitinated BCL10 and loss of association with the NEMO L329P ubiquitin-binding mutant. [The ABC DLBCL study](https://pubmed.ncbi.nlm.nih.gov/27070702/) similarly co-immunoprecipitates modified BCL10 with WT but not L329P NEMO. NEMO reads the attached ubiquitin chains; BCL10 provides the modified recruitment platform. The retained generic IPI describes that measured association, not a newly asserted BCL10 ubiquitin-recognition activity or unmodified-polypeptide interface. These source-specific limits support non-core retention and do not supply evidence that the reported association is false.

The TRADD and BCL3 contacts are explicitly reported in their original/corrected abstracts; lack of a new enzyme-class term does not make them unverified interactions. COG6 remains a curator-recorded screen association with no independently reconstructed pair-level supplementary result and no inferred Golgi role. The supplied ActionEnum is applied consistently to these seven records; they are not removed solely because a generic-binding policy advisory persists. A missing Golgi-function claim is not negative evidence for a physical interaction.

Short normal-cache anchors now accompany the BCL3 and three NEMO association reviews, and the earlier IRAK1, CaMKII and PKCzeta refinements. The kinase anchors preserve their original limits: recruitment, substrate phosphorylation, or proximity/complex evidence is not relabeled as purified binary affinity. Existing quotations are unchanged, with newly added snippets counted against the full per-source aggregate. All totals remain at most 25 words per source, including repeated occurrences; this is an authoring constraint rather than a repository validator rule.

This finite follow-up independently read thirteen complete normal abstracts, selected Results/Discussion/Methods from six full-text caches, and the specified external primary mouse study portions. Figure images, supplements and exact high-throughput pair datasets were not inspected. All 178 original source objects, products-as-seeded, actions, one core and 99 formal references (62 PMIDs) remain preserved. Earlier internal check identifiers in this append-only journal are execution provenance, not public scientific citations; the linked papers identify the science. No canonical review, source cache or history has been changed at this proposal stage.

Focused temporary validation passed with 16 advisories: seven retained generic-binding policy warnings, one unchanged IBA propagation-metadata warning, and eight unchanged ACCEPT records without supported_by. Term, schema and supporting-text checks passed. Canonical source equality was checked separately because temporary-path validation used --no-goa.


Independent scientific review passed for this focused follow-up (2026-10-01). The exact approved YAML and appended notes were applied after matching canonical preimages. All 178 source objects, annotation actions, the existing core, 99 formal references, raw sources, normal caches and previous history remain unchanged. Five negative TRAF2 entries were removed from positive support; seven brief anchors and three NEMO assay explanations were added. The cellular SPHK1 dispute is scoped separately from purified S1P-dependent TRAF2 activity. Canonical validation, rendering and a generated history record follow.


Focused canonical validation, HTML rendering and history validation passed (2026-10-01). The rendered page embeds the exact approved YAML. The canonical validator reports seven retained generic-binding advisories and one unchanged IBA propagation-metadata advisory; the temporary proposal check also disclosed eight unchanged ACCEPT records without short evidence anchors. All normal sources and prior history remain unchanged. No full-repository validation is claimed.

## Generic-binding policy cleanup, 2026-10-05 UTC

This cleanup supersedes the earlier retention rationale for the final seven GO:0005515 rows. The corrected TRADD and BCL3 interactions and both COG6 screen associations are now REMOVE: they preserve the original source object and partner accession but remove the uninformative generic term when no evidence-backed replacement molecular function is available. The three NEMO rows are now UNDECIDED because the inspected experiments detect CARMA1-dependent coassociation or NEMO recognition of ubiquitinated BCL10, but they do not establish a direct unmodified-polypeptide BCL10-NEMO binding activity.

No source assertion, qualifier, evidence code, product, or supporting entity was removed. The final existing-annotation action totals are 80 ACCEPT, 48 MODIFY, 36 KEEP_AS_NON_CORE, 10 UNDECIDED and 4 REMOVE across 178 source rows; no GO:0005515 row remains at KEEP_AS_NON_CORE. The short TRADD and BCL3 anchors were extended to the surrounding cached abstract clauses so the rendered evidence snippets identify their subjects.


## Source-specific binding follow-up, 2026-10-09 UTC

This entry supersedes the 2026-10-05 generic-binding cleanup for seven source rows. The governing authority is the explicit user instruction published in the [CLINGEN_MENDELIAN project at immutable main revision f7dc8b60](https://github.com/ai4curation/ai-gene-review/blob/f7dc8b60bf8be80744f75955c3c1a3c16bd73888/projects/CLINGEN_MENDELIAN.md#curation-instructions): retain a supported, biologically correct `GO:0005515` (protein binding) annotation as `KEEP_AS_NON_CORE` when no evidence-backed, more specific replacement has been established. The earlier ActionEnum-only authority and blanket removal rationale are superseded. This instruction does not establish an unverified interaction or justify a more specific molecular function without evidence.

The corrected [TRADD source PMID:10400625](https://pubmed.ncbi.nlm.nih.gov/10400625/) explicitly reports BCL10/c-E10 co-precipitation with TRADD. The original erroneous PMID:1040062 and its formal reference replacement remain intact. The complete [PMID:16280327 abstract](https://pubmed.ncbi.nlm.nih.gov/16280327/) supports BCL3 association after BCL10 phosphorylation in the TNFalpha/MCF7 nuclear-translocation context. These two supported associations return from REMOVE to KEEP_AS_NON_CORE; neither supplies a supported narrower BCL10 molecular function. Access for these judgments was the complete normal cached abstracts, not a new full-article or figure audit.

Both COG6 source rows also return from REMOVE to KEEP_AS_NON_CORE after exact pair-level verification. For [PMID:27107012](https://pubmed.ncbi.nlm.nih.gov/27107012/), human O95999-Q9Y2V7 records EBI-11773232/IM-25015-675 and EBI-11781927/IM-25015-1582 identify barcode-fusion and validated two-hybrid assays with Table EV2/figure provenance. For [PMID:32296183](https://pubmed.ncbi.nlm.nih.gov/32296183/), EBI-23098775/IM-25472-43058, EBI-24457201/IM-25472-128838 and EBI-24966990/IM-25472-18194 identify two-hybrid array, validated two-hybrid and prey-pooling assays, each citing Supplementary Table 9. These [IntAct source records](https://www.ebi.ac.uk/intact/search?query=O95999%20AND%20Q9Y2V7) establish the target/partner/publication/method linkage. They share provenance with GOA and are not independent experimental replication. Original screen images, all controls and full supplements were not newly audited. No Golgi function or endogenous mammalian complex is inferred.

The three NEMO rows move from UNDECIDED to KEEP_AS_NON_CORE because the selected primary Results directly resolve the annotated low-resolution associations. [PMID:17363905, Figure 2C Results](https://pmc.ncbi.nlm.nih.gov/articles/PMC1847656/) immunoprecipitate endogenous NEMO and detect BCL10/CARMA1 association in stimulated CARMA1-reconstituted cells. [PMID:18287044, Figure 2D/E and Figure 3 Results](https://pmc.ncbi.nlm.nih.gov/articles/PMC2268578/) detect ubiquitinated BCL10 by GST-NEMO pull-down and endogenous co-IP in stimulated Jurkat cells, with loss for NEMO L329P. [PMID:27070702, Figure 4 Results](https://pmc.ncbi.nlm.nih.gov/articles/PMC6026033/) detect modified BCL10-NEMO association in ABC DLBCL and distinguish WT from L329P NEMO in HBL1 cells. These are target-specific BCL10 association assays, not isolated ubiquitin experiments or pathway membership alone. NEMO recognizes attached ubiquitin; BCL10 supplies the modified recruitment platform. No intrinsic ubiquitin-binding activity, kinase activity, E3 activity, purified binary affinity or unmodified-polypeptide interface is assigned to BCL10. The [current GO:0005515 definition](https://www.ebi.ac.uk/QuickGO/term/GO:0005515) does not impose the previous unmodified-polypeptide requirement. Access was selected Results from the unchanged full-text caches; figure pixels, complete Methods and supplements were not newly inspected.

Only these seven reviews and two of their short source anchors change. The TRADD anchor is shortened from 16 to 3 words and the BCL3 anchor from 9 to 5, leaving their subjects and experimental contexts explicit in the surrounding reasons. Other duplicated occurrences are preserved; aggregate YAML quotation totals, including repeated snippets, fall from 36 to 23 words for PMID:10400625 and from 29 to 25 for PMID:16280327. No new scientific quotation is added. Current totals are 80 ACCEPT, 48 MODIFY, 43 KEEP_AS_NON_CORE and 7 UNDECIDED across 178 source rows. The 51 generic-binding rows comprise 44 evidence-specific MODIFY and seven supported KEEP_AS_NON_CORE. All original source fields, qualifiers, supporting entities, products, core functions, references and normal caches remain unchanged. This follow-up remains subject to the fresh PR's review and CI; a merged original PR alone does not complete the campaign hold.


## 2026-10-09 — self-contained TRADD evidence excerpt

The TRADD evidence now includes the complete cached sentence naming c-E10
(BCL10), the transfection context and TRADD co-precipitation. Duplicate short
adaptor excerpts at two other annotations are removed while their source links,
reasons and actions are retained. The remaining NF-kappaB excerpt is unchanged.
The earlier three-word truncation is superseded; the four source links now
carry 23 quoted words in total. Limiting repeated quotation was an authoring
constraint, not a repository validation rule or a scientific reason to shorten
the subject out of the evidence. No annotation decision changes. The earlier
history record is retained as provenance and corrected by this new entry and
the accompanying append-only history record.

The [COG6 interaction evidence](BCL10-interaction-evidence.json) preserves the
exact five human BCL10–COG6 pair records used for the two screen assertions,
including interaction IDs, PSI-MI methods, publication/IMEx IDs, species and
figure/table provenance. It includes the two source-specific IntAct query URLs
and response hashes. These records were read from the returned data, not inferred
from accession names. They provide traceability to the curator-recorded assays,
not independent replication of those experiments.


## 2026-10-09 — signaling-adaptor evidence locators

The two signaling-adaptor decisions now cite the mechanistic evidence directly in
their reasons and `supported_by` lists. Selected full-text Results in
[PMID:24074955](https://pmc.ncbi.nlm.nih.gov/articles/PMC3929958/) describe human
CARMA1-dependent BCL10 assembly (Figure 1), MALT1 incorporation and activation
(Figures 3A-B), and cellular complexes (Figures 3C-D). The complete cached abstract
of [PMID:15125833](https://pubmed.ncbi.nlm.nih.gov/15125833/) independently describes
reconstituted signaling by BCL10-MALT1 oligomers. These findings establish
BCL10's noncatalytic organizing role; the protease, ubiquitin-ligase and kinase
activities remain those of its partners.

The earlier adaptor interpretation in PMID:10400625 remains cited as corroboration.
The two reasons paraphrase the evidence and provide its experimental locators;
they no longer promise a displayed abstract excerpt. The complete TRADD sentence
and every existing excerpt remain intact. No new scientific quotation or
annotation decision is introduced. The prior quotation accounting documents an
authoring constraint, not a repository rule or a basis for judging biological
validity.
