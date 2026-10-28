# motB (PA4953, Q9HUL2) notes

## Identity

- UniProt Q9HUL2, unreviewed, 347 aa; gene motB, locus PA4953. One N-terminal
  TM helix (26-45, Phobius), OmpA-like peptidoglycan-binding domain (162-281,
  PROSITE PS51123; Pfam PF00691 OmpA, PF13677 MotB_plug), PANTHER PTHR30329
  (stator element of flagellar motor complex). Partner gene PA4954 (motA).
- Nomenclature trap: Doyle et al. 2004 called PA4954-PA4953 "motCD"
  [PMID:15375113 "PA1460-PA1461 (motAB) and PA4954-PA4953 (motCD)"], whereas
  Toutain et al. 2005 and the PAO1 annotation call PA4954-PA4953 MotAB and
  PA1460-PA1461 MotCD [PMID:15629949 "we propose to designate PA4954 and PA4953
  as MotA and MotB and PA1460 and PA1461 as MotC and MotD, respectively"].
  The later (O'Toole) naming is used below.

## Literature

- Two redundant stators power the single polar flagellum. Removing both MotB
  homologues abolishes motility [PMID:15375113 "Mutation of both genes
  encoding the MotA homologs or MotB homologs was sufficient to abolish
  motility."]; mixed pairs still work [PMID:15375113 "Mutants carrying double
  mutations in nonequivalent genes (i.e., motA motD or motB motC) retained
  motility, indicating that noncognate components can function together."].
- Swarming (PA14; Toutain et al. 2005): the single motAB deletion swarms like
  wild type, the motCD deletion fails at agar >= 0.5%, the double mutant never
  swarms [PMID:15629949 "The Δ motAB mutant is able to swarm as well as the WT
  in agar concentrations up to 0.7%."; "The fact that the motCD mutant, but not
  the motAB mutant, has a phenotype with respect to swarming suggests that these
  two stators may have different roles in swarming motility."]. MotAB in
  multicopy inhibits swarming [PMID:15629949 "These data suggest that
  introduction of the MotAB stator in multicopy can inhibit swarming."]. The
  authors still conclude both stators act in swarming [PMID:15629949 "we
  conclude that the MotAB and MotBC proteins are stators that play a role in
  flagellar motor function for both swimming and swarming motility."]. MotAB
  alone (the motCD mutant) supports swarming on 0.45% agar.
- Kuchma et al. 2015 (PA14; abstract only, PMC full text not retrievable):
  motAB mutation increases swarming; MotAB is needed for c-di-GMP repression
  of swarming [PMID:25349157 "Here we show that the repression of swarming
  motility requires a functional MotAB stator complex."; "Mutating the motAB
  genes restores swarming motility to a strain with artificially elevated
  levels of c-di-GMP as well as stimulates swarming in the wild-type strain"].
  Model: MotAB displaces MotCD from the motor at high c-di-GMP.

## Participation test

MotB is a stator subunit: it does part of the work of flagellar rotation
(ion conduction, peptidoglycan anchoring). So GO:0071973 flagellum-dependent
cell motility is participation, not a phenotype. Swarming is a context: MotB
sits in the motor during swarming, but its loss does not reduce swarming (and
in PA14 increases it). The swarming term is therefore true at most as a
context-specific statement for P. aeruginosa, and its IMP support is
genetic-interaction (only visible without MotCD). For the PTN001251133 clade
(E. coli/Salmonella MotB, Yersinia MotB and LafU, Xanthomonas MotB,
Bradyrhizobium PomB, Thermodesulfovibrio MotB), swarming is a lifestyle
phenotype that many members have never been shown to display; the propagable
claim is flagellum-dependent cell motility plus the stator complex (the
latter already at the node from E. coli MotB).

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN001251133 | GO:0071978 bacterial-type flagellum-dependent swarming motility | 1 (sole) | 9 (7 taxa) | GO:0071978, IMP, PMID:15629949 and PMID:25349157 (PseudoCAP) | OVER-SPECIFIC | MotB is a genuine stator subunit, so flagellar motility is its own process, but the swarming seed is weak (the single motAB mutant swarms like wild type, PMID:15629949, or better, PMID:25349157) and swarming is a lifestyle context, not a clade-wide role. The node should carry GO:0071973 bacterial-type flagellum-dependent cell motility. |

## Decisions summary

- ACCEPT: plasma membrane (IEA); flagellum-dependent cell motility (IMP,
  PMID:15375113); stator complex (IBA).
- MODIFY: membrane (IEA) to plasma membrane.
- KEEP_AS_NON_CORE: the three swarming rows (IBA, two IMPs), with PSEUDOCAP
  defects (evidence code / phenotype sign) and a GO_CENTRAL defect asking for
  GO:0071973 at PTN001251133.
