# Regulation and signalling: GO annotation guidelines

Status: draft v0.1 (2026-11-15) · Part of [GO_GUIDELINES](../../GO_GUIDELINES.md)

**In brief:**

- "Regulation of X" means the gene product's activity sits outside X and changes whether, how often, how fast or how much X happens. If you cannot name the X participant (or the step) that it acts on, the claim is an upstream effect. Annotate it under [BP-4](biological-process.md#bp-4).
- Pathway members that activate the next step are part of the pathway, not its regulators. Limiting quantities, constitutive prerequisites and substrate supply are not regulation.
- Sign is judged in vivo, from the gene product's effect rather than the mutant's phenotype. A wrong sign is a contradiction to correct, not an imprecision to tolerate.
- A signalling pathway runs from ligand–receptor engagement to the last effector, often a transcription factor. The ligand, the receptor, the transducers and that effector are in it. Target genes and the downstream cellular process are not.
- Regulation does not cross transcription. A component of pathway A that changes transcription of pathway B's genes is not a regulator of pathway B.
- "Response to X" is for gene products that detect X, transduce it, or carry out a response specific to it. A change in expression after X is IEP evidence of a peripheral role at most, and usually non-core.

## Scope

This document covers:

- regulation terms ("regulation of", "positive regulation of", "negative regulation of" a process), including their sign and directness;
- the boundary between being part of a process and regulating it;
- signalling pathway annotation: ligands, receptors, transducers, intracellular cassettes, second messengers and pathway ends;
- "response to" terms, cellular versus organism-level responses, and IEP-based annotation.

Related documents:

- The general participation test (`involved_in` versus `acts upstream of`) is in [biological-process.md](biological-process.md).
- Transcription regulation, DNA-binding transcription factor activity and target genes are in [transcription-regulation.md](transcription-regulation.md).
- The MF side of regulators (enzyme regulator, molecular adaptor, receptor ligand activity) is in [molecular-function.md](MF/README.md).
- GO-CAM causal relations (`directly positively regulates`, `constitutively upstream of`, `removes input for`) are in [gocam-modeling.md](gocam-modeling.md).
- Evidence codes, including IEP, are in [evidence-codes.md](evidence-codes.md).

## Principles

**Regulation is a relation between activities, read at the process level.** GO defines process P1 as regulating P2 if P1 starts or stops P2, changes the frequency of its starting or stopping, or changes the rate or extent of its output ([wiki: Annotating from phenotypes](https://wiki.geneontology.org/index.php/Annotating_from_phenotypes)). For a gene product, "involved in regulation of P2" therefore means: the gene product's activity acts on an activity that is part of P2. The phenotype guideline states the evidential bar. There "should be evidence that the MF of the gene product being annotated *regulates* an MF of a gene that is *involved in* the process" (same page).

**Every process has a start, a middle and an end.** Whether a gene product is in a process or regulating it depends on where the process boundaries are drawn. Signalling pathways have the clearest boundaries, and organism-level processes the vaguest ([wiki: Annotating regulation](https://wiki.geneontology.org/index.php/Annotating_regulation)). When the boundaries are vague, the safe annotation is the process itself with an upstream relation, not a regulation term.

**Regulation is conditional and specific.** A regulator changes an activity in response to something, and it targets particular activities. A housekeeping requirement does neither ([Drive: MF-MF relations abstract, ISB 2023](https://drive.google.com/open?id=1r-tnt3Jk7H4Sb3xzIbx7ODVGCUbbyh9uyxPN1JhUK-M); [Drive: FlyBase pathway curation guide](https://drive.google.com/open?id=1Toyf0QhDjuGMYa1KyDGF-T9qXnXfvxAuYisLpAxfZoI)).

**Abundance change is not activity.** A transcript that rises after a stimulus says the gene is regulated by the response. It does not say the gene product takes part in it ([IEP](../../IEP.md)).

## Rules

<a id="rs-1"></a>

### RS-1. Decide between "part of X" and "regulation of X" by locating the gene product's activity relative to the process boundaries

**Statement.** First establish where X starts and ends: from the term definition, a GO-CAM, or a current review of the pathway. If the gene product performs one of the activities between the start and the end, it is `involved_in` X. If it acts from outside X to start, stop or modulate it, it is `involved_in` regulation of X. If you cannot tell, annotate X with `acts upstream of or within` and a sign.

**Rationale.** These are Guidelines 1 and 2 of [wiki: Annotating regulation](https://wiki.geneontology.org/index.php/Annotating_regulation), restated at the 2022 GOC breakout ([Drive: Breakout – Annotating to a process or its regulation, 2022](https://drive.google.com/open?id=1ii8kFkraHYYSGThmYZq9i6EyqNmY4v91hpGuuvIMunk)). The 2017 decision that "gene product involved_in X regulation" uses the plain `involved_in` relation, rather than a separate `regulates` relation, makes the term carry the regulation ([go-annotation#1687](https://github.com/geneontology/go-annotation/issues/1687)).

**Worked example.** Yeast Atg1 is a protein kinase needed to form autophagic vesicles. Authors' language could support either autophagosome formation or its regulation. SGD annotated Atg1 to the process because, once Atg1 is active, the decision to proceed with autophagy has already been taken. The genes upstream of that decision regulate the pathway ([wiki: Annotating regulation](https://wiki.geneontology.org/index.php/Annotating_regulation)).

**Provenance.** [GOC].

<a id="rs-2"></a>

### RS-2. Annotate regulation of X only when the gene product modulates X, and name the target

**Statement.** A regulation annotation needs evidence that the gene product's activity changes the activity, amount or location of a specific participant of X, or changes when X starts or stops. Record the participant when known: `has_input` on the BP annotation, or the regulated gene product in a GO-CAM. A perturbation that changes the outcome of X, with no target, does not support a regulation term. It supports `acts upstream of or within, positive/negative effect` X (BP-4).

**Rationale.** The phenotype guideline asks for MF-level evidence and says mutant phenotypes "more often provide supporting, rather than definitive" evidence for regulation ([wiki: Annotating from phenotypes](https://wiki.geneontology.org/index.php/Annotating_from_phenotypes)). Curators in [go-annotation#2570](https://github.com/geneontology/go-annotation/issues/2570) argued that regulation terms should require mechanistic evidence of control. In the 2022 PomBase breakdown of 922 "regulation of biological process" annotations, nearly all valid cases fell into two mechanisms, signalling and regulation of gene expression. The remainder were mostly ontology or annotation errors ([Drive: 2022 questions about regulation](https://drive.google.com/open?id=1J_WpQPSyn4wvsMtxEAG4d7xA4SLmA0m2)). The 2020 GO-CAM jamboree gave three patterns for a regulatory link between activities. The first is a direct state change of a successive activity of another gene product (MAPKK to MAPK). The second is a binding activity that switches on another activity of the same product. The third is a specificity factor that controls the amount of the downstream product (a transcription factor and its target, a miRNA and its mRNA). Enzymes that modify a protein only as part of its trafficking were excluded ([Drive: GO-CAM Jamboree 2020 – Regulation notes](https://drive.google.com/open?id=1mAIocbi6UvG_zbfCrWOUrneia3vl2XkjVPM39tmSx40)). The extension relation for the regulated entity is now `has_input`; `has_regulation_target` was retired for it, although PomBase keeps a local display label ([go-annotation#2587](https://github.com/geneontology/go-annotation/issues/2587)).

**Worked examples.**

- Human cGAS enables GO:0061501 2',3'-cyclic GMP-AMP synthase activity. Its product, cGAMP, activates STING1. The 2018 review found that cGAS should not be annotated as a regulator of the viral life cycle, because the cyclic nucleotide does the regulating and the enzyme acts upstream of it ([go-annotation#1979](https://github.com/geneontology/go-annotation/issues/1979)). With the current ontology, the second-messenger producer is a participant of the pathway it starts: GO:0140896 cGAS/STING signaling pathway. It is not a regulator of GO:0016032 viral process.
- Activity is more specific than outcome. A GEF does not alter the GTPase's catalytic rate, so it is not GO:0005096 GTPase activator activity ([go-annotation#1166](https://github.com/geneontology/go-annotation/issues/1166)). On the BP side, the GEF is part of the signalling pathway the GTPase transduces.

**Provenance.** [GOC+]. Requiring a named target, or the honest fallback to an upstream relation, is our sharpening.

<a id="rs-3"></a>

### RS-3. Limiting quantities, constitutive prerequisites and substrate supply are not regulation

**Statement.** Do not annotate a gene product to regulation of X only because X slows or stops without it. In particular:

1. a pathway member whose abundance limits flux, such as receptor number at the surface;
2. a constitutive step that is rate-limiting but not modulated, such as nuclear transport of a signalling component;
3. a process that supplies a substrate or cofactor (folate, ATP, lipids) consumed by X;
4. a gene whose mutation creates a problem that a checkpoint or stress pathway then detects.

**Rationale.** [wiki: Annotating regulation](https://wiki.geneontology.org/index.php/Annotating_regulation), Guideline 6, gives the receptor example. In [go-annotation#1955](https://github.com/geneontology/go-annotation/issues/1955), translocation into the nucleus is rate-limiting in the G2/M pathway, but the nuclear pore "isn't doing anything mechanistically" to modulate it. Generic perturbation phenotypes such as cell cycle delay do not justify a regulation term. Folate-generating processes are causally upstream of nucleotide and amino acid metabolism but do not regulate them. When to annotate such dependencies at all remains unsettled ([go-annotation#2431](https://github.com/geneontology/go-annotation/issues/2431)). Mutations that activate a checkpoint show that the checkpoint works, not that the gene is in it ([wiki: Guidelines for checkpoints](https://wiki.geneontology.org/index.php/Guidelines_for_checkpoints)). GO-CAM gives constitutive requirements their own relation, `constitutively upstream of`, separate from regulation ([wiki: Annotation Relations](https://wiki.geneontology.org/index.php/Annotation_Relations)).

**Worked example.** NRAS palmitoylation by ZDHHC9 is needed for NRAS signalling but is not regulated by the signal. In a GO-CAM it is `constitutively upstream of` the NRAS activity ([wiki: Constitutively upstream of](https://wiki.geneontology.org/index.php/Constitutively_upstream_of)). In a standard annotation, ZDHHC9 does not get "positive regulation of Ras protein signal transduction". It gets its palmitoyltransferase MF and the process that MF is part of.

**Provenance.** [GOC]. Item 3 is [GOC+]: GOC raised it without resolving it, and we state the default.

<a id="rs-4"></a>

### RS-4. Pathway members that activate the next member are part of the pathway, not regulators of it; feedback is the exception

**Statement.** Do not annotate a component to "positive regulation of P" because it activates the next component of P. Activation is how signalling pathways work. A component may also carry a regulation term for P when it feeds back on an earlier step, as in ERK inhibition of FRS2α, or when its role in P is to restrain P. Do not annotate both "P" and "regulation of P" from the same evidence.

**Rationale.** [wiki: Annotating regulation](https://wiki.geneontology.org/index.php/Annotating_regulation), Guideline 6: "MAPKK would not be annotated to positive regulation of MAPKKK cascade just because it phosphorylates and activates MAPK." The ontology made the same correction. GO removed the `regulates o part_of → regulates` property chain because it inferred, for example, that MAPKK activity positively regulates the MAPK cascade ([Drive: Ontology development update, SAB 2019](https://drive.google.com/open?id=1csX9z0szrud0-XIUitPR2pesr8ry-0xcTQNkCv5fsHo)). The FlyBase rules allow a gene product to be both in a pathway and its regulator, as positive and negative regulator in different contexts ([Drive: FlyBase pathway curation guide](https://drive.google.com/open?id=1Toyf0QhDjuGMYa1KyDGF-T9qXnXfvxAuYisLpAxfZoI)).

**Worked examples.**

- MAP2K1: `involved_in` GO:0000165 MAPK cascade. Not GO:0043410 positive regulation of MAPK cascade.
- In canonical Wnt signalling, the destruction complex keeps β-catenin low without a signal, and Wnt inhibits that degradation. Components such as GSK3 are participants in the pathway even though the signal inactivates them ([wiki: Signaling Curation Manual](https://wiki.geneontology.org/index.php/Signaling_Curation_Manual), GSK3 example; [Drive: FlyBase pathway curation guide](https://drive.google.com/open?id=1Toyf0QhDjuGMYa1KyDGF-T9qXnXfvxAuYisLpAxfZoI)). FlyBase likewise puts Yorkie, the transcriptional effector that Hippo signalling retains in the cytoplasm, directly on GO:0035329 hippo signaling.

**Provenance.** [GOC].

<a id="rs-5"></a>

### RS-5. Judge sign in vivo, from the gene product's effect, and correct a wrong sign rather than tolerating it

**Statement.** The sign of a regulation annotation is the direction in which the normal gene product changes the process in the organism. Derive it from the gene product's effect, not from the mutant's phenotype: a knockout that increases X means the gene negatively regulates X. Use the signed term whenever the direction is known. Use the sign-neutral parent only when the direction genuinely depends on context, and say so. An in vitro activity of the opposite sign does not outweigh an established in vivo direction. In review, a wrong sign is `MODIFY` to the opposite-sign term (a lateral correction, not a refinement). Use `REMOVE` if the row also has no sound source.

**Rationale.** A too-general term is still true. An inverted one is false, and it propagates intact through ISS, IBA, Ensembl Compara and GO-CAM causal edges ([REGULATION_SIGN](../../REGULATION_SIGN.md)). A census of reviews in this repository found 35 sign-flip MODIFYs on 25 genes. IMP was the largest evidence class (15 of 35), consistent with phenotype direction being recorded as gene effect. FlyBase requires signed regulation terms for pathways ([Drive: FlyBase pathway curation guide](https://drive.google.com/open?id=1Toyf0QhDjuGMYa1KyDGF-T9qXnXfvxAuYisLpAxfZoI)). GO asks for the signed child of `acts upstream of or within` for the same reason ([wiki: Annotation Relations](https://wiki.geneontology.org/index.php/Annotation_Relations)).

**Worked examples.**

- Human GNAI2, GO:0007189 adenylate cyclase-activating G protein-coupled receptor signaling pathway (IEA, Ensembl Compara): Gαi2 inhibits the cyclase, so MODIFY to GO:0007193 adenylate cyclase-inhibiting G protein-coupled receptor signaling pathway (review `genes/human/GNAI2`).
- Human GNAI1, the same term by ISS from an adenylyl cyclase donor: the in vitro stimulation of type I/II cyclases by high Gαi concentrations does not rescue it, so REMOVE ([REGULATION_SIGN](../../REGULATION_SIGN.md)).
- Human NLRP3, GO:0050728 negative regulation of inflammatory response (IMP ×3): MODIFY to GO:0050729 positive regulation of inflammatory response. Human LRP5, GO:0045668 negative regulation of osteoblast differentiation: MODIFY to GO:0045669 positive regulation of osteoblast differentiation.
- Human NTSR1, GO:0040017 positive regulation of locomotion: knockouts are hypolocomotor, but the receptor also mediates stimulant-induced hyperactivity. MODIFY to the sign-neutral GO:0040012 regulation of locomotion, and record that the direction is context-dependent.

**Provenance.** [GOC+]. The in vivo principle and the handling of in vitro opposite-sign activity are [NEW], from [REGULATION_SIGN](../../REGULATION_SIGN.md).

<a id="rs-6"></a>

### RS-6. A signalling pathway runs from ligand–receptor engagement to the last effector; annotate its members, not its targets

**Statement.** Annotate to a signalling pathway term:

- the ligand (for protein ligands), the receptor, co-receptors and adaptors;
- the transducers and second-messenger enzymes that relay the signal;
- the last effector that hands the signal to the downstream process. This is often a DNA-binding transcription factor, or a kinase acting on the translation or metabolic machinery.

Do not annotate to the pathway:

- target genes whose expression the pathway changes;
- the machinery of the downstream process (RNA polymerase, ribosome, glycogen synthase);
- general factors that every pathway needs, such as Mediator, NuRD or ESCRT.

Avoid direct annotation to GO:0007165 signal transduction when a receptor- or ligand-specific pathway term exists.

**Rationale.** The Signaling Curation Manual sets the end of a pathway at "the transfer of information to gene products carrying out a downstream cellular process". The downstream process itself is not part of signalling. S6K is the last effector of PI3K signalling, SREBP1 is the last effector of EGFR-to-AKT signalling, and glycogen synthase is outside the pathway ([wiki: Signaling Curation Manual](https://wiki.geneontology.org/index.php/Signaling_Curation_Manual)). The draft cassette guidelines add that "the very downstream targets of the pathway – such as the genes whose levels are regulated by the pathway – are not annotated to the pathway" ([Drive: Intracellular signaling guidelines](https://drive.google.com/open?id=1ukxL3vKfLbV4NAiGSeGg3EbpLKijfXXOr0npHeUYLI4)). FlyBase's rules give the same boundary and exclude general chromatin and Mediator factors, and the endocytic machinery as opposed to the ubiquitin ligase that targets the receptor ([Drive: FlyBase pathway curation guide](https://drive.google.com/open?id=1Toyf0QhDjuGMYa1KyDGF-T9qXnXfvxAuYisLpAxfZoI)). The 2017 Cambridge signalling workshop agreed that every signalling term should have a defined start and end ([wiki: 2017 Cambridge GOC Signalling Workshop](https://wiki.geneontology.org/index.php/2017_Cambridge_GOC_Signalling_Workshop)).

**Worked examples**, from the FlyBase pattern presented at the 2022 GOC breakout ([Drive: Breakout use cases, 2022](https://drive.google.com/open?id=1nSVZ-LoPOnnWf_2e9ZOLAxbBjnTT9QKVq_Vb0448yGw)):

- Drosophila pnt enables GO:0001228 DNA-binding transcription activator activity, RNA polymerase II-specific (with `has_input` its target gene). It is `involved_in` GO:0007173 epidermal growth factor receptor signaling pathway and `involved_in` GO:0045944 positive regulation of transcription by RNA polymerase II. The ligand is not annotated to the transcription regulation term.
- Drosophila S6k is `involved_in` GO:0008286 insulin receptor signaling pathway and GO:2000767 positive regulation of cytoplasmic translation. RpS6 is not annotated to the pathway.

**Provenance.** [GOC]. The Signaling Curation Manual is flagged as under construction (2018) and cites some obsolete terms; its boundary rules are the part we adopt.

<a id="rs-7"></a>

### RS-7. Intracellular signalling cassettes are part of pathways; cassette members may carry both terms

**Statement.** A cassette, a child of GO:0141124 intracellular signaling cassette such as GO:0000165 MAPK cascade or GO:0043491 phosphatidylinositol 3-kinase/protein kinase B signal transduction, starts with activation of its first component and runs to a predictable output. Annotate:

- cassette members to the cassette term, and also to the receptor pathway it serves when the evidence places them there;
- the ligand, the receptor and the components between the receptor and the first cassette member to the receptor pathway. Annotate them to "positive regulation of" the cassette only when the cassette term is used without its pathway context;
- the targets of the cassette's last kinase to the receptor pathway, not to the cassette.

A pathway-specific scaffold that tethers cassette components is part of the cassette. If it also directly activates a component, add the regulator MF separately.

**Rationale.** These are the draft intracellular signalling guidelines ([Drive: Intracellular signaling guidelines](https://drive.google.com/open?id=1ukxL3vKfLbV4NAiGSeGg3EbpLKijfXXOr0npHeUYLI4)). The 2025 PAINT signalling work applied them to the cassette children of GO:0141124 ([Drive: PAINT signaling annotation – meeting minutes, 2025](https://drive.google.com/open?id=1B-NLo77GEnuDkNNt7j6La3uQVL2X_o7F13lxxgci5lM)). The scaffold ruling comes from the 2017 MAPK review: FlyBase chose "part of", to separate scaffolds from proteins that merely modulate the cascade. PomBase proposed GO:0005078 MAP kinase scaffold activity together with a separate enzyme regulator MF where the scaffold also allosterically activates a kinase ([go-annotation#1592](https://github.com/geneontology/go-annotation/issues/1592)). The 2023–2024 cascade review implemented these conclusions, and GO:0000165 MAPK cascade is not being obsoleted (same thread).

**Worked example.** In an RTK pathway, GRB2, SOS1 and RAS lie between the receptor and the first cassette member, RAF. They are `involved_in` the receptor pathway (for example GO:0007173), and, with only the cassette in view, in GO:0043410 positive regulation of MAPK cascade. RAF, MEK1/2 and ERK1/2 are `involved_in` GO:0000165, and in GO:0007173 where the evidence places them there. An ERK substrate transcription factor is `involved_in` GO:0007173 but not GO:0000165 ([MAPK_CASCADES](../../MAPK_CASCADES.md)).

**Provenance.** [GOC+]. The cassette document is a draft with open comments, so we state its rules as recommended practice.

<a id="rs-8"></a>

### RS-8. Protein ligands are part of the pathway they start; annotate them with receptor ligand activity, not receptor-specific binding terms

**Statement.** A protein ligand that activates a receptor is annotated as follows:

- MF: GO:0048018 receptor ligand activity, or a child.
- BP: `involved_in` the pathway it initiates, not "positive regulation of" that pathway.

Receptor-specific binding terms (GO:0005112 Notch binding, GO:0005109 frizzled binding, GO:0005113 patched binding, GO:0048495 Roundabout binding) are not the ligand's MF. In review, MODIFY them to the ligand activity term when the row's evidence shows ligand action. Ligand biogenesis, processing and secretion have their own process terms (GO:0061355 Wnt protein secretion, GO:0007225 patched ligand maturation). Annotate them there, not to the pathway or its regulation. Reserve "regulation of" the pathway for extracellular factors that specifically change ligand–receptor engagement: antagonists, sequestering proteins, co-receptors acting as modulators.

**Rationale.** Since 2017, GOC has treated ligands as pathway participants ([go-annotation#1691](https://github.com/geneontology/go-annotation/issues/1691); [go-annotation#1712](https://github.com/geneontology/go-annotation/issues/1712)), and the GO-CAM signalling-receptor guideline gives ligands receptor ligand activity, `part_of` the ligand's process ([Drive: Signaling receptor activity (archived; moved to MF guidelines for GO-CAM)](https://drive.google.com/open?id=1dZKucnM45V05MYJUkpuf3Epje6mZRxRv3-62Y5JwAHw)). A survey in this repository found 23 of 24 human and all 14 fly textbook ligands annotated `involved_in` their pathway ([LIGANDS_IN_SIGNALING](../../LIGANDS_IN_SIGNALING.md)). In January 2026 GO changed receptor ligand activity from a kind of signaling receptor binding to a term with signaling receptor binding as a part. A ligand annotated only to "Roundabout binding" therefore no longer counts as a ligand (same page; go-ontology#31015). FlyBase keeps ligand biogenesis and secretion out of the pathway and its regulation ([Drive: FlyBase pathway curation guide](https://drive.google.com/open?id=1Toyf0QhDjuGMYa1KyDGF-T9qXnXfvxAuYisLpAxfZoI)).

**Worked examples.**

- Human KITLG has no GO:0038109 Kit signaling pathway annotation. It is the one exception in the ligand survey and a real gap: GO:0005173 stem cell factor receptor binding alone does not make it a ligand in GO ([LIGANDS_IN_SIGNALING](../../LIGANDS_IN_SIGNALING.md)).
- A Wnt secretion factor such as Wntless belongs on GO:0061355 Wnt protein secretion, not on GO:0090263 positive regulation of canonical Wnt signaling pathway.
- Ligand withdrawal that triggers signalling (dependence receptors) is GO:0038034 signal transduction in absence of ligand or a child. The withdrawn ligand is annotated to regulation of that pathway ([wiki: Signaling Curation Manual](https://wiki.geneontology.org/index.php/Signaling_Curation_Manual)).

**Provenance.** [GOC+]. This departs from older advice that factors limiting ligand availability regulate the pathway, and from PomBase's local convention (see Differences).

<a id="rs-9"></a>

### RS-9. Receptors, G proteins and second-messenger enzymes: annotate the specific pathway the evidence shows, with the right coupling and sign

**Statement.**

- Receptors: annotate the most specific receptor activity the ligand and mechanism support (for example GO:0004941 beta2-adrenergic receptor activity rather than GO:0004930 G protein-coupled receptor activity, when the row's own evidence names the ligand). Annotate the matching pathway.
- G proteins: annotate coupling pathway terms (GO:0007189, GO:0007193, GO:0007200 phospholipase C-activating G protein-coupled receptor signaling pathway) from direct evidence on the Gα class, not from family membership.
- Second-messenger enzymes: annotate an adenylate cyclase that makes the second messenger of a GPCR pathway to that pathway. Annotate an enzyme that destroys the second messenger, such as a phosphodiesterase, to negative regulation of the pathway.
- Inhibitory receptors: a receptor whose ligand switches its activity off, such as Patched, is annotated to regulation of the pathway, with the sign the receptor exerts. Smoothened carries the pathway term.

**Rationale.** The 2025 PAINT signalling minutes record the plan to obsolete GO:0019933 cAMP-mediated signaling and GO:0141156 cAMP/PKA signal transduction, with members re-annotated to GO:0007189. The same minutes place PKA in the pathway and propose PDEs as negative regulation ([Drive: PAINT signaling annotation – meeting minutes, 2025](https://drive.google.com/open?id=1B-NLo77GEnuDkNNt7j6La3uQVL2X_o7F13lxxgci5lM)). GO:0019933 is obsolete in the current release. The 2017 review asked curators to rehouse "regulation of adenylate cyclase activity" and "regulation of cAMP biosynthesis" rows on GPCRs to the AC-activating or AC-inhibiting pathway terms ([go-annotation#1691](https://github.com/geneontology/go-annotation/issues/1691)). In the ligand survey, PTCH1 and Drosophila ptc carry only regulation terms ([LIGANDS_IN_SIGNALING](../../LIGANDS_IN_SIGNALING.md)). The Gs/Gi split is the commonest source of family-level sign errors ([GPCR](../../GPCR.md); [REGULATION_SIGN](../../REGULATION_SIGN.md)).

**Worked example.** PTCH1 restrains Smoothened until Hedgehog binds. Annotate PTCH1 to GO:0045879 negative regulation of smoothened signaling pathway, and Smoothened to GO:0007224 smoothened signaling pathway.

**Provenance.** [GOC+]. The PDE convention is a 2025 PAINT working decision (minutes), not yet a published guideline.

<a id="rs-10"></a>

### RS-10. Regulation does not cross transcription, and general machinery is not a pathway regulator

**Statement.**

- A component of pathway A that changes the transcription of pathway B's components does not regulate pathway B. Annotate it to pathway A, and annotate the transcription factor at A's end to regulation of transcription with `has_input` the target genes.
- A transcription factor whose targets build a tissue is not, by that alone, a regulator of the tissue's development. Regulation of gene expression by an miRNA acting on a pathway component's mRNA is direct and may be annotated to regulation of that pathway.
- Generic regulators that affect many processes are not annotated to a specific pathway or its regulation, even when authors call them essential for it. Examples are general chromatin modifiers, Mediator, translation factors and proteasome subunits.

**Rationale.** FlyBase pathway rules: "Regulation should not traverse transcription, which should mark a natural breakpoint". Their example is Wnt signalling regulating Notch signalling transcriptionally. They treat miRNAs as acting on a gene product, and generic regulators as non-specific ([Drive: FlyBase pathway curation guide](https://drive.google.com/open?id=1Toyf0QhDjuGMYa1KyDGF-T9qXnXfvxAuYisLpAxfZoI)). Their 2022 breakout statement: "we would not annotate the ligand, for example, as a regulator of transcription BP as it [is] separated by multiple steps" ([Drive: Breakout use cases, 2022](https://drive.google.com/open?id=1nSVZ-LoPOnnWf_2e9ZOLAxbBjnTT9QKVq_Vb0448yGw)). [OVER_ANNOTATION_PATTERNS](../../OVER_ANNOTATION_PATTERNS.md), pattern 4, records the same failure in reviews: a kinase that phosphorylates one transcription factor ends up annotated to "regulation of cell proliferation".

**Worked example.** A Wnt-pathway component annotated "negative regulation of Notch signaling pathway" because Wnt signalling represses a Notch ligand gene: MODIFY or REMOVE the Notch row, unless the paper shows a direct interaction with Notch pathway components.

**Provenance.** [GOC+]. A FlyBase rule, adopted here for all groups.

<a id="rs-11"></a>

### RS-11. Use "response to X" for gene products that detect X, transduce it, or carry out a response specific to X

**Statement.** Annotate "response to X" or "cellular response to X" when the gene product is required for the response to occur, because it detects X, relays the signal, regulates the response programme, or is an effector whose deployment is that response (heat-shock chaperones, infection-induced antimicrobials). Prefer:

- the most informative term: the named signalling pathway, the "defense response to" term for defensive effectors, or the specific stimulus;
- "cellular response to X" when the evidence is cell-autonomous, and "response to X" when it is organism-level or unresolved.

Do not annotate high-level response terms, which are do-not-annotate in the current ontology: GO:0050896 response to stimulus, GO:0051716 cellular response to stimulus, GO:0042221 response to chemical, GO:0009605 response to external stimulus, GO:0009607 response to biotic stimulus, GO:0009628 response to abiotic stimulus, GO:0009719 response to endogenous stimulus. Do not annotate a gene to "response to X" because its expression changes after X (see RS-12).

**Rationale.** The 2013 GO best-practices paper states that "response to" terms are for gene products "required for the response to occur and are a direct result of the organism's reaction to the stimuli", and that changes in expression do not in themselves show a contribution ([PMID:23842463](https://europepmc.org/article/MED/23842463), A guide to best practices for GO manual annotation). The 2012 working-group discussion on the (now deprecated) wiki page reached the same view, as did MGI's practice: these terms are reserved for gene products "that actively interpret a stimulus" ([wiki: Response to x annotation guidelines](https://wiki.geneontology.org/index.php/Response_to_x_annotation_guidelines)). PAINT does not normally propagate "response to" terms ([go-annotation#2171](https://github.com/geneontology/go-annotation/issues/2171); [go-annotation#2250](https://github.com/geneontology/go-annotation/issues/2250)). The terms are defined as beginning with detection of the stimulus and ending with a change in state of the cell or organism ([wiki: Guidelines from Annotation Camp](https://wiki.geneontology.org/index.php/Guidelines_from_Annotation_Camp); [wiki: Detection and Response to stimulus](https://wiki.geneontology.org/index.php/Detection_and_Response_to_stimulus)).

**Worked examples.**

- *C. elegans* hsp-16.2 and *E. coli* DnaK keep GO:0009408 response to heat. Being made during heat stress is their function ([IEP](../../IEP.md), "Where IEP is legitimate").
- Arabidopsis PIF3 carries seven IEP "response to" rows, six from one expression survey. PIF3 is a phytochrome-interacting transcription factor that runs those programmes, so annotating it as a responder to each stimulus inverts regulator and target. The rows were flagged as over-annotated; the gene's real role is carried by its IMP annotations ([IEP](../../IEP.md), pattern 4).
- *E. coli* arnF, GO:0010041 response to iron(III) ion: the operon's promoter responds to iron through BasS–BasR, but ArnF is a flippase for undecaprenyl phosphate-α-L-Ara4N that does not sense or handle iron. The iron response belongs to the promoter, not to the protein ([IEP](../../IEP.md), pattern 5).

**Provenance.** [GOC+]. The best-practices restriction is GOC's. The do-not-annotate list is from the current ontology.

<a id="rs-12"></a>

### RS-12. IEP supports "response to" and other BP terms only for normal expression, and usually only as a non-core role

**Statement.** IEP may support BP terms only (GORULE:0000006), and only from normal expression patterns. Overexpression and ectopic expression are IDA or IMP evidence. Before accepting an IEP row, ask whether the gene product is an agent of the process or a bystander whose abundance tracks it. In review, the default action for a sound induction observation that is not the gene's job is `KEEP_AS_NON_CORE`. Use `MARK_AS_OVER_ANNOTATED` for stimulus clouds (one enzyme, many unrelated "response to X" terms from separate exposure papers), for developmental time-courses read as tissue-building roles, and for one-screen batches. Use `REMOVE` only for a categorical mismatch. Do not remove an IEP row merely because the code is weak.

**Rationale.** [wiki: Inferred from Expression Pattern (IEP)](https://wiki.geneontology.org/index.php/Inferred_from_Expression_Pattern_%28IEP%29) restricts the code to BP and to normal expression, and advises caution and high-level terms. In this repository's reviews, 22.5% of IEP rows were accepted and 55.6% kept as non-core. The characteristic IEP row is true but peripheral ([IEP](../../IEP.md)). Both figures come from AI reviews primed to look for over-annotation, so they describe one reviewer population, not an independent audit (same page).

**Worked example.** Rat Gstt1 carries GO:0009410 response to xenobiotic stimulus plus salicylic acid, selenium ion and vitamin E response terms, each from a separate induction paper. All describe one broad-specificity transferase. Keep the xenobiotic term as non-core. Mark the sibling stimulus terms as over-annotated ([IEP](../../IEP.md), pattern 1).

**Provenance.** [GOC] for the code restrictions. [GOC+] for the review dispositions.

<a id="rs-13"></a>

### RS-13. Do not use MF regulator terms when the regulatory activity is unknown, and do not give a regulator the activity it regulates

**Statement.** If a gene product is known to regulate a process but its molecular activity is unknown, annotate the BP regulation term and leave MF unannotated. GO:0098772 molecular function regulator activity is do-not-annotate. Conversely, when a gene product regulates an enzyme or receptor, annotate it with the regulator activity (enzyme activator, inhibitor, ligand), not the activity of its target.

**Rationale.** [go-annotation#2827](https://github.com/geneontology/go-annotation/issues/2827): "We don't recommend using a MF if we don't know what the MF is. You can use BP 'regulation of x pathway'". The pilot function-requirement rules in this repository found that regulators annotated with the activity they regulate are a recurring class among flagged experimental `enables` rows ([FUNCTION_REQUIREMENT_RULES](../../FUNCTION_REQUIREMENT_RULES.md)). The GTPase case is the standard example: a GEF is not a GTPase activator ([go-annotation#1166](https://github.com/geneontology/go-annotation/issues/1166)).

**Provenance.** [GOC].

<a id="rs-14"></a>

### RS-14. Annotate regulation at the level where it acts, not at every enclosing process

**Statement.** Annotate the most proximal process that the gene product regulates. Regulation of a step does not imply regulation of the process containing it, and GO no longer infers it. Add a regulation term for an enclosing process only with separate evidence. Do not stack regulation terms for each enclosing level (cascade, pathway, response, organ development) from one experiment.

**Rationale.** GO removed the `regulates o part_of → regulates` chain in 2019 and asserted the 1,484 inferred relations that editors reviewed and chose to keep ([Drive: Ontology development update, SAB 2019](https://drive.google.com/open?id=1csX9z0szrud0-XIUitPR2pesr8ry-0xcTQNkCv5fsHo)). Regulation therefore no longer propagates silently up `part_of`. The Apoptosis manual applies the same restraint to MOMP and cytochrome c release ([wiki: Apoptosis Curation Manual](https://wiki.geneontology.org/index.php/Apoptosis_Curation_Manual)).

**Worked example.** A phosphatase shown to dephosphorylate and inactivate ERK is annotated to negative regulation of the ERK1/2 cascade (a regulation child of GO:0070371 ERK1 and ERK2 cascade) and, if shown, the receptor pathway. It is not annotated to negative regulation of cell population proliferation unless the paper shows that its ERK action controls proliferation of a named cell type.

**Provenance.** [GOC+].

## Decision aid

For a gene product G and a process X that a paper says G "regulates":

| # | Question | If yes | If no |
|---|---|---|---|
| 1 | Does G perform an activity between X's start and end? | `involved_in` X (RS-1); add regulation only for feedback (RS-4) | go on |
| 2 | Is G a substrate supplier, a limiting component, a constitutive prerequisite, or the cause of damage that X detects? | Not regulation (RS-3); annotate G's own process | go on |
| 3 | Is there evidence that G changes the activity, amount or location of a named X participant, or X's timing? | `involved_in` (positive/negative) regulation of X, with the target as `has_input` (RS-2) | go on |
| 4 | Does G act through transcription of X's components while belonging to another pathway? | G's own pathway; no regulation of X (RS-10) | go on |
| 5 | Is the effect real, directional and mechanism-unknown? | `acts upstream of or within, positive/negative effect` X ([BP-4](biological-process.md#bp-4)) | no annotation |

Then check the sign against the gene product's in vivo effect (RS-5).

For signalling-pathway membership:

| Entity | Pathway term | Regulation of pathway | Neither |
|---|---|---|---|
| Protein ligand, receptor, co-receptor, adaptor, transducer, second-messenger synthase, last effector (TF, S6K) | yes | feedback only | |
| Inhibitory receptor (Patched), second-messenger degrader (PDE), extracellular antagonist, pathway-specific E3 ligase targeting a component | | yes (signed) | |
| Ligand biogenesis/secretion factor | | | own process term |
| Target genes, downstream-process machinery, general chromatin/Mediator/ESCRT | | | yes |

## Common errors

- **Phenotype read as regulation.** "Knockdown reduced X" becomes "positive regulation of X". Fix: RS-2 and BP-4.
- **Sign inverted from the phenotype.** A knockout raises X, so the gene "positively regulates X". Fix: RS-5; record a sign correction as MODIFY.
- **Pathway member as its own pathway's regulator.** A kinase annotated to positive regulation of the cascade it is a tier of. Fix: RS-4.
- **Target gene in the pathway.** A gene induced by the pathway annotated to the pathway. Fix: RS-6.
- **Transcription traversed.** A signalling component annotated to regulation of a second pathway, or of a developmental process, through transcription. Fix: RS-10.
- **Ligand on a receptor-binding term only.** Fix: RS-8.
- **Second-messenger enzyme as a regulator of the outcome.** cGAS as "regulation of viral life cycle". Fix: RS-2 and RS-9; put the enzyme in the pathway.
- **Stimulus cloud.** Many "response to X" IEP rows on one enzyme. Fix: RS-12.
- **Hub inversion.** A master transcription factor annotated as responding to every stimulus whose programme it drives. Fix: RS-11, RS-12.
- **High-level response or regulation terms.** GO:0050896, GO:0042221, GO:0050794 regulation of cellular process, GO:0048583 regulation of response to stimulus and similar grouping terms are do-not-annotate. Fix: specific term or none.
- **Family-level sign leakage.** Gs/Gi coupling terms crossing the split by IBA or ISS. Fix: RS-5, RS-9; see [phylogenetic-propagation.md](phylogenetic-propagation.md).

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [wiki: Annotating downstream processes](https://wiki.geneontology.org/index.php/Annotating_downstream_processes) | "A factor which limits or increases the availability of a ligand to a receptor should be annotated as regulating the ligand/receptor pathway." | Ligand biogenesis, processing and secretion go to their own terms. Only factors that specifically change ligand–receptor engagement (antagonists, sequestering proteins, modulating co-receptors) get regulation of the pathway (RS-8). | FlyBase's more recent rules exclude upstream biogenesis and secretion, and dedicated terms now exist. The wiki page is itself flagged "to be reviewed". |
| [wiki: Annotating regulation](https://wiki.geneontology.org/index.php/Annotating_regulation), Guideline 2 | If unsure, annotate the parent process with `acts upstream of or within`. | Same, but always with the positive- or negative-effect child (RS-1, RS-5). | The relation table and wiki now ask for the signed child. A perturbation almost always gives the direction. |
| [wiki: Annotating regulation](https://wiki.geneontology.org/index.php/Annotating_regulation), Guideline 5 | IMP can support regulation terms when assay, allele type and gene identity are considered. | IMP alone supports an upstream relation. A regulation term needs a named target or a known regulatory mechanism (RS-2). | The 2022 PomBase breakdown and #2570 show that phenotype-based regulation rows are the main source of errors in this class. |
| [wiki: Signaling Curation Manual](https://wiki.geneontology.org/index.php/Signaling_Curation_Manual) | Extracellular ligands of PI3K signalling are annotated to "positive regulation of phosphatidylinositol 3-kinase signaling". Ligands use "receptor agonist activity". | GO:0014068 and GO:0014065 are obsolete. Ligands get receptor ligand activity and the receptor pathway term; "positive regulation of" the cassette only when the cassette is annotated without pathway context (RS-7, RS-8). | The page dates from 2018 and cites obsolete terms. "Receptor agonist activity" was renamed receptor ligand activity in 2017 ([LIGANDS_IN_SIGNALING](../../LIGANDS_IN_SIGNALING.md)). |
| [Drive: Intracellular signaling guidelines](https://drive.google.com/open?id=1ukxL3vKfLbV4NAiGSeGg3EbpLKijfXXOr0npHeUYLI4) vs [go-annotation#1712](https://github.com/geneontology/go-annotation/issues/1712) | The cassette draft puts ligand and receptor in "positive regulation of" the cassette. #1712 puts ligands in the pathway, not its regulation. | Both hold, at different levels: the ligand is `involved_in` the receptor pathway and acts upstream of the cassette it triggers (RS-7). | Apparent conflict. The cassette document regulates the cassette, and #1712 concerns the receptor pathway. |
| PomBase convention, reported in [LIGANDS_IN_SIGNALING](../../LIGANDS_IN_SIGNALING.md) | Pheromones, receptors and Gα annotated to "positive regulation of pheromone response MAPK cascade"; only the kinases are `involved_in` the cascade. | Ligand, receptor and Gα `involved_in` the receptor pathway term where one exists (RS-6, RS-8). | One convention across GO. PomBase's choice follows from the obsolescence of the old pathway term, so the fix may be ontological (a pathway term to annotate to). Raise it with PomBase rather than overriding locally. |
| [Drive: FlyBase pathway curation guide](https://drive.google.com/open?id=1Toyf0QhDjuGMYa1KyDGF-T9qXnXfvxAuYisLpAxfZoI) (FlyBase-only) | Regulation does not traverse transcription; general regulators stay off pathways; regulation terms must be signed. | Adopt for all groups (RS-5, RS-10). | The rules work well in FlyBase's exhaustive pathway curation and match the GOC wiki's intent. |
| [Drive: Kimberly & Pascale minutes](https://drive.google.com/open?id=1PTb0-s9LE8IhsStqhdc25Hb5prdlxBGWbOr8oLfIWNA) vs [Drive: Breakout use cases, 2022](https://drive.google.com/open?id=1nSVZ-LoPOnnWf_2e9ZOLAxbBjnTT9QKVq_Vb0448yGw) | Minutes (GO-CAM standardisation): curators would not annotate +/- regulation of transcription, only the "larger" BP. FlyBase: the pathway TF is `involved_in` both the pathway and positive regulation of transcription by RNA Pol II. | For standard annotation of a pathway's terminal TF, follow FlyBase: pathway term plus the regulation-of-transcription term, with `has_input` the targets (RS-6). The GO-CAM convention is left to [gocam-modeling.md](gocam-modeling.md). | The two sources address different products. In a GAF, the transcription term is the only place the TF's regulatory role appears. |
| [wiki: Response to x annotation guidelines](https://wiki.geneontology.org/index.php/Response_to_x_annotation_guidelines) (deprecated) | Debate between restricting "response to" to signal interpretation (MGI) and including effectors of cell-state change. | Include effectors only when their deployment is the specific response (HSPs, antimicrobials). Exclude generic machinery that any response uses (RS-11). | Settles the 2008–2012 debate with the criterion the [IEP](../../IEP.md) review found discriminating. |
| [wiki: Inferred from Expression Pattern (IEP)](https://wiki.geneontology.org/index.php/Inferred_from_Expression_Pattern_%28IEP%29) | IEP examples include annotating a gene upregulated during ER stress (Atp2a2) to "response to endoplasmic reticulum stress". | Acceptable only as non-core unless the gene's job is the response (RS-12). | The wiki's own example is the inducible-bystander pattern. GO's 2013 best-practices paper sets the stricter "required for the response" bar. |
| [wiki: Response to and signaling](https://wiki.geneontology.org/index.php/Response_to_and_signaling); [LIGANDS_IN_SIGNALING](../../LIGANDS_IN_SIGNALING.md) | Pathway terms are part of "cellular response to X", so ligands inherit response annotations. Whether ligands should carry the response term is unresolved (go-ontology#15477). | Do not annotate ligands directly to "cellular response to [ligand]". Let inference supply it through the pathway term. | Annotating the ligand as responding to itself reads badly in a GAF. Inference already gives users the link. |
| [Drive: PAINT signaling minutes, 2025](https://drive.google.com/open?id=1B-NLo77GEnuDkNNt7j6La3uQVL2X_o7F13lxxgci5lM) | Working decision: PDEs are negative regulation of cAMP pathways; cAMP-mediated signaling to be obsoleted. | Adopted (RS-9). | Fills a gap: no published guideline covered second-messenger degraders. |
| [REGULATION_SIGN](../../REGULATION_SIGN.md) (repository) vs earlier review practice | An earlier review held GNAI1's AC-activating row UNDECIDED because of in vitro cyclase stimulation. | Sign is judged in vivo. Opposite-sign in vitro activity is not grounds for UNDECIDED (RS-5). | Sharpens a gap. GOC documents no rule on conflicting in vitro and in vivo sign. |

## Open questions

1. **Scaffolds and adaptors: part of, or regulation of?** [go-annotation#1592](https://github.com/geneontology/go-annotation/issues/1592) records dissent, and the 2022 PomBase questions (WASP and Arp2/3, securin and separase) show the same ambiguity outside signalling ([Drive: 2022 questions about regulation](https://drive.google.com/open?id=1J_WpQPSyn4wvsMtxEAG4d7xA4SLmA0m2)). Is a substrate inhibitor (securin) part of sister chromatid separation, or a negative regulator of it?
2. **Upstream dependencies.** Should any "acts upstream of" annotations be made for constitutive metabolic prerequisites, such as folate for nucleotide synthesis? If so, where does the chain stop ([go-annotation#2431](https://github.com/geneontology/go-annotation/issues/2431))?
3. **Antagonist ligands.** Receptor ligand activity is now classed as an activating activity, but Hedgehog binding inhibits Patched. Should GO have agonist and antagonist ligand terms (go-ontology#14275, open since 2017; [LIGANDS_IN_SIGNALING](../../LIGANDS_IN_SIGNALING.md))?
4. **Pathway end for non-transcriptional outputs.** Where does a pathway end when its output is cytoskeletal or metabolic? The 2022 breakout noted that terms "ultimately effecting a change in the functioning of the cell" leave this unclear ([Drive: Breakout – Annotating to a process or its regulation, 2022](https://drive.google.com/open?id=1ii8kFkraHYYSGThmYZq9i6EyqNmY4v91hpGuuvIMunk)).
5. **"Response to" qualifier.** Should GO distinguish "acts in the response" from "is induced during the response", by an extension or a qualifier, so that IEP rows stop competing with mechanistic ones ([IEP](../../IEP.md), recommendation 5)?
6. **PomBase pheromone convention.** Should GO restore a pheromone signalling pathway term so that ligands and receptors can be `involved_in` it?
7. **Tissue-development regulation.** The 2022 breakout asked where the boundary lies between a process and its regulation for tissue development, which needs signalling, trafficking and cell-cycle control. The BP refactoring draft suggests regulation exists only at the level of pathways and cells ([Drive: BP refactoring 2022](https://drive.google.com/open?id=1FafBfb44nAk-7PwUDj42XQLgwJYxPdq8ec4n-cWwKkg)). Should "regulation of [organ] development" terms be retired?

## Sources

**GO wiki**

- [Annotating regulation](https://wiki.geneontology.org/index.php/Annotating_regulation) (flagged "to be reviewed"; updated 2021)
- [Annotating from phenotypes](https://wiki.geneontology.org/index.php/Annotating_from_phenotypes)
- [Annotating downstream processes](https://wiki.geneontology.org/index.php/Annotating_downstream_processes)
- [Annotation Relations](https://wiki.geneontology.org/index.php/Annotation_Relations)
- [Constitutively upstream of](https://wiki.geneontology.org/index.php/Constitutively_upstream_of)
- [Signaling Curation Manual](https://wiki.geneontology.org/index.php/Signaling_Curation_Manual) (under construction, 2018)
- [2017 Cambridge GOC Signalling Workshop](https://wiki.geneontology.org/index.php/2017_Cambridge_GOC_Signalling_Workshop)
- [Response to x annotation guidelines](https://wiki.geneontology.org/index.php/Response_to_x_annotation_guidelines) (deprecated)
- [Response to and signaling](https://wiki.geneontology.org/index.php/Response_to_and_signaling)
- [Detection and Response to stimulus](https://wiki.geneontology.org/index.php/Detection_and_Response_to_stimulus)
- [Guidelines from Annotation Camp](https://wiki.geneontology.org/index.php/Guidelines_from_Annotation_Camp) (historical)
- [Guidelines for checkpoints](https://wiki.geneontology.org/index.php/Guidelines_for_checkpoints)
- [Inferred from Expression Pattern (IEP)](https://wiki.geneontology.org/index.php/Inferred_from_Expression_Pattern_%28IEP%29)
- [Apoptosis Curation Manual](https://wiki.geneontology.org/index.php/Apoptosis_Curation_Manual)

**GO Consortium Drive**

- [Intracellular signaling guidelines](https://drive.google.com/open?id=1ukxL3vKfLbV4NAiGSeGg3EbpLKijfXXOr0npHeUYLI4) (draft)
- [FlyBase pathway curation guide](https://drive.google.com/open?id=1Toyf0QhDjuGMYa1KyDGF-T9qXnXfvxAuYisLpAxfZoI) (draft for discussion)
- [Breakout – Annotating to a process or its regulation, 2022 (slides)](https://drive.google.com/open?id=1ii8kFkraHYYSGThmYZq9i6EyqNmY4v91hpGuuvIMunk)
- [Breakout use cases – Annotating to a process or its regulation, 2022](https://drive.google.com/open?id=1nSVZ-LoPOnnWf_2e9ZOLAxbBjnTT9QKVq_Vb0448yGw)
- [2022 questions about regulation (PomBase)](https://drive.google.com/open?id=1J_WpQPSyn4wvsMtxEAG4d7xA4SLmA0m2)
- [GO-CAM Jamboree 2020 – Regulation notes](https://drive.google.com/open?id=1mAIocbi6UvG_zbfCrWOUrneia3vl2XkjVPM39tmSx40)
- [MF-MF relations abstract, ISB 2023](https://drive.google.com/open?id=1r-tnt3Jk7H4Sb3xzIbx7ODVGCUbbyh9uyxPN1JhUK-M)
- [Ontology development update, SAB 2019](https://drive.google.com/open?id=1csX9z0szrud0-XIUitPR2pesr8ry-0xcTQNkCv5fsHo)
- [Signaling receptor activity (archived)](https://drive.google.com/open?id=1dZKucnM45V05MYJUkpuf3Epje6mZRxRv3-62Y5JwAHw)
- [PAINT signaling annotation – meeting minutes, 2025](https://drive.google.com/open?id=1B-NLo77GEnuDkNNt7j6La3uQVL2X_o7F13lxxgci5lM)
- [Kimberly & Pascale – minutes](https://drive.google.com/open?id=1PTb0-s9LE8IhsStqhdc25Hb5prdlxBGWbOr8oLfIWNA)
- [BP refactoring 2022 – developmental process](https://drive.google.com/open?id=1FafBfb44nAk-7PwUDj42XQLgwJYxPdq8ec4n-cWwKkg) (draft)

**go-annotation issues**

[#1166](https://github.com/geneontology/go-annotation/issues/1166), [#1592](https://github.com/geneontology/go-annotation/issues/1592), [#1687](https://github.com/geneontology/go-annotation/issues/1687), [#1691](https://github.com/geneontology/go-annotation/issues/1691), [#1712](https://github.com/geneontology/go-annotation/issues/1712), [#1955](https://github.com/geneontology/go-annotation/issues/1955), [#1979](https://github.com/geneontology/go-annotation/issues/1979), [#2171](https://github.com/geneontology/go-annotation/issues/2171), [#2250](https://github.com/geneontology/go-annotation/issues/2250), [#2431](https://github.com/geneontology/go-annotation/issues/2431), [#2570](https://github.com/geneontology/go-annotation/issues/2570), [#2587](https://github.com/geneontology/go-annotation/issues/2587), [#2827](https://github.com/geneontology/go-annotation/issues/2827). go-ontology issues cited via LIGANDS_IN_SIGNALING: #14275, #15477, #31015.

**Papers**

- [PMID:23842463](https://europepmc.org/article/MED/23842463) A guide to best practices for Gene Ontology (GO) manual annotation (2013)

**Repository**

- [REGULATION_SIGN](../../REGULATION_SIGN.md)
- [LIGANDS_IN_SIGNALING](../../LIGANDS_IN_SIGNALING.md)
- [MAPK_CASCADES](../../MAPK_CASCADES.md)
- [GPCR](../../GPCR.md)
- [IEP](../../IEP.md)
- [INTEGRATED_STRESS_RESPONSE](../../INTEGRATED_STRESS_RESPONSE.md) (EIF2AK3: GO:0140467 not added as NEW, being an ancestor of the accepted GO:0036499)
- [CGAS_STING_PATHWAY](../../CGAS_STING_PATHWAY.md)
- [OVER_ANNOTATION_PATTERNS](../../OVER_ANNOTATION_PATTERNS.md)
- [FUNCTION_REQUIREMENT_RULES](../../FUNCTION_REQUIREMENT_RULES.md)
- [CLAUDE.md](../../../CLAUDE.md) (MODIFY for sign corrections; "Do not overrule curators")
