# cysB (PA1754, G3XCU6) notes

## Identity

- Locus PA1754 (UniProt G3XCU6 `GN Name=cysB; OrderedLocusNames=PA1754`). The task brief guessed PA0281;
  the worklist and UniProt agree on PA1754, which is used here.
- LysR-family regulator: LysR HTH (IPR000847), CysB-type substrate-binding domain (IPR037423 CysB_PBP2),
  PANTHER PTHR30126:SF6 "HTH-TYPE TRANSCRIPTIONAL REGULATOR CYSB-RELATED". Adjacent, divergent *cysH*
  (PAPS reductase).

## Literature

- [PMID:9218775 "led to the discovery of a protein of 36 kDa (p36) able to bind downstream from ihf2, to
  the 3' region of palgD."] — work in mucoid strain CHA; the protein is 63% identical to E. coli /
  S. typhimurium CysB.
- [PMID:9218775 "A CysB-deficient mutant of CHA, constructed by insertional inactivation of cysB, was a
  cysteine auxotroph and was unable to form a specific complex with palgD in vitro."] — this is the basis
  of the PseudoCAP IMP to L-cysteine biosynthetic process: a mutant phenotype (auxotrophy).
- [PMID:9218775 "Thus, P. aeruginosa CysB can act as an activator of algD expression."]
- [PMID:20370820 "The CysB protein directly binds to the pvdS promoter in vitro and acts as a positive
  regulator of PvdS expression in vivo."] — basis for the PseudoCAP IDA to positive regulation of
  DNA-templated transcription.
- [PMID:20370820 "Given the role of CysB as master regulator of sulfur metabolism, our findings establish a
  novel molecular link between the iron and sulfur regulons in P. aeruginosa."]
- Both cached papers are abstract-only.

## Regulator vs participant (CLAUDE.md "Do not add what curators deliberately declined to add")

- Which entity performs the steps of L-cysteine biosynthesis? Serine acetyltransferase (CysE) and
  O-acetylserine sulfhydrylase (CysK/CysM), with sulfide supplied by the sulfate-assimilation enzymes
  (CysDNC, CysH, CysIJ). CysB catalyses none of these; it activates their genes. The cysteine auxotrophy
  of the cysB mutant shows necessity, not participation.
- Comparator check (QuickGO, 2026-10-28): E. coli CysB (P0A9F3) has EcoCyc experimental annotations to
  DNA binding, transcription and regulation but no experimental GO:0019344; its only GO:0019344 is the IBA
  from PTN002824317, which is seeded by P. aeruginosa CysB alone.
- The node PTN002824317 passes GO:0019344 (IBA) to 10 leaves: CysB of P. aeruginosa, S. typhimurium
  (P06614), E. coli (P0A9F3), H. influenzae (P45105), Y. pestis (Q0WEU7), S. oneidensis (Q8EDU4),
  X. campestris (Q8P602), N. meningitidis (Q9K116), V. cholerae VC_1907 (Q9KQU1), and E. coli Cbl
  (Q47083), a CysB paralog that activates taurine/sulfonate-utilisation genes. Every leaf is a
  transcriptional regulator. The same node also feeds TreeGrafter IEAs (about 1,200 GO:0019344 rows in
  QuickGO withFrom PTN002824317).
- GO's "regulation of cysteine metabolic process" terms are obsolete; the live GO:1900059 positive
  regulation of sulfate assimilation is the nearest regulatory term, but the P. aeruginosa papers do not
  test sulfate-assimilation gene expression, so I do not propose it as NEW. CysB's own process is captured
  by GO:0045893 positive regulation of DNA-templated transcription (IDA, PMID:20370820).

## Annotation decisions

- GO:0019344 L-cysteine biosynthetic process (IMP PseudoCAP; IBA PTN002824317): MARK_AS_OVER_ANNOTATED.
  PSEUDOCAP and GO_CENTRAL defects recorded.
- GO:0045893 positive regulation of DNA-templated transcription (IDA PseudoCAP, PMID:20370820): ACCEPT.
- GO:0006355 regulation of DNA-templated transcription (IBA PTN001248394; IEA): ACCEPT.
- GO:0000976 transcription cis-regulatory region binding (IBA): ACCEPT (binds the algD and pvdS
  promoters).
- GO:0003677 DNA binding (IEA): MODIFY to GO:0000976.
- GO:0003700 DNA-binding transcription factor activity (IEA): ACCEPT, core MF.
- GO:0006351 DNA-templated transcription (IEA): MARK_AS_OVER_ANNOTATED.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN001248394 | GO:0006355 regulation of DNA-templated transcription | 7 | 202 (30 taxa) | GO:0045893, IDA, PMID:20370820 (PseudoCAP) | SOUND | Purified CysB binds the pvdS promoter and activates pvdS expression in vivo; direct evidence for transcriptional regulation. The generic regulation term suits a 202-leaf LysR clade; six further seeds (E. coli, B. subtilis, P. aeruginosa paralogs) also support it. |
| PTN002824317 | GO:0019344 L-cysteine biosynthetic process | 1 (sole) | 10 (9 taxa) | GO:0019344, IMP, PMID:9218775 (PseudoCAP) | INDIRECT-PHENOTYPE | The seed is the cysteine auxotrophy of a cysB insertion mutant. CysB is the transcriptional activator of the cys regulon and performs no step of cysteine synthesis; the enzymes (CysE, CysK/M) do. Every leaf of the node is a CysB/Cbl-type regulator, none with experimental support for the process (E. coli CysB has none in EcoCyc). The term is wrong for the whole clade as a participation claim. |
