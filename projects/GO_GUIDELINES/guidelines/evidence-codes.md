# Evidence codes: GO annotation guidelines

Status: draft v0.1 (2026-11-15) · Part of [GO_GUIDELINES](../../GO_GUIDELINES.md)

**In brief:**

- Pick the code from what the experiment did to the gene product, not from how convinced you are. A direct assay of the product is IDA; a perturbation of the product is IMP; two perturbations are IGI; an identified partner is IPI; the product's own abundance changing is IEP.
- An evidence code records provenance, not quality. A review judges the claim about the gene. A weak code is never by itself a reason to remove a row.
- IEP supports only biological process terms, and only from the gene's normal expression. Ask whether the product does the work of the process or is merely induced during it.
- Every inferential code (IPI, IGI, ISS family, IC, IEA) needs a WITH/FROM value that a reader can check. IDA, EXP, TAS and ND take none.
- High-throughput (HTP family) evidence meets the same bar as low-throughput evidence. What the dataset was used to claim matters more than the code it carries.
- ND is correct when no literature on this gene product, in this species, identifies a function in that aspect. Inferred rows in the same aspect do not make it stale.

## Scope

This document covers the choice and the review of GO evidence codes for single
(standard) annotations, and the ECO classes that sit behind them. It covers the
experimental codes (EXP, IDA, IPI, IMP, IGI, IEP), their high-throughput twins
(HTP, HDA, HMP, HGI, HEP), the similarity codes (ISS, ISO, ISA, ISM, IGC), author
and curator statements (TAS, NAS, IC), ND, and, briefly, RCA and IEA. The
phylogenetic codes (IBA, IBD, IKR, IRD) are summarised in one rule and treated in
full in [phylogenetic-propagation.md](phylogenetic-propagation.md); electronic
pipelines are treated in [electronic-annotation.md](electronic-annotation.md).

Going from a paper's figures to a term is the subject of
[from-paper-to-annotation.md](from-paper-to-annotation.md). This document assumes
the term is chosen and asks which code, which WITH/FROM, and which reference.
Qualifiers (NOT, contributes_to) are in
[qualifiers-and-negation.md](qualifiers-and-negation.md).

## Principles

**A code names an inference, not an experiment.** The [GO evidence code
guide](https://wiki.geneontology.org/index.php/Guide_to_GO_Evidence_Codes) says
codes "are not necessarily a classification of types of experiments" and must
not be read apart from the term. The same immunoprecipitation supports IDA for a
complex term and IPI for a binding term. The question is always: what step of
reasoning connects this observation to this term for this gene product?

**A code is not a confidence score.** The same guide states that evidence codes
"cannot be used as a measure of the quality of the annotation." This repository
holds the reviewing side of that principle: a review judges claims about the gene,
and rows that share a term reinforce each other
([CLAUDE.md](../../../CLAUDE.md); [action consistency](../../../docs/action_consistency.md)).

**Inferential codes must be auditable.** An IPI row without the partner, an ISO
row without the donor, or an IC row without the source annotation cannot be
checked, so it cannot be trusted. WITH/FROM is how a reader re-runs the curator's
reasoning.

**GAF codes are a lossy projection of ECO.** Curation tools now record ECO classes.
Each class maps to one GAF code, and a class with two parents in different GAF
branches is forced into one of them. Several systematic errors in GOA come from
that projection, not from curators (rule [EV-15](#ev-15)).

## Rules

<a id="ev-1"></a>

### EV-1. Use the most specific experimental code; do not use EXP when IDA, IPI, IMP, IGI or IEP applies.

EXP (ECO:0000269, experimental evidence used in manual assertion) is the parent of
the five low-throughput experimental codes. The [EXP wiki page](https://wiki.geneontology.org/index.php/Inferred_from_Experiment_%28EXP%29)
asks curators to use a child code and to leave WITH/FROM empty. A bare EXP hides the
inference a reviewer most needs to see. When reviewing an EXP row, read the paper and
judge the claim as though it carried the specific code the method warrants.

*Example.* PNPLA3 carries `GO:0003841` 1-acylglycerol-3-phosphate O-acyltransferase
activity as EXP from [PMID:21878620](https://europepmc.org/article/MED/21878620),
a paper that assayed the reaction and found no activity. Reading it as "IDA, enzyme
assay" makes the defect visible: the assay is a direct test of the term and the
result was negative, so the claim is a NOT, not a positive
([MISCITATIONS](../../MISCITATIONS.md); review in `genes/human/PNPLA3`).

Provenance: [GOC] [wiki: EXP](https://wiki.geneontology.org/index.php/Inferred_from_Experiment_%28EXP%29).

<a id="ev-2"></a>

### EV-2. Use IDA when the experiment measures the gene product's own activity, location or complex membership directly.

IDA (ECO:0000314) covers enzyme assays, in vitro reconstitution, immunolocalisation,
cell fractionation, and binding assays in which the partner cannot be given an
identifier (a nucleic acid, a lipid, actin filaments). IDA takes no WITH/FROM
(GORULE:0000017) and must not be used for `GO:0005488` binding or `GO:0005515`
protein binding (GORULE:0000003). Isolating a complex by pulling down a tagged
subunit is IDA for the complex (CC) term, because it assays the complex directly.

A protein expressed in a heterologous or overexpression system is still IDA when
the system is the vehicle for an assay of normal activity or location. The 2026
clarification ([go-annotation#6468](https://github.com/geneontology/go-annotation/issues/6468))
settled the boundary: overexpression used to measure a molecular function is IDA;
gain- or loss-of-function phenotypes used to infer a process are IMP
([EV-4](#ev-4)).

*Examples.* `GO:0004596` protein-N-terminal amino-acid acetyltransferase activity
for NAA50 from enzyme kinetics ([PMID:21900231](https://europepmc.org/article/MED/21900231),
the IDA wiki example). `GO:0051015` actin filament binding for mouse Actn1 is IDA,
not IPI, because F-actin has no gene-product identifier. Rat guanylate cyclase GC-F
expressed in COS cells and assayed for `GO:0004383` guanylate cyclase activity is
IDA, not IEP ([wiki: IEP](https://wiki.geneontology.org/index.php/Inferred_from_Expression_Pattern_%28IEP%29), PMID:7831337).

*Counter-example.* MGI annotated CREG1 (UniProtKB:O75629) to `GO:0006897`
endocytosis and `GO:0006914` autophagy as IDA from overexpression and knockdown
phenotypes. After #6468 these were recoded; process inferences from perturbation
phenotypes are IMP.

Provenance: [GOC] [wiki: IDA](https://wiki.geneontology.org/index.php/Inferred_from_Direct_Assay_%28IDA%29);
[go-annotation#6468](https://github.com/geneontology/go-annotation/issues/6468).

<a id="ev-3"></a>

### EV-3. Use IPI only with the partner's identifier in WITH/FROM, and only for binding, complex or interaction-dependent terms; never for catalytic activity.

IPI (ECO:0000353) is a direct assay in which the partner is known and has a stable
identifier (gene, protein, RNA, ComplexPortal complex). The identifier is
mandatory (GORULE:0000018). Independent partners are separated by pipes; partners
required simultaneously by commas
([go-annotation#2349](https://github.com/geneontology/go-annotation/issues/2349)).
IPI must not support `GO:0003824` catalytic activity or any is_a descendant
(GORULE:0000007). Enzyme regulator terms are outside that ban; the scope was
narrowed deliberately in [go-annotation#2131](https://github.com/geneontology/go-annotation/issues/2131).
A complex co-precipitated through a tagged or antibody-targeted subunit may be
recorded as IPI with that subunit in WITH/FROM for a `GO:0044877`
protein-containing complex binding term.

**Our sharpening: when IPI may support a non-binding term.** The wiki allows IPI
for any MF (except catalytic) or BP when the gene product "interacts with another
entity that was shown experimentally to be involved in that process." That is
guilt by association, and it reproduces the necessity-versus-participation error
the repository warns against ([CLAUDE.md](../../../CLAUDE.md), "Do not add what
curators deliberately declined to add"). We restrict it. IPI may support:

1. a specific binding term naming the partner class (`GO:0019901` protein kinase
   binding, `GO:0045296` cadherin binding);
2. a complex term, when the interaction is the evidence of membership;
3. a regulator or adaptor MF (`GO:0004860` protein kinase inhibitor activity,
   `GO:0030674` protein-macromolecule adaptor activity) only when the same paper
   also shows the binding changes the partner's activity or bridges two named
   partners (record that assay too, usually as IDA);
4. a BP term only as part of a set: the interaction plus an IMP or IDA in the same
   paper that places the gene product's own activity in the process.

A co-immunoprecipitation with a process component, alone, supports at most the
specific binding term.

*Examples.* ZBP1 has an IPI row from [PMID:19590578](https://europepmc.org/article/MED/19590578)
whose WITH/FROM is UniProtKB:Q13601 (KRR1, a ribosome biogenesis factor); the
partner in the paper is RIPK1 (Q13546). GRID1 has two IPI rows with
UniProtKB:P68871, haemoglobin beta, a classic affinity-purification contaminant
([MISCITATIONS](../../MISCITATIONS.md)). In both, the reference is sound and the
WITH/FROM is wrong. Record such rows as source defects (`defect_type: WRONG_WITH_FROM`, see
[source defects](../../../docs/source_defects.md)), not as reference problems.

Bare `GO:0005515` protein binding from IPI is uninformative. The repository policy
removes it, or modifies it to a specific term the paper supports
(`src/ai_gene_review/validation/protein_binding_policy.py`). The wiki's
requirement for a reciprocal protein-binding row on the partner predates that
policy and should not drive new curation.

Provenance: [GOC] for the WITH/FROM and catalytic rules
([wiki: IPI](https://wiki.geneontology.org/index.php/Inferred_from_Physical_Interaction_%28IPI%29),
[go-annotation#2131](https://github.com/geneontology/go-annotation/issues/2131));
[NEW] for the restriction on non-binding terms.

<a id="ev-4"></a>

### EV-4. Use IMP when the inference rests on comparing alleles, or perturbed and unperturbed states, of one gene.

IMP (ECO:0000315) covers mutations, natural variants, RNAi, morpholinos, CRISPR
alleles, antibody depletion, and inhibitors or conditions that perturb the gene
product, including overexpression when the resulting phenotype is used to infer
normal function. siRNA knockdown is IMP; the more specific ECO:0000019 (RNAi
evidence) maps to it ([go-annotation#1407](https://github.com/geneontology/go-annotation/issues/1407)).
Rescue of a mutant by the same gene strengthens the IMP; it is not IGI. Put the
allele or reagent identifier in WITH/FROM when one exists.

Two cautions apply. Gain-of-function alleles seldom reveal normal function. And
small-molecule inhibitors are only as specific as the drug: the wiki's own
example, baicalein inhibiting 12-LOX and reducing proliferation, supports at most a
non-core `acts_upstream_of_or_within` process row, because the readout is a
convergent phenotype ([from-paper-to-annotation LIT-8](from-paper-to-annotation.md#lit-8)).

IMP may support an MF only with supporting molecular evidence. A loss of activity
in a knockout lysate shows the gene is necessary for the activity, not that its
product carries it; an active-site point mutant that abolishes activity in
purified protein is a different and much stronger observation (it is also IDA).
The PAINT review of TMX3 ([go-annotation#4697](https://github.com/geneontology/go-annotation/issues/4697))
records the consensus that an MF "shouldn't be MF by IMP unless there is
additional supporting evidence", and that IDA is over-used by curators who are
persuaded by a paper whatever its method.

Provenance: [GOC] [wiki: IMP](https://wiki.geneontology.org/index.php/Inferred_from_Mutant_Phenotype_%28IMP%29);
[GOC+] for the MF restriction.

<a id="ev-5"></a>

### EV-5. Use IGI when the inference depends on perturbing two or more genes; put the other gene in WITH/FROM; annotate only the gene whose role the experiment informs.

IGI (ECO:0000316) covers suppression, enhancement and synthetic interactions,
co-transfection of two gene products to test their joint function, and
complementation of a mutation in one gene by expression of another, including
cross-species complementation. The deciding question is the point of reference:
one perturbation against control is IMP; the effect of a second perturbation is IGI
([wiki: IGI](https://wiki.geneontology.org/index.php/Inferred_from_Genetic_Interaction_%28IGI%29)).
For complementation, WITH/FROM holds the endogenous gene that was complemented,
which may be in another species (lgg-1 complementing yeast atg8Δ).

Three cases are not IGI. Rescue by the same gene is IMP. A miRNA repressing a
3′UTR reporter is IDA, because the target's expression is read without perturbing
it. A mutation in gene A that changes gene B's localisation or activity is an IMP
annotation **to gene A**, with gene B in an extension
(`transports_or_maintains_localization_of`, `has_input`).

The wiki IMP page also says that when "a mutation in gene A provides information
about gene B being annotated", IGI is used. That sentence contradicts the IGI
page, and the 2015 discussion in [go-annotation#1327](https://github.com/geneontology/go-annotation/issues/1327)
shows curators reading the two pages in opposite directions. We resolve it this
way: a single perturbation of gene A never supports an annotation to gene B.
Either gene B was also perturbed (IGI, B annotated with A in WITH/FROM) or it was
not, and then gene A is annotated (IMP with an extension naming B).

*Example.* GSK3B antagonists cause nuclear accumulation of GATA6: GSK3B gets
`GO:1900181` negative regulation of protein localization to nucleus, IMP, with
GATA6 in the extension. GATA6 gets nothing from this experiment.

Provenance: [GOC] [wiki: IGI](https://wiki.geneontology.org/index.php/Inferred_from_Genetic_Interaction_%28IGI%29);
[GOC+] for resolving the A/B contradiction.

<a id="ev-6"></a>

### EV-6. Use IEP only for biological process terms, only from normal expression, and only when the gene product's job is the response itself.

IEP (ECO:0000270) infers involvement in a process from the timing or place of the
gene's own expression. GORULE:0000006 restricts it to BP. Overexpression and
ectopic expression are never IEP; they are IDA or IMP. The wiki asks for high-level
terms and warns "Use this code with caution!"; the [GO best-practices paper](https://europepmc.org/article/MED/23842463)
says "response to" terms are for products "required for the response to occur."

The [IEP project](../../IEP.md) found that reviewers accepted only 22.5% of IEP
rows and kept 55.6% as non-core. The characteristic row is true but peripheral.
We therefore make the agency test explicit: *does the gene product exist for this
process, or is its abundance modulated by it?*

- **Annotate (core is fine):** effectors whose deployment is the response:
  heat-shock chaperones to `GO:0009408` response to heat (worm/hsp-16.2,
  ECOLI/DnaK); infection-induced immune effectors; clock components whose
  oscillating expression is the mechanism.
- **Annotate as non-core, or not at all:** constitutive enzymes induced by many
  insults. rat/Gstt1 collected four `response to X` terms from four induction
  papers for one glutathione transferase; the informative row is
  `GO:0009410` response to xenobiotic stimulus once, not the catalogue.
- **Do not annotate:** developmental time-courses read as tissue-building roles
  (rat/Ckmt2 rising after birth does not make creatine kinase part of
  `GO:0007507` heart development); regulon membership (ECOLI/arnF is induced by
  iron through BasS-BasR but does not handle iron); a signalling hub annotated as
  a responder to each stimulus it drives (ARATH/PIF3); one differential screen
  yielding one term for N genes ([PMID:21492153](https://europepmc.org/article/MED/21492153)
  gave eight unrelated genes `GO:0030855` epithelial cell differentiation).

When reviewing, keep the induction observation and judge the term: the usual
action is KEEP_AS_NON_CORE or MARK_AS_OVER_ANNOTATED, with REMOVE reserved for a
process of a different functional class. The wiki's own example of primate
IRF2BPL annotated to "development of secondary female sexual characteristics" from
pubertal induction would fail our agency test unless the activation data the wiki
mentions are annotated in their own right.

Provenance: [GOC] for the BP and normal-expression restrictions
([wiki: IEP](https://wiki.geneontology.org/index.php/Inferred_from_Expression_Pattern_%28IEP%29), GORULE:0000006);
[GOC+] for the agency test ([IEP](../../IEP.md); [go-annotation#2025](https://github.com/geneontology/go-annotation/issues/2025)).

<a id="ev-7"></a>

### EV-7. Classify a paper as high-throughput by how it was done, not by how many genes it names; then hold its annotations to the low-throughput standard.

The HTP family (HTP ECO:0006056; HDA ECO:0007005; HMP ECO:0007001; HGI
ECO:0007003; HEP ECO:0007007) maps one-to-one onto EXP, IDA, IMP, IGI and IEP.
There is no HTP equivalent of IPI; large interaction datasets go to IntAct. A study
is HTP when it applies one workflow to many genes in parallel, without explicit
target selection, produces tabular datasets expected to contain false positives,
and assigns the same property to everything above a threshold. There is no minimum
size, and a large hypothesis-driven screen that dissects one process may warrant
IMP/IGI ([go-annotation#1390](https://github.com/geneontology/go-annotation/issues/1390),
[go-annotation#1774](https://github.com/geneontology/go-annotation/issues/1774)).
Use HDA/HMP/HGI/HEP rather than the parent HTP.

The same rules apply as at low throughput, so most HTP papers should not be
curated ([wiki: HTP](https://wiki.geneontology.org/index.php/Inferred_from_High_Throughput_Experiment_%28HTP%29);
[PMID:30715275](https://europepmc.org/article/MED/30715275)). Operational criteria:

- **Proteomics (HDA):** peptide FDR below 1%, at least two unique peptides
  (razor peptides do not count), and a purification, not an enrichment, judged by
  multi-step protocols, contaminant assays or multivariate methods such as LOPIT
  ([wiki: HDA](https://wiki.geneontology.org/index.php/Inferred_from_High_Throughput_Direct_Assay_%28HDA%29);
  [go-annotation#1382](https://github.com/geneontology/go-annotation/issues/1382)).
- **Localisation screens (HDA):** annotate; tagged-protein screens are among the
  most reliable HTP sources (63-89% accepted in the [omics project](../../OMICS_EVIDENCE.md)).
- **RNAi and mutant screens (HMP/HGI):** never annotate the primary screen. Annotate
  validated hits; hits confirmed by low-throughput work in the same paper get IMP
  as well as HMP ([go-annotation#1839](https://github.com/geneontology/go-annotation/issues/1839)).
- **Expression profiling (HEP):** as for IEP, BP only and rarely.

**Our sharpening: judge the use, not the code.** The [omics project](../../OMICS_EVIDENCE.md)
shows that what predicts whether an omics row holds up is how the data were used:

| Use of the data | Verdict |
|---|---|
| fraction or tagged localisation → location | usually sound |
| vesicle or body-fluid proteome → `GO:0070062` extracellular exosome | true but almost never informative; keep as non-core unless the protein is a vesicle component |
| membrane-fraction proteome → `GO:0016020` membrane | soluble contaminants plus an uninformative term; prefer a specific membrane or none |
| assay of the activity itself (RNA crosslinking, activity probes) → MF | sound; check abundant-protein carry-over |
| co-location or proximity labelling → MF ("found with X, so binds X") | unreliable: E-cadherin proximity labelling produced `GO:0045296` cadherin binding for 255 genes, 2 of 50 accepted |
| differential abundance → process, coded HDA | wrong code (it is HEP at most) and wrong inference: 0 of 9 accepted |

Provenance: [GOC] for the definitions and criteria; [GOC+] for the use-based
review table ([OMICS_EVIDENCE](../../OMICS_EVIDENCE.md)).

<a id="ev-8"></a>

### EV-8. Use ISS, ISO, ISA or ISM only after a curator has reviewed the inference; name the experimentally supported donor or the model in WITH/FROM.

The similarity codes record manual sequence-based inference. ISS (ECO:0000250) is
the umbrella when several methods were combined; ISO (ECO:0000266) when the donor
is an established ortholog; ISA (ECO:0000247) for a reviewed alignment; ISM
(ECO:0000255) for a match to a sequence model (Pfam, TIGRFAM, Rfam, TMHMM). If any
step of a bulk transfer is unreviewed, the code is IEA. WITH/FROM is mandatory for
ISS, ISO and ISA; for ISM it holds the model accession when one exists.

Donor requirements:

- A gene-product donor must carry the same or a more specific term with
  experimental evidence (GORULE:0000038). The wiki also accepts IC on the donor; we
  accept it only when that IC itself rests on an experimental annotation of the
  donor, so that no chain is a transfer of a transfer.
- For ISO, list every paralog when the target is co-orthologous to several genes,
  and revisit the annotation when orthology calls change.
- HTP-supported donors are allowed, with case-by-case review
  ([go-annotation#1775](https://github.com/geneontology/go-annotation/issues/1775)).
- Antibody cross-reactivity is not sequence similarity
  ([go-annotation#11](https://github.com/geneontology/go-annotation/issues/11)).
- No ISS-family annotation to `GO:0005515` protein binding (GORULE:0000005).

When reviewing an ISO row, ask three separate questions ([ISO](../../ISO.md)): is
the donor annotation still present and experimental; is the donor the target's
ortholog rather than a paralog or one of a one-to-many set; and is the term safe
to move (conserved biochemistry usually is; tissue, developmental and regulatory
context often is not)? Record the answer in `review.propagation_review`. Mouse Ang2
shows the paralog failure: all its ISO rows come from human ANG, but Ang2 is a
divergent member of an expanded family, and 41 of 46 rows were removed.

Provenance: [GOC] ([wiki: ISS](https://wiki.geneontology.org/index.php/Inferred_from_Sequence_or_structural_Similarity_%28ISS%29),
[wiki: ISO](https://wiki.geneontology.org/index.php/Inferred_from_Sequence_Orthology_%28ISO%29),
[wiki: ISA](https://wiki.geneontology.org/index.php/Inferred_from_Sequence_Alignment_%28ISA%29),
[wiki: ISM](https://wiki.geneontology.org/index.php/Inferred_from_Sequence_Model_%28ISM%29));
[GOC+] for the donor-chain restriction and the three-question review.

<a id="ev-9"></a>

### EV-9. Treat the phylogenetic codes as a PAINT curator's node judgement; challenge the node placement, not the donor count.

IBA (ECO:0000318) rows follow mechanically from a PAINT curator's IBD
(ECO:0000319) placed on an ancestral PANTHER node after reading the family's
experimental annotations. IKR (ECO:0000320) records loss of key residues and
produces NOT rows; IRD (ECO:0000321) records rapid divergence, sits only on
internal nodes, and blocks descent without producing any gene-level NOT
([IRD_EVIDENCE](../../IRD_EVIDENCE.md)). A short donor list is not weak support,
and a target that appears among the sources of its own IBA has experimental
grounding of its own; neither is circularity. Full treatment, including a 2018
GOC thread that called such rows "self-referential", is in
[phylogenetic-propagation.md](phylogenetic-propagation.md).

Provenance: [GOC] ([PMID:21873635](https://europepmc.org/article/MED/21873635));
[GOC+] for the review stance ([CLAUDE.md](../../../CLAUDE.md), [IBA_REVIEW](../../IBA_REVIEW.md)).

<a id="ev-10"></a>

### EV-10. Use TAS only when the cited source is traceable and you cannot annotate from the primary paper; a textbook or "common knowledge" is not traceable.

TAS (ECO:0000304) records an author's statement attributed to a cited primary
source, usually in a review or in a primary paper's introduction. The wiki asks
curators to track down and annotate the cited experiment when they can, because
reviews often cite work done in another organism. Since the 2006 annotation camp,
textbook knowledge is not TAS. Reactome events enter GOA as TAS; check each against
the gene product that actually executes the reaction ([REACTOME](../../REACTOME.md)).
A P2X1 event supporting a P2X7 location is a typical failure
([MISCITATIONS](../../MISCITATIONS.md)).

Producing versus reviewing. The wiki recommends removing a TAS row once an
experimental row exists for the same term. That is advice for producers about
redundancy. A reviewer does not REMOVE a TAS row because an experimental row
covers the same term; rows sharing a term must get consistent actions, and REMOVE
is never a deduplication tool ([action consistency](../../../docs/action_consistency.md)).
REMOVE a TAS row only when its claim is wrong or its source does not support it.

Provenance: [GOC] [wiki: TAS](https://wiki.geneontology.org/index.php/Traceable_Author_Statement_%28TAS%29);
[NEW] for the reviewer stance.

<a id="ev-11"></a>

### EV-11. Use NAS only for an author's assertion, not for their speculation.

NAS (ECO:0000303) records a statement with neither results nor a citation behind
it, including uncited database records. The wiki permits it whenever "the author
makes a statement that a curator wants to capture." We add a test: the statement
must be asserted as fact. Hedged discussion ("may", "possibly", "could be
important for") is speculation and is not annotatable. In [go-annotation#1381](https://github.com/geneontology/go-annotation/issues/1381)
a NAS to `GO:0016226` iron-sulfur cluster assembly for SDHAF1 rested on a
discussion sentence saying the protein "possibly" acts in Fe-S insertion; the
original curator agreed and deleted it.

The wiki's NAS example is itself inconsistent: it quotes a sentence about predicted
nuclear localisation and then annotates CELF3 to pre-mRNA binding (the page is
marked "NEEDS REVIEW"). An author stating that something is unknown is ND, not NAS
or TAS ([go-annotation#170](https://github.com/geneontology/go-annotation/issues/170)).

Provenance: [GOC] [wiki: NAS](https://wiki.geneontology.org/index.php/Non-traceable_Author_Statement_%28NAS%29);
[GOC+] for the speculation test.

<a id="ev-12"></a>

### EV-12. Use IC only for a one-step inference from another annotation on the same gene product; put the GO id of that annotation in WITH/FROM.

IC (ECO:0000305) is legitimate when a term follows from an evidenced annotation
plus general biological knowledge, and no direct evidence exists. The canonical
case: a yeast protein with RNA polymerase II DNA-binding transcription factor
activity is in the nucleus. WITH/FROM must hold the supporting GO id; several ids
joined by commas mean AND and by pipes OR, and multi-source IC uses
GO_REF:0000036 ([wiki: IC](https://wiki.geneontology.org/index.php/Inferred_by_Curator_%28IC%29)).

IC is not legitimate for:

- computational predictions. CAFA-derived IC rows put ribosomal proteins in
  ribosome assembly from a proteomics quantification, and were withdrawn
  ([go-annotation#1626](https://github.com/geneontology/go-annotation/issues/1626));
- homology (use the ISS family);
- necessity reasoning ("the knockout lacks X, so the gene is involved in X");
- chains of more than one inference, or inferences from annotations on other genes.

In this repository, a reviewer authoring a `NEW` row from several independent
lines (a transmembrane segment, a cleavable presequence, an organelle assay) uses
IC with the root-organelle annotation in WITH/FROM and states each line in
`reason` ([ORGANELLES](../../ORGANELLES.md)). When a single paper shows the
location and sequence analysis resolves the topology, GOC practice since 2016 is
IDA from that paper ([wiki: Transmembrane proteins](https://wiki.geneontology.org/index.php/Transmembrane_Proteins);
[go-annotation#1621](https://github.com/geneontology/go-annotation/issues/1621)).

Provenance: [GOC] for the definition and WITH/FROM; [GOC+] for the exclusions.

<a id="ev-13"></a>

### EV-13. ND says a curator searched the literature for one aspect and found nothing; accept it when that is still true, whatever inferred rows exist.

ND (ECO:0000307) goes only on the three roots, `GO:0003674` molecular_function,
`GO:0008150` biological_process and `GO:0005575` cellular_component
(GORULE:0000011), with GO_REF:0000015 and no WITH/FROM. It is per aspect and dated.
Cloning, disease-association and biomarker papers do not count as data, so they
leave an ND standing ([wiki: ND](https://wiki.geneontology.org/index.php/No_biological_Data_available_%28ND%29_evidence_code)).
A NOT annotation needs a positive annotation in the same aspect, which may be the
ND root.

The review test ([NO_DATA](../../NO_DATA.md); [CLAUDE.md](../../../CLAUDE.md)):
is there literature on **this gene product, in this species**, that identifies a
function in **this aspect**? If not, ACCEPT, and cite the search (PMIDs checked, or
a quote from the deep-research or notes file recording the queries). IBA, ISO, ISS
and IEA rows in the same aspect are not literature on the gene and do not make the
ND stale. A bare protein-binding IPI does not either; an NAS or Reactome TAS row on
the gene does. If such literature exists, REMOVE (or MODIFY when no term fitted)
with `nd_case: STALE` or `ONTOLOGY_BLOCKED`, quoting the paper. Never use
KEEP_AS_NON_CORE, MARK_AS_OVER_ANNOTATED or TOO_GENERAL on an ND, and never propose
a NEW ND.

*Examples.* CANAL/LPL1: ND for MF next to an IBA phospholipase B row. ACCEPT; the
IBA carries the function. yeast/MDM10: an ND for MF dated 2022 sits beside an IDA
for ER-mitochondrion tethering. REMOVE as stale.

Provenance: [GOC] for the definition; [GOC+] for the acceptance rule, which departs
from the 2018 GOA proposal to delete NDs automatically when ISS or IGC rows exist
([go-annotation#2045](https://github.com/geneontology/go-annotation/issues/2045)).

<a id="ev-14"></a>

### EV-14. Use RCA and IEA only for what they define; do not recode reviewed work as IEA or unreviewed predictions as anything else.

RCA (ECO:0000245, now labelled "automatically integrated combinatorial evidence
used in manual assertion") is for curator-reviewed predictions from computational
analysis of large experimental datasets. It is not for sequence-only inference
(ISS family) or for a single experiment (use its code). Its use for function
predictions was judged a misuse in [go-annotation#1801](https://github.com/geneontology/go-annotation/issues/1801),
and NOT rows derived from a protein's absence from a fraction's reported set are not
negative evidence ([OMICS_EVIDENCE](../../OMICS_EVIDENCE.md)). IEA (ECO:0000501) is for
unreviewed pipeline output and needs a GO_REF and a WITH/FROM naming the mapping or
model; see [electronic-annotation.md](electronic-annotation.md).

The 2025 [Tips page](https://wiki.geneontology.org/index.php/Tips_to_Produce_High_Quality_Annotations)
adds a rule for AI-assisted curation: an association an AI tool suggests from
experimental data, once a trained curator has confirmed it against the paper, takes
the experimental code of the experiment. In this repository that confirmation is a
verbatim `supporting_text` from the paper, checked by the validator.

Provenance: [GOC] ([wiki: RCA](https://wiki.geneontology.org/index.php/Inferred_from_Reviewed_Computational_Analysis_%28RCA%29),
[wiki: IEA](https://wiki.geneontology.org/index.php/Inferred_from_Electronic_Annotation_%28IEA%29),
[wiki: Tips](https://wiki.geneontology.org/index.php/Tips_to_Produce_High_Quality_Annotations)).

<a id="ev-15"></a>

### EV-15. Read the ECO class, not only the GAF code.

Choose the ECO class by the method, then check what GAF code it projects to. When
reviewing, read the ECO id in the GOA row before judging the code. Known projection
artefacts:

| ECO class | Projects to | Problem | Correct reading |
|---|---|---|---|
| ECO:0000279 qualitative western immunoblotting evidence used in manual assertion | IEP (via ECO:0000284) | 1,110 of 1,147 CC rows violating GORULE:0000006 in GOA; mostly SynGO synaptosome or PSD fractions | a localisation assay; IDA ([IEP](../../IEP.md)) |
| ECO:0000282 heterologous protein expression evidence used in manual assertion | IEP | heterologous expression used to assay function is IDA under #6468 | IDA or IMP by intent ([go-annotation#6468](https://github.com/geneontology/go-annotation/issues/6468)) |
| ECO:0007129 chromatin immunoprecipitation-qPCR evidence used in manual assertion | inherits the IPI WITH/FROM requirement | the partner is a DNA region with no stable identifier | a DNA-binding direct assay; do not invent an identifier ([go-annotation#2576](https://github.com/geneontology/go-annotation/issues/2576)) |
| ECO:0000096 electrophoretic mobility shift assay evidence | IPI since 2020 (was IDA) | old and new rows for the same assay carry different codes | treat as one assay type ([go-annotation#2771](https://github.com/geneontology/go-annotation/issues/2771)) |
| ECO:0007744 combinatorial computational and experimental evidence used in manual assertion | no GAF code (2026-11-07) | GOA rows with an empty code | keep the ECO id; do not manufacture a code ([goa-evidence](../../../docs/goa-evidence.md)) |

Provenance: [NEW], built from the cited issues and project audits.

<a id="ev-16"></a>

### EV-16. Several codes from one paper are several annotations; never let a code stand in for a judgement of the claim.

If one paper supports a term by two methods (localisation by immunofluorescence
and by fractionation; an enzyme assay and an active-site mutant), make one row per
method; identical term and reference with different codes is allowed
([evidence guide](https://wiki.geneontology.org/index.php/Guide_to_GO_Evidence_Codes)).
When reviewing, the rows that share a term reinforce each other and their actions
must be consistent; an IEA row and an IDA row for the same correct term are not
treated differently because of the code. Do not REMOVE a row because its code is
weak; REMOVE when its claim is wrong ([CLAUDE.md](../../../CLAUDE.md)). Equally, an
experimental code does not protect a claim the paper does not make: the reviewer
must read what the curator read before overruling it, and use UNDECIDED when the
full text is not available.

Provenance: [GOC] for multiple rows; [GOC+] for the reviewing rule.

## Decision aid

**Choosing a code from an experiment.**

| What the experiment did | Code | WITH/FROM |
|---|---|---|
| Assayed the purified or expressed product's activity | IDA | none |
| Localised the product (antibody, tag, fractionation) | IDA | none |
| Pulled down a complex via a tagged subunit (CC term) | IDA | none |
| Showed binding to an identified molecule | IPI | partner id |
| Showed binding to an unidentifiable partner (DNA region, lipid, F-actin) | IDA | none |
| Compared mutant or knocked-down with wild type (one gene) | IMP | allele or reagent, if any |
| Rescued a mutant with the same gene | IMP | |
| Compared single and double perturbations; complemented gene A's mutant with gene B | IGI | the other gene |
| Overexpressed to assay activity | IDA | none |
| Overexpressed and read a phenotype | IMP | |
| Measured the gene's own normal expression under a condition (BP only) | IEP | none |
| Any of the above in a screen without target selection | HDA / HMP / HGI / HEP | as for the LTP code |
| Curator-reviewed sequence or orthology inference | ISS / ISO / ISA / ISM | donor or model |
| Statement in a review citing primary work | TAS (prefer the primary paper) | none |
| Uncited author assertion | NAS | none |
| One-step inference from another annotation on the same gene | IC | GO id |
| Searched, found nothing (root term only) | ND | none |

**Reviewing a row by code: the first question to ask.**

| Code | First question |
|---|---|
| IDA | Was the assay of the product's own activity or location, or a phenotype coded as IDA? |
| IPI | Is WITH/FROM the partner the paper reports, and is the term a binding or interaction-dependent term? |
| IMP | Is the readout proximal to the term, or a convergent phenotype? Is the term MF? |
| IGI | Which gene was perturbed, and is that the gene annotated? |
| IEP | Does the product exist for this process, or is it induced by it? |
| HDA/HMP/HEP | How were the data used (location, assay, co-location, differential abundance, primary screen)? |
| ISS/ISO | Is the donor still experimental, an ortholog, and is the term safe to move? |
| TAS/NAS | Does the source say this, about this gene, in this species, as an assertion? |
| IC | Is the WITH/FROM annotation real, on the same gene, and is the step one inference? |
| ND | Is there literature on this gene in this species identifying a function in this aspect? |

## Common errors

| Error | Example | Fix |
|---|---|---|
| Phenotype coded IDA | CREG1 endocytosis and autophagy from overexpression and knockdown phenotypes (#6468) | Recode IMP; judge the process term as a phenotype inference |
| Positive row from a negative result | PNPLA3 LPAAT EXP from a paper reporting no activity | MARK_AS_OVER_ANNOTATED; record a `MISSING_NEGATION` source defect |
| Wrong partner in IPI WITH/FROM | ZBP1 with KRR1 for RIPK1; GRID1 with haemoglobin beta | Source defect on the WITH/FROM; judge the binding claim on the real partner |
| IEP stimulus cloud | rat/Gstt1 four `response to X` terms | Keep the parent stimulus term; mark the rest over-annotated or non-core |
| IEP developmental time-course | rat/Ckmt2 `GO:0007507` heart development | MARK_AS_OVER_ANNOTATED |
| Differential proteome coded HDA for a process | `GO:0001649` osteoblast differentiation from PMID:16210410 (42 rows) | It is HEP at most; usually MARK_AS_OVER_ANNOTATED |
| CC rows coded IEP | SynGO western-blot fractions (ECO:0000279) | Read as IDA; review the location on its merits |
| IC for predictions | CAFA ribosome-assembly IC rows (#1626) | REMOVE |
| NAS from speculation | SDHAF1 Fe-S assembly (#1381) | REMOVE |
| ND removed because an IBA exists | 37 reviews in the [NO_DATA](../../NO_DATA.md) inventory | ACCEPT the ND; review the IBA on its own row |
| TAS removed as redundant to an IDA | common in older reviews | Give both rows the same action |
| ISO from a paralog | mouse Ang2 from human ANG | REMOVE with `propagation_review` naming WRONG_ORTHOLOG_OR_PARALOG |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [wiki: IPI](https://wiki.geneontology.org/index.php/Inferred_from_Physical_Interaction_%28IPI%29) | IPI may support any MF except catalytic, or any BP, because the partner is involved | IPI supports binding, complex and (with an activity assay) regulator/adaptor terms; BP only alongside evidence placing the product's own activity in the process (EV-3) | Interaction with a process component shows association, not participation |
| [wiki: IPI](https://wiki.geneontology.org/index.php/Inferred_from_Physical_Interaction_%28IPI%29) | `GO:0005515` must be IPI with a reciprocal annotation | Do not create bare protein-binding rows; MODIFY to a specific term or REMOVE | Repo protein-binding policy; the term carries no functional information |
| [wiki: IMP](https://wiki.geneontology.org/index.php/Inferred_from_Mutant_Phenotype_%28IMP%29) vs [wiki: IGI](https://wiki.geneontology.org/index.php/Inferred_from_Genetic_Interaction_%28IGI%29) | IMP page: gene A's mutation informing gene B is IGI; IGI page: it is IMP on A with an extension | A single perturbation of A never annotates B; annotate A (IMP + extension) or, if B was also perturbed, B by IGI (EV-5) | The two pages contradict each other; #1327 shows curators split |
| [wiki: IDA](https://wiki.geneontology.org/index.php/Inferred_from_Direct_Assay_%28IDA%29) before 2026 | Overexpression "considered to be an assay system" is IDA, including for processes | IDA for activity or location assayed in an expression system; IMP for process inferred from the resulting phenotype (EV-2, EV-4) | Settled in #6468; ECO:0000282 still projects to IEP, which conflicts |
| [wiki: IMP](https://wiki.geneontology.org/index.php/Inferred_from_Mutant_Phenotype_%28IMP%29) | IMP may support function, process or location | IMP supports MF only with molecular corroboration | Necessity of a gene for an activity is not possession of it (#4697) |
| [wiki: IEP](https://wiki.geneontology.org/index.php/Inferred_from_Expression_Pattern_%28IEP%29) | Stage- or organ-selective expression may support "xxx development" | Developmental time-courses do not support tissue-development terms unless the product is the differentiated output | Metabolic demand tracks maturation without an instructive role ([IEP](../../IEP.md)) |
| [wiki: ISS](https://wiki.geneontology.org/index.php/Inferred_from_Sequence_or_structural_Similarity_%28ISS%29) | Donor may have experimental or IC support | IC on the donor counts only if it rests on an experimental annotation of the donor | Prevents transfers of transfers |
| [wiki: TAS](https://wiki.geneontology.org/index.php/Traceable_Author_Statement_%28TAS%29); [Annotation camp](https://wiki.geneontology.org/index.php/Guidelines_from_Annotation_Camp) | Remove TAS/NAS/IC rows once a better-evidenced row exists for the same term | Producers should not create them; reviewers give them the same action as the experimental row and REMOVE only wrong claims | Reviews judge claims, not codes; rows sharing a term must be consistent |
| [wiki: NAS](https://wiki.geneontology.org/index.php/Non-traceable_Author_Statement_%28NAS%29) | Any author statement a curator wants to capture | Assertions only; hedged speculation is not annotatable | #1381; speculation is not a claim |
| [go-annotation#2045](https://github.com/geneontology/go-annotation/issues/2045) (GOA proposal, 2018) | Delete NDs automatically when EXP, HTP, ISS or IGC rows exist in the aspect | ND stands unless literature on this gene in this species identifies a function; ISS/IGC/IBA/IEA do not count | ND records a literature search; inference is not literature ([NO_DATA](../../NO_DATA.md)) |
| [wiki: IC](https://wiki.geneontology.org/index.php/Inferred_by_Curator_%28IC%29); [go-annotation#1621](https://github.com/geneontology/go-annotation/issues/1621) | IC from another annotation; IDA for experiment plus sequence (2016) | Both stand; a reviewer's NEW row synthesised from several lines uses IC with the supporting GO id, while a single paper with location plus topology uses IDA | Distinguishes the producer's paper-based row from the reviewer's synthesis |
| [wiki: HTP family](https://wiki.geneontology.org/index.php/Inferred_from_High_Throughput_Experiment_%28HTP%29) | Quality criteria per assay type | Additionally judge by use: location from fraction is sound; function from co-location is not; vesicle cargo is non-core | Same data, different inference, different reliability ([OMICS_EVIDENCE](../../OMICS_EVIDENCE.md)) |
| [wiki: IEP](https://wiki.geneontology.org/index.php/Inferred_from_Expression_Pattern_%28IEP%29) / GORULE:0000006 | IEP on CC is a curation error | Most CC IEP rows are an ECO:0000279 projection artefact; read them as IDA | ECO multiple parentage ([IEP](../../IEP.md)) |

## Open questions

1. Should the GOC fix ECO-to-GAF projection by aspect (ECO:0000279 to IDA for CC),
   or re-parent ECO:0000279 and ECO:0000282? Either clears about 1,100 GORULE:0000006
   violations without curation.
2. Should IPI to non-binding terms be formally restricted (EV-3), and should
   GORULE:0000007's catalytic ban extend to transporter activity, where binding is
   equally uninformative about transport?
3. A DNA-binding ChIP assay has no stable partner identifier. Should the IPI
   WITH/FROM requirement be dropped for ECO classes whose partner is a genomic
   region (#2576)?
4. "Response to" terms conflate "acts in the response" with "is induced during
   it." Would a qualifier or extension distinguishing them let IEP rows coexist
   with agency claims ([IEP](../../IEP.md) recommendation 5)?
5. There is no way in this repository to propose an evidence-code upgrade (right
   term, IEA only, but species IDA exists): NEW is rejected for a term already in
   GOA. This matters most for all-electronic species.
6. Should HTP rows be excluded from IBD seeding by default, given #1775 allows them
   as ISS donors?

## Sources

**GO wiki (evidence codes):**
[Guide to GO evidence codes](https://wiki.geneontology.org/index.php/Guide_to_GO_Evidence_Codes) ·
[EXP](https://wiki.geneontology.org/index.php/Inferred_from_Experiment_%28EXP%29) ·
[IDA](https://wiki.geneontology.org/index.php/Inferred_from_Direct_Assay_%28IDA%29) ·
[IPI](https://wiki.geneontology.org/index.php/Inferred_from_Physical_Interaction_%28IPI%29) ·
[IMP](https://wiki.geneontology.org/index.php/Inferred_from_Mutant_Phenotype_%28IMP%29) ·
[IGI](https://wiki.geneontology.org/index.php/Inferred_from_Genetic_Interaction_%28IGI%29) ·
[IEP](https://wiki.geneontology.org/index.php/Inferred_from_Expression_Pattern_%28IEP%29) ·
[HTP](https://wiki.geneontology.org/index.php/Inferred_from_High_Throughput_Experiment_%28HTP%29) ·
[HDA](https://wiki.geneontology.org/index.php/Inferred_from_High_Throughput_Direct_Assay_%28HDA%29) ·
[HMP](https://wiki.geneontology.org/index.php/Inferred_from_High_Throughput_Mutant_Phenotype_%28HMP%29) ·
[HEP](https://wiki.geneontology.org/index.php/Inferred_from_High_Throughput_Expression_Pattern_%28HEP%29) ·
[HGI](https://wiki.geneontology.org/index.php/Inferred_from_High_Throughput_Genetic_Interaction_%28HGI%29) ·
[ISS](https://wiki.geneontology.org/index.php/Inferred_from_Sequence_or_structural_Similarity_%28ISS%29) ·
[ISO](https://wiki.geneontology.org/index.php/Inferred_from_Sequence_Orthology_%28ISO%29) ·
[ISA](https://wiki.geneontology.org/index.php/Inferred_from_Sequence_Alignment_%28ISA%29) ·
[ISM](https://wiki.geneontology.org/index.php/Inferred_from_Sequence_Model_%28ISM%29) ·
[IGC](https://wiki.geneontology.org/index.php/Inferred_from_Genomic_Context_%28IGC%29) ·
[TAS](https://wiki.geneontology.org/index.php/Traceable_Author_Statement_%28TAS%29) ·
[NAS](https://wiki.geneontology.org/index.php/Non-traceable_Author_Statement_%28NAS%29) ·
[IC](https://wiki.geneontology.org/index.php/Inferred_by_Curator_%28IC%29) ·
[ND](https://wiki.geneontology.org/index.php/No_biological_Data_available_%28ND%29_evidence_code) ·
[RCA](https://wiki.geneontology.org/index.php/Inferred_from_Reviewed_Computational_Analysis_%28RCA%29) ·
[IEA](https://wiki.geneontology.org/index.php/Inferred_from_Electronic_Annotation_%28IEA%29)

**GO wiki (other):**
[Tips to produce high quality annotations](https://wiki.geneontology.org/index.php/Tips_to_Produce_High_Quality_Annotations) (reviewed 2025) ·
[Transmembrane proteins](https://wiki.geneontology.org/index.php/Transmembrane_Proteins) (refers to the obsolete integral-to-membrane terms) ·
[Guidelines from annotation camp](https://wiki.geneontology.org/index.php/Guidelines_from_Annotation_Camp) (historical, c. 2007-2010)

**go-annotation issues:**
[#11](https://github.com/geneontology/go-annotation/issues/11) antibody cross-reactivity is not ISS ·
[#170](https://github.com/geneontology/go-annotation/issues/170) ND vs TAS/NAS for "unknown" ·
[#1327](https://github.com/geneontology/go-annotation/issues/1327) IGI vs IMP wording ·
[#1381](https://github.com/geneontology/go-annotation/issues/1381) NAS from speculation ·
[#1382](https://github.com/geneontology/go-annotation/issues/1382) HTP proteomics criteria applied ·
[#1390](https://github.com/geneontology/go-annotation/issues/1390) what counts as HTP ·
[#1407](https://github.com/geneontology/go-annotation/issues/1407) siRNA is IMP ·
[#1621](https://github.com/geneontology/go-annotation/issues/1621) IDA for experiment plus sequence ·
[#1626](https://github.com/geneontology/go-annotation/issues/1626) no IC for predictions ·
[#1774](https://github.com/geneontology/go-annotation/issues/1774) large screens need case-by-case review ·
[#1775](https://github.com/geneontology/go-annotation/issues/1775) HTP as a propagation source ·
[#1801](https://github.com/geneontology/go-annotation/issues/1801) RCA review ·
[#1839](https://github.com/geneontology/go-annotation/issues/1839) RNAi screen: IMP for validated, HMP otherwise ·
[#2025](https://github.com/geneontology/go-annotation/issues/2025) IEP and ND conflicts ·
[#2045](https://github.com/geneontology/go-annotation/issues/2045) proposed automatic ND deletion ·
[#2131](https://github.com/geneontology/go-annotation/issues/2131) GORULE:0000007 ·
[#2349](https://github.com/geneontology/go-annotation/issues/2349) comma vs pipe in WITH/FROM ·
[#2576](https://github.com/geneontology/go-annotation/issues/2576) ChIP-qPCR ECO and WITH/FROM ·
[#2771](https://github.com/geneontology/go-annotation/issues/2771) EMSA moved to IPI ·
[#4697](https://github.com/geneontology/go-annotation/issues/4697) MF by IMP; IDA over-use ·
[#6468](https://github.com/geneontology/go-annotation/issues/6468) IDA vs IMP for overexpression (2026)

**Papers:**
[PMID:23842463](https://europepmc.org/article/MED/23842463) GO best practices ·
[PMID:30715275](https://europepmc.org/article/MED/30715275) annotation of high-throughput studies ·
[PMID:21873635](https://europepmc.org/article/MED/21873635) PAINT ·
[PMID:21878620](https://europepmc.org/article/MED/21878620) PNPLA3 enzymology ·
[PMID:19590578](https://europepmc.org/article/MED/19590578) ZBP1 interaction ·
[PMID:21492153](https://europepmc.org/article/MED/21492153) Caco-2 differentiation proteome ·
[PMID:21900231](https://europepmc.org/article/MED/21900231) NAA50 structure and activity

**Repository:**
[CLAUDE.md](../../../CLAUDE.md) ·
[action consistency](../../../docs/action_consistency.md) ·
[goa-evidence](../../../docs/goa-evidence.md) ·
[source defects](../../../docs/source_defects.md) ·
[IEP](../../IEP.md) ·
[ISO](../../ISO.md) ·
[IRD_EVIDENCE](../../IRD_EVIDENCE.md) ·
[IBA_REVIEW](../../IBA_REVIEW.md) ·
[OMICS_EVIDENCE](../../OMICS_EVIDENCE.md) ·
[NO_DATA](../../NO_DATA.md) ·
[MISCITATIONS](../../MISCITATIONS.md) ·
[ORGANELLES](../../ORGANELLES.md) ·
[REACTOME](../../REACTOME.md)
