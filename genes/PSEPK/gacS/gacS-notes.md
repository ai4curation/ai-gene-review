# gacS Gene Review Notes

## Identity and architecture

- gacS (PP_1650; UniProt Q88MC3) encodes a membrane-bound hybrid sensor histidine kinase with predicted HAMP, histidine kinase, receiver, and C-terminal HPt domains, consistent with a multistep phosphorelay architecture [UniProt:Q88MC3 "DOMAIN          292..513 /note=\"Histidine kinase\""] [UniProt:Q88MC3 "DOMAIN          669..788 /note=\"Response regulatory\""] [UniProt:Q88MC3 "DOMAIN          824..917 /note=\"HPt\""].
- UniProt places GacS in the inner membrane as a multi-pass membrane protein and annotates histidine kinase catalytic activity [UniProt:Q88MC3 "-!- SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000256|ARBA:ARBA00004429}; Multi-pass membrane protein {ECO:0000256|ARBA:ARBA00004429}."] [UniProt:Q88MC3 "-!- CATALYTIC ACTIVITY: Reaction=ATP + protein L-histidine = ADP + protein N-phospho-L-histidine.; EC=2.7.13.3; Evidence={ECO:0000256|ARBA:ARBA00000085};"].

## Organism-specific functional evidence

- In KT2440 attachment screens, gacS mutants showed reduced biofilm formation and impaired attachment to biotic surfaces [PMID:22458445 "Phenotypic characterization of the mutants showed that 11 of the inactivated proteins were required for attachment to biotic surfaces too. ... including the global regulator RpoN and GacS"].
- In KT2440, expression of the K1 type VI secretion system gene cluster is positively regulated by the GacS-GacA two-component system and repressed by RetS [PMID:36748579 "Importantly, expression of the K1-T6SS gene cluster is positively regulated by the GacS-GacA two-component regulatory system (TCS) and repressed by the RetS sensor kinase"].

## Interpretation for GO review

- The core molecular role is phosphorelay sensor kinase activity at the membrane.
- Process terms should center on phosphorelay signal transduction; the documented adhesion and T6SS phenotypes are downstream outputs of that global signaling role rather than separate direct molecular activities.
- Independent adaptive evolution studies repeatedly recovered loss-of-function gacS/gacA mutations to improve engineered growth or product formation, reinforcing that GacS is a pleiotropic global regulator whose removal rewires many downstream programs [PMID:31931111 "The genes gntZ and gacS were also disrupted in several evolved clones, and deletion of these genes further improved strain growth and muconate production"] [PMID:39701409 "Whole-genome re-sequencing identified multiple converged mutations, including loss-of-function mutations to global regulators gacS, gacA, and turA"].
