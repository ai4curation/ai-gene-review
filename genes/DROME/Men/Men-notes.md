# Men notes

- 2026-10-09: Initial review of Men (Q9VG31; FBgn0002719), cytosolic NADP-malic enzyme.
- Cytosolic: "NADP-malic enzyme (NADP-ME) (E.C. 1.1.1.40) is situated in the cytosol of Drosophila
  melanogaster." and "The tissue activity of NADP-ME is very high in early third instar larvae,
  providing about 33% of the NADPH at this life stage." [PMID:120193]
- Sole source of cytosolic ME: "we could show that the ME activity recovered in cytosolic fractions
  originates exclusively from the Men gene"; "is a non-mitochondrial enzyme recovered in the
  cytosolic fraction" [PMID:12398416].
- Apoptosis threshold via NADPH and Dronc phosphorylation: "Indeed, abrogation of malate-induced NADPH
  production by downregulation of Men demolished the protective effects of malate" [PMID:20700104].
- Overexpression: "Men overexpression by S106-GeneSwitch-Gal4 driver increased pyruvate content and
  NADPH/NADP(+) ratio" [PMID:25511696].
- N-terminus MGNSSSICADRN... (no mitochondrial presequence). Mitochondrion IBA (ME2/ME3 donors)
  REMOVED; mitochondrial paralog is Men-b.
- NAD binding IEA -> NADP binding; generic MF IEA -> GO:0004473. Added NEW GO:0006740 NADPH
  regeneration (enzyme performs the NADPH-producing step).
- Sleep IMP (P-element screen, abstract only) kept as non-core.
- Falcon deep research (Men-deep-research-falcon.md, arrived after initial commit): 96.7% of adult
  NADP-ME activity in the soluble supernatant (only 1.5% mitochondrial), supporting removal of the
  mitochondrion IBA; Men-null larvae have NADPH/NADP+ ratio 1.3 vs 8.9 in wild type, supporting the
  NEW NADPH regeneration annotation; Men reduction suppresses CryAB-R120G reductive-stress
  cardiomyopathy; SREBP-driven Men expression affects head NADP+/NADPH and night sleep in Cyfip
  mutants (relevant to the sleep IMP, which stays non-core). No annotation changes.
