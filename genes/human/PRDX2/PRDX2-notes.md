# PRDX2 notes

## 2026-11-28 PTHR10681 human family review

Automated Falcon deep research was attempted only on the first gene in the family and failed because
the local deep-research client had no non-Claude provider available. No extra sub-workers were allowed
for this campaign, so this review used manual literature triage from the seeded GOA references, the
UniProt record, Reactome records, and the existing PTHR10681 family review.

Key evidence:

- PMID:8554614 identifies human red-cell PRP/PRDX2 as a thioredoxin/thioredoxin-reductase-linked
  peroxidase.
- PMID:9497357 shows that recombinant Prx I, II, and III have peroxidase activity, use thioredoxin
  as reducing equivalents for H2O2 reduction, and places Prx I/II in the cytosol.
- PMID:8144038 cloned the human PRP cDNA and showed that expression in E. coli yielded an active
  thiol-specific antioxidant protein.
- PMID:12943237 supports a non-core oxidative-stress/apoptosis phenotype after PRDX2 knockdown in
  SH-SY5Y neuroblastoma cells.
- PMID:20978343 is mouse VSMC work in which Cd36/Nrf2 signaling changes Prdx2 abundance; it does
  not directly show that PRDX2 removes superoxide radicals.

Decisions:

- The core retained function is cytosolic thioredoxin-dependent peroxiredoxin activity in hydrogen
  peroxide catabolism and cell redox homeostasis.
- The three `GO:0019430` removal-of-superoxide-radicals rows are over-propagated from mouse vascular
  phenotypes and do not match the known PRDX2 hydroperoxide-reducing chemistry.
- The `GO:0002357` defense-response-to-tumor-cell row from PMID:30429596 is not retained: the cached
  full text is a murine endothelial-cell-to-HSC conversion protocol and does not support a PRDX2
  function in tumor-cell defense.
- PRDX2 perturbation effects on apoptosis and coagulation are treated as downstream phenotypes rather
  than as core GO processes for the peroxidase itself.
