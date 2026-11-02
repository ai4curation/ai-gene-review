# ndx-1 (T26E3.2, O45830) review notes

## Identity

- 365-aa Nudix hydrolase; PANTHER PTHR22769:SF56 "8-OXO-DGDP PHOSPHATASE NUDT18", the
  family of human NUDT18 (MTH3). The GOA IBA rows come from PAINT node PTN001103015, seeded
  by human NUDT18 (Q6ZVK8).
- Sanada et al. 2011 call it a "MutT homolog" because of its Nudix box and its rescue of
  E. coli mutT. By family and substrate it is a NUDT18-type 8-oxo-dGDP phosphatase, not a
  MutT/MTH1-type 8-oxo-dGTPase.

## Sanada et al. 2011 (PMID:21873335), full text read from a PDF supplied by the curator

Paywalled (OUP) and not in PMC; only the abstract is cached in `publications/`. The excerpts
below are verbatim from the PDF, with line-break hyphenation and ligatures normalised.

- Substrate specificity, by HPLC:
  "The results shown in Fig. 3C indicate that NDX-1 is able to hydrolyze 8-oxo-dGDP, but not 8-oxo-dGTP, to the monophosphate form."
  "NDX-1 did not hydrolyze 2-oh-dATP or 2-oh-dADP (Table I). In addition, it did not hydrolyze normal dGTP, dGDP, dATP or dADP (Table I)."
- Table I (transcribed; 10 uM substrate, 0.2 ug NDX-1, 4 mM MgCl2, 37 C, 30 min):
  8-oxo-dGDP 61.5% hydrolysed; dGTP, dGDP, 8-oxo-dGTP, dATP, dADP, 2-oh-dATP and 2-oh-dADP
  all below 2% (the PDF renders "<2" as "52" because of a font substitution).
- Metal dependence:
  "Among these metal ions, Mg2+ stimulated the activity of NDX-1 most effectively. Mn2+ gave 47% of the activity obtained in the presence of Mg2+, whereas there was no detectable hydrolysis activity with Zn2+ or Ca2+ (Fig. 3D)."
- E. coli complementation:
  "The frequency of mutation leading to reversion to LacZ+ in E. coli CC101 mutT was potently reduced by expressing NDX-1, compared with that of the mutT mutant carrying an empty vector (Fig. 2A)."
  The same figure shows "expression of NDX-2 had only a partial effect on the mutation frequency (Fig. 2A)."
- RNAi in worms:
  "The lifespan of ndx-1-RNAi worms did not differ from that of control worms (Fig. 4B)."
  "The ndx-1-RNAi worms showed higher sensitivity to MV and menadione bisulfite compared with the control worms (Figs. 4C and 4D)."
  The ndx-1 RNAi did not deplete ndx-2, ndx-3, ndx-4 or ndx-9 mRNA but slightly reduced ndx-8
  (their Supplementary Fig. S1), so a minor off-target contribution cannot be excluded.

## Sanada & Zhang-Akiyama 2014 (PMID:24435662), PMC full text

Table I (transcribed): NDX-1 (0.73 uM, 20 uM substrate, 30 min) hydrolysed 8-oxo-dGDP 62.7%,
8-oxo-GDP 63.2% and 8-oxo-GTP 10.5%; dGDP, dGTP, 8-oxo-dGTP, GDP and GTP <5%.
[PMID:24435662 "As shown in Figure 1C and Table I , NDX-1 and NDX-2 showed 8-oxo-GDPase activity."]

So NDX-1 hydrolyses both the deoxy and ribo forms of 8-oxo-GDP and strongly discriminates
against unoxidised GDP and dGDP: a selective oxidised-nucleotide phosphatase.

## Miyaji et al. 2018 (PMID:30425296), PMC full text

Uses ndx-1 RNAi as a way to raise oxidised nucleotides in an exo-3 background; it adds no
new NDX-1 biochemistry.
[PMID:30425296 "Accordingly, ndx-1 (RNAi) and ndx-2 (RNAi) lead to an increase in 8-oxo-dGDP in the nucleotide pool."]
That sentence is the authors' inference from the enzyme data, not a measurement of the pool.

## Curation decisions

- GO:0044715 8-oxo-dGDP phosphatase (IBA): ACCEPT, the core function, directly supported by
  PMID:21873335 and PMID:24435662. No separate NEW IDA row is added because the term is already
  carried.
- GO:0044716 8-oxo-GDP phosphatase (IBA): ACCEPT, directly supported by PMID:24435662 Table I.
- GO:0017110 nucleoside diphosphate phosphatase (IEA, InterPro): MODIFY to GO:0044715. NDX-1
  does not hydrolyse unoxidised NDPs, so the generic term misdescribes its specificity.
- GO:0016787 hydrolase activity (IEA): MODIFY to GO:0044715.
- GO:0016529 sarcoplasmic reticulum (HDA, PMID:21611156): T26E3.2 is in that screen's
  "Sarcoplasmic reticulum-like" category (GFP fusion driven by a muscle promoter). This is
  experimental, so it is not overruled, but it is an overexpression pattern in one cell type
  for an enzyme expected to act on the cytosolic nucleotide pool, so it is kept as non-core.
- No process term is proposed. Survival on MV or menadione and E. coli mutT rescue show the
  activity matters under oxidative stress; they do not identify a worm process that NDX-1
  performs beyond the reaction itself.
