# LCIA (NAR1.2; Q75NZ3; Cre06.g309000) notes

## Deep research status

- 2026-10-03: `scripts/deep_research_wrapper.py CHLRE LCIA falcon --fallback perplexity-lite`
  was run once. Falcon timed out (600 s; falcon currently returns HTTP 402) and the
  perplexity-lite fallback failed ("Provider 'perplexity' not available"). Not retried.
  No `-deep-research-*.md` file exists; the review is built from the cached primary
  literature below.

## Identity

- UniProt Q75NZ3 (TrEMBL, unreviewed, PE 1), 336 aa, gene LciA, also NAR1.2;
  KEGG cre:CHLRE_06g309000v5. FNT transporter family (TC 1.A.16), Pfam PF01226,
  PANTHER PTHR30520:SF6. Six predicted TM helices (106-322). Cryo-EM structure
  PDB 9V2A (residues 39-336, five chains A-E, i.e. an FNT-type pentamer).
- Same protein as NAR1.2: [PMID:25336519 "Limiting CO2 Inducible A (LCIA; also named NAR1.2)"].
- Has an N-terminal chloroplast transit peptide: [PMID:16905358 "NAR1.1, NAR1.2, and
  NAR1.5 contain putative chloroplast transit peptides"]. Removing the predicted 73-aa
  transit peptide sends LCIA:GFP to the cytosol in tobacco
  [PMID:26538195 "When expressed transiently in tobacco, LCIA: GFP lacking the predicted
  native LCIA‐TP (73 aa)"].

## Expression

- Identified as a CCM1(CIA5)-dependent low-CO2-inducible gene
  [PMID:15235119 "Among low-CO2 inducible genes, two novel genes, LciA and LciB, were
  identified, which may be involved in inorganic carbon transport."]
- Unlike other NAR1 paralogs it is carbon-regulated, not nitrogen/Nit2-regulated
  [PMID:16905358 "One gene, Nar1.2, was strongly carbon-regulated independently of Nit2"].
- Expression depends on the Ca2+-binding protein CAS (retrograde signal from the
  pyrenoid) [PMID:27791081 "the perturbation of intracellular Ca2+ homeostasis by a
  Ca2+-chelator or calmodulin antagonist impaired the accumulation of HLA3 and LCIA"].

## Location: chloroplast envelope

- Immunofluorescence (cup-shaped chloroplast signal) and envelope membrane fractionation
  [PMID:26015566 "LCIA was highly enriched in the CE fraction, where CE protein CCP1 (30)
  was also enriched."; "we concluded that HLA3 and LCIA were localized to the PM and CE,
  respectively."]
- Venus fusion in Chlamydomonas and GFP in tobacco/Arabidopsis
  [PMID:26538195 "LCIA: Venus was confined to the chloroplast envelope"].
- Which envelope membrane: Nolke et al. place transgenic LCIA in the inner envelope of
  tobacco [PMID:29888874 "the bicarbonate transporter LCIA in the inner chloroplast
  membrane"]. Not resolved for the native protein in Chlamydomonas, so chloroplast
  envelope (GO:0009941) is the safe level; inner membrane (GO:0009706) is plausible
  because the outer envelope is generally porous to small anions.
- Plasma membrane location of bacterial FNT members (IBA donors) does not transfer: LCIA
  carries a transit peptide and is not at the plasma membrane in Chlamydomonas.

## Activity: bicarbonate (and nitrite) transport

- Xenopus oocytes, electrophysiology (Mariscal 2006, abstract only):
  [PMID:16905358 "The electrophysiological response to HCO3- and NO2- provides evidence
  that NAR1.2 is involved in both HCO3- and NO2- transport."]
- Xenopus oocytes, H14CO3- uptake with mature LCIA (no transit peptide)
  [PMID:26538195 "Oocytes transformed with mLCIA: GFP or HLA3: GFP accumulated 2.0‐ and
  2.7‐fold more 14C than water‐injected controls, respectively"].
- Complementation of E. coli lacking carbonic anhydrases and Arabidopsis beta-ca5
  (Forster 2023, abstract only) [PMID:36987927 "Expression of LCIA restored growth in both
  systems in ambient CO2 conditions, which strongly suggests that LCIA is facilitating
  HCO3- uptake in each system."]
- Cryo-EM structure (Guo 2026, abstract only): FNT-type channel with a bicarbonate
  selectivity filter (Lys220; Ala117/Val267); K136A/A114F increase activity; bacterial
  nitrite channel NirC could be engineered to conduct bicarbonate, and Chlamydomonas
  NAR1.1/NAR1.5 have some bicarbonate transport capacity [PMID:41507353].
- Mechanism: FNT family proteins are pentameric anion channels; the 2026 abstract calls
  LciA "a chloroplast envelope bicarbonate channel". GO has GO:0160133 bicarbonate
  channel activity (is_a GO:0015106). I used the parent GO:0015106 in core_functions
  because the channel mechanism for LCIA rests on an abstract-only structural paper and
  family inference; flagged as a question.
- Formate: no report that LCIA transports formate. Its bicarbonate selectivity is set by
  a specific filter, and the IBA formate terms come from bacterial FocA-type members
  (P0AC23 FocA, P77733 FocB). Formate IBA rows modified to bicarbonate.
- Nitrite: oocyte currents with NO2- (PMID:16905358); physiological relevance unclear
  because LCIA is not nitrogen-regulated. Not proposed as a NEW annotation.

## In vivo role in the CCM

- Off-target LCIA knockdown together with HLA3 RNAi strongly reduced Ci uptake at pH 9
  [PMID:19321421 "additional evidence supporting a role for LCIA in chloroplast envelope
  HCO(3)(-) transport"].
- lcia/lcib double mutant cannot survive very low CO2; LCIA associated with HCO3-
  uptake, LCIB with CO2 uptake [PMID:25336519 "LCIB appears to function in a CO2 uptake
  system, whereas LCIA appears to be associated with a HCO3(-) transport system."]
- Insertion mutants and overexpression: cooperative HLA3/LCIA HCO3- uptake; LCIA loss
  also lowers HLA3 mRNA (retrograde) [PMID:26015566 "simultaneous overexpression of HLA3
  with LCIA significantly increased Ci affinity/accumulation"].
- Heterologous expression in Arabidopsis gave no growth advantage (PMID:26538195);
  Nolke 2019 reported increased CO2 uptake and biomass in tobacco (PMID:29888874).

## Module check (modules/pyrenoid_ccm.yaml, annoton lcia_envelope_uptake)

- Module asserts GO:0015106 bicarbonate transmembrane transporter activity at GO:0009941
  chloroplast envelope. Both supported (oocyte uptake, E. coli/Arabidopsis
  complementation, structure; IF/fractionation/fluorescent fusions).
