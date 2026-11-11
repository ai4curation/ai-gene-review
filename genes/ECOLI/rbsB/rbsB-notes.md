# rbsB (Escherichia coli K-12, P02925) curation notes

## 2026-11-11 initial review

- Reviewed as the E. coli exemplar of the RbsB periplasmic D-ribose-binding subunit of the RbsABC importer in `modules/bacterial_ribose_uptake_and_entry.yaml`.
- Deep research was not run: no deep-research provider credentials were available in this environment,
  and no `-deep-research-<provider>.md` file was created. The review relies on the cached publications
  cited by GOA (`publications/PMID_*.md`, mostly abstract-only) and the curated UniProt record.
- RbsB binds beta-D-ribopyranose tightly and specifically [PMID:1583688 "giving rise to tight binding
  (0.1 microM for ribose) and high specificity"]. It has two roles, transport and chemotaxis via Trg
  [PMID:1304894 "Ribose-binding protein is a bifunctional soluble receptor found in the periplasm of
  Escherichia coli."].
- The four bare protein-binding rows (IleS by TAP and by Y2H, a cross-linking partner, and RbsC) were removed
  under the protein-binding policy. Complex membership is captured by GO:0055052.
- Refinements with MODIFY: periplasmic space to outer membrane-bounded periplasmic space, and transmembrane
  transport to D-ribose transmembrane transport. The two generic membrane rows are marked over-annotated,
  because RbsB is a soluble periplasmic protein that docks on RbsC only transiently.
- OLS shows that GO:0048029 monosaccharide binding has no ribose-specific child. A D-ribose binding term is
  proposed, and the RbsB-Trg docking activity behind chemotaxis is raised as a suggested question.
