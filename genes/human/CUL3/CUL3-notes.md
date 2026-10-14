# CUL3 notes

Initial Falcon pass, 2026-05-12. CUL3 started as a fully pending review with
228 annotations. I kept this pass centered on the conserved CRL3 scaffold
function and left most generic protein-binding and substrate-specific rows for
later source-level review.

Core molecular function: CUL3 is the scaffold of cullin-RING E3 ligase
complexes. Falcon states that CUL3 bridges RBX1/E2 ubiquitin-conjugating
machinery with BTB-domain substrate adaptors
[file:human/CUL3/CUL3-deep-research-falcon.md "CUL3 is the **central
scaffold** of CRL3 ubiquitin ligases, bridging (i) a **RING protein (RBX1)**
that recruits E2~ubiquitin and (ii) **BTB-domain substrate adaptor/receptor
proteins** that recruit specific substrates."]. I accepted ubiquitin ligase
complex scaffold activity and Cul3-RING ubiquitin ligase complex rows as the
core axis.

Core process: protein ubiquitination, polyubiquitination, and
proteasome-mediated ubiquitin-dependent catabolism are proximal outputs of many
CRL3 complexes [file:human/CUL3/CUL3-deep-research-falcon.md "Proteasomal
targeting is a canonical outcome for many CRLs, and reviews explicitly describe
substrate ubiquitination “for proteasomal degradation” as a CRL3 output"]. I
accepted well-supported ubiquitination and catabolic-process rows, but kept the
caveat that not every CUL3 ubiquitination event is degradative.

Molecular-function specificity: Falcon cautions that CUL3 is best represented
as the scaffold rather than the catalytic ubiquitin transferase
[file:human/CUL3/CUL3-deep-research-falcon.md "evidence best supports a CUL3
annotation consistent with **“ubiquitin ligase complex scaffold activity”** /
**E3 ligase scaffold** rather than “ubiquitin-protein transferase activity”
(which is catalytic and typically attributed to the E2/E3 catalytic machinery
rather than the scaffold)"]. I therefore modified ubiquitin-protein transferase
and ubiquitin protein ligase activity rows to the scaffold term.

Non-core contexts: many CUL3 annotations reflect the substrate/adaptor being
studied: KEAP1/NRF2 oxidative stress, KLHL3/WNK ion transport, KLHL12/COPII,
KBTBD/KCTD complexes, mitotic substrates, neuronal phenotypes, viral processes,
and disease models. Falcon warns that broad phenotypes should not be promoted
to core CUL3 functions without direct mechanistic evidence
[file:human/CUL3/CUL3-deep-research-falcon.md "oxidative stress response,
blood pressure/electrolyte phenotypes, neurodevelopmental phenotypes, or
cancer-associated phenotypes can be downstream of CUL3-dependent substrate
regulation. These should not be treated as core CUL3 BP terms without direct
mechanistic evidence that CUL3’s scaffold activity is required in the specific
pathway node being annotated."].

Localization: CUL3 complex membership is core. I accepted a few broad
cytoplasm/cytosol/nuclear rows, but Falcon notes that specific membrane,
centrosome, cytoskeleton, and other locations require caution
[file:human/CUL3/CUL3-deep-research-falcon.md "**Membrane/centrosome/cytoskeleton
claims require caution:**"]. Most highly specific or repetitive localization
rows remain pending unless a direct source was already strong enough for a
non-core decision.

Left for later: generic protein-binding rows should be triaged by partner
(BTB/POZ adaptor, RBX1, substrate, CSN/CAND1 regulator, or nonspecific
interaction). Substrate-specific phenotype rows should be reviewed one adaptor
module at a time rather than treated as core CUL3 biology.


## Source-based augmentation, October 2026

The earlier Falcon-centered pass above is preserved as history. Its blanket catalytic refinements are superseded here: the source annotations explicitly qualified `contributes_to` are valid contributions to assembled ubiquitin transfer. CUL3 itself performs scaffold activity, linking BTB adaptors to RBX1/E2 machinery. The genuine Falcon report remains unchanged and was assessed as secondary background, not treated as an experimental source. PMID:14528312 and the actual PMID:20389280 reconstitution support this distinction. The compact core records one scaffold unit, its complex contribution, CRL3 membership, protein ubiquitination and proteasomal catabolism; it does not duplicate the nested polyubiquitination process or imply that all ubiquitination is degradative.

All 228 historical source objects are retained exactly, including qualifiers, absent defaults and tested-product fields. The preserved GOA has 383 raw rows; the genuine fresh seed has 375 rows, with different multiplicity, and the independent current QuickGO capture has 400. Those observations are not combined into a fabricated GOA. All three official products reconstruct exactly (768, 744 and 702 residues). The latter products delete residues 1–24 and 23–88, respectively. Historical 17–768 yeast bait and exon-deletion bait, artificial 34–74 deletion and the disease-associated 403–459 deletion remain separate construct contexts; equal function of all products is not established.

Actual PTHR11932 topology includes the exact CUL3 sequence and all six source IBDs on its ancestral path, with no target-path loss. Three historical/current donor sets differ, which is recorded without rewriting the historical source. Donor count and target self-evidence are not reasons to reject a PAINT inference. Complete donor pagination, literal source/term joins and all current ARBA branches were reconstructed. The adult mouse kidney-deletion source PMID:25250572 establishes injury and homeostasis, not embryonic kidney development; the COPII source PMID:22358839 establishes performed export regulation, without proving every downstream integrin, division or cleavage process.

The 57 interaction assertions were assessed against 1,466 IntAct and 91 MINT records, 262 used records and 524 exact sequence ROGIDs. This identity reconstruction does not prove every interaction is direct or physiological. Supported generic binding is retained as non-core under the standing ClinGen instruction; a measured partner/domain permits a more precise binding term. Source-specific interactions without an adjudicated target assay remain undecided. COPS5 enzyme binding, HSP90AB1 binding, ACOT7 thioesterase binding and experimentally mapped BTB contacts are refinements, not transfers of those partners' catalytic functions to CUL3.

Several original distinctions matter. PMID:25619834 supports RBX1/KLHL20 binding but reports failure of wild-type IVNS1ABP/KLHL39 to bind CUL3, with engineered substitutions restoring binding. Its original source tuple is preserved and the different partner arm is explained. PMID:38225382 measures positive KCTD7 BRET yet rejects the predicted interface for validation; it does not establish an isolated BTB interface. PMID:23455478 concerns KLHL22/PLK1 localization control, whereas PMID:22358839 concerns KLHL12/SEC31/collagen export. PMID:27561354 concerns KLHL15/CtIP, not KBTBD7. The positive nuclear CtIP turnover result does not establish misfolded-protein quality control, and the free-cyclin-E pathway of PMID:10500095 is not APC/C-dependent.

The original PMID:29769719 KLHL22–DEPDC5 mechanism is disputed by PMID:39780017 and defended in PMID:39780003. The challenge maintained cells in DMEM but used RPMI for its 50-minute starvation and 10-minute refeeding protocol. The reply invokes antibody, cleavage, tagging and medium differences and a regulated DEPDC5 subset. The challenge does not rule out ubiquitin regulation generally. The evidence does not settle the specific nutrient-response/TORC1 assertions; these remain undecided. Independently established CRL3 scaffold and proteasomal roles are retained without treating the disputed DEPDC5 route as a settled example. The paper is not labeled retracted or invalid.

Positive mitotic, centrosomal, Golgi and partner-recruited membrane pools are retained at their actual source scope. Human CUL3 knockdown, reconstitution and localization in the Aurora/PLK1/KLHL42 studies support contextual participation, not intrinsic kinase or microtubule catalytic activity. Non-degradative SEC31, Aurora and TCOF1/NOLC1 modifications remain distinct from proteasomal targeting. The urinary-exosome database supporting PMID:19056867 contains a single-peptide CUL3/NP_003581 identification at zero-based HTML row 325, reference 2; it establishes detection, not secretion or extracellular function. The unresolved YTS membrane screen is not rescued merely by independent plasma-membrane recruitment in another experiment.

All 15 target GO-CAM activities place CUL3 in the scaffold role with separate neighboring adaptor/catalytic roles. A bounded current Reactome reconstruction authenticated 521 objects, 700 edges and 42 Q13618 target paths; 31 nested IDs remain unresolved after genuine access failures and a fixed retry budget. The compact evidence index distinguishes those incomplete paths from reached target paths. Cached event context and independent localization can support the existing broad compartment assertions, but missing objects are not negative evidence and neighboring deneddylase, NEDD8-transferase, proteasome or adaptor functions are not transferred to CUL3.

ROOT independently read the two-source catalytic-contribution slice, five ARMC5 sources and the KLHL22 dispute; their complete reports and exact source bindings were read and reproduced by the owner. Other personally read primary windows are recorded in the owner source ledger, with explicit limits for abstracts, selected full-text paragraphs, author reprints and inaccessible supplementary assays. The 19782033 erratum contents remain unavailable. References 29249570, 31898230 and 37628845 are reviews, not new primary assays. An available cache or an exact interaction ID does not imply that every target table or figure was read.

The current review replaces the former 318 provider-centered/repeated support items with source-specific support and a small set of literal primary anchors. This is not a claim that all quote leaves are unchanged: the original review and this notes prefix retain their historical wording. Newly authored primary quotations are checked against unchanged caches and limited to 25 words per source across their occurrences; this appendix adds no primary quotation. No NEW annotation is proposed.


## Whole-review precision corrections

The independent whole review identified one source-specific action correction. Row 207 is now UNDECIDED: the complete PMID:18826954 abstract and current interaction exports do not resolve its CUL3–DCUN1D1 assay. The paper-specific reference assessment is UNVERIFIED, while the genuine positive association established by separate DCNL–CUL3 studies remains acknowledged. This is an access and evidence limit, not a claim of nonbinding. The final actions are 112 ACCEPT, 73 KEEP_AS_NON_CORE, 21 MODIFY, 13 UNDECIDED and 9 MARK_AS_OVER_ANNOTATED.

Three prose corrections identify GO_REF:0000002 as InterPro-to-GO, place the DCDC2C emphasis in the PMID:28395323 abstract, and distinguish the PMID:18397884 abstract's CUL3-dependent TIP60 result from an unrecovered literal interaction record. Row 176 remains supported through the same-paper functional evidence and curated IPI, without claiming a recovered target pair. All 228 historical source objects, 132 reference identifiers/titles, three product objects and the core model remain unchanged.

The preceding support-consolidation statement describes the first whole draft. The final review restores the exact inherited PMID:24145166 Golgi-localization excerpt once on row 86. Its old duplicate on row 11 and the redundant RhoBTB3–cyclin-E sentence remain omitted; the two old PMID:14528312 excerpts do not resolve the distinct autoubiquitination assay and remain omitted. The 312 former Falcon support items are replaced by source-specific assessment, while the genuine Falcon document stays protected. The restored Golgi excerpt is inherited repository text, separately tracked from the ten newly selected primary anchors; no new quotation is added by this appendix.


## CUL3 finite external-review follow-up

The published source objects, all annotation actions, three products, existing support excerpts and one integrated core are retained. Extracellular-exosome row 171 remains KEEP_AS_NON_CORE because the original urinary-exosome table reports the exact CUL3 target; the one-peptide identification is limited evidence for a preparation-specific compartment, not evidence of a secretion mechanism or extracellular enzymatic role. Neither of the latter is required by the cellular-component term. PMID:19056867 is now MEDIUM relevance, while unrecovered CUL3-specific screen records in PMID:19946888 and PMID:40205054 are LOW relevance and remain UNVERIFIED.

The core explicitly incorporates BTB/POZ adaptor engagement within the scaffold assembly activity. GO:0160072 already describes bringing together an ubiquitin ligase and its substrate adaptor. The accepted POZ-domain binding refinements are preserved and supported in that same functional unit; no second copy of this assembly step is added solely because the same binding term occurs in multiple source rows.

The new CUL3-primary-source-notes.md gives DOI, printed-page and section locators for the adult renal study and both KLHL22 letters, with short exact anchors from the original PDFs. It corrects the previous row 65 statement: nephron qPCR maps Klhl3/Cul3 expression, whereas the adult-deletion work mainly measures protein abundance, phosphorylation and renal physiology. This does not establish CUL3 performing gene expression, so the source-specific over-annotation remains; no contrary experiment is invented. The independent stem-cell and cleavage source is PMID:22358839. Original publication caches and previous notes are unchanged.

GO_REF assessments now describe their particular mapping or inference methods. The screen-table access task formerly posed as the third expert question belongs here: unresolved interactions, homomeric binding and autoubiquitination require the original target assays before their uncertainty can be closed. Existing biological isoform and KLHL22 questions remain. Authored index spacing is corrected without changing literal source identifiers. The historical notes prefix and history records remain intact; prior text is superseded only where this appendix explicitly corrects it.
