# EIF2B4 review notes

## Source-specific reassessment

The review retains all 53 imported source contexts, including the four historical assertions absent from the current annotation feed. The current GOA contains 49 contexts; the exact earlier 57-row file is preserved in [the dated source snapshot](source-snapshots/2026-10-21-main-81298ef/EIF2B4-goa.tsv). Changes in feed coverage are provenance changes, not automatic biological rejections or retirement decisions. The distinct PMID:29599245 source is not replaced by PMID:29599213.

The integrated core describes delta's structural and regulatory contribution to eIF2B exchange and cytoplasmic translation initiation in cytosol. Positive human assembly/interface and patient-extract evidence is distinguished from hamster perturbations, the S. pombe structural preparation and whole-complex assays. Imported enables relations remain unchanged while three source-specific queries ask whether contributes_to better represents the evidence; these are conditional checks, not confirmed errors or an isolated-subunit activity requirement.

The native HeLa preparation in PMID:11323413 resolves cytoplasm. Target-resolved Reactome component 72521 independently supports the finer cytosol location. The T-cell stimulation results in PMID:8626696 show downstream whole-complex activation but leave delta's work in the T-cell receptor signaling process unresolved. PMID:15060152 reports negative isolated beta associations alongside positive multicomponent assembly; factor-binding refinements also cite independent human interface evidence.

The positive EIF2B4 clinical evidence in PMID:14566705 is kept separate from the negative isolated premature-ovarian-failure screen in PMID:15507143. Rat heat, glucose and peptide-hormone donor annotations retain their organismal and whole-complex limits. Unresolved clinical/developmental assertions are not called wrong-gene annotations merely because complete supporting evidence could not be recovered.

Three natural products of 523, 543 and 522 residues are preserved. The overexpressed 543-aa Flag construct called V1 in PMID:37014850 is not assigned to a UniProt product by length alone. Its free-delta sequestration and altered gamma/epsilon subcomplex models remain alternatives, not established autonomous delta exchange mechanisms. The product-comparison questions describe a testable uncertainty rather than a new process annotation.

Supported generic binding is retained as non-core when no evidence-backed narrower class is available, following the [ClinGen project policy](../../../projects/CLINGEN_MENDELIAN.md). Verified partner classes support refinements without requiring purified binary interfaces or transferring the partner's activity to delta. Reference-sequence checksums and assayed regions remain separate.

Three inherited publication supporting_text fields were removed after exact source checks: the noncontiguous PMID:8626696 excerpt and two copies of an unsupported PMID:29599213 paraphrase. Their reference IDs remain. All other inherited quotation occurrences are preserved. The retained generated-research excerpts are not upgraded to independently verified primary evidence.

The [source guide](EIF2B4-source-guide.md) gives the actual access scope, original locators and cache hashes. HTTP failures and no-result responses are retained in provenance; selected indexed originals are not described as complete papers. Normal publication flags remain exact. The [reproducible analysis](EIF2B4-bioinformatics/RESULTS.md) derives literal database joins from archived inputs without republishing article bodies.

## 2026-10-21: explicit source lifecycle decision and heat-response corroboration

This dated decision supersedes the earlier provisional statement that all four historical absences were retained without retirement. The complete fresh QuickGO query returned 49 annotations on one page and matches all 49 contexts in the normal-current GOA, including evidence, references, qualifiers and source identifiers. Historical indices 2, 6 and 7 (GO_REF:0000043) and index 13 (PMID:29599245) are now explicitly marked retired. All 53 review objects remain: 49 active and four retired. Retirement records disappearance from the current source snapshot, not a biological REMOVE judgment; the original source identities, scientific reviews and dated old GOA snapshot are preserved. PMID:29599245 remains distinct from PMID:29599213.

The clinical PMID:12499492 heat-response row is retained as non-core using independent corroboration from the rat Q63186 IDA evidence in PMID:9341116. That study's authentic abstract describes heat-dependent regulation of whole eIF2B in rat H35 cells. It does not identify delta as a temperature sensor or supply a direct human delta perturbation. The clinical paper remains abstract-only, its exact delta-specific evidence is unresolved, and its inherited supporting text is unchanged. Corroborating the biological annotation does not claim recovery of the clinical paper's complete experiments.

The revised disposition counts are 21 ACCEPT, 18 MODIFY, 12 KEEP_AS_NON_CORE and two UNDECIDED across the 53 retained objects. All 83 supporting_text occurrences, the integrated core and three product objects are unchanged.
