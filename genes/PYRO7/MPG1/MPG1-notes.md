# MPG1 (P52751) notes — Magnaporthe oryzae class I hydrophobin

## Sources
- UniProt P52751; Falcon deep research (MPG1-deep-research-falcon.md); cached PMIDs 8312740, 12239409, 8755621, 12481998, 15773983 (abstract only) and 27142249 (full text).

## Key facts
- Secreted class I hydrophobin: [PMID:12239409 "we identified a 15-kD secreted protein with characteristics that establish it as a class I hydrophobin"]
- Builds the conidial rodlet layer: [PMID:12239409 "MPG1 directs formation of a rodlet layer on conidia composed of interwoven ~5-nm rodlets, which contributes to their surface hydrophobicity"]; [PMID:27142249 "The spores of M. oryzae are covered with a layer composed of the hydrophobin MPG1 and the protein is also present in appressoria"]
- Interface-driven amyloid assembly: [PMID:27142249 "We show that MPG1 self-assembly into functional amyloid rodlets is strictly limited to a hydrophobic:hydrophilic interface."]
- Disulphides needed for secretion not assembly: [PMID:15773983 "disulphide bridges in a hydrophobin are dispensable for aggregation, but essential for secretion"]
- Mutant phenotype (necessity evidence): [PMID:8312740 "Mpg1 mutants have a reduced ability to cause disease symptoms that appears to result from an impaired ability to undergo appressorium formation."]; easily wettable.
- Surface recognition: [PMID:8755621 "Mpg1p is not specifically required for appressorium formation, but is involved in the interaction with, and recognition of, the host surface."] Defect rescued in trans by WT cells and (per deep research) by cAMP.
- Regulation: PMK1, NPR1, NUT1 required for starvation expression; CPKA represses [PMID:12481998].
- Cut2 retention by MPG1 coatings in vitro only [PMID:27142249].

## Curation decisions
- All 5 GOA rows (structural constituent of cell wall IEA; extracellular region EXP x2 + IEA; fungal-type cell wall IEA) ACCEPTED.
- NEW: spore wall (GO:0031160) and asexual spore wall assembly (GO:0042243). Comparator check via QuickGO: A. fumigatus RodA P41746 has GO:0031160 EXP; A. nidulans RodA P28346 has GO:0031160 IDA/EXP and GO:0042243 IMP. MPG1 is the self-assembling subunit, so passes participation.
- Deliberately NOT proposed: appressorium formation, conidium formation, pathogenesis / host-interaction terms — supported only by mutant (necessity) phenotypes; mechanism (sensor vs adhesion) unresolved. No GOA row uses host-interaction terms.
