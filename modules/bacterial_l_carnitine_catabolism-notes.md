# L-carnitine catabolism audit

## 2026-11-07 — evidence and taxon boundary

The modeled three-reaction mechanism starts at free L-carnitine and ends at glycine betaine. Pseudomonadota is retained because both gamma- and alphaproteobacterial realizations are supported. This is an occurrence envelope, not universal presence. The prior module has already been curated in PR5954; this audit adds systematic literature assessment, source-matched gene reviews, family scrutiny and pathway-capacity checks.

Four reviews were located and manually assessed: PMID9037756 (historical bacterial pathways), PMID9706218 (microbial and mammalian metabolism), PMID25787873 (bacterial physiology and distinct carnitine fates), and PMID23354714 (choline/GB homeostasis). All four protected caches are abstract-only. For 25787873, attempted PMC/publisher routes returned challenges, EuropePMC returned an error, and NCBI efetch explicitly stated that the publisher does not allow full-text XML download. No full-text review section is claimed read. Findings are limited to the accessible abstracts; primary sources and preserved source-analysis consultations support detailed reaction and strain assertions. The exact three-step mechanism postdates the 1997/1998 reviews.

PMID3058208 concerns P. putida IFP206, not KT2440. The official 24240508 supplementary datasets nevertheless contain direct KT2440 PP_0303 screening as BKACE511. Those signals must not be silently converted to accepted activities without the statistical cutoff, nor dismissed because KT2440 was once called unassayed. PAO1 BKACE529 is not in the accessible screening table; publication-linked curated reaction evidence is distinguished from a target assay read firsthand. See psepk-consultation/evidence.md and exact archived publisher spreadsheets.

The 2019 Sinorhizobium primary study uses cloned 3D0a2 proteins and Rm2011 genetics. Independent sequence matching bridges to the 1021 review representatives, while native 1021 GBB growth failure remains explicit. BcoEF performs three measured activities: carnitine oxidation, betainyl-CoA hydrolysis and upstream carnitinyl-CoA hydrolysis. The module uses only the first two. BcoG catalysis is demonstrated, but BcoG was not in the reported mutant set; its inherited IMP proposal is archived and explicitly retired. The source-derived row and NEW action are retained.

PMID40853000 is a recent boundary comparator. CJ25 produces GB anaerobically, but its metabolomic/proteomic FadJ/FadI hypothesis does not establish this module's CdhC/betainyl-CoA reaction chain. Shared end products or substrate-dependent growth do not substitute for the missing enzymatic assignments.

The module Falcon request failed with HTTP 403; the genuine failure log remains in ignored cache. No handwritten provider report was created. Individual consultations reuse genuine existing research where available and document their own provider-access outcomes.

Current state: literature and module boundary revised; RHIME pair validated and frozen; PSEPK/PSEAE gene reviews and five family reviews are being finalized. Full module/capacity/full-corpus checks and the dedicated PR remain pending. This is not a completion record.

## Further literature access

PMID17910757 adds a fifth review, with full text available. Its comparative pathway section supports the oxidation step and alternative-route boundaries, while its Rhizobium-like production discussion separates synthesis from degradation. The cache classifies it as PRIMARY_RESEARCH; manual reference metadata correctly records REVIEW without rewriting the source. The module now assesses eleven references.

## 2026-11-07 — focused audit complete

Comparative audit ready for full validation: 11 manually assessed references including five reviews; 14 COMPLETE gene reviews, five family reviews and 49 capacity cases with 14 module mutations and five sensitivity checks. All ordered source rows preserved; three inherited proposals explicitly retired. Dedicated PR and actual merge pending.

The added 2007 review is available in full text. Its manually recorded review classification differs from the fetched machine classification; the immutable cache remains unchanged. Final consultations and capacity evidence are linked in the audit README.


## 2026-11-07 — PR #6182 evidence clarification

Expanded three truncated review quotations to complete source clauses, checked against the unchanged cached publications (PMIDs 9037756, 25787873, 23354714). The module retains its reaction boundary and family/activity/interface gates. Round-one gene follow-up retires two redundant historical proposals without deleting them and represents PP_0303 chemistry by its exact proposed activity; source-specific transport evidence is reviewed separately.


## 2026-11-08 — canonical CbcW review

The duplicate Q9HTI7/PA5377 review is consolidated into genes/PSEAE/cbcW/cbcW-ai-review.yaml, which is authoritative for the module. All 25 source rows and the GO_CENTRAL/PSEUDOCAP defect records are retained. CbcW contributes the membrane component of the shared QAC ABC importer; CaiX provides carnitine specificity. The older raw records and history remain traceable through the canonical folder and the consolidation receipt.
