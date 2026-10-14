# Diap2 notes

Reviewed `Diap2` for the APOPTOSIS conserved IAP comparator slice.

DIAP2 is the major fly IAP-family E3 in the Imd innate immune pathway rather
than the essential canonical apoptosis brake. Two null-allele papers anchored
that split: diap2 mutants develop normally but are acutely sensitive to
Gram-negative infection [PMID:16894030, "acutely sensitive to infection by
gram-negative bacteria"], and an independent analysis found the mutants "show
no defects in developmental or stress-induced apoptosis" while failing innate
immune Relish activation [PMID:17068333]. I therefore centered the review on
peptidoglycan recognition protein signaling and kept `defense response to
Gram-negative bacterium` as a broader non-core organismal output.

Mechanistically, DIAP2 is the RING E3 ligase that builds K63-linked ubiquitin
scaffolds on several Imd-pathway targets. IMD cleavage exposes an IAP-binding
motif and enables DIAP2-dependent IMD modification; in adult flies,
RING-mutant DIAP2 failed to rescue IMD ubiquitination in diap2 mutants
[PMID:20122400, "DIAP2 is the E3 for IMD K63-Ubiquitination in vivo"]. DIAP2
also binds DREDD and "promoted the conjugation of K63-linked Ub chains on
DREDD" [PMID:22549468]. The later Kenny/LUBEL work extends this pathway to
the regulatory IKK subunit Kenny, with K63-linked chains conjugated by DIAP2
[PMID:30026495, "K63-linked ubiquitin chains conjugated to Kenny by DIAP2"],
and the Drice intestinal-inflammation paper confirmed the same Dredd/Kenny
axis in the gut [PMID:34262145, "Unrestrained Diap2 drives Imd sigalling by
ubiquitinating Imd, Dredd and Kenny"].

The apoptotic branch is real but secondary. DIAP2 binds the effector caspase
DrICE through BIR3 and forms a mechanism-based complex after cleavage at
Asp100; its RING is also required to target DrICE for ubiquitylation
[PMID:18166655, "target drICE for ubiquitylation"]. The phenotype of losing
Diap2 is increased basal DrICE activity and stress sensitization, not
spontaneous death, so `negative regulation of apoptotic process` rows were
kept as non-core threshold effects rather than the same kind of core
annotation assigned to `Diap1`.

Several older or electronic rows were deliberately not forced into a clean
story. `GO:0005515` rows for Hid, Reaper, and Grim were removed as generic
binding even though the contacts exist [PMID:18166655, "Rpr and Grim
preferentially bound to the BIR2 domain of DIAP2"]. The `PMID:17205079` rows
for DIAP1 degradation and K48-linked ubiquitination remain unresolved because
the cache exposes only a preliminary abstract statement that DIAP2 mediates
DIAP1 degradation. The `PMID:23940367` rows also remain unresolved locally:
the visible abstract is a DIAP1/Grim study, even though FlyBase may have read a
full-text Diap2 assay.
