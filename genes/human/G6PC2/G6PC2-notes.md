# G6PC2 (human, Q9NQR9, HGNC:28906) review notes

## 2026-11-10 Session 1: de novo review

### Context

Reviewed as part of the BGEEDB_EXPRESSION project (projects/BGEEDB_EXPRESSION.md),
as the human counterpart of the already-completed mouse review
(`genes/mouse/G6pc2/G6pc2-ai-review.yaml`). The project's controlled design for this
family is the sister paralogs G6PC1/G6PC3 against G6PC2 in the tissues where
gluconeogenesis can run (liver, kidney cortex, small intestine; from the
pathway-satisfiability engine).

Inputs: 13 GOA rows (3 MF, 5 CC, 5 BP), the UniProt record, the claude_code
deep-research file (treated as a lead list), the generated Bgee report
(`G6PC2-bioinformatics/RESULTS.md`), the two cached Reactome entries, and the mouse
review as the consistency reference. Each row was judged on human evidence; the
places where human and mouse evidence differ are flagged below.

### Where human evidence differs from mouse

Three differences matter for this review:

1. **The catalytic activity is experimentally established on the human protein.**
   Mouse rested partly on inference from PMID:14722102 (whose abstract does not state
   the construct's species) plus knockout islets. For human there is direct
   structure-function work: PAP2-motif mutagenesis of human G6PC2 expressed in
   islet-derived 832/13 cells [PMID:38095063 "The data show that individual mutation
   of residues in all six regions of the PAP2 motif resulted in a significant decrease
   in enzyme activity"], including the four predicted catalytic residues Arg79, His115,
   Arg168 and His174, and detectable microsomal activity from the human ORF
   [PMID:34954144 "low microsomal G6Pase activity could now be detected in vitro
   following transient expression of G6PC2 in 832/13 cells"].
2. **The subcellular location is experimental for human, by-similarity for mouse.**
   UniProt's `SUBCELLULAR LOCATION: Endoplasmic reticulum membrane` carries
   `ECO:0000269|PubMed:15044018` on Q9NQR9 but `ECO:0000250` on Q9Z186: PMID:15044018
   is a topology and glycosylation study of the *human* protein.
3. **The expression argument is weaker in human.** Mouse had 10 absent calls in the
   gluconeogenic context; human has none. In human the only calls there are low present
   calls (duodenum 51, metanephros cortex 43, liver 41, right lobe of liver 40, cortex
   of kidney 38, small intestine 33) against G6PC1 at 98/97
   (file:human/G6PC2/G6PC2-bioinformatics/RESULTS.md). Per the project's rules of use,
   human expression is cited as a paralog-controlled consistency check only, never as
   the deciding line.

### Identity and protein features

- 355 aa, 9 predicted TM helices (UniProt TRANSMEM 25-45 ... 319-339, ECO:0000255),
  lumenal N-terminus and cytoplasmic C-terminus, C-terminal ER-retention motif 352-355
  ("Prevents secretion from ER", ECO:0000255). Active sites His115 (proton donor,
  ECO:0000255) and His174 (nucleophile, ECO:0000250); substrate-binding Arg79 and
  Arg168.
- N-glycosylated at Asn92, established by mutagenesis
  [file:human/G6PC2/G6PC2-uniprot.txt "N->A: Loss of N-glycosylation."]; the
  non-glycosylated form is unstable and proteasome-degraded (UniProt PTM, ECO:0000269).
- PANTHER PTHR12591:SF1 (GLUCOSE-6-PHOSPHATASE 2); InterPro IPR016275, PIRSF000905,
  Pfam PF01569 (PAP2), CDD cd03381 PAP2_glucose_6_phosphatase. No FamilyReview exists
  for PTHR12591 (only entries/metadata/paint.tsv), so there are no `member_exceptions`
  to manage.
- Both alternative products are catalytically dead by inspection of the VAR_SEQ
  features: isoform 2 (VSP_033648/VSP_033649) replaces 74-102 and deletes 103-355, so
  it loses both His115 and His174; isoform 3 (VSP_046180/VSP_046181) replaces 148-154
  and deletes 155-355, so it keeps His115 but loses His174. No annotation is isoform
  scoped, and all 13 GOA rows concern the displayed isoform, so no `isoform` fields
  were added. (PMID:16520917 reports differential splicing in thymus and spleen versus
  pancreas; that is relevant to immune tolerance, not to enzymology, and is not cached.)

### Catalytic activity (GO:0004346): ACCEPT all three rows, core

- Reaction and kinetics: [file:human/G6PC2/G6PC2-uniprot.txt "Reaction=D-glucose
  6-phosphate + H2O = D-glucose + phosphate;"] with
  `Evidence={ECO:0000269|PubMed:14722102}`; KM 0.45 mM at pH 6.5
  [PMID:14722102 "The K(m) and V(max) values determined using glucose-6-phosphate as
  the substrate were 0.45 mm and 32 nmol/mg/min by malachite green assay"].
- Human-specific mutagenesis confirms the motif is required
  [PMID:38095063 "These data support the AF2 model and indicate that G6PC2 contains a
  bona fide PAP2 motif critical for its hydrolysis of G6P."].
- Intrinsically low turnover relative to G6PC1 [PMID:34954144 "G6PC1 exhibited much
  higher G6Pase activity than G6PC2 in these in vitro assays"];
  [PMID:38431189 "the observed Vmax for G6P hydrolysis by G6PC1 was considerably greater
  than that for G6PC2 and G6PC3"].
- ENZYME_SPECIFICITY judgement: not promiscuous noise. G6P hydrolysis is the protein's
  own reaction, it owns the reaction in islets (G6PC1 is not detected in islets in mouse
  [PMID:32213654 "G6pc2 expression is much higher than G6pc3 in both pancreas and islets
  with G6pc1 expression not detected"], and human islet G6PC1 sits at 69 against G6PC2 at
  99 in Bgee), human coding variants that reduce the protein or its activity shift fasting
  glucose [PMID:34954144], and loss of the activity has an in vivo phenotype. Low Vmax is
  the physiology (a modulator of glucokinase flux), not evidence against function.
- The IBA's `WITH/FROM` includes UniProtKB:Q9NQR9 itself. Per CLAUDE.md that is expected
  and is a marker of experimental grounding on the target, not circularity.

### Localisation

- ER (GO:0005783): root organelle term, informative, so ACCEPT both synthesis rows
  (IBA from PTN000971890, seeded by mouse G6pc1/G6pc2/G6pc3 and human G6PC3; IEA from
  ARBA00028672 plus the mouse ortholog). The organelle claim holds on independent human
  grounds: [PMID:15044018 "IGRP is a glycoprotein, held in the endoplasmic reticulum by
  nine transmembrane domains"], the ER-retention motif, and Asn92 glycosylation.
- ER membrane (GO:0005789): ACCEPT the SubCell IEA and the Reactome TAS. UniProt's
  ER-membrane and multi-pass statements are `ECO:0000269|PubMed:15044018` on the human
  entry, and the Reactome reaction places the catalysis on the ER membrane with the ER
  lumen as the other compartment, matching the lumen-facing active site. No NEW
  sub-compartment row is needed: the gene already carries it.
- membrane (GO:0016020) IBA: a generic term, not a root organelle term, so the
  "correct but general is MODIFY" rule applies. MODIFY to GO:0005789, which the gene
  already carries.

### Gluconeogenesis (GO:0006094): REMOVE all three rows (IBA, IEA, Reactome TAS)

Same conclusion as mouse, reached on human evidence, plus one row mouse did not have.

- **IBA.** The IBD sits at PTN000971890 (taxon:6072) and its GO:0006094 seeds are
  FB:FBgn0031463, MGI:1915651 (G6pc3), MGI:95607 (G6pc1), RGD:2644, RGD:727875 and
  UniProtKB:P35575 (G6PC1) — no G6PC2 among them
  (interpro/panther/PTHR12591/PTHR12591-paint.tsv, dated 20241120).
  `just paint-losses human G6PC2`: "No IRD or IKR loss on this gene's lineage", so the
  row is current and the argument is with the node reaching the G6PC2 clade. Human
  G6PC2's path is PTN000971890 > ... > PTN002650241 > PTN000287500 > ... > PTN002488967
  (projects/BGEEDB_EXPRESSION/data/panther_leaves.tsv).
- **Biology.** G6PC2 is pancreas and islet restricted
  [file:human/G6PC2/G6PC2-uniprot.txt "Specifically expressed in pancreas and also"
  (detected to a lower extent in testis), ECO:0000269|PubMed:11297555]. In islet cells
  its substrate is glucokinase-derived G6P, so its activity is a futile substrate cycle
  that lowers glycolytic flux [PMID:25552595 "glucose cycling was abolished in G6pc2 KO
  mouse islets, confirming that G6pc2 opposes the action of the glucose sensor
  glucokinase by hydrolyzing G6P"], not a route from pyruvate, lactate, glycerol or amino
  acids to glucose (the GO definition of gluconeogenesis). Islet cells do not export
  glucose to the blood; the demonstrated consequences of the activity are the glucose set
  points of insulin and glucagon secretion.
- **Bgee (supporting only).** 8 present and 0 absent calls in the gluconeogenic context,
  all low, versus G6PC1 at 98 in liver; 2/10 top tissues in context (chance 0.9) against
  5/10 for G6PC1. Low presence is not absence, so this is consistency, not the argument.
- **The one direct measurement is human and nominal.** [PMID:19669124 "Among elderly
  twins, G allele carriers had higher basal hepatic glucose production (p = 0.04)."]
  Because it is human it deserves more weight here than in the mouse review, and it is
  still not enough: a subgroup of 159 twins, unreplicated, at a locus that also contains
  ABCB11, with the same allele raising early insulin responses, i.e. compatible with a
  higher defended glucose level rather than with hepatic G6PC2 catalysis. Pound et al.
  weighed exactly this alternative [PMID:23274894 "The latter explanation appears less
  likely since human G6PC2 (6,35) and mouse G6pc2 (9,36) are only expressed in islets and
  not in liver."]
- **Reactome TAS (new relative to mouse).** The reaction behind the TAS is explicitly the
  islet reaction — `R-HSA-3266566` "G6PC2 hydrolyzes G6P to form Glc and Pi (islet)",
  [Reactome:R-HSA-3266566 "This enzyme is expressed in islet cells of the pancreas
  (Petrolonis et al. 2004)."] — yet it is a contained event of `R-HSA-70263`
  Gluconeogenesis, whose own summary says [Reactome:R-HSA-70263 "Gluconeogenesis is
  confined to cells of the liver and kidney"]. I confirmed the containment through the
  Reactome ContentService: `pathways/low/entity/R-HSA-3266566` returns R-HSA-70263, and
  that pathway's contained events list the liver (G6PC), ubiquitous (G6PC3) and islet
  (G6PC2) hydrolysis reactions side by side. So Reactome's placement contradicts its own
  statement of the pathway's tissue scope, and the GOA TAS inherits the contradiction.
  Recorded as a source defect for Reactome (CHECK: move the islet reaction out of
  Gluconeogenesis). The same reaction remains sound support for the ER membrane TAS; only
  the pathway placement is at issue.
- **Paralog contrast is deliberate.** The human G6PC3 review keeps its gluconeogenesis
  rows as KEEP_AS_NON_CORE because mouse G6pc3 has its own experimental glucose-production
  evidence in astrocytes (PMID:15661744). G6PC2 has no such evidence in any tissue or
  species, so the decisions do not conflict; they are paralog specific.
- **UniProt source defects** (as in mouse, now on Q9NQR9): the FUNCTION text is still a
  by-similarity carry-over from G6PC1 ("May be responsible for glucose production through
  glycogenolysis and gluconeogenesis", ECO:0000250) even though human-specific
  experimental data now exist, and the `PATHWAY: Carbohydrate biosynthesis;
  gluconeogenesis` line (with the matching KW) is what GO_REF:0000041 maps to GO:0006094.

### Glucose homeostasis (GO:0042593): ACCEPT

- The IMP source is a 6,822-participant Chinese replication study
  [PMID:20668700 "We replicated the association between GCK rs1799884, G6PC2 rs16856187
  and MTNR1B rs10830963 and fasting glucose in our samples"]. A population association is
  weak as a perturbation of the protein, but the claim is independently established for
  human: coding variants that reduce G6PC2 protein or activity track with fasting glucose
  [PMID:34954144], the promoter work ties the FPG-raising allele to higher promoter
  activity [PMID:20622168 "the rs13431652-A allele is associated with both elevated FPG
  (Table 1) and G6PC2 promoter activity"], UniProt records the locus as FGQTL1, and the
  mouse knockouts give the mechanism.
- GO:0042593 has exactly one child, intracellular glucose homeostasis (checked in OLS),
  which does not apply, so the term is as precise as warranted.

### Regulation of insulin secretion (GO:0050796): MODIFY to GO:0061179

- The human direction is in the IMP source itself: in Table 2 the fasting-glucose-raising
  allele at G6PC2 rs16856187 is associated with *lower* first-phase insulin secretion
  (beta -0.0245, SE 0.0096, p = 0.0108) and lower second-phase secretion under a dominant
  model (p = 0.0431), i.e. more G6PC2 activity goes with less glucose-stimulated insulin
  release. Corroborated in a second human cohort [PMID:34128214 "Two G6PC2 variants
  (rs13387347 and rs560887) were associated to both parameters of insulin secretion (DC
  and PC) and to fasting C-peptide levels"].
- The sign and the stimulus are established mechanistically in beta cells
  [PMID:23274894 "These data suggest that G6pc2 represents a novel, negative regulator of
  basal GSIS that acts by hydrolyzing glucose-6-phosphate, thereby reducing glycolytic
  flux."]; [PMID:35176280 "deletion of G6pc2 led to ∼60% increases in glycolytic and
  citric acid cycle (CAC) fluxes at both 5 and 11 mM glucose concentrations"].
- Participation test: G6PC2's own catalysis opposes glucokinase at the entry to
  glycolysis, which is the step that sets the glucose sensitivity of insulin release, so
  the gene product does part of the work of the process.
- GO:0061179 verified in OLS: "negative regulation of insulin secretion involved in
  cellular response to glucose stimulus", an is_a descendant of GO:0050796 via GO:0046676
  and GO:0061178. Same replacement as the mouse review.

### NEW: positive regulation of glucagon secretion (GO:0070094), IMP PMID:39742505

Bahl et al. 2025 (Sci Transl Med, full text cached) is the first functional study of
G6PC2 in alpha cells, and it has a human arm.

- **What was done in mouse.** An inducible, alpha-cell-specific deletion
  (`G6pc2loxP/loxP; Gcg-CreERT2`, 88% of alpha cells) with no change in islet composition,
  alpha/beta proportions or proliferation.
- **Direction and condition.** Glucagon was stimulated by a 4 mM amino acid mixture and
  then suppressed by rising glucose. At zero glucose secretion was the same in both
  genotypes; [PMID:39742505 "when incubated in the presence of 0.5mM, 1mM, 3mM, or 5mM
  glucose, α-G6PC2KO islets secreted significantly (P < 0.0001) less glucagon relative to
  control islets, confirming a left shift in the glucose response curve for glucagon
  release"]. So the specific change is in **glucose suppression of amino-acid-stimulated
  glucagon secretion**: losing G6PC2 makes suppression happen at lower glucose.
  In vivo, [PMID:39742505 "revealed lower glucagon concentrations in both male and female
  α-G6PC2KO mice relative to controls"], with insulin unchanged, and the same during an
  insulin tolerance test and under phloridzin, which excludes a paracrine insulin
  explanation. Summarised by the authors as [PMID:39742505 "Using inducible, cell
  type-specific gene ablation of G6pc2 in mice we document a dramatic shift in the
  set-point for glucose suppression of glucagon secretion, resulting in more than
  half-maximal reduction in glucagon release from isolated islets at 1 mM glucose."]
- **What was shown in human cells.** G6PC2 protein is in human alpha cells
  [PMID:39742505 "we performed immunofluorescent staining on non-diabetic human pancreatic
  sections for G6PC2, insulin, and glucagon, and found that the G6PC2 protein is indeed
  detectable in human α cells"]; the futile cycle runs there
  [PMID:39742505 "the efflux of 2-NBDG from human α cells was significantly reduced after
  shRNA-mediated suppression of G6PC2"]; and shRNA knockdown (86% mRNA reduction) in
  sorted primary human alpha cells aggregated into >90% alpha-cell pseudo-islets made
  glucagon secretion more glucose sensitive at 1, 3, 5 and 9 mM glucose, with
  [PMID:39742505 "Total glucagon content was not different between the two experimental
  groups"]. Allele-specific expression at rs2232328 in human alpha cells from four donors
  ties the fasting-glucose-raising allele to higher alpha-cell G6PC2.
- **Sign.** Loss of G6PC2 lowers glucagon output at any given glucose (and lowers maximal
  secretion in the human pseudo-islets), so G6PC2 is a **positive** regulator of glucagon
  secretion. GO:0070094 "positive regulation of glucagon secretion" (checked in OLS;
  is_a GO:0070092 and GO:0090277; no children) is the correctly signed term. There is no
  "glucagon secretion involved in cellular response to glucose stimulus" analogue of
  GO:0061178, so the set-point detail stays in the row's summary rather than in the term.
- **Participation test.** The regulated step is alpha-cell glycolytic flux, and G6PC2's
  own G6P hydrolysis is what lowers it; the paper's model is explicit that the enzyme
  opposes glucokinase [PMID:39742505 "The catalytic subunit of the islet-specific
  glucose-6-phosphatase enzyme (G6PC2) opposes the action of glucokinase and creates a
  futile substrate cycle"]. The gene product does the work; this is not a
  "required for" or substrate relationship.
- **Comparator check.** Cell-intrinsic regulators of alpha-cell glucagon release do carry
  these terms, so there is no convention against annotating an intracellular islet enzyme
  here: QuickGO (exact-term query over human and mouse, 2026-11-10) returns PASK
  GO:0070092 IMP PMID:21181396, KCNK16 GO:0070092 IMP PMID:29402588, SYT7 GO:0070092 IMP
  PMID:19171650 and Ffar4 GO:0070094 IMP PMID:24742677. Glucokinase itself (P35557)
  carries no glucagon term despite the alpha-cell GCK knockout literature, which reads as
  a curation lag on recent papers rather than a convention — and GCK's absence cannot
  argue against a row that rests on direct evidence rather than on pathway completeness.
- **Prior expectation revised.** The O'Brien group predicted the alpha-cell role but
  argued it would matter mainly in human, because mouse G6pc2 is ~20-fold beta-biased
  while human is only ~5-fold [PMID:39121091 "In contrast, in humans, relative to mice,
  G6PC2 expression is reduced in β-cells (695 vs 1097 RPLM) and elevated in α-cells (141
  vs 59 RPLM)"], and because germline knockouts showed no change in fasting glucagon. The
  conditional knockout overturns that negative: a cell-autonomous alpha-cell effect is
  demonstrable in mouse, and is confirmed in human cells. The mouse review was updated in
  the same session.

### Curation gaps (not knowledge gaps)

- The `beta_cell_glucose_stimulated_insulin_secretion` module does not include the
  glucokinase/G6PC2 substrate cycle, and no module covers the alpha-cell set point; both
  are candidate modulatory nodes for module curators.
- `modules/gluconeogenesis_human.yaml` calls G6PC2 a "largely catalytically inactive
  autoantigen" in its paralog-trap note. The paralog-trap decision is right, but the
  parenthetical overstates the case: the activity is low but real, is required for the
  islet glucose cycle, and human PAP2-motif mutagenesis measures it directly
  (PMID:38095063). Module-level issue, not edited here (same note as in the mouse review).
- Human G6PC2 had no review until now; G6PC1 and G6PC3 reviews exist and were consulted
  for consistency.

### Deep research (claude_code) verification

- Verified: identity, family and domains, 9 TM helices, active-site and substrate-binding
  residues, the Km values, ER membrane location and Asn92 glycosylation, the futile-cycle
  model, the beta-cell and alpha-cell knockout results, the nsSNP and promoter genetics,
  and the autoantigen material. Its own caveats about unread full texts are honest, and
  its table of per-row assessments agrees with the actions reached here.
- Errors and weaknesses found:
  - It says "glucose-6-phosphatase activity and glucose cycling are abolished in G6pc2
    knockout islets", citing Bosma 2020 (PMID:32213654). The activity is *reduced*, not
    abolished, and the measurement is in Pound 2013 (PMID:23274894) and Wall 2015
    (PMID:25552595), not Bosma.
  - It attributes "Arg79Gln, Gly114Arg and Ser324Pro reduce activity without affecting
    expression" to Boortz 2016 as tested "in mouse G6pc1 as a surrogate"; PMID:34954144
    reports Gly114Arg among the variants assayed directly on human G6PC2, so the surrogate
    framing is out of date.
  - It cites several sources only as PMC ids or publisher URLs, including Shieh 2005
    (Diabetologia) and the Wall 2015 PDF, which cannot be resolved to PMIDs without
    further checking; I did not use any claim that rested only on those.
  - It did not retrieve PMID:20668700 (the IMP source) at all, so its assessment of the
    two IMP rows was made without the evidence; and it did not look up any GO term ids.
  None of these affect the conclusions reached independently above.

### Validation

`env -u UV_NATIVE_TLS just validate human G6PC2` and the equivalent mouse command were
run to completion with no errors. `just backfill-record-sections genes/human/G6PC2` was
run after the final edit to derive `record_section` on the UniProt quotes.
