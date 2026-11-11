# A0A1S3BTE3 (Cucumis melo LOC103492960) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 files were not opened or used.

### Identity
- A0A1S3BTE3 is the 492-aa product XP_008451774.1 of LOC103492960 (chromosome 7). Its 492-aa
  length and 56.6 kDa MW match CmMAPK19 (MELO3C016139) in the melon MAPK survey
  [PMID:32407323 "the remaining 7 members were assigned to group D (CmMAPK9-1, CmMAPK9-2, CmMAPK9-4, CmMAPK16, CmMAPK19, CmMAPK20-1 and CmMAPK20-2)"].
- It is not a fragment. Of the four UniProt entries for LOC103492960 (A0A1S3BTE3 492 aa,
  A0A1S3BRP7 423, A0A1S3BSC0 422, A0A1S3BS89 410), it is the longest. None is reviewed, so
  there is no separate canonical product to review. The kinase domain (25-316) is complete.
  The protein is shorter than Arabidopsis MPK18/19/20 (598-615 aa) only in the group D
  C-terminal extension.

### Evolutionary placement (A0A1S3BTE3-bioinformatics/RESULTS.md)
- Catalytic residues K54, D151 (HRD) and D169 (DFG) are intact, and the activation loop has
  TDY at 187-189, which makes this a group D MAPK.
- NJ tree with all 20 Arabidopsis MPKs: the target falls in the MPK18/MPK19/MPK20 clade,
  sister to MPK18+MPK19. Identities: MPK19 73.5%, MPK18 72.4%, MPK20 70.2%.
- The target's PANTHER subfamily is not obtainable: InterPro and UniProt give only PTHR24055,
  and melon is not a PANTHER genome. The three Arabidopsis relatives sit in three different
  subfamilies (SF420 MPK18, SF200 MPK19, SF392 MPK20).
- PAINT: PTHR24055's only GO:0004707 IBD node (PTN001171896) is seeded by fungal genes
  only. The family-root node PTN000622075, which has plant seeds including AT1G53510/MPK18,
  carries GO:0004674, nucleus, cytoplasm and intracellular signal transduction. The target
  has no IBA rows, presumably because melon is not in the PANTHER tree. I did not add NEW
  location terms; this is a curation gap, not a knowledge gap.

### Decisions
- MAP kinase activity: ACCEPT (core). MAPK cascade: ACCEPT. ATP binding and protein serine
  kinase activity: KEEP_AS_NON_CORE. GO:0106310 is not an ancestor of GO:0004707 (OLS check).
- Nucleotide binding and signal transduction were changed from MARK_AS_OVER_ANNOTATED to
  TOO_GENERAL. Both are true, and each is entailed by a more specific accepted term.
- Supporting quotes no longer rely on ARBA-derived UniProt text (name, EC, Rhea reactions,
  "Belongs to" note). Support now comes from PROSITE/CDD signatures, the ProRule binding
  site, the new phylogeny and PMID:32407323.
- The MPK18 microtubule function [PMID:19392697 "Mutant mpk18 seedlings show defects in microtubule-related functions, and have moderately stabilized microtubules."]
  is not transferred, because the subfamily is unresolved. MKKK20 can phosphorylate MPK18
  directly [PMID:28848569 "In vitro phosphorylation assays showed that MKKK20 phosphorylates both MKK3 and MPK18."],
  so the upstream wiring of this clade may be non-canonical.
- The falcon deep research is generic (plant MAPK reviews) and adds no gene-specific
  evidence.

### Relative to review next
Arabidopsis MPK18 (Q9C5C0, PANTHER SF420) is the best-characterised member of the clade.
The repo has no review for it, nor for MPK19 or MPK20.
