# ABCA4 annotation review notes

## Scope and provenance — 2026-09-25

The clean dedicated checkout was initialized on `cmungall/clingen-abca4` from main. `just fetch-gene human ABCA4` retrieved UniProt P78363, 60 GOA records and 59 deduplicated review rows. All 59 source assertions are preserved and independently assessed. Falcon deep research was started with a 1,200-second timeout concurrently with `just fetch-gene-pmids human ABCA4`; the known exhausted Perplexity quota was not retried. Primary-source caching and ontology verification proceeded while research ran. This file records manual interpretation, not provider-generated research.

The ClinGen Retina GCEP association is autosomal recessive **ABCA4-related retinopathy**, Definitive (CCID004006, MONDO:0800406, evaluated 2022-10-06). The [ClinGen report](https://search.clinicalgenome.org/kb/gene-validity/CGGV:assertion_38729563-bf36-48ae-929e-fa69a225de39-2022-10-06T160000.000Z) groups Stargardt/fundus flavimaculatus and the cone-rod degeneration spectrum. It specifically cautions that classic rod-cone retinitis pigmentosa evidence is weak and advanced cone-rod disease may explain older diagnoses; dominant age-related macular degeneration evidence is conflicting. These older disease labels in UniProt are therefore not repeated as settled distinct Mendelian associations.

## Direct catalytic mechanism and substrate chemistry

The decisive direct transport study is [PMID:22735453, *ABCA4 is an N-retinylidene-phosphatidylethanolamine and phosphatidylethanolamine importer*]. Purified protein and reconstituted membranes demonstrate NRPE and PE movement from exoplasmic/lumenal to cytosolic leaflet. The study distinguishes retinal's rapid membrane diffusion from active movement of its PE adduct. Importantly, “ATP-dependent transfer was not observed for [3H]-all-trans retinol”. Retinol, retinal and NRPE are chemically different and cannot be interchanged in GO assignments.

[PMID:24097981, *Differential phospholipid substrates and directional transport by ATP-binding cassette proteins ABCA1, ABCA7, and ABCA4 and disease-causing mutants*] directly compares inward PE transport by ABCA4 with outward phospholipid transport by ABCA1/ABCA7. The initially abstract-only cache was upgraded through the normal `fetch-pmid --force` tool, which successfully obtained full text by its HTML fallback. No cached source was manually rewritten.

[PMID:24707049, *ATP-binding cassette transporter ABCA4 and chemical isomerization protect photoreceptor cells from the toxic accumulation of excess 11-cis-retinal*] extends the transport mechanism to 11-cis-NRPE. Isomerization is chemical; RDH enzymes reduce retinal after adduct dissociation. ABCA4 is not the reductase or isomerase. The core functions therefore describe two distinct demonstrated substrates (NRPE and PE) in the same inward flippase mechanism, not a series of redundant ATP-binding and ATPase functions.

Human ATP-binding and hydrolysis are supported by [PMID:33605212, *Molecular structures of the eukaryotic retinal importer ABCA4*] and [PMID:39128720, *Structural and functional characterization of the nucleotide-binding domains of ABCA4 and their role in Stargardt disease*]. Basal ATP hydrolysis is retained as a real intrinsic activity, alongside the coupled transport role.

## Retinoid binding and nucleotide promiscuity

[PMID:20404325] directly studies all-trans-retinal binding by recombinant human ECD2. [PMID:23144455] directly studies 11-cis-retinal binding by isolated human NBD1. These explicit domain-level binding observations are retained as non-core biochemical capacities; NRPE being the physiological transported substrate does not invalidate them.

In contrast, the full-length disease-variant binding studies [PMID:29847635] and [PMID:33375396] mix retinal and PE to form **NRPE**, then measure adduct binding and ATP-dependent release. The latter explicitly states: “ABCA4 immobilized on an immunoaffinity matrix was treated with ATR in the presence of PE to generate N-Ret-PE.” The associated free-all-trans-retinal binding rows are retained as non-core capacities supported by the independent domain and intact-protein binding studies, with an explicit caveat that the cited variant assays measure NRPE. Binding evidence is not converted into transport evidence.

The GTPase ISS donor was traced from GOA to reviewed bovine ABCA4 **UniProtKB:F1MWM0**, and live QuickGO traces its GTPase IDA to [PMID:10767284, *The effect of lipid environment and retinoids on the ATPase activity of ABCR*]. The abstract explicitly reports ATPase and GTPase assays. PMID:22735453 also reports partial replacement of ATP by GTP in transport. This is valid experimentally grounded biochemical promiscuity, not a spurious transfer from a small GTPase. Retain as non-core; physiological GTP-driven human transport remains uncertain.

## Localization and interpretation of expression systems

Photoreceptor outer segments and disc rims/incisures are established sites of ABCA4 function. Both rod and cone expression are supported by modern work; the historical rod-only claim in the 1997 cloning abstract is not adopted.

The full text of PMID:24097981 distinguishes wild-type ABCA4 in large calnexin-positive vesicles from reticular ER retention by some misfolded variants. However, PMID:29847635 explicitly also observes **some ER reticular staining for wild type**, and PMID:33375396 retains the distinction between folded variants that exit ER and misfolded variants retained there. Thus neither deleting all ER localization as mutant-specific nor defining ER as the physiological site of visual-cycle transport is justified. ER and unspecified cytoplasmic vesicle annotations are retained as non-core expression-context localizations.

The [Human Protein Atlas subcellular page](https://www.proteinatlas.org/ENSG00000198691-ABCA4/subcellular), read live, reports ER staining with HPA064420 in HeLa, MCF-7 and U2OS cells and a supported reliability score. RNA levels are low in those lines; the observation is retained within that context.

[PMID:30397118, *Expression of ABCA4 in the retinal pigment epithelium and its implications for Stargardt macular degeneration*] establishes endogenous RPE expression using human/mouse RNA measurements, human fetal RPE and mouse protein/localization controls. Mouse protein colocalizes with endolysosomal markers, and RPE-only expression partially rescues the knockout phenotype. The proposed RPE endolysosomal NRPE transport mechanism is a model, not a direct transport measurement.

[PMID:36306781, *Cell-autonomous lipid-handling defects in Stargardt iPSC-derived retinal pigment epithelium cells*] provides direct surface proteomics, fractionation, apical-marker colocalization and immunogold TEM evidence for **human RPE apical plasma membrane ABCA4**. This corroborates the existing plasma-membrane annotation, which is retained as non-core rather than dismissed because photoreceptor discs are the major site. RPE phenotypes do not justify manufacturing extra lipid-homeostasis, lysosomal acidification, phagocytosis or proteolysis process annotations.

## Ontology and pathway audit

Live QuickGO definitions were read for NRPE/PE flippase, retinal/retinoid metabolism, retinol transporter/transport, organic hydroxy compound transport, visible-light phototransduction and visual perception. Retinol terms expressly describe the alcohol. The Reactome events [R-HSA-1467466](https://reactome.org/content/detail/R-HSA-1467466) and [R-HSA-2466802](https://reactome.org/content/detail/R-HSA-2466802), read through the Content Service, describe retinal or NRPE while GOA maps them to retinol transporter activity. The direct negative retinol assay and positive NRPE assays support correction of these source assertions and the related retinol/organic-alcohol process assignments.

**GO:0140347 definition issue:** the live term label is “N-retinylidene-phosphatidylethanolamine flippase activity”, but its text definition names “N-retinylidene-N-retinylphosphatidylethanolamine”. The latter appears to name the doubly retinylated bisretinoid rather than NRPE. The official label and direct ABCA4 annotations identify the intended function. The review preserves the official ID and label and raises an explicit expert question; it does not silently rewrite ontology text or assert transport of the bisretinoid.

The broad visual-perception electronic annotation is kept non-core. PMID:9425888 has no accessible abstract or full text, and PMID:9202155 is abstract-only with only a proposed photoresponse role. Both were initially UNDECIDED; the PMID:9202155 decision is resolved by the later full-text recovery recorded below. The live visible-light phototransduction definition describes conversion of absorbed photons to molecular signal; retinoid clearance is not sufficient evidence to assume direct participation in that conversion.

No ABCA4/P78363 entry was found in `gocams/index.tsv`. No NEW process annotation is proposed. Existing transport assertions already cover the actual steps performed by the protein.

## Research completion and source-sensitive decisions

The authentic Falcon/Edison report completed successfully in 529.53 seconds and its generated artifact is retained unchanged. Its core substrate/direction conclusions agree with the independent primary-literature audit. Therapeutic and prevalence material is outside this functional review and was not adopted. The report does not override the direct 2022 human RPE apical-localization evidence or the carefully scoped isolated-domain binding assays. The conservative IBA and TAS ATPase-coupled transporter annotations are both retained; specificity is provided by the existing lipid-carrier/flippase assertions. All three free-all-trans-retinal binding rows are non-core, with source-specific ligand caveats; differing visual-perception actions reflect inability to access the specific 1998 report.

The Falcon report led to two additional primary checks: PMID:15471866 verifies preferential NRPE binding with some free-retinal binding by purified full-length protein (and no retinol binding); PMID:36931393 provides 2023 direct specificity/mutagenesis evidence showing that the retinal-PS adduct is not an ABCA4 substrate. Neither supports treating all retinal-phospholipid adducts as interchangeable. The free-retinal binding reviews distinguish the ligand assayed in the 2018/2021 sources while retaining the independently established free-retinal capacity.

## Validation and access follow-up

Initial action counts: 36 ACCEPT, 11 KEEP_AS_NON_CORE, 10 MODIFY, 2 UNDECIDED. Initial `just validate human ABCA4` passed with two source-sensitive action warnings; the binding-action split is corrected below. History validation, rendering and diff checks pass. The Nature page for PMID:9425888 confirms subscription-only content. Search for PMID:9202155 retrieved the abstract and a full-paper mirror, but the full PDF retrieval timed out; the complete paper remains unread, so UNDECIDED is retained.


## PR #3132 evidence review follow-up — 2026-09-26

The two full-length variant-study retinal-binding rows now use KEEP_AS_NON_CORE, consistent with the isolated-domain row. The cited assays identify NRPE rather than free retinal, but independent human-domain and purified bovine full-length experiments establish free-retinal binding. The reasons explicitly retain that distinction; neither binding assay is converted into a new transport assertion. Source terms, evidence codes and reference identifiers remain unchanged.

The three NRPE flippase rows now cite primary PMID:36931393 headgroup-specificity evidence alongside the direct transport studies, replacing the Falcon sentence about unmodified PE. The plasma-membrane row now explicitly includes PMID:30397118 internal/endolysosomal RPE evidence alongside PMID:36306781 human apical-surface evidence, leaving the relative pools unresolved.

The reviewer also suggested changing phototransduction TAS/PMID:9202155 to over-annotated because its abstract is accessible. The full source remains unavailable. The repository instruction to use UNDECIDED for inaccessible relevant publications is not waived by an abstract or by the TAS evidence code. The reason now distinguishes that access limitation from the modern evidence for retinoid clearance and avoids treating an abstract-only assessment as a complete adjudication. The action remains UNDECIDED pending full-text assessment.

Updated decisions: 36 ACCEPT, 13 KEEP_AS_NON_CORE, 8 MODIFY, 2 UNDECIDED. No NEW annotations.

Follow-up validation passes. The two remaining advisory warnings are the intentional visual-perception action difference and the absence of a deep-research-file quotation in annotation support. The authentic report remains retained and discussed as research provenance; primary evidence supports the decisions. Source assertion comparison, history validation, rendering and diff checks pass.


## Recovery of the original phototransduction source — 2026-09-26

After the first reviewer-response commit, the complete original [PMID:9202155 Wiley article](https://febs.onlinelibrary.wiley.com/doi/10.1016/S0014-5793(97)00517-6) became accessible through the HTML route, despite the mirror PDF continuing to time out. I read its methods, results and discussion. The experiments identify and characterize the rim protein; the discussion treats calcium-handling and light-stimulated ATPase roles as hypotheses and explicitly leaves function unresolved: “The function of RmP in photoreceptors remains a critical open question.” It also considers retinoid transport less likely, a historical interpretation superseded by the direct NRPE/PE transport experiments.

This changes the evidentiary premise of the previous UNDECIDED decision. GO:0007603 now receives MARK_AS_OVER_ANNOTATED: the original source does not establish phototransduction, and modern primary evidence supports retinoid clearance rather than direct conversion of photons to a molecular signal. The full text was read on the publisher website; the cached publication remains unchanged and abstract-only. The schema's supporting_text_fulltext field records the short exact discussion quote transparently. The inaccessible PMID:9425888 visual-perception row remains UNDECIDED.

Current decisions: 36 ACCEPT, 13 KEEP_AS_NON_CORE, 8 MODIFY, 1 MARK_AS_OVER_ANNOTATED, 1 UNDECIDED. No source assertion fields or core functions changed in this follow-up.

Full-text follow-up validation passes with the same two documented advisory warnings. History validation, rendering, source assertion comparison and diff checks pass.
