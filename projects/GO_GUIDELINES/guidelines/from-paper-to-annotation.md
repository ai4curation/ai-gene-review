# From paper to annotation: GO annotation guidelines

Status: draft v0.1 (2026-11-15) · Part of [GO_GUIDELINES](../../GO_GUIDELINES.md)

**In brief:**

- Annotate what the experiment shows, not what the authors conclude or what the assay is called. A wound-healing assay measures cell motility.
- The readout sets the aspect. A measurement of the product's own activity can support a molecular function; a downstream phenotype supports at most a process, usually as non-core.
- A phenotype shows that a gene is necessary. Participation needs a mechanism: name which gene product performs the step before writing `involved_in`.
- Annotate the gene product and species that were actually assayed, cite the primary paper that contains the data, and check that the identifiers resolve to what you think they do.
- Read the negatives. A paper that reports no activity supports a NOT, and a negative control is not a positive result.
- One row per claim per method, each traceable to a figure or a quoted sentence. Less is more.

## Scope

This document covers the step from a paper's experiments to a set of GO
annotations: which assays support which aspect and how deep a term, overexpression
and heterologous systems, the right reference and the right organism,
phenotype-to-process traps, findings that should not be annotated, and how to
record one annotation per claim. It applies both to making new annotations and to
reviewing existing literature-based ones.

The choice of evidence code is in [evidence-codes.md](evidence-codes.md). Detailed
process rules (relations, regulation, causal distance) are in
[biological-process.md](biological-process.md) and
[regulation-and-signaling.md](regulation-and-signaling.md); location rules in
[cellular-component.md](cellular-component.md); NOT and other qualifiers in
[qualifiers-and-negation.md](qualifiers-and-negation.md); the review workflow in
[reviewing-annotations.md](reviewing-annotations.md).

## Principles

**GO describes the normal role of a gene product.** The
[Tips page](https://wiki.geneontology.org/index.php/Tips_to_Produce_High_Quality_Annotations)
(reviewed 2025) and the [phenotype guideline](https://wiki.geneontology.org/index.php/Annotating_from_phenotypes)
both start here. Experiments perturb, overexpress and relocate proteins; the
curator's job is to infer the unperturbed function from them, and to stop where
the inference stops.

**What a paper shows is narrower than what it claims.** Titles, abstracts and
discussions summarise and speculate. The annotation must rest on a result: a
figure, a table, a sentence in Results. Authors write "required for" and "plays a
role in"; GO's `involved_in` has a defined meaning that those phrases do not carry
([wiki: Annotating from phenotypes](https://wiki.geneontology.org/index.php/Annotating_from_phenotypes)).

**The distance from readout to product decides what a result licenses.** The
[ASSAY_TO_FUNCTION](../../ASSAY_TO_FUNCTION.md) project mined the papers behind
about 37,000 PMID-backed annotations: across thematically aligned annotations,
molecular readouts supported a molecular-function term 77% of the time (567/738)
and phenotypic hub readouts 8% (90/1,087), most of the latter being the legitimate
case of a reporter assay for a real transcription factor. Evidence codes do not
record this distance, so the curator must.

**A paper is evidence about the gene product it studied.** Papers on paralogs,
orthologs, complexes and pathways are routinely cited for the wrong member. The
[Wrong-Gene Leads](../../WRONG_GENE_LEADS.md) and
[Miscitation](../../MISCITATIONS.md) projects found that most such errors pass
every mechanical check.

## Rules

<a id="lit-1"></a>

### LIT-1. Annotate the conclusion the experiment supports, not the assay's name or the authors' framing.

Some assays share a name with a GO term but measure something else. The Tips page
lists them: a scratch "wound-healing assay" measures `GO:0048870` cell motility,
not `GO:0042060` wound healing; DNA fragmentation and caspase activation measure
whether apoptosis happened, not whether the gene product does
`GO:0006309` apoptotic DNA fragmentation. Likewise, "expressed during" or
"activated during" a stage is not involvement in the process that defines the
stage: a yeast spore-wall protein induced during meiosis is not involved in
meiotic division ([go-annotation#1005](https://github.com/geneontology/go-annotation/issues/1005)).

Some assay conditions test general properties of the protein rather than its
function. The Tips page's example: DNase II is less active when tunicamycin blocks
its glycosylation ([PMID:16500043](https://europepmc.org/article/MED/16500043)).
The figure supports `GO:0004531` deoxyribonuclease II activity and nothing about
regulation, because tunicamycin is not shown to bind DNase II and glycosylation is
not a known regulatory switch for it.

*How to apply.* For each candidate term, write the one-sentence result it rests
on, in your own words, without the term's label. If the sentence describes a
readout ("migration into the scratch was reduced"), annotate the process the
readout measures, or nothing.

Provenance: [GOC] [wiki: Tips](https://wiki.geneontology.org/index.php/Tips_to_Produce_High_Quality_Annotations).

<a id="lit-2"></a>

### LIT-2. Let the readout's proximity to the gene product set the aspect and the depth of the term.

Classify the readout before choosing the term
([ASSAY_TO_FUNCTION rubric](../../ASSAY_TO_FUNCTION/RUBRIC.md)):

- **Molecular readouts** measure the product's own activity: enzyme kinetics,
  in vitro kinase or ubiquitination assays, GTPase assays, electrophysiology of
  the pore-forming subunit, EMSA and ChIP for DNA binding, direct binding assays.
  They can support an MF term at the depth of what was measured.
- **Phenotypic hub readouts** report the state of a process that many inputs
  feed: ROS probes, caspase activity, viability and proliferation, autophagy
  flux, UPR reporters, calcium imaging, mitochondrial membrane potential,
  migration assays. A positive result after perturbing the gene supports at most
  a BP term ("regulation of P", "response to P") at the level the readout
  reports, defaults to non-core, and never supports a regulatory or process-like
  MF.

Two exceptions mark the boundaries. A luciferase reporter for a sequence-specific
DNA-binding transcription factor legitimately supports `GO:0003700` DNA-binding
transcription factor activity or its RNA polymerase II-specific children,
because the reporter reads that activity. The same reporter for a coregulator
that does not bind DNA does not support `GO:0003713` transcription coactivator
activity unless other evidence places the protein in the transcriptional
machinery (AIP was over-annotated this way; β-catenin and NICD were not). And a
binding or catalytic MF measured directly in the same paper is unaffected by the
paper also using hub readouts.

Promote a hub-derived process term to core only when independent evidence puts
the gene in the recognised machinery for that process: BCL2-family proteins for
apoptosis, ATG proteins for autophagy, IRE1/PERK/ATF6 for the UPR. PDGFB's
`GO:0072126` positive regulation of glomerular mesangial cell proliferation and
VEGFA's `GO:0043066` negative regulation of apoptotic process were moved to
non-core for this reason; VEGFA's endothelial proliferation, the ligand's
signature output, stayed core ([ASSAY_TO_FUNCTION/EDITS](../../ASSAY_TO_FUNCTION/EDITS.md)).

Provenance: [GOC+] — the GOC phenotype guideline warns against read-outs; the
proximity rule, its MF exclusion and the machinery test come from
[ASSAY_TO_FUNCTION](../../ASSAY_TO_FUNCTION.md).

<a id="lit-3"></a>

### LIT-3. An in vitro activity supports a molecular function only at the depth that was tested; decide whether the protein evolved to perform it.

An enzyme assay supports the reaction that was assayed, with the substrate that
was used. Do not climb to a narrower term (a specific substrate the paper did not
test) or jump to a pathway: an activity on a pathway intermediate supports the MF,
and a BP annotation to the pathway needs in vivo evidence or an IC that states the
step ([evidence-codes EV-12](evidence-codes.md#ev-12)).

Measured activity is not automatically function
([CLAUDE.md](../../../CLAUDE.md); [ENZYME_SPECIFICITY](../../ENZYME_SPECIFICITY.md)).
State the judgement in `reason`:

| Tier | Action | When |
|---|---|---|
| Genuine secondary activity | KEEP_AS_NON_CORE | respectable efficiency; plausible physiological substrate or in vivo phenotype; no other enzyme owns the reaction |
| Real in vitro activity, relevance unknown | MARK_AS_OVER_ANNOTATED | activity is real, nothing shows it is used |
| Promiscuous noise | REMOVE, even on IDA | a dedicated enzyme for the reaction exists in the organism; the activity is orders of magnitude lower; the protein lacks the specificity determinants |

*Examples.* ECOLI/yciO, `GO:0061710` L-threonylcarbamoyladenylate synthase
activity: REMOVE. TsaC is the essential dedicated enzyme, YciO's rate is about
10⁴-fold lower, and YciO lacks the KRSN tetrad. ECOLI/yjdM, `GO:0047400`
phosphonoacetate hydrolase activity: MARK_AS_OVER_ANNOTATED, because E. coli has
no dedicated enzyme to assign the reaction to. Fission yeast aga1 (ArgJ) carries
both `GO:0004358` (acetyl-L-ornithine donor) and `GO:0004042` (acetyl-CoA donor);
the acetyl-CoA activity was measured in an overexpression study at about 0.3% of
the ornithine-donor rate, and PomBase had not annotated it experimentally
([go-annotation#5845](https://github.com/geneontology/go-annotation/issues/5845)).
The review keeps the IBA and IEA rows for it as non-core.

Provenance: [GOC+]. GO documentation has no promiscuity rule; the tiers follow
de Crécy-Lagard et al. 2025 (PMID:40703034) as adopted in
[ENZYME_SPECIFICITY](../../ENZYME_SPECIFICITY.md).

<a id="lit-4"></a>

### LIT-4. Weigh localisation data by what was localised: endogenous protein in its native cell outranks a tagged, overexpressed construct.

A localisation result supports a CC term at the resolution of the assay. Rank the
evidence:

1. endogenous protein, specific antibody or knock-in tag, native cell type, with a
   compartment marker;
2. tagged protein at near-endogenous level, with a marker;
3. overexpressed tagged protein, with a marker;
4. overexpressed protein described by shape alone ("perinuclear", "resembling the
   Golgi");
5. a crude fraction not checked for contaminating compartments.

Levels 1-3 can support the organelle term. Level 4 supports nothing beyond the
cell. Level 5 is the subject of [ORGANELLES](../../ORGANELLES.md): a
"mitochondrial" fraction not checked for an ER marker cannot separate mitochondria
from mitochondria-associated ER membranes. A sub-compartment
(`GO:0005743` mitochondrial inner membrane, `GO:0005789` endoplasmic reticulum
membrane) needs an assay that resolves it or two independent lines that agree.

Overexpression creates specific artefacts. Saturated targeting machinery leaves
protein in the ER, and mutant or misfolded protein is retained there. A secreted or
plasma-membrane protein seen in the ER is in transit, not resident; its ER row is
non-core only with direct evidence on the endogenous protein, otherwise
over-annotated. In the ORGANELLES audit CABP2's Golgi row rested on overexpressed
CaBP2 "resembling the Golgi apparatus", while all marker work in the paper was on
CaBP7/8; CERKL's ER rows all came from overexpressed tagged constructs.

Being located somewhere does not mean acting there. Whether to use `located_in`
or `is_active_in` is a CC question ([cellular-component.md](cellular-component.md)).

Provenance: [GOC+] — the IDA page accepts overexpression as an assay system; the
ranking and the transit rule come from [ORGANELLES](../../ORGANELLES.md).

<a id="lit-5"></a>

### LIT-5. In overexpression and heterologous systems, separate the assay from the phenotype, and annotate the gene that was expressed.

Expression systems are legitimate vehicles. A protein expressed in COS cells,
insect cells or E. coli and assayed for its activity is a direct assay of that
protein. A phenotype caused by expressing it is something else: a gain-of-function
or dosage effect, which seldom reveals normal function
([wiki: IMP](https://wiki.geneontology.org/index.php/Inferred_from_Mutant_Phenotype_%28IMP%29);
[go-annotation#6468](https://github.com/geneontology/go-annotation/issues/6468)).
Three checks:

- **Is the readout the product's own activity or location?** Then annotate the
  MF or CC (IDA). If it is a cellular phenotype, annotate a process only by the
  rules for phenotypes ([LIT-8](#lit-8)), as IMP.
- **Does dose change the answer?** Fission yeast Epe1 at single copy removes
  ectopic heterochromatin only partly, while overexpressed Epe1 erases it
  completely ([PMID:31206516](https://europepmc.org/article/MED/31206516), cited
  in the Epe1 review). A result seen only on overexpression describes capacity,
  not normal function.
- **Whose gene is it?** The annotation goes to the expressed gene in its own
  species, not to the host. Mouse cDNA expressed in human HEK293 cells annotates
  the mouse gene. A human gene complementing a yeast mutant annotates the human
  gene by IGI, with the yeast gene in WITH/FROM
  ([evidence-codes EV-5](evidence-codes.md#ev-5)).

Provenance: [GOC] for the IDA/IMP boundary (#6468); [GOC+] for the dose check.

<a id="lit-6"></a>

### LIT-6. Annotate the gene product and organism actually assayed; a paper about a paralog, ortholog or partner is not evidence for your gene.

Before writing a row, confirm from the paper that the protein assayed is the one
being annotated: the species, the gene, and where relevant the isoform.

- **Orthologs.** A mouse experiment annotates the mouse gene. The human ortholog
  gets the function by ISO from that annotation, not by IDA citing the mouse paper.
  The TAS page makes the same point about reviews: authors often cite
  experiments in other organisms ([wiki: TAS](https://wiki.geneontology.org/index.php/Traceable_Author_Statement_%28TAS%29)).
  For ND review, a paper on an ortholog is not literature on the gene, however
  strong ([CLAUDE.md](../../../CLAUDE.md)).
- **Paralogs.** CSGALNACT1 carried ten rows from [PMID:11514575](https://europepmc.org/article/MED/11514575),
  which cloned the paralog CHSY1. PAPSS1 carried `skeletal system development`
  (TAS) from a paper whose abstract names the mutated gene as PAPSS2. Both are now
  recorded as `WRONG_GENE_PRODUCT` source defects
  ([WRONG_GENE_LEADS](../../WRONG_GENE_LEADS.md)).
- **Name collisions.** "AP-2" is both a transcription factor family and a
  clathrin adaptor complex, and an early AP-2α splice product was called "AP-2B";
  both collisions reached GOA as rows on TFAP2A and TFAP2B. "ARH1" and "BACH1" are
  similar traps ([MISCITATIONS](../../MISCITATIONS.md)).
- **Isoforms.** Record the isoform tested (`isoform:`), without assuming the
  function is isoform-specific ([ISOFORMS](../../ISOFORMS.md)).
- **Antibodies.** A cross-reacting antibody against another species' protein is
  not evidence of orthology or identity
  ([go-annotation#11](https://github.com/geneontology/go-annotation/issues/11)).

Multi-gene papers are legitimate: a calmodulin-mutation paper about CALM1 may
assay all three identical CALM proteins. The test is whether the gene was assayed,
not whether it is in the title.

Provenance: [GOC] for annotating the organism assayed; [GOC+] for the paralog and
collision checks.

<a id="lit-7"></a>

### LIT-7. Cite the primary paper that contains the evidence, and verify that the identifier resolves to it.

The reference is the paper whose results support the annotation. A review is the
right reference only for TAS, and TAS is the right code only when the primary
paper cannot be reached ([evidence-codes EV-10](evidence-codes.md#ev-10)). Recent
reviews are still worth reading for context: the Tips page asks curators to work
gene by gene or pathway by pathway, not paper by paper.

Primary evidence means results. A meeting report is not: UniProt cites
[PMID:37160800](https://europepmc.org/article/MED/37160800), an 18-author
peroxisome meeting report with no abstract, with ECO:0000269 (experimental
evidence) for PEX39's function, two years before the primary paper. A paper in a
predatory journal deserves the same scepticism (Tips page).

Then check the identifier:

- **Digit errors.** NLRP3 carried IDA rows citing PMID:1189953, a 1975 psychiatry
  paper; a digit was dropped. PMID:22572157 (a platelet-antibody chip) stands in
  for PMID:22752157 (VRK2 anchoring KSR1-MEK1 to the ER) on 31 MGI rows.
- **Batch errors.** PMID:19593445, a paper on BAD in prostate cancer, supports
  `GO:0071260` cellular response to mechanical stimulus (IEP) on 36 human genes it
  never mentions. One wrong identifier is rarely wrong once; check the gene's
  neighbours in the complex or family
  ([MISCITATIONS](../../MISCITATIONS.md)).
- **Partner errors.** For IPI rows, check the WITH/FROM partner against the paper
  ([evidence-codes EV-3](evidence-codes.md#ev-3)).

In this repository a `supporting_text` must be a verbatim substring of the cached
paper, and the reference title is checked against fetched metadata. These checks
catch a wrong PMID whose title no longer matches; they do not catch a right paper
used for a claim it does not make. That is what `reference_review.correctness:
MISCITED` records ([CLAUDE.md](../../../CLAUDE.md)).

Provenance: [GOC] for citing primary work; [GOC+] for the identifier checks.

<a id="lit-8"></a>

### LIT-8. A phenotype shows necessity; annotate the most proximal process and use the weakest relation the evidence allows.

A knockout that abolishes a process shows the gene is needed for it, and the gene
product could be a step in the process, an upstream regulator, a supplier of a
substrate, or the substrate itself. Before writing `involved_in`, name the gene
product that performs the step ([CLAUDE.md](../../../CLAUDE.md), "Do not add what
curators deliberately declined to add"). The GOC phenotype guideline gives the
traps and the defaults
([wiki: Annotating from phenotypes](https://wiki.geneontology.org/index.php/Annotating_from_phenotypes)):

- **Required for is not involved in.** `involved_in` asserts that the product's
  MF is part of the process. If that is not shown, use `acts_upstream_of_or_within`
  (or its positive or negative child) or do not annotate the process.
- **Work outward from the MF.** For a transcription factor, the most proximal
  process is regulation of transcription; next, the cell fate it specifies; the
  behaviour of the animal is a phenotype, not a GO process for the TF
  ([Drive: Case studies, annotating from mutant phenotypes](https://drive.google.com/open?id=17FQlI3iWhra_eIW0luhjtOOn4RD_RiSp4GTYJvG4jS0)).
- **High-level phenotypes.** For lifespan, behaviour, growth, cell death,
  proliferation, migration, development and protein localisation, the guideline
  "strongly encourage[s]" curators not to annotate unless the mechanism is known.
- **Pleiotropy.** Yeast spliceosome mutants have translation defects because most
  yeast introns are in ribosomal protein genes; their `GO:0006412` translation rows
  were removed once splicing was established. Splicing factors are needed for
  cell-cycle progression without being part of it. Inviable mutants are a warning
  sign.
- **Regulation needs a mechanism.** A "regulation of P" annotation should be backed
  by evidence that the product's MF regulates an MF in P.
- **Substrates are not participants.** Angiotensinogen is necessary for
  `GO:0002003` angiotensin maturation and carries no annotation to it in human,
  mouse or rat; the proteases that cut it do.

*Example (not to annotate).* CHCHD10 mutant alleles inhibit apoptosis by
preventing cytochrome c release ([PMID:26666268](https://europepmc.org/article/MED/26666268)).
The guideline allows at most a causally-upstream annotation to apoptotic process and
explicitly rejects `GO:0090200` positive regulation of release of cytochrome c from
mitochondria.

Details on relations, regulation and causal distance are in
[biological-process.md](biological-process.md) and
[regulation-and-signaling.md](regulation-and-signaling.md).

Provenance: [GOC] for the phenotype rules; [GOC+] for the performer test and the
substrate convention ([CLAUDE.md](../../../CLAUDE.md)).

<a id="lit-9"></a>

### LIT-9. Read what the paper reports as negative; never annotate a negative control or a failed assay as a positive.

Two seed cases in the [miscitation project](../../MISCITATIONS.md) are positive
annotations from negative results:

- **SULT1B1**, `GO:0006068` ethanol catabolic process (IDA), from
  [PMID:23207770](https://europepmc.org/article/MED/23207770). The abstract names
  four ethanol-sulfating enzymes among eleven tested; SULT1B1 is one of the eleven
  and not one of the four. The cache is abstract-only, so the review marks the row
  over-annotated rather than removing it ([LIT-13](#lit-13)).
- **PNPLA3**, `GO:0003841` 1-acylglycerol-3-phosphate O-acyltransferase activity
  (EXP), from [PMID:21878620](https://europepmc.org/article/MED/21878620), which
  found no transfer to lysophosphatidic acid with a positive control in place. The
  quote passes the verbatim check; the row asserts the reverse of the result. With a
  NOT qualifier the citation would be impeccable.

A clear negative from a direct assay supports a NOT annotation
([qualifiers-and-negation.md](qualifiers-and-negation.md)); record the error in an
existing positive row as a `MISSING_NEGATION` source defect
([source defects](../../../docs/source_defects.md)). When one paper finds an
activity and another does not (PMID:22560221 against PMID:21878620 for PNPLA3),
the claim is contested; grade the pair `DISPUTED` and keep both visible.

Provenance: [GOC+]. GO documentation does not address negative controls; the rule
comes from [MISCITATIONS](../../MISCITATIONS.md).

<a id="lit-10"></a>

### LIT-10. Know which findings are not annotatable, and leave them out.

The following do not support a GO annotation by themselves:

| Finding | Why not | Sources |
|---|---|---|
| Cloning, sequence, chromosomal location | no function shown | [wiki: ND](https://wiki.geneontology.org/index.php/No_biological_Data_available_%28ND%29_evidence_code) |
| Disease association, biomarker use, GWAS hit | no function shown | wiki: ND |
| Expression atlas, tissue distribution | expression is not function | [IEP](../../IEP.md) |
| Primary hits of a genome-wide screen | false-positive rate; validate first | [wiki: HMP](https://wiki.geneontology.org/index.php/Inferred_from_High_Throughput_Mutant_Phenotype_%28HMP%29) |
| Membership of a regulon or co-expression cluster | a property of the promoter | [IEP](../../IEP.md) |
| A protein found in a vesicle or body-fluid proteome | true but uninformative, usually non-core | [OMICS_EVIDENCE](../../OMICS_EVIDENCE.md) |
| Oligomeric state, stoichiometry | out of GO scope | [go-annotation#2521](https://github.com/geneontology/go-annotation/issues/2521) |
| Effect of a chemical that alters the cellular environment | not regulation of the protein | [wiki: Tips](https://wiki.geneontology.org/index.php/Tips_to_Produce_High_Quality_Annotations) |
| A PTM required for activity, absent a regulatory role | a property, not a function | wiki: Tips |
| Speculation in the discussion | not a result | [go-annotation#1381](https://github.com/geneontology/go-annotation/issues/1381) |
| Lipid profiles, metabolite levels or expression changes in a mutant | readouts, not the gene's role | [go-annotation#5160](https://github.com/geneontology/go-annotation/issues/5160) |
| A computational prediction in a paper | IC and experimental codes do not apply; use ISS family or nothing | [go-annotation#1626](https://github.com/geneontology/go-annotation/issues/1626) |
| A bare interaction with no functional consequence | `GO:0005515` is removed by policy | [evidence-codes EV-3](evidence-codes.md#ev-3) |

"Not annotatable in GO" does not mean worthless. Phenotypes, interactions and
expression data have their own resources, which is why GO can be selective. If a
gene has no annotatable data in an aspect, the honest record is ND, and the
absence may be a knowledge gap ([NO_DATA](../../NO_DATA.md)).

Provenance: [GOC] for most rows; [GOC+] for the readout and vesicle rows.

<a id="lit-11"></a>

### LIT-11. Make one annotation per claim per method, each traceable to a result; do not harvest every term a paper touches.

One row records one gene product, one term, one evidence code and one reference.
If two methods in a paper support the same term, make two rows; if a result
supports a term and its regulation, consider which is the claim and make only that
one. The Tips page asks curators to "favor quality over quantity" and capture the
core function; "response to" and protein-binding terms are named as uninformative
when better terms exist.

Two batch patterns inflate annotation sets without adding information:

- **Many terms, one gene.** rat/Gstt1 carries four `response to X` terms from four
  induction papers; one `GO:0009410` response to xenobiotic stimulus says more. A
  paper that tests one perturbation under five conditions has one finding.
- **One term, many genes.** PMID:21492153 put `GO:0030855` epithelial cell
  differentiation on every protein that changed in a Caco-2 proteome; GOA has
  references producing 72 to 291 annotations each this way ([IEP](../../IEP.md)).

In this repository, a row's support is a verbatim `supporting_text` with its
`reference_section_type` (RESULTS, a figure legend) where known. A quote from the
introduction or discussion supports TAS or NAS at most.

Provenance: [GOC] for one row per method; [GOC+] for the batch tests.

<a id="lit-12"></a>

### LIT-12. Judge a paper against the rest of the literature: contested, superseded and retracted findings need explicit handling.

The Tips page says GO "is not an archive of all findings published on a protein"
and asks curators to remove annotations based on invalidated hypotheses. That
requires reading beyond the paper in hand.

- **Contested.** When good papers disagree, keep both visible and say so. Epe1's
  two experimental H3K9 demethylase rows (`GO:0032454`) are UNDECIDED: no assay has
  detected the activity, but genetic data do not rule it out. Its four electronic
  demethylase and oxidoreductase rows are removed as pseudo-enzyme propagations
  ([CONTESTED_FUNCTION](../../CONTESTED_FUNCTION.md)).
- **Superseded.** When later work explains an earlier phenotype (yeast
  spliceosome and translation, [LIT-8](#lit-8)), the earlier process annotation
  goes. Record the later paper in `finding_review.superseded_by`.
- **Retracted.** A retraction is a fact about the source, not the biology. Flag the
  reference (`is_invalid: true`, `correctness: DISPUTED`), cite the notice, and ask
  what rests on it. If the retracted paper is the sole support, the row becomes
  UNDECIDED or a proposed REMOVE sent upstream; if other evidence supports it,
  keep it and say so. Do not remove every annotation on the gene
  ([RETRACTIONS](../../RETRACTIONS.md); worked example human/TNFRSF21).

Provenance: [GOC] for representing current knowledge; [GOC+] for the retraction
procedure.

<a id="lit-13"></a>

### LIT-13. When reviewing someone else's literature annotation, read what they read before overruling it; an abstract can confirm, but only the full text can refute.

The curator who made an experimental annotation read the full text. Many cached
papers in this repository are abstract-only, and a title that foregrounds a
paralog often hides an assay of the gene being annotated. So:

- Do not REMOVE an experimental row, or call it a wrong-gene attribution, because
  the cached title or abstract is about something else. Use UNDECIDED if you cannot
  verify it, or ACCEPT if the function is independently established
  ([CLAUDE.md](../../../CLAUDE.md), "Do not overrule curators from incomplete
  evidence").
- Reserve a confident "this paper is about X" for cases where the abstract says
  so. FLNC, SOCS3 and NLRP3 leads whose abstracts never named the gene stayed as
  queries; PAPSS1, whose abstract named PAPSS2, was confirmed
  ([WRONG_GENE_LEADS](../../WRONG_GENE_LEADS.md)).
- An abstract is usually enough to confirm. In a blinded pilot the abstract alone
  supported ACCEPT for 18 of 21 annotations, while REMOVE support in the corpus is
  93% primary research ([EVIDENCE_SOURCE_SUFFICIENCY](../../EVIDENCE_SOURCE_SUFFICIENCY.md)).
  Read the full text before REMOVE or MODIFY.
- Automated flags are leads. A function-requirement rule ("a protein that enables
  T has one of these domains") or a wrong-gene score never by itself justifies
  changing an annotation ([FUNCTION_REQUIREMENT_RULES](../../FUNCTION_REQUIREMENT_RULES.md)).

Provenance: [NEW], from the repository's review experience.

<a id="lit-14"></a>

### LIT-14. Record provenance so the next reader can check the inference without rereading the paper.

For each annotation made or reviewed, record: the reference; the figure, table or
section; a verbatim quote of the result; the gene product and species assayed;
and, for inferential codes, the WITH/FROM. For each reference, record whether it
was checked (`reference_review.correctness`) and its relevance. Errors that live in
a source database go in `source_defects` with the responsible resource, so they can
be reported upstream; errors in this repository's own review are fixed in place
([reference curation](../../../docs/reference_curation.md);
[source defects](../../../docs/source_defects.md)).

AI-assisted extraction follows the same rule: the GOC accepts an association
suggested by an AI tool once a trained curator has confirmed it against the
experimental data, and it then takes the experimental code (Tips page, 2025). The
verbatim quote is how this repository shows that confirmation happened.

Provenance: [GOC] for AI-assisted associations; [GOC+] for the provenance fields.

## Decision aid

**What an assay can support.**

| Assay | Aspect | Typical code | How deep | Watch for |
|---|---|---|---|---|
| Purified-protein enzyme assay | MF | IDA | the reaction and substrate tested | promiscuity tiers (LIT-3) |
| Active-site point mutant, purified protein | MF | IDA (also IMP) | as above | folding defect |
| Knockout lysate loses activity | MF only with corroboration | IMP | — | necessity, not possession |
| EMSA, ChIP, DNA footprinting | MF (DNA binding) | IDA or IPI by ECO class | sequence-specific binding | ChIP partner has no identifier |
| Reporter assay, sequence-specific TF | MF (TF activity), BP | IDA | Pol II-specific child if shown | coregulators without DNA binding |
| Co-IP, two-hybrid, pull-down | MF (specific binding) | IPI | the partner class | WITH/FROM partner; contaminants |
| Tagged-subunit complex purification | CC (complex) | IDA | the named complex | substoichiometric contaminants |
| Immunofluorescence, endogenous, with marker | CC | IDA | organelle; sub-compartment if resolved | — |
| Overexpressed tagged protein | CC | IDA | organelle at most | ER retention, saturation |
| Fractionation | CC | IDA / HDA | fraction purity decides | MAM contamination; `membrane` |
| Knockout or knockdown phenotype | BP | IMP | most proximal process; `acts_upstream_of_or_within` if MF unknown | high-level phenotypes, pleiotropy |
| Double mutant, suppression, complementation | BP | IGI | as above | which gene is annotated |
| Hub readout (ROS, caspase, viability, ΔΨm) | BP | IMP | the level the readout reports | non-core by default; never MF |
| Induced expression under a stimulus | BP | IEP | parent stimulus term | agency test |
| Genome-wide screen | BP / CC | HMP / HDA | validated hits only | primary screen |

**Is this result annotatable?**

```
Is there a result (figure, table, Results sentence), not speculation?
├─ No  → do not annotate (or NAS only for a clear uncited assertion)
└─ Yes → Was THIS gene product, in THIS species, assayed?
         ├─ No  → annotate the gene that was assayed; yours gets ISO/ISS later
         └─ Yes → Is the readout the product's own activity/location?
                  ├─ Yes → MF/CC at the depth tested (LIT-2, LIT-3, LIT-4)
                  └─ No (phenotype) → Is the product's MF part of the process?
                           ├─ Yes → involved_in the most proximal process
                           ├─ Unknown → acts_upstream_of_or_within, or nothing
                           └─ It is a substrate/regulator elsewhere → not this term
```

## Common errors

| Error | Example | Fix |
|---|---|---|
| Assay name used as term | wound-healing assay → `GO:0042060` wound healing | `GO:0048870` cell motility, or nothing |
| Hub readout drives a core process | VEGFA anti-apoptosis from survival signalling | KEEP_AS_NON_CORE |
| Reporter drives coactivator MF for a non-DNA-binding protein | AIP → transcription coactivator activity | MARK_AS_OVER_ANNOTATED |
| Weak in vitro activity accepted as function | ECOLI/yciO TC-AMP synthase | REMOVE (promiscuous noise tier) |
| Overexpressed construct read as residence | CABP2 Golgi, CERKL ER | stay at the root or MARK_AS_OVER_ANNOTATED |
| Paralog's paper on the gene | CSGALNACT1 from a CHSY1 paper | `WRONG_GENE_PRODUCT` source defect |
| Name collision | TFAP2A IPI from a clathrin AP-2 paper | MISCITED; REMOVE the row |
| Wrong PMID | NLRP3 PMID:1189953 | `WRONG_IDENTIFIER` with a verified replacement if found |
| Negative control annotated positive | SULT1B1 ethanol catabolism | MARK_AS_OVER_ANNOTATED (abstract-only) or REMOVE |
| Negative result annotated positive | PNPLA3 LPAAT | `MISSING_NEGATION` source defect |
| Pleiotropic phenotype read as process | spliceosome mutants → translation | REMOVE once mechanism is known |
| Substrate given the processing term | angiotensinogen → angiotensin maturation (proposed NEW) | do not add |
| Meeting report as experimental evidence | PEX39 UniProt FUNCTION | cite the primary paper |
| Experimental row removed from an abstract | any abstract-only paralog-titled paper | UNDECIDED |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [wiki: Tips](https://wiki.geneontology.org/index.php/Tips_to_Produce_High_Quality_Annotations) | Select terms that reflect the core function; avoid maximising terms | Make sound non-core rows when the evidence supports them and mark them non-core; do not create uninformative ones | Non-core is a review judgement recorded on the row; deleting true peripheral facts loses information |
| [wiki: Annotating from phenotypes](https://wiki.geneontology.org/index.php/Annotating_from_phenotypes) | For high-level phenotypes, "strongly encourage" not annotating; elsewhere, `acts_upstream_of_or_within` is acceptable when little else is known | Default to not annotating high-level phenotypes; use `acts_upstream_of_or_within` only for the most proximal process the phenotype reports, and only when the gene has no better annotation | The page gives both answers; we pick one |
| [wiki: IDA](https://wiki.geneontology.org/index.php/Inferred_from_Direct_Assay_%28IDA%29) (pre-2026) | Overexpression is IDA when "considered an assay system", without separating MF from BP | Activity or location in an expression system is IDA; a phenotype from it is IMP and judged as a phenotype | Resolved in #6468 after MGI used IDA for CREG1 process rows |
| wiki: IDA | Overexpressed localisation is acceptable IDA | Rank localisation evidence; overexpressed protein supports the root organelle at most; transit is not residence | ER retention and saturation artefacts ([ORGANELLES](../../ORGANELLES.md)) |
| [wiki: IMP](https://wiki.geneontology.org/index.php/Inferred_from_Mutant_Phenotype_%28IMP%29) | Inhibitor effects are IMP (baicalein, 12-LOX, proliferation) | Inhibitor effects are IMP for the target only if the drug is specific; a hub readout gives at most a non-core upstream row | The example uses a convergent readout and a promiscuous drug |
| [wiki: IEP](https://wiki.geneontology.org/index.php/Inferred_from_Expression_Pattern_%28IEP%29) | Selective expression at a stage may support "xxx development" | Not unless the product is the differentiated output | Metabolic demand tracks maturation ([IEP](../../IEP.md)) |
| [Guidelines from annotation camp](https://wiki.geneontology.org/index.php/Guidelines_from_Annotation_Camp) | Request "X involved in Y" terms for downstream processes | Annotate X; record Y in GO-CAM, a module or core functions | Current practice decomposes precomposed terms ([INVOLVED_IN_PRECOMPOSITION](../../INVOLVED_IN_PRECOMPOSITION.md)) |
| Annotation camp | For poorly characterised genes, annotate downstream processes and remove them later | Prefer ND or `acts_upstream_of_or_within` to the most proximal process; do not create rows expected to be removed | Downstream rows propagate by IBA and ISO before anyone removes them |
| GO documentation (none) | No rule for negative controls or reported negatives | A negative result supports NOT; a positive row from it is a `MISSING_NEGATION` defect | SULT1B1, PNPLA3 |
| GO documentation (none) | No rule on promiscuous activity | Three tiers: non-core, over-annotated, REMOVE even on IDA | [ENZYME_SPECIFICITY](../../ENZYME_SPECIFICITY.md); #5845 |
| [wiki: NAS](https://wiki.geneontology.org/index.php/Non-traceable_Author_Statement_%28NAS%29) | Annotate an author statement the curator wants to capture | Discussion-section speculation is not annotatable | #1381 |
| GO documentation (none) | No guidance on reviewing others' literature annotations | Abstract can confirm; refute only from full text; flags are leads | [CLAUDE.md](../../../CLAUDE.md); [EVIDENCE_SOURCE_SUFFICIENCY](../../EVIDENCE_SOURCE_SUFFICIENCY.md) |
| [CLAUDE.md](../../../CLAUDE.md) substrate convention vs GO practice | GO annotates thyroglobulin, fibrinogen and C3 to the processes acting on them | A substrate gets the process term only if it does part of the work (scaffold, cofactor, chemistry) | The exceptions define the line; necessity alone never does |

## Open questions

1. Should the GOC adopt an explicit localisation-evidence ranking (LIT-4), and should
   overexpressed localisation require a compartment marker to support IDA at all?
2. Should "required for" phenotypes on high-level processes be disallowed outright
   for genes with no known MF, rather than discouraged?
3. Is a promiscuity threshold needed in GO documentation, or is a stated judgement
   (no number) enough? The repository has chosen the latter.
4. How should a reviewer record a suspected wrong-gene attribution when the full
   text is unavailable and the curator cannot be reached? `SUSPECTED` source defects
   exist, but nothing routes them to the source.
5. Should GOC require a figure or section reference on literature annotations, as
   this repository does with `supporting_text`?

## Sources

**GO wiki:**
[Tips to produce high quality annotations](https://wiki.geneontology.org/index.php/Tips_to_Produce_High_Quality_Annotations) (reviewed 2025-11) ·
[Annotating from phenotypes](https://wiki.geneontology.org/index.php/Annotating_from_phenotypes) (reviewed 2018) ·
[Guidelines from annotation camp](https://wiki.geneontology.org/index.php/Guidelines_from_Annotation_Camp) (historical, partly superseded) ·
[IDA](https://wiki.geneontology.org/index.php/Inferred_from_Direct_Assay_%28IDA%29) ·
[IMP](https://wiki.geneontology.org/index.php/Inferred_from_Mutant_Phenotype_%28IMP%29) ·
[IEP](https://wiki.geneontology.org/index.php/Inferred_from_Expression_Pattern_%28IEP%29) ·
[TAS](https://wiki.geneontology.org/index.php/Traceable_Author_Statement_%28TAS%29) ·
[NAS](https://wiki.geneontology.org/index.php/Non-traceable_Author_Statement_%28NAS%29) ·
[ND](https://wiki.geneontology.org/index.php/No_biological_Data_available_%28ND%29_evidence_code) ·
[HMP](https://wiki.geneontology.org/index.php/Inferred_from_High_Throughput_Mutant_Phenotype_%28HMP%29)

**Drive:**
[Case studies: annotating from mutant phenotypes](https://drive.google.com/open?id=17FQlI3iWhra_eIW0luhjtOOn4RD_RiSp4GTYJvG4jS0) (draft discussion document)

**go-annotation issues:**
[#11](https://github.com/geneontology/go-annotation/issues/11) ·
[#1005](https://github.com/geneontology/go-annotation/issues/1005) "activated during" is not "involved in" ·
[#1381](https://github.com/geneontology/go-annotation/issues/1381) NAS from speculation ·
[#1626](https://github.com/geneontology/go-annotation/issues/1626) predictions are not IC ·
[#2521](https://github.com/geneontology/go-annotation/issues/2521) oligomerisation out of scope ·
[#5160](https://github.com/geneontology/go-annotation/issues/5160) readouts are not roles ·
[#5845](https://github.com/geneontology/go-annotation/issues/5845) secondary activity from overexpression ·
[#6468](https://github.com/geneontology/go-annotation/issues/6468) IDA vs IMP for overexpression

**Papers:**
[PMID:27812934](https://europepmc.org/article/MED/27812934) best practices in manual annotation ·
[PMID:18460184](https://europepmc.org/article/MED/18460184) what GO annotations mean ·
[PMID:16500043](https://europepmc.org/article/MED/16500043) DNase II glycosylation (Tips example) ·
[PMID:26666268](https://europepmc.org/article/MED/26666268) CHCHD10 (phenotype example) ·
[PMID:23207770](https://europepmc.org/article/MED/23207770) ethanol sulfation by SULTs ·
[PMID:21878620](https://europepmc.org/article/MED/21878620) PNPLA3 enzymology ·
[PMID:11514575](https://europepmc.org/article/MED/11514575) chondroitin synthase cloning ·
[PMID:37160800](https://europepmc.org/article/MED/37160800) peroxisome meeting report ·
[PMID:31206516](https://europepmc.org/article/MED/31206516) Epe1 dosage and JmjC

**Repository:**
[CLAUDE.md](../../../CLAUDE.md) ·
[ASSAY_TO_FUNCTION](../../ASSAY_TO_FUNCTION.md) and its [rubric](../../ASSAY_TO_FUNCTION/RUBRIC.md) and [edits](../../ASSAY_TO_FUNCTION/EDITS.md) ·
[FUNCTION_REQUIREMENT_RULES](../../FUNCTION_REQUIREMENT_RULES.md) ·
[MISCITATIONS](../../MISCITATIONS.md) ·
[WRONG_GENE_LEADS](../../WRONG_GENE_LEADS.md) ·
[RETRACTIONS](../../RETRACTIONS.md) ·
[CONTESTED_FUNCTION](../../CONTESTED_FUNCTION.md) ·
[ENZYME_SPECIFICITY](../../ENZYME_SPECIFICITY.md) ·
[ORGANELLES](../../ORGANELLES.md) ·
[IEP](../../IEP.md) ·
[OMICS_EVIDENCE](../../OMICS_EVIDENCE.md) ·
[NO_DATA](../../NO_DATA.md) ·
[EVIDENCE_SOURCE_SUFFICIENCY](../../EVIDENCE_SOURCE_SUFFICIENCY.md) ·
[INVOLVED_IN_PRECOMPOSITION](../../INVOLVED_IN_PRECOMPOSITION.md) ·
[reference curation](../../../docs/reference_curation.md) ·
[source defects](../../../docs/source_defects.md) ·
[ISOFORMS](../../ISOFORMS.md)
