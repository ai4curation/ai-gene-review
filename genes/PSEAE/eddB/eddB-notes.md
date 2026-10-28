# eddB (PA3909, Q9HXA4) notes

No deep-research provider was available; this is a manual literature review
(PubMed search; cached publications). PMID:20370819 is abstract-only;
PMID:29967090 and PMID:21705528 have full text cached.

## Identity

- UniProt Q9HXA4 (TrEMBL, PE 4), 779 aa, "Extracelullar DNA degradation
  protein, EddB" (submitter name). SignalP signal peptide 1..23.
- Domains: lamin-tail (LTD, PF00932, 19..131), endonuclease/exonuclease/
  phosphatase (PF03372, IPR005135; DNase I-like fold SSF56219, CDD cd10283
  MnuA_DNase1-like), NCBIfam NF033681 ExeM_NucH_DNase, InterPro IPR047971
  ExeM-like, CDD cd04486 YhcR_OBF_like, PANTHER PTHR42834.
- Operon: eddA (PA3910, PhoD-type alkaline phosphatase/phosphodiesterase) -
  eddB [PMID:29967090 "The DNase EddB (extracellular DNA degradation protein B)
  is downstream of a predicted alkaline phosphatase"].

## Literature

- Mulcahy et al. 2010 (PMID:20370819, PseudoCAP seed paper): "PA3909 encodes an
  extracellular deoxyribonuclease (DNase), which is required for degradation of
  DNA and utilization of DNA as a source of carbon, nitrogen and phosphate."
  Induced by phosphate limitation and by DNA; activity in culture supernatants
  needs excess Mg2+/Ca2+ for stabilisation; secretion via the Xcp type II
  secretion system [PMID:20370819 "The primary Xcp type II secretion system but
  not the Hxc type II secretion system is required for DNase activity and the
  ability to use DNA as a source of nutrients."].
- Wilton et al. 2018 (PMID:29967090, full text): supernatants of the eddB::lux
  mutant were strongly impaired in degrading Sytox-labelled DNA and pEddB
  complementation restored it [PMID:29967090 "Bacterial supernatants from P.
  aeruginosa lacking either the Xcp type II secretion system or PA3909 ( eddB )
  were strongly impaired for the degradation of Sytox green-labeled
  extracellular salmon sperm DNA, relative to the control"]. EddB degrades
  neutrophil extracellular trap DNA and contributes to survival against NET
  killing; eDNA and NETs induce the operon. Residual activity in mutants suggests
  other secreted nucleases exist.
- Gödeke et al. 2011 (PMID:21705528): the Shewanella oneidensis relatives ExeS
  and ExeM (ExeS is one of the other two PTN001684760 leaves) are extracellular
  endonucleases needed for eDNA degradation and DNA use as a nutrient
  [PMID:21705528 "Mutants lacking exeS and/or exeM exhibit decreased eDNA
  degradation"].

## GO term reasoning

- MF GO:0004536 DNA nuclease activity: the supernatant DNase activity depends on
  eddB and is restored by eddB in trans; EddB carries the DNase I-like
  endo/exonuclease/phosphatase domain of the ExeM/NucH family. The assay is on
  supernatants, not purified protein, so the strict evidence is genetic, but the
  gene product carrying a nuclease domain is the obvious catalyst. Endo- versus
  exonucleolytic mode is not shown for EddB, so stay at DNA nuclease activity.
- BP GO:0006308 DNA catabolic process: EddB hydrolyses DNA (extracellular DNA) to
  provide nutrients. The gene product catalyses the breakdown, so it does the
  work of the process (participation test passes). Seed SOUND.
- CC: secreted through Xcp T2SS, activity in culture supernatant, SignalP
  signal peptide -> GO:0005576 extracellular region (NEW). Two independent lines
  agree (signal peptide + T2SS dependence + supernatant activity).
- catalytic activity IEA (InterPro IPR005135): too general -> MODIFY to
  GO:0004536.
- Node PTN001684760: 3 leaves (EddB, Shewanella ExeS Q8EFX1, Xanthomonas
  XCC0255). ExeS is independently characterised as an extracellular
  endonuclease, so the node term suits the clade.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN001684760 | GO:0006308 DNA catabolic process | 1 (sole seed) | 3 (3 taxa: P. aeruginosa EddB, S. oneidensis ExeS, X. campestris XCC0255) | GO:0006308 DNA catabolic process, IMP, PMID:20370819 (PseudoCAP) | SOUND | eddB mutant supernatants lose DNase activity and the ability to use DNA as a C/N/P source; complementation restores DNA degradation (PMID:29967090). EddB carries the ExeM/NucH DNase I-like nuclease domain, so it is the catalyst of the breakdown, not just required for it. The term suits a small clade of secreted ExeM/NucH-family nucleases; ExeS is independently shown to degrade eDNA (PMID:21705528). |

## Decisions summary

- DNA catabolic process IBA and IMP: ACCEPT.
- DNA nuclease activity IDA: ACCEPT.
- catalytic activity IEA: MODIFY to GO:0004536.
- NEW: GO:0005576 extracellular region (IDA, PMID:20370819).
