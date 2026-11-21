# eutC curation notes

- Q88QF2 / PP_0542 is the reviewed KT2440 EutC small subunit; P19636 and P19265 are verified protein-level EutC exemplars.
- All seven QuickGO rows were reviewed. The amino-acid-process mapping is removed; the two microcompartment localizations are `UNDECIDED` pending reproducible KT2440 evidence. Incorrect `enables` relations for EutBC activity and cobalamin binding are paired with `NEW contributes_to` assertions.
- GOA cites `PANTHER:PTN002446609` for GO:0009350. The canonical PAINT cache for PTHR39330 instead resolves GO:0009350 to `PTN002217404`, seeded by P19636 and P19265. The GOA PTN is preserved as source provenance but is not presented as a canonical ancestral node.
- The completed OpenScientist report was integrated for subunit structure. Its unaccompanied Pfam absence claim is not used as curation evidence.

## Revision 2026-11-04 (ethanolamine module completion)
- Applied the shared convention for E. coli and KT2440 eutB/eutC:
  - GO:0008851 `enables` IEA on EutC: ACCEPT the term and record `source_defects` WRONG_QUALIFIER
    (enables -> contributes_to), same as the E. coli EutC EXP/IEA rows (genes/ECOLI/eutC) and the
    genes/rat/Kcnj16, genes/CANAL/VMA8 precedent. The earlier REMOVE + NEW contributes_to pair was dropped.
  - GO:0031419 cobalamin binding: ACCEPT. The E. coli ortholog P19636 has experimental cobalamin-contact
    residues (FT BINDING 207, 228, 258; ECO:0000269 PMID:20519496/21142024), so EutC binds the cofactor
    directly. The NEW contributes_to row was dropped.
  - GO:0031469 / GO:0031471: REMOVE (were UNDECIDED). The proteome-wide shell inventory
    (`eutC-bioinformatics/RESULTS.md`, checked against `bmc_shell_inventory.tsv`: KT2440 has 0 hits for
    PF00936, PF03319, IPR000249 and IPR004992; the E. coli control gives 4 BMC proteins (EutL, EutS, EutM,
    EutK) and 1 vertex protein (EutN)) shows KT2440 encodes no shell protein, so the HAMAP-derived
    microcompartment location is over-propagated.
- Status set to COMPLETE.

## 2026-11-06 native-location and source-scope follow-up

The earlier “must act as a free cytoplasmic enzyme” interpretation exceeds the shell inventory. Zero detected conventional shell signatures (with E. coli positive control) support the bounded rejection of conventional BMC annotations, but do not directly locate active KT2440 EutBC. The inventory and raw output remain unchanged historical sources. PMID:19762342 concerns E. coli, including a truncated construct with altered solubility; PMID:20519496 assigns the catalytic barrel to EutB and cofactor-contact support to EutC in an E. coli structure. Neither establishes native KT2440 localization or kinetics. Conserved activities remain accepted with explicit homolog inference.

EutC retains its contribution-qualified core and accepted reaction. The combined UniProt GO_REF:0000120 qualifier caution is PROBABLE, not CONFIRMED, with exact mapping components recorded. The correction rests on the inferred small-subunit role, not a rule that enables requires autonomous isolated-subunit activity.

All historical annotation payloads and source/provider bytes are preserved; no NEW rows were added.
