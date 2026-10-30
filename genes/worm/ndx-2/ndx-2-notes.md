# ndx-2 (W02G9.1, O61902) review notes

## Identity

- 223-aa Nudix hydrolase; PANTHER PTHR11839:SF1 "ADP-SUGAR PYROPHOSPHATASE", the
  NUDT5 / yeast YSA1 family. The GOA IBA rows come from PAINT nodes PTN000217303,
  PTN000217263 and PTN000217304, seeded by human NUDT5 (Q9UKK9; UniProt: "ADP-sugar
  pyrophosphatase ... 8-oxo-dGDP phosphatase") and yeast YSA1 (SGD:S000000315 = Q01976,
  "ADP-ribose pyrophosphatase"), plus Arabidopsis loci for the broad process node.
- Sanada & Zhang-Akiyama 2014 describe it the same way:
  [PMID:24435662 "C. elegans NDX-2 is predicted to be an ADP sugar diphosphatase orthologous to human NUDT5."]

## Sanada & Zhang-Akiyama 2014 (PMID:24435662), PMC full text (main NDX-2 paper)

- 8-oxo-dGDP to 8-oxo-dGMP; triphosphates not hydrolysed:
  [PMID:24435662 "As shown in Figure 1B , NDX-2 degraded 8-oxo-dGDP to its monophosphate form, and hydrolysis of 8-oxo-dGTP was hardly detected."]
- Not selective for the oxidised deoxy form:
  [PMID:24435662 "NDX-2 can hydrolyze normal dGDP as efficiently as 8-oxo-dGDP ( Table I )."]
  [PMID:24435662 "The 8-oxo-dGDPase activity of NDX-2 was significantly lower than that of NDX-1."]
- Table I (transcribed; NDX-2 at 5 uM, about 7 times the NDX-1 concentration, 20 uM substrate,
  30 min): dGDP 66.4%, 8-oxo-dGDP 54.4%, 8-oxo-GDP 25.2%, GDP 5.40%; dGTP, 8-oxo-dGTP,
  GTP and 8-oxo-GTP <5%. So it is a diphosphatase; on ribonucleotides it prefers 8-oxo-GDP
  about 5-fold over GDP, while on deoxyribonucleotides it does not discriminate.
- E. coli mutT: partial suppression of the mutator phenotype (it also rescues MV sensitivity):
  [PMID:24435662 "This fact might explain why the suppression of mutagenesis by the expression of NDX-2 was not as efficient as that by NDX-1 or NDX-4 ( 11 , 12 )."]
- In worms, ndx-2 RNAi makes developing worms sensitive to MV and menadione bisulphite; the
  effect is rescued by chk-2 or clk-2 depletion (checkpoint signalling):
  [PMID:24435662 "As shown in Figure 3A , knockdown of ndx-2 caused sensitivity to both MV and menadione bisulphite."]
- Redundancy:
  [PMID:24435662 "However, NDX-1 and NDX-2 provide mutual backup in sanitisation of the nucleotide pool."]
- ADP-ribose and other ADP-sugars, the NUDT5-family substrates, were not tested in any worm
  study.

## Arczewska et al. 2010/2011 (PMID:21111690), from the curator-supplied PDF

NDX-2 was one of six worm Nudix proteins screened for 8-oxo-dGTP hydrolysis; it was negative.
Verbatim (paywalled, not in PMC):
"Of the remaining constructs, only extract from the clone overexpressing NDX-4 hydrolyzed 8-oxodGTP"

## Sanada et al. 2011 (PMID:21873335), from the curator-supplied PDF

"Expression of NDX-4 also significantly reduced the spontaneous mutation frequency in E. coli CC101 mutT, while expression of NDX-2 had only a partial effect on the mutation frequency (Fig. 2A)."

## Miyaji et al. 2018 (PMID:30425296)

Uses ndx-2 RNAi as a tool to raise oxidised nucleotides in exo-3 mutants; no new NDX-2 biochemistry.

## Curation decisions

- GO:0047631 ADP-ribose diphosphatase (IBA): ACCEPT. A sound PAINT inference in the NUDT5/YSA1
  clade. NDX-2 conserves the family, and no evidence suggests loss of the activity. It has
  not been assayed in the worm, which is raised as a suggested experiment.
- NEW GO:0044715 8-oxo-dGDP phosphatase activity (IDA, PMID:24435662): directly shown. The
  reason notes it hydrolyses dGDP equally well. The general parent GO:0017110 would describe
  the lack of selectivity better, but proposing parent and child together is redundant, and
  the 8-oxo term records what was specifically demonstrated.
- NEW GO:0044716 8-oxo-GDP phosphatase activity (IDA, PMID:24435662): 25.2% versus GDP 5.4%.
- GO:0016787 hydrolase activity (IEA): MODIFY to GO:0044715.
- GO:0005634 nucleus (IBA): KEEP_AS_NON_CORE as a plausible PAINT inference from human NUDT5;
  there are no direct worm localization data.
- GO:0006753 nucleoside phosphate metabolic process and GO:0019693 ribose phosphate metabolic
  process (IBA): KEEP_AS_NON_CORE. Both are correct but very broad consequences of the
  diphosphatase activities.
- No process term is proposed from the stress-sensitivity data. NDX-2 is not a dedicated
  sanitiser: it hydrolyses dGDP and 8-oxo-dGDP equally and only partly rescues E. coli mutT.
