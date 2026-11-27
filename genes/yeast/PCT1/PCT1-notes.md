# PCT1 (CCT1, YGR202C, P13259) notes

## Identity
- CTP:phosphocholine cytidylyltransferase, EC 2.7.7.15; amphitropic, membrane-associated activity [UniProt:P13259].

## Evidence
- Cloned by complementation of thermolabile CCT mutant [PMID:2826147 "The cloned DNA restored both the growth and cholinephosphate cytidylyltransferase activity of the mutant."]
- Rate-limiting CDP-choline step [PMID:19141610 "In S. cerevisiae, the rate-determining step in the synthesis of phosphatidylcholine via the CDP-choline pathway is catalyzed by Pct1."]
- Nuclear/nuclear membrane localization [PMID:12200438 "Immunofluorescence microscopy localized Pct1p to the nucleus and nuclear membrane."]; Kap60-mediated import, nuclear exclusion does not affect PC synthesis [PMID:19141610 "Exclusion of Pct1 from the nucleus by elimination of its nuclear localization signal or by decreasing Kap60 function did not affect the level of phosphatidylcholine synthesis."]
- Sec14 regulation of CCT and pathway flux in sac1 [PMID:10397762 "sac1 mutants also exhibit a specific acceleration of phosphatidylcholine biosynthesis via the CDP-choline pathway"].

## Curation decisions
- Core: GO:0004105 + GO:0006657 CDP-choline pathway; nuclear envelope/nucleus.
- GO:0042564 (importin complex) marked over-annotated: Pct1 is cargo, not a component.
- PC binding IBA (from rat CCTalpha) kept non-core; cytosol RCA removed; catalytic activity IEA -> MODIFY.
