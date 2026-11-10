# dksA (PA4723, G3XD14) notes

## Identity

- UniProt G3XD14 (unreviewed, PE 3), "RNA polymerase-binding transcription factor DksA" (HAMAP
  MF_00926). N-terminal coiled-coil (DksA_N, PF21157) and C4 zinc finger (PF01258; Zn ligands Cys111,
  114, 132, 135 by HAMAP). PANTHER PTHR33823:SF2. NCBIfam TIGR02420.
- PAO1 also encodes the Zn-independent paralog DksA2 (PA5536, Q9HT38), Zur-repressed, which can substitute
  for DksA [PMID:21255113 "DksA2 can functionally substitute for the canonical DksA in vivo in Escherichia
  coli and P. aeruginosa"].

## Function

- DksA binds RNA polymerase (secondary channel in E. coli) and, with ppGpp, alters initiation at target
  promoters [PMID:21255113 "DksA is a global transcriptional regulator that directly interacts with RNA
  polymerase (RNAP) and, in conjunction with an alarmone ppGpp, alters transcription initiation at target
  promoters"].
- In P. aeruginosa, DksA represses rRNA transcription in exponential growth and stringent conditions; the
  dksA mutant overproduces rRNA without changing ppGpp; ChIP places DksA at rRNA promoters together with
  RNAP; DksA co-purifies with RNAP subunits; with ppGpp it increases RNAP binding to rRNA promoters in band
  shifts [PMID:15853892 abstract "DksA, a protein with pleiotropic effects, is a negative regulator of rRNA
  transcription both during exponential growth and stringent conditions"; "Moreover DksA can be copurified
  with RNAP subunits in vivo"]. Abstract only in the cache.
- Multicopy dksA suppresses elastase and rhamnolipid production by inhibiting rhlI transcription; the
  authors judge the effects on lasB and rhlAB indirect [PMID:11160083 "It therefore appears that dksA does
  not inhibit the expression of lasB and rhlAB directly but affects both elastase and rhamnolipid
  production indirectly by the inhibition of rhlI transcription"].
- An STM screen found dksA required for anaerobic nitrate and nitrite respiration [PMID:18203836
  abstract]; mechanism not shown.

## Annotation decisions

- GO:0045892 negative regulation of DNA-templated transcription (IMP, PseudoCAP, PMID:15853892): ACCEPT.
- GO:0006355 regulation of DNA-templated transcription (IBA): ACCEPT (DksA both represses and activates
  promoters across the clade; the unsigned term fits).
- GO:0070063 RNA polymerase binding (IDA, PMID:21255113): ACCEPT the term (DksA co-purifies with RNAP,
  PMID:15853892). The cited paper's biochemistry is on DksA2 with E. coli RNAP, so the reference is likely
  the wrong one for PA4723; SUSPECTED PseudoCAP defect.
- GO:0045861 negative regulation of proteolysis (IDA, PMID:11160083): REMOVE. Overexpression lowered
  elastase production indirectly via rhlI; that is not regulation of proteolysis.
- GO:0051055 negative regulation of lipid biosynthetic process (IDA, PMID:11160083): MARK_AS_OVER_ANNOTATED
  (overexpression, indirect via quorum sensing).
- GO:1901857 positive regulation of cellular respiration (IMP, PMID:18203836): MARK_AS_OVER_ANNOTATED
  (requirement in a mutant screen of a pleiotropic regulator).
- GO:0010468 regulation of gene expression (IEA): MODIFY to GO:0006355.
- GO:0008270 zinc ion binding (IEA): KEEP_AS_NON_CORE (structural C4 zinc finger).
- GO:0005737 cytoplasm (IEA): ACCEPT.

## PseudoCAP IBA-seed assessment

PTN002139169 has 17 leaves (16 taxa, local PAINT leaf GAF 2026-10-28): DksA of gamma/beta/delta-
proteobacteria and Aquifex, the P. aeruginosa DksA2 paralog (Q9HT38), Bacteroides BT_0807 and Streptomyces
SCO2075.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN002139169 | GO:0006355 regulation of DNA-templated transcription | 1 (sole) | 17 (16 taxa) | GO:0045892 negative regulation of DNA-templated transcription, IMP, PMID:15853892 (PseudoCAP) | SOUND | The paper shows rRNA overexpression in the mutant plus direct association of DksA with RNAP on rRNA promoters (ChIP, co-purification, band shift with ppGpp), so DksA itself regulates transcription; not an indirect phenotype. Generalising to the unsigned parent is right for the node, because DksA family proteins both repress (rRNA) and activate (amino-acid biosynthesis) promoters, and the term is broad enough for the divergent Streptomyces and Bacteroides members. |
