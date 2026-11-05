# atsA (PA0183) review notes

## Literature search (2026-11-05)

No deep-research provider was available. PubMed MCP and Europe PMC search
endpoints failed during this session, so research used the cached GOA/UniProt
papers (PMID:7744061, PMID:9748219, PMID:19554727) plus PMID:11435113, fetched
with `ai-gene-review fetch-pmid`. All four are abstract-only in the cache.

## Findings

- Purified PAO1 arylsulfatase, sulfate-repressed, Km 105 microM for
  4-nitrocatechol sulfate; atsA cloned by complementation [PMID:7744061 "An
  arylsulfatase (EC 3.1.6.1) was extracted from Pseudomonas aeruginosa PAO1 and
  purified 2700-fold to homogeneity"].
- No signal peptide; presumed cytoplasmic [PMID:7744061 "The lack of this signal
  peptide suggests that the P. aeruginosa arylsulfatase is neither periplasmic nor
  membrane-associated"].
- Cys51 is converted to formylglycine; the Ser mutant is inactive [PMID:9748219].
- 1.3 A structure: formylglycine hydrate nucleophile, active-site Ca2+
  [PMID:11435113].
- Promiscuous phosphate monoester hydrolysis, kcat 620-fold below sulfatase
  [PMID:19554727 "Besides hydrolyzing sulfate monoesters, this enzyme catalyzes
  the hydrolysis of phosphate monoesters with multiple turnovers"]. PseudoCAP
  annotated this paper to GO:0008081 phosphoric *diester* hydrolase activity,
  which does not match the abstract (PSEUDOCAP WRONG_TERM defect, PROBABLE).

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | other seeds | IBD stands without this seed? | verdict | rationale |
|---|---|---|---|---|---|---|---|---|
| PTN000819263 | GO:0004065 arylsulfatase activity | 6 | 320 (50 taxa) | GO:0004065, IDA, PMID:7744061 (PseudoCAP; also UniProt IDA PMID:9748219) | human ARSA P15289, ARSL (formerly ARSE) P51690, ARSF P54793; mouse Arsg MGI:1921258; rat Arsg RGD:1310381 | Yes (human ARSA alone is a classic arylsulfatase) | SOUND | Purified enzyme assayed with 4-nitrocatechol sulfate. Node term fits an arylsulfatase clade. |

No GO_CENTRAL defect. The phosphodiester row does not seed a worklist IBD.
