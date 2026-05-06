# PPP2CA Review Notes

## Gene Identity
- **Gene:** PPP2CA (Protein Phosphatase 2A Catalytic subunit alpha)
- **UniProt:** P67775
- **EC:** 3.1.3.16
- **Aliases:** PP2A-alpha, RP-C (Replication protein C)

## Core Function Summary
PPP2CA encodes the catalytic subunit alpha of PP2A, a major serine/threonine phosphatase. The PP2A holoenzyme is a heterotrimer: catalytic C subunit (PPP2CA or PPP2CB) + scaffolding A subunit (PPP2R1A or PPP2R1B) + variable regulatory B subunit (from B55, B56, PR72, or striatin families). Over 80 distinct holoenzymes exist, together accounting for ~50-70% of cellular Ser/Thr phosphatase activity [deep-research-falcon; PMID:33243860 "INTAC complex dephosphorylates the carboxy-terminal repeat domain of RNA polymerase II at serine-2, -5, and -7"].

## Key Complexes
1. **Canonical PP2A holoenzyme** (AC dimer + B subunit) - substrate specificity determined by B subunit
2. **INTAC complex** (Integrator + PP2A-AC) - dephosphorylates Pol II CTD at S2, S5, S7 to regulate transcription [PMID:33243860, PMID:34004147, PMID:37080207, PMID:38570683]
3. **STRIPAK complex** (PP2A + striatins + STRIP1 + MOB4 etc.) - regulates Hippo signaling [PMID:33633399, PMID:29063833]

## Key Regulation
- Leu309 methylation by LCMT-1, reversed by PME-1, regulates B subunit binding [PMID:8206937; UniProt PTM]
- Tyr307/Thr304 phosphorylation inhibits activity [UniProt PTM]
- Endogenous inhibitors: CIP2A, SET, PABIR1/FAM122A, ARPP19 [PMID:27588481, PMID:38123684]

## Localization
- Cytoplasm, nucleus, chromosome (centromere during prometaphase), spindle pole during mitosis [PMID:16541025; UniProt SUBCELLULAR LOCATION]
- Chromatin-associated via INTAC complex [PMID:33243860, PMID:34004147]
- Membrane raft localization reported for ADCY8 interaction [PMID:16258073]

## Substrate Landscape (2024 data)
- Brewer et al. 2024 (iScience) used dTAG degradation: 6,280 phosphopeptides increased >1.5-fold after PPP2CA loss, 2,651 >2-fold. Enriched in spliceosome, cell cycle, ubiquitin-mediated proteolysis pathways [deep-research-falcon].

## Key Substrates (from UniProt FUNCTION)
- SV40 large T antigen, p53/TP53 [PMID:1848668]
- AXIN1 [PMID:9920888]
- RAF1 at Ser-259 (activation) [PMID:10801873]
- PIM3 (promoting degradation) [PMID:12473674]
- p53 at Thr55 (DNA damage response) [PMID:17245430]
- MYC (promoting degradation via AMBRA1) [PMID:25438055]
- FOXO3 (stabilization via AMBRA1) [PMID:30513302]
- WEE1 (stabilization, G2/M checkpoint) [PMID:33108758]
- Pol II CTD S2, S5, S7 (as INTAC) [PMID:33243860, PMID:34004147]
- MST1/2 T-loop (as STRIPAK) [PMID:33633399]
- AKT1 at Ser-473 (By similarity)
- CRTC3 [PMID:30611118]

## Protein tyrosine phosphatase claim
- PMID:15525651 reports PP2A has tyrosine phosphatase activity stimulated by Galpha12. This is an unusual claim for PP2A. The paper shows "approximately 300% increase in phosphotyrosine phosphatase activity" in vitro. This is atypical and should be noted.

## Disease
- Houge-Janssens syndrome 3 (HJS3) - de novo mutations cause syndromic intellectual disability [PMID:30595372]

## Annotations Review Strategy
- Accept core phosphatase function annotations (GO:0004722, GO:0006470)
- Accept INTAC, STRIPAK complex memberships
- Accept well-supported localizations (cytoplasm, nucleus, chromatin, centromere)
- Mark "protein binding" annotations as uninformative - prefer more specific terms
- Evaluate pleiotropic process annotations (Wnt, Hippo, EMT, etc.) as non-core or context-dependent
- Some IEA annotations may be too broad or specific
