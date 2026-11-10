---
title: "Bgee expression as evidence: explaining, corroborating and contesting function"
maturity: IN_PROGRESS
tags: [PIPELINE, EVALUATION]
species: [human, mouse]
autolink_exclude: [old, Dark, RPE]
genes: [PAX6, G6pc2, Pax4, ATOH1, OLIG2, MITF, GCG, CRYAA, G6PC1, G6PC3, ACTL8, AGFG1, AGFG2, GBX2, FGF8, PTF1A, RORA, RELN, SHH, SMO, FBXO41, DNER, PTPN11, EN1, EN2]
---

# Bgee expression as evidence

**Bottom line:** Bgee expression is a useful *consistency* check on GO
annotations but a poor *discriminator* between good and bad ones. It becomes
real evidence only where something controls for what the data cannot see:

- a sister paralog that is detected in the same anatomy;
- a satisfiability context that says where a pathway must run;
- stage-resolved data for a developmental step.

We joined Bgee 15.2 calls to 12,080 reviewed human annotations whose GO term names an anatomy (via go-plus logical
definitions such as *eye development* `results_in_development_of` eye). The
term's anatomy is among the gene's top-10% tissues for 46% of ACCEPT rows,
against 26% for the same terms paired with a random gene. So annotations and
expression agree well beyond chance. But MARK_AS_OVER_ANNOTATED rows are just
as concordant (43%): expression in a tissue does not make a gene act there,
which is the old lesson of IEP in numbers. Absence carries the signal people
hope for, but only after four predictable artifacts are screened out:

- developmental terms read against adult data;
- regulators and secreted ligands acting on other cells;
- transcriptionally silent cells;
- rare cells diluted in bulk tissue.

Once those are screened, true absence is rare (0.5% of ACCEPT rows that have data,
1.3% by chance). The project's positive results are the three controlled
designs. G6PC1, G6PC2 and G6PC3 all inherit *gluconeogenesis* from one PAINT
node, but only G6PC1's top tissues fall where the satisfiability engine says
gluconeogenesis can run. AGFG2 and ACTL8 are absent from the anatomy of an
inherited IBA term in which their sister paralog is detected. And the
cerebellum-development module switches on in a staggered wave that broadly
follows module order. The wave also exposes two module-modelling issues and two
gaps in the Cell Ontology. Full reviews of mouse G6pc2 and Pax4, the two
strongest paralog leads, removed the inherited gluconeogenesis, brain and
forebrain terms and marked the retina terms as over-annotations. In both,
expression was one supporting line among phylogeny, phenotype and literature,
never the deciding one. The Pax4 review also traced an expression-only (IEP)
rat annotation into both an orthology projection and a PAINT seed.

## Contents

- [Why expression, and why carefully](#why-expression-and-why-carefully)
- [How it works](#how-it-works)
- [Results](#results)
- [Rules of use](#rules-of-use-when-expression-can-count)
- [Leads for curators](#leads-for-curators)
- [Limitations and next steps](#limitations-and-next-steps)
- [Methods & reproduction](BGEEDB_EXPRESSION/methods.md)

## Why expression, and why carefully

PAX6 is expressed in the eye, and that should be explainable by what PAX6
does. Expression has also been abused in GO: IEP annotations turn "transcript
changes in condition X" into "involved in X". The question here is narrower.
Can expression add weight to other evidence in clear cases? And can it lend
evidence *against* a function, for example against a paralog inheriting a
function by phylogenetic propagation? The project tests three uses:

1. **Explain** a gene's expression by its reviewed functions, and find top
   tissues that no function explains.
2. **Corroborate or contest** an annotation, calibrated against the
   decisions reviewers have already made in this repository, and sharpened by
   comparing paralogs below the PAINT node (PTN) that propagated the term.
3. **Time** a developmental module, extending
   [pathway satisfiability](PATHWAY_SATISFIABILITY.md) from "can this pathway
   run in this tissue?" to "is each step's gene on, where the step acts, when
   it acts?". This uses the [cerebellum development module](../modules/cerebellum_development.html).

## How it works

- **Anatomy of a GO term.** go-plus logical definitions and existential
  axioms supply UBERON or CL fillers, for example *type B pancreatic cell
  differentiation* → `CL:0000169`. A term without its own anatomy borrows its nearest
  ancestor's, and the classifier records when that anatomy was reached only
  through a `regulates` edge. Physiology and metabolism terms usually name no
  anatomy at all. *Gluconeogenesis* has none, so for it the context comes from
  a module or from satisfiability.
- **Matching a call to an anatomy.** UBERON and CL relations decide how a sampled
  entity relates to a target:
  - *within*: a lens sample for *eye development*;
  - *precursor*: ganglionic eminence for *forebrain development*;
  - *container*: a whole-eye sample for *retina development*;
  - *co-located*: a putamen sample for an oligodendrocyte term, because CL
    places oligodendrocytes in the CNS, not in each region.

  Whole-body samples never count as containers.
- **Tiers.**
  - `ENRICHED`: present, and the anatomy is in the gene's own top 10%.
  - `CONSISTENT`: present, but not enriched.
  - `ABSENT`: Bgee has calls in or around the anatomy, all absent.
  - `NO_DATA`: Bgee has nothing there.
  - Labelled absences that are uninformative: developmental term with
    stage-merged data; regulator; extracellular or ligand product; quiescent
    target cell.
- **Data.** Bgee 15.2 per-species "simple" call files, which hold present
  *and* absent calls merged over stages, for the corpus. The Bgee REST API
  supplies stage-resolved present calls and OMA orthologs. PANTHER 19 trees give
  PTN clades. Details are in [Methods & reproduction](BGEEDB_EXPRESSION/methods.md).

## Results

### 1. Explaining a gene's expression by its functions

For 1,618 human genes with at least one retained anatomy-bearing annotation,
an average of 18.0% of their top-10 Bgee tissues are explained by a retained
annotation, against 10.7% when scored with another gene's annotations. For the
single top tissue the rates are 19.6% and 11.1%. Most explanations are broad.
*Brain development* explains a cerebellum sample, for example, and only 4.2%
(2.0% shuffled) are explained by a target no larger than about 500
anatomical classes. Per-gene tables are in
[tissue_explanation_cases.md](BGEEDB_EXPRESSION/results/tissue_explanation_cases.md).

- **PAX6 (10/10 explained).** Conjunctiva by *camera-type eye development*, β-cells by *type B
  pancreatic cell differentiation*, and the brain samples by forebrain and brain
  development.
- **ATOH1 (7/10 explained).** Seven of its top ten tissues are intestinal
  (colon, rectum, duodenum, appendix, caecum). All seven are explained by
  *intestinal epithelial cell differentiation*.
- **OLIG2 (9/10).** Brain regions are explained through oligodendrocyte terms, co-located
  in the CNS.
- **Unexplained top tissues** are the leads:
  - MITF: retinal pigment epithelium (its top tissue), heart and skeletal
    muscle. The review retains only *melanocyte differentiation* as an
    anatomy-bearing term.
  - GCG: colon and rectum.
  - CRYAA: the lens is not sampled in human Bgee.
  - G6PC1: liver, kidney and intestine.

  The G6PC1 case is instructive. Its top tissues are exactly where the
  [satisfiability engine](PATHWAY_SATISFIABILITY.md) finds gluconeogenesis
  satisfiable, yet no GO anatomy can say so. Explaining expression by a
  metabolic function needs the module's context, not the GO term.
- Only 187 of 16,034 top tissues (1.2%) would be explained by a row the
  reviewers rejected. Reviewers are not discarding annotations that expression
  supports.

### 2. Calibration against reviewers' decisions

![Share of anatomy-bearing annotations whose anatomy is among the gene's top-10% Bgee tissues, by reviewer action, with the shuffled rate as a reference tick](BGEEDB_EXPRESSION/fig-calibration.svg)

*Figure 1. Real gene–term pairs (bars) are concordant with expression well
above chance (dashed tick: same terms, random gene). But
MARK_AS_OVER_ANNOTATED rows are as concordant as ACCEPT rows, and REMOVE rows
nearly so. Generated by `scripts/figures.py` from `results/corpus_calibration.yaml`.*

| | rejected rows | retained rows | ratio (95% CI) |
|---|---|---|---|
| ENRICHED, all evidence | 349/827 | 3157/7647 | 1.02 (0.94–1.11) |
| ABSENT before screening, all evidence | 36/827 | 293/7647 | 1.14 (0.81–1.59) |
| ABSENT before screening, IBA | 4/34 | 30/670 | 2.63 (0.98–7.03) |
| ABSENT before screening, ISS/ISO/ISA | 9/157 | 47/1723 | 2.10 (1.05–4.21) |
| ABSENT after screening, all evidence | 6/827 | 26/7647 | 2.13 (0.88–5.17) |
| ABSENT after screening, IBA | 2/34 | 3/670 | 13.1 (2.3–76) |

*Rejected = REMOVE or MARK_AS_OVER_ANNOTATED; retained = ACCEPT or
KEEP_AS_NON_CORE; rows with no Bgee data excluded. Source:
`results/corpus_calibration.yaml`.*

Presence is not evidence that a function is real: the ENRICHED ratio sits on 1.0.
Absence leans toward rejection for inferred annotations (IBA, ISS), but most
raw absences are artifacts. The table below lists the four failure modes. The
classifier screens each one, and 111 of the 119 absent rows on retained
experimental annotations fell into one of them. The screened IBA ratio is
large, but it rests on five rows (2 rejected, 3 retained), so read it as a
direction, not an effect size.

| failure mode | example from the corpus | screen |
|---|---|---|
| regulator acts on another cell | *positive regulation of endothelial cell proliferation* (13 retained experimental rows) | anatomy reached only via `regulates` |
| secreted / ligand product | CCL11 *eosinophil chemotaxis*, GDF2 *ossification* | gene annotated extracellular (not exosome/vesicle) or receptor ligand |
| quiescent target cell | sperm flagellum and acrosome terms (sperm carry spermatid-made protein) | sperm, erythrocyte, platelet |
| developmental term, adult data | ATOH1, NEUROG1/2 *sensory organ development* | term under *developmental process* |

A fifth failure mode is not screened: rare cells diluted in bulk tissue, or
low-sensitivity single-cell samples. Examples are hair-cell genes (CABP2,
GRXCR2) where the cochlea is not sampled, and ubiquitous MYH9 and PGAM2 read as
absent in oocyte samples. Such cases make up most of the 17 remaining
[leads](BGEEDB_EXPRESSION/results/corpus_leads.tsv), so treat those leads as
prompts to check, not as findings.

### 3. Paralogs at the PTN level: the sister as a positive control

An absent call says little on its own. A sister paralog below the same PAINT
node that *is* detected in that anatomy shows that the anatomy was sampled and
that the assay could see a family member there. That makes the absence a
comparison rather than a missing value.

**G6PC (PTHR12591, node PTN000971890).** The node propagates gluconeogenesis.
GO gives gluconeogenesis no anatomy, so the context is where the
gluconeogenesis module is satisfiable: liver, kidney cortex and small intestine.

| gene | top tissue | top-10 tissues in context (chance) | breadth (share of sampled entities present) |
|---|---|---|---|
| human G6PC1 | liver (98) | 5/10 (1.8) | 0.27 |
| human G6PC2 | islet of Langerhans (99) | 2/10 (0.9) | 0.67 |
| human G6PC3 | adenohypophysis (98) | 1/10 (0.4) | 0.97 |
| mouse G6pc1 | kidney (98) | 6/10 (2.0) | 0.18 |
| mouse G6pc2 | islet of Langerhans (100) | 1/10 (0.4) | 0.29 |
| mouse G6pc3 | choroid plexus (96) | 0/10 (0.4) | 0.86 |

The satisfiability engine already gates gluconeogenesis on G6PC1. Expression
adds that G6PC2 is islet-dominant in both species. Its GOA record carries
*gluconeogenesis* by IBA and Reactome TAS alongside IMP rows for *glucose
homeostasis* and *regulation of insulin secretion* (PMID:20668700), so the
inherited process term is the one expression argues against. G6PC3 is present
almost everywhere, including kidney cortex (score 96), so expression cannot
argue against its inherited term. The existing G6PC3 review keeps that row as
KEEP_AS_NON_CORE on phylogenetic grounds, and expression neither supports nor
contradicts that.

**PAX4 / PAX6 (PTHR45636, node PTN002900580).** In PANTHER 19 the PAX4/PAX6
split is a Mammalia-level duplication (PTN000676674), below the Euteleostomi
node that carries the IBDs for *retina development in camera-type eye*,
*forebrain development* and *type B pancreatic cell differentiation*. So PAX4
inherits all three.

- **Retina.** Human PAX6 is enriched in the only sampled retina, the pigmented
  layer (score 89, 93rd percentile of its own profile). Human PAX4 is absent
  there, a controlled but stage-merged absence. Mouse Pax4, though, has a
  present call in the eyeball (score 54, 56th percentile) where Pax6 is at the
  top of its profile.
- **β-cell term.** Concordant for both paralogs.

Expression shows quantitative divergence, with PAX6 top-ranked and PAX4
marginal. It does not show absence, so it supports questioning the node
placement but cannot settle it alone.

**Corpus scan.** 1,865 IBA groups (one PTN, one GO term) cover two or more
reviewed human genes. 86 of them name an anatomy, and 7 are discordant
([table](BGEEDB_EXPRESSION/results/paralog_discordant_groups.tsv)):

- **ACTL8, `axon`** (PTN007551913). ACTB is detected in neurons, while ACTL8,
  present in only 20 of 275 sampled entities, all germline, is strictly
  absent. The reviewer left the row UNDECIDED, and the paralog comparison
  argues for MARK_AS_OVER_ANNOTATED.
- **AGFG2, `acrosome assembly`** (PTN002919572). AGFG1 scores 98–100 in sperm and
  male germ cells, where AGFG2 is absent. Here the sister also controls for the
  quiescent-sperm caveat. The AGFG2 row is ACCEPTed and is worth a second look.
- **The remaining five groups** are bHLH and homeodomain developmental terms
  where adult data cannot decide (stage-merged absences). One, OLIG2 *sensory
  organ development*, was already REMOVEd by its reviewer.

### 4. Cerebellum development: is the module switched on in order?

![Cerebellum module genes by mouse developmental stage, coloured by whether each is expressed in its step's declared context, only in the wider cerebellar territory, or only elsewhere](BGEEDB_EXPRESSION/fig-cerebellum.svg)

*Figure 2. Mouse Bgee stage-resolved present calls for the OMA ortholog of each
module participant. Rows follow module steps. Dark = expressed in the step's
declared context at that stage; light = only in the wider cerebellar territory
(midbrain-hindbrain boundary, rhombomere 1, rhombic lip, metencephalon). The
step-by-stage verdicts come from the `module_logic` engine; full tables are in
[cerebellum_timing.md](BGEEDB_EXPRESSION/results/cerebellum_timing.md).*

A metabolic module is satisfiable all at once. A developmental module is a sequence, so
satisfiability is asked per stage, and the expectation is a staggered wave.
With the territory oracle, steps first become satisfiable in this order:

| step | first stage satisfiable |
|---|---|
| anlage allocation (GBX2, FGF8) | E8–E10.5 |
| germinal zones (ATOH1, PTF1A) | E10.5–E14 |
| Purkinje cells (RORA, RELN, SHH) | E10.5–E14 |
| GCP proliferation (SMO) | E14–birth |
| migration and Bergmann glia (FBXO41, DNER, PTPN11) | P0–P7 |
| foliation (EN1/EN2) | E8–E10.5 |

That gives 9 concordant, 4 discordant and 2 tied step pairs. Every discordance
comes from the foliation step.

What the wave says about the module:

- **Step 1's declared context cannot be met by its own genes.** It declares
  `cerebellum`, but GBX2 and FGF8 act at the midbrain-hindbrain boundary and in
  rhombomere 1 before a cerebellum exists. UBERON links the cerebellum only to
  the rhombic lip, through `develops_from`. Declaring the boundary or
  rhombomere 1 as the step's context would make the step testable.
- **EN1/EN2 are on from E8, five steps early.** They are placed only in the
  foliation step, but their expression starts with the isthmic genes. Whether
  Engrailed also belongs in the anlage step is a question for the module's
  curators. It is listed under suggested module questions below, not asserted.
- **The postnatal steps switch on on time.** FBXO41 and PTPN11 first appear in
  their declared context at P0–P7; DNER is already in the territory before birth.
- **Resolution is the limit.** With the strict oracle, where a call must lie in the layer or
  cell type the step names, nearly nothing is satisfiable. Bgee's stage-resolved
  calls for these genes are annotated to whole cerebellum or metencephalon,
  rarely to a layer.
- **Two Cell Ontology gaps block cell-type matching.**
  - *Cerebellar granule cell precursor* (CL:0002362) is `part_of` the upper
    rhombic lip only, not the external granule layer where it proliferates
    after birth.
  - *Cerebellar granule cell* (CL:0001031) has no location axiom.
- **No call is not no expression.** The API returns present calls only. SMO has 8
  calls at P0–P7 and 2 at P7–P21, so step 4's patchy postnatal row is
  a coverage gap, not biology.

### 5. Follow-up reviews: mouse G6pc2 and Pax4

The two strongest paralog leads were reviewed in full, in mouse, which has the
richest Bgee data for both genes. G6pc2 has 95 anatomical entities and 35
stages across in situ, Affymetrix, RNA-seq and single-cell data. Pax4 has 47
entities and 22 stages, including 34 in situ calls. Each review cites a
per-gene expression report (`scripts/gene_report.py`) that scores every
anatomy-bearing GO term for the gene and its sister paralogs:

- G6pc2: `genes/mouse/G6pc2/G6pc2-bioinformatics/RESULTS.md`
- Pax4: `genes/mouse/Pax4/Pax4-bioinformatics/RESULTS.md`

**mouse/G6pc2** (17 GOA rows plus 1 NEW: 12 ACCEPT, 3 MODIFY, 2 REMOVE,
1 NEW).

- **Core function.** Glucose-6-phosphatase activity in the ER of islet β
  and α cells is core. It opposes glucokinase and so sets two glucose
  thresholds. In β cells it shifts the glucose dose-response of insulin
  secretion, and *regulation of insulin secretion* is refined to the
  negative, glucose-stimulated child. In α cells it sets the glucose level
  that suppresses glucagon secretion: α-cell-specific deletion lowers
  glucagon output at low glucose (PMID:39742505). That adds a NEW
  *positive regulation of glucagon secretion* row.
- **Gluconeogenesis.** The IBA and the UniPathway IEA are removed as
  over-propagation from PTN000971890, whose seeds include no G6PC2.
  Deleting G6pc2 in β-cells alone accounts for the phenotype, and islets do
  not supply blood glucose.
- **How expression was used.** The paralog-controlled context check is
  quoted in the reason as supporting evidence only. In liver, kidney and
  intestine G6pc2 has 10 absent calls and only low present calls, while
  G6pc1 is present at scores near 98. The review notes that G6pc2's trace
  liver calls mean expression alone could not have carried the decision.

**mouse/Pax4** (50 rows: 21 ACCEPT,
18 MODIFY, 6 MARK_AS_OVER_ANNOTATED, 5 REMOVE). The core functions are
transcriptional repression, β-cell fate allocation by cross-repression with
Arx, and enteroendocrine fate in the gut.

- **The IBA eye and brain rows.**
  - *Brain development* and *forebrain development* are removed.
  - *Retina development* and *sensory organ development* are marked as
    over-annotated. A late role in photoreceptor maturation has never been
    tested, because null mice die early.
  - The evidence: no Pax4 ortholog has an eye or brain phenotype, and Pax4
    and Pax6 cannot substitute for each other. Synteny places Pax4 among
    the vertebrate Pax4/6/10 genes, which "are not implicated in the
    development of eyes" (PMID:24951566).
- **Expression did not decide those rows.** Mouse Pax4 is
  ENRICHED-tier for brain terms, from adult Affymetrix samples and one E13
  in situ timepoint, yet the review removed them. That is rules 1 and 2
  below: presence is not participation.
- **The IEP chain.** The rat retina paper (PMID:19012751) found Pax4 in
  photoreceptors, peaking in the adult, and says this "argues against a role
  in development". The same paper's expression-pattern (IEP) annotations
  still reach mouse Pax4 by two routes.
  - **Ensembl orthology projection.** *Retina development* and *circadian
    rhythm* come from PMID:19012751, and *response to cAMP* and *response to
    xenobiotic stimulus* from the pineal paper PMID:18818287.
  - **PAINT.** Rat Pax4 (RGD:620433) is one of the seeds of the retina IBD
    at PTN002900580.

  The circadian, cAMP and xenobiotic rows are removed: a transcript that
  oscillates or responds to a signal is an output of the pathway, not a
  participant in it. Here mouse Bgee supplies a controlled absence for a
  non-developmental term. Pax4 is absent from the pineal body (gold) where
  Pax6 is present.

**Double check on G6pc2.** Two further checks tested the gluconeogenesis
removal.

- **Targeted literature search.** The only direct measurement of glucose
  production bearing on G6PC2 is a nominal human association: higher basal
  hepatic glucose production in carriers of the fasting-glucose-raising
  allele (p = 0.04, elderly twins; PMID:19669124). The review now weighs it.
  No study measures glucose production in G6pc2-null mice, so that is a
  suggested experiment.
- **Blinded OpenScientist run.** It was given the neutral hypothesis but not
  the review's decision, its reasoning or the Bgee report, and it reached
  the same verdict from the literature alone. Its first proposed
  confirmatory test was an expression-atlas cross-check of G6PC2 against its
  paralogs, which is exactly what the held-out Bgee report contains. This is
  the calibration result: expression corroborated a conclusion the
  literature already supported, as rule 2 says it should.
- **The PTN-level twist.** Chicken liver studies report a hepatic G6PC2
  transcript. Bgee shows chicken G6PC1 is the liver and kidney paralog and
  chicken G6PC2 is low everywhere, but chicken islets are not sampled. The
  suggested PAINT loss was therefore narrowed from the whole G6PC2 clade to
  the mammalian G6PC2 node (PTN000287500).

Both reviews record source defects for the upstream resources and pose the
PAINT node questions as suggested questions.

**Human reviews.** Human G6PC2 and PAX4 were then reviewed, with the mouse
reviews as the consistency reference and per-gene human Bgee reports.

- **human/G6PC2** (13 GOA rows plus 1 NEW).
  - **Gluconeogenesis.** All three rows are removed, including a Reactome
    TAS row that mouse did not have. Reactome places its islet G6PC2
    reaction inside the Gluconeogenesis pathway, whose own summary says
    gluconeogenesis "is confined to cells of the liver and kidney"; this is
    recorded as a Reactome source defect.
  - **Insulin secretion.** The human variant study behind the IMP rows
    gives a direction: the fasting-glucose-raising allele lowers
    first-phase insulin secretion. The row is refined to the same negative,
    glucose-stimulated term as in mouse.
  - **Glucagon.** The α-cell glucagon row is added here too, on the human
    α-cell knockdown in the same paper.
  - **Expression.** Human Bgee gives weaker expression support than mouse:
    G6PC2 has only low present calls in the gluconeogenic tissues and no
    absent calls.
- **human/PAX4** (30 rows: 16 ACCEPT, 7 MODIFY, 3 MARK_AS_OVER_ANNOTATED,
  2 TOO_GENERAL, 2 REMOVE). Actions match mouse on every shared term.
  - The β-cell role is contributory rather than essential in human:
    knockout stem-cell lines still make β-like cells, and complete loss
    causes transient neonatal diabetes with "No extra pancreatic features"
    (PMID:40614820).
  - The human enteroendocrine rows rest on an organoid CRISPR screen.
  - MODY9 is recorded as contested and supports no term.

## Rules of use: when expression can count

These rules come from the calibration and are offered as working guidance for
reviewers. They are not repository policy.

1. **Never as sole evidence, never for a NEW process term.** Presence does not
   separate accepted from over-annotated rows (ratio 1.02).
2. **Presence corroborates; it does not establish.** An ENRICHED tier on an
   annotation that already has independent support is fair to mention in
   `reason`. A CONSISTENT tier adds nothing.
3. **Absence counts only with a control and after the screens.** Read it as
   evidence against an annotation only when all of these hold:
   - the term is not developmental, or the data are stage-matched;
   - the anatomy is not reached through `regulates`;
   - the product is not secreted or a ligand;
   - the target cell is not transcriptionally quiescent;
   - ideally, a sister paralog is detected in the same anatomy.
4. **Metabolic and physiological terms need a context source.** GO gives them no
   anatomy; use the module's context or the satisfiability engine's satisfiable
   tissues.
5. **Developmental modules need stage-resolved, cell-resolved data.** Organ-level
   in situ calls can show order but not which cell expresses the gene.
6. **Cite Bgee calls, not tiers.** Quote the entity, score and data type from
   `data/*.tsv` or the Bgee gene page, and keep the tier as reasoning in
   `reason`.

## Leads for curators

| kind | item | what expression shows | suggested action |
|---|---|---|---|
| IBA | ACTL8 `axon` (GO:0030424) | ACTB detected in neurons; ACTL8 germline-only and absent | reconsider the UNDECIDED row; candidate MARK_AS_OVER_ANNOTATED |
| IBA | AGFG2 `acrosome assembly` (GO:0001675) | AGFG1 at 98–100 in sperm and male germ cells; AGFG2 absent | re-check the ACCEPT against AGFG2-specific literature |
| IBA | G6PC2 `gluconeogenesis` (GO:0006094) | islet-dominant; 2/10 top tissues in the gluconeogenic context | **done (mouse and human):** IBA, IEA and the human Reactome TAS REMOVEd; IRD suggested at the mammalian G6PC2 node PTN000287500 |
| IBA / PAINT | PAX4 retina and forebrain terms from PTN002900580 | PAX6 enriched; PAX4 absent (human) or marginal (mouse) | **done (mouse and human):** brain and forebrain REMOVEd, retina and sensory organ MARK_AS_OVER_ANNOTATED; IRDs suggested on PTN000676639 and PTN009180007 |
| source (Reactome) | G6PC2 islet reaction R-HSA-3266566 inside Gluconeogenesis R-HSA-70263 | the pathway summary confines gluconeogenesis to liver and kidney | recorded as a Reactome source defect on human G6PC2 |
| module | `modules/gluconeogenesis_human.yaml` paralog-trap note | calls G6PC2 a "largely catalytically inactive autoantigen", contradicted by the G6PC2 enzymology and mutagenesis papers (PMID:14722102, PMID:38095063) | correct the parenthetical; the paralog-trap decision itself stands |
| review gap | MITF RPE, heart, skeletal muscle | top tissues unexplained by any retained anatomy term | check whether the review is missing functions |
| module | cerebellum step 1 context | GBX2/FGF8 expressed at the midbrain-hindbrain boundary and rhombomere 1, not in the declared `cerebellum` | change the step context |
| module | EN1/EN2 placement | expressed from E8, with the isthmic genes | suggested question for module curators |
| ontology (CL) | CL:0002362, CL:0001031 | GCP lacks an external-granule-layer location; granule cell has none | request axioms from CL |
| source (MGI) | mouse G6pc2 ER IDA citing PMID:10787428 | not expression: the cited paper is about NPC1 | recorded as a suspected wrong reference for MGI to check |
| source (RGD, Ensembl) | rat Pax4 IEP rows (PMID:19012751, PMID:18818287) | rhythmic or regulated transcript levels, not function | recorded as source defects; four rows reach mouse Pax4 by orthology, and one seeds the PAINT retina IBD |

The full machine-generated lists are
[corpus_leads.tsv](BGEEDB_EXPRESSION/results/corpus_leads.tsv) and
[paralog_discordant_groups.tsv](BGEEDB_EXPRESSION/results/paralog_discordant_groups.tsv).

## Limitations and next steps

- **Coverage.** Human Bgee samples about 330 entities, mostly adult tissues. Many
  developmental and cell-type anatomies are `NO_DATA` (24% of ACCEPT rows).
- **Ontology-mediated matching** is only as good as UBERON and CL partonomy. Co-location
  and container matches are deliberately weaker tiers and are labelled as such.
- **Circularity.** Reviewers may occasionally have used expression in their
  reasoning; the calibration cannot rule that out row by row.
- **Next steps:**
  - add Bgee's single-cell calls to the oracle, for cell-resolved
    developmental timing;
  - run the paralog design across PANTHER families with PAINT IBDs, not
    only reviewed human genes;
  - use module `context` as a second anatomy source;
  - promote the classifier into `src/` once the tiers stabilise;
  - offer the tiers to reviewers as an optional `review.reason` aid.

## Methods & reproduction

Scripts, data provenance and the commands that regenerate every number and
figure on this page: **[Methods & reproduction](BGEEDB_EXPRESSION/methods.md)**.
