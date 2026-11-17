# PA0655 (coq7) review notes (P. aeruginosa PAO1, Q9I5R6)

Reviewed for the ubiquinone_biosynthesis module (Coq7 late hydroxylase
variant); compared read-only with genes/PSEPK/coq7 and genes/human/COQ7.

## Provenance

- No deep-research provider was available (no API keys); no
  `-deep-research-<provider>.md` file exists or was fabricated. Built from the
  reviewed UniProt record, the cached abstract of PMID:11435415 and the
  PTHR11237 PAINT table.

## Function

- Coq7 is a di-iron hydroxylase. [PMID:11435415 "Here we identify Coq7 as
  belonging to a family of a di-iron containing oxidases/hydroxylases based on a
  conserved sequence motif for the iron ligands, supporting a direct function of
  Coq7 as a hydroxylase."]
- P. aeruginosa coq7 replaces E. coli UbiF. [PMID:11435415 "show that indeed
  this gene complements an Escherichia coli mutant that lacks an unrelated
  5-demethoxyubiquinone hydroxylase"]
- P. aeruginosa makes UQ9. [PMID:32409583 "we established that UQ9 is the major
  quinone of Pseudomonas aeruginosa"]

## Decisions and sibling consistency

- Monooxygenase (InterPro, IGI) and oxidoreductase (ARBA): MODIFY to GO:0008682.
  Human COQ7 and the P. putida coq7 draft marked monooxygenase
  MARK_AS_OVER_ANNOTATED; MODIFY follows the correct-but-general rule.
- Plasma membrane (HAMAP) ACCEPT, as for P. putida coq7 and the module;
  membrane (NAS) MODIFY to plasma membrane.
- GO:0160224 (NADH) IBA ACCEPT, as for human COQ7; the bacterial electron donor
  is untested (suggested experiment).
