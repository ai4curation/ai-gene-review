# JAK3 notes

Deep research (falcon / perplexity-lite) failed (providers unavailable). Notes from cached publications and UniProt P52333.

- Binds C-terminal region of IL2RG (gamma c); JAK1 binds IL2RB [PMID:7973658 "Jak1 and Jak3 associated with IL-2R beta and gamma c, respectively"].
- Reconstitutes IL-2 signaling in JAK3-negative fibroblasts [PMID:7973659].
- Activated by IL-2/IL-15 in T cells [PMID:7568001], IL-7 in thymocytes and pre-B cells [PMID:9182906], associates with IL4R in B cells [PMID:7538655].
- Autophosphorylation Y904/Y939 positively regulates kinase activity [PMID:18250158].
- TCPTP dephosphorylates JAK3 [PMID:11909529].
- JAK3 deficiency -> SCID [PMID:19290934]; mouse KO loses gammadelta T and NK, reduced alphabeta [PMID:9973401].
- GHR binding/GH signaling IBA from JAK family node; JAK3 is gamma c-specific -> marked over-annotated.

Localization: cytoplasmic, peripheral on cytoplasmic face of PM bound to gamma c; no extracellular exposure.

## 2026-11-23 ORGANELLES endosome batch 1

- Two GO:0005768 rows: IEA ARBA00028568 (unvetted ML rule) and Reactome TAS R-HSA-8983335 (black-box IL15/IL15RA recycling event; JAK3 included as part of the modelled complex).
- Line found and cached: [PMID:15143194 "Without gamma(c), Jak3 localized in the cytosol, whereas in the presence of the receptor, it colocalized with gamma(c) in endosomes and at the plasma membrane."] Abstract only; PMC416416 returned no full text. MeSH lists COS and HeLa cells, so probably co-expression in non-lymphoid cells.
- Both rows KEEP_AS_NON_CORE (unchanged) on abstract deference (rule 9), recorded as the weakest of the three JAK lines; MARK_AS_OVER_ANNOTATED if the full text shows only co-overexpression in foreign cells. PMID:26306492 (IL-4R dimers in endosomes) does not localise JAK3 in its abstract and was not used.
- The endomembrane-system row's supported_by no longer uses the shared YAML alias of the endosome rows (content unchanged).
