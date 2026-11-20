# H3-3A curation notes

## 2026-11-09 — resumed intake

The current official HGNC symbol is H3-3A (HGNC:4764; historical H3F3A/H3F3). The fetched reviewed UniProt entry P84243 represents the identical H3.3 protein encoded by H3-3A and H3-3B. Evidence about purified H3.3, mass-spectrometric peptides, or an unspecified H3.3 expression construct does not by itself distinguish those loci. Retain that distinction when describing the product and experimental provenance. [UniProt:P84243, GN and sequence records]

`just fetch-gene human H3-3A --uniprot-id P84243 --no-fetch-titles` retrieved 147 raw QuickGO records and generated 146 annotation stubs. The TSV is byte-identical to the retained 2026-11-07 forecast. A fresh complete-object comparison also confirms all 147 original records, including the three annotation-extension atoms. One pair projects to the same TSV row despite different context: the two PMID:20458337 extracellular-exosome assertions. The extended context must remain a distinct review row. Source identifiers, evidence codes, WITH/FROM values, qualifiers and extensions are machine assertions to preserve; preservation does not constitute biological acceptance.

The usual Falcon deep-research call failed authentication (403). Its configured Perplexity-lite fallback failed with insufficient quota (401). No provider report was obtained. Research for this review will therefore be documented as manual primary-source reading, without fabricating a provider-labelled report.

The ordinary publication helper cached all 29 GOA-cited PMIDs, reusing existing cache entries. Several remain abstract-only; full-text and supplement availability will be reported separately from whether a relevant experiment was actually inspected. No source cache has been manually rewritten.

The ClinGen project instruction applies: retain a supported generic protein-binding assertion as KEEP_AS_NON_CORE unless a more informative activity is demonstrated; use UNDECIDED for evidence that cannot be adjudicated. This does not infer an endogenous function from a physical association.

The retained PMID:19633671 material supports four incoming records (raw 0, 1, 36 and 143), not only the three listed in the old reserved-slice note. The paper examines H3.3/H2A.Z nucleosome occupancy; evaluation of sequence-specific DNA recognition will use its actual methods and the checked term ancestry.

## 2026-11-09 — completed annotation assessment

All 147 incoming contexts have decisions: 103 ACCEPT, 33 KEEP_AS_NON_CORE, seven UNDECIDED, two MODIFY, one TOO_GENERAL and one MARK_AS_OVER_ANNOTATED. There are no PENDING or NEW rows. The two molecular-function replacements point to an already represented term; they are not additional annotation proposals. The review remains DRAFT because the unresolved source questions are explicit.

The three extension atoms and the distinct exosome contexts were independently replayed against the complete original records. Separate readers examined interaction evidence, Reactome participant paths, PAINT ancestry and the primary experimental assertions. The [source guide](H3-3A-source-guide.md) distinguishes normal-cache availability from sections actually inspected through other primary routes.

Focused validation passed with 30 warnings: 28 supported generic binding rows retained under the ClinGen instruction; one binding row with a demonstrated mutant-context overreach; and one cross-context nucleus-action warning. The sperm proteomics assertion is unresolved while other nuclear-localization evidence is accepted. These source-specific distinctions are intentional.

## 2026-11-10 — PR scientific follow-up

The DAXX claim from the unverified AP-MS source is now retained as non-core on independent binding evidence [PMID:20211137; PMID:20504901]. Its original source remains UNVERIFIED. The growth-regulation judgment now flags over-annotation: the inspected assay measures proliferation, whereas the GO term concerns individual-cell growth [PMID:21274551]. Earlier session counts above remain historical. Current counts are 103 ACCEPT, 33 KEEP_AS_NON_CORE, six UNDECIDED, two MODIFY, two MARK_AS_OVER_ANNOTATED and one TOO_GENERAL. No machine context or extension was changed.

The source caution was checked: [PMID:27392148] retracts [PMID:22483618]; [PMID:27735137] is a subsequent report with overlapping authors. Only their abstracts/notice metadata were read. Neither report supplies an annotation or core-function assertion here. The description's disease context does not create a normal-function annotation from a pathogenic substitution.

Project completion is recorded by the coordinator after the actual merge and successful integration checks, following the review-progress ownership rule. It is not withheld merely because this review remains DRAFT.
