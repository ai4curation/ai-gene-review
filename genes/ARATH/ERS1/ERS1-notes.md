# ERS1 (At2g40940, Q38846) curation notes

## 2026-10-05 session (ethylene_signaling module)

- Deep research (`just deep-research-falcon ARATH ERS1`) failed (provider exit code 1); review based on cached publications and UniProt.
- Identity confirmed: ERS1_ARATH, Q38846, At2g40940, subfamily 1 ethylene receptor, lacks receiver domain.
- Ethylene binding: [PMID:10938361 "yeast expressing the ERS1 protein contains ethylene-binding sites, indicating ERS1 is also an ethylene-binding protein"]; all five receptors bind ethylene [PMID:15703053].
- Dimerization/membrane: [PMID:10938361 "ERS1, like ETR1, forms a membrane-associated, disulfide-linked dimer."]
- ER localization: [PMID:19825542 "all ethylene receptors are targeted to the ER endomembrane network and do not localize to the plasmalemma"] -> nucleus ISM (AtSubP) removed.
- Genetics: dominant ers mutation gives insensitivity, ERS upstream of CTR1 [PMID:7569898]; null etr1-9 ers1-3 double strongly constitutive [PMID:17224067 "Our results are consistent with the ethylene receptors acting as redundant negative regulators of ethylene signaling, but with subfamily 1 receptors playing the predominant role."]
- Dual role controversy: [PMID:20374664 "Our results suggest that ERS1 has dual functions in the regulation of ethylene responses."] -> reference flagged DISPUTED.
- Kinase: [PMID:15358768 "histidine autophosphorylation is lost when ERS1 is assayed in the presence of both Mg2+ and Mn2+, suggesting that this activity may not occur in vivo"] -> His kinase KEEP_AS_NON_CORE, phosphorelay terms over-annotated.
- CTR1 association: Y2H [PMID:9560288]; weak in pull-down [PMID:25814663 "we did not observe co-purification of ERS1 or ERS2 with CTR1 in our pull-down analysis"].
- Protein binding (TRP1, PMID:19567478) removed as uninformative (interaction itself is real).
- Core MF: ethylene receptor activity (GO:0038199), ethylene binding (GO:0051740), ER membrane.
