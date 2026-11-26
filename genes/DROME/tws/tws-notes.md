# tws (twins / PR55 / B55, Drosophila melanogaster) curation notes

Accession: P36872 (FBgn0004889).

Deep research: `tws-deep-research-falcon.md` (falcon; completed after a wrapper timeout message). It agrees that Tws selects substrates for the Mts catalytic subunit (Tws itself has no catalytic activity), describes the Greatwall-Endos inhibition switch, adds Map205 pSer283 and Otefin Ser50/54 as PP2A-Tws substrates at mitotic exit, reports Tws in both cytoplasm and nucleus (nuclear foci after irradiation), and supports positive regulation of Wingless signaling between Dsh and Sgg. Consistent with the decisions below (Wg rows kept as non-core, nucleus kept as non-core).

## Literature journal

- PP2A-B55/Tws and Greatwall-Endos [PMID:33836042 "Mitotic entry involves inhibition of protein phosphatase 2A bound to its B55/Tws regulatory subunit (PP2A-B55/Tws), which dephosphorylates substrates of mitotic kinases"];
  cytoplasmic function [PMID:33836042 "We find that Tws shuttles through the nucleus via a conserved nuclear localization signal (NLS), but expression of Tws in the cytoplasm and not in the nucleus rescues the development of tws mutants"].
- Anaphase [PMID:8382567 "aar mutants display intact lagging chromatids that have undergone separation from their sisters, but that remain at the position formerly occupied by the metaphase plate"] [PMID:17306545 "knockdown of the Twins B subunit led to bridged and lagging chromosomes"].
- Activity/localization [PMID:7844174 "The 55 kDa regulatory subunit of Drosophila protein phosphatase 2A is located in the cytoplasm at all cell cycle stages"].
- Centrosomes/centrioles [PMID:18798690 "this form of PP2A (PP2Atws) seems to be the only one that is essential for centrosome maturation"] [PMID:21987638 "we show that PP2A (Protein Phosphatase 2A(Twins)) counteracts Plk4 autophosphorylation, thus stabilizing Plk4 and promoting centriole duplication"].
- Neuroblasts [PMID:19374896 "Both Twins and Mts are required to exclude aPKC from the basal neuroblast cortex"].

## Decisions

- Mitotic cell cycle IMP (lagging chromosomes) -> mitotic sister chromatid segregation; NAS row kept general (statement is about overall mitotic progression).
- Centrosome cycle (centrosome maturation screen) accepted; centriole duplication captured by regulation of centriole replication.
- Positive regulation of smoothened signaling (PMID:21730325) UNDECIDED: cached paper shows inhibitory PP2A role and does not show Tws data.
- Meiotic spindle assembly -> regulation of spindle assembly (PP2A opposes Aurora B), consistent with wdb/mts/Pp2A-29B.
