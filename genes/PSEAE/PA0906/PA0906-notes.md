# PA0906 (Q9I551) notes — AlpR

## Identity

- PA0906 is *alpR* (McFarland et al. 2015, PMID:26100878), a lambda CI/LexA-like repressor: Cro/C1-type
  HTH (PF01381, PS50943) plus a peptidase S24 (LexA-like) C-terminal domain (PF00717, IPR039418).
  PANTHER PTHR40661:SF2 is named after PrtR (PA0611), the pyocin repressor, a different paralog.
- Divergent from *alpABCDE* (PA0907-PA0911), a lysis cassette.

## Literature (full text cached, PMC4500232)

- [PMID:26100878 "We therefore reasoned PA0906, which we refer to here as AlpR, might be essential in P.
  aeruginosa because it represses the expression of genes whose products can be lethal."]
- [PMID:26100878 "Exposure of P. aeruginosa cells to the antibiotic ciprofloxacin, which leads to DNA
  damage, resulted in cleavage of wild-type AlpR but not the AlpR mutant AlpR(S153A)"] — DNA-damage
  induced autocleavage dependent on the Ser-Lys dyad serine.
- [PMID:26100878 "ChIP-Seq with an epitope-tagged version of AlpR revealed that AlpR associates with only
  two regions of the PAO1 chromosome: the alpR-alpA and alpA-alpB intergenic regions"]
- [PMID:26100878 "AlpR therefore exerts its effect on expression of these target genes directly."]
- [PMID:26100878 "Cleavage of AlpR triggers a cell lysis program through de-repression of the alpA gene,
  which encodes a positive regulator that activates expression of the alpBCDE lysis cassette."]
- So AlpR is a direct, DNA-damage-inactivated repressor of alpR and alpA; lysis is executed by the AlpBCDE
  proteins (holin-like AlpB etc.), not by AlpR.

## Annotation decisions

- GO:0045892 negative regulation of DNA-templated transcription (IDA PseudoCAP): ACCEPT, core.
- GO:0006355 regulation of DNA-templated transcription (IBA PTN002221379; IEA): MODIFY to GO:0045892.
- GO:0003677 DNA binding (IEA): MODIFY to GO:0000976 transcription cis-regulatory region binding (ChIP-seq
  to the two promoter-containing intergenic regions).
- GO:0006351 DNA-templated transcription (IEA): MARK_AS_OVER_ANNOTATED.
- GO:0006974 DNA damage response (IDA PseudoCAP): ACCEPT; AlpR is itself cleaved in response to DNA damage
  (ciprofloxacin, H2O2), which is its signal-transduction step.
- GO:0001896 autolysis (IMP PseudoCAP): MODIFY to GO:0043069 negative regulation of programmed cell death.
  AlpR does not execute lysis; it represses the lysis genes, and its removal/cleavage de-represses them.
  GO has no "regulation of autolysis" term; autolysis is_a programmed cell death. Not a PAINT seed.
- NEW GO:0001217 DNA-binding transcription repressor activity (IDA): core MF, not in GOA.
- NEW GO:0016540 protein autoprocessing (IMP): S153A abolishes DNA-damage-induced cleavage; by analogy to
  LexA/CI this is RecA-stimulated self-cleavage. Self-catalysis is not shown in vitro in this paper, so
  this is moderate.

## PseudoCAP IBA-seed assessment

QuickGO (2026-10-28) shows 10 IBA leaves for PTN002221379 (matches the worklist): PA0906, P. aeruginosa
PrtR (Q06553), S. oneidensis prophage cI/C repressors, S. typhimurium STM0898, H. influenzae HI_1476,
N. meningitidis NMB0910/NMB0556 and others — all CI/LexA-like HTH-S24 repressors.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN002221379 | GO:0006355 regulation of DNA-templated transcription | 1 (sole) | 10 (6 taxa) | GO:0045892, IDA, PMID:26100878 (PseudoCAP) | SOUND | ChIP-seq places AlpR on the alpR-alpA and alpA-alpB promoter regions, ectopic AlpR represses the promoter fusions, and blocking its cleavage blocks induction: direct evidence for transcriptional repression. The generic regulation term (the IBD did not propagate the negative sign) is appropriate for a clade of CI/LexA-like phage and pyocin repressors. |
