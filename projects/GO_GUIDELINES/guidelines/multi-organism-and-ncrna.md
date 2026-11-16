# Multi-organism processes and non-coding RNAs: GO annotation guidelines

Status: draft v0.1 (2026-11-15) · Part of [GO_GUIDELINES](../../GO_GUIDELINES.md)

**In brief:**

- Annotate the organism that does the work. A symbiont gene product that acts on its host gets a "symbiont-mediated ... of host ..." term; the host gene product that responds gets a host-side term (defence response, host-mediated suppression, regulation of a viral process). Never the reverse.
- "Host" is the larger organism and "symbiont" the smaller, with no implication of harm; viruses, bacteria and parasites are all symbionts.
- Do not annotate host proteins to viral or symbiont life-cycle processes because a virus uses them. A host protein keeps its normal function; the dependence is recorded on the viral side, or in a GO-CAM.
- A symbiont term needs agency: the symbiont product evolved to do it. Being recognised by host immunity is not a symbiont process, and an antimicrobial effector is not a participant in the signalling that induces it.
- Annotate a non-coding RNA by its mature, identified product (an RNAcentral or MOD identifier), with RNA-specific function terms: base-pairing repressor, miRNA inhibitor, adaptor, scaffold, guide. Never with bare `RNA binding` or `protein binding`.
- miRNA function comes only from adding the miRNA (IDA) or removing it (IMP), never from expression changes. Target-specific MF annotations need binding evidence in the paper being annotated; prediction alone captures nothing.

## Scope

This document covers two areas that need rules beyond the general ones.

**Part A, multi-organism processes:** host-symbiont interactions of every kind
(viral, bacterial, fungal, oomycete, protist and metazoan parasites, mutualists,
venoms and toxins), the "symbiont" and "host" terms under `GO:0044419`
biological process involved in interspecies interaction between organisms,
effector proteins, host cellular component terms, recording the interacting
taxon, and immune and defence process terms on the host side.

**Part B, non-coding RNA genes:** miRNAs, siRNAs, piRNAs, lncRNAs and guide RNAs
(snoRNAs), as annotated objects; the proteins that make and regulate them; and
the evidence pitfalls specific to RNA experiments.

Evidence code choice in general is in [evidence-codes.md](evidence-codes.md);
extension syntax is in [annotation-extensions.md](annotation-extensions.md);
GO-CAM modelling of host-symbiont interactions follows
[gocam-modeling.md](gocam-modeling.md). Prokaryotic anti-phage defence is in
scope where it concerns process term choice.

This repository reviews gene products keyed by UniProt accession. ncRNA genes
have no UniProt entry, so Part B applies mainly to the protein side (Dicer,
Argonaute, TDMD ligases, snoRNP proteins) and to future ncRNA reviews; see Open
questions.

## Principles

**GO describes what a gene product evolved to do.** The 2021 multi-organism
working group restated this as its first aim: keep terms for normal gene
functions, and remove terms whose content is a host's reaction or a
pathological outcome. More than 300 terms were obsoleted, `multi-organism
process` (`GO:0051704`) among them, and the branch was rebuilt under
`GO:0044419`, which itself is in the do-not-annotate subset
([Drive: Intro - Host-Pathogen interaction session](https://drive.google.com/open?id=1FcqOAw-yKqDyM8KvFaGCnt_fY1ox4bMjVehlkkObY70)).
A virus subverting host translation is the virus's process. The host ribosome
is still doing host translation.

**The term name says which organism has agency.** The "symbiont-mediated"
labels introduced in 2023-2024 were chosen to settle this: the symbiont acts,
the host is acted on
([Drive: Interspecies interaction - level of granularity](https://drive.google.com/open?id=1035MddHFPgk1n2v1TnOTAqFS6FTymDqk2dw76lsZ48E)).
Most errors in this branch are host proteins annotated with symbiont terms. In
2021, 461 of 497 annotations to "modulation by symbiont of entry into host"
were to host proteins, and 557 of the first 600 annotations to viral entry into
host cell were host proteins
([go-annotation#3814](https://github.com/geneontology/go-annotation/issues/3814)).

**An RNA is annotated like a protein: with the activity it performs and the
process that activity serves.** The 2016 miRNA guidelines and the 2024 revision
of ncRNA terms gave RNAs their own MF terms, so the RNA no longer needs to
borrow its target's processes
([PMID:26917558](https://europepmc.org/article/MED/26917558) Guidelines for the functional annotation of microRNAs using the Gene Ontology;
[PMID:39374113](https://europepmc.org/article/MED/39374113) Representation of non-coding RNA-mediated regulation of gene expression using the Gene Ontology).

## Rules: Part A, multi-organism processes

<a id="mo-1"></a>

### MO-1. Annotate each organism's gene products with the terms written from that organism's side.

Before choosing a term, decide which organism's gene product does the step,
then use the term family for that side:

| Who acts | On whom | Term family | Example |
|---|---|---|---|
| Symbiont | host process | symbiont-mediated perturbation / suppression / activation of host X; effector-mediated ... | `GO:0052041` symbiont-mediated suppression of host programmed cell death |
| Symbiont | own life cycle in host | viral process children; symbiont entry into host | `GO:0046718` symbiont entry into host cell |
| Host | symbiont | defence response to X; host-mediated suppression of symbiont process; regulation of viral process | `GO:0051607` defense response to virus; `GO:0045071` negative regulation of viral genome replication |
| Venom component | another organism | venom-mediated ... | `GO:0035738` venom-mediated perturbation of biological process |

Host-side regulation terms (`GO:0045071` negative regulation of viral genome
replication, `GO:0044793` host-mediated suppression of viral process) are
legitimate for host restriction factors: they describe the host acting on the
virus.

*Example.* In GO-CAM `62b4ffe300002385`, *Shigella flexneri* OspC3
(UniProtKB:A0A0H2US87) enables `GO:0140740` ADP-riboxanase-[protein] activity
with `has input` human CASP4 (UniProtKB:P49662), occurs in `GO:0030430` host
cell cytoplasm, and is part of `GO:0052041`; its activity directly negatively
regulates CASP4 `GO:0004197` cysteine-type endopeptidase activity, which is
part of host `GO:0070269` pyroptotic inflammatory response. CASP4 gets no
symbiont term.

*Provenance:* [GOC+]. Sources:
[Drive: Interspecies interaction - level of granularity](https://drive.google.com/open?id=1035MddHFPgk1n2v1TnOTAqFS6FTymDqk2dw76lsZ48E);
[go-annotation#3814](https://github.com/geneontology/go-annotation/issues/3814);
[go-annotation#2720](https://github.com/geneontology/go-annotation/issues/2720).

<a id="mo-2"></a>

### MO-2. "Host" means the larger organism and "symbiont" the smaller; neither says anything about harm.

Symbiosis covers mutualism, commensalism and parasitism, so a pathogen is a
symbiont. When the partners are of similar size, terms say "other organism"
or "another organism". Do not pick between terms by whether the interaction
helps or harms; the 2021 refactor obsoleted "pathogenesis" for this reason,
since friendly and unfriendly symbionts use the same processes.

*Example.* A *Sinorhizobium meliloti* nodulation factor and a *Magnaporthe*
effector are both symbionts of their plant hosts; nodulation (`GO:0009877`)
and effector-mediated suppression of host pattern-triggered immunity
(`GO:0052034`) sit in the same branch.

*Provenance:* [GOC]. Sources:
[Drive: Multi-species terms - documentation to review](https://drive.google.com/open?id=12_2bJFup0Wn9TVYlysfbxFz8YERibJ4OXDB8GRowueU) (marked "to be reviewed");
[Drive: Intro - Host-Pathogen interaction session](https://drive.google.com/open?id=1FcqOAw-yKqDyM8KvFaGCnt_fY1ox4bMjVehlkkObY70).

<a id="mo-3"></a>

### MO-3. Do not annotate a host gene product to a viral or symbiont process because the symbiont uses it.

Host translation factors used for viral IRES-driven translation, host
transcription factors that transcribe a viral genome, host receptors a virus
enters through: each keeps its normal host function. Do not annotate them to
`GO:0016032` viral process, `GO:0019058` viral life cycle, `GO:0075522`
IRES-dependent viral translational initiation, `GO:0046718` symbiont entry into
host cell or other symbiont-process terms. Record the dependence on the
symbiont side, as an input of the viral protein's activity, or in a GO-CAM
that shows both.

For a host surface protein that a virus binds to enter, the MF `GO:0001618`
virus receptor activity is available. It is a binding term (its parent is
exogenous protein binding), not a receptor activity in the signalling sense.
Keep it as non-core when a direct binding or entry assay supports it; the
host protein's core function is its normal one.

In reviews, an existing host annotation to a symbiont-process term is
`MARK_AS_OVER_ANNOTATED` when it rests on an experiment (the curator saw real
data about the virus), and `REMOVE` when it comes from an electronic mapping or
propagation (a UniProt keyword such as KW-0945 Host-virus interaction once
mapped every tagged human protein to viral process).

*Example.* Human SSB and PCBP2 carried IDA annotations to `GO:0075522`
IRES-dependent viral translational initiation, which then implied a role in
host translation. Neither is a viral translation factor in the host's own
biology
([go-annotation#1507](https://github.com/geneontology/go-annotation/issues/1507)).

*Provenance:* [GOC+]. Earlier discussion conflicts: a 2016 comment recalled a
decision allowing host proteins "co-opted for the parasitic process"
([go-annotation#1367](https://github.com/geneontology/go-annotation/issues/1367)),
while the 2003, 2017 and 2018 threads and the 2021 working group took the
opposite view. We take the stricter view; see Differences and Open questions.
Sources:
[go-annotation#1](https://github.com/geneontology/go-annotation/issues/1);
[go-annotation#1507](https://github.com/geneontology/go-annotation/issues/1507);
[go-annotation#1891](https://github.com/geneontology/go-annotation/issues/1891);
[Drive: Combined multiorg + immune system process call 2021-11-22](https://drive.google.com/open?id=1fSGDMGKS4ogdCrTW8LWGltx_6acLWY5rxhTez_N98so).

<a id="mo-4"></a>

### MO-4. A symbiont term requires that the symbiont product evolved to cause the effect; being recognised is not a symbiont process.

A microbial molecule that the host detects (a flagellin, a lipopolysaccharide
biosynthetic enzyme, a pore-forming toxin that trips the inflammasome) does
not "activate the host immune response". The host's detection is a host
process. GO obsoleted the "induction by symbiont of host defense response"
terms (`GO:0044416` is obsolete) and removed terms such as "modulation by
symbiont of microbe-associated molecular pattern-induced host innate immune
response" for this reason.

Effector-mediated terms apply when there is evidence that the effector targets
the host function: a biochemical activity on a host target, a host protein it
binds and inhibits, a phenotype specific to the effector rather than to the
presence of the microbe.

Avirulence effectors recognised by a plant resistance protein are a special
case. `GO:0080185` effector-mediated activation of plant hypersensitive
response by symbiont is the term the working group kept for necrotrophs that
induce host cell death deliberately. In the current ontology it sits under
`GO:0052170` symbiont-mediated suppression of host innate immune response, so
every effector annotated to it also inherits a suppression claim. Use it only
when the effector's evolved role is to trigger the response, and report the
placement upstream.

*Example.* The repository's plant-fungal review found AVR4 and AVR9 annotated
to `GO:0080185`; AVR4's real function is protecting hyphae from plant
chitinases, and its recognition by Cf-4 is a host process
([PLANT_FUNGAL_INTERACTIONS](../../PLANT_FUNGAL_INTERACTIONS.md)).

*Provenance:* [GOC+]. Sources:
[Drive: Intro - Host-Pathogen interaction session](https://drive.google.com/open?id=1FcqOAw-yKqDyM8KvFaGCnt_fY1ox4bMjVehlkkObY70);
[Drive: Interspecies interaction - level of granularity](https://drive.google.com/open?id=1035MddHFPgk1n2v1TnOTAqFS6FTymDqk2dw76lsZ48E);
[PLANT_FUNGAL_INTERACTIONS](../../PLANT_FUNGAL_INTERACTIONS.md).

<a id="mo-5"></a>

### MO-5. Give an effector its molecular function, its host target and its host location, not only a process term.

An effector annotation set is complete when it has: the MF the effector
performs (a catalytic activity, an inhibitor activity, a sequestering
activity, a binding term with a specific ligand), with `has input` the host
target; a host CC term for where it acts; and the symbiont-mediated or
effector-mediated BP. A process term alone hides the mechanism and makes it
impossible to tell effectors apart.

*Example.* OspC3 (MO-1) has all four parts. In the plant-fungal reviews, the
LysM effector Slp1 lacked chitin binding (`GO:0008061`) and PWL2 had locations
only; each of the four chitin-binding proteins (ECP6, AVR4, Slp1 and the
receptors) now carries its own mechanism.

*Provenance:* [GOC+]. Sources:
[PLANT_FUNGAL_INTERACTIONS](../../PLANT_FUNGAL_INTERACTIONS.md);
GO-CAM `62b4ffe300002385`.

<a id="mo-6"></a>

### MO-6. Use a single-organism process term only for a process within the organism that encodes the gene product.

A toxin that blocks neurotransmitter release in its victim is not annotated
to `GO:0046929` negative regulation of neurotransmitter secretion; that term
describes a process within a metazoan. Use the symbiont or venom term,
`GO:0044762` symbiont-mediated suppression of host neurotransmitter secretion.
Taxon constraints on single-organism terms are correct and should not be
relaxed to admit toxin or viral annotations.

*Example.* A botulinum neurotoxin encoded by a *Clostridium botulinum* phage
triggered a taxon violation on `GO:0046929`; the fix was the symbiont term
([go-annotation#4582](https://github.com/geneontology/go-annotation/issues/4582)).

*Provenance:* [GOC]. Sources:
[go-annotation#4582](https://github.com/geneontology/go-annotation/issues/4582);
[Drive: Multi-species terms - documentation to review](https://drive.google.com/open?id=12_2bJFup0Wn9TVYlysfbxFz8YERibJ4OXDB8GRowueU).

<a id="mo-7"></a>

### MO-7. Locate symbiont products in host compartments with host CC terms, and virion proteins with virion terms.

A symbiont protein that acts inside or on a host cell takes a term under
`GO:0018995` host cellular component (`GO:0030430` host cell cytoplasm,
`GO:0042025` host cell nucleus, `GO:0020002` host cell plasma membrane,
`GO:0033644` host cell membrane), not the plain cellular term. A structural
protein of the virus particle takes a term under `GO:0044423` virion component
(`GO:0019028` viral capsid, `GO:0055036` virion membrane, `GO:0019031` viral
envelope). Host proteins that are incorporated into virions are not annotated to
virion terms. The plain cellular terms (cytoplasm, nucleus) are for gene
products located in the organism that makes them under normal conditions.

*Rationale.* The host branch exists to keep pathological localisations out of
the normal CC annotations
([Drive: host_symbiont_annotation](https://drive.google.com/open?id=1NiJfYB4JmClhbsr4G3Xwwr-6Bw4GWXGJ)).
For GO-CAM, host CC terms do not resolve to a compartment in the repository's
spatial model; edges into them cross organisms
([GOCAM_COMPARTMENTS](../../GOCAM_COMPARTMENTS.md)).

*Provenance:* [GOC]. Sources: as above;
[Drive: Multi-species terms - documentation to review](https://drive.google.com/open?id=12_2bJFup0Wn9TVYlysfbxFz8YERibJ4OXDB8GRowueU).

<a id="mo-8"></a>

### MO-8. Record the other organism for interspecies annotations, and only for physiological interactions.

For an annotation to a term under `GO:0044419`, record the interacting
organism. The long-standing mechanism is a second taxon in GAF column 13
(gene product's taxon first, interacting taxon second; the same taxon twice for
an intraspecies interaction). A 2020 announcement recommended moving to a
`has input` extension naming the interacting organism or its gene product; GAF
2.2 and GPAD 2.0 kept the interacting-taxon field, and several groups do not
use extensions. Until the GOC decides, record the interacting taxon in the
taxon field and, where the host target gene product is known, add it as `has
input` on the MF.

Do not add a second taxon to annotations made by sequence similarity, and do
not create interspecies binding annotations from heterologous experiments
(a human protein screened against a mouse library, a protein expressed in COS
cells). An interspecies interaction annotation states that the two proteins
meet in nature. For a heterologous experiment, the partner identifier goes in
WITH/FROM, describing the experiment.

*Provenance:* [GOC+]. Sources:
[Drive: Multi-species terms - documentation to review](https://drive.google.com/open?id=12_2bJFup0Wn9TVYlysfbxFz8YERibJ4OXDB8GRowueU);
[go-annotation#3514](https://github.com/geneontology/go-annotation/issues/3514);
[go-annotation#3314](https://github.com/geneontology/go-annotation/issues/3314);
[Drive: host_symbiont_annotation](https://drive.google.com/open?id=1NiJfYB4JmClhbsr4G3Xwwr-6Bw4GWXGJ).

<a id="mo-9"></a>

### MO-9. On the host side, annotate participation in defence to the most specific defence or immune term the evidence supports, and keep response-to and susceptibility separate.

Use this ladder:

1. **Recognition and signalling components** take the receptor or signalling
   MF and the pathway BP: `GO:0038187` pattern recognition receptor activity,
   `GO:0002221` pattern recognition receptor signaling pathway, `GO:0045087`
   innate immune response or a child such as `GO:0140374` antiviral innate
   immune response.
2. **Effectors** that act on the microbe take the defence term for the target
   class: `GO:0042742` defense response to bacterium (or `GO:0050829`/
   `GO:0050830` for Gram-negative/Gram-positive), `GO:0050832` defense response
   to fungus, `GO:0051607` defense response to virus; for antimicrobial
   peptides, `GO:0061844` antimicrobial humoral immune response mediated by
   antimicrobial peptide.
3. **Direct restriction factors** acting on a viral step take the host-side
   regulation term (`GO:0045071` negative regulation of viral genome
   replication).
4. **Transcriptional induction alone** supports at most `GO:0009617` response
   to bacterium or `GO:0009615` response to virus, and in reviews is
   non-core.
5. **A susceptibility factor** whose loss increases resistance is a negative
   regulator: `defense response` becomes negative regulation of defense
   response, not defense response.

Use "immune response" terms for organisms with an immune system as GO defines
it; for bacteria and archaea (CRISPR, restriction-modification, abortive
infection) use defence terms. In the current ontology, `GO:0045087` innate
immune response is a subclass of `GO:0140546` defense response to symbiont,
so defence is the grouping term and nothing is lost.

*Example.* MLO in barley and Arabidopsis MLO2 had `defense response` rows;
both reviews changed the sign to negative regulation of defense response,
because loss of MLO gives powdery mildew resistance
([PLANT_FUNGAL_INTERACTIONS](../../PLANT_FUNGAL_INTERACTIONS.md)). Genes known
only from infection phenotypes (LYM2, CYP79B2) did not get `defense response to
fungus`; genes that do part of the work (CYP71B15 making camalexin, ABCG36
exporting it) did.

*Provenance:* [GOC+]. Sources:
[Drive: Combined multiorg + immune system process call 2021-11-22](https://drive.google.com/open?id=1fSGDMGKS4ogdCrTW8LWGltx_6acLWY5rxhTez_N98so);
[wiki: Immunology Revisions](https://wiki.geneontology.org/index.php/Immunology_Revisions);
[INNATE_IMMUNITY](../../INNATE_IMMUNITY.md);
[PLANT_FUNGAL_INTERACTIONS](../../PLANT_FUNGAL_INTERACTIONS.md).

<a id="mo-10"></a>

### MO-10. An induced effector is not a participant in the signalling pathway that induces it, and an enzyme that makes a second messenger is not a regulator of the virus.

Antimicrobial peptides, interferon-stimulated genes and lysozymes are outputs
of immune signalling. They take defence terms for what they do (MO-9), not the
signalling-pathway term (Toll signalling, type I interferon signalling). Apply
the participation test from [CLAUDE.md](../../../CLAUDE.md): which entity
performs the step?

Cytokine "production" terms (`GO:0001816` cytokine production, `GO:0032606`
type I interferon production and their kin) are in the do-not-annotate subset
since 2021, because synthesis and secretion are not specific programmes; their
regulation terms remain annotatable.

*Example.* cGAS (`GO:0061501` 2',3'-cyclic GMP-AMP synthase activity) was
annotated as a regulator of the viral life cycle. The cyclic dinucleotide is
the signal; the enzyme makes it. The fix was the enzyme activity and the
signalling process, not a viral-process term
([go-annotation#1979](https://github.com/geneontology/go-annotation/issues/1979)).

*Provenance:* [GOC+]. Sources:
[INNATE_IMMUNITY](../../INNATE_IMMUNITY.md) (curation question 7);
[Drive: Combined multiorg + immune system process call 2021-11-22](https://drive.google.com/open?id=1fSGDMGKS4ogdCrTW8LWGltx_6acLWY5rxhTez_N98so);
[go-annotation#1979](https://github.com/geneontology/go-annotation/issues/1979).

<a id="mo-11"></a>

### MO-11. Keep mutualistic programmes separate from defence.

Nodulation (`GO:0009877`) and arbuscular mycorrhizal association
(`GO:0036377`) are symbiosis processes, annotated separately from defence even
when the same receptors (LysM receptor kinases, CERK1) take part in both. A
gene in the common symbiosis pathway does not get defence terms because a
chitin-like signal is involved.

*Example.* Rice CERK1 had no symbiosis term in GOA; the review added
arbuscular mycorrhizal association as a separate core function from chitin
immunity. NORK, DMI1, CASTOR and CYCLOPS carry nodulation and mycorrhizal terms
and no defence terms ([PLANT_FUNGAL_INTERACTIONS](../../PLANT_FUNGAL_INTERACTIONS.md)).

*Provenance:* [GOC+]. Source:
[PLANT_FUNGAL_INTERACTIONS](../../PLANT_FUNGAL_INTERACTIONS.md).

<a id="mo-12"></a>

### MO-12. Check taxon fit before accepting an inferred multi-organism or immune annotation.

Phylogenetic and electronic annotations spread host-defence and symbiont terms
into lineages where the biology differs. Before accepting an IBA, ISS or IEA row
in this area, check that:

- a symbiont-side term is on a symbiont's gene product (taxon-constrained terms
  are designed to fail on hosts: `GO:0052042` symbiont-mediated activation of
  host programmed cell death is never in Metazoa or plants);
- a vertebrate-specific process (type I interferon, adaptive immunity) is not
  on an invertebrate orthologue;
- a ligand-specific term (LPS recognition, the fly Toll pathway) has not been
  spread to paralogues or orthologues that cannot share the ligand.

*Example.* The Drosophila Toll-pathway term leaked onto human IRAK4 and MYD88 by
phylogenetic inference, and LPS and lipopeptide receptor terms were spread
across TLR partners that do not bind those ligands
([INNATE_IMMUNITY](../../INNATE_IMMUNITY.md)).

*Provenance:* [GOC] for taxon constraints; [GOC+] for the review checklist.
Sources:
[go-annotation#2720](https://github.com/geneontology/go-annotation/issues/2720);
[INNATE_IMMUNITY](../../INNATE_IMMUNITY.md);
[phylogenetic-propagation.md](phylogenetic-propagation.md).

## Rules: Part B, non-coding RNAs

<a id="mo-13"></a>

### MO-13. Annotate the mature, functional RNA, identified by an RNAcentral or MOD identifier.

The annotated object is the RNA that does the work: for a miRNA, the mature
5p or 3p strand, not the precursor or stem-loop; for a lncRNA, the primary
transcript identifier, not degradation fragments or alternative records of the
same locus. Use RNAcentral URS identifiers with taxon (`URS..._9606`) or the
MOD's ncRNA gene identifier. If an RNA has no stable identifier (many
siRNAs), annotate nothing to the RNA, but annotate the proteins of the
pathway as usual.

For a miRNA cluster studied as a whole, annotate the individual mature miRNAs
that the authors show or predict to act; if the experiment perturbs the whole
cluster, use IGI with the other predicted miRNAs in WITH/FROM, and make no MF
annotation.

*Example.* Rfam2GO propagated a FlyBase annotation for mature dme-miR-998 to
four precursor and stem-loop records; FlyBase asked for the mapping to be
fixed ([go-annotation#4195](https://github.com/geneontology/go-annotation/issues/4195)).
RNAcentral propagation put a mouse lncRNA annotation on fragments of the same
locus ([go-annotation#4954](https://github.com/geneontology/go-annotation/issues/4954)).

*Provenance:* [GOC]. Sources: as above;
[wiki: MicroRNA GO annotation manual](https://wiki.geneontology.org/index.php/MicroRNA_GO_annotation_manual);
[wiki: SiRNA GO annotation manual](https://wiki.geneontology.org/index.php/SiRNA_GO_annotation_manual).

<a id="mo-14"></a>

### MO-14. Give an RNA an RNA-specific function term; bare `RNA binding` and `protein binding` are not functions for an ncRNA.

| What the RNA does | MF | Typical BP |
|---|---|---|
| Base-pairs with an mRNA to repress it (miRNA, siRNA, some lncRNAs) | `GO:1903231` mRNA base-pairing post-transcriptional repressor activity | `GO:0035195` miRNA-mediated post-transcriptional gene silencing; `GO:0140766` siRNA-mediated ...; `GO:0000512` lncRNA-mediated ... |
| Base-pairs with a miRNA to block it | `GO:0140869` miRNA inhibitor activity via base-pairing | `GO:0000512`; `GO:0140958` target-directed miRNA degradation where it applies |
| Recruits a protein to chromatin | `GO:0140463` chromatin-protein adaptor activity | `GO:0006325` chromatin organization; `GO:0060816` random inactivation of X chromosome |
| Forms a DNA-RNA triplex and recruits a protein | `GO:0141180` dsDNA-RNA triple helix-forming chromatin adaptor activity | as above |
| Brings a protein to a specific RNA | `GO:0160134` protein-RNA sequence-specific adaptor activity | the silencing or processing BP |
| Holds a protein away from its targets | `GO:0140311` protein sequestering activity | negative regulation of the target's process |
| Nucleates a condensate | `GO:0140693` molecular condensate scaffold activity | `GO:0030575` nuclear body organization |
| Guides a modification enzyme to a site | `GO:0030561` RNA 2'-O-ribose methylation guide activity; `GO:0030559` rRNA pseudouridylation guide activity | `GO:0000451` rRNA 2'-O-methylation; `GO:0031118` rRNA pseudouridine synthesis |
| Catalyses a reaction (ribozyme) | the catalytic term, e.g. `GO:0004526` ribonuclease P activity | as for an enzyme |
| Coregulates transcription | `GO:0003713` transcription coactivator activity | regulation of transcription |

`mRNA 3'-UTR binding` (`GO:0003730`) is not needed for a canonical miRNA,
because almost all act there; use a specific mRNA-region binding term only when
the miRNA binds elsewhere.

*Example.* Mouse Cyrano (Oip5os1) has `GO:0140869` with `has input` miR-7a-5p
and miR-7b-5p, and BP `GO:0140958` target-directed miRNA degradation
(PMID:29887379). Human NEAT1 has `GO:0140693` and `GO:0030575` nuclear body
organization (PMID:19716791). Both examples are from the lncRNA manual.

*Provenance:* [GOC] for the terms and examples; [GOC+] for the ban on bare
binding, which follows from the general binding policy. Sources:
[wiki: LncRNA GO annotation manual](https://wiki.geneontology.org/index.php/LncRNA_GO_annotation_manual);
[PMID:39374113](https://europepmc.org/article/MED/39374113);
[Drive: ncRNA Update](https://drive.google.com/open?id=1kxTQvGwlxlXWYrVcopDCoNrJ3deM2gNfCu7tg0VfDos).

<a id="mo-15"></a>

### MO-15. Annotate a miRNA target with BP plus `has input`; add the MF only from the paper that shows binding.

The 2024 decision table:

| Evidence in hand | Annotation |
|---|---|
| Change in target protein or mRNA when the miRNA is added or inhibited, target predicted or shown to bind elsewhere | `involved_in` `GO:0035195` (or a child, MO-17), `has input` target gene |
| Plus binding shown in this paper (reporter with the target's UTR and a seed-site mutant, or in vivo deletion of the response element) | also `enables` `GO:1903231`, `has input` target gene, `part of` the BP |
| Target only predicted (TargetScan, miRBase, other tools), no functional data | nothing |
| Functional effect, but no prediction or binding evidence can be found | `GO:0010629` negative regulation of gene expression, no target |
| High-throughput binding alone (CLIP, CLASH) | not enough; needs a low-throughput regulation assay as well |
| Sequencing or expression profiling alone | nothing |

The target identifier is the UniProt or MOD gene identifier. Binding evidence
may come from another paper for the `has input` on the BP, but the MF row must
be made from the paper that has the binding experiment.

A miRNA that activates transcription (by binding a promoter) takes the
transcription terms; if only an increase in target mRNA is shown, use
`GO:0010628` positive regulation of gene expression with `has input`.

*Provenance:* [GOC]. Sources:
[wiki: MicroRNA GO annotation manual](https://wiki.geneontology.org/index.php/MicroRNA_GO_annotation_manual);
[Drive: ncRNA Update](https://drive.google.com/open?id=1kxTQvGwlxlXWYrVcopDCoNrJ3deM2gNfCu7tg0VfDos);
[PMID:26917558](https://europepmc.org/article/MED/26917558).

<a id="mo-16"></a>

### MO-16. For RNA experiments, adding the RNA is IDA, removing or blocking it is IMP, a reporter assay is IDA, and expression change is never evidence of function.

- miRNA mimic, pre-miR or overexpression of an unchanged sequence: **IDA**. If
  the miRNA is expressed where it normally is not, consider IMP.
- Antagomir, LNA inhibitor, knockout, eraser, or a sponge designed against one
  miRNA: **IMP**. A sponge against a seed family cannot be attributed to one
  miRNA; do not annotate.
- Luciferase or other reporter carrying the target UTR: **IDA**, not IGI. The
  assay measures the miRNA acting on the target; it does not test two genes
  working together.
- **IGI** only when two gene products are perturbed and the inference depends on
  both (a protein's effect on a target abolished by blocking the miRNA).
- **IEP** never supports a miRNA function annotation; co-expression with a
  condition says nothing about what the miRNA does.
- siRNA knockdown of a protein-coding gene is a perturbation of that gene:
  **IMP** (or the ECO class `ECO:0000019` RNAi evidence, a phenotypic-evidence
  sibling of IMP). It is not evidence about any siRNA.

*Provenance:* [GOC]. The reporter-assay rule resolves a conflict between the
miRNA manual's IGI examples and the IGI page (see Differences). Sources:
[wiki: MicroRNA GO annotation manual](https://wiki.geneontology.org/index.php/MicroRNA_GO_annotation_manual);
[wiki: Inferred from Genetic Interaction (IGI)](https://wiki.geneontology.org/index.php/Inferred_from_Genetic_Interaction_%28IGI%29);
[go-annotation#1407](https://github.com/geneontology/go-annotation/issues/1407).

<a id="mo-17"></a>

### MO-17. Choose the silencing child term from what was measured.

| Measured | Term (miRNA) | Term (siRNA) |
|---|---|---|
| target protein falls; mRNA not measured | `GO:0035195` | `GO:0140766` |
| target mRNA and protein fall | `GO:0035279` miRNA-mediated gene silencing by mRNA destabilization | `GO:0090625` siRNA-mediated gene silencing by mRNA destabilization |
| target protein falls, mRNA unchanged | `GO:0035278` miRNA-mediated gene silencing by inhibition of translation | `GO:0070549` siRNA-mediated gene silencing by inhibition of translation |

Cleavage by AGO2 is a form of destabilization and takes the same term; only
AGO2 among the human Argonautes has endonuclease activity, so the
cleavage mechanism should not be attributed to AGO1, AGO3 or AGO4.

For siRNA-directed chromatin silencing, use the specific terms only where the
mechanism exists: `GO:0140727` siRNA-mediated pericentric heterochromatin
formation (fission yeast-type), `GO:1902795` siRNA-mediated facultative
heterochromatin formation (gene-specific repression), `GO:0080188` gene
silencing by siRNA-directed DNA methylation (initiated by DNA methylation, as
in plant RdDM).

*Provenance:* [GOC]. Sources:
[wiki: SiRNA GO annotation manual](https://wiki.geneontology.org/index.php/SiRNA_GO_annotation_manual);
[wiki: MicroRNA GO annotation manual](https://wiki.geneontology.org/index.php/MicroRNA_GO_annotation_manual);
[Drive: ncRNA Update](https://drive.google.com/open?id=1kxTQvGwlxlXWYrVcopDCoNrJ3deM2gNfCu7tg0VfDos).

<a id="mo-18"></a>

### MO-18. Downstream processes of a miRNA are regulation terms and non-core; context extensions need evidence of endogenous expression.

A miRNA that represses a target in a signalling pathway may be annotated to
regulation of that pathway or of a cellular outcome (`GO:2000145` regulation of
cell motility) with IDA or IMP, even when the targets are unknown. These are
regulation terms, never participation in the pathway, and in a review they are
`KEEP_AS_NON_CORE`: the core function is the silencing of named targets.

Add a cell type or tissue with `occurs_in` only when inhibiting the miRNA
changes the endogenous target in that cell, or when the miRNA is shown to be
expressed there and the authors are confident the target is regulated there.
Do not add a cancer cell type; an established line standing in for a normal
cell type may be used.

*Provenance:* [GOC] for the extension rules; [GOC+] for the non-core verdict.
Sources:
[wiki: MicroRNA GO annotation manual](https://wiki.geneontology.org/index.php/MicroRNA_GO_annotation_manual);
[Drive: ncRNA Update](https://drive.google.com/open?id=1kxTQvGwlxlXWYrVcopDCoNrJ3deM2gNfCu7tg0VfDos).

<a id="mo-19"></a>

### MO-19. Annotate proteins that change miRNA levels to the step they act on; the core processing machinery carries no specific miRNA or mRNA in extensions.

- A TF that drives a pri-miRNA: `GO:0061614` miRNA transcription or its
  regulation terms, with `has input` the miRNA gene.
- Processing enzymes: `GO:0031053` primary miRNA processing (DROSHA, DGCR8),
  `GO:0031054` pre-miRNA processing (DICER1). DROSHA and DICER1 enable
  `GO:0004525` ribonuclease III activity.
- An agent that changes miRNA level by an unknown step: `GO:0010468`
  regulation of gene expression (or its signed children) with `has input` the
  miRNA.
- Do not use `GO:0010586` miRNA metabolic process for biogenesis; it covers
  catabolism and isoform formation. Target-directed degradation is
  `GO:0140958`.

Do not put a miRNA identifier (or an mRNA identifier, for Argonaute) in the
extension of an annotation to the general machinery; the pathway serves
thousands of miRNAs and the extension carries no information.

*Example.* TGF-beta1 lowering miR-29b in aortic fibroblasts by an unknown step
is `GO:0010629` negative regulation of gene expression, IDA, `has_input`
miR-29b, `occurs_in` the fibroblast type (PMID:22269326, as worked in the miRNA
manual).

*Provenance:* [GOC]. Sources:
[wiki: MicroRNA GO annotation manual](https://wiki.geneontology.org/index.php/MicroRNA_GO_annotation_manual);
[MIRNA_DEGRADATION](../../MIRNA_DEGRADATION.md).

<a id="mo-20"></a>

### MO-20. For a lncRNA, establish the mechanism class first, and distinguish the RNA's activity from the act of transcribing the locus.

Classify the lncRNA's reported mechanism (miRNA inhibitor, TDMD trigger,
base-pairing repressor, chromatin adaptor, triplex adaptor, protein
sequestration, condensate scaffold, coregulator, enzyme inhibitor) and use the
matching term from MO-14. Two distinctions decide most cases:

- **Sponge versus TDMD.** If the lncRNA level stays constant while its miRNA
  falls, the lncRNA is a TDMD trigger (`GO:0140958`). If the lncRNA falls with
  the miRNA, it is not TDMD; use `GO:0140869` with the silencing BP, or
  `GO:0010587` miRNA catabolic process where degradation is shown. A sponge
  needs a large molar excess over its miRNA to work; treat sponge claims for
  low-abundance lncRNAs with caution.
- **Product versus locus.** A deletion or promoter knockout of a lncRNA gene
  removes DNA elements and the act of transcription as well as the RNA. A
  BP annotation that depends on the RNA product needs an experiment that
  removes the RNA without removing the locus (antisense knockdown,
  polyadenylation-signal insertion) or that restores function with the RNA
  expressed elsewhere. Otherwise the evidence supports only a role for the
  locus, and the annotation should say so in the review.

*Provenance:* [GOC] for the sponge versus TDMD test; [NEW] for the
product-versus-locus requirement, which the lncRNA manual does not address.
Sources:
[wiki: LncRNA GO annotation manual](https://wiki.geneontology.org/index.php/LncRNA_GO_annotation_manual);
[PMID:39374113](https://europepmc.org/article/MED/39374113).

<a id="mo-21"></a>

### MO-21. A guide RNA's family supports its guide activity; its target-specific process needs the target.

A box C/D snoRNA family member may carry `GO:0030561` RNA 2'-O-ribose
methylation guide activity, and an H/ACA snoRNA `GO:0030559` rRNA
pseudouridylation guide activity (or the general `GO:0030555` RNA modification
guide activity when the target class is unknown), on the strength of family
membership and a sequence-based assignment (ISS or ISM with the reference
family). The process term (`GO:0000451` rRNA 2'-O-methylation) needs a
predicted or mapped target site in rRNA; methylation-guide snoRNAs also target
snRNAs, and orphan snoRNAs have no known target and take the MF only.

*Rationale.* The evidence code committee argued in the 2000s that box C/D
membership, validated against experimentally proven snoRNAs, is good evidence
for methylation guide activity but not for involvement in rRNA processing.

*Provenance:* [GOC+]. Source:
[wiki: Responses to MGI from Karen](https://wiki.geneontology.org/index.php/Responses_to_MGI_from_Karen) (correspondence; old).

## Decision aid

**Host or symbiont term?**

| Question | Yes | No |
|---|---|---|
| Is the gene product encoded by the smaller partner and acting on the larger? | symbiont-mediated / effector-mediated term, host CC, host target as input | next question |
| Is it the host's own component acting against the symbiont? | defence term, host-mediated suppression, or negative regulation of viral process | next question |
| Is it a host component the symbiont exploits? | normal host function only; dependence recorded on the symbiont side | next question |
| Is the evidence only that the host responds to the symbiont's presence? | host-side response term on host genes; nothing on the symbiont gene | |

**Which miRNA annotation?**

| Assay | Code | BP | MF |
|---|---|---|---|
| mimic, target protein down | IDA | `GO:0035195` + has input | none |
| inhibitor, target protein and mRNA up | IMP | `GO:0035279` + has input | none |
| reporter with UTR, seed mutant abolishes effect | IDA | `GO:0035195` + has input | `GO:1903231` + has input + part of |
| CLIP alone | none | none | none |
| miRNA changes with disease | none (IEP not allowed) | none | none |
| protein changes miRNA level, step unknown | IDA/IMP on the protein | `GO:0010468` child + has input miRNA | none |

## Common errors

| Error | Example | Fix |
|---|---|---|
| Host protein on a symbiont-process term | human proteins on `GO:0046718` symbiont entry into host cell; 59 of 206 annotations to the host programmed cell death symbiont term were host proteins (2021) | remove (electronic) or mark over-annotated (experimental); use the host's normal function |
| Host protein on viral translation or replication | SSB, PCBP2 on `GO:0075522` | as above |
| Keyword mapping to viral process | KW-0945 mapped CENP-A to viral process | mapping removed in 2016; remove remaining rows |
| PAMP-bearing protein on "activation of host immunity" | flagellin, toxin annotated to induction of host defence | no symbiont term; host receptors get the recognition terms |
| Single-organism term on a toxin | botulinum toxin on `GO:0046929` | `GO:0044762` |
| Plain CC for a symbiont protein in a host | effector on `GO:0005737` cytoplasm | `GO:0030430` host cell cytoplasm |
| Effector with process only | PWL2 with locations only | add MF, target, host CC |
| Antimicrobial effector on the inducing pathway | AMP on Toll signalling pathway | defence term for its target class |
| Susceptibility factor on defence response | MLO on defense response | negative regulation of defense response |
| Toll term on human IRAK4 by IBA | lineage-specific pathway term propagated | review the PAINT node; [phylogenetic-propagation.md](phylogenetic-propagation.md) |
| Precursor miRNA annotated | Rfam2GO on dme-mir-998 stem-loop | annotate the mature 5p/3p record |
| miRNA MF from prediction | GO:1903231 with a TargetScan target only | no annotation; BP with has input only if a functional effect is shown |
| IGI for a reporter assay | miR-133 reporter as IGI | IDA |
| miRNA annotated from expression | IEP to a disease process | do not annotate |
| ncRNA with bare RNA binding | lncRNA `GO:0003723` RNA binding | the mechanism term from MO-14 |
| Core machinery with a miRNA extension | DICER1 `GO:0031054` with has input miR-X | remove the extension |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [Drive: Multi-species terms - documentation to review](https://drive.google.com/open?id=12_2bJFup0Wn9TVYlysfbxFz8YERibJ4OXDB8GRowueU) (wiki-derived, marked "to be reviewed") | Use terms under multi-organism process `GO:0051704` and CC other organism `GO:0044215`. | Use `GO:0044419` descendants and `GO:0018995` host cellular component descendants (MO-1, MO-7). | Both old roots are obsolete; `GO:0044419` itself is do-not-annotate, so annotate to its children. |
| Same | If a symbiont affects a normal host process, request a new term in the multi-organism node rather than annotate the normal term with two taxa. | Unchanged in spirit; the new terms now follow the "symbiont-mediated perturbation/suppression/activation of host X" pattern (MO-1, MO-6). | The 2023-2024 relabelling made agency explicit and removed separate "by virus" terms. |
| [go-annotation#1367](https://github.com/geneontology/go-annotation/issues/1367) (2016) vs [go-annotation#1](https://github.com/geneontology/go-annotation/issues/1), [#1507](https://github.com/geneontology/go-annotation/issues/1507), [#1891](https://github.com/geneontology/go-annotation/issues/1891) | 2016: host proteins co-opted for a parasitic process may be annotated to it. Other threads: host proteins should not carry viral-process terms. | Do not annotate co-opted host proteins to symbiont processes; host-side regulation and defence terms remain (MO-3). | The sources conflict. The 2021 working group's first aim (normal functions only) and the annotation counts in #3814 support the stricter reading. A 2021 call raised a possible exception (T7 using host thioredoxin as a processivity factor); see Open questions. |
| [go-annotation#3514](https://github.com/geneontology/go-annotation/issues/3514) (2020) | Migrate the interacting species from the taxon field to a `has input` extension. | Keep the interacting taxon field; add `has input` for a known host target (MO-8). | GAF 2.2 and GPAD 2.0 kept the field; most groups making these annotations did not use extensions. |
| Pre-2021 ontology | "induction by symbiont of host defense response" and similar terms were available. | Never annotate a symbiont product to activation of host immunity because it is recognised (MO-4). | Obsoleted by the working group (`GO:0044416` is obsolete). |
| [Drive: Intro - Host-Pathogen interaction session](https://drive.google.com/open?id=1FcqOAw-yKqDyM8KvFaGCnt_fY1ox4bMjVehlkkObY70) (2021) | Kept an effector-mediated term for deliberate induction of plant hypersensitive response (`GO:0080185`) as the exception. | Use it only for effectors whose evolved role is induction, and request a move out from under suppression (MO-4). | The current ontology places `GO:0080185` under `GO:0052170` symbiont-mediated suppression of host innate immune response, so every annotation inherits a contradictory claim. |
| [Drive: Interspecies interaction - level of granularity](https://drive.google.com/open?id=1035MddHFPgk1n2v1TnOTAqFS6FTymDqk2dw76lsZ48E) (2023) | The discussion preferred "modulation" to "perturbation". | Use the labels GO adopted ("symbiont-mediated perturbation of host ..."). | The ontology chose "perturbation"; guidelines follow the ontology. |
| [Drive: Combined multiorg + immune system process call 2021-11-22](https://drive.google.com/open?id=1fSGDMGKS4ogdCrTW8LWGltx_6acLWY5rxhTez_N98so) | Left open whether immune system process is a system process; suggested unicellular defence is defence, not immunity. | Use defence terms for prokaryotes; immune terms for animals and plants as GO defines them (MO-9). | `GO:0045087` innate immune response is now a subclass of `GO:0140546` defense response to symbiont, so defence groups both. |
| [wiki: MicroRNA GO annotation manual](https://wiki.geneontology.org/index.php/MicroRNA_GO_annotation_manual) (edited 2026) | Names `GO:1903231` as "mRNA binding involved in posttranscriptional gene silencing" in places; lists `GO:0035278` with the MF label; gives `GO:0035279` as "mRNA cleavage involved in gene silencing by miRNA". | `GO:1903231` mRNA base-pairing post-transcriptional repressor activity (MF); `GO:0035278` and `GO:0035279` are the BP children in MO-17. | Labels and merges changed after the examples were written; the [ncRNA Update deck](https://drive.google.com/open?id=1kxTQvGwlxlXWYrVcopDCoNrJ3deM2gNfCu7tg0VfDos) shows an intermediate label, "mRNA base-pairing translational repressor activity". |
| [wiki: MicroRNA GO annotation manual](https://wiki.geneontology.org/index.php/MicroRNA_GO_annotation_manual) vs [wiki: IGI](https://wiki.geneontology.org/index.php/Inferred_from_Genetic_Interaction_%28IGI%29) | The manual uses IGI for some miRNA-target annotations and for whole-cluster experiments. The IGI page says a reporter assay is IDA, not IGI. | Reporter assays are IDA; IGI only when two gene products are perturbed (protein plus miRNA, or a whole cluster) (MO-16). | Both are right for different experiments; the manual's examples did not draw the line. |
| [wiki: IGI](https://wiki.geneontology.org/index.php/Inferred_from_Genetic_Interaction_%28IGI%29) | Example extensions use `has_direct_input` and `regulates_expression_of`. | `has input` (MO-15). | `has_direct_input` was merged into `has input` (2020 annotation call); the other relation is not used for miRNA targets in the current manual. |
| [wiki: MicroRNA GO annotation manual](https://wiki.geneontology.org/index.php/MicroRNA_GO_annotation_manual) and [Drive: ncRNA Update](https://drive.google.com/open?id=1kxTQvGwlxlXWYrVcopDCoNrJ3deM2gNfCu7tg0VfDos) | Manual: add the cell type when the cell normally expresses the miRNA. Deck: do not add a cancer cell type. | Both conditions (MO-18). | Complementary rules from two documents. |
| [wiki: MicroRNA GO annotation manual](https://wiki.geneontology.org/index.php/MicroRNA_GO_annotation_manual) | Downstream-process annotations of miRNAs are allowed with IDA. | Allowed, as regulation terms, and non-core in reviews (MO-18). | The manual does not rank them; the review's core function is silencing of named targets. |
| [wiki: LncRNA GO annotation manual](https://wiki.geneontology.org/index.php/LncRNA_GO_annotation_manual) | Examples include a malformed identifier ("UniProtKB:Q62504Q8VEK3" for Xist partners) and a mouse lncRNA (Mhrt) given a `_9606` RNAcentral suffix. | Check identifiers and taxon suffixes when copying the manual's examples. | Errors in the source text; reported here so they are not propagated. |
| [wiki: LncRNA GO annotation manual](https://wiki.geneontology.org/index.php/LncRNA_GO_annotation_manual) | Silent on whether a locus deletion supports a claim about the RNA product. | Require evidence that removes the RNA without the locus, or rescues in trans (MO-20). | Locus deletions confound transcription, DNA elements and product. |
| [wiki: Responses to MGI from Karen](https://wiki.geneontology.org/index.php/Responses_to_MGI_from_Karen) (old correspondence) | Predicted snoRNA annotations can be treated as experiment-based. | Family membership supports the guide MF by ISS/ISM; target-specific BP needs a target site (MO-21). | Narrows the claim to what the argument in the source supports. |

## Open questions

1. **Co-opted host factors.** Is there any case where a host gene product
   should carry a viral-process term, for example host thioredoxin acting as
   the processivity factor of T7 DNA polymerase, where the host protein is a
   physical part of the viral machine? If so, GO needs a term family that keeps
   these out of host-process enrichment (the 2017 thread suggested a separate
   branch).
2. **Virus receptors.** `GO:0001618` virus receptor activity is a binding term
   under exogenous protein binding. Should it be retained, replaced by `has
   input` on the host protein's normal receptor activity, or obsoleted, given
   that "receptor" here describes the virus's use of the protein?
3. **Interacting taxon.** Taxon field or `has input` extension? The 2020
   recommendation was never carried into the file formats.
4. **Immune system process.** Is `GO:0002376` immune system process a system
   process, and should its definition exclude unicellular defence?
5. **`GO:0080185` placement.** Should effector-mediated activation of the plant
   hypersensitive response move out from under suppression of host innate
   immunity?
6. **ncRNA reviews in this repository.** The review pipeline is keyed to UniProt.
   Should ncRNA genes be reviewed with RNAcentral identifiers, and how should
   their GOA rows (many from RNAcentral propagation and Rfam2GO) be fetched?
7. **Phylogenetic propagation for ncRNAs.** miRNA families are deeply conserved,
   but seed identity does not guarantee shared targets. Should Rfam2GO-style
   propagation carry target-specific BP at all, or only MF?
8. **lncRNA product versus locus.** Should GO provide a way to state that a
   function belongs to the act of transcription at a locus rather than to the
   RNA (a qualifier, or a process term on the gene)?

## Sources

**GO Consortium Drive**

- [Ontology/Multiorganisms/Multi-species terms - documentation to review](https://drive.google.com/open?id=12_2bJFup0Wn9TVYlysfbxFz8YERibJ4OXDB8GRowueU) (out of date)
- [Ontology/Multiorganisms/Combined multiorg + immune system process call 2021-11-22](https://drive.google.com/open?id=1fSGDMGKS4ogdCrTW8LWGltx_6acLWY5rxhTez_N98so)
- [Ontology/Multiorganisms/host_symbiont_annotation](https://drive.google.com/open?id=1NiJfYB4JmClhbsr4G3Xwwr-6Bw4GWXGJ) (draft proposal)
- [Ontology/Multiorganisms/Interspecies interaction - level of granularity](https://drive.google.com/open?id=1035MddHFPgk1n2v1TnOTAqFS6FTymDqk2dw76lsZ48E)
- [2021-05 GOC/Intro - Host-Pathogen interaction session](https://drive.google.com/open?id=1FcqOAw-yKqDyM8KvFaGCnt_fY1ox4bMjVehlkkObY70)
- [Ontology/ncRNAs/ncRNA Update](https://drive.google.com/open?id=1kxTQvGwlxlXWYrVcopDCoNrJ3deM2gNfCu7tg0VfDos)

**GO wiki**

- [MicroRNA GO annotation manual](https://wiki.geneontology.org/index.php/MicroRNA_GO_annotation_manual)
- [LncRNA GO annotation manual](https://wiki.geneontology.org/index.php/LncRNA_GO_annotation_manual)
- [SiRNA GO annotation manual](https://wiki.geneontology.org/index.php/SiRNA_GO_annotation_manual)
- [Inferred from Genetic Interaction (IGI)](https://wiki.geneontology.org/index.php/Inferred_from_Genetic_Interaction_%28IGI%29)
- [Multi-species processes](https://wiki.geneontology.org/index.php/Multi-species_processes)
- [Immunology Revisions](https://wiki.geneontology.org/index.php/Immunology_Revisions)
- [Responses to MGI from Karen](https://wiki.geneontology.org/index.php/Responses_to_MGI_from_Karen)

**GitHub issues**

- [go-annotation#1](https://github.com/geneontology/go-annotation/issues/1) (viral terms on host gene products, 2003)
- [go-annotation#1367](https://github.com/geneontology/go-annotation/issues/1367) (viral process from UniProt keyword on CENP-A)
- [go-annotation#1407](https://github.com/geneontology/go-annotation/issues/1407) (evidence code for siRNA knockdown)
- [go-annotation#1507](https://github.com/geneontology/go-annotation/issues/1507) (human genes on viral processes)
- [go-annotation#1891](https://github.com/geneontology/go-annotation/issues/1891) (symbiont process on human genes)
- [go-annotation#1979](https://github.com/geneontology/go-annotation/issues/1979) (cGAS and cyclic nucleotide terms)
- [go-annotation#2720](https://github.com/geneontology/go-annotation/issues/2720) (symbiont programmed cell death term on host genes; taxon constraint)
- [go-annotation#3314](https://github.com/geneontology/go-annotation/issues/3314) (interspecies protein binding from IntAct)
- [go-annotation#3514](https://github.com/geneontology/go-annotation/issues/3514) (interacting species as has input)
- [go-annotation#3814](https://github.com/geneontology/go-annotation/issues/3814) (symbiont-specific terms on host proteins)
- [go-annotation#4195](https://github.com/geneontology/go-annotation/issues/4195) (Rfam2GO on miRNA precursors)
- [go-annotation#4582](https://github.com/geneontology/go-annotation/issues/4582) (neurotransmitter secretion term on a toxin)
- [go-annotation#4954](https://github.com/geneontology/go-annotation/issues/4954) (lncRNA annotation on fragments)

**Papers**

- [PMID:26917558](https://europepmc.org/article/MED/26917558) Guidelines for the functional annotation of microRNAs using the Gene Ontology (RNA, 2016)
- [PMID:39374113](https://europepmc.org/article/MED/39374113) Representation of non-coding RNA-mediated regulation of gene expression using the Gene Ontology (RNA Biology, 2024)
- Cited via the manuals' worked examples, not re-read here: [PMID:29887379](https://europepmc.org/article/MED/29887379) (Cyrano and miR-7), [PMID:19716791](https://europepmc.org/article/MED/19716791) (NEAT1), [PMID:22269326](https://europepmc.org/article/MED/22269326) (TGF-beta1 and miR-29b)

**Repository pages**

- [CLAUDE.md](../../../CLAUDE.md)
- [INNATE_IMMUNITY](../../INNATE_IMMUNITY.md)
- [ADAPTIVE_IMMUNITY](../../ADAPTIVE_IMMUNITY.md)
- [PLANT_FUNGAL_INTERACTIONS](../../PLANT_FUNGAL_INTERACTIONS.md)
- [PHAGES](../../PHAGES.md) (phage life-cycle terms; true biological absences of modules)
- [PARASITES](../../PARASITES.md) and [PARASITE_IMMUNE_MODULATORS](../../PARASITE_IMMUNE_MODULATORS.md)
- [CAEEL_SURVEILLANCE_IMMUNITY](../../CAEEL_SURVEILLANCE_IMMUNITY.md)
- [MIRNA_DEGRADATION](../../MIRNA_DEGRADATION.md)
- [GOCAM_COMPARTMENTS](../../GOCAM_COMPARTMENTS.md)
- GO-CAM `62b4ffe300002385` (Shigella OspC3 and human CASP4), cached under `gocams/`
