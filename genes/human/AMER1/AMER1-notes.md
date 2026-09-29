# AMER1 research and annotation notes

## 2026-09-27 — initial full audit

AMER1 (HGNC:26837; UniProt Q5JTC6; historical FAM123B/WTX) has 61 seeded annotations and two annotated alternative products. The three normal fetched seed files match the source archive exactly. The current main and canonical/alias/history/open-PR checks found no competing review. The normal Falcon research wrapper, including its configured fallback, failed before generating a report. Ordinary publication caching found all nine original PMID records; the 21 original Reactome records are also present. Source files remain unchanged.

### Working biological synthesis

AMER1 is a membrane-associated scaffold with context-dependent effects on canonical Wnt signaling. Its N-terminal phosphatidylinositol-4,5-bisphosphate interaction recruits APC to the membrane. The original paper describes redistribution between APC's membrane and microtubule pools, rather than AMER1 being a microtubule motor [PMID:17925383]. The WTX interaction-network study links the scaffold to beta-catenin ubiquitination and destruction; the enzymes in that process remain distinct from AMER1 [PMID:17510365].

The 2011 studies support distinct functional configurations. Membrane-bound AMER1 can stabilize Axin and organize destruction-complex components [PMID:21498506]. During receptor activation it can recruit Axin/GSK3 and associate with CK1gamma/LRP6, facilitating LRP6 phosphorylation [PMID:21304492]. These are compatible context-dependent activities; the presence of both positive and negative Wnt regulation annotations is not by itself a contradiction. The two original cached abstracts explicitly support these different configurations. Direct PMC opens currently returned a browser-check page; indexed primary passages are available, but complete Methods and all source panels have not yet been read.

The nuclear-shuttling study describes human WTX association with WT1 and paraspeckles, with WT1-dependent transcription tested in cells. It also distinguishes full-length WTX from an earlier predicted 804-residue construct, so construct boundaries must be checked before generalizing an assay to both endogenous isoforms [PMID:19416806; https://pmc.ncbi.nlm.nih.gov/articles/PMC2677091/]. This study's abstract and indexed Results passages were read; its complete experimental record is not yet assessed.

### Source and inference boundaries

The AMER3 paper explicitly identifies AMER1 as an interacting partner. Its title foregrounding AMER3 is not evidence that the AMER1 annotations are misassigned. AMER3 lacks the N-terminal membrane targeting domain, so its localization or direction of Wnt regulation should not be transferred indiscriminately [PMID:24251807]. The primary family analysis provides a comparative framework, but it does not establish the placement of a particular PAINT IBD node [PMID:20843316; https://pmc.ncbi.nlm.nih.gov/articles/PMC2949870/].

The 21 Reactome event summaries were read. They cover destruction-complex assembly, phosphorylation, ubiquitination, degradation and mutant contexts. These are cytosol annotations, not assertions that AMER1 catalyzes every event. Most summaries lack AMER1-specific experimental detail, so independent localization evidence will inform their assessment. No AMER1/Q5JTC6 entry was found in the local GO-CAM index.

Most original publication caches are abstract-only. The BioPlex cache is marked full text but contains a partial introduction/discussion extraction; AMER1-specific interaction records have not been independently inspected [PMID:33961781]. The 2025 multimodal cell-map cache has not yet been read [PMID:40205054]. Inaccessible experimental evidence will remain unresolved rather than being rejected from a title or a missing supplementary table.

Four additional sources have been requested once through the ordinary cache command: the initial somatic tumor study [PMID:17204608], the germline skeletal-dysplasia study [PMID:19079258], nuclear shuttling [PMID:19416806], and the family analysis [PMID:20843316]. Their identifiers and titles were verified against primary PubMed/PMC records. The attempt failed with DNS errors for all four. Somatic tumor association and germline skeletal phenotypes provide biological context, not an automatic molecular-function or developmental-process annotation.

This entry records research in progress. Annotation decisions, independent consultation, core synthesis and validation remain to be completed.

### Additional source access during this session

The source archive also retained a richer normal extraction of [PMID:21304492] separately from the existing abstract-only canonical cache. Its Results, Discussion and Methods were now read. The canonical cache was preserved. The study used human HEK293T, SW480 and MCF-7 cells, endogenous complexes and engineered constructs. Axin recruitment persisted when LRP6 phosphorylation was inhibited, and Axin linked GSK3beta to AMER1. Thus recruitment is supported by experiments beyond a generic knockdown phenotype. The authors did not directly detect AMER1 within their overexpressed signalosomes; necessity for their formation should not be rewritten as demonstrated residence in that structure.

The long S1 construct promoted LRP6 phosphorylation, whereas S2, lacking residues 50–326, did not. Specific depletion of S1 reduced that response while S2 depletion did not. Both splice products remain in the review, and these results qualify the relevant function rather than silently assigning a tested-isoform tag to every original GOA row. Lipid-strip assays used bacterially produced GST fusions. Phosphorylation was performed by the recruited kinases, not AMER1. The LRP6 intracellular-domain fusion activated downstream transcription, while AMER1 alone retained an inhibitory effect on that downstream readout. This supports contextual regulation rather than an unconditional Wnt activation claim.

The ordinary PAINT fetch for PTHR22237 failed with DNS errors. Cached family membership is available; the actual IBD tree was not recovered, so no inferred node-placement defect is asserted.

### Completed first annotation pass and construct reconciliation

All 61 original annotation objects and both alternative-product records are preserved. The first full pass contains 41 ACCEPT, seven MODIFY, two KEEP_AS_NON_CORE and 11 UNDECIDED decisions, with no NEW annotations. The compact core uses the existing protein-membrane adaptor activity and broad canonical Wnt regulation terms. AMER1 physically organizes proteins at a membrane; this supplies a participation mechanism beyond necessity alone. The kinases, ubiquitin-transfer machinery and proteasome retain their respective catalytic roles. No new process assertion, signalosome-membership assertion or redundant ancestor/descendant pair is proposed.

**The names S2 and short are not sufficient sequence identifiers.** The 2011 studies use an S2 construct lacking residues 50–326. The immutable current UniProt record instead assigns Q5JTC6-2 a replacement at residues 786–804 and absence of residues 805–1135. The seeded alternative-product label includes “Amer1-S2, Short”, but its sequence changes do not establish equivalence to the experimental N-terminal deletion. Both source products remain unchanged; no tested-isoform field is invented. The earlier 804-residue WTX reagent, canonical 1135-residue protein and 2011 deletion construct must remain distinct unless their sequences are reconciled [PMID:17925383; PMID:21304492; PMID:21498506; PMID:19416806; UniProt:Q5JTC6].

The author-uploaded original 2007 JCS article was read through the remaining Materials and Methods. Human AMER1 sequence provenance, endogenous co-immunoprecipitation, recombinant lipid-binding assays and cellular membrane recruitment support the adaptor interpretation. The initial mouse library and canine MDCK host are separate from the expressed human construct. The Discussion does not itself supply a new Wnt reporter experiment [PMID:17925383; https://www.researchgate.net/publication/5920420_AMER1_regulates_the_distribution_of_the_tumor_suppressor_APC_between_microtubules_and_the_plasma_membrane].

Independent original-source consultation recovered indexed Science Results, including Fig. 2C: recombinant WTX binds beta-catenin and beta-TrCP1/BTRC. This resolves the BTRC-specific uncertainty left by an abstract naming beta-TrCP2/FBXW11. Other recovered partners remain at their own association-evidence resolution. Author-deposited reagents identify human WTX 1–804; complete supplemental production methods remain unavailable. Xenopus-extract ubiquitination is not an intrinsic AMER1 E3-ligase assay [PMID:17510365; https://citeseerx.ist.psu.edu/document?doi=5308156687cba9e7f4cefc74fcecde909d7aaba6&repid=rep1&type=pdf; https://www.addgene.org/36956/; https://www.addgene.org/36958/].

The original 2012 Cell main paper was independently read, verifying endogenous Axin1 IP-MS in human cells. Its AMER1-specific supplementary hit was not recovered. That row remains UNDECIDED, without asserting a wrong citation [PMID:22682247; https://www.hubrecht.eu/app/uploads/2017/11/PIIS0092867412005302.pdf]. The 2025 cell-map Methods were also inspected: human tagged ORFeome baits and U2OS affinity-purification scoring do not reveal the specific AMER1–FBXW11 pair in the available body [PMID:40205054].

The official Human Protein Atlas page supports nuclear bodies and plasma membrane in specified human cell lines. These locations are retained, with nuclear bodies recorded outside the compact membrane core; the broad nuclear-body annotation is not silently narrowed to paraspeckles [GO_REF:0000052; https://www.proteinatlas.org/ENSG00000184675-AMER1/subcellular]. The GO protein-membrane adaptor definition was checked against its official term page [https://amigo.geneontology.org/amigo/term/GO:0043495].

Four additional primary records still lack canonical normal caches after the ordinary DNS failure. Their fixed recovery request is tracked separately. Independent all-row consultation, final validation and final source closure remain pending; this is not a completion claim.

### KEAP1/NRF2 evidence added during independent review

The primary study tests direct WTX–KEAP1 binding, motif-dependent competition with NRF2 and reduced NRF2 ubiquitination. Its historical human 804-residue construct is distinguished from the canonical protein and internal-deletion form. This supports bounded functional prose and a follow-up question; it does not identify the unrecovered original 2007 screen entry or assign AMER1 ligase catalysis. No NEW annotation was added [PMID:22215675; DOI:10.1074/jbc.M111.316471; https://pmc.ncbi.nlm.nih.gov/articles/PMC3307315/]. One ordinary normal fetch failed with DNS. This fifth required record is separate from the four already requested sources; the dispatched request inventory was not altered.


## 2026-09-27 — four normal source records recovered

The normal records for [PMID:17204608], [PMID:19079258], [PMID:19416806] and [PMID:20843316] are now present with their exact fetched bytes. The first three contain abstracts only; a PMC identifier on the nuclear-shuttling paper does not mean its full text was recovered. The complete available abstracts were read. The OSCS publisher abstract also confirms the primary identity and clinical scope; its main text remains subscription-restricted. Its reference assessment is now VERIFIED within that scope.

The family paper contains a readable extracted body. Its actual Figure 4 and Methods use mouse Amer constructs amplified from BACs in HEK293T cells with human beta-catenin and a TOP/FOP reporter. Amer1 suppresses reporter output under those conditions, whereas Amer2/3 do not. That result supports distinguishing downstream functions across the family; a predicted Amer3 APC-recruitment role is not a new experimental result or a recovered PAINT node. Current AMER1 splice labels remain separate from historical construct identities.

The 61 original source assertions, all action decisions, two alternative products and one core are unchanged. One normal publication record, [PMID:22215675], remains pending in a separate bounded recovery. No provider report was generated or authored, and no recovered abstract is represented as a full paper.

## 2026-09-27 — final normal source recovered

The normal XML-derived record for [PMID:22215675] is now present unchanged. Its Methods, Results and figure captions confirm purified human WTX binding to KEAP1 with CUL3 negative, motif-dependent peptide competition with NRF2, and reduced NRF2 ubiquitination in translated-component assays. The study explicitly uses the historical 804-residue construct; the 1135-residue canonical protein and 858-residue internal-deletion form remain distinct. Endogenous perturbation readouts provide separate corroboration. Duplicated extraction aggregates and uninspected supplements are not counted as additional evidence.

All 14 cited PMID caches and 21 Reactome records are present. The final source closure adds a verifiable finding and updates availability notes; it preserves all 61 seeded source assertions, their action decisions, both alternative products and the single membrane-adaptor core. Eleven source-specific scientific uncertainties remain explicit, and no NEW annotation is proposed.

## 2026-09-27: PR #3329 follow-up — adjudicate binding assertions using independent evidence

The review distinguishes the biological assertion from the availability of a particular screen's pair record. Nine generic binding rows are now `MODIFY`, supported by separately identified mechanistic studies; the original PMID, evidence type, partner set and all other source fields remain unchanged. None of the later experiments is represented as a reconstruction of the earlier screen.

- KEAP1 (`PMID:17510365`, Q14145): `PMID:22215675` directly tests recombinant WTX–KEAP1 binding and NRF2 competition. `GO:0031625 ubiquitin protein ligase binding` describes recognition of the CUL3 E3 machinery through its KEAP1 substrate-recognition subunit. KEAP1 is not a standalone ligase, and that study did not detect direct WTX–CUL3 binding. Its human 804-residue reagent remains distinct from the full-length 1135-residue protein and the delta-50–326 858-residue construct.
- AXIN1/APC screen or interaction rows (`PMID:22682247`, `PMID:24251807`, `PMID:26496610`): independent `PMID:21498506` recruitment of APC and Axin/Conductin supports `GO:1904713 beta-catenin destruction complex binding`.
- CTNNB1 (`PMID:26496610`): direct armadillo-repeat binding in `PMID:21498506` supports `GO:0008013 beta-catenin binding`.
- FBXW11/BTRC (`PMID:33961781`, `PMID:40205054`): the new FBXW11 binding-domain experiment in `PMID:22215675` and direct BTRC experiment in `PMID:17510365` Fig. 2C support the existing complex-binding term. The BTRC statement in `PMID:22215675` corroborates earlier work; the original abstract naming beta-TrCP2 is not used as BTRC-specific proof. No screen-specific bait direction, confidence, construct or cell context is inferred.

The refinements to already seeded specific binding terms subsume the generic rows. They do not add independent experiments or new annotations. SKP1 and AMER3 remain `UNDECIDED`: their source-specific evidence still does not establish a supported informative replacement. The AMER3 abstract does report binding; the unresolved point is its functional interpretation, not a claim of paralog confusion.

The core now explicitly includes N-terminal PtdIns(4,5)P2 binding as the membrane-recognition component of the adaptor mechanism, supported by `PMID:17925383` and the two existing experimental annotation rows. This introduces no additional process assertion. The standalone description omits reagent/construct framing. The Wnt-regulation IMP rationale now directly cites the APC-abundance decrease after AMER1 knockdown in `PMID:17925383`; it does not invent a reporter assay in that paper.

Repeated host/species and Reactome cautions were shortened in the row explanations. Their scientific boundaries remain: the 21 Reactome annotations concern cytosolic location, and event participation does not assign kinase, ubiquitin-ligase or proteasome catalysis to AMER1. Historical human constructs, host-cell species, and the current alternative-products records remain separately documented above. The source records and previous history entry are preserved.

Follow-up tally: 61 reviewed source objects; 41 ACCEPT, 16 MODIFY, 2 KEEP_AS_NON_CORE, 2 UNDECIDED, and 0 NEW; two core molecular functions. Full schema, GOA coverage, source quotes, rendering and new-history checks are rerun for the follow-up; independent bounded annotation consultation is recorded in the new session history.
