# Biological process: GO annotation guidelines

Status: draft v0.1 (2026-11-15) · Part of [GO_GUIDELINES](../../GO_GUIDELINES.md)

**In brief:**

- `involved_in` says the gene product's own activity is a step of the process. Before using it, name the step the product performs. If the honest answer is "it is needed for the process" or "it is what the process acts on", the relation is wrong, the term is wrong, or both.
- A knockout phenotype shows necessity, not participation. With no known mechanism, use `acts upstream of or within`, choose its positive or negative child, and use the most proximal process the data support. Leaving the row unannotated is also acceptable.
- Annotate the process nearest the activity, not the assay readout and not the organism-level outcome. Behaviour, development, lifespan, growth, proliferation and cell death need a mechanism before they become GO terms.
- Do not request, add or split precomposed "X involved in Y" terms. Annotate X, and record where Y went: a model, a core function, or nowhere.
- Before adding a process term because "every other participant has it", run the comparator check. A systematic absence across species is usually a convention.
- In review, a real but distal process is `KEEP_AS_NON_CORE`. `REMOVE` is for claims that are contradicted, not for claims that are merely far from the core.

## Scope

This document covers annotation of gene products to Biological Process (BP) terms with the BP gene-product-to-term relations (`involved in`, `acts upstream of or within` and `acts upstream of`, with their positive- and negative-effect children). It covers choosing between participation and upstream effect, interpreting phenotypes, developmental and organism-level processes, cell death, precomposed terms, pathway versus step terms, term depth, and the core versus non-core call made in reviews.

Out of scope, with pointers:

- Regulation terms, signalling pathways and "response to" terms: [regulation-and-signaling.md](regulation-and-signaling.md). The boundary between "part of X" and "regulation of X" is drawn there (RS-1 to RS-5).
- Transcription and its regulation: [transcription-regulation.md](transcription-regulation.md).
- Evidence-code mechanics (IMP versus IGI versus HMP, IEP): [evidence-codes.md](evidence-codes.md).
- Annotation extension syntax (`occurs_in`, `has_input`): [annotation-extensions.md](annotation-extensions.md).
- IBA and other propagation of BP terms: [phylogenetic-propagation.md](phylogenetic-propagation.md).
- NOT annotations: [qualifiers-and-negation.md](qualifiers-and-negation.md).

## Principles

**A BP annotation is a claim about normal biology.** It says that, in the wild-type organism, an activity of this gene product contributes to the process. Mutant, overexpression and drug experiments are evidence for that claim. They are not the claim. GO is not a phenotype database, and most contributing groups curate phenotypes separately ([wiki: Annotating from phenotypes](https://wiki.geneontology.org/index.php/Annotating_from_phenotypes)).

**A process is an ordered assembly of molecular functions.** RO and GO define `involved_in` as: the gene product enables some function that is `part_of` the process ([wiki: Annotating from phenotypes](https://wiki.geneontology.org/index.php/Annotating_from_phenotypes); [wiki: Annotation Relations](https://wiki.geneontology.org/index.php/Annotation_Relations)). Every `involved_in` row should therefore be explainable by an MF, known or unknown, that is a step of the process. A row that cannot be explained this way is an upstream claim and needs an upstream relation.

**The relation carries directness; the term carries the process.** Do not use one to repair the other. A distal phenotype is not fixed by moving to a vaguer term while keeping `involved_in`. It is fixed by choosing the proximal process, the upstream relation, or both.

**Necessity is not participation.** Substrates, precursors, cofactor suppliers, assembly factors and housekeeping machinery are all necessary for many processes. Being necessary is exactly what a substrate is. A perturbation experiment, however clean, cannot tell a participant from a substrate. Only a model of which entity performs which step can ([CLAUDE.md](../../../CLAUDE.md), "Do not add what curators deliberately declined to add").

**Annotations are for users who ask "which genes do X?"** An annotation that puts a ribosomal protein in apoptosis or a tubulin in locomotory behaviour makes that query less accurate. That cost is why the bar for organism-level terms is high.

## Rules

<a id="bp-1"></a>

### BP-1. Use `involved in` only when the gene product's activity is a step of the process

**Statement.** Annotate `involved_in` P only if you can name the activity of the gene product that is part of P. That activity may be catalysis, binding that performs a step, a structural or scaffolding contribution the step depends on, or transport. If you cannot name it, use an upstream relation (BP-4) or do not annotate.

**Rationale.** The relation means "enables some f, and f is part_of P" ([wiki: Annotation Relations](https://wiki.geneontology.org/index.php/Annotation_Relations); [Drive: Annotation relations – Guidelines for P2GO](https://drive.google.com/open?id=1DXdjAuNf7u8CKXYlgW5kyzPgq7vnp-Aai0S5Sh63guc)). The wiki asks curators to "think of the Molecular Functions that make up that process" and check whether the gene product enables one ([wiki: Annotating from phenotypes](https://wiki.geneontology.org/index.php/Annotating_from_phenotypes)). We make that test mandatory and operational: write the step down, at least in the review reason or the curator's notes.

**Worked examples.**

- Human MAP2K1 enables GO:0004708 MAP kinase kinase activity and phosphorylates ERK1/2. That activity is a step of GO:0000165 MAPK cascade, so `involved_in` GO:0000165 is correct.
- Yeast Brr6 is an essential nuclear envelope membrane protein whose mutants show nucleocytoplasmic transport defects. The later paper attributes the defect to lipid homeostasis at the NE-ER membrane and NPC assembly. Brr6 performs no transport step, so it is not `involved_in` GO:0006913 nucleocytoplasmic transport. The GOC case study discusses `acts upstream of or within` GO:0006998 nuclear envelope organization or GO:0055088 lipid homeostasis instead ([Drive: Case studies annotating from mutant phenotypes](https://drive.google.com/open?id=17FQlI3iWhra_eIW0luhjtOOn4RD_RiSp4GTYJvG4jS0)). The same lesson appears in [go-annotation#2456](https://github.com/geneontology/go-annotation/issues/2456): nuclear retention caused by a processing defect does not make the processing factor a transport factor.

**Provenance.** [GOC+]. GOC defines the relation. The requirement to name the step is our sharpening.

<a id="bp-2"></a>

### BP-2. Name the entity that performs the step; substrates and products are not participants unless they do some of the work

**Statement.** Before annotating, or accepting, a process term on a substrate, precursor, product or other consumed entity, ask which gene product performs the step. If the answer is a different gene product, the term belongs to that one. The exceptions are substrates that contribute to the process themselves: by supplying a scaffold, acting as a cofactor, or carrying out the chemistry.

**Rationale.** In process terms under GO:0006508 proteolysis and similar transformation processes, the participant is the agent of the transformation. GO's annotation corpus follows this convention almost everywhere, even though no wiki page states it. [go-annotation#211](https://github.com/geneontology/go-annotation/issues/211) states it for a transport case: process terms go to the gene products that facilitate the process, not to the cargo. [go-annotation#2425](https://github.com/geneontology/go-annotation/issues/2425) notes that GAF generation from GO-CAM pushed target molecules into process annotations, and proposes removing them.

**Worked examples.**

- **Not a participant.** Human AGT (angiotensinogen) is not annotated to GO:0002003 angiotensin maturation. GO:0002003 `is_a` GO:0016486 peptide hormone processing (verified), and it is annotated to the proteases that cleave angiotensinogen: REN, ACE, ACE2 and others. The comparator check (BP-3) confirms the convention. INS is absent from GO:0030070 insulin processing, POMC is absent from GO:0016486, and APP is absent from GO:0034205 amyloid-beta formation ([CLAUDE.md](../../../CLAUDE.md); review `genes/human/AGT`).
- **Participants by exception.** Thyroglobulin carries GO:0006590 thyroid hormone generation because it supplies the tyrosyl residues and positions the coupling pair: the scaffold case. Fibrin(ogen) carries GO:0042730 fibrinolysis because fibrin is the template that accelerates tPA-mediated plasminogen activation: the cofactor case. C3 carries GO:0006956 complement activation because its own thioester forms the covalent bond to the target: the chemistry case. Autoprocessing is the limiting case, where the substrate is the enzyme (GO:0016540 protein autoprocessing).
- **Necessity data.** High-throughput fungal growth screens show many mutants failing on alternative carbon or nitrogen sources. Respiratory assembly factors fail on glycerol because they are needed for respiration, not because they act on glycerol. Such data may corroborate an existing pathway annotation, or flag one for a second look. They must not create one ([FUNGAL_PHENOTYPES](../../FUNGAL_PHENOTYPES.md)).

**Provenance.** [GOC+]. The convention is GOC practice, and #211 states it for transport. The general test and the three-way exception (scaffold, cofactor, chemistry) are ours, from [CLAUDE.md](../../../CLAUDE.md).

<a id="bp-3"></a>

### BP-3. Run the comparator check before treating an absence as a gap

**Statement.** Before proposing a `NEW` process annotation because related genes carry the term and this one does not, name two or three gene products that stand in the same role (other substrates, other ligands, other assembly factors) for the same kind of process. Check whether they carry the term. A systematic absence across genes, species and MODs is a convention to identify, not an oversight to correct.

**Rationale.** "Every other participant has this term" usually means the term describes something this gene does not do. The check turns an assumption into a prediction that one QuickGO query can falsify. Also check production GO-CAMs (in this repository `gocams/index.tsv`): a curator who modelled the pathway, included the gene, and gave it a different role made a decision. If you disagree, argue with it explicitly.

**Worked example.** The renin–angiotensin GO-CAM (`gocams/6246724f00000549/`) contains AGT twice, once as the hormone-activity node and once as the proteases' input. Both roles are represented without placing AGT in GO:0002003 ([CLAUDE.md](../../../CLAUDE.md)).

**Provenance.** [NEW].

<a id="bp-4"></a>

### BP-4. When the mechanism is unknown, use `acts upstream of or within`, choose a sign, and choose the most proximal process

**Statement.** If the evidence shows that the gene product affects a process but not how its activity relates to that process, annotate with `acts upstream of or within`. Use the positive- or negative-effect child whenever the direction is known, which it almost always is from a perturbation. Choose the most proximal process the data support, not the furthest readout. Making no annotation is acceptable when the only available term is organism-level (BP-7).

**Rationale.** The relation was introduced at the 2017 Cambridge GOC meeting for this case ([go-annotation#1517](https://github.com/geneontology/go-annotation/issues/1517)). Both the wiki and the P2GO relation table tell curators to pick the signed child ([wiki: Annotation Relations](https://wiki.geneontology.org/index.php/Annotation_Relations); [Drive: Annotation relations – Guidelines for P2GO](https://drive.google.com/open?id=1DXdjAuNf7u8CKXYlgW5kyzPgq7vnp-Aai0S5Sh63guc)). It is also the default BP relation: GORULE:0000061 assigns it when none is asserted ([wiki: Annotation Relations](https://wiki.geneontology.org/index.php/Annotation_Relations)). The 2017 Corvallis presentation argued that legacy BP annotations, made before relations existed, mean only "most likely upstream of, and possibly a participant in" ([Drive: Regulation and causality & use of qualifiers in legacy annotations](https://drive.google.com/open?id=1fmgRMOPel-8_7iIuMAkVDNGuxurUWTxJRdsZTgSeNRM)).

**Worked examples.**

- Human CHCHD10: mutant alleles inhibit apoptosis by preventing cytochrome c release. The wiki says the only valid annotation is `acts upstream of or within` GO:0006915 apoptotic process (here the negative-effect child), and explicitly not GO:0090200 positive regulation of release of cytochrome c from mitochondria ([wiki: Annotating from phenotypes](https://wiki.geneontology.org/index.php/Annotating_from_phenotypes)).
- *Dictyostelium* AbcA knockouts have sorocarp defects. The curator who proposed the relation gave this as the model case, `acts upstream of or within` sorocarp morphogenesis ([go-annotation#1517](https://github.com/geneontology/go-annotation/issues/1517)).

**In review.** An `involved_in` row supported only by a phenotype, with no mechanism, has the wrong relation. That does not make it a false claim. Correct the relation as structured data, following [QN-7](qualifiers-and-negation.md#qn-7): mark the row `MODIFY`, say in `reason` that only the relation changes, and add a `NEW` row with the same term and `qualifier: acts_upstream_of_or_within` (with its sign where known). When a more proximal term exists, the `MODIFY` proposes it instead. Where the source should change its export, also record a source defect (`defect_type: WRONG_QUALIFIER`, see [docs/source_defects.md](../../../docs/source_defects.md)). If the process is real but peripheral, the corrected row is non-core. Do not `REMOVE` a true claim because its relation was too strong.

**Provenance.** [GOC]. The review handling is [GOC+].

<a id="bp-5"></a>

### BP-5. Use `acts upstream of` (without "or within") only when the mechanism is known and the activity is outside the process and does not regulate it

**Statement.** `acts upstream of` and its signed children mean three things: the mechanism linking the activity to the process is known; the activity occurs before the process; and the activity is neither part of the process nor a regulator of it. Use them rarely. When the upstream process has its own GO term, annotate that term with `involved_in`. Use `acts upstream of` only when downstream users would lose real information without it.

**Rationale.** Definitions are from the P2GO table and the wiki ([Drive: Annotation relations – Guidelines for P2GO](https://drive.google.com/open?id=1DXdjAuNf7u8CKXYlgW5kyzPgq7vnp-Aai0S5Sh63guc); [wiki: Annotation Relations](https://wiki.geneontology.org/index.php/Annotation_Relations)). The phenotype guideline asks curators to "think about how relevant and informative the resulting *acts upstream of* annotation would be" ([wiki: Annotating from phenotypes](https://wiki.geneontology.org/index.php/Annotating_from_phenotypes)). PomBase's policy is to avoid causal relations of this kind entirely, and its boundaries remain debated ([go-annotation#2417](https://github.com/geneontology/go-annotation/issues/2417); [go-annotation#1532](https://github.com/geneontology/go-annotation/issues/1532)).

**Worked example.** A sperm motility protein is `involved_in` GO:0097722 sperm motility. It is not `involved_in` GO:0009566 fertilization. If a curator wants the fertilization link visible, the honest relation is `acts upstream of, positive effect` GO:0009566 ([go-annotation#1450](https://github.com/geneontology/go-annotation/issues/1450) records that `causally_upstream_of` can express this). In most cases the motility annotation suffices, because a user can follow the ontology from motility to its role.

**Repository note.** The schema's `AnnotationQualifierEnum` currently describes `acts_upstream_of` as "acts upstream of or within". That conflates two different RO relations and should be corrected (see Open questions).

**Provenance.** [GOC].

<a id="bp-6"></a>

### BP-6. Annotate the process the gene product acts in, not the readout that was measured

**Statement.** Identify what was measured and what conclusion the authors drew. Then annotate the process closest to the gene product's activity that the evidence supports. Never annotate the assay readout as a process when the readout is a downstream marker of something else.

**Rationale.** "Beware of read-outs" is long-standing GOC guidance. The wiki's example is DNA fragmentation, a readout for apoptosis that does not place the mutated gene in DNA catabolism ([wiki: Annotating from phenotypes](https://wiki.geneontology.org/index.php/Annotating_from_phenotypes)). The QC group's reports repeat it as "annotate to the conclusion of the experiment, not the read-out" ([Drive: GOC NYC 2018 QC group report](https://drive.google.com/open?id=1cTLQGeV9aUiMvMgW5DxB8pNOARlMoNmmz7nqiyxXPg0)).

**Common readouts and what they do not show:**

| Readout | Tempting term | Why it fails | Source |
|---|---|---|---|
| TUNEL, annexin V, cleaved caspase-3, PARP cleavage | apoptotic signaling or its regulation | late endpoints of almost any death; annexin V marks PS exposure, which is not the gene's activity | [wiki: Apoptosis Curation Manual](https://wiki.geneontology.org/index.php/Apoptosis_Curation_Manual); [APOPTOSIS assay readouts](../../APOPTOSIS/ASSAY_READOUT_OVERANNOTATION.md) |
| cytochrome c release, MOMP | regulation of cytochrome c release / MOMP | "pretty much any apoptosis-inducing event will trigger MOMP" | [wiki: Apoptosis Curation Manual](https://wiki.geneontology.org/index.php/Apoptosis_Curation_Manual) |
| mitochondrial membrane depolarisation | mitochondrion organization | readout of reduced mitochondrial activity | [go-annotation#2469](https://github.com/geneontology/go-annotation/issues/2469) |
| reduced DNA synthesis after siRNA | regulation of DNA replication | many cell-cycle blocks give the same result | [go-annotation#2510](https://github.com/geneontology/go-annotation/issues/2510) |
| cell size in a screen | regulation of cell size | indirect growth effects | [go-annotation#1886](https://github.com/geneontology/go-annotation/issues/1886) |
| checkpoint arrest in a mutant | checkpoint terms | arrest shows the checkpoint works; the mutated gene caused the damage | [wiki: Guidelines for checkpoints](https://wiki.geneontology.org/index.php/Guidelines_for_checkpoints) |
| altered spindle pole body separation from nuclear envelope defects | SPB separation | indirect phenotype | [go-annotation#1631](https://github.com/geneontology/go-annotation/issues/1631) |

**Worked example.** Silencing human RPS19 produces condensed DNA, nuclear fragmentation and PARP cleavage. Curators decided not to annotate regulation of apoptosis, because RPS19's role in small-subunit biogenesis explains the death as an indirect effect ([wiki: Apoptosis Curation Manual](https://wiki.geneontology.org/index.php/Apoptosis_Curation_Manual)).

**Provenance.** [GOC].

<a id="bp-7"></a>

### BP-7. Organism-level and other "high-level" processes need a mechanism

**Statement.** The following processes are reached by almost any perturbation: behaviour, development (embryonic, larval, organ), lifespan, growth, locomotion, cell proliferation, cell death, cell migration, protein localization and reproduction. Annotate a gene product to them only when the mechanism links its activity to the process. In practice that means the gene product acts in the circuit, signalling pathway or cell-level step that makes up the process. Without a mechanism, do not annotate. In review of an existing row, apply BP-14.

Term-specific constraints, checked against the current ontology:

- GO:0007610 behavior, GO:0048856 anatomical structure development, GO:0008219 cell death and GO:0040007 growth are in `gocheck_do_not_annotate`. Use a specific child or nothing.
- GO:0007568 aging and GO:0000003 reproduction are obsolete in the current release. Do not create new annotations to them.
- GO:0008283 cell population proliferation is not flagged do-not-annotate. The 2018 annotation review converged on requiring a cell-type extension rather than a flag ([go-annotation#2204](https://github.com/geneontology/go-annotation/issues/2204)). Use a cell-type-specific child, such as GO:0050673 epithelial cell proliferation, or add the cell type as an extension.
- The same reasoning covers GO:0008284 positive regulation of cell population proliferation, which a 2019 thread said should not be used directly ([go-annotation#2469](https://github.com/geneontology/go-annotation/issues/2469)). The term carries no flag, so this is practice rather than enforcement.

**Rationale.** The wiki lists these processes and strongly encourages curators not to annotate them when the mechanism is unknown ([wiki: Annotating from phenotypes](https://wiki.geneontology.org/index.php/Annotating_from_phenotypes)). Behaviour is the cleanest test. In this repository's corpus, 86% of reviewer-adjudicated behaviour annotations were downgraded (197 adjudicated, September 2026). The rows accepted as core were mostly sensory receptors and channels acting in the relevant neurons, clock components and neuropeptides ([BEHAVIOR](../../BEHAVIOR.md)). [go-annotation#2820](https://github.com/geneontology/go-annotation/issues/2820) (open) questions human `adult behavior` annotations from autism-association papers on the same grounds.

**Worked examples.**

- Mouse Tuba1a carries five behaviour terms, all IMP, including GO:0007626 locomotory behavior. The behaviours are distal consequences of brain malformation, so all five are kept as non-core ([BEHAVIOR](../../BEHAVIOR.md)).
- *C. elegans* lov-1 and pkd-2 are the polycystin sensory channels of the male-mating circuit, so `mating behavior` is accepted as core. Drosophila CRY gets GO:0048512 circadian behavior because the behaviour is the clock's direct output ([BEHAVIOR](../../BEHAVIOR.md)).

**Provenance.** [GOC+]. The list is GOC's. The subset and obsoletion checks, the extension requirement and the behaviour rubric are sharpenings.

<a id="bp-8"></a>

### BP-8. Give pleiotropic core machinery its core processes, not every process it affects

**Statement.** Some gene products have a central role whose loss disturbs many processes: RNA polymerase, spliceosome, ribosome, proteasome, general chaperones, general chromatin modifiers, Mediator. Annotate them to the processes their activity is part of. Do not annotate the downstream processes that fail when they are removed. Remove such downstream rows, or demote them in review, once the core activity is known.

**Rationale.** [wiki: Annotating downstream processes](https://wiki.geneontology.org/index.php/Annotating_downstream_processes) gives two examples. Yeast RPB2 should be annotated to transcription, not to the many processes transcription feeds. Yeast spliceosome mutants had been annotated to translation because of translation defects, and those rows were removed once their role in mRNA splicing was established, since many ribosomal transcripts are spliced in yeast. FlyBase pathway guidance treats NuRD and Mediator as non-specific and keeps them off pathway terms ([Drive: FlyBase pathway curation guide](https://drive.google.com/open?id=1Toyf0QhDjuGMYa1KyDGF-T9qXnXfvxAuYisLpAxfZoI)). The Term Matrix QC system finds such errors by flagging co-annotation to processes that rarely share genes ([PMID:32875947](https://europepmc.org/article/MED/32875947), Term Matrix; [go-annotation#1396](https://github.com/geneontology/go-annotation/issues/1396)).

**Worked example.** A spliceosomal protein with IMP rows to GO:0006412 translation and IDA rows to GO:0000398 mRNA splicing, via spliceosome: keep splicing as core. For translation, use `REMOVE` if the paper's own data attribute the defect to splicing. Otherwise use `MARK_AS_OVER_ANNOTATED`.

**Provenance.** [GOC].

<a id="bp-9"></a>

### BP-9. Developmental processes: annotate the cell-level step, at the right grain, for genes that perform it

**Statement.** Annotate developmental processes when the gene product performs a defined step: a fate decision, a differentiation programme, a morphogenetic cell behaviour, or a signalling pathway acting in that tissue. Prefer the cell-level process (GO:0045165 cell fate commitment, GO:0030154 cell differentiation, cell-type-specific children) over organ development terms. Use the standard sub-process that matches the evidence: formation, morphogenesis, structural organization, differentiation, fate specification, determination, commitment or maturation. Organ- and organism-level development terms come from phenotypes far more often than from steps. Treat them as non-core unless the gene's activity defines that organ's development.

**Rationale.** GO's development node has a fixed pattern. `x development` has parts: morphogenesis, which includes formation and structural organization; maturation; and differentiation of the cells that make up x. Cell differentiation has fate commitment (specification and determination) and cell development ([wiki: Development](https://wiki.geneontology.org/index.php/Development)). The pattern is precise, but the evidence for a given step often is not. Fate specification and determination differ in an assay (reversible or not in a neutral environment) that most papers do not perform ([NEURON_DEVELOPMENT](../../NEURON_DEVELOPMENT.md)). The 2022 BP refactoring proposal separates cell-level from organism-level development. It notes that "regulation of gross anatomical structure development" is doubtful, because regulation happens at the level of pathways and cells ([Drive: BP refactoring 2022 – developmental process](https://drive.google.com/open?id=1FafBfb44nAk-7PwUDj42XQLgwJYxPdq8ec4n-cWwKkg)). The 2023 draft on macro processes calls organ-level terms "laundry lists of genes" ([Drive: Decomposition of macro biological processes](https://drive.google.com/open?id=1q7PE8VGRGYWyohbLMwpiYpd6dnCJQVuomyzsK5dC9bc)).

**Worked examples.**

- Human NOTCH1 and ASCL1: GO:0048663 neuron fate commitment is kept as an exemplar term. Notch-mediated lateral inhibition is a genuine binary fate decision with strong experimental support ([NEURON_DEVELOPMENT](../../NEURON_DEVELOPMENT.md)).
- A specification term inferred from early transcriptional bias, with no test of plasticity, is over-precise. Use the commitment or differentiation parent the data support (`MODIFY`), as the NEURON_DEVELOPMENT framework recommends for glial specification rows.
- An IEP time-course in which a metabolic enzyme rises as a tissue matures, such as rat Ckmt2 in postnatal heart, does not show a role in building the tissue. `MARK_AS_OVER_ANNOTATED` ([IEP](../../IEP.md), pattern 2).

**Provenance.** [GOC+]. The term structure is GOC's. Preferring cell-level terms and treating organ-level terms as non-core are our synthesis.

<a id="bp-10"></a>

### BP-10. Cell death: choose the phase, keep regulation for specific effects, and do not equate death with apoptosis

**Statement.** For apoptosis, annotate the phase when the evidence identifies it: extrinsic (GO:0097191) or intrinsic (GO:0097193) apoptotic signalling, with GO:0097190 apoptotic signaling pathway used downstream of the BID crosstalk point or when the initiating signal is unknown, and GO:0097194 execution phase of apoptosis. Annotate GO:0006915 apoptotic process directly only when the phase cannot be told. Use regulation terms (GO:0043065, GO:0043066 and children) only when the gene product specifically modulates the process. A side effect of disrupting a major pathway does not qualify. A viability defect alone does not show apoptosis.

**Rationale.** These are the Apoptosis Curation Manual's central rules ([wiki: Apoptosis Curation Manual](https://wiki.geneontology.org/index.php/Apoptosis_Curation_Manual)). The manual also records the obsoletion of cell death terms that "did not represent normal, physiological processes", and states the current practice that the mechanism of death must be known before annotating. [go-annotation#1056](https://github.com/geneontology/go-annotation/issues/1056) rehoused "induction of apoptosis" annotations on the same principle. This repository's apoptosis work found that readout-based rows are usually true but non-core. Of 72 mined readout rows, 35 were kept as non-core and 27 accepted ([APOPTOSIS assay readouts](../../APOPTOSIS/ASSAY_READOUT_OVERANNOTATION.md)).

**Worked examples.**

- Human CASP3 rows on GO:0006915 can usually move to GO:0097194 execution phase of apoptosis, because the caspase's role in that phase is direct ([APOPTOSIS](../../APOPTOSIS.md), curation heuristics).
- Mouse Pten, GO:0006915 from genetic interaction data: the apoptosis outcome lies downstream of PTEN/PI3K/AKT signalling, so `KEEP_AS_NON_CORE` ([APOPTOSIS assay readouts](../../APOPTOSIS/ASSAY_READOUT_OVERANNOTATION.md)).
- Restraint is regulation. BCL2, XIAP and CFLAR are direct regulators of apoptosis even though their function is to prevent it ([APOPTOSIS](../../APOPTOSIS.md)).
- For cell type, the manual's advice still holds: keep GO:0006915 and add the cell type (for example a neutrophil, CL:0000775) as an extension, rather than moving to GO:0001781 neutrophil apoptotic process and stranding ISS transfers to species that may lack the cell type ([wiki: Apoptosis Curation Manual](https://wiki.geneontology.org/index.php/Apoptosis_Curation_Manual)).

**Provenance.** [GOC]. The non-core default for readout rows is [GOC+].

<a id="bp-11"></a>

### BP-11. Do not request, add or split precomposed "X involved in Y" terms; decompose them to X and record where Y went

**Statement.** Do not request new "X involved in Y" terms, and do not use them for new annotations when the X term exists. When reviewing a row on such a term:

1. Read the logical definition. If it has no `part_of`, the "involved in" is either entailed by X (regulation of MOMP) or absent (grouping classes). Keep the term.
2. Otherwise decide whether X alone still says what the gene does. If it does, `MODIFY` to X, and record in `review.decomposed_into` where Y went: a GO-CAM or module, the gene's core functions, or `context_dropped: true`.
3. Never split the row into two unrelated annotations (`involved_in` X plus `involved_in` Y). Never re-encode Y as an extension `part_of(Y)` on X, which restates the retired class. Extensions that add cell type or location (`occurs_in`) are not decomposition and remain fine.
4. Justify each half separately. A decomposition is a review, not a reformat.

**Rationale.** GO has obsoleted more than a thousand precomposed terms, most with the comment that the term "should be captured as a GO-CAM model". Of 784 live terms with this label pattern, many remain in use ([INVOLVED_IN_PRECOMPOSITION](../../INVOLVED_IN_PRECOMPOSITION.md)). `replaced_by` keeps one half automatically. `consider` lists both halves, but it is curator advice, so check each half against the evidence ([CLAUDE.md](../../../CLAUDE.md)). Some terms are the right grain despite the label. GO:0106074 aminoacyl-tRNA metabolism involved in translational fidelity names editing, which has no other GO term. GO:0006271 DNA strand elongation involved in DNA replication names a stage ([INVOLVED_IN_PRECOMPOSITION](../../INVOLVED_IN_PRECOMPOSITION.md), round 5).

**Worked examples.**

- Human HSPA8, GO:0061740 protein targeting to lysosome involved in chaperone-mediated autophagy: MODIFY to GO:0006622 protein targeting to lysosome. Y (GO:0061684 chaperone-mediated autophagy) is a mechanism, so it goes to the chaperone-mediated autophagy module.
- *C. elegans* engulfment genes ced-1, ced-6 and ced-7, GO:1904747 positive regulation of apoptotic process involved in development: MODIFY to GO:0043065 positive regulation of apoptotic process with `context_dropped: true`. The developmental context is where the pro-death role was measured, not a mechanism. The gene's own GOA rows on the same claim move with the replacements, so that no gene proposes a term while keeping its child ([INVOLVED_IN_PRECOMPOSITION](../../INVOLVED_IN_PRECOMPOSITION.md), round 6).

**Provenance.** [GOC+] for decomposition, which GO's own obsoletion comments direct. [NEW] for the `decomposed_into` record and the rule against `part_of(Y)` extensions. This departs from older guidance that encouraged requesting such terms (see Differences).

<a id="bp-12"></a>

### BP-12. Annotate the step term when the evidence reaches it; do not demand BP specificity that only restates the MF

**Statement.** If the evidence identifies the step (for example a named cascade or a phase), annotate the step term. Its pathway ancestors follow by inference, so do not add them separately from the same evidence. Annotate a pathway-level term directly only when no step term fits or the evidence stops at the pathway, for example a genetic requirement with no step assignment, which takes an upstream relation under BP-4. Do not push toward a BP child whose only added specificity repeats a fact already asserted in MF.

**Rationale.** Ontology inference propagates `involved_in` over `is_a` and `part_of`, so a step annotation already says the gene is in the pathway. The cross-aspect case is documented in [OVER_ANNOTATION_PATTERNS](../../OVER_ANNOTATION_PATTERNS.md), pattern 9. The amino-acid-specific tRNA aminoacylation BP terms (GO:0006419 alanyl-tRNA aminoacylation and its siblings) each pair one-to-one with an MF that already names the amino acid (GO:0004813 alanine-tRNA ligase activity). GO directs annotation to the MF plus the compartment-level process. The same caution applies to step terms under regulation. An assay that reads out one step does not show that the step is where regulation acts. A gene product that blocks a cargo's nuclear translocation is better annotated to GO:0042308 negative regulation of protein import into nucleus than to regulation of the translocation step, because regulating that step would imply the earlier steps, such as docking, proceed normally ([go-annotation#1011](https://github.com/geneontology/go-annotation/issues/1011); see [RS-2](regulation-and-signaling.md#rs-2)).

**Worked example.** Annotate MAP2K1 `involved_in` GO:0000165 MAPK cascade (a cassette, GO:0141124 intracellular signaling cassette). Annotate the receptor pathway it serves, such as GO:0007173 epidermal growth factor receptor signaling pathway, only when the evidence places it there (see [RS-7](regulation-and-signaling.md#rs-7)).

**Provenance.** [GOC+].

<a id="bp-13"></a>

### BP-13. Choose the deepest term the row's own evidence supports, and no deeper

**Statement.** For each row, use the most specific term its own evidence supports. A correct but general term with evidence for a specific descendant is `MODIFY` to that descendant, ideally one the gene already carries. A general term whose evidence stops there is kept: `ACCEPT` if core, `KEEP_AS_NON_CORE` if not. `TOO_GENERAL` is only for terms that are imprecise on their own once a specific term is asserted elsewhere in the review. Over-specific terms, such as a cell-type, stimulus or context the evidence does not establish, are `MODIFY` to the parent.

**Rationale.** This is the repository's maintainer ruling of 2026-11-14 ([CLAUDE.md](../../../CLAUDE.md), MODIFY rules), applied to BP. The opposite failure is as common: a specific term chosen from the paper's framing rather than its data. Examples are a hormone-specific apoptotic pathway without evidence of the hormone's mechanism ([wiki: Apoptosis Curation Manual](https://wiki.geneontology.org/index.php/Apoptosis_Curation_Manual)), or a rodent stress-model term applied to a plant ([IEP](../../IEP.md), pattern 7).

**Worked example.** A kinase row on GO:0097190 apoptotic signaling pathway whose paper shows only that knockdown increases staurosporine-induced death: the evidence does not reach a pathway step. Use `acts upstream of or within, negative effect` GO:0006915, or `KEEP_AS_NON_CORE` on an existing row. Do not deepen it to the intrinsic branch, because staurosporine's mechanism does not identify the branch ([wiki: Apoptosis Curation Manual](https://wiki.geneontology.org/index.php/Apoptosis_Curation_Manual), example 1).

**Provenance.** [GOC+].

<a id="bp-14"></a>

### BP-14. In review, separate core processes from real but peripheral ones, and reserve REMOVE for contradicted claims

**Statement.** A process is core when the gene product's core activity is a step of it. A process is non-core when the claim is true but peripheral: a downstream outcome, a tissue context, a pleiotropic consequence. Map the cases to actions:

| Situation | Action |
|---|---|
| Activity is a step of the process | `ACCEPT` |
| Real, reproducible effect, distal to the activity | `KEEP_AS_NON_CORE`, with the proximal defect named in `reason` |
| Effect real but the term overstates it (uselessly broad, or an expression correlate read as a role) | `MARK_AS_OVER_ANNOTATED` |
| Same claim, better term available from this row's evidence | `MODIFY` |
| Contradicted (wrong gene or paralog, opposite sign, refuted mechanism, demonstrably wrong mapping) | `REMOVE` |
| Evidence inaccessible or unadjudicated | `UNDECIDED` |

**Rationale.** The GOC wiki says older phenotype-based annotations "should be reviewed and removed" when new knowledge shows they do not reflect the gene's MF–BP relation ([wiki: Annotating from phenotypes](https://wiki.geneontology.org/index.php/Annotating_from_phenotypes)). It also acknowledges that groups differ, and that some keep downstream annotations as a record ([wiki: Annotating downstream processes](https://wiki.geneontology.org/index.php/Annotating_downstream_processes)). In a review we cannot see the curator's full text ([CLAUDE.md](../../../CLAUDE.md), "Do not overrule curators from incomplete evidence"). Demotion preserves the data and still removes the row from the core picture. Rows that share a term must receive consistent actions, and REMOVE is never a way to deduplicate ([docs/action_consistency.md](../../../docs/action_consistency.md)).

**Worked examples.** Mouse Agtr1a, `drinking behavior`: direct central-angiotensin experiments assign the behaviour to the paralog AT1B, so the claim is contradicted and `REMOVE` is correct. Mouse Tuba1a, `locomotory behavior`: distal, so `KEEP_AS_NON_CORE` ([BEHAVIOR](../../BEHAVIOR.md)).

**Provenance.** [NEW], building on GOC guidance.

<a id="bp-15"></a>

### BP-15. Do not propagate developmental, behavioural or stimulus-response terms without a conserved mechanism, and check that the pathway can exist in the target taxon

**Statement.** Organism-level process terms (development, behaviour, physiology) and "response to" terms should not be transferred by orthology, ISS or IBA unless the mechanism that places the gene in the process is conserved and the process exists in the target lineage. A pathway term whose definition requires a component the target genome lacks is unsatisfiable there.

**Rationale.** [go-annotation#1344](https://github.com/geneontology/go-annotation/issues/1344) argued against Ensembl Compara propagation of developmental and response-to-substance terms and proposed a not-for-propagation flag. [go-annotation#1364](https://github.com/geneontology/go-annotation/issues/1364) concluded that downstream processes regulated by signalling molecules should not be propagated unless broadly conserved. PAINT does not normally propagate "response to" terms ([go-annotation#2171](https://github.com/geneontology/go-annotation/issues/2171); [go-annotation#2250](https://github.com/geneontology/go-annotation/issues/2250)). Taxon constraints enforce part of this (GORULE:0000013; [Drive: Taxon constraints for signaling pathways, Padua 2023](https://drive.google.com/open?id=117j8ysvt6FpVR0KCeFgrRDjUjm3jVXm8-nNReVU-hEg)).

**Worked example.** *Dictyostelium* STATa/c carried GO:0007259 cell surface receptor signaling pathway via JAK-STAT, but *Dictyostelium* has no JAK. The rows were rescoped to the JAK-independent parent GO:0097696 cell surface receptor signaling pathway via STAT ([PATHWAY_SATISFIABILITY taxon-absent-component detector](../../PATHWAY_SATISFIABILITY/taxon_absent_component/README.md)). See [phylogenetic-propagation.md](phylogenetic-propagation.md) for the IBA side.

**Provenance.** [GOC+].

## Decision aid

Start with the evidence and the gene product, and ask in order:

| # | Question | If yes | If no |
|---|---|---|---|
| 1 | Is the claim contradicted (wrong gene, opposite sign, refuted)? | Do not annotate / `REMOVE` | go on |
| 2 | Can you name the gene product's activity that is a step of P? | `involved_in` P (BP-1) | go on |
| 3 | Is the gene product a substrate, product, precursor or other input of P that supplies no scaffold, cofactor role or chemistry? | Not P; the agent gets P (BP-2) | go on |
| 4 | Is the gene product a known modulator of a P participant? | Regulation term (see [RS-2](regulation-and-signaling.md#rs-2)) | go on |
| 5 | Is P a readout for something more proximal? | Annotate the proximal process (BP-6) | go on |
| 6 | Is P organism-level (behaviour, development, growth, lifespan, proliferation, death)? | Only with a mechanism; else none (new) / non-core (review) (BP-7) | go on |
| 7 | Is the mechanism unknown but the effect real and directional? | `acts upstream of or within, positive/negative effect` P (BP-4) | no annotation |

For precomposed terms, apply BP-11 before question 2: decompose first, then evaluate each half.

## Common errors

- **"Required for" read as "involved in".** Authors write "X is required for Y". The paper shows necessity, and a GO annotation states participation ([wiki: Annotating from phenotypes](https://wiki.geneontology.org/index.php/Annotating_from_phenotypes)). Fix: upstream relation (BP-4) or proximal term (BP-6).
- **Substrate on the processing term.** A precursor annotated to its own maturation or processing term. Fix: remove the precursor from the term (BP-2) and check that the processing enzyme carries it.
- **Assembly factors on the complex's process.** Subunits or chaperones needed for a complex's assembly, annotated to the process the complex performs. [go-annotation#2942](https://github.com/geneontology/go-annotation/issues/2942) states that factors needed for maturation of a process's members are not normally annotated to that process. [go-annotation#2149](https://github.com/geneontology/go-annotation/issues/2149) found complex assembly itself over-annotated to subunits.
- **Housekeeping knockout on a specific process.** A ribosomal, splicing or proteasome subunit annotated to apoptosis, cell cycle or a signalling pathway from a knockdown. Fix: BP-8.
- **Behaviour or development from a structural or metabolic gene's phenotype.** Fix: BP-7 and BP-14 (`KEEP_AS_NON_CORE`, with the proximal defect named).
- **IEP time-course on a developmental term.** Expression rising as a tissue matures, annotated as building the tissue. Fix: `MARK_AS_OVER_ANNOTATED` ([IEP](../../IEP.md)).
- **Batch annotation from one screen.** One paper, one term, many unrelated genes. Treat each row as suspect ([IEP](../../IEP.md), pattern 3; [go-annotation#1869](https://github.com/geneontology/go-annotation/issues/1869)).
- **Decomposing by splitting.** `involved_in` X plus `involved_in` Y loses the fact that X occurs as part of Y. Fix: BP-11.
- **Host proteins on pathogen processes.** Host factors co-opted by a virus annotated to viral transcription or replication. The host protein does not perform the viral process ([go-annotation#1507](https://github.com/geneontology/go-annotation/issues/1507); see [multi-organism-and-ncrna.md](multi-organism-and-ncrna.md)).
- **Reading "activated during" as "involved in".** A gene activated during meiosis is not thereby `involved_in` meiosis, and the GO meiosis term means the meiotic division, not the developmental phase ([go-annotation#1005](https://github.com/geneontology/go-annotation/issues/1005)).

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [wiki: Annotating downstream processes](https://wiki.geneontology.org/index.php/Annotating_downstream_processes); [wiki: Guidelines from Annotation Camp](https://wiki.geneontology.org/index.php/Guidelines_from_Annotation_Camp) | Request specific "X involved in Y" terms (e.g. "BMP signaling involved in cardiac cell differentiation") rather than annotating X and Y separately. | Never request them; annotate X, and put Y in a GO-CAM/module, a core function, or drop it (BP-11). | GO has since obsoleted over a thousand such terms as precomposed GO-CAMs. Both pages predate that. The Annotation Camp page is flagged as historical and partly superseded. |
| [wiki: Annotating downstream processes](https://wiki.geneontology.org/index.php/Annotating_downstream_processes) | Groups differ: some remove downstream annotations when mechanism is known, some keep them. Both are acceptable. | At curation time, do not make them. At review time, demote real but distal rows (`KEEP_AS_NON_CORE`) and remove only contradicted ones (BP-14). | Resolves a stated inconsistency. Demotion keeps the data out of the core picture without discarding experimental results the reviewer may not fully see. |
| [wiki: Annotating from phenotypes](https://wiki.geneontology.org/index.php/Annotating_from_phenotypes) | Older IMP annotations "should be reviewed and removed" when they no longer reflect the MF–BP relation. | Change the relation (record `WRONG_QUALIFIER`) or the term (`MODIFY`). Remove only if the claim is false (BP-4, BP-14). | A true upstream effect annotated with too strong a relation is still true. Removing it loses information that the correct relation would carry. |
| [wiki: Annotating from phenotypes](https://wiki.geneontology.org/index.php/Annotating_from_phenotypes) (high-level phenotypes) | "Strongly encourage" not annotating high-level processes without mechanism. | Same for new annotations. For existing rows: the BEHAVIOR rubric (accept if the gene acts in the circuit, non-core if distal, over-annotated if uselessly broad, remove if contradicted) (BP-7, BP-14). | The wiki gives no review-time guidance. The repository rubric fills that gap. |
| [wiki: Annotating from phenotypes](https://wiki.geneontology.org/index.php/Annotating_from_phenotypes) (list of high-level processes) | Lists aging and reproduction among high-level processes to treat with caution. | GO:0007568 aging and GO:0000003 reproduction are now obsolete; behavior, anatomical structure development, cell death and growth are do-not-annotate (BP-7). | The ontology has changed since the 2018 review of the page. |
| [go-annotation#2204](https://github.com/geneontology/go-annotation/issues/2204), [go-annotation#2469](https://github.com/geneontology/go-annotation/issues/2469) | Proposed making cell population proliferation do-not-annotate, then a mandatory-extension rule. A later thread says positive regulation of cell population proliferation "is not for direct annotation". | Neither term carries the flag. Require a cell type (child term or extension) for both (BP-7). | The decision was never enforced in the ontology. We state the practice explicitly so reviewers apply it consistently. |
| [wiki: Apoptosis Curation Manual](https://wiki.geneontology.org/index.php/Apoptosis_Curation_Manual), "Other annotation examples" | Staurosporine-induced or light-induced death data support "positive/negative regulation of apoptotic process". | For a phenotype with no mechanism, use `acts upstream of or within` with a sign on GO:0006915. A regulation term needs a specific effect (BP-4, BP-10, BP-13). | The manual contradicts itself. Its later section says current practice requires a known mechanism, and the phenotype guideline's CHCHD10 example forbids the regulation term. We follow the newer statements. |
| [wiki: Apoptosis Curation Manual](https://wiki.geneontology.org/index.php/Apoptosis_Curation_Manual) vs [INVOLVED_IN_PRECOMPOSITION](../../INVOLVED_IN_PRECOMPOSITION.md) | The manual recommends a cell-type extension on GO:0006915 over a cell-type-specific term. The repository forbids `part_of(Y)` extensions as re-precomposition. | Both hold: `occurs_in` cell type is context and fine; `part_of` another process is a precomposition and not (BP-10, BP-11). | Apparent conflict. The two concern different relations. |
| [Drive: Regulation and causality & legacy qualifiers, 2017](https://drive.google.com/open?id=1fmgRMOPel-8_7iIuMAkVDNGuxurUWTxJRdsZTgSeNRM) | Legacy BP annotations should be read as "causally upstream of or within". | Do not assume any legacy `involved_in` is a participation claim. Test each one against BP-1 in review. | Sharpening. Legacy rows now carry `involved_in` in GAF/GPAD output, and the qualifier alone does not show that the relation was assessed. |
| [CLAUDE.md](../../../CLAUDE.md), [go-annotation#211](https://github.com/geneontology/go-annotation/issues/211) | Substrates are not participants (no GO wiki page states this generally). | General rule with three exceptions: scaffold, cofactor, chemistry (BP-2). | Fills a documentation gap. GO's corpus already follows the convention, but no written guideline exists. |
| [CLAUDE.md](../../../CLAUDE.md) | Comparator check before `NEW` process terms. | Same, and also when judging whether an existing lone annotation is an outlier (BP-3). | Extension of the same logic to review. |
| [Drive: BP refactoring 2022](https://drive.google.com/open?id=1FafBfb44nAk-7PwUDj42XQLgwJYxPdq8ec4n-cWwKkg); [Drive: Decomposition of macro BPs, 2023](https://drive.google.com/open?id=1q7PE8VGRGYWyohbLMwpiYpd6dnCJQVuomyzsK5dC9bc) | Draft proposals to separate cell-level from organism-level development and to model macro processes as has-part of cell-level processes. | Prefer cell-level developmental terms now; organ-level rows from phenotypes default to non-core (BP-9). | Acts on the direction of both drafts without waiting for the ontology change. |
| [FUNGAL_PHENOTYPES](../../FUNGAL_PHENOTYPES.md) vs [wiki: HMP](https://wiki.geneontology.org/index.php/Inferred_from_High_Throughput_Mutant_Phenotype_(HMP)) | HMP is equivalent to IMP and allowed when the screen phenotype correlates well with the process. | HTP growth phenotypes may corroborate or question an existing row. They should not create a new process annotation without a mechanism (BP-2). | The HMP criteria assess screen quality, not participation. Necessity data from a perfect screen are still necessity data. |
| Repository schema, `AnnotationQualifierEnum` | `acts_upstream_of` described as "acts upstream of or within". | `acts_upstream_of` is the mechanism-known, outside-the-process relation (BP-5). | Error in the repository's own enum description, not in GO guidance. |

## Open questions

1. **Scaffold proteins in pathways.** Is a MAPK scaffold part of the cascade, or a regulator of it? [go-annotation#1592](https://github.com/geneontology/go-annotation/issues/1592) settled on "part of", with a separate regulator MF where the scaffold also allosterically activates a kinase. The thread records dissent. We follow #1592 in [RS-7](regulation-and-signaling.md#rs-7), but the GOC has not written the rule into a guideline.
2. **When is `acts upstream of` worth asserting?** PomBase does not use it ([go-annotation#2417](https://github.com/geneontology/go-annotation/issues/2417)). The wiki leaves it to the curator. A criterion is needed, for example "only when the upstream process has no GO term".
3. **Developmental terms whose distinctions are rarely tested.** Should the specification/determination split be retired in favour of commitment for lineages where single-cell data show continuous trajectories ([NEURON_DEVELOPMENT](../../NEURON_DEVELOPMENT.md))?
4. **Should cell population proliferation and its regulation terms carry a GO rule requiring an extension**, as proposed in #2204?
5. **Machine-readable substrate relationships.** GO puts substrate relations on the enzyme (`has_input`), but `has_input` on a BP annotation does not appear in the GAF. How should standard annotation expose that angiotensinogen is the input of angiotensin maturation?
6. **Repository schema fix.** Correct the `acts_upstream_of` description in `AnnotationQualifierEnum`, and decide whether the relation-only MODIFY + NEW pattern ([QN-7](qualifiers-and-negation.md#qn-7)) should become a dedicated field.

## Sources

**GO wiki**

- [Annotating from phenotypes](https://wiki.geneontology.org/index.php/Annotating_from_phenotypes) (reviewed 2018)
- [Annotating downstream processes](https://wiki.geneontology.org/index.php/Annotating_downstream_processes) (flagged "to be reviewed")
- [Annotation Relations](https://wiki.geneontology.org/index.php/Annotation_Relations) (edited 2026)
- [Causally upstream of or within](https://wiki.geneontology.org/index.php/Causally_upstream_of_or_within) (reviewed 2023)
- [Apoptosis Curation Manual](https://wiki.geneontology.org/index.php/Apoptosis_Curation_Manual)
- [Development](https://wiki.geneontology.org/index.php/Development)
- [Guidelines for checkpoints](https://wiki.geneontology.org/index.php/Guidelines_for_checkpoints)
- [Guidelines from Annotation Camp](https://wiki.geneontology.org/index.php/Guidelines_from_Annotation_Camp) (historical)
- [Inferred from High Throughput Mutant Phenotype (HMP)](https://wiki.geneontology.org/index.php/Inferred_from_High_Throughput_Mutant_Phenotype_(HMP))

**GO Consortium Drive**

- [Annotation relations – Guidelines for P2GO](https://drive.google.com/open?id=1DXdjAuNf7u8CKXYlgW5kyzPgq7vnp-Aai0S5Sh63guc)
- [Case studies annotating from mutant phenotypes](https://drive.google.com/open?id=17FQlI3iWhra_eIW0luhjtOOn4RD_RiSp4GTYJvG4jS0)
- [GOC Corvallis 2017: Regulation and causality & use of qualifiers in legacy annotations](https://drive.google.com/open?id=1fmgRMOPel-8_7iIuMAkVDNGuxurUWTxJRdsZTgSeNRM)
- [GOC NYC 2018: QC group report](https://drive.google.com/open?id=1cTLQGeV9aUiMvMgW5DxB8pNOARlMoNmmz7nqiyxXPg0)
- [BP refactoring 2022 – developmental process](https://drive.google.com/open?id=1FafBfb44nAk-7PwUDj42XQLgwJYxPdq8ec4n-cWwKkg) (draft)
- [Decomposition of macro biological processes](https://drive.google.com/open?id=1q7PE8VGRGYWyohbLMwpiYpd6dnCJQVuomyzsK5dC9bc) (2023 draft)
- [FlyBase pathway curation guide](https://drive.google.com/open?id=1Toyf0QhDjuGMYa1KyDGF-T9qXnXfvxAuYisLpAxfZoI) (draft for discussion)
- [Taxon constraints for signaling pathways, Padua 2023](https://drive.google.com/open?id=117j8ysvt6FpVR0KCeFgrRDjUjm3jVXm8-nNReVU-hEg)

**go-annotation issues**

[#211](https://github.com/geneontology/go-annotation/issues/211), [#1005](https://github.com/geneontology/go-annotation/issues/1005), [#1011](https://github.com/geneontology/go-annotation/issues/1011), [#1056](https://github.com/geneontology/go-annotation/issues/1056), [#1344](https://github.com/geneontology/go-annotation/issues/1344), [#1364](https://github.com/geneontology/go-annotation/issues/1364), [#1396](https://github.com/geneontology/go-annotation/issues/1396), [#1450](https://github.com/geneontology/go-annotation/issues/1450), [#1507](https://github.com/geneontology/go-annotation/issues/1507), [#1517](https://github.com/geneontology/go-annotation/issues/1517), [#1532](https://github.com/geneontology/go-annotation/issues/1532), [#1592](https://github.com/geneontology/go-annotation/issues/1592), [#1631](https://github.com/geneontology/go-annotation/issues/1631), [#1869](https://github.com/geneontology/go-annotation/issues/1869), [#1886](https://github.com/geneontology/go-annotation/issues/1886), [#2149](https://github.com/geneontology/go-annotation/issues/2149), [#2171](https://github.com/geneontology/go-annotation/issues/2171), [#2204](https://github.com/geneontology/go-annotation/issues/2204), [#2250](https://github.com/geneontology/go-annotation/issues/2250), [#2417](https://github.com/geneontology/go-annotation/issues/2417), [#2425](https://github.com/geneontology/go-annotation/issues/2425), [#2456](https://github.com/geneontology/go-annotation/issues/2456), [#2469](https://github.com/geneontology/go-annotation/issues/2469), [#2510](https://github.com/geneontology/go-annotation/issues/2510), [#2820](https://github.com/geneontology/go-annotation/issues/2820), [#2942](https://github.com/geneontology/go-annotation/issues/2942)

**Papers**

- [PMID:32875947](https://europepmc.org/article/MED/32875947) Term Matrix: a GO annotation quality control system based on ontology term co-annotation patterns (2020)

**Repository**

- [CLAUDE.md](../../../CLAUDE.md): "Do not add what curators deliberately declined to add", MODIFY rules, "Decomposing precomposed terms", "Do not overrule curators"
- [INVOLVED_IN_PRECOMPOSITION](../../INVOLVED_IN_PRECOMPOSITION.md)
- [OVER_ANNOTATION_PATTERNS](../../OVER_ANNOTATION_PATTERNS.md)
- [BEHAVIOR](../../BEHAVIOR.md)
- [NEURON_DEVELOPMENT](../../NEURON_DEVELOPMENT.md)
- [APOPTOSIS](../../APOPTOSIS.md) and [APOPTOSIS/ASSAY_READOUT_OVERANNOTATION](../../APOPTOSIS/ASSAY_READOUT_OVERANNOTATION.md)
- [FUNGAL_PHENOTYPES](../../FUNGAL_PHENOTYPES.md)
- [PATHWAY_SATISFIABILITY](../../PATHWAY_SATISFIABILITY.md) and its [taxon-absent-component detector](../../PATHWAY_SATISFIABILITY/taxon_absent_component/README.md)
- [IEP](../../IEP.md)
- [FUNCTION_REQUIREMENT_RULES](../../FUNCTION_REQUIREMENT_RULES.md) (regulators annotated with the activity they regulate, as a flagged error class)
- [docs/action_consistency.md](../../../docs/action_consistency.md), [docs/source_defects.md](../../../docs/source_defects.md)
