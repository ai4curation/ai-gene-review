# pbpG (PSEPK, UniProt Q88GD0) curation notes

## 2026-11-04 (Claude, AI-assisted), PR #5959 review follow-up

- The PMID:8063800 quote ("PBP7/8, recently shown to be a DD-endopeptidase, bind
  to Slt70 in vitro.") is an Slt70-binding result and had been used as support for
  five rows. Those rows now cite the primary E. coli PBP7 enzymology,
  PMID:7925376, and the two NEW ISS rows now have it as their original reference.
- The NEW row GO:0031504 peptidoglycan-based cell wall organization was dropped,
  and the term was removed from core_functions. The only evidence is ortholog
  phenotype data (PMID:16855223, "These functions may be responsible for the
  contributions of PBPs 4 and 7 to the generation of regular cell shape and the
  production of normal biofilms."), which is hedged. E. coli PBP7's role there is
  explicitly secondary to PBP4's ("Another endopeptidase, PBP 7, fulfills a
  secondary role."). That does not clear the conservative bar for a NEW process
  term on an unassayed ortholog. GO:0000270 still captures the protein's direct
  participation in peptidoglycan metabolism.
- The GO:0006508 InterPro2GO removal is recorded as a source_defect, consistently
  with the sibling PBP4/PBP7 reviews.
