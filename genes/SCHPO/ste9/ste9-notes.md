# ste9 (srw1) — curation notes

UniProt O13286 (SRW1_SCHPO), PomBase SPAC144.13c, PANTHER PTHR19918:SF1 (Fizzy-related
subfamily). 556 aa, seven C-terminal WD repeats (246-541), disordered N-terminus carrying
the Cdk sites S62, T98, T177, S214 (PMID:10921878) and a mass-spec phosphosite S187
(PMID:18257517). Cited as the fission yeast Cdh1 exemplar in
`modules/metaphase_anaphase_transition_and_mitotic_exit.yaml`; the yeast CDH1 and human
FZR1 reviews are the finished comparators.

## Identity and history

- Isolated twice: as `srw1` (suppressor of rad1-1 wee1-50), a multicopy suppressor of
  hyperactivated Cdc2 [PMID:9398669 "We recently isolated a new gene named srw1(+), capable
  of encoding a WD repeat protein, as a multicopy suppressor of hyperactivated p34(cdc2)"],
  and as the classical sterile mutant `ste9` [PMID:9571240 "Ste9 is a WD-repeat protein
  that is highly homologous to Hct1/Cdh1 and Fizzy-related"]. Yamaguchi et al. note the
  identity: [PMID:9398669 "Recently we learned that srw1 + is identical to ste9 +"].

## What APC/C-Ste9 does

- G1-specific mitotic cyclin destruction. [PMID:10921876 "We show that APC ste9/srw1
  specifically promotes the degradation of mitotic cyclins cdc13 and cig1 but not the
  S-phase cyclin cig2."] and [PMID:10921876 "APC ste9/srw1 is not necessary for the
  proteolysis of cdc13 and cig1 that occurs at the metaphase–anaphase transition but it is
  absolutely required for their degradation in G 1 ."]
- Independent confirmation: [PMID:10921878 "srw1p is not required for the degradation of
  cdc13p during mitotic exit demonstrating that there are two systems operative at different
  stages of the cell cycle for cdc13p degradation"]. Mitotic-exit cyclin destruction is
  attributed to Slp1.
- Cig2 is NOT an APC/C-Ste9 substrate (contrary to the brief I was given, which said Ste9
  targets Cig2). Yamaguchi 1997: [PMID:9398669 "Regardless of the presence or absence of
  Srw1, Cig2 was degraded upon nitrogen starvation, suggesting that Srw1 might inhibit p34
  cdc2 /Cig2 by a different mechanism."] and Blanco 2000 as above. Ste9 restrains Cdc2-Cig2
  genetically (cig2 deletion suppresses ste9 sterility) but not by degrading Cig2. The
  description and core functions reflect Cdc13 + Cig1, not Cig2.
- Direct biochemistry (Kimata 2011, the PomBase IDA source): purified Lid1-TAP APC/C plus
  in vitro translated coactivators. [PMID:21389117 "Ste9 showed the most robust stimulation
  of ubiquitylation for both substrates."] (Cut2 and Cdc13). Cell-cycle regulation is
  reproduced in extracts: [PMID:21389117 "As expected, Slp1, but not Ste9, was able to
  support Cdc13 destruction in mitotic extracts (Figure 5C, top), consistent with the
  established notion that CDH1 orthologues are inhibited by Cdk1-dependent phosphorylation in
  mitosis."] and [PMID:21389117 "In contrast, in interphase egg extracts, Slp1 was unable to
  activate Cdc13 destruction whereas Ste9 stimulated Cdc13 destruction efficiently (Figure
  5C, bottom)."]. Ste9 also ubiquitylates Mes1 in vitro.
- IMP arm of Kimata 2011: Ste9 repressed in meiosis (Puhp1-HA-ste9) — [PMID:21389117 "In
  all the mutants (ste9, fzr2Δ, and fzr3Δ), Mes1 levels were significantly increased at the
  end of meiosis II (5.5–6 h) rather than in early meiosis, pointing to their roles in Mes1
  destruction in meiosis II."]. Ste9 is hyperphosphorylated (inactive) through most of
  meiosis and is not involved in the MI to MII transition.

## Regulation

- Cdc2-Cdc13 phosphorylation inhibits Ste9 two ways: [PMID:10921876 "In the rest of the
  cell cycle, phosphorylation of ste9/srw1 by cdc2–cyclin complexes both triggers
  proteolysis of ste9/srw1 and causes its dissociation from the APC/C."] and [PMID:10921876
  "APC/C–ste9 interaction occurs only in G 1 when ste9 is in its dephosphorylated form."]
- Four Cdk sites; unphosphorylatable mutant stabilised and hyperactive: [PMID:10921878
  "Mutant forms of srw1 that could not be phosphorylated on the four Cdk consensus sites in
  srw1p were more stable than wild-type srw1p: the half-life of the unphosphorylatable srw1p
  was >120 min, compared with 40 min for wild-type srw1p (Figure 7 B)."]; [PMID:10921878
  "Consistent with this view, cdc13p was degraded more quickly in unphosphorylatable srw1
  mutant cells (Figure 7 E), indicating that phosphorylation leads to the inhibition of
  srw1p activity."]; the 4A mutant causes diploidisation, suppressed by extra Cdc13.
- Phosphorylation depends mainly on Cdc2-Cdc13, not Cig1/Cig2 [PMID:10921878 "We have
  also shown that the phosphorylation of srw1p is mainly dependent on the cdc2p–cdc13p
  complex."]
- From the deep-research file (papers not in the cache, not used for any action):
  PP2A-B56/Par1 needed for Ste9 dephosphorylation and Cdc13 loss in pre-Start G1 (Stonyte
  2020, iScience 23:101063); Cds1 phosphorylates and inhibits Ste9 during HU arrest,
  protecting the MBF activator Rep2, an APC/C-Ste9 substrate (Chu 2009, MCB,
  doi:10.1128/MCB.00562-09). Both raised as suggested_questions rather than annotated.

## Physiology (the G1 terms)

- Nitrogen-starvation G1 arrest, sterility: [PMID:9398669 "Cells lacking srw1(+) are
  sterile and defective in cell cycle controls."]; [PMID:9571240 "The ste9 mutants were
  sterile because they were defective in cell cycle arrest in the G1-phase upon
  starvation."]; [PMID:9398669 "In the srw1 disruptant, Cdc13 fails to be degraded when
  cells are starved for nitrogen."]
- Pre-Start G1 block to mitosis: [PMID:9571240 "In the double mutants of ste9 cdc10(ts),
  cells arrested in G1-phase at the restrictive temperature, but the level of mitotic cyclin
  (Cdc13) did not decrease. In these cells, abortive mitosis occurred from the pre-Start
  G1-phase."]; synthetic lethality with wee1.
- Gain of function: [PMID:9571240 "Overexpression of Ste9 decreased the Cdc13 protein
  level and the H1-histone kinase activity. In these cells, mitosis was inhibited and an
  extra round of DNA replication occurred."]
- Size control framing (Blanco): [PMID:10921876 "This is important for small cells that
  had to lengthen the G 1 -phase until they reach the minimum cell size required to initiate
  DNA replication or to prevent entry into mitosis from G 1 ."]
- Redundancy with Rum1: the ste9 rum1 double deletion is viable with no mitotic defect
  [PMID:10921878 "the double deletion mutant of srw1 and rum1 is fully viable and shows no
  mitotic defects"].
- Localisation: nucleus by ORFeome YFP screen (PMID:16823372, abstract-only cache; the
  Ste9 datum is in the supplementary data, cited by UniProt). No cell-cycle-resolved imaging
  of endogenous Ste9 in the dedicated literature; suggested as an experiment.

## Annotation decisions

All 18 GOA rows reviewed; all ACCEPT. One NEW row added (GO:0005680 anaphase-promoting
complex, part_of, IDA from PMID:10921876). Rationale for the rows that needed thought:

- GO:0031568 mitotic G1 cell size control checkpoint signaling (IGI 9398669 with cig2;
  IMP 9571240). Definition: "A signal transduction process that contributes to a cell size
  control checkpoint during the G1/S transition". PomBase uses the same term for rum1, cig2,
  cdc2 and wee1, i.e. it is their term for the pre-Start G1 delay. Ste9 executes the
  cyclin-destruction arm of that delay, which is its core physiological role, so ACCEPT
  rather than KEEP_AS_NON_CORE (the cdc2 review used non-core because for the master kinase
  it is one of many downstream outputs; for Ste9 it is the main output). Raised the
  "signaling" wording as a question.
- GO:2000134 negative regulation of G1/S transition (IGI 9571240 with cig2). Definition is
  a pathway that inhibits cell-cycle CDK activity at G1/S; Ste9 lowers Cdc2-Cdc13 activity
  by destroying Cdc13, and cig2 mutation suppresses the sterility. ACCEPT.
- GO:0097027 ubiquitin-protein transferase activator activity (IEA InterPro). Parent of
  GO:1990757; accepted as in the CDH1 and FZR1 reviews (the slp1 draft used MODIFY; I
  followed the completed exemplars).
- GO:0031145 (IMP 21389117) rests on the meiotic Mes1 stabilisation, a partial phenotype
  shared with fzr2 and fzr3; still a genuine dependence of APC/C substrate destruction on
  Ste9, so ACCEPT.
- Kimata 2011's title is about Fzr1/Mfr1 and Slp1, but the cached full text contains the
  Ste9 assays, so the PomBase IDA/IMP rows are verified, not inferred.
- NEW GO:0005680 anaphase-promoting complex (part_of). Comparator check: yeast CDH1 (IPI
  with Cdc23/Cdc16 and IBA), human FZR1, and fission yeast slp1 (IBA) all carry part_of
  APC/C, and slp1's IBA comes from PTN000460086, the same PAINT node that supplies ste9's
  GO:0031145/GO:1905786/GO:1990757 IBAs. So this is a propagation gap, not a MOD-wide
  convention against annotating coactivators to the complex. Direct evidence in this
  species: Blanco 2000 co-association of dephosphorylated Ste9 with the APC/C in G1
  (cut9-HA strain) and Kimata 2011 reconstitution of the holoenzyme from purified APC/C
  plus in vitro translated Ste9. It is a CC assertion, not a BP participation claim, so the
  "do not add what curators declined" bar for process terms does not apply in the same way;
  still raised as a question for PomBase.
- proposed_new_terms empty.

## Deep research

`ste9-deep-research-falcon.md` (Edison/falcon) was present and used for context. It is
accurate on the core biology and correctly warns that the 2024 Slp1/Pmk1 papers concern Slp1
not Ste9. Its statement that localisation is "unresolved" ignores the ORFeome HDA, which is
a legitimate (high-throughput) observation. Kominami 1998 (PMID:9736616), the Rep2 paper and
the Par1 paper are not in the publications cache; I did not fetch them and did not base any
action on them.
