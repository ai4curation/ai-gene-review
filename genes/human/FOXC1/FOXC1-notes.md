# FOXC1 review notes

## 2026-10-31 — initial review

Human FOXC1 (Q12948) was genuinely imported from UniProt and QuickGO before curation. The 143 original contexts project to 141 stored annotations; both duplicate groups and all three singleton annotation extensions are retained with their original source objects. The reviewed record has a 553-amino-acid displayed sequence and no enumerated alternative natural products.

The one core function is selective cis-regulatory DNA binding coupled to positive RNA polymerase II transcription in the nucleus. Original human WT reporter and endogenous promoter evidence supports that synthesis. Direct transcriptional targets, partner-mediated effects, mouse developmental consequences and cancer-context perturbations are kept distinct. The [source guide](FOXC1-source-guide.md) and [evidence map](FOXC1-source-evidence.md) document selected original reading, abstract-only evidence, construct/species limits and unresolved assays.

The applied decisions are 37 ACCEPT, 47 KEEP_AS_NON_CORE, 38 TOO_GENERAL, 4 MODIFY and 15 UNDECIDED. Four supported binding refinements use filamin binding or RNA polymerase II-specific DNA-binding transcription-factor binding. Supported generic associations remain non-core where a functional subtype is not established. Inaccessible experimental detail is not treated as refutation. No NEW annotations, publication quotations or invented natural products were added.

All 40 normal dependencies are preserved byte-for-byte after genuine acquisition or exact-main hydration: 37 publications and three PANTHER files. The seven auxiliary donor papers support existing transfer contexts. Source flags are not full-paper reading claims. Six IBA origins were independently replayed; two donor/date snapshot differences remain explicitly recorded without source repair.

The candidate was applied after independent scientific review of the molecular-function, biological-process, cellular-component and binding proposals. Validation results will be appended after execution.

## Validation outcome

Default schema, reference-title, best-practice and ontology-term validation passed with 14 advisories. Strict GOA comparison passed, and the repository status computation resolves this candidate to DRAFT. The advisories are three intentionally retained generic-binding contexts, five term-level action differences caused by explicit source-specific uncertainty, and six accepted contexts without a supported_by entry. The exact source citations and rationale remain in those rows; no publication quotations were added to suppress a warning. The environment also emits a pkg_resources deprecation notice.

Exact conservation checks passed for all 143 original objects, 141 reviewed annotations, three extension atoms, 45 reference entries and 40 unchanged normal sources. The genuine CLI-generated history validates, and the private HTML render completes. Initial unpublished extension predicates were corrected from objects to the schema's required strings; an independent source check removed the unsupported BT549 description and retained only the checkable MDA-MB-231, mouse 4T1 and human nuclear-immunohistochemistry evidence. Neither correction changed an annotation decision. The initial status command reported the existing INITIALIZED mismatch without rewriting it; the repository's computed DRAFT result was then applied and the status check passed.

A further check of the retained PMID:20406990 extracts did not verify the earlier BT549/S8 inference. The current three rationales and source assessment therefore use only the checkable human MDA-MB-231 overexpression, mouse 4T1 knockdown and human nuclear immunohistochemistry. The earlier reading note is preserved with an additive superseding correction; all annotation actions and the core function remain unchanged.

### Final reference-support check

Six accepted source contexts now explicitly link their already-read original paper through reference-only supported_by entries: stored rows 56, 62, 68, 69, 117 and 119. No quotation, annotation action, rationale, core function or source field changed. Final default validation passed with eight remaining advisories: three retained generic-binding contexts and five source-specific same-term action differences. The earlier 14-advisory outcome above is retained as the preceding validation record. Conservation, final history and private rendering were checked again for the completed candidate.
