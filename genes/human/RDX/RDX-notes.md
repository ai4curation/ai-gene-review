# RDX PTHR23281 ERM split notes

## Seed and family context

- Human RDX (`UniProtKB:P35241`) is the PTHR23281 radixin member (`PANTHER:PTHR23281:SF14`).
- The family review already separates Merlin/NF2 from the canonical ERM proteins. RDX keeps the PTN001150648 actin-binding and endosomal IBA rows that were only problematic on the Merlin branch.
- All 91 seeded GOA rows were reviewed; none remain `PENDING`.

## Main evidence used

- `PMID:17825285` directly supports the human Caco-2 apical membrane and ABCC2/MRP2 localization rows: radixin concentrated at the apical membrane, associated with ABCC2/MRP2, and radixin knockdown caused loss of ABCC2/MRP2 from the cell surface.
- `PMID:21148287` supports the ERM/HOPS branch: Vps11 bound radixin and moesin as well as ezrin, and ERM depletion delayed EGFR traffic through EEA1-positive early endosomes and Rab7 recruitment during early-to-late endosome maturation.
- `PMID:17321526` supports a refinement of one bare `GO:0005515` row to `GO:0005178` integrin binding because radixin bound the beta2 integrin cytoplasmic tail.
- `PMID:22467863` supports non-core adherens-junction regulation through Rac1/Vav signaling.

## Calls and risk areas

- Accepted the plasma membrane, apical plasma membrane, microvillus, stereocilium-base, actin-binding, ABCC2/ATPase-binding, and ERM/HOPS endosomal rows as the strongest RDX biology.
- Removed most bare `GO:0005515` rows under the generic protein-binding policy, including EZR high-throughput interactions and SARS-CoV-2 viral-host interactions; the ITGB2 row was modified to integrin binding.
- Kept exosome, focal-adhesion, protrusion, adherens-junction, and cleavage-furrow localizations as non-core.
- Marked RNA binding, the E-cadherin HDA cadherin-binding row, barbed-end actin filament capping, and the MYADM endothelial-barrier/gene-expression rows as likely over-annotations.
- Treated the extracellular-region colostrum hit as too general relative to the kept extracellular-exosome rows.
- Left several rodent-transfer rows unresolved where the seeded human RDX caches did not contain the source evidence: T-tubule, midbody, Rap signaling, PDGF response, PKA binding, cell tip, thyroid-hormone response, postsynaptic receptor diffusion trapping, and G1/S regulation.
