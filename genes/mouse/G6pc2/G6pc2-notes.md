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
