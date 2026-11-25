

## 2026-10-26 full annotation audit: evidence review in progress

The preserved acquisition baseline and raw-file hashes are in `.cache/module-audit-logs/b-cell-panel-baseline.json`. This review covers all annotations, including functions outside B-cell signaling. Normal acquisition and actual provider attempts are recorded in `b-cell-acquisition-report.md` and `b-cell-fetch/provider-publication-results.json`; provider failures are not research reports. Existing genuine exact-target reports, where available, are discovery aids. Original machine annotation payloads and raw source records will be preserved.


## 2026-10-26 completed full annotation audit

p110γ belongs to class IB complexes with p101 or p84/p87, not class IA p85 complexes. PMID:7624799 explicitly reports lack of p85 interaction, and PMID:10358071 characterizes the p101 complex. The original class IA rows, including the PAINT PTN000799659 row, are retained as machine payloads and corrected to the proper complex type with explicit propagation metadata.

The human p110γ comparator in full PMID:16123124 produces PI3P, PI(3,4)P2 and PIP3. The first two are real biochemical substrate activities, retained as non-core instead of being dismissed because class I enzymes primarily signal through PIP3. Protein serine kinase activity is also real: PMID:12502714 maps Ser1101 autophosphorylation, and PMID:16094730 tests tropomyosin phosphorylation. The broad kinase refinement retains both lipid and protein kinase chemistry.

GPCR regulation is a major route, not an exclusive mechanism. PMID:23824069 supports PKCβ-dependent activation after FcεRI stimulation. Cardiac scaffolding/cAMP regulation and immune-cell migration, respiratory burst and activation remain context-specific functions; human p110γ deficiency in PMID:31554793 can increase selected myeloid cytokines, so cytokine direction is not universal. Glucose homeostasis and exact self-association claims remain unresolved where the cited isoform or assay cannot be established. Gamma remains a full standalone review even though it is not the default p85-associated BCR lipid kinase.

All 102 original annotation payloads, including qualifiers and any negation flags, were preserved; no NEW assertions were added. Normal source acquisition and actual provider outcomes are retained in the acquisition logs. Failed provider calls were not replaced with fabricated reports. Source-access limits are recorded above and in the individual row reasons; partial publisher pages and captcha responses were not treated as full articles. The six-member focused strict/schema, GO-term and source-quotation check passed with zero errors and warnings before final packaging; the final package reruns those checks after finding additions. Record-section backfill, HTML rendering, helper-generated Codex provenance and exact payload/raw-hash checks accompany the package.
