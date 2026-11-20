---
id: MF
title: Molecular function
status: proposed
aspects:
- F
differences:
- prior_source: '[wiki: Contributes to](https://wiki.geneontology.org/index.php/Contributes_to)'
  prior_said: RNA polymerase example uses `GO:0001055` RNA polymerase II activity
  we_recommend: Use a live term (`GO:0003899` DNA-directed RNA polymerase activity)
  why: GO:0001055 is obsolete; the example needs updating
- prior_source: '[wiki: Non-catalytic Molecular Functions](https://wiki.geneontology.org/index.php/Non-catalytic_Molecular_Functions)'
  prior_said: Lists `GO:0140299` as "small molecule sensor activity"
  we_recommend: The term is now labelled "molecular sensor activity"
  why: Label drift; the page was last reviewed in 2022
date: '2026-11-15'
---

# Molecular function: GO annotation guidelines

Status: see each guideline · Part of [GO_GUIDELINES](../../../GO_GUIDELINES.md)

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
([protein-complexes.md](../protein-complexes.md)); signaling pathways and BP regulation
([regulation-and-signaling.md](../regulation-and-signaling.md)); transcription regulators
([transcription-regulation.md](../transcription-regulation.md)); evidence codes
([evidence-codes.md](../evidence-codes.md)); extension syntax
([annotation-extensions.md](../annotation-extensions.md)); NOT annotations
([qualifiers-and-negation.md](../qualifiers-and-negation.md)); IBA and electronic
pipelines ([phylogenetic-propagation.md](../phylogenetic-propagation.md),
[electronic-annotation.md](../electronic-annotation.md)).

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
([CLAUDE.md](../../../../CLAUDE.md), maintainer ruling of 2026-11-14).

## Rules

Each rule is its own record in this folder. Its frontmatter holds the metadata (status, provenance, differences from prior guidance, open questions, sources).

<!-- BEGIN GENERATED RULE INDEX -->

| Id | Guideline | Status | Provenance |
|---|---|---|---|
| [MF-1](MF-1.md) | Assert an MF only for an activity the gene product itself performs | proposed | [GOC] |
| [MF-2](MF-2.md) | Annotate at the depth this row's evidence supports, and refine only on that evidence | proposed | [GOC+] |
| [MF-3](MF-3.md) | Prefer an activity term to a binding term | proposed | [GOC] |
| [MF-4](MF-4.md) | Do not co-annotate binding that an activity term already implies | proposed | [GOC] |
| [MF-5](MF-5.md) | Treat bare `GO:0005515` protein binding as uninformative: never propose it, and in review replace or remove it | proposed | [NEW] |
| [MF-6](MF-6.md) | Use class-level binding children; name the specific partner in `has_input` | proposed | [GOC] |
| [MF-7](MF-7.md) | For small molecules, annotate the physiological ligand; never the drug or probe | proposed | [GOC] |
| [MF-8](MF-8.md) | Distinguish adaptor, scaffold, sequestering, carrier and regulator by what the binding does | proposed | [GOC+] |
| [MF-9](MF-9.md) | Support catalytic activity with evidence of catalysis, at the enzyme's natural specificity | proposed | [GOC] |
| [MF-10](MF-10.md) | Annotate the physiological reaction, not the assay substrate | proposed | [GOC+] |
| [MF-11](MF-11.md) | Measured activity is not automatically function: apply the three tiers | proposed | [NEW] |
| [MF-12](MF-12.md) | Check each axis of specificity before accepting a family-derived enzyme term | proposed | [NEW] |
| [MF-13](MF-13.md) | Do not annotate catalysis to a pseudoenzyme; annotate what it does instead | proposed | [NEW] |
| [MF-14](MF-14.md) | Give each subunit of a complex the activity it performs | proposed | [GOC] |
| [MF-15](MF-15.md) | Annotate transport as a specific transmembrane transporter or channel activity, on the physiological solute | proposed | [GOC+] |
| [MF-16](MF-16.md) | Annotate a receptor's signaling activity and a ligand's ligand activity, not reciprocal binding | proposed | [GOC] |
| [MF-17](MF-17.md) | Reserve regulator MFs for direct, non-covalent action on an identified target activity | proposed | [GOC+] |
| [MF-18](MF-18.md) | Treat an electronic MF as a claim about the family, and check it fits this member | proposed | [GOC+] |

<!-- END GENERATED RULE INDEX -->

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
| Assists folding | `GO:0044183` protein folding chaperone; carrier holdases `GO:0140309` | see [UNFOLDED_PROTEIN_BINDING](../../../UNFOLDED_PROTEIN_BINDING.md) |
| Binding of a defined class, role unknown | class-level binding child (e.g. `GO:0019901`) | `has_input` the specific partner |
| Binding of an unnamed protein class, role unknown | nothing new; in review `MODIFY` or `REMOVE` existing `GO:0005515` | partner in With/From |

### Reviewing a measured enzyme activity

1. Is the activity on the physiological substrate? If no, go to [MF-10](MF-10.md).
2. Is the protein catalytically competent (residues, motif, assay)? If no, go to
   [MF-13](MF-13.md).
3. Is the substrate, cofactor, mechanism and subunit right? If no, go to
   [MF-12](MF-12.md).
4. Is it the protein's evolved activity? Apply the tiers of [MF-11](MF-11.md).
5. Is the term as deep as this row's evidence, and no deeper? See [MF-2](MF-2.md).

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
informative term the same paper supports, else `REMOVE` ([MF-5](MF-5.md)).

**Adaptor activity from one IPI hit.** A single binary interaction becomes
`GO:0060090`. Fix: use a class-level binding term unless two bridged partners are
shown ([MF-8](MF-8.md)).

**Scaffold filed as adaptor, or adaptor as scaffold.** Fix: check the branch. Complex
scaffolds are structural molecule activity; condensate scaffolds and histone readers are
adaptor children.

**Implied binding stacked on an activity.** ATP binding, metal ion binding and heme
binding rows beside a kinase, metalloenzyme or P450. Fix: do not add them; in review,
mark them non-core or `TOO_GENERAL` rather than removing a true statement ([MF-4](MF-4.md)).
When the activity itself is wrong (a pseudoenzyme), remove the dependent rows with it
([MF-13](MF-13.md)).

**Assay substrate as function.** Histone kinase activity for a kinase tested on
histones; a chromogenic-substrate reductase; a rubidium flux. Fix: annotate the
physiological activity or the general activity the assay supports ([MF-10](MF-10.md)).

**Catalytic activity by IPI.** Fix: re-code to the assay that shows catalysis, or remove
(gorule-0000007).

**Family membership read as specificity.** Transaminase activity for a phospho-lyase
in the aminotransferase family; UDP-sugar transferase for a dTDP-sugar enzyme. Fix:
check the four axes of [MF-12](MF-12.md).

**Regulator MF from a knockdown.** A loss-of-function change in an enzyme's activity
annotated as enzyme activator activity. Fix: BP regulation unless direct binding is shown
([MF-17](MF-17.md)).

**GTPase activity on GPCRs and G beta/gamma.** Fix: `REMOVE`; the receptor's MF is
receptor activity, and G beta/gamma hold G alpha in the GDP-bound state rather than
hydrolysing GTP ([FUNCTION_REQUIREMENT_RULES](../../../FUNCTION_REQUIREMENT_RULES.md)).

**Transporter activity root.** `GO:0005215` is do-not-annotate. Fix: use the specific
transmembrane transporter, channel or carrier term the evidence supports.

**Oligomerisation as function.** `GO:0042802` identical protein binding or protein
dimerization activity used to record that a protein forms a dimer. Fix: capture the
complex in CC; keep an oligomerisation MF only when the oligomer is the functional
point, and expect these terms to become do-not-annotate ([MF-5](MF-5.md)).

## Reading list


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

- [CLAUDE.md](../../../../CLAUDE.md) (MODIFY/TOO_GENERAL ruling; protein binding; measured activity is not function; IBA reading)
- [protein_binding_policy.py](../../../../src/ai_gene_review/validation/protein_binding_policy.py)
- [action consistency](../../../../docs/action_consistency.md)
- [MOLECULAR_ADAPTOR_ACTIVITY](../../../MOLECULAR_ADAPTOR_ACTIVITY.md) and its GRB2, LDLRAP1 and RPTOR worked examples
- [ENZYME_SPECIFICITY](../../../ENZYME_SPECIFICITY.md)
- [NONPHYSIOLOGICAL_REACTIONS](../../../NONPHYSIOLOGICAL_REACTIONS.md)
- [PSEUDOENZYMES](../../../PSEUDOENZYMES.md)
- [FUNCTION_REQUIREMENT_RULES](../../../FUNCTION_REQUIREMENT_RULES.md)
- [UNFOLDED_PROTEIN_BINDING](../../../UNFOLDED_PROTEIN_BINDING.md)
- [LIGANDS_IN_SIGNALING](../../../LIGANDS_IN_SIGNALING.md)
- [GPCR](../../../GPCR.md)
- [TCDB](../../../TCDB.md)
- [RHEA](../../../RHEA.md)
- [TRANSCRIPTION_FACTORS](../../../TRANSCRIPTION_FACTORS.md)

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build-guidelines` -->

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [wiki: Contributes to](https://wiki.geneontology.org/index.php/Contributes_to) | RNA polymerase example uses `GO:0001055` RNA polymerase II activity | Use a live term (`GO:0003899` DNA-directed RNA polymerase activity) | GO:0001055 is obsolete; the example needs updating |
| [wiki: Non-catalytic Molecular Functions](https://wiki.geneontology.org/index.php/Non-catalytic_Molecular_Functions) | Lists `GO:0140299` as "small molecule sensor activity" | The term is now labelled "molecular sensor activity" | Label drift; the page was last reviewed in 2022 |

<!-- END GENERATED -->
