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
