# G6pc2 (mouse, Q9Z186, MGI:1277193) review notes

## 2026-11-08 Session 1: de novo review

### Context

Reviewed as part of the BGEEDB_EXPRESSION project (projects/BGEEDB_EXPRESSION.md).
Mouse was chosen for the richest Bgee data. The project's controlled design for
this family is the sister paralogs G6pc1/G6pc3 against G6pc2 in the tissues
where gluconeogenesis can run (liver, kidney cortex, small intestine; from the
pathway-satisfiability engine).

Inputs: 17 GOA rows (5 MF, 5 CC, 7 BP), the UniProt record, the claude_code
deep-research file (treated as a lead list), and the generated Bgee report
(`G6pc2-bioinformatics/RESULTS.md`).

### Identity and protein features

- 355 aa, 9 predicted TM helices (UniProt TRANSMEM 25-45 ... 319-339, ECO:0000255),
  C-terminal ER-retention motif 352-355 ("Prevents secretion from ER", ECO:0000255),
  N-glycosylation Asn92 in a predicted luminal loop. Active sites His115 (proton donor)
  and His174 (nucleophile) retained; the exon-IV-skipping isoform 2 (Q9Z186-2) lacks
  His174 [PMID:10078553 "neither of which possessed His174, a residue thought to be the
  phosphoryl acceptor"].
- PANTHER PTHR12591:SF1 (GLUCOSE-6-PHOSPHATASE 2). No FamilyReview exists for
  PTHR12591 (only entries/metadata/paint.tsv), so no `member_exceptions` to manage.

### Catalytic activity (GO:0004346)

- 1999 cloning: activity not detected in transfected cells [PMID:10078553 "the IGRP
  failed to show glucose phosphotransferase or phosphatase activity with p-nitrophenol
  phosphate, inorganic pyrophosphate, or a range of sugar phosphates hydrolyzed by the
  liver enzyme"].
- 2004: recombinant IGRP has G6Pase activity [PMID:14722102 "The K(m) and V(max) values
  determined using glucose-6-phosphate as the substrate were 0.45 mm and 32 nmol/mg/min by
  malachite green assay"]; a selective inhibitor exists [PMID:14722102 "this inhibitor did
  not affect LG-6-Pase activity"]. Abstract does not state the species of the construct;
  UniProt mouse entry attributes the CATALYTIC ACTIVITY to this paper (ECO:0000269) and
  Reactome uses it for a human EXP row. Not resolvable from the abstract.
- KO islets lose activity [PMID:23274894 "Fig. 1A shows that glucose-6-phosphatase activity
  is reduced in islets isolated from G6pc2 KO mice"]; glucose cycling abolished
  [PMID:25552595 "glucose cycling was abolished in G6pc2 KO mouse islets, confirming that
  G6pc2 opposes the action of the glucose sensor glucokinase by hydrolyzing G6P"].
- Intrinsically low turnover: [PMID:34954144 "G6PC1 exhibited much higher G6Pase activity
  than G6PC2 in these in vitro assays"]; mouse G6PC2 microsomal activity detectable
  [PMID:34954144 "Higher G6Pase activity was detected following transient expression of His
  tagged mouse G6PC2 compared with His-tagged human G6PC2"]; Vmax ranking
  [PMID:38431189 "the observed Vmax for G6P hydrolysis by G6PC1 was considerably greater than
  that for G6PC2 and G6PC3"].
- Judgement (ENZYME_SPECIFICITY tiers): not promiscuous noise. G6P hydrolysis is the
  protein's own reaction, it owns the reaction in islets (G6pc1 not detected in islets
  [PMID:32213654 "G6pc2 expression is much higher than G6pc3 in both pancreas and islets
  with G6pc1 expression not detected"]), and loss of the activity has an in vivo phenotype.
  Low Vmax is the physiology (a modulator of glucokinase flux), not evidence against
  function. ACCEPT all five MF rows as core.

### Physiological role

- Glucokinase/G6PC2 futile cycle sets glucose sensitivity of GSIS [PMID:23274894 "G6pc2
  deletion resulted in a leftward shift in the dose-response curve for glucose-stimulated
  insulin secretion (GSIS)"; "These data suggest that G6pc2 represents a novel, negative
  regulator of basal GSIS that acts by hydrolyzing glucose-6-phosphate, thereby reducing
  glycolytic flux."].
- Submaximal glucose only; Vmax of GSIS unaffected [PMID:23274894 "This observation
  suggests that the absence of G6pc2 does not affect the Vmax of GSIS."].
- Fasting glucose lower, fasting insulin unchanged [PMID:23274894 "blood glucose levels were
  indeed reduced in both male and female G6pc2 KO mice relative to their WT littermates (16.4
  and 14.4%, respectively), whereas fasting insulin levels were unchanged"]; first KO
  [PMID:17265032 "a small but significant decrease in blood glucose was observed in both male
  (-14%) and female (-11%) G6pc2 (-/-) mice"].
- Beta-cell-specific deletion is sufficient [PMID:32213654 "In adult mice, beta cell-specific
  deletion of G6pc2 was sufficient to reduce FBG without changing FPI."].
- Increased glycolytic/CAC flux in KO beta cells [PMID:35176280 "deletion of G6pc2 led to ∼60%
  increases in glycolytic and citric acid cycle (CAC) fluxes at both 5 and 11 mM glucose
  concentrations"].
- Protects against hypoglycemia [PMID:32569842 "When challenged with either a ketogenic diet
  or 24 hr fasting, blood glucose fell to 70 mg/dl or less in G6pc2 KO but not WT mice"].
- Glucocorticoid induction / stress [PMID:27300767]; dexamethasone effects [PMID:27653037].
  These are regulation of G6pc2 expression, not functions of the protein; no rows added.
- Possible alpha-cell / glucagon role in humans [PMID:39121091 "opposes the action of
  glucokinase in pancreatic islets, thereby modulating the sensitivity of insulin and glucagon
  secretion to glucose"]: mouse expression is ~20-fold beta-biased, so not annotated.

### Gluconeogenesis (GO:0006094): REMOVE (IBA + IEA, consistent)

- IBA from PTN000971890 (taxon:6072). PAINT IBD seeds for GO:0006094: FB:FBgn0031463,
  MGI:1915651 (G6pc3), MGI:95607 (G6pc1), RGD:2644, RGD:727875, UniProtKB:P35575 (G6PC1).
  No G6PC2 among the seeds. `just paint-losses mouse G6pc2`: "No IRD or IKR loss on this
  gene's lineage." So the IBA is current; the argument is with the node reaching the G6PC2
  clade.
- Biology: G6pc2 is islet/beta-cell restricted, its substrate is glucokinase-derived G6P in
  a futile cycle, and its effect on fasting glucose is mediated by insulin secretion.
  [PMID:32213654 "G6PC2 is highly unlikely to directly affect metabolism in these tissues"];
  [PMID:23274894 "The latter explanation appears less likely since human G6PC2 (6,35) and
  mouse G6pc2 (9,36) are only expressed in islets and not in liver."].
- Bgee (paralog-controlled, supporting only): in the gluconeogenic context G6pc2 has 9
  present (all low; best renal corpuscle 55.3) and 10 absent calls (left lobe of liver absent
  36; duodenum absent 27), 1/10 top tissues in context (chance 0.4); G6pc1 17 present/4
  absent, top in context left lobe of liver 97.9, 6/10 in context. G6pc3 near-ubiquitous.
  Caveat: G6pc2 does have low present calls in adult liver (46-60, Affymetrix|RNA-Seq) and
  developing kidney, matching the trace extra-islet expression reported by PMID:12878201 and
  PMID:32213654. Low presence is not absence; the argument rests on the literature and the
  sister-paralog contrast, with expression as consistency only.
- The gluconeogenesis_human module marks G6PC2 as a "paralog trap". That is a modelling
  decision, so I did not cite it as independent evidence. Note: that module's note calls
  G6PC2 "largely catalytically inactive autoantigen", which overstates the case (activity is
  low but real and abolished in KO islets). Module-level issue; not edited here.
- Human G6PC3 review keeps its gluconeogenesis IBA as KEEP_AS_NON_CORE (G6pc3 has its own
  experimental glucose-production evidence). The G6PC2 decision is paralog-specific and does
  not conflict.

### Insulin secretion and glucose homeostasis

- ISO/IEA rows come from human Q9NQR9, whose IMP rows cite PMID:20668700 (a Chinese
  population SNP association study of GCK/GCKR/G6PC2/MTNR1B), i.e. genetic association,
  not a perturbation of the protein. The mouse KO data independently support the claims.
- GO:0042593 glucose homeostasis: only child is intracellular glucose homeostasis (not
  applicable). ACCEPT both rows.
- GO:0050796 regulation of insulin secretion: MODIFY both rows to GO:0061179 negative
  regulation of insulin secretion involved in cellular response to glucose stimulus (verified
  in OLS; is_a GO:0046676 and GO:0061178). Participation test: G6pc2's own catalysis is the
  mechanism (it opposes glucokinase on the glycolytic entry step), so it does part of the work.
- No NEW rows: the existing rows plus the MODIFY replacement cover the supported biology.

### Cellular component

- ER (GO:0005783): root organelle term, informative. IBA (seeded by MGI:1277193 itself plus
  G6pc1/G6pc3), IEA (ARBA) and IDA all ACCEPT.
- IDA PMID:10787428 is a Niemann-Pick C1 localization paper; the cached abstract is explicitly
  about NPC1 ("we use subcellular fractionation and microscopy to determine the localization of
  the murine Niemann-Pick C1 (NPC1) protein") and does not mention IGRP/G6pc2. Full text (JLR)
  returned 403 from both jlr.org and the OA PDF link. ACCEPT (ER location is clearly right on
  other evidence), and record a SUSPECTED WRONG_REFERENCE source defect for MGI (CHECK).
- ER membrane (GO:0005789): IEA SubCell + ISS 10078553; human IGRP topology paper fetched
  [PMID:15044018 "IGRP is a glycoprotein, held in the endoplasmic reticulum by nine
  transmembrane domains"]. ACCEPT both.
- membrane (GO:0016020) IBA: generic, MODIFY to GO:0005789.

### Curation gaps (not knowledge gaps)

- The beta_cell_glucose_stimulated_insulin_secretion module does not include the
  glucokinase/G6PC2 substrate cycle; a candidate modulatory node for module curators.
- No human G6PC2 review exists in the repository.
- UniProt Q9Z186 FUNCTION text still reads "May hydrolyze ... May be responsible for glucose
  production through glycogenolysis and gluconeogenesis (By similarity)" and carries the
  gluconeogenesis PATHWAY line; recorded as source defects.

### Deep research (claude_code) verification

- Verified: identity, 9 TM helices, active-site residues, Km values, KO phenotypes, futile
  cycle model, ER retention signal.
- Errors: says mouse GOA carries a Reactome-based GO:0004346 assertion (it does not; the
  Reactome EXP is on human Q9NQR9); says the glucose homeostasis / insulin secretion rows
  are "IMP/ISO from the knockout work" (mouse rows are ISO/IEA from human, whose IMP source is
  the SNP study PMID:20668700). Neither affects the review's conclusions.

## 2026-11-09: targeted check — does G6pc2 contribute to glucose production?

Question: is there any direct measurement of glucose production or gluconeogenic flux in
G6pc2-deficient animals or G6PC2 variant carriers that could overturn the gluconeogenesis REMOVE?
PubMed searches combined G6pc2/IGRP/G6PC2 with clamp, tracer, isotope, glucose production,
glucose turnover, pyruvate tolerance and gluconeogenesis, plus searches for human variant studies
of hepatic or endogenous glucose production and for extra-islet expression.

- The only direct measurement found is human and nominal: [PMID:19669124 "Among elderly twins, G
  allele carriers had higher basal hepatic glucose production (p = 0.04)."] It is a subgroup of
  159 twins at the G6PC2/ABCB11 locus, and the same allele raised early insulin responses, so it is
  compatible with a higher defended glucose level and does not place G6PC2 in hepatic
  gluconeogenesis. Pound et al. weighed exactly this alternative: [PMID:23274894 "The latter
  explanation appears less likely since human G6PC2 (6,35) and mouse G6pc2 (9,36) are only
  expressed in islets and not in liver."]
- No mouse study found measures glucose production in G6pc2-null mice. Added as a suggested
  experiment (tracer flux, pyruvate tolerance and clamp in global and beta-cell knockouts).
- Extra-islet expression in mouse is trace: [PMID:16477532 "was detectable only in hypothalamus
  tissue at increased template inputs"].
- Birds: poultry liver studies measure a nutritionally regulated hepatic G6PC2 transcript
  [PMID:31676410 "hepatic G6PC2 mRNA levels in males"]. Bgee shows chicken G6PC1 is the liver and
  kidney paralog (scores 99) while chicken G6PC2 is low everywhere (liver 40), and no chicken
  pancreas or islet sample exists (file:mouse/G6pc2/G6pc2-bioinformatics/chicken_paralogs.md).
  So the evidence for a non-gluconeogenic, islet-restricted G6PC2 is mammalian; the suggested IRD
  was scoped to the mammalian G6PC2 node PTN000287500, with the Euteleostomi node PTN002650241
  left as a question.

Outcome: the REMOVE stands. The reason now weighs PMID:19669124 explicitly.

## 2026-11-09: blinded OpenScientist check on gluconeogenesis

Run: `just gene-hypothesis-research openscientist mouse G6pc2 --record-slug
existing-go-0006094-remove --as-function-hypothesis` (3 iterations). The prompt held the neutral
hypothesis "G6pc2 has gluconeogenesis (GO:0006094)", the term, the deep-research file and four
PMIDs cited by this review (32213654, 23274894, 10078553, 25552595); it did not hold the REMOVE
decision, its rationale, the Bgee report or the literature check above. Report:
`G6pc2-hypotheses/function-hypothesis-go-0006094/openscientist.md`.

- Verdict agrees: [file:mouse/G6pc2/G6pc2-hypotheses/function-hypothesis-go-0006094/openscientist.md
  "The gluconeogenesis BP should be removed or flagged as a non-core, paralog-driven IBA
  carry-over."] It keeps glucose-6-phosphatase activity and lists GO:0061179 among the process
  terms that fit, as this review does.
- It used no expression atlas. Its first proposed confirmatory test was an atlas cross-check of
  G6PC2 against G6PC1/G6PC3 in gluconeogenic tissues, which the held-out Bgee report supplies, so
  expression corroborated a conclusion the literature already supported.
- Weaker than the review on two points: it calls G6pc2 absent from liver (trace expression is
  reported), and it missed PMID:19669124 and the non-mammalian G6PC2 question.
- Spot-checked quotations (PMID:32213654, PMID:23274894, PMID:10078553) are verbatim.

## 2026-11-10: alpha-cell function added (Bahl 2025), during the human G6PC2 review

While reviewing human G6PC2 (`genes/human/G6PC2/`) I read the full text of Bahl et al. 2025
(PMID:39742505, Sci Transl Med), which was not in this review. It is the first functional
study of G6PC2 in alpha cells and it uses a mouse conditional knockout, so it is mouse
evidence and belongs here.

### What the paper shows

- New conditional allele (`G6pc2loxP/loxP`, exons 1-3 floxed) crossed to Gcg-CreERT2;
  tamoxifen ablated G6pc2 in [PMID:39742505 "G6pc2 expression was ablated in 88% of α cells"].
- No change in islet composition or turnover [PMID:39742505 "We observed no changes in
  proliferation of α or β cells, nor in their relative proportions in islets of 12-week-old
  α-G6PC2KO versus age-matched control mice"].
- Direction and condition: glucagon was stimulated with a 4 mM amino acid mixture and then
  suppressed by rising glucose. At zero glucose secretion was identical; [PMID:39742505 "when
  incubated in the presence of 0.5mM, 1mM, 3mM, or 5mM glucose, α-G6PC2KO islets secreted
  significantly (P < 0.0001) less glucagon relative to control islets, confirming a left shift
  in the glucose response curve for glucagon release"]. So the affected process is **glucose
  suppression of amino-acid-stimulated glucagon secretion**, and losing G6pc2 makes suppression
  happen at lower glucose.
- In vivo: [PMID:39742505 "revealed lower glucagon concentrations in both male and female
  α-G6PC2KO mice relative to controls"] with insulin unchanged; slower recovery from
  insulin-induced hypoglycaemia with hypoglucagonaemia at 30 min; and under 14 days of
  phloridzin, lower glucagon with unchanged insulin, which excludes increased alpha-cell
  insulin sensitivity as the cause. Males had significantly lower blood glucose after a 16 h
  fast.
- Mechanism: 2-NBDG efflux was retained in mutant islets, consistent with loss of futile
  cycling in the mutant alpha cells; the authors' model is the same glucokinase-opposing cycle
  as in beta cells [PMID:39742505 "The catalytic subunit of the islet-specific
  glucose-6-phosphatase enzyme (G6PC2) opposes the action of glucokinase and creates a futile
  substrate cycle"].
- Human arm: G6PC2 protein is detectable in human alpha cells, 2-NBDG efflux from human alpha
  cells falls on knockdown, and shRNA knockdown in sorted primary human alpha cells
  (pseudo-islets) reproduces the leftward shift with unchanged glucagon content.

### What changed in this review

- **NEW row GO:0070094 positive regulation of glucagon secretion, IMP, PMID:39742505.**
  Sign: deleting G6pc2 lowers glucagon at a given glucose, so G6pc2 is a positive regulator.
  GO:0070094 checked in OLS (is_a GO:0070092 and GO:0090277; no children). There is no
  glucagon analogue of GO:0061178/GO:0061179, so the set-point condition is stated in the
  row summary; raised as a suggested question in the human review.
  Participation test: the regulated step is alpha-cell glycolytic flux and G6pc2's own G6P
  hydrolysis is what lowers it, so the gene product does the work. Comparator check (QuickGO,
  exact term, human and mouse): Pask GO:0070092 IMP PMID:21181396, Kcnk16 GO:0070092 IMP
  PMID:29402588, Syt7 GO:0070092 IMP PMID:19171650, Ffar4 GO:0070094 IMP PMID:24742677 - so
  cell-intrinsic regulators of alpha-cell glucagon release do carry these terms. Gck carries
  none, which is a curation lag on the recent alpha-cell GCK literature, not a convention.
- **Description revised.** It said G6pc2 is "expressed almost exclusively in pancreatic islet
  beta cells"; that overstated the restriction. It now says islet endocrine cells, about
  twenty-fold more in beta than alpha cells, and describes both hormonal arms.
- **core_functions** gained GO:0070094 under `directly_involved_in`, CL:0000171 pancreatic A
  cell under `anatomical_locations`, a two-cell-type description, and the Bahl quote under
  `supported_by`.
- **PMID:39121091 reference_review revised.** It previously read "a possible alpha-cell role is
  argued mainly for humans, so no glucagon-secretion term is proposed". That reasoning is
  superseded: the paper's prediction was right and a mouse effect is demonstrable despite the
  20-fold bias. Its inference from unchanged fasting glucagon in germline knockouts
  [PMID:39121091 "These observations are consistent with the absence of a change in fasting
  glucagon levels in G6pc2 KO mice"] did not hold for the conditional knockout. Relevance
  raised LOW to MEDIUM and two findings added.
- **Gluconeogenesis IBA reason extended.** The alpha-cell result does not weaken the REMOVE,
  it strengthens it: both arms of the fasting-glucose phenotype are islet-hormonal (insulin
  from beta cells, glucagon from alpha cells) and neither involves glucose output by the islet.
- **suggested_questions**: the old question "Does G6pc2 influence glucagon secretion from mouse
  alpha cells, or is that role confined to species with higher alpha-cell expression such as
  human?" is answered for mouse, and was replaced by the open quantitative question - how much
  of the global-knockout fasting-glucose phenotype comes from each arm, and whether the balance
  differs in human.

Validation: `env -u UV_NATIVE_TLS just validate mouse G6pc2` passes with no errors, after
`just backfill-record-sections genes/mouse/G6pc2` (no changes needed; the new quotes are
publication quotes, not UniProt).
