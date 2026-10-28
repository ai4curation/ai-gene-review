# FLNC review notes

## 2026-10-28 — initial annotation review

Applied the annotation-reviewer and core-function-synthesizer criteria to the genuine human FLNC seed and the independently reviewed primary-source consultations. All 32 original contexts map one-to-one to 32 stored review rows. Final planned decisions are 11 ACCEPT, 8 KEEP_AS_NON_CORE, 9 MODIFY and 4 TOO_GENERAL. There are no NEW annotations, no publication quotations, two unchanged natural products and one structural core.

The core combines actin-filament binding, sarcomere organization and documented muscle structural contacts. It does not transfer myotilin's proposed alpha-actinin bridge, Xin's other ligand interfaces or ankyrin's membrane behavior to a separate FLNC activity. [PMID:11038172](https://pubmed.ncbi.nlm.nih.gov/11038172/), [PMID:16076904](https://pubmed.ncbi.nlm.nih.gov/16076904/), [PMID:34405687](https://pubmed.ncbi.nlm.nih.gov/34405687/)

Nine generic-binding contexts receive informative evidence-backed subtypes. The two remaining generic associations are supported but lack an established narrower FLNC activity and remain non-core under the campaign instruction. Exact pair, fragment, species and natural-product limits are retained. Product 2's 1734–1766 deletion overlaps one tested SH3-binding peptide but not the separately positive 260–273 peptide; no complete binding loss is inferred.

The original raw4 occurs_in GO:0014704 extension and all original partner/context fields are retained in the context guide and typed projection proof. The source's human/chicken nebulette contexts, rat O70511-7 Ank3 context and mouse/rat donor transfers are not silently relabeled. The experimental PMID:12393796 cytoplasm assertion is not rejected because the selected primary sections foreground other filamins; its correct broad compartment is covered by independent target evidence, and exact source-specific FLNC support remains explicitly unverified.

Eleven existing main sources were hydrated and hash-checked before genuine fetch. Six absent publications were fetched normally, including the additional mouse-donor PMID:16914736. All 17 normal sources are present, with existing bytes preserved. PTHR38537 sources are reused unchanged from accepted FLNA work; its genuine single plant-branch PAINT record is not on the human target path, and FLNC has no incoming IBA. No bulk family archive was downloaded. Existing provider credential/quota failures were not retried; the evidence synthesis honestly records manual primary research rather than a fabricated provider report.

The [evidence synthesis](FLNC-source-evidence.md) and [source guide](FLNC-source-guide.md) preserve actual reading limits, original URLs, ontology paths, source identities and product boundaries. Validation and independent canonical peer review follow the scientific authoring; their results will be appended here.

## Validation and independent canonical QA

All seven scoped checks passed: schema/best practices/term and reference checks, strict GOA matching, history schema, deterministic status, private rendering and whitespace checks. The status remains DRAFT. Exactly two advisories concern the supported FBXL22/RTF2 generic-binding rows retained as non-core under the campaign instruction; these are not unresolved interaction claims. The PMID markdown helper found no pathway files and did not validate these notes. The shared runtime emitted a dependency deprecation warning; no environment was created. Independent canonical peer review read all 32 decisions and supporting documents, replayed exact seed/context/product preservation and found no scientific issue. Two duplicated citation prefixes were then corrected without changing any assertion.
