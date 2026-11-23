# pdha-1 review notes

## 2026-10-28 session

- fetch-gene resolved P52899 (ODPA_CAEEL, Swiss-Prot, WormBase WBGene00011510, GeneID 3565996). 9 GOA rows.
- No deep research API; manual summary in pdha-1-deep-research-manual.md.
- PMID:15340492 (mmBCFA paper) was requested as a key paper. Read in full: its only pdha-1 content is one
  sentence citing unpublished RNAi data [PMID:15340492 "RNAi suppression of another predicted component of the
  BCKAD complex, pyruvate dehydrogenase (T05H10.6), resulted in a similar decrease in C15ISO and C17ISO
  (unpublished data)"]. This calls T05H10.6 a BCKAD component, which is inaccurate (it is the PDH E1 alpha,
  PTHR11516/TIGR03182 PDH_E1_alph_y). Not used for any GO term; no NEW BP proposed (RNAi phenotype, unpublished,
  indirect). Not a GOA source so no source_defects entry.
- RNAi literature (PMID:24445252, PMID:42844987, PMID:21533078, PMID:30586284) consistently shows PDH-deficiency
  phenotypes (elevated alanine/lactate, lethality/sterility, UPRmt) - necessity evidence supporting the IBA
  process row, not a basis for new process terms.
- MF qualifier: E1 is an alpha2beta2 heterotetramer with ThDP bound at the alpha/beta interface
  [uniprot "ligand shared with beta subunit"]. Core function uses contributes_to_molecular_function GO:0004739.
  The two enables rows are accepted for the term but recorded with WRONG_QUALIFIER source defects (PROBABLE).
  Note other reviews in the repo (human PDHA1, yeast PDA1) keep enables; this is a convention question raised in
  suggested_questions.
- GO:0005967 mitochondrial PDH complex is obsolete (OAK), so GO:0045254 stays as is.
- GO:0016624 is an ancestor of GO:0004739 (OLS getAncestors), so the InterPro2GO row is MODIFY -> GO:0004739.
