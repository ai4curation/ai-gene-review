# bgs4 (O74475, SPCC1840.02c; cwg1, orb11, pbr1) notes

## Summary
- Essential GT48/FKS 1,3-beta-glucan synthase; the only Bgs subunit shown to be part of the GS enzyme [PMID:15615781 "Bgs4p is the only subunit found to be a part of the GS enzyme and essential for maintaining cell integrity during cytokinesis and polarized growth"].
- Makes the major branched beta-1,3-glucan of the wall and most GS activity [PMID:34959732 "It synthesizes the branched β(1,3)-D-glucan and is responsible for most GS activity"; PMID:24165938 "Bgs4 is responsible for the cell wall B-BG synthesis and the major β(1,3)GS activity."].
- Septum: arrives after septum initiation; required for the secondary septum and primary septum completion [PMID:24165938 "Bgs4 absence causes the total absence of SS."].
- Ring coupling: [PMID:24165938 "Bgs4-derived β(1,3)glucan is required for correct and stable actomyosin ring positioning in the cell middle"].
- Trafficking: poles -> late Golgi -> PM next to the ring, needs Rga7 [PMID:25977474 "Cells without Rga7p moved Bgs4p normally from the poles to the Golgi complex near to the cell center"].
- Regulation: Rho1 regulatory subunit [PMID:35049972 "the essential GTPase Rho1 is the β-GS regulatory subunit responsible for the activation of GS catalytic subunits Bgs1 to Bgs4"]; Rgf1 GEF [PMID:23907979 "Rgf1p is a Rho1p GEF that activates the β-GS complex containing the catalytic subunit Bgs4p"].
- Not a Ghs2 partner [PMID:42786154 "whereas GFP-Ghs2 and RFP-Bgs4 did not"; "In contrast, GFP-Ghs2 localization was unaffected in bgs4 (cwg1-1) and bgs1 (cps1-191) mutants"]. Associates with Smi1 (stated in PMID:42786154).
- Drug target: pbr1 resistance alleles are bgs4 point mutations [PMID:34959732 "These two mutants are exclusively due to point mutations in the bgs4+ sequence."].

## Curation decisions
- GO:0140752 (TAS) accepted as core MF; all GO:0003843 rows MODIFY -> GO:0140752 (coordinator guidance; PomBase GO-CAM gomodel:6918f23700003787 uses GO:0140752 for Bgs4 in secondary cell septum biogenesis). Caveat: branching rests on mutant wall composition, not on a reconstituted enzyme; for Bgs3 branching is attributed to Ghs2.
- General process rows (GO:0006075, GO:0051278) MODIFY -> GO:0071970; membrane -> plasma membrane; cell septum -> division septum; contractile ring -> cleavage furrow; cell cortex of growing tip -> plasma membrane of cell tip (Bgs4 is integral PM, not cortical).
- Golgi (transit), spore wall, mating projection tip, new growing tip, primary septum kept as non-core; cytoplasm HDA marked over-annotated.
