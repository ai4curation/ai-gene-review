# Molecular function: GO annotation guidelines

Status: draft v0.1 (2026-11-15) · Part of [GO_GUIDELINES](../../GO_GUIDELINES.md)

**In brief:**

- A molecular function (MF) annotation says that this gene product, alone or as an
  identified part of a complex, *performs* an activity. It is not a statement about a
  process the product takes part in, a phenotype, or a partner it was seen with.
- Prefer an activity to a binding term. Bare `GO:0005515` protein binding is never a
  goal: in review, replace it with an informative term that the same paper supports, or
  remove it.
- Annotate the activity the protein evolved to perform, on its physiological substrate.
  An assay substrate, a proxy compound or a measurable side reaction is not a function.
- Family membership is a hypothesis about activity, not evidence of it. Check the
  catalytic residues, the substrate, the cofactor and the subunit before accepting a
  family-derived enzyme term.
- A regulator MF needs direct, non-covalent action on an identified target activity.
  Without that, the claim belongs in biological process (BP).
- The term is as deep as *this row's* evidence. A correct general term is refined
  (`MODIFY`) only when the row's own evidence supports the deeper term.

## Scope

This document covers what an MF annotation asserts and how to choose the term:
activity versus binding; the protein binding policy; non-catalytic activities
(adaptor, scaffold, sequestering, carrier, chaperone); enzyme activities, substrate
specificity and promiscuous or non-physiological reactions; pseudoenzymes;
transporters and channels; receptors and ligands (briefly); and regulator activities.

Covered elsewhere: the `contributes_to` qualifier and complex subunits in detail
([protein-complexes.md](protein-complexes.md)); signaling pathways and BP regulation
([regulation-and-signaling.md](regulation-and-signaling.md)); transcription regulators
([transcription-regulation.md](transcription-regulation.md)); evidence codes
([evidence-codes.md](evidence-codes.md)); extension syntax
([annotation-extensions.md](annotation-extensions.md)); NOT annotations
([qualifiers-and-negation.md](qualifiers-and-negation.md)); IBA and electronic
pipelines ([phylogenetic-propagation.md](phylogenetic-propagation.md),
[electronic-annotation.md](electronic-annotation.md)).

## Principles

**An MF is something a molecule does.** The GO editors' definition is "a molecular
process that can be carried out by the action of a single macromolecular machine",
a protein, a non-coding RNA or a complex, usually through direct physical interaction
with other molecules ([wiki: Guidelines for new Molecular Functions](https://wiki.geneontology.org/index.php/Guidelines_for_new_Molecular_Functions)).
MF and BP are meant to be orthogonal: a concept that is really a process (for example
the obsolete "apoptosis inhibitor activity") does not become a function by adding the
word "activity".

**The function is the biological one.** MF substrate specificity represents "the
inferred, in vivo biological specificity of the gene product, which may or may not
correspond exactly to the substrate used in the experiment"
([wiki: Guidelines for catalytic activity terms](https://wiki.geneontology.org/index.php/Guidelines_for_catalytic_activity_terms)).
Curators annotate the conclusion of a paper, not its read-out
([Drive: 2017 GOC training talk](https://drive.google.com/open?id=1m9v6KbdXs32ihzMjqGJYQpuK1Qf49Gh-)).

**Binding is the weakest kind of MF statement.** Every activity involves binding.
A binding term is informative only when binding is the end point (a stable,
biologically meaningful interaction) or when it is all the evidence shows. GO's
non-catalytic MF refactoring created adaptor, carrier, sequestering, receptor and
chaperone terms precisely so that curators could say what a binding protein does
([wiki: Non-catalytic Molecular Functions](https://wiki.geneontology.org/index.php/Non-catalytic_Molecular_Functions)).

**Depth follows evidence, row by row.** A review judges each claim about the gene,
but the action on a row depends on what that row's evidence supports
([CLAUDE.md](../../../CLAUDE.md), maintainer ruling of 2026-11-14).

## Rules

<a id="mf-1"></a>
### MF-1. Assert an MF only for an activity the gene product itself performs

**Use `enables` for an activity the gene product carries out, alone or as the
responsible subunit of a complex. Do not use an MF term to record a process role, a
phenotype, an interaction partner's activity, or an activity the protein merely
supports.**

Rationale. `enables` is the default MF relation and is reserved for "gene products
that mediate a Molecular Function"; accessory subunits "should not be annotated to a
Molecular Function in which they do not directly participate" and usually take
`GO:0060090` molecular adaptor activity or a regulator term instead
([wiki: Enables](https://wiki.geneontology.org/index.php/Enables)). A gene product that
is necessary for an activity is not thereby its performer; the same distinction
governs BP `involved_in` ([CLAUDE.md](../../../CLAUDE.md), "Do not add what curators
deliberately declined to add").

Worked example. In the AMP-activated protein kinase, PRKAA1 is the catalytic subunit
and enables `GO:0004679` AMP-activated protein kinase activity. PRKAG1 binds AMP/ADP and
stabilises the activation loop; it is annotated to `GO:0019887` protein kinase
regulator activity and does *not* contribute to the kinase activity
([wiki: Contributes to](https://wiki.geneontology.org/index.php/Contributes_to)). In the
PIGM–PIGX mannosyltransferase, only PIGM enables `GO:0000030` mannosyltransferase
activity, although PIGX is required.

Where the responsible subunit of a complex is unknown, make no MF annotation; capture
the complex membership (CC) and the process (BP)
([wiki: Contributes to](https://wiki.geneontology.org/index.php/Contributes_to)). The
`contributes_to` qualifier is reserved for irreducible molecular machines; see
[protein-complexes.md](protein-complexes.md).

Provenance: [GOC]. Sources: [wiki: Enables](https://wiki.geneontology.org/index.php/Enables),
[wiki: Contributes to](https://wiki.geneontology.org/index.php/Contributes_to),
[wiki: Guidelines for new Molecular Functions](https://wiki.geneontology.org/index.php/Guidelines_for_new_Molecular_Functions).

<a id="mf-2"></a>
### MF-2. Annotate at the depth this row's evidence supports, and refine only on that evidence

**Choose the most specific term that the cited evidence supports. In review, a correct
but general term is `MODIFY` only when the row's own evidence supports a named deeper
term; otherwise keep it. `TOO_GENERAL` is for terms that are imprecise on their own
once a more specific term is asserted elsewhere.**

Rationale. Electronic and family-level rows legitimately stop at the level their
signature can justify. Refining such a row to the specific term invents evidence. The
2026-11-14 maintainer ruling in [CLAUDE.md](../../../CLAUDE.md) settled a split between
reviews that read the action enum two ways: `MODIFY` needs both a deeper replacement
and this row's evidence for it.

Worked example. An InterPro2GO row maps a generic GPCR signature to `GO:0004930` G
protein-coupled receptor activity on ADRB2. The signature cannot identify the ligand,
so the row stays at `GO:0004930` (`ACCEPT` if core). A separate IDA row from a
ligand-binding and signaling paper supports `GO:0004941` beta2-adrenergic receptor
activity. The IEA row is not `TOO_GENERAL`: a receptor class term is respectably
specific. By contrast, a `GO:0003674` molecular_function-level grouping term or bare
`GO:0005488` binding beside a specific term is imprecise on its own.

When a pleiotropic gene has several supported specific activities, list each one
rather than picking one ([CLAUDE.md](../../../CLAUDE.md)). Lateral corrections (wrong
substrate, wrong cofactor) are also `MODIFY`, and their replacement need not be a
descendant ([MF-11](#mf-11)).

Provenance: [GOC+]. Sources: [CLAUDE.md](../../../CLAUDE.md);
[action consistency](../../../docs/action_consistency.md);
[wiki: Guidelines for catalytic activity terms](https://wiki.geneontology.org/index.php/Guidelines_for_catalytic_activity_terms).

<a id="mf-3"></a>
### MF-3. Prefer an activity term to a binding term

**When the evidence shows what a binding interaction achieves (bridging, carrying,
sequestering, catalysis, regulation, signal transduction, folding), annotate that
activity. Use a binding term only when binding itself is the biologically meaningful
end point, or when binding is all that has been shown.**

Rationale. GO's stated aim is "an annotation to a term other than binding or protein
binding" for every gene product
([wiki: Non-catalytic Molecular Functions](https://wiki.geneontology.org/index.php/Non-catalytic_Molecular_Functions)).
Binding annotations are for interactions that inform the product's normal role;
"protein-protein interactions for which there is not yet sufficient biological context
are out of scope for GO MF annotations"
([wiki: Annotating binding](https://wiki.geneontology.org/index.php/Annotating_binding)).

Worked examples.

- GRB2 carries hundreds of `GO:0005515` rows. Its function is to link activated
  receptor tyrosine kinases to effectors: `GO:0005068` transmembrane receptor protein
  tyrosine kinase adaptor activity and `GO:0005091` guanyl-nucleotide exchange factor
  adaptor activity, with `GO:0001784` phosphotyrosine residue binding as the recognition
  step (`genes/human/GRB2`;
  [worked example](../../MOLECULAR_ADAPTOR_ACTIVITY/worked-example-GRB2.md)).
- Chaperone rows on the obsolete `GO:0051082` unfolded protein binding were reassigned
  to mechanism terms: foldases to `GO:0044183` protein folding chaperone, carrier
  holdases such as the small TIMs to `GO:0140309` unfolded protein holdase activity, and
  SCG5 to `GO:0140318` protein transporter activity. In-situ holdases (CRYAB and others)
  have no fitting term yet and use a proposed "holdase chaperone activity" term
  ([UNFOLDED_PROTEIN_BINDING](../../UNFOLDED_PROTEIN_BINDING.md)).
- When a binding protein's activity is unknown, a class-level binding term is the right
  stopping point, for example `GO:0019901` protein kinase binding or `GO:0035612` AP-2
  adaptor complex binding with the partner in `has_input` ([MF-6](#mf-6)).

Provenance: [GOC]. Sources:
[wiki: Non-catalytic Molecular Functions](https://wiki.geneontology.org/index.php/Non-catalytic_Molecular_Functions),
[wiki: Annotating binding](https://wiki.geneontology.org/index.php/Annotating_binding),
[MOLECULAR_ADAPTOR_ACTIVITY](../../MOLECULAR_ADAPTOR_ACTIVITY.md).

<a id="mf-4"></a>
### MF-4. Do not co-annotate binding that an activity term already implies

**Do not add binding annotations for the substrates, products, cofactors or transported
solutes of an enzyme or transporter activity that is annotated. Annotate the binding term
only when binding is shown and the activity is not.**

Rationale. "An enzyme MUST bind all of the substrates and products of the reaction it
catalyzes. Similarly, a transporter MUST bind the molecules it transports"
([wiki: Binding Guidelines](https://wiki.geneontology.org/index.php/Binding_Guidelines)).
Redundant binding rows add noise and are a common carrier for pseudoenzyme errors,
because cofactor-binding IEA rows travel with the catalytic term ([MF-13](#mf-13)).

Worked examples.

- A kinase annotated to `GO:0004674` protein serine/threonine kinase activity does not
  need `GO:0005524` ATP binding from the same evidence.
- A paper that shows binding of a non-hydrolysable ATP analogue but no ATPase activity
  supports `GO:0005524` ATP binding by IDA, with the analogue in With/From where the
  evidence code allows it ([wiki: Binding Guidelines](https://wiki.geneontology.org/index.php/Binding_Guidelines)).
- Do not put the bound entity in an extension when the term already names it
  (`GO:0005524` ATP binding with `has_input` ATP is redundant).

In review, an existing implied-binding row is true; it is not `REMOVE`. Use
`KEEP_AS_NON_CORE`, or `TOO_GENERAL` when it is a general term such as `GO:0046872`
metal ion binding beside an activity that specifies the metal-dependent chemistry.

Provenance: [GOC]. Sources:
[wiki: Binding Guidelines](https://wiki.geneontology.org/index.php/Binding_Guidelines),
[wiki: Annotating binding](https://wiki.geneontology.org/index.php/Annotating_binding).

<a id="mf-5"></a>
### MF-5. Treat bare `GO:0005515` protein binding as uninformative: never propose it, and in review replace or remove it

**Never make a new bare `GO:0005515` annotation. In review, an existing bare
`GO:0005515` row is `MODIFY` when the row's paper supports a more informative MF
(adaptor, regulator, a class-level binding term), otherwise `REMOVE`, or `UNDECIDED` when
the paper cannot be read. Never `ACCEPT`, `KEEP_AS_NON_CORE` or `MARK_AS_OVER_ANNOTATED`
it. A `REMOVE` says the annotation is uninformative, not that the interaction is false.**

Rationale. GO:0005515 says that a protein sticks to something, not what it does. An
IEA working group proposal (2026) puts the scale plainly: protein binding is 33% of all
experimental annotations and 70% of experimental MF annotations, 82% of those come from
IntAct exports, and many groups do not curate it at all
([Drive: protein binding do_not_annotate proposal](https://drive.google.com/open?id=1KKM7gxsPvQgszjppuyD_ZldM_T8cGV0ajSUIfLmyNQc)).
The same proposal would add `GO:0042802` identical protein binding and
`GO:0046983` protein dimerization activity (and its homo- and hetero- children) to the
do-not-annotate subset, because they carry the same information content and
multimerisation is out of scope for GO. This repository already enforces the policy on
GO:0005515 as a validator warning
([protein_binding_policy.py](../../../src/ai_gene_review/validation/protein_binding_policy.py)).
It is the one sanctioned case where `REMOVE` may be used on a true statement
([CLAUDE.md](../../../CLAUDE.md)).

Rules that still apply to any surviving GO:0005515 row, and that a reviewer should
check: the partner must be in With/From (gorule-0000003, gorule-0000018); `NOT` must
not be used with GO:0005515; ISS must not be used; and interspecies binding is allowed
only for physiological interactions, with the experimentally used partner in With/From
([wiki: Binding Guidelines](https://wiki.geneontology.org/index.php/Binding_Guidelines);
[go-annotation#3314](https://github.com/geneontology/go-annotation/issues/3314)).

Worked example. RPTOR has 61 GO:0005515 rows. Split by partner, they fall into two
groups: binding to MTOR, and binding to TOS-motif substrates such as the 4E-BPs and
S6 kinases. The second group supports `GO:0140767` enzyme-substrate adaptor activity
(`MODIFY`); single co-immunoprecipitation hits with no bridging context are `REMOVE`
([worked example](../../MOLECULAR_ADAPTOR_ACTIVITY/worked-example-RPTOR.md)).

For `GO:0042802` and `GO:0046983` rows: until GO decides the proposal, keep a row only
when the oligomer is itself functionally informative and the evidence shows it;
otherwise treat the row the way GO:0005515 is treated. Earlier GOC reviews moved
`IDA` heterodimerization rows to GO:0005515 with an interactor in With/From and removed
`NAS`/`TAS` rows
([go-annotation#2683](https://github.com/geneontology/go-annotation/issues/2683)).

Provenance: [NEW] for the review actions (this repository's policy, ahead of a pending
GOC proposal); [GOC] for the QC rules. Sources: as cited.

<a id="mf-6"></a>
### MF-6. Use class-level binding children; name the specific partner in `has_input`

**When a binding term is warranted, choose the child that names the class of partner
(`GO:0019901` protein kinase binding, `GO:0030971` receptor tyrosine kinase binding).
Put the specific physiological partner in `has_input`; put the partner actually used in
the experiment in With/From. Do not request binding terms for individual proteins.**

Rationale. Subclasses of GO:0005515 "should represent general classes of proteins, not
specific proteins"
([wiki: Guidelines for new Binding terms](https://wiki.geneontology.org/index.php/Guidelines_for_new_Binding_terms)).
GO obsoleted the per-partner children of transcription factor binding for the same
reason ([wiki: Proposal to obsolete children of "transcription factor binding"](https://wiki.geneontology.org/index.php/Proposal_to_obsolete_children_of_%22transcription_factor_binding%22)).
With/From supports the evidence; the extension modifies the term. A mouse receptor shown
to bind a human ligand is annotated with the human ligand in With/From and the
orthologous mouse ligand in `has_input`
([wiki: Annotating binding](https://wiki.geneontology.org/index.php/Annotating_binding)).

Worked example. C. elegans UNC-115 binds filaments made from rabbit skeletal muscle
actin: `GO:0051015` actin filament binding, IPI, rabbit actin in With/From. Actin,
tubulin and histone binding are exceptions to the `has_input` recommendation because
many identical copies exist and the copy used is rarely known
([wiki: Annotating binding](https://wiki.geneontology.org/index.php/Annotating_binding)).

Provenance: [GOC]. Sources: as cited.

<a id="mf-7"></a>
### MF-7. For small molecules, annotate the physiological ligand; never the drug or probe

**Annotate small-molecule binding as `GO:0005488` binding (or an existing specific
binding term) with `has_input` a ChEBI entity, rather than requesting a new
pre-composed term. When a compound was used as a proxy for a natural ligand, annotate
binding of the natural ligand. Make no binding annotation for a drug interaction that
is a gain of function outside the protein's normal role.**

Rationale. The 2020 ontology editors' decision asks curators to use binding plus
`has_input` ChEBI for chemical binding
([wiki: Annotation Conf. Call 2020-02-04](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2020-02-04)).
The obsoletion of "drug binding" set the three-way rule for compounds
([go-annotation#3166](https://github.com/geneontology/go-annotation/issues/3166)):
proxy for a natural ligand, annotate the natural ligand; pathway inhibitor, annotate the
pathway BP only for products that normally act in it; gain-of-function drug binding,
annotate nothing.

Worked examples. LSD binding to a serotonin receptor supports `GO:0051378` serotonin
binding (LSD in With/From where allowed); strychnine binding supports `GO:0016594`
glycine binding. FKBP1A (FKBP12) inhibits TORC1 only when bound to rapamycin, which is
not part of its normal role, so its drug binding rows were deleted and no TORC1
signaling annotation is made for it. Its own enzymatic activity,
`GO:0003755` peptidyl-prolyl cis-trans isomerase activity, is the informative MF.
(`GO:0005528` FK506 binding is itself a drug-named term worth questioning; see Open
questions.)

Provenance: [GOC]. Sources: as cited.

<a id="mf-8"></a>
### MF-8. Distinguish adaptor, scaffold, sequestering, carrier and regulator by what the binding does

**Choose among the non-catalytic activities by the test in the [Decision aid](#decision-aid):
adaptor (brings two or more molecules together so they act in a coordinated way),
scaffold (structural organiser of a complex), sequestering (binds a molecule to keep it
from its partners or location), carrier (moves with its cargo to an acceptor or
location), regulator (modulates the target's activity directly). An adaptor annotation
needs evidence of at least two bridged partners.**

Rationale. The GO-CAM activity-unit guidelines define each activity by its inputs and
its causal effect
([Drive: MF guidelines for GO-CAM](https://drive.google.com/open?id=1DWvc_g5yH4S8-Tc2rPtaAyPOIkYzITagK1sXysj0CY4)).
The adaptor activity "has input the two (or more) molecules it brings together", and the
guideline warns that a single input suggests adaptor activity may not be the right term.
A single binary interaction (one IPI hit) evidences binding, not bridging
([MOLECULAR_ADAPTOR_ACTIVITY](../../MOLECULAR_ADAPTOR_ACTIVITY.md), decision rule 1).
In the ontology the adaptor and scaffold branches are separate: `GO:0140378` protein
complex scaffold activity (and its child `GO:0160072` ubiquitin ligase complex scaffold
activity) sit under `GO:0005198` structural molecule activity, not under `GO:0060090`
molecular adaptor activity, whereas `GO:0140693` molecular condensate scaffold activity
and `GO:0140566` histone reader activity are adaptor children (checked against the
local GO release, 2026-11-15).

Worked examples.

- LDLRAP1 bridges the LDL receptor's NPxY motif to clathrin and AP-2:
  `GO:0035615` clathrin-cargo adaptor activity (`genes/human/LDLRAP1`).
- In a cullin–RING ligase, CUL4A or DDB1 enables `GO:0160072` ubiquitin ligase complex
  scaffold activity with `has_input` the substrate adaptor and the ligase, and the
  substrate receptor enables `GO:1990756` ubiquitin-like ligase-substrate adaptor
  activity with `has_input` the substrate
  ([Drive: MF guidelines for GO-CAM](https://drive.google.com/open?id=1DWvc_g5yH4S8-Tc2rPtaAyPOIkYzITagK1sXysj0CY4)).
- CAV1 binds TLR4 and holds it inactive: `GO:0140311` protein sequestering activity,
  `has_input` TLR4, part of negative regulation of the TLR4 pathway.
- CD14 delivers LPS to TLR4–MD-2: `GO:0140104` molecular carrier activity; the
  carrier "moves with the substrate it carries", which distinguishes it from a
  transporter ([wiki: Non-catalytic Molecular Functions](https://wiki.geneontology.org/index.php/Non-catalytic_Molecular_Functions)).

In standard annotation, the MF-to-MF relations (`directly positively regulates`,
`provides input for`) are not captured; record the MF, its `has_input` partners, the BP
and the CC ([Drive: MF guidelines for GO-CAM](https://drive.google.com/open?id=1DWvc_g5yH4S8-Tc2rPtaAyPOIkYzITagK1sXysj0CY4)).
A general adaptor term may stand beside a specific child only for a distinct bridging
event the child does not cover; otherwise the parent is `TOO_GENERAL`
([MOLECULAR_ADAPTOR_ACTIVITY](../../MOLECULAR_ADAPTOR_ACTIVITY.md), decision rule 5).

Provenance: [GOC+]. Sources: as cited;
[go-annotation#3510](https://github.com/geneontology/go-annotation/issues/3510) for
adaptor terms on non-catalytic transporter subunits.

<a id="mf-9"></a>
### MF-9. Support catalytic activity with evidence of catalysis, at the enzyme's natural specificity

**Annotate a catalytic activity only from evidence that the product catalyses the
reaction (an activity assay, a catalytic-residue mutant, a complementation with
activity read-out). Never use IPI for catalytic activity terms. Choose the term whose
substrate range matches the enzyme's in vivo specificity: annotate the L-amino acid or
D-sugar form by default, and annotate both the NAD+ and NADP+ terms when the enzyme
uses both.**

Rationale. Gorule-0000007 forbids IPI for `is_a` descendants of `GO:0003824` catalytic
activity: "It is unlikely that enough information can be obtained from a binding
interaction to support such an annotation"
([wiki: IPI](https://wiki.geneontology.org/index.php/Inferred_from_Physical_Interaction_%28IPI%29);
[go-annotation#2131](https://github.com/geneontology/go-annotation/issues/2131)). The
2021 Rhea jamboree set the specificity rules: "The specificity of GO MFs is at the same
level of the specificity of enzymes; we do not create terms for each substrate if an
enzyme can act on a group of substrates"; amino acids default to the L form and sugars
to the D form; NAD(P) in a GO label means the cofactor is *unknown*, unlike IUBMB usage,
so an enzyme known to use both gets two annotations
([wiki: Annotation Conf. Call 2021-08-03](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2021-08-03);
[wiki: Guidelines for catalytic activity terms](https://wiki.geneontology.org/index.php/Guidelines_for_catalytic_activity_terms)).

Worked examples. Phospholipases that act on many acyl chains are annotated to the
general reaction (`GO:0004620` glycerophospholipase activity and its reaction-level
children), not to one Rhea reaction per chain. Phosphoserine phosphatases are annotated
to `GO:0036424` L-phosphoserine phosphatase activity; the parent and the D-form term
were merged or obsoleted after a spot check showed every annotation concerned the L
form. Positional terms for protein substrates are out of scope except for the histone
code (`GO:0042800` histone H3K4 methyltransferase activity) and ncRNA modifications.

Provenance: [GOC]. Sources: as cited.

<a id="mf-10"></a>
### MF-10. Annotate the physiological reaction, not the assay substrate

**Do not annotate an activity whose only support is an assay substrate, a chromogenic or
fluorogenic surrogate, a tracer ion, or a non-physiological reaction. Annotate the
physiological activity the assay was designed to measure, if the paper supports it;
otherwise annotate the more general activity the assay does establish.**

Rationale. "Annotate the conclusion rather than the assay": rubidium is used to assay
potassium transport, and kinases are often tested on histones that are not their
substrates ([Drive: 2017 GOC training talk](https://drive.google.com/open?id=1m9v6KbdXs32ihzMjqGJYQpuK1Qf49Gh-)).
PomBase does not annotate in vitro substrates known to be irrelevant in vivo
([go-annotation#1953](https://github.com/geneontology/go-annotation/issues/1953)). GO
has obsoleted molecular function terms for non-physiological reactions, keeping the EC
number but removing the EC-to-GO mapping
([go-annotation#1514](https://github.com/geneontology/go-annotation/issues/1514),
[go-annotation#1519](https://github.com/geneontology/go-annotation/issues/1519)).

Worked examples.

- Gamma-glutamyl transpeptidases hydrolyse glutathione; transfer to an acceptor needs
  millimolar acceptor concentrations. `GO:0003840` gamma-glutamyltransferase activity is
  now obsolete for that reason.
- `GO:0102306` benzil reductase [(S)-benzoin-forming] activity was a chromogenic
  read-out that EC and Rhea turned into a reaction; GO obsoleted it, and the S. pombe
  annotations were moved up to the grouping class `GO:0016616` oxidoreductase
  activity, acting on the CH-OH group of donors, NAD or NADP as acceptor
  ([go-annotation#5840](https://github.com/geneontology/go-annotation/issues/5840)).
  The obsoletion left Rhea:25968 as a narrow match on that grouping class, which now
  generates uninformative IEA rows ([NONPHYSIOLOGICAL_REACTIONS](../../NONPHYSIOLOGICAL_REACTIONS.md)).
- A synthetic substrate is not by itself the test. Atrazine chlorohydrolase and
  haloalkane dehalogenase act on man-made chemicals but are selected,
  pathway-committed enzymes; they keep their specific terms. Use pathway membership and
  host genetics to tell an evolved xenobiotic-degrading enzyme from an assay artefact;
  kinetics alone is the weakest signal ([NONPHYSIOLOGICAL_REACTIONS](../../NONPHYSIOLOGICAL_REACTIONS.md)).

Provenance: [GOC] for the principle; [GOC+] for the synthetic-substrate distinction.
Sources: as cited.

<a id="mf-11"></a>
### MF-11. Measured activity is not automatically function: apply the three tiers

**For an enzyme activity that was measured but is weak or promiscuous, decide whether
the protein evolved to catalyse the reaction, and act by tier: a genuine secondary
activity is `KEEP_AS_NON_CORE`; real in vitro activity of unknown relevance is
`MARK_AS_OVER_ANNOTATED`; noise-level activity, when a dedicated enzyme for the same
reaction exists in the organism, is `REMOVE`, even on an IDA row. State the judgement in
`reason`; there is no numeric cutoff.**

Rationale. The tiers follow de Crécy-Lagard et al. 2025
([PMID:40703034](https://europepmc.org/article/MED/40703034), a framework for
evaluating function predictions) and were adopted after a single "secondary activities
are non-core" rule would have kept a noise-level activity
([ENZYME_SPECIFICITY](../../ENZYME_SPECIFICITY.md); [CLAUDE.md](../../../CLAUDE.md)).
`REMOVE` in the third tier accepts the measurement and argues that the activity is not
the gene's function, which is the "genuinely contradicted function" case that permits
removing an experimental row.

Indicators for the `REMOVE` tier (most should hold): a dedicated enzyme for the reaction
exists in the same organism, ideally essential or non-redundant; the activity is orders
of magnitude below it (about 10³-fold or more as a guide); the protein sits in a
different subfamily or lacks the specificity determinants; there is no in vivo
phenotype for the reaction.

Worked pair ([ENZYME_SPECIFICITY](../../ENZYME_SPECIFICITY.md)).

- E. coli YciO, `GO:0061710` L-threonylcarbamoyladenylate synthase activity: `REMOVE`.
  TsaC is the essential dedicated enzyme, YciO's rate is about 10⁴-fold lower, and
  YciO lacks the KRSN tetrad and sits in another subfamily.
- E. coli YjdM, `GO:0047400` phosphonoacetate hydrolase activity:
  `MARK_AS_OVER_ANNOTATED`. The phosphonate link is a name collision, but E. coli has no
  dedicated phosphonoacetate hydrolase, so the activity cannot be assigned elsewhere.

Provenance: [NEW]. GOC guidance says to annotate physiological activities but gives no
rule for graded promiscuity. Sources: as cited.

<a id="mf-12"></a>
### MF-12. Check each axis of specificity before accepting a family-derived enzyme term

**Before accepting a catalytic term that rests on family membership (IEA, IBA, ISS, or
an experimental row that names a broad class), check four axes: substrate range (and
chain length), cofactor or donor, reaction mechanism, and subunit, paralog or name
identity. A failure on any axis is `MODIFY` (lateral or refining) or `REMOVE`.**

Rationale. Specificity errors are where family-based annotation is most confidently
wrong: the fold and often the EC class are right, so nothing looks amiss until someone
checks the substrate, cofactor or subunit ([ENZYME_SPECIFICITY](../../ENZYME_SPECIFICITY.md)).

Worked examples, all from completed reviews in this repository:

| Axis | Gene | Row | Action |
|---|---|---|---|
| Substrate too narrow | C. albicans LPL1 | `GO:0004622` phosphatidylcholine lysophospholipase A1 activity | `MODIFY` → `GO:0102545` B-type glycerophospholipase activity |
| Chain length | human HADH | `GO:0016509` long-chain (3S)-3-hydroxyacyl-CoA dehydrogenase (NAD+) activity | `MARK_AS_OVER_ANNOTATED`; the short/medium-chain `GO:0003857` is correct |
| Mechanism | human PHYKPL | `GO:0008483` transaminase activity | `REMOVE`; the enzyme is a phospho-lyase (`GO:0016838` carbon-oxygen lyase activity, acting on phosphates) |
| Donor | S. erythraea EryCIII | `GO:0008194` UDP-glycosyltransferase activity | `REMOVE`; it transfers a dTDP-sugar, and `GO:0016758` hexosyltransferase activity is already present |
| Subunit | human HADHA | `GO:0003985` acetyl-CoA C-acetyltransferase activity | `REMOVE`; thiolase is the HADHB subunit's activity |
| Name collision | human ACAT1 | `GO:0034736` cholesterol O-acyltransferase activity | `REMOVE`; the row came from a SOAT1 paper via the shared "ACAT1" nickname |

A specific term should be verified, not assumed, even when it is probably right: the
C. albicans GND1 review confirmed NADP+ specificity (`GO:0004616`) from the coenzyme
motifs rather than accepting it from family membership.

Provenance: [NEW] for the four-axis check; [GOC] for the underlying "annotate in vivo
specificity" principle. Sources: [ENZYME_SPECIFICITY](../../ENZYME_SPECIFICITY.md),
[RHEA](../../RHEA.md).

<a id="mf-13"></a>
### MF-13. Do not annotate catalysis to a pseudoenzyme; annotate what it does instead

**A protein that keeps an enzyme fold but lacks the catalytic machinery does not get the
family's catalytic activity, or the cofactor-binding and process terms that follow from
it. Check catalytic residues, the motif context around them, and biochemical data. Where
a non-catalytic role is shown (activator, scaffold, reader, decoy, chaperone), annotate
that role.**

Rationale. InterPro2GO, EC2GO, UniRule, ARBA and IBA propagate catalytic terms from
family membership without checking residue conservation, so pseudoenzymes are a
systematic source of false enzyme annotations
([PSEUDOENZYMES](../../PSEUDOENZYMES.md)). The same check generalises as "function
requirement" rules: a catalytic or transport term should be flagged when the protein
lacks a domain the activity needs. Flags from those rules include beta-adrenergic
receptors annotated to `GO:0003924` GTPase activity (a GPCR activates G proteins and does
not hydrolyse GTP) and G beta and gamma subunits annotated `enables` GTPase activity
([FUNCTION_REQUIREMENT_RULES](../../FUNCTION_REQUIREMENT_RULES.md)).

Action ladder ([PSEUDOENZYMES](../../PSEUDOENZYMES.md), decision tree):

1. Confirm the protein is in the family you think (a "broken" Cu/Zn-SOD can be a normal
   Mn-SOD from another family).
2. Catalytic residues lost: `MARK_AS_OVER_ANNOTATED` the catalytic rows.
3. Residues present but family motif context broken: `MARK_AS_OVER_ANNOTATED`, with the
   caveat stated.
4. Activity refuted biochemically: `REMOVE` the catalytic rows and their dependent
   cofactor and process rows, and add `NEW` rows for the shown function.
5. Residues intact, no assay: keep the catalytic row, noting it rests on sequence.

Worked examples. S. pombe Epe1, a JmjC protein with no detectable demethylase activity:
electronic `GO:0032452` histone demethylase activity, `GO:0051213` dioxygenase activity
and `GO:0016491` oxidoreductase activity rows `REMOVE`; experimental `GO:0032454`
histone H3K9 demethylase activity rows `UNDECIDED`, since a latent activity is not
excluded. EryCII, a P450-fold activator of the glycosyltransferase EryCIII:
`GO:0004497` monooxygenase activity, `GO:0005506` iron ion binding and `GO:0020037`
heme binding `REMOVE`. Human pseudokinases illustrate the replacement terms: STRAD
activates LKB1 (`GO:0043539` protein serine/threonine kinase activator activity).

Provenance: [NEW]. GOC guidance does not address pseudoenzymes as a class; PAINT handles
them case by case through loss annotations. Sources: as cited;
[PMID:40703034](https://europepmc.org/article/MED/40703034) (PSEUDOENZYME_OVERANNOTATION
error class).

<a id="mf-14"></a>
### MF-14. Give each subunit of a complex the activity it performs

**Annotate the catalytic subunit with `enables`; annotate regulatory subunits with a
regulator activity, bridging subunits with an adaptor activity, and structural subunits
with a structural or scaffold activity. Use `contributes_to` only for an irreducible
machine whose activity cannot be ascribed to a subset of subunits.**

Rationale. The 2020 complex working group established that the MF goes to the subunit
that performs it and that non-participating subunits receive no MF
([wiki: Contributes to](https://wiki.geneontology.org/index.php/Contributes_to)). Its
checklist asks whether the activity occurs without the subunit, whether the subunit can
be given another MF, and whether the annotation would still hold if the qualifier were
dropped. Details and the complex-membership rules are in
[protein-complexes.md](protein-complexes.md).

Worked examples. Non-catalytic subunits of the Na+/K+-ATPase move from `contributes_to`
the pump activity to `GO:0001671` ATPase activator activity, `GO:0030674`
protein-macromolecule adaptor activity or `GO:0016247` channel regulator activity, with
`has_input` the catalytic subunit
([go-annotation#3510](https://github.com/geneontology/go-annotation/issues/3510)).
eIF2 gamma enables GTPase activity; eIF2 alpha and beta do not.

Provenance: [GOC]. Sources: as cited.

<a id="mf-15"></a>
### MF-15. Annotate transport as a specific transmembrane transporter or channel activity, on the physiological solute

**Use a descendant of `GO:0022857` transmembrane transporter activity that names the
solute and, where known, the mechanism (`GO:0015267` channel activity, `GO:0015293`
symporter activity, `GO:0015297` antiporter activity, `GO:0042626` ATPase-coupled
transmembrane transporter activity). Never annotate `GO:0005215` transporter activity
(do-not-annotate). Name the physiological solute, not the tracer. Do not transfer
substrate specificity across species without clear 1:1 orthology.**

Rationale. GO:0005215 was made do-not-annotate in 2019
([go-annotation#2311](https://github.com/geneontology/go-annotation/issues/2311)).
Transporter substrate specificity diverges among paralogs, so a mammalian substrate
should not be propagated to yeast without a clear 1:1 relationship
([go-annotation#2033](https://github.com/geneontology/go-annotation/issues/2033)).
A transmembrane transporter needs a transmembrane segment or a membrane barrel, carrier
or channel family (FRR:0004 in [FUNCTION_REQUIREMENT_RULES](../../FUNCTION_REQUIREMENT_RULES.md)).
TCDB classification would be a good source of transporter MF annotations, but GO has no
`tc2go` pipeline, and family-level TC leads over-propagate
([TCDB](../../TCDB.md)).

Worked examples. A ⁸⁶Rb⁺ flux assay on a potassium channel supports `GO:0005249`
voltage-gated potassium channel activity if voltage gating is shown, or a potassium
channel term otherwise; it does not support a rubidium term (GO obsoleted rubidium ion
transmembrane transporter activity because it "represents an assay";
[NONPHYSIOLOGICAL_REACTIONS](../../NONPHYSIOLOGICAL_REACTIONS.md)). A secreted
lipid-binding protein that shuttles its ligand is a carrier (`GO:0140104`), not a
transporter ([MF-8](#mf-8)).

Provenance: [GOC] for the do-not-annotate and orthology rules; [GOC+] for the
membrane-requirement check. Sources: as cited;
[Drive: Transporter activity guidelines (archived)](https://drive.google.com/open?id=1h26nq-KExaYZKuBVKqJ2yWkK06dCWUQelZkTI262_PA).

<a id="mf-16"></a>
### MF-16. Annotate a receptor's signaling activity and a ligand's ligand activity, not reciprocal binding

**A signaling receptor enables `GO:0038023` signaling receptor activity or a descendant
(ligand-specific where the evidence identifies the ligand). A protein ligand enables
`GO:0048018` receptor ligand activity or a descendant, with `has_input` its receptor. The
receptor's input is its effector, not its ligand. Small-molecule ligands are not
annotated.**

Rationale. The GO-CAM receptor guideline (reviewed 2023 and 2026) keeps the causal flow
from ligand to receptor to effector
([Drive: MF guidelines for GO-CAM](https://drive.google.com/open?id=1DWvc_g5yH4S8-Tc2rPtaAyPOIkYzITagK1sXysj0CY4)).
In the ontology, `GO:0048018` receptor ligand activity has part `GO:0005102` signaling
receptor binding and is part of `GO:0007165` signal transduction, so a ligand annotated
correctly does not also need the binding term. Ligands carrying only a
receptor-specific binding term (such as "Roundabout binding") instead of a ligand
activity are a recurring gap ([LIGANDS_IN_SIGNALING](../../LIGANDS_IN_SIGNALING.md)).
Pathway membership of ligands and receptors is covered in
[regulation-and-signaling.md](regulation-and-signaling.md).

Worked example. Netrin-1 enables `GO:0048018` receptor ligand activity with
`has_input` DCC (`genes/human/NTN1`); its IBA rows to DNA-binding transcription factor
activity were `REMOVE` ([TRANSCRIPTION_FACTORS](../../TRANSCRIPTION_FACTORS.md)). A
ligand-specific receptor term such as `GO:0004941` beta2-adrenergic receptor activity
needs evidence that identifies the ligand ([MF-2](#mf-2)). A coreceptor that is
activated by the ligand-bound receptor enables `GO:0015026` coreceptor activity.

Provenance: [GOC]. Sources: as cited.

<a id="mf-17"></a>
### MF-17. Reserve regulator MFs for direct, non-covalent action on an identified target activity

**Annotate a molecular function regulator (a descendant of `GO:0098772`, such as
`GO:0004857` enzyme inhibitor activity, `GO:0008047` enzyme activator activity,
`GO:0019887` protein kinase regulator activity or `GO:0008200` ion channel inhibitor
activity) only when the product binds the target and changes its activity without
covalently modifying it. Name the target in `has_input`. If the target is modified
covalently, annotate the catalytic activity. If direct action is not shown, annotate the
BP regulation term instead. Never annotate `GO:0098772` itself (do-not-annotate).**

Rationale. GO defines a regulator as acting "via non-covalent binding that does not
result in covalent modification to the target"; catalytic activities that modify a
target are out of scope for regulator terms
([wiki: Guidelines for new Molecular Functions](https://wiki.geneontology.org/index.php/Guidelines_for_new_Molecular_Functions)).
PomBase's practice, recorded in the 2018 IPI discussion, is to capture direct
regulation as an MF and to avoid BP "regulation of enzyme activity", which can be far
upstream ([go-annotation#2131](https://github.com/geneontology/go-annotation/issues/2131)).
In 2014 GO agreed that binding and regulation may come from two experiments in one
paper, or from two papers, and be combined into one regulator annotation by IC
([wiki: Annotation Conf. Call, January 14, 2014](https://wiki.geneontology.org/index.php/Annotation_Conf._Call,_January_14,_2014)).
IPI is permitted for enzyme regulator terms: gorule-0000007 applies only to `is_a`
descendants of catalytic activity ([go-annotation#2131](https://github.com/geneontology/go-annotation/issues/2131)).

Worked examples.

- A serpin that binds and inactivates a serine protease: `GO:0004867` serine-type
  endopeptidase inhibitor activity, `has_input` the protease.
- A kinase that phosphorylates and inactivates another kinase: protein kinase activity
  with `has_input` the target, not `GO:0004860` protein kinase inhibitor activity.
- A knockdown that raises a kinase's activity in cell lysates, with no binding data:
  a BP regulation term ([regulation-and-signaling.md](regulation-and-signaling.md)),
  not an MF.
- A decoy receptor that binds a ligand so it cannot reach the signaling receptor: in
  GO-CAM, binding that `directly negatively regulates` the receptor activity
  ([wiki: Annotation Conf. Call 2019-11-19](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2019-11-19));
  in standard annotation, `GO:0140311` protein sequestering activity with `has_input`
  the ligand.
- An endogenous small molecule that activates the product is not a reason for a
  regulator MF on the product. The 2019–2020 reannotation turned `activated_by`
  extensions into a binding annotation on the product, and restricted
  `directly regulates` to activities of different gene products
  ([wiki: Annotation Conf. Call 2020-02-04](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2020-02-04)).

Provenance: [GOC+]. GOC states the definition; the "covalent means catalytic" and
"unknown mechanism means BP" rules are spread across several calls and are stated here
together. Sources: as cited.

<a id="mf-18"></a>
### MF-18. Treat an electronic MF as a claim about the family, and check it fits this member

**An IEA or IBA MF row is a claim that this member shares the family's activity. Accept
it when the member retains what the activity requires and nothing specific contradicts
it. Challenge it with member-specific evidence (lost residues, different subfamily,
divergent substrate, contrary experiment), not with the type of evidence.**

Rationale. An IBA carries a PAINT curator's judgement about where in the tree a function
arose; challenging it means arguing with the node placement, not with donor counts
([CLAUDE.md](../../../CLAUDE.md); [phylogenetic-propagation.md](phylogenetic-propagation.md)).
InterPro2GO and UniRule mappings are usually right for most members and wrong for
specific subfamilies, which is where curated exception rules belong
([electronic-annotation.md](electronic-annotation.md)). The common MF failure modes,
all with worked cases above, are pseudoenzymes ([MF-13](#mf-13)), wrong-paralog
specificity ([MF-12](#mf-12)), and adaptor or dbTF terms over-propagated to members
that do not bridge or bind DNA ([MF-8](#mf-8);
[transcription-regulation.md](transcription-regulation.md)).

Worked example. C. albicans LPL1's `GO:0047372` monoacylglycerol lipase activity IBA
traced to the S. cerevisiae ROG1 paralog at the PAINT node; LPL1 sits in the
phospholipase B branch, so the row was `REMOVE`
([ENZYME_SPECIFICITY](../../ENZYME_SPECIFICITY.md)).

Provenance: [GOC+]. Sources: as cited.

## Decision aid

### Choosing an MF for a binding protein

| What the evidence shows | Term family | Required context |
|---|---|---|
| Catalysis of a reaction (assay, active-site mutant) | descendant of `GO:0003824` catalytic activity | substrate in the term or `has_input`; never IPI |
| Brings two or more molecules together so they act together | `GO:0060090` molecular adaptor activity or a child (`GO:0030674` and below) | `has_input` both partners |
| Holds a complex together structurally | `GO:0140378` protein complex scaffold activity or `GO:0005198` structural molecule activity | complex in CC |
| Binds a molecule to keep it from partners or location | `GO:0140313` molecular sequestering activity (`GO:0140311` for proteins) | `has_input` the sequestered molecule; BP is negative regulation of its process |
| Binds and moves with a molecule to an acceptor or location | `GO:0140104` molecular carrier activity | `has_input` the cargo |
| Moves a solute across a membrane without moving itself | descendant of `GO:0022857` | solute in term or `has_input` |
| Binds a target and changes its activity, non-covalently | descendant of `GO:0098772` (not the root) | `has_input` the target |
| Receives a signal and transmits it | descendant of `GO:0038023` signaling receptor activity | `has_input` the effector |
| Activates a receptor as its ligand | `GO:0048018` receptor ligand activity or a child | `has_input` the receptor |
| Assists folding | `GO:0044183` protein folding chaperone; carrier holdases `GO:0140309` | see [UNFOLDED_PROTEIN_BINDING](../../UNFOLDED_PROTEIN_BINDING.md) |
| Binding of a defined class, role unknown | class-level binding child (e.g. `GO:0019901`) | `has_input` the specific partner |
| Binding of an unnamed protein class, role unknown | nothing new; in review `MODIFY` or `REMOVE` existing `GO:0005515` | partner in With/From |

### Reviewing a measured enzyme activity

1. Is the activity on the physiological substrate? If no, go to [MF-10](#mf-10).
2. Is the protein catalytically competent (residues, motif, assay)? If no, go to
   [MF-13](#mf-13).
3. Is the substrate, cofactor, mechanism and subunit right? If no, go to
   [MF-12](#mf-12).
4. Is it the protein's evolved activity? Apply the tiers of [MF-11](#mf-11).
5. Is the term as deep as this row's evidence, and no deeper? See [MF-2](#mf-2).

### MF regulator or BP regulation?

| Evidence | Annotation |
|---|---|
| Direct binding and a change in the target's activity, no covalent change | regulator MF, `has_input` target |
| Covalent modification of the target that changes its activity | catalytic MF, `has_input` target |
| Change in target activity, mechanism unknown | BP regulation term |
| Binding only | class-level binding term at most |
| Binding (one experiment) plus regulation (another) | regulator MF by IC citing both |

## Common errors

**Bare protein binding kept as core.** Reviews that `ACCEPT` or `KEEP_AS_NON_CORE`
GO:0005515 preserve an annotation with no functional content. Fix: `MODIFY` to the
informative term the same paper supports, else `REMOVE` ([MF-5](#mf-5)).

**Adaptor activity from one IPI hit.** A single binary interaction becomes
`GO:0060090`. Fix: use a class-level binding term unless two bridged partners are
shown ([MF-8](#mf-8)).

**Scaffold filed as adaptor, or adaptor as scaffold.** Fix: check the branch. Complex
scaffolds are structural molecule activity; condensate scaffolds and histone readers are
adaptor children.

**Implied binding stacked on an activity.** ATP binding, metal ion binding and heme
binding rows beside a kinase, metalloenzyme or P450. Fix: do not add them; in review,
mark them non-core or `TOO_GENERAL` rather than removing a true statement ([MF-4](#mf-4)).
When the activity itself is wrong (a pseudoenzyme), remove the dependent rows with it
([MF-13](#mf-13)).

**Assay substrate as function.** Histone kinase activity for a kinase tested on
histones; a chromogenic-substrate reductase; a rubidium flux. Fix: annotate the
physiological activity or the general activity the assay supports ([MF-10](#mf-10)).

**Catalytic activity by IPI.** Fix: re-code to the assay that shows catalysis, or remove
(gorule-0000007).

**Family membership read as specificity.** Transaminase activity for a phospho-lyase
in the aminotransferase family; UDP-sugar transferase for a dTDP-sugar enzyme. Fix:
check the four axes of [MF-12](#mf-12).

**Regulator MF from a knockdown.** A loss-of-function change in an enzyme's activity
annotated as enzyme activator activity. Fix: BP regulation unless direct binding is shown
([MF-17](#mf-17)).

**GTPase activity on GPCRs and G beta/gamma.** Fix: `REMOVE`; the receptor's MF is
receptor activity, and G beta/gamma hold G alpha in the GDP-bound state rather than
hydrolysing GTP ([FUNCTION_REQUIREMENT_RULES](../../FUNCTION_REQUIREMENT_RULES.md)).

**Transporter activity root.** `GO:0005215` is do-not-annotate. Fix: use the specific
transmembrane transporter, channel or carrier term the evidence supports.

**Oligomerisation as function.** `GO:0042802` identical protein binding or protein
dimerization activity used to record that a protein forms a dimer. Fix: capture the
complex in CC; keep an oligomerisation MF only when the oligomer is the functional
point, and expect these terms to become do-not-annotate ([MF-5](#mf-5)).

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [wiki: Annotating binding](https://wiki.geneontology.org/index.php/Annotating_binding) (2020 proposal) | "Annotation to these compounds is not discouraged" (substrate and cofactor binding) | Do not co-annotate substrate, product, cofactor or solute binding implied by an activity ([MF-4](#mf-4)) | The sentence contradicts its own heading and the older [Binding Guidelines](https://wiki.geneontology.org/index.php/Binding_Guidelines); we read it as a typo for "is discouraged" |
| [wiki: Binding Guidelines](https://wiki.geneontology.org/index.php/Binding_Guidelines); [wiki: IPI](https://wiki.geneontology.org/index.php/Inferred_from_Physical_Interaction_%28IPI%29) | Reciprocal GO:0005515 IPI annotations must be made | Do not create new bare GO:0005515 annotations at all; reciprocity is moot for new work ([MF-5](#mf-5)) | Protein binding records interaction, which MI databases curate; the 2026 IEA WG proposal would make it do-not-annotate |
| [Drive: protein binding announcement (go-ontology#11094)](https://drive.google.com/open?id=1CDLNsl-FgwqdsLP3jTfuA7h3nTdGq_ASEyYyLiTLhWE) | Convert identical protein binding and homodimerization rows to GO:0005515 with `has_input` | Do not convert into GO:0005515; refine to an informative MF or remove ([MF-5](#mf-5)) | Conversion moves the problem; the 2026 proposal treats both terms as equally uninformative |
| [Drive: oligomerization obsoletion proposal](https://drive.google.com/open?id=1JxzNwl1fr5Fj-IJy_Fo1lLfAlAQB8IxPDwwYKxIXBZo) | Assembled subunits may be given structural molecule activity, "protein binding, bridging" or protein binding | Structural or adaptor terms only with evidence for them; never GO:0005515 as a landing term | Same reason; "protein binding, bridging" is now `GO:0030674` and needs two partners |
| protein_binding_policy docstring vs [MOLECULAR_ADAPTOR_ACTIVITY](../../MOLECULAR_ADAPTOR_ACTIVITY.md) | The policy says REMOVE is the general case and MODIFY when the paper supports an informative MF; the project page says the policy "prefers MODIFY" | MODIFY when the row's paper supports the informative term; otherwise REMOVE ([MF-5](#mf-5)) | The two repo texts read the same policy differently; the validator accepts either action, so the evidence decides |
| [MOLECULAR_ADAPTOR_ACTIVITY](../../MOLECULAR_ADAPTOR_ACTIVITY.md) | Names `GO:0032947` as "protein-containing complex scaffold activity", the out-of-branch scaffold term | Use `GO:0140378` protein complex scaffold activity ([MF-8](#mf-8)) | GO:0032947 does not resolve in the GO release used here; GO:0140378 is the live structural scaffold term |
| [wiki: Annotating binding](https://wiki.geneontology.org/index.php/Annotating_binding) | Binding annotations use IPI | IPI when the partner can be identified; IDA when it cannot; never IPI for catalytic terms | Matches the IPI page; the binding page oversimplifies |
| [wiki: Guidelines for new Molecular Functions](https://wiki.geneontology.org/index.php/Guidelines_for_new_Molecular_Functions); term definition of `GO:0140416` | Regulators act "solely by non-covalent means"; but GO:0140416 transcription regulator inhibitor activity is defined "via direct binding and/or post-translational modification" | Treat covalent modification as a catalytic activity with `has_input` the target ([MF-17](#mf-17)) | The ontology is internally inconsistent; we follow the general MF principle and flag the term (Open questions) |
| [wiki: Annotation Conf. Call, January 14, 2014](https://wiki.geneontology.org/index.php/Annotation_Conf._Call,_January_14,_2014) | Proposed making enzyme regulator activity a child of enzyme binding; left open whether ortholog binding evidence suffices | Direct binding to the target is required; binding may come from a second experiment combined by IC, but binding shown only in an ortholog supports ISS at most | Keeps the regulator claim about the product itself |
| [go-annotation#5840](https://github.com/geneontology/go-annotation/issues/5840) | "It's in RHEA and EC - usually we've been keeping these" | Physiological relevance decides; presence in EC or Rhea does not ([MF-10](#mf-10)) | The same thread ended by moving the annotations up a level, and GO later obsoleted the term |
| GOC guidance (none) | No rule for weak or promiscuous measured activities | Three tiers: non-core, over-annotated, removed ([MF-11](#mf-11)) | Needed to treat noise-level activity of a paralog differently from a genuine side activity |
| GOC guidance (none) | No class rule for pseudoenzymes | Residue-plus-context check and action ladder ([MF-13](#mf-13)) | Pseudoenzymes are a predictable error source for every family-based pipeline |
| [wiki: Contributes to](https://wiki.geneontology.org/index.php/Contributes_to) | RNA polymerase example uses `GO:0001055` RNA polymerase II activity | Use a live term (`GO:0003899` DNA-directed RNA polymerase activity) | GO:0001055 is obsolete; the example needs updating |
| [wiki: Non-catalytic Molecular Functions](https://wiki.geneontology.org/index.php/Non-catalytic_Molecular_Functions) | Lists `GO:0140299` as "small molecule sensor activity" | The term is now labelled "molecular sensor activity" | Label drift; the page was last reviewed in 2022 |
| CLAUDE.md before the 2026-11-14 ruling | `TOO_GENERAL` usable for any general term with a specific term elsewhere, including `GO:0004930` | `TOO_GENERAL` only for terms imprecise on their own; `MODIFY` needs the row's own evidence ([MF-2](#mf-2)) | Two reviews read the enum in opposite ways; earlier reviews are not retroactively defective |

## Open questions

1. **Protein binding and oligomerisation terms.** Should GO adopt the 2026 IEA working
   group proposal to make `GO:0005515`, `GO:0042802` and the dimerization terms
   do-not-annotate, and archive the IntAct-derived rows in a MITAB file? This document
   assumes yes for new work but cannot retire existing rows.
2. **Holdase term.** `GO:0051082` unfolded protein binding is obsolete, and
   `GO:0140309` still requires escorting the client to an acceptor. In-situ holdases
   (CRYAA, CRYAB, HSPB6, CLU, DNAJB6, DNAJB8) need a general holdase chaperone term.
3. **Covalent regulators.** Should `GO:0140416` transcription regulator inhibitor
   activity (and similar terms) drop "and/or post-translational modification" from the
   definition, to match the regulator principle?
4. **Drug-named binding terms.** `GO:0005528` FK506 binding names an exogenous compound.
   Should such terms be reviewed under the 2020 drug-binding rules?
5. **Promiscuity tiers in the ontology.** The tiers of [MF-11](#mf-11) are a review
   convention. Should GO record graded relevance (for example, a qualifier for
   non-physiological activity), or keep relying on removal?
6. **Rhea residues of obsoletions.** Nine Rhea reactions now sit as narrow matches on
   EC grouping classes (for example Rhea:25968 on `GO:0016616`) and generate
   uninformative IEA rows. Who owns the clean-up, GO or the rhea2go pipeline?
7. **Adaptor with one input.** The GO-CAM guideline permits a single `has_input` on an
   adaptor activity while warning that it may be the wrong term. Should that be a
   hard requirement of two inputs?

## Sources

**GO wiki**

- [Guidelines for new Molecular Functions](https://wiki.geneontology.org/index.php/Guidelines_for_new_Molecular_Functions) (reviewed 2024)
- [Guidelines for catalytic activity terms](https://wiki.geneontology.org/index.php/Guidelines_for_catalytic_activity_terms)
- [Non-catalytic Molecular Functions](https://wiki.geneontology.org/index.php/Non-catalytic_Molecular_Functions) (reviewed 2022)
- [Annotating binding](https://wiki.geneontology.org/index.php/Annotating_binding) (2020 proposal, marked to be reviewed)
- [Binding Guidelines](https://wiki.geneontology.org/index.php/Binding_Guidelines) (2014, partly unresolved)
- [Guidelines for new Binding terms](https://wiki.geneontology.org/index.php/Guidelines_for_new_Binding_terms)
- [Enables](https://wiki.geneontology.org/index.php/Enables) (reviewed 2018)
- [Contributes to](https://wiki.geneontology.org/index.php/Contributes_to) (reviewed 2023, edited 2026)
- [Inferred from Physical Interaction (IPI)](https://wiki.geneontology.org/index.php/Inferred_from_Physical_Interaction_%28IPI%29) (reviewed 2018)
- [Proposal to obsolete children of "transcription factor binding"](https://wiki.geneontology.org/index.php/Proposal_to_obsolete_children_of_%22transcription_factor_binding%22)
- [Annotation Conf. Call, January 14, 2014](https://wiki.geneontology.org/index.php/Annotation_Conf._Call,_January_14,_2014)
- [Annotation Conf. Call 2019-11-19](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2019-11-19)
- [Annotation Conf. Call 2020-02-04](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2020-02-04)
- [Annotation Conf. Call 2021-08-03](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2021-08-03)

**GO Consortium Drive**

- [MF guidelines for GO-CAM (copy; reviewed 2026-03)](https://drive.google.com/open?id=1DWvc_g5yH4S8-Tc2rPtaAyPOIkYzITagK1sXysj0CY4)
- [IEA WG: protein binding do_not_annotate proposal (2026-05)](https://drive.google.com/open?id=1KKM7gxsPvQgszjppuyD_ZldM_T8cGV0ajSUIfLmyNQc) (pending)
- [Protein binding announcement, go-ontology#11094](https://drive.google.com/open?id=1CDLNsl-FgwqdsLP3jTfuA7h3nTdGq_ASEyYyLiTLhWE) (status unclear)
- [Protein oligomerization obsoletion proposal](https://drive.google.com/open?id=1JxzNwl1fr5Fj-IJy_Fo1lLfAlAQB8IxPDwwYKxIXBZo)
- [2017 GOC training talk: translating research data into GO annotations](https://drive.google.com/open?id=1m9v6KbdXs32ihzMjqGJYQpuK1Qf49Gh-)
- [Transporter activity annotation guidelines (archived)](https://drive.google.com/open?id=1h26nq-KExaYZKuBVKqJ2yWkK06dCWUQelZkTI262_PA)

**go-annotation issues**

- [go-annotation#1514](https://github.com/geneontology/go-annotation/issues/1514), [#1519](https://github.com/geneontology/go-annotation/issues/1519) (non-physiological gamma-glutamyltransferase)
- [go-annotation#1953](https://github.com/geneontology/go-annotation/issues/1953) (in vitro histone substrates)
- [go-annotation#2033](https://github.com/geneontology/go-annotation/issues/2033) (transporter specificity transfer)
- [go-annotation#2131](https://github.com/geneontology/go-annotation/issues/2131) (gorule-0000007, IPI and catalytic activity)
- [go-annotation#2311](https://github.com/geneontology/go-annotation/issues/2311) (transporter activity do-not-annotate)
- [go-annotation#2683](https://github.com/geneontology/go-annotation/issues/2683) (heterodimerization review)
- [go-annotation#3166](https://github.com/geneontology/go-annotation/issues/3166) (drug binding obsoletion)
- [go-annotation#3314](https://github.com/geneontology/go-annotation/issues/3314) (interspecies protein binding)
- [go-annotation#3510](https://github.com/geneontology/go-annotation/issues/3510) (non-catalytic transporter subunits)
- [go-annotation#5840](https://github.com/geneontology/go-annotation/issues/5840) (benzil reductase)

**Papers**

- [PMID:40703034](https://europepmc.org/article/MED/40703034) de Crécy-Lagard et al. 2025, assessment categories for function predictions

**Repository pages**

- [CLAUDE.md](../../../CLAUDE.md) (MODIFY/TOO_GENERAL ruling; protein binding; measured activity is not function; IBA reading)
- [protein_binding_policy.py](../../../src/ai_gene_review/validation/protein_binding_policy.py)
- [action consistency](../../../docs/action_consistency.md)
- [MOLECULAR_ADAPTOR_ACTIVITY](../../MOLECULAR_ADAPTOR_ACTIVITY.md) and its GRB2, LDLRAP1 and RPTOR worked examples
- [ENZYME_SPECIFICITY](../../ENZYME_SPECIFICITY.md)
- [NONPHYSIOLOGICAL_REACTIONS](../../NONPHYSIOLOGICAL_REACTIONS.md)
- [PSEUDOENZYMES](../../PSEUDOENZYMES.md)
- [FUNCTION_REQUIREMENT_RULES](../../FUNCTION_REQUIREMENT_RULES.md)
- [UNFOLDED_PROTEIN_BINDING](../../UNFOLDED_PROTEIN_BINDING.md)
- [LIGANDS_IN_SIGNALING](../../LIGANDS_IN_SIGNALING.md)
- [GPCR](../../GPCR.md)
- [TCDB](../../TCDB.md)
- [RHEA](../../RHEA.md)
- [TRANSCRIPTION_FACTORS](../../TRANSCRIPTION_FACTORS.md)
