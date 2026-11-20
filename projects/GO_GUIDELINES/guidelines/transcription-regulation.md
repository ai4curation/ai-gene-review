# Transcription regulation: GO annotation guidelines

Status: draft v0.1 (2026-11-15) · Part of [GO_GUIDELINES](../../GO_GUIDELINES.md)

**In brief:**

- Classify each transcription activity as one of four kinds before choosing terms: RNA
  polymerase, general transcription factor (GTF), DNA-binding transcription factor
  (dbTF), or transcription coregulator (coTF). Proteins that act on transcription
  regulators away from chromatin are a fifth, separate kind.
- A dbTF annotation needs two things shown for the protein itself: sequence-specific
  binding to double-stranded DNA that gives a genomic address, and regulation of target
  genes through that binding. A DNA-binding domain alone is not enough, and neither is a
  ChIP peak or a nuclear-extract gel shift.
- A coTF acts at a specific locus through a dbTF (or through a mark a dbTF caused to be
  laid down). Most coTFs do not bind DNA; those that bind DNA without sequence
  specificity stay coTFs.
- Chromatin enzymes, readers and chaperones get their own activity. They get a
  transcription-regulation annotation only when gene-specific recruitment and an effect
  on those genes are shown; a global chromatin defect is not regulation of transcription.
- Use RNA polymerase II-specific terms for eukaryotic protein-coding genes without
  waiting for the paper to say so. Name target genes with `has_input`, one target per
  annotation, direct targets only.

## Scope

This document covers molecular function (MF) and biological process (BP) annotation of
proteins that carry out or regulate DNA-templated transcription: RNA polymerases, GTFs,
dbTFs (including nuclear receptors, bacterial regulators and sigma factors), coTFs,
inhibitors and activators of transcription regulators, and chromatin proteins insofar as
they regulate transcription. It covers the DNA-binding evidence standard, polymerase
specificity, activator versus repressor, cis-regulatory binding terms and target-gene
extensions.

Covered elsewhere: general MF principles and the protein binding policy
([molecular-function.md](molecular-function.md)); evidence codes, including how to
code ChIP and EMSA ([evidence-codes.md](evidence-codes.md)); extension syntax
([annotation-extensions.md](annotation-extensions.md)); signaling pathways ending in a
transcription factor ([regulation-and-signaling.md](regulation-and-signaling.md));
complexes such as Mediator and TFIID ([protein-complexes.md](protein-complexes.md));
GO-CAM models of transcription ([gocam-modeling.md](gocam-modeling.md)); ncRNA and
siRNA-mediated silencing ([multi-organism-and-ncrna.md](multi-organism-and-ncrna.md)).

## Principles

**Transcription was refactored around what each class of protein does.** Between 2017
and 2021 the GO transcription working group and the GREEKC consortium replaced the old
terms with three activity classes: GTFs, "the molecular machine that assembles with the
RNA polymerase at the promoter"; dbTFs, which "provide genomic addresses and specify the
cell types and the conditions under which specific genes are expressed"; and coTFs,
which bridge GTFs and dbTFs, specify the dbTF's effect, or modify chromatin, "normally
... independent of high affinity binding to specific DNA sequences"
([Drive: TF annotation guidelines, archived 2023](https://drive.google.com/open?id=1bqCxx7QUblrc9q4PIynbJzoCXv248UWBxJa7fguJyXs);
[PMID:34461313](https://europepmc.org/article/MED/34461313), Gene Ontology
representation for transcription factor functions, 2021). The 2021 paper is the
canonical reference; the archived Drive guideline adds a four-question checklist,
worked examples and pitfalls, and remains useful.

**Author vocabulary is unreliable.** "Transcription factor" is used for all three
classes, and "coactivator" has been used for a dbTF's dimer partner. Read what the
experiments show, not what the protein is called
([Drive: human TF catalogue talk, 2020](https://drive.google.com/open?id=11wth1xVtY8S5U93KHsiklVWWaa_ORs_CkbRHLV2ewNE)).

**Curate the gene, not the paper.** The guideline asks curators to read the
literature on a gene before deciding between dbTF and coTF, because a single
experiment rarely settles it and earlier papers may be superseded
([Drive: TF annotation guidelines](https://drive.google.com/open?id=1bqCxx7QUblrc9q4PIynbJzoCXv248UWBxJa7fguJyXs)).

**Being required for expression is not regulating transcription.** Many proteins
change a gene's mRNA level without acting on its transcription. GO uses regulation of
gene expression for that, and keeps regulation of transcription for evidence that the
protein acts on transcription itself
([Drive: 2017 transcription guidelines](https://drive.google.com/open?id=0B_c5g4FezmhfNENjNk5RbjJwQUk)).

## Rules

<a id="tr-1"></a>
### TR-1. Classify the activity first: polymerase, GTF, dbTF, coTF, or regulator of a regulator

**Before choosing terms, decide which class of transcription activity the evidence shows
and use that class's terms:**

| Class | MF (pick the most specific child) | BP relation |
|---|---|---|
| RNA polymerase core | `GO:0003899` DNA-directed RNA polymerase activity (catalytic-core subunits `contributes_to`) | part of transcription |
| GTF | `GO:0140223` general transcription initiation factor activity; `GO:0016251` for RNA polymerase II | part of transcription (`GO:0006366` for Pol II) |
| dbTF | `GO:0003700` DNA-binding transcription factor activity; `GO:0000981` (Pol II), `GO:0001228` activator / `GO:0001227` repressor (Pol II), `GO:0004879` nuclear receptor activity, `GO:0016987` sigma factor activity | part of regulation of transcription |
| coTF | `GO:0003712` transcription coregulator activity; `GO:0003713` coactivator / `GO:0003714` corepressor | part of regulation of transcription |
| Regulator of a transcription regulator, away from chromatin | `GO:0140416` transcription regulator inhibitor activity; `GO:0140537` transcription regulator activator activity | part of regulation of gene expression |

**A protein may have more than one class of activity when each is shown; do not assign
a second class to cover uncertainty.** Never annotate `GO:0140110` transcription
regulator activity, which is a do-not-annotate grouping term.

Rationale. The classes differ in what they act on: a dbTF's input is the target gene, a
coTF's input is the dbTF, a GTF acts at every promoter of its polymerase
([Drive: MF guidelines for GO-CAM](https://drive.google.com/open?id=1DWvc_g5yH4S8-Tc2rPtaAyPOIkYzITagK1sXysj0CY4)).
The ontology encodes the split: `GO:0003700` is part of `GO:0006355` regulation of
DNA-templated transcription, while `GO:0140223` is part of `GO:0006351` DNA-templated
transcription. GO:0140223's usage note: dbTFs "modulate the selection of which genes are
expressed under specific conditions, while general transcription factors are the
constitutive machinery required for transcription initiation"
([go-annotation#2853](https://github.com/geneontology/go-annotation/issues/2853)).
Dual function is allowed: the archived guideline lists "acts as a DNA-binding
transcription factor in certain contexts and as a cofactor in others" among legitimate
outcomes of a literature review.

Worked examples from the GOC workshop examples
([Drive: TF annotation guidelines](https://drive.google.com/open?id=1bqCxx7QUblrc9q4PIynbJzoCXv248UWBxJa7fguJyXs)):
GTF2H2, a TFIIH subunit, is a GTF; NKX6-3, a homeodomain protein shown by ChIP and
reporter assays to act through TAAT motifs, is a dbTF; SIN3A, recruited to the SOCS3
promoter through STAT3 and lacking a DNA-binding domain, is a corepressor, and its old
dbTF annotation was removed.

Provenance: [GOC]. Sources: as cited.

<a id="tr-2"></a>
### TR-2. Annotate dbTF activity only when the protein's own sequence-specific DNA binding and its regulation of targets are both supported

**Annotate `GO:0003700` or a descendant when (a) the protein itself binds a specific
double-stranded DNA sequence in a cis-regulatory region and (b) that binding regulates
transcription of a limited set of target genes. The strength of evidence needed for (a)
depends on the protein's family:**

| Prior | Evidence needed for DNA binding |
|---|---|
| Member of a well-characterised dbTF family (homeodomain, GATA, bHLH with basic region, bZIP, nuclear receptor) or a 1:1 ortholog of a demonstrated dbTF | ChIP or nuclear-extract EMSA at a known motif may suffice, together with regulation of the target |
| Domain family with mixed members (C2H2 zinc finger, Myb/SANT, ARID, HMG, single zinc finger) | direct binding with purified protein (EMSA, footprinting, SELEX, structure) at a defined motif |
| No family precedent | purified-protein sequence-specific binding plus regulation of transcription through the cognate motif in a cis-regulatory module |

Rationale. The archived guideline sets the two-part requirement and the family-graded
standard, and warns that "the presence of a DNA binding domain in a protein does not
always imply the protein functions as a dbTF"
([Drive: TF annotation guidelines](https://drive.google.com/open?id=1bqCxx7QUblrc9q4PIynbJzoCXv248UWBxJa7fguJyXs)).
The term's usage note singles out zinc finger, Myb/SANT and ARID proteins, "since only a
subset of proteins containing these domains directly and selectively bind to regulatory
DNA motifs". A protein with one zinc finger and weak binding evidence is not classed as
a dbTF ([go-annotation#3231](https://github.com/geneontology/go-annotation/issues/3231)).
Each THAP family member needs its own direct evidence
([go-annotation#3125](https://github.com/geneontology/go-annotation/issues/3125)).

Worked examples. HDAC4 carries IDA/IMP rows to dbTF activator activity; it has no
DNA-binding domain and acts through MEF2, so the rows were `MODIFY` to `GO:0003714`
transcription corepressor activity and its DNA-binding row to `GO:0000976`
(`genes/human/HDAC4`; [TRANSCRIPTION_FACTORS](../../TRANSCRIPTION_FACTORS.md)). MACC1
had an IDA dbTF activator row from a nuclear-extract EMSA; GOC curators found no
paper showing direct binding and changed it to `GO:0003713` transcription coactivator
activity ([go-annotation#3168](https://github.com/geneontology/go-annotation/issues/3168)).

Provenance: [GOC]. Sources: as cited;
[PMID:23981286](https://europepmc.org/article/MED/23981286) (2013 dbTF curation
protocol, partly superseded).

<a id="tr-3"></a>
### TR-3. Read each DNA-binding assay for what it shows: location, binding, or direct sequence-specific binding

**ChIP and nuclear-extract EMSA (including supershift) show that a protein is at a
region or in a complex that binds it; they do not show that the protein binds DNA. Use
them for `GO:0000785` chromatin (CC) and, for an established dbTF, to identify targets.
Use purified-protein assays (EMSA, footprinting, SELEX, crystal structure) for DNA-binding
MF terms. HT-SELEX shows sequence recognition but not regulation. An InterPro mapping
supports DNA binding only if the InterPro entry itself maps to a DNA-binding term.**

Rationale. "In vivo ChIP experiments do not usually provide sufficient evidence for a
protein-DNA interaction because it does not demonstrate whether the interaction is
direct" ([wiki: Annotation consistency: ChIP experiments](https://wiki.geneontology.org/index.php/Annotation_consistency_%3A_ChIP_experiments),
reviewed 2023; [go-annotation#943](https://github.com/geneontology/go-annotation/issues/943)).
The exception on that page, studies premised on direct binding through a known motif,
is the family prior of [TR-2](#tr-2). Nuclear extracts identify transcription complexes,
so a shift "is not sufficient to attribute direct DNA binding because binding may be
indirect, through another DNA binding protein"
([go-annotation#3235](https://github.com/geneontology/go-annotation/issues/3235)).
ISM annotations of dbTF activity from InterPro entries that carry no DNA-binding mapping
were removed as unsupported
([go-annotation#2985](https://github.com/geneontology/go-annotation/issues/2985)).
The guideline's high-throughput notes say HT-SELEX supports DNA binding but not dbTF
activity without functional evidence, and ChIP-seq is inconclusive alone
([TRANSCRIPTION_FACTORS](../../TRANSCRIPTION_FACTORS.md), summarising the 2023 PDF).

Worked example. LYAR was reported to bind rDNA in a supershift assay with nuclear
extract. The antibody supershift does not show direct binding, and other papers show it
regulates rDNA transcription without binding DNA, so the evidence does not support a
dbTF annotation ([go-annotation#3235](https://github.com/geneontology/go-annotation/issues/3235)).

Provenance: [GOC]. Sources: as cited.

<a id="tr-4"></a>
### TR-4. Require a genomic address: non-specific, structure-specific and modification-specific DNA binders are not dbTFs

**Binding that cannot select a limited set of genes does not support dbTF activity.
Annotate it with the specific binding term and, if the protein regulates transcription
through a dbTF, a coregulator term: AT-hook and other minor-groove binders
(`GO:0003680` minor groove of adenine-thymine-rich DNA binding); methyl-CpG binders
(`GO:0008327` methyl-CpG binding); hairpin and single-strand binders (`GO:0032448` DNA
hairpin binding, `GO:0003697` single-stranded DNA binding); G-quadruplex binders
(`GO:0051880` G-quadruplex DNA binding).**

Rationale. "All dbTFs should bind double-stranded DNA specifically. The binding will
provide a genomic address to allow condition-specific gene regulation"
([Drive: human TF catalogue talk](https://drive.google.com/open?id=11wth1xVtY8S5U93KHsiklVWWaa_ORs_CkbRHLV2ewNE)).
AT-hook proteins bind a sequence too short to address a gene and act with dbTFs
([go-annotation#3110](https://github.com/geneontology/go-annotation/issues/3110)).
MeCP2 binds methyl-CpG, so its location is specified by methylation rather than
sequence; its dbTF rows were removed in favour of methyl-CpG binding
([go-annotation#3086](https://github.com/geneontology/go-annotation/issues/3086)).
Hairpin or single-strand binding is not dbTF evidence, "we really do double strand DNA
binding for the dbTFs" ([go-annotation#3135](https://github.com/geneontology/go-annotation/issues/3135)).

Worked examples. Mouse ARID3A and ARID3B dbTF rows: `GO:0003680` plus
`GO:0003713` transcription coactivator activity where the paper supports it. NR0B1
(DAX1) hairpin binding: `GO:0032448`, coregulator rather than dbTF. Human NME2, which
binds a G-quadruplex promoter element of MYC, was kept as a non-core, non-canonical
promoter regulator rather than a dbTF ([TRANSCRIPTION_FACTORS](../../TRANSCRIPTION_FACTORS.md)).

Provenance: [GOC]. Sources: as cited.

<a id="tr-5"></a>
### TR-5. Annotate coTF activity for locus-specific action through a dbTF, and protect proteins with a real DNA-binding domain from it

**Annotate `GO:0003712` (or `GO:0003713`, `GO:0003714`) when the protein is recruited
to specific genes by a DNA-bound dbTF, or by reading a mark laid down at a
dbTF-specified locus, or by another coTF in such a chain, and changes their
transcription. For a protein with a characterised DNA-binding domain and DNA-binding
evidence, annotate coTF activity only with evidence that the regulatory effect does not
use its own DNA binding.**

Rationale. GO:0003712 is defined as modulating transcription "via binding to a
DNA-binding transcription factor at a specific genomic locus, either on its own or as
part of a complex", with the usage note that most coregulators do not bind DNA. The GOC
expert reading sets three recruitment routes (direct binding by a dbTF, reading a
histone mark, recruitment by another coTF) and declines to make separate
"coactivator-coactivator" terms ([go-annotation#4554](https://github.com/geneontology/go-annotation/issues/4554);
[go-annotation#4000](https://github.com/geneontology/go-annotation/issues/4000)). For Cdx2
and Pou5f1, both with characterised homeodomains and DNA-binding evidence, coTF
annotations based on protein–protein interaction were changed to dbTF: "To apply that
term you would need evidence that the activity does NOT involve DNA binding"
([go-annotation#2972](https://github.com/geneontology/go-annotation/issues/2972)).

Worked examples. RFXANK, a subunit of the RFX complex that binds the MHC class II X box,
had its dbTF activator row `MODIFY` to `GO:0003713` and its DNA-binding row `REMOVE`;
RFXAP likewise (`genes/human/RFXANK`). NOTCH1's intracellular domain activates targets in
complex with the DNA-binding RBPJ; its IDA rows to cis-regulatory DNA binding and dbTF
activator activity were removed by the curating group, leaving `GO:0003713`
([go-annotation#5743](https://github.com/geneontology/go-annotation/issues/5743)).

When a coTF binds DNA non-specifically as part of its mechanism, annotate
`GO:0000976` transcription cis-regulatory region binding (the term's comment admits
non-specific binding) alongside the coTF term, not `GO:0003700`
([go-annotation#5743](https://github.com/geneontology/go-annotation/issues/5743)).

Provenance: [GOC+]. The recruitment-chain reading is GOC expert practice stated in
issues, not in the 2021 paper's term definitions. Sources: as cited.

<a id="tr-6"></a>
### TR-6. Separate GTFs from coTFs by where they are recruited, and annotate GTFs to transcription itself

**A protein recruited through core promoter elements (TATA box, initiator) to act at
every promoter of its polymerase is a GTF: annotate the polymerase-specific GTF activity
and the transcription BP, not regulation of transcription. A protein recruited through
gene-specific elements by a dbTF is a coTF, even if it is also a subunit of a GTF in
another context. Use `GO:0006351` DNA-templated transcription and its children only for
RNA polymerase subunits and GTFs.**

Rationale. "If the protein(complex) recruitment happens via the core promoter elements
(TATA box, initiator, etc) then it is a GTF. Via the other (gene-specific elements)
located in the promoter/enhancer, then it is a cofactor"
([go-annotation#4554](https://github.com/geneontology/go-annotation/issues/4554)). GO
decided that GTFs are core machinery annotated to transcription, not to its regulation
([go-annotation#2853](https://github.com/geneontology/go-annotation/issues/2853)), and
that the transcription term and children are for RNA polymerase and GTFs only, with
other annotations moved to regulation terms
([go-annotation#2933](https://github.com/geneontology/go-annotation/issues/2933); the
review is still open). The ontology makes the GTF terms part of transcription.

Worked examples. S. pombe Taf11, a TFIID subunit, had an IBA to `GO:0003713`
transcription coactivator activity; it was filtered and annotated to `GO:0016251` RNA
polymerase II general transcription initiation factor activity
([go-annotation#4554](https://github.com/geneontology/go-annotation/issues/4554)). Some
TFIID subunits also belong to coactivator complexes (SAGA); those take a coTF term only
from experiments showing dbTF-directed recruitment. Mediator subunits are coactivators
by definition: GO:0003713's definition names "the Mediator complex, which bridges
sequence-specific DNA binding transcription factors and RNA polymerase".

Provenance: [GOC]. Sources: as cited.

<a id="tr-7"></a>
### TR-7. Proteins that act on transcription regulators away from chromatin are regulator-of-regulator, not coTFs

**A protein that binds a dbTF or coTF and keeps it from chromatin (cytoplasmic or
nuclear sequestration, blocking DNA binding by heterodimerisation) enables
`GO:0140416` transcription regulator inhibitor activity, `has_input` the regulator. One
that enables a regulator to reach chromatin or its partners enables `GO:0140537`
transcription regulator activator activity. Do not annotate coTF terms or regulation of
dbTF activity BP terms for these.**

Rationale. "The difference between coTFs and dbTF regulators is that the latter do not
act at the genomic location of target regulated gene"
([Drive: TF annotation guidelines](https://drive.google.com/open?id=1bqCxx7QUblrc9q4PIynbJzoCXv248UWBxJa7fguJyXs)).
GO:0140416's usage note gives TCF23 (heterodimerises with dbTFs and prevents DNA
binding), NFKBIA (holds NF-kB in the cytoplasm) and HSP90 (holds steroid receptors away
from DNA) as examples. The BP terms for regulation of dbTF activity (for example
`GO:0051090`, now obsolete) were retired, partly because the `regulates` inference chain
turned regulation of a dbTF's activity into regulation of DNA binding
([wiki: Ontology meeting 2018-10-01](https://wiki.geneontology.org/index.php/Ontology_meeting_2018-10-01)).

Worked example. The bHLH ID proteins lack a basic region and inhibit dbTFs by
dimerisation; they are correctly excluded from dbTF annotation
([TRANSCRIPTION_FACTORS](../../TRANSCRIPTION_FACTORS.md)) and fit GO:0140416.

Note that GO:0140416 and GO:0140537 are defined "via direct binding and/or
post-translational modification". Where the effect is a covalent modification of the
regulator (a kinase or SUMO ligase acting on a dbTF), annotate the catalytic activity with
`has_input` the regulator, consistent with [MF-17](molecular-function.md#mf-17).

Provenance: [GOC] for the class; [GOC+] for the covalent-modification exclusion. Sources:
as cited.

<a id="tr-8"></a>
### TR-8. Use RNA polymerase II terms for eukaryotic protein-coding genes; name Pol I or III only when shown

**For a regulator of a eukaryotic protein-coding gene, use the RNA polymerase
II-specific terms (`GO:0000981`, `GO:0001228`, `GO:0001227`, `GO:0000978`, `GO:0006357`)
without requiring the paper to mention the polymerase. Use RNA polymerase I or III terms
(`GO:0001181`, `GO:0000995`, `GO:0006360`, `GO:0006383`) only when the paper identifies
those polymerases' templates. For bacteria, archaea, mitochondria and plastids, use the
terms without polymerase qualification (`GO:0003700`, `GO:0001216`, `GO:0001217`,
`GO:0006355`), or the organelle transcription terms.**

Rationale. The electronic transcription jamboree agreed that "for almost all protein
coding genes in eukaryotes ... you can confidently use the RNA Pol II terms even if the
paper doesn't explicitly mention that detail", with rare exceptions such as
trypanosome genes transcribed by Pol I
([wiki: Transcription jamboree](https://wiki.geneontology.org/index.php/Transcription_jamboree),
archived). The 2017 working group told curators to "always use regulation of RNA
polymerase II transcription terms when there is evidence that the transcription factor
regulates mRNA levels" ([Drive: 2017 transcription guidelines](https://drive.google.com/open?id=0B_c5g4FezmhfNENjNk5RbjJwQUk)).
The Pol II-specific dbTF term `GO:0000981` occurs in `GO:0000785` chromatin, which no
bacterial protein does.

Worked examples. A yeast zinc-cluster activator of a glucose-repressed gene:
`GO:0001228` with `has_input` the gene. A plant MYB activator of an anthocyanin gene:
`GO:0001228`. E. coli LacI: `GO:0001217` DNA-binding transcription repressor activity.
Plant RNA polymerase IV and V transcription (`GO:0001059`, `GO:0001060`) belongs to
siRNA-directed silencing, not to dbTF annotation.

Provenance: [GOC]. Sources: as cited.

<a id="tr-9"></a>
### TR-9. State activator or repressor when the direction at a target is shown; allow both when context changes it

**Use the activator or repressor child of dbTF activity (or coactivator/corepressor)
when the paper shows the direction of the effect on an identified target. A protein may
carry both, each with its own target or context. When direction is not shown, or the
paper's effect may be indirect, use the unqualified term. Do not infer direction for a
coTF from the class of its chromatin activity alone.**

Rationale. The archived guideline: dbTFs and coregulators "often act as activators or
repressors in different promoters or dependent on the context, so annotation to both
activator and repressor is not considered inconsistent"
([Drive: TF annotation guidelines](https://drive.google.com/open?id=1bqCxx7QUblrc9q4PIynbJzoCXv248UWBxJa7fguJyXs)).
The GO-CAM activity units use the activator and repressor children and capture one target
per activity unit ([Drive: MF guidelines for GO-CAM](https://drive.google.com/open?id=1DWvc_g5yH4S8-Tc2rPtaAyPOIkYzITagK1sXysj0CY4)).
A PAINT discussion recorded agreement to use the unqualified "regulation of
transcription" for dbTFs, and doubt over whether coTF direction can be read from the
chromatin modification they catalyse
([go-annotation#3932](https://github.com/geneontology/go-annotation/issues/3932)). We
reconcile the two by applying the unqualified term to propagated and family-level rows,
where direction varies between members and targets, and the directional terms to
experimental rows with a target.

Worked example. Rpd3S complex members (S. cerevisiae RCO1, S. pombe Cph1/Cph2) carry
IBA rows to positive regulation of transcription by RNA polymerase II, although the
complex is a deacetylase that represses cryptic transcription. The direction depends on
the target gene and assay; the RCO1 review modified the broad BP toward the chromatin
mechanism rather than choosing a direction ([YEAST_EPIGENETICS_HISTONE_INHERITANCE](../../YEAST_EPIGENETICS_HISTONE_INHERITANCE.md)).

Provenance: [GOC+]. Sources: as cited.

<a id="tr-10"></a>
### TR-10. For dbTF DNA binding use the cis-regulatory sequence-specific terms; put region and motif in extensions

**For a dbTF's DNA binding, use `GO:0000978` RNA polymerase II cis-regulatory region
sequence-specific DNA binding (or `GO:0000987` cis-regulatory region sequence-specific
DNA binding outside Pol II), or `GO:1990837` sequence-specific double-stranded DNA
binding when the region is not regulatory or not known. Do not use terms that encode
proximal, distal, enhancer or promoter in the label; record the region or motif with a
Sequence Ontology term in `has_input`. A separate DNA-binding annotation is optional
when dbTF activity is annotated from the same evidence. Core promoter binding
(`GO:0001046` core promoter sequence-specific DNA binding) belongs to GTFs and sigma
factors.**

Rationale. GO obsoleted "promoter binding" terms because promoter had no workable
definition ([wiki: Proposal to obsolete "promoter binding" and child terms](https://wiki.geneontology.org/index.php/Proposal_to_obsolete_%22promoter_binding%22_and_child_terms)),
and later obsoleted transcription factor binding terms that specified proximal or distal
regions, moving the region into SO terms or extensions
([wiki: Ontology meeting 2018-09-24](https://wiki.geneontology.org/index.php/Ontology_meeting_2018-09-24)).
When `occurs_at` was deprecated, SO motifs on DNA-binding annotations moved to `has_input`
([go-annotation#2584](https://github.com/geneontology/go-annotation/issues/2584)). The
ontology gives `GO:0000981` a `has_part` link to `GO:0000977` RNA polymerase II
transcription regulatory region sequence-specific DNA binding, so the binding is implied
by the dbTF term, and "DNA binding ... can annotate to DNA binding terms, but not
required" ([Drive: 2020 GO-CAM jamboree, transcription](https://drive.google.com/open?id=1_T0d9BJAY7yC0iZ1aQ9l3bNeOHKL4TLx14Eddml-XHs)).
Make the binding annotation when DNA binding is shown in a separate experiment from the
regulation, or when binding is shown and regulation is not.

Worked examples. S. cerevisiae CUP9 binds the PTR2 regulatory region and represses PTR2:
`GO:0001227` with `has_input` PTR2, and, from the purified-protein EMSA,
`GO:0000978` ([wiki: Transcription jamboree](https://wiki.geneontology.org/index.php/Transcription_jamboree),
where it was annotated to a now-merged "core promoter proximal region" term). B. subtilis
SigE: `GO:0016987` sigma factor activity, which has part core promoter sequence-specific
DNA binding (`genes/BACSU/sigE`).

Provenance: [GOC+]. Sources: as cited.

<a id="tr-11"></a>
### TR-11. Annotate regulation of transcription only from evidence of a transcriptional effect; use regulation of gene expression for mRNA-level changes

**Annotate a regulation of transcription BP only when the evidence shows an effect on
transcription (reporter or enhancer assay, nuclear run-on, nascent RNA) by a protein that
acts at the gene (DNA binding, or recruitment by a dbTF). A change in steady-state mRNA
alone (qPCR, northern blot, RNA-seq) supports `GO:0010468` regulation of gene expression
at most. Do not annotate signaling molecules, receptors or metabolic enzymes to
regulation of transcription because they change a gene's expression.**

Rationale. The 2016–2017 working group: "GO curators to use regulation of gene
expression for annotation, when the only evidence to support annotation is a change in
mRNA levels"; its decision tree is "NOT appropriate for annotation of gene products which
are constitutively bound to DNA (e.g. histones), or are not localized near a DNA
regulatory region such as signaling molecules"
([Drive: 2017 transcription guidelines](https://drive.google.com/open?id=0B_c5g4FezmhfNENjNk5RbjJwQUk);
[Drive: UCL decision tree 2016](https://drive.google.com/open?id=0B_c5g4FezmhfSzV5OERKcHJ1MUk)).
Core-machinery mutants alter many processes; curators "should only annotate to the gene
product's transcription activity, rather than the multiple downstream processes"
([wiki: Annotating downstream processes](https://wiki.geneontology.org/index.php/Annotating_downstream_processes)).
Host proteins co-opted by a virus are not annotated to viral transcription
([go-annotation#1507](https://github.com/geneontology/go-annotation/issues/1507)).

Where the MF is annotated, the BP regulation of transcription is already implied
(`GO:0003700` is part of `GO:0006355`). The informative BP for a dbTF is the program its
targets serve (for example a cell fate specification term); GO-CAM curators now annotate
to that larger process rather than to positive or negative regulation of transcription
([Drive: managers' minutes, 2026](https://drive.google.com/open?id=1PTb0-s9LE8IhsStqhdc25Hb5prdlxBGWbOr8oLfIWNA)).

Worked example. A membrane receptor such as GPER1 annotated to dbTF activity or
regulation of transcription on the strength of downstream gene induction is flagged by the
function-requirement rule for dbTFs and should lose the dbTF row; its pathway BP stays
([FUNCTION_REQUIREMENT_RULES](../../FUNCTION_REQUIREMENT_RULES.md), FRR:0009).

Provenance: [GOC]. Sources: as cited.

<a id="tr-12"></a>
### TR-12. Give chromatin enzymes, readers and chaperones their own activity; add transcription regulation only on gene-specific evidence

**Annotate a histone or DNA modifier with its catalytic activity, a reader with the
specific histone reader activity, a chaperone with histone chaperone activity, and a
remodeler with `GO:0140658` ATP-dependent chromatin remodeler activity, at the residue
level the evidence supports. Annotate a coTF term or regulation of transcription only
when the protein is shown to be recruited to specific genes (by a dbTF or a locally
deposited mark) and to change their transcription. Annotate global or pleiotropic
chromatin roles to chromatin processes: `GO:0045815` transcription initiation-coupled
chromatin remodeling, `GO:0140673` transcription elongation-coupled chromatin
remodeling, `GO:0140718` facultative heterochromatin formation, `GO:0140719` constitutive
heterochromatin formation. When a protein has both reader and writer activity, annotate
both.**

Rationale. The current chromatin manual (reviewed 2025) maps histone marks to the
processes they drive and says "if a protein has both reader and writer activities, it
should be annotated to both molecular functions"
([wiki: Chromatin remodeling manual](https://wiki.geneontology.org/index.php/Chromatin_remodeling_manual)).
GO obsoleted all "modified histone binding" terms in favour of reader activities (36
reader terms) and writer terms (173) after reviewing over 2,000 histone binding
annotations ([Drive: ontology group report, 2025-05](https://drive.google.com/open?id=18n5uLIg0K2pnJ5e06E4Ssxn8zJ6anDdcOJ-k0Xft2W8);
[Drive: GO-CAM transcription histone readers, 2025](https://drive.google.com/open?id=1L_5jlDwXazGGNZUOsz1r8kWYInYeEagk)).
Readers are adaptors in the ontology: `GO:0140566` histone reader activity is a child of
`GO:0140463` chromatin-protein adaptor activity. On whether chaperones and modifiers are
coregulators, the GOC position moved from "OK to say histone chaperones and modifiers are
co-regulators" ([go-annotation#3414](https://github.com/geneontology/go-annotation/issues/3414))
to a stricter test: HIRA "would fit a coTF" only "if a dbTF is shown to require HIRA to
induce or repress a gene", because chromatin assembly defects have pleiotropic effects
"that could mistakenly be interpreted as coTF function"
([go-annotation#4040](https://github.com/geneontology/go-annotation/issues/4040)).

Worked examples. S. cerevisiae SWI3 lost four DNA-binding rows (its SWIRM domain is a
protein-interaction module), and SWI1 lost a cis-regulatory region binding row
([YEAST_EPIGENETICS_HISTONE_INHERITANCE](../../YEAST_EPIGENETICS_HISTONE_INHERITANCE.md)).
A HAT shown to be recruited by a specific activator to its target promoters takes
`GO:0004402` histone acetyltransferase activity (or the residue-specific child) and
`GO:0003713`. A histone chaperone whose loss derepresses cryptic transcription
genome-wide takes `GO:0140713` histone chaperone activity and
`GO:0140673`, not a coTF term. S. pombe Epe1, recruited to heterochromatin and
associated with SAGA, was argued by the GOC expert to be a coTF through the third
recruitment route, with a stricter alternative of `GO:0140537` and
`GO:0045815` ([go-annotation#4000](https://github.com/geneontology/go-annotation/issues/4000)).

Provenance: [GOC+]. Sources: as cited.

<a id="tr-13"></a>
### TR-13. Treat an enzyme activity plus dbTF activity on one protein as a probable error

**When a protein carries both a catalytic activity and dbTF activity, assume the
catalytic activity indicates a coregulator role and review the dbTF rows. Keep both only
when each is shown for the protein.**

Rationale. GO:0003700's usage note: "Most DNA-binding transcription factors do not have
enzymatic activity ... If a protein has an enzymatic activity ... and no known DNA
binding domain, consider annotating to GO:0003712". A 2018 consistency check found many
false positives among proteins annotated to both
([go-annotation#2130](https://github.com/geneontology/go-annotation/issues/2130)).

Worked examples. Human HDAC4 and HDAC5, menin, MED12 and alpha-enolase appear among
experimental dbTF annotations on proteins with no DNA-binding domain
([FUNCTION_REQUIREMENT_RULES](../../FUNCTION_REQUIREMENT_RULES.md)). S. pombe Mot1, an
ATPase that binds the core promoter, is the exception the 2018 thread allowed.

Provenance: [GOC]. Sources: as cited.

<a id="tr-14"></a>
### TR-14. Name the direct target gene with `has_input`, one target per annotation; a coTF's input is the dbTF

**On a dbTF MF or regulation of transcription BP annotation, record each directly
regulated gene with `has_input` (a gene or gene-product identifier), one target per
annotation. On a coTF annotation, `has_input` is the dbTF, not the target gene. Record
only direct targets (bound and regulated); do not list every differentially expressed
gene. Do not use the retired `regulates_transcription_of`, `has_regulation_target` or
`has_direct_input` relations.**

Rationale. The GO-CAM guideline: the dbTF activity "has input the gene whose
expression it regulates", with a separate activity unit per target, while the coTF "has
input: the transcription factor regulated, when known"
([Drive: MF guidelines for GO-CAM](https://drive.google.com/open?id=1DWvc_g5yH4S8-Tc2rPtaAyPOIkYzITagK1sXysj0CY4)).
The 2018 GO-CAM working group added inputs only for direct regulation; for indirect or
unknown regulation, no input is added
([wiki: GO-CAM Working Group Call 2018-09-25](https://wiki.geneontology.org/index.php/GO-CAM_Working_Group_Call_2018-09-25)).
`regulates_transcription_of` was proposed for replacement by `has_input`
([go-annotation#2598](https://github.com/geneontology/go-annotation/issues/2598)), and
`has_direct_input` merged into `has_input` in 2020
([wiki: Annotation Conf. Call 2020-02-04](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2020-02-04)).
Only the direct target belongs in the extension ([wiki: Binding Guidelines](https://wiki.geneontology.org/index.php/Binding_Guidelines)).

Worked example. FOXO1 regulation of G6PC1 and PCK1 is two annotations (or two activity
units), each `GO:0001228` with one `has_input`
([Drive: dbTF guidelines, archived](https://drive.google.com/open?id=1o06rwrGwx8Fw_fqw3ldsrGlM0ot21Q137yQ95ySpasc)).
A ChIP-seq plus RNA-seq study supports `has_input` only for genes that are both bound
near a motif and regulated.

Provenance: [GOC+]. The archived guideline's line "target gene of a dbTF or a coTF:
has_input [dbTF]" is garbled; this rule states the intended meaning. Sources: as cited.

<a id="tr-15"></a>
### TR-15. Bacterial and plant regulators follow the same evidence standard with their own terms

**Annotate bacterial dbTFs to `GO:0003700`, `GO:0001216` or `GO:0001217`, sigma factors to
`GO:0016987` sigma factor activity (a dbTF descendant in GO), and two-component response
regulators that bind DNA to the dbTF term, adding `GO:0000156` phosphorelay response
regulator activity when phosphotransfer to the protein is shown. Annotate plant TFs with the RNA polymerase II terms, applying
the same domain caution as for animals. Anti-sigma factors and other sequestering
regulators take `GO:0016989` sigma factor antagonist activity or `GO:0140416`.**

Rationale. In the current ontology `GO:0016987` is a subclass of `GO:0003700`, with
`has_part` core promoter sequence-specific DNA binding and RNA polymerase core enzyme
binding (checked against the local GO release, 2026-11-15), so a sigma factor is a dbTF
in GO's sense even though its role resembles a GTF's. In review, a sigma factor carrying
bare `GO:0003700` is refined to `GO:0016987` when the row's evidence identifies it as a
sigma factor (B. subtilis SigE; [BACSU](../../BACSU.md)). Arabidopsis reviews routinely
sharpen dbTF, DNA binding and regulation rows to activator, repressor or
sequence-specific children (77 of 244 dbTF rows modified), and transcription corepressor
activity is the most common `NEW` term ([ARATH](../../ARATH.md)).

Worked examples. B. subtilis Spo0A, the sporulation master regulator: `GO:0003700`
accepted as its core MF, with `GO:0000160` phosphorelay signal transduction system as
the BP (`genes/BACSU/spo0A`); `GO:0000156` would add the receiver-domain activity where
phosphotransfer to Spo0A is shown. B. subtilis SigE: `MODIFY` `GO:0003700` →
`GO:0016987`.

Provenance: [NEW]. The GOC transcription guidelines are written for eukaryotes ("prokaryotes
use a single polymerase") and say little about bacterial or plant regulators. Sources: as
cited.

<a id="tr-16"></a>
### TR-16. Review electronic and propagated dbTF rows against the family and the member

**An IEA, ISM or IBA dbTF row is acceptable when the member has a DNA-binding domain from
a dbTF family, retains its sequence-reading features, and nothing specific contradicts
it. Flag for review any dbTF row on a protein without one of the recognised DNA-binding
domain families, or with an enzymatic domain. In review: a protein that regulates
transcription through a dbTF is `MODIFY` to the coTF term; a protein with no
transcriptional role is `REMOVE`; an experimental dbTF row whose full text you cannot
read is `UNDECIDED`, never `REMOVE` on the strength of an abstract.**

Rationale. Sixty DNA-binding domain families cover 92% of proteins with experimental
dbTF annotations; the remainder mixes likely misannotations and non-canonical binders
([FUNCTION_REQUIREMENT_RULES](../../FUNCTION_REQUIREMENT_RULES.md), FRR:0009). Of 1,447
human proteins with dbTF annotations, 95.6% agree with the GREEKC curated catalogue; the
62 GOA-only proteins are the place to look for errors, and 945 human dbTF proteins rest on
IEA alone ([TRANSCRIPTION_FACTORS](../../TRANSCRIPTION_FACTORS.md);
[PMID:34673265](https://europepmc.org/article/MED/34673265), a GO catalogue of human
DNA-binding transcription factors). An IBA is a curator's judgement about node placement
([phylogenetic-propagation.md](phylogenetic-propagation.md)); a member that keeps the
domain fold but has lost the sequence-reading features is outside the inheriting clade
([IBA_REVIEW](../../IBA_REVIEW.md), worm STAT sta-2). Experimental rows deserve the
deference described in [CLAUDE.md](../../../CLAUDE.md) ("Do not overrule curators from
incomplete evidence").

Worked example. Human netrin-1 and netrin-3 carried IBA rows to dbTF activity and
cis-regulatory DNA binding, seeded from POU-domain proteins at a PAINT node of the
netrin/laminin family; both were `REMOVE` and the provenance discrepancy recorded in a
family review ([TRANSCRIPTION_FACTORS](../../TRANSCRIPTION_FACTORS.md)).

Provenance: [GOC+]. Sources: as cited.

## Decision aid

### Which class?

```
Does the protein assemble with RNA polymerase at core promoter elements of all/most genes?
  yes -> GTF (TR-6)
Does it bind double-stranded DNA itself, at a motif specific enough to select genes?   (TR-2, TR-3, TR-4)
  yes, and regulates targets through that binding -> dbTF (activator/repressor if shown, TR-9)
  binds DNA, but AT-rich minor groove / methyl-CpG / hairpin / ssDNA / G4 / non-specific -> specific binding term; go on
Is it recruited to specific genes by a dbTF, by a locally deposited mark, or by another coTF, and does it change their transcription?
  yes -> coTF (coactivator/corepressor if shown, TR-5); add its own enzymatic/reader activity (TR-12)
Does it bind a transcription regulator away from chromatin to block or enable it?
  yes -> GO:0140416 / GO:0140537 (TR-7)
Does it alter target mRNA levels with no evidence of acting at the gene?
  yes -> regulation of gene expression at most (TR-11), or the process it really performs
```

### Which evidence supports what?

| Evidence | DNA-binding MF | dbTF MF | CC chromatin | `has_input` target |
|---|---|---|---|---|
| Purified-protein EMSA, footprinting, SELEX, structure at a motif | yes | with regulation | no | with regulation |
| HT-SELEX motif only | yes (`GO:1990837`) | no | no | no |
| Nuclear-extract EMSA or supershift | no | only with a strong family prior | no | supports, for an established dbTF |
| ChIP / ChIP-seq | no | only with a strong family prior and regulation | yes | supports, if also regulated |
| Reporter or enhancer assay with motif mutation | no | yes, with binding | no | yes |
| qPCR / RNA-seq change only | no | no | no | no; BP regulation of gene expression |
| InterPro domain match | only if InterPro maps it | only via a dbTF-family signature | no | no |

### Chromatin protein: which BP?

| What was shown | BP |
|---|---|
| Recruited by a named dbTF to named genes; changes their transcription | regulation of transcription (with coTF MF) |
| Mark-dependent action at promoters of active genes | `GO:0045815` transcription initiation-coupled chromatin remodeling |
| Restores chromatin behind elongating polymerase; loss gives cryptic transcription | `GO:0140673` transcription elongation-coupled chromatin remodeling |
| Maintains silent domains | `GO:0140719` or `GO:0140718` heterochromatin formation |
| Genome-wide expression changes after deletion, mechanism unknown | none from this evidence; at most regulation of gene expression |

## Common errors

**DNA-binding domain read as dbTF.** Zinc finger, Myb/SANT, ARID and HMG proteins given
dbTF activity from domain or IBA alone. Fix: require the family-graded evidence of
[TR-2](#tr-2); `MODIFY` to coTF or `REMOVE`.

**ChIP read as DNA binding.** IDA rows to `GO:0000978` from ChIP or nuclear-extract
EMSA. Fix: chromatin CC, and DNA binding only from purified-protein assays
([TR-3](#tr-3)).

**Coactivator in a DNA-bound complex annotated as dbTF.** NOTCH1, RFXANK, RFXAP, MACC1.
Fix: `MODIFY` to `GO:0003713`; remove the DNA-binding row unless the protein contacts DNA
itself ([TR-5](#tr-5)).

**dbTF annotated as coTF from a protein–protein interaction.** Cdx2 and Pou5f1. Fix:
keep dbTF unless the regulatory effect is shown not to use DNA binding ([TR-5](#tr-5)).

**GTF subunit annotated as coactivator by propagation.** TFIID subunits. Fix: GTF
activity and transcription BP ([TR-6](#tr-6)).

**Chromatin enzyme annotated to regulation of transcription from a deletion
phenotype.** Fix: the enzyme's activity and the chromatin process; coTF only with
gene-specific recruitment ([TR-12](#tr-12)).

**Signaling protein annotated to regulation of transcription.** Receptors, kinases and
ligands whose pathway ends in gene induction. Fix: the pathway BP; regulation of
transcription is for proteins acting at the gene ([TR-11](#tr-11)).

**Every differentially expressed gene in `has_input`.** Fix: direct targets only
([TR-14](#tr-14)).

**Grouping terms.** `GO:0140110` transcription regulator activity is do-not-annotate;
bare `GO:0003677` DNA binding beside a specific dbTF or binding term is `TOO_GENERAL`.

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| 2012 transcription guidelines (as quoted in [go-annotation#2046](https://github.com/geneontology/go-annotation/issues/2046)) | Annotate every TF to a DNA-binding term by EXP, a regulation BP by EXP, and the TF MF by IC from the two | Annotate dbTF MF directly when both parts are shown; a separate DNA-binding row is optional ([TR-10](#tr-10)) | The refactored dbTF terms have part cis-regulatory DNA binding; PomBase marked the missing-binding check "not required" |
| [Drive: 2017 transcription guidelines](https://drive.google.com/open?id=0B_c5g4FezmhfNENjNk5RbjJwQUk) | `contributes_to` dbTF activity when the protein acts in a complex; `has_direct_input` and `regulates_transcription_of` extensions; CC "nuclear chromatin" | `enables` for each DNA-binding partner (dimer partners each bind DNA); `has_input` only; CC `GO:0000785` chromatin ([TR-14](#tr-14)) | Relations retired in 2020; `contributes_to` is for irreducible machines; "nuclear chromatin" no longer resolves in GO |
| [Drive: TF annotation guidelines (archived 2023)](https://drive.google.com/open?id=1bqCxx7QUblrc9q4PIynbJzoCXv248UWBxJa7fguJyXs) vs [wiki: ChIP experiments](https://wiki.geneontology.org/index.php/Annotation_consistency_%3A_ChIP_experiments) and [go-annotation#3168](https://github.com/geneontology/go-annotation/issues/3168) | Guideline: for well-characterised families "weaker evidence of DNA binding, such as ChIP experiments is sufficient". Wiki and issue: ChIP does not show binding | ChIP may complete a dbTF annotation for a well-characterised family member, but never supports a DNA-binding MF on its own, and never for a protein without a recognised DBD ([TR-2](#tr-2), [TR-3](#tr-3)) | The sources conflict; the reconciliation keeps both the family prior and the ChIP limitation |
| [Drive: TF annotation guidelines](https://drive.google.com/open?id=1bqCxx7QUblrc9q4PIynbJzoCXv248UWBxJa7fguJyXs) | "target gene of a dbTF or a coTF: has_input [dbTF]" | dbTF: `has_input` the target gene; coTF: `has_input` the dbTF ([TR-14](#tr-14)) | The line is garbled; the GO-CAM guideline states the intended pattern |
| [go-annotation#3932](https://github.com/geneontology/go-annotation/issues/3932) | Use unqualified "regulation of transcription" for dbTFs | Directional terms for experimental rows with a named target; unqualified for propagated rows ([TR-9](#tr-9)) | The GO-CAM guideline and the activator/repressor MF children assume direction is captured where known |
| [Drive: managers' minutes, 2026](https://drive.google.com/open?id=1PTb0-s9LE8IhsStqhdc25Hb5prdlxBGWbOr8oLfIWNA) | GO-CAM curators annotate the larger BP, not +/- regulation of transcription | Adopt for standard annotation too: the dbTF MF implies regulation of transcription; the BP row should name the program ([TR-11](#tr-11)) | Avoids thousands of redundant regulation-of-transcription rows |
| [go-annotation#1720](https://github.com/geneontology/go-annotation/issues/1720) (open) | Make "transcription, DNA-templated" do-not-annotate and always specify promoter type, including "transcription from bacterial-type RNA polymerase promoter" | Specify the polymerase for eukaryotes; for bacteria use `GO:0006351` ([TR-8](#tr-8)) | The proposed bacterial term (`GO:0001121`) no longer exists in GO |
| [go-annotation#3414](https://github.com/geneontology/go-annotation/issues/3414) | "OK to say histone chaperones and modifiers are co-regulators" | coTF only with gene-specific recruitment and effect ([TR-12](#tr-12)) | The later [go-annotation#4040](https://github.com/geneontology/go-annotation/issues/4040) and the 2025 chromatin manual give chromatin processes their own BP terms |
| [go-annotation#4000](https://github.com/geneontology/go-annotation/issues/4000) | Two readings of coTF: any protein in a recruitment cascade, or only proteins directly recruited by a dbTF | Cascade reading, provided the chain is shown to start at a dbTF or at a mark it caused ([TR-5](#tr-5)) | Matches [go-annotation#4554](https://github.com/geneontology/go-annotation/issues/4554) and the current GO:0003712 definition ("at a specific genomic locus") |
| `GO:0000976` term text | Definition: binding "to a specific sequence of DNA"; comment: "meant to also capture non-specific binding" | Use GO:0000976 for non-specific regulatory-region binding by coTFs, as the comment and [go-annotation#5743](https://github.com/geneontology/go-annotation/issues/5743) intend ([TR-5](#tr-5)) | The definition and the comment contradict each other; we follow the usage guidance and flag the definition |
| [wiki: Transcription jamboree](https://wiki.geneontology.org/index.php/Transcription_jamboree) (archived) | CUP9 example annotated to "RNA polymerase II core promoter proximal region sequence-specific DNA binding" | `GO:0000978` RNA polymerase II cis-regulatory region sequence-specific DNA binding, region in `has_input` ([TR-10](#tr-10)) | Region-named binding terms were merged or obsoleted in 2018 |
| [Drive: TF annotation guidelines](https://drive.google.com/open?id=1bqCxx7QUblrc9q4PIynbJzoCXv248UWBxJa7fguJyXs) | dbTFs and coTFs "part of GO:0005667 transcription factor complex" | `GO:0005667` (now "transcription regulator complex") or `GO:0090575` only when the complex is shown | A dbTF is not by definition in a stable complex; the label has also changed |
| GO:0140416 / GO:0140537 definitions | Regulator-of-regulator activity "via direct binding and/or post-translational modification" | Covalent modification of a regulator is a catalytic activity with `has_input` ([TR-7](#tr-7)) | Aligns with the general regulator principle in [molecular-function.md](molecular-function.md#mf-17) |
| GOC transcription guidelines (eukaryote-only) | No guidance on sigma factors or two-component regulators | Sigma factors to `GO:0016987`; DNA-binding response regulators to dbTF, plus `GO:0000156` when phosphotransfer is shown ([TR-15](#tr-15)) | Fills a gap; follows the current ontology structure |

## Open questions

1. **Locus by modification.** MeCP2 binds methyl-CpG and recruits corepressors, doing for
   methylated sites what a dbTF does for motifs. One curator argued for a new
   "methyl-CpG-dependent" regulator term rather than methyl-CpG binding plus coTF
   ([go-annotation#3086](https://github.com/geneontology/go-annotation/issues/3086)). Should
   GO create one?
2. **Definition of GO:0000976.** Should the definition be widened to match its comment
   (non-specific regulatory-region binding), or should a separate non-specific term be
   created?
3. **Strict versus cascade coTF.** Is the recruitment-chain reading of [TR-5](#tr-5) the
   consortium position, or should GO:0003712 be reserved for proteins directly bound by a
   dbTF, with a new term for "co-coregulators"?
4. **Direction for coTFs.** Can a corepressor be inferred from deacetylase or H3K27
   methyltransferase activity, or must direction always be shown at a target?
5. **HT-SELEX plus domain.** SKI and SKIL were annotated as dbTFs by PAINT because the
   SKOR DNA-binding domain is present and SKOR proteins bind DNA in HT-SELEX, despite
   evidence that SKI binds DNA only in complex
   ([go-annotation#2985](https://github.com/geneontology/go-annotation/issues/2985)). When
   is domain-plus-relative evidence enough?
6. **Identifier namespace for target genes.** The question raised when
   `regulates_transcription_of` was retired, whether `has_input` takes gene or gene-product
   identifiers, is unresolved ([go-annotation#2598](https://github.com/geneontology/go-annotation/issues/2598)).
7. **Should `GO:0006351` become do-not-annotate?** Proposed in 2017 and still open
   ([go-annotation#1720](https://github.com/geneontology/go-annotation/issues/1720)).
8. **Bacterial and plant guidance.** The GOC guidelines were written for eukaryotic Pol
   II. Should bacterial regulators (sigma factors, response regulators, nucleoid proteins
   such as H-NS) have their own documented conventions?

## Sources

**Papers**

- [PMID:34461313](https://europepmc.org/article/MED/34461313) Gene Ontology representation for transcription factor functions (2021; canonical)
- [PMID:23981286](https://europepmc.org/article/MED/23981286) GO annotation of sequence-specific DNA binding transcription factors (2013; partly superseded)
- [PMID:34673265](https://europepmc.org/article/MED/34673265) A GO catalogue of human DNA-binding transcription factors (2021)

**GO Consortium Drive**

- [Transcription Factors Annotation Guidelines (archived, last updated 2023-10-24)](https://drive.google.com/open?id=1bqCxx7QUblrc9q4PIynbJzoCXv248UWBxJa7fguJyXs)
- [MF guidelines for GO-CAM (copy; reviewed 2026-03)](https://drive.google.com/open?id=1DWvc_g5yH4S8-Tc2rPtaAyPOIkYzITagK1sXysj0CY4)
- [Transcription coregulator activity (archived)](https://drive.google.com/open?id=1Wq-_3w6F2L_CGvneQT8n-pv-Ekk_i2_QpUZJeO_kvxI)
- [DNA-binding transcription factor activity annotation guidelines (archived)](https://drive.google.com/open?id=1o06rwrGwx8Fw_fqw3ldsrGlM0ot21Q137yQ95ySpasc)
- [2017 transcription working-group guidelines and decision tree](https://drive.google.com/open?id=0B_c5g4FezmhfNENjNk5RbjJwQUk)
- [UCL expression/transcription decision tree, 2016](https://drive.google.com/open?id=0B_c5g4FezmhfSzV5OERKcHJ1MUk)
- [2020 GO-CAM jamboree: transcription and its regulation](https://drive.google.com/open?id=1_T0d9BJAY7yC0iZ1aQ9l3bNeOHKL4TLx14Eddml-XHs)
- [2020 GOC meeting: human transcription factor catalogue](https://drive.google.com/open?id=11wth1xVtY8S5U93KHsiklVWWaa_ORs_CkbRHLV2ewNE)
- [2025 ontology group report (histone readers and writers)](https://drive.google.com/open?id=18n5uLIg0K2pnJ5e06E4Ssxn8zJ6anDdcOJ-k0Xft2W8)
- [2025 GO-CAM transcription: histone readers](https://drive.google.com/open?id=1L_5jlDwXazGGNZUOsz1r8kWYInYeEagk)
- [Managers' minutes (GO-CAM transcription conventions, 2026)](https://drive.google.com/open?id=1PTb0-s9LE8IhsStqhdc25Hb5prdlxBGWbOr8oLfIWNA)

**GO wiki**

- [Annotation consistency: ChIP experiments](https://wiki.geneontology.org/index.php/Annotation_consistency_%3A_ChIP_experiments) (reviewed 2023)
- [Chromatin remodeling manual](https://wiki.geneontology.org/index.php/Chromatin_remodeling_manual) (reviewed 2025)
- [Annotating downstream processes](https://wiki.geneontology.org/index.php/Annotating_downstream_processes)
- [Transcription jamboree](https://wiki.geneontology.org/index.php/Transcription_jamboree) (archived)
- [Proposal to obsolete "promoter binding" and child terms](https://wiki.geneontology.org/index.php/Proposal_to_obsolete_%22promoter_binding%22_and_child_terms)
- [Ontology meeting 2018-09-24](https://wiki.geneontology.org/index.php/Ontology_meeting_2018-09-24)
- [Ontology meeting 2018-10-01](https://wiki.geneontology.org/index.php/Ontology_meeting_2018-10-01)
- [GO-CAM Working Group Call 2018-09-25](https://wiki.geneontology.org/index.php/GO-CAM_Working_Group_Call_2018-09-25)
- [Annotation Conf. Call 2020-02-04](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2020-02-04)
- [Binding Guidelines](https://wiki.geneontology.org/index.php/Binding_Guidelines)

**go-annotation issues**

- [#943](https://github.com/geneontology/go-annotation/issues/943) ChIP and DNA binding
- [#1507](https://github.com/geneontology/go-annotation/issues/1507) host proteins and viral transcription
- [#1720](https://github.com/geneontology/go-annotation/issues/1720), [#2933](https://github.com/geneontology/go-annotation/issues/2933) use of the transcription term
- [#2046](https://github.com/geneontology/go-annotation/issues/2046) DNA-binding annotation for TFs
- [#2130](https://github.com/geneontology/go-annotation/issues/2130) catalytic activity plus dbTF
- [#2584](https://github.com/geneontology/go-annotation/issues/2584) `occurs_at` deprecation
- [#2598](https://github.com/geneontology/go-annotation/issues/2598) `regulates_transcription_of`
- [#2853](https://github.com/geneontology/go-annotation/issues/2853) GTF usage guidance
- [#2972](https://github.com/geneontology/go-annotation/issues/2972) Cdx2 and Pou5f1
- [#2985](https://github.com/geneontology/go-annotation/issues/2985) SKI and SKIL
- [#3086](https://github.com/geneontology/go-annotation/issues/3086) MeCP2
- [#3110](https://github.com/geneontology/go-annotation/issues/3110) ARID and AT-hook proteins
- [#3125](https://github.com/geneontology/go-annotation/issues/3125) THAP proteins
- [#3135](https://github.com/geneontology/go-annotation/issues/3135) NR0B1 hairpin binding
- [#3168](https://github.com/geneontology/go-annotation/issues/3168) MACC1
- [#3231](https://github.com/geneontology/go-annotation/issues/3231) single zinc finger proteins
- [#3235](https://github.com/geneontology/go-annotation/issues/3235) LYAR
- [#3414](https://github.com/geneontology/go-annotation/issues/3414), [#4040](https://github.com/geneontology/go-annotation/issues/4040) histone chaperones as coregulators
- [#3932](https://github.com/geneontology/go-annotation/issues/3932) direction of regulation
- [#4000](https://github.com/geneontology/go-annotation/issues/4000) Epe1 and coTF criteria
- [#4554](https://github.com/geneontology/go-annotation/issues/4554) Taf11, GTF versus coTF
- [#5743](https://github.com/geneontology/go-annotation/issues/5743) NOTCH1

**Repository pages**

- [TRANSCRIPTION_FACTORS](../../TRANSCRIPTION_FACTORS.md) and its synthesized guidelines
- [YEAST_EPIGENETICS_HISTONE_INHERITANCE](../../YEAST_EPIGENETICS_HISTONE_INHERITANCE.md)
- [YEAST_DNA_REPAIR_CHROMATIN](../../YEAST_DNA_REPAIR_CHROMATIN.md)
- [FUNCTION_REQUIREMENT_RULES](../../FUNCTION_REQUIREMENT_RULES.md)
- [IBA_REVIEW](../../IBA_REVIEW.md)
- [ARATH](../../ARATH.md), [BACSU](../../BACSU.md)
- [CLAUDE.md](../../../CLAUDE.md)
