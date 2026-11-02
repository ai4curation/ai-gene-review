# PIK3CD curation notes

## 2026-05-12 Falcon integration

Generated Falcon deep research at `PIK3CD-deep-research-falcon.md` and used it with
UniProt plus cached publications to complete the initialized GO review.

Core synthesis: PIK3CD encodes p110delta, a leukocyte-enriched class IA PI3K
catalytic subunit. The central molecular function is PI(4,5)P2 3-kinase
activity producing PIP3 in p85-family regulatory complexes at receptor-activated
membranes. Falcon summarizes this as: [file:human/PIK3CD/PIK3CD-deep-research-falcon.md
"**PIK3CD** encodes the catalytic subunit **p110δ** of **class IA phosphoinositide
3-kinase (PI3Kδ)**, a lipid kinase that produces **PI(3,4,5)P3 (PIP3)** at
membranes downstream of receptor signaling in immune cells, particularly in
lymphocytes."] Direct biochemical work also reports that recombinant p110delta
phosphorylates phosphatidylinositol and associates with p85 [PMID:9235916
"Recombinant p110delta phosphorylates phosphatidylinositol and coimmunoprecipitates
with p85."].

The most informative process terms are PI3K/AKT signaling plus immune receptor
contexts, especially BCR, TCR, and CD28. Falcon frames the receptor context as
[file:human/PIK3CD/PIK3CD-deep-research-falcon.md "In immune cells, class IA PI3K
(including p110δ) propagates signaling downstream of **BCR, TCR, CD28, ICOS,
CD19, BAFF-R, CD40**"] and UniProt separately records BCR and TCR requirements
[file:human/PIK3CD/PIK3CD-uniprot.txt "Required for B-cell receptor (BCR) signaling."]
[file:human/PIK3CD/PIK3CD-uniprot.txt "Required for T-cell receptor (TCR) signaling."].

Broad immune, chemotaxis, endothelial migration, angiogenesis, mast-cell,
neutrophil, NK-cell, and cytokine-production annotations were retained as
non-core where supported. The main evidence is that PI3Kdelta participates in
multiple leukocyte outputs [PMID:20940048 "PI3Kδ participates in the
development, activation and migration of T cells and NK cells."] and myeloid
activities [PMID:20940048 "The role of PI3Kδ in myeloid cell activities, such
as inflammation driven cell infiltration, neutrophil oxidative burst, immune
complex mediated macrophage activation, as well as mast cell maturation and
degranulation, has been well illustrated in various studies."].

Several terms were deliberately modified or marked over-annotated:

- Generic PI3K complex was modified to class IA PI3K complex.
- Generic kinase/transferase/nucleotide-binding terms were narrowed toward ATP
  binding or PI(4,5)P2 3-kinase activity.
- PI3P biosynthetic process was modified because that term implies class
  III/VPS34-like biology; PIK3CD is primarily a PIP3-producing class IA kinase.
- Protein binding was marked over-annotated because complex membership and lipid
  kinase activity are the informative annotations.
- Protein phosphorylation was modified because PMID:9113989 supports lipid
  substrate specificity and says p110delta does not phosphorylate p85
  [PMID:9113989 "Unlike p110alpha, p110delta does not phosphorylate p85 but
  instead harbors an intrinsic autophosphorylation capacity."].


## 2026-10-26 full annotation audit: evidence review in progress

The preserved acquisition baseline and raw-file hashes are in `.cache/module-audit-logs/b-cell-panel-baseline.json`. This review covers all annotations, including functions outside B-cell signaling. Normal acquisition and actual provider attempts are recorded in `b-cell-acquisition-report.md` and `b-cell-fetch/provider-publication-results.json`; provider failures are not research reports. Existing genuine exact-target reports, where available, are discovery aids. Original machine annotation payloads and raw source records will be preserved.


## 2026-10-26 completed full annotation audit

p110δ catalyzes the major PIP3-generating class IA reaction, but its experimentally documented PI and PI4P substrate activities are not false. PI3P biosynthesis and the corresponding kinase activities are retained as secondary chemistry. PMID:10064595 identifies Ser1039 autophosphorylation, so the general protein-phosphorylation row is refined to autophosphorylation and the serine kinase activity is preserved. Phosphosite evidence in cells does not automatically identify the in-cell phosphodonor.

The full angiogenesis paper PMID:31915155 combines native human endothelial experiments with mouse oxygen-induced retinopathy, supporting a specific angiogenesis refinement of generic development/morphogenesis. PMID:22079609 supports selected protein-expression effects, while the stromal chemokine study PMID:24009720 is native mouse evidence and is labeled accordingly. Integral ATP binding is core. Neutrophil positive-apoptosis claims remain unresolved because the accessible PMID:25339672 evidence does not isolate the delta-specific mechanism and death mode. These are claim-level uncertainties, not penalties for an evidence code.

All 114 original annotation payloads, including qualifiers and any negation flags, were preserved; no NEW assertions were added. Normal source acquisition and actual provider outcomes are retained in the acquisition logs. Failed provider calls were not replaced with fabricated reports. Source-access limits are recorded above and in the individual row reasons; partial publisher pages and captcha responses were not treated as full articles. The six-member focused strict/schema, GO-term and source-quotation check passed with zero errors and warnings before final packaging; the final package reruns those checks after finding additions. Record-section backfill, HTML rendering, helper-generated Codex provenance and exact payload/raw-hash checks accompany the package.
