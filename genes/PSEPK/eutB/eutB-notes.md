# eutB curation notes

- A forced QuickGO refresh restored eight source rows. All eight are reviewed; incorrect `enables` relations for enzyme activity and cobalamin binding are paired with `NEW contributes_to` assertions under the qualifier-aware validator.
- The amino-acid-process mapping is removed. Both microcompartment localizations are `UNDECIDED` because the cytosol IEA and compact locus raise doubt but do not replace a reproducible localization or shell inventory.
- P0AEJ6 is the verified reviewed, protein-level E. coli EutB exemplar. `PTHR39329:SF1` is the exact EutB subfamily.
- No completed eutB OpenScientist artifact was present. Research was not restarted.

## Revision 2026-11-04 (ethanolamine module completion)
- Applied the shared convention for E. coli and KT2440 eutB/eutC:
  - GO:0008851 `enables` IEA: REMOVE -> ACCEPT. EutB carries the active-site TIM barrel and substrate-binding
    residues in the E. coli ortholog [PMID:20519496 "The active site is in the (beta/alpha)(8) barrel of the alpha-subunit"],
    so `enables` is right for the large subunit. The NEW contributes_to row was deleted; core function now
    uses molecular_function GO:0008851.
  - GO:0031419 cobalamin binding: REMOVE -> ACCEPT. E. coli P0AEJ6 has experimental cobalamin-contact residues
    (FT BINDING 194, 246, 295, 401; ECO:0000269 PMID:20519496/21142024/29797764). NEW contributes_to row deleted.
  - GO:0031469 / GO:0031471: UNDECIDED -> REMOVE, citing the KT2440 shell inventory
    (`genes/PSEPK/eutC/eutC-bioinformatics/RESULTS.md`: zero PF00936/PF03319/IPR000249/IPR004992 proteins in
    UP000000556; E. coli control positive). Cytosol (TreeGrafter IEA) ACCEPT now cites the same analysis.
- Status set to COMPLETE.
