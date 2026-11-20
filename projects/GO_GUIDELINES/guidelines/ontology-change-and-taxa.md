# Ontology change and taxon scope: GO annotation guidelines

Status: draft v0.1 (2026-11-15) · Part of [GO_GUIDELINES](../../GO_GUIDELINES.md)

**In brief:**

- A GO term means its definition and its place in the graph, not its label. A relabel is not
  a redefinition; read the definition and parents before using, migrating or arguing about a term.
- `replaced_by` claims the two terms mean the same thing and is applied mechanically. Check
  that it stays in the right branch and fits your gene before accepting it. `consider` is
  advice; every annotation needs its own decision.
- An obsoletion does not repoint annotations, and a wrong annotation is not a reason to
  obsolete a term. Requests to the ontology and corrections to annotation records go to
  different places.
- Request a new term only when real evidence for a real gene needs it and no existing term,
  composition or GO-CAM pattern can carry it. Never request precomposed "X involved in Y",
  chemical-specific binding, assay or taxon-named terms.
- A missing term is an ontology gap, not a knowledge gap. Record it as a proposed term or a
  question, not as a biological unknown.
- Taxon constraints say where a term can apply. A non-experimental annotation that violates
  one is removed and its source fixed; an experimental one is examined, because the constraint
  may be too narrow.

## Scope

This document covers how curators live with a GO that changes under them: obsoletions and
how annotations should move, merges, relabelling and redefinition, proposals for new terms
and for obsoletion, the separation between ontology gaps and knowledge gaps, and the taxon
scope of terms (`only_in_taxon`, `never_in_taxon`, lineage-specific terms and pathways that
presuppose a component some lineages lack).

It is written for annotating curators and reviewers, not for ontology editors. The editor
procedures (Protégé deprecation, notification email, xref clean-up) are referenced where they
determine what a curator will see. How to review an annotation set generally is in
[reviewing-annotations.md](reviewing-annotations.md); how phylogenetic propagation places
and loses functions is in [phylogenetic-propagation.md](phylogenetic-propagation.md);
multi-organism terms and their taxon handling are in
[multi-organism-and-ncrna.md](multi-organism-and-ncrna.md).

## Principles

**An identifier is bound to a meaning.** GO keeps every identifier it has issued; removed
terms are deprecated, not deleted. A new meaning needs a new identifier even if the label
stays, and a reworded definition with the same meaning keeps its identifier
([wiki: Principles for term obsoletion](https://wiki.geneontology.org/index.php/Principles_for_term_obsoletion)).
Everything below follows from taking that seriously in both directions.

**Ontology change is cheap for editors and expensive for annotators.** One obsoletion can
touch thousands of rows, mostly electronic copies of a few seeds. The GOC's own policy asks
editors to be conservative for this reason
([wiki: Principles for term obsoletion](https://wiki.geneontology.org/index.php/Principles_for_term_obsoletion)).
The corresponding duty for curators is to migrate deliberately rather than accept every
automated redirect.

**Term state is a fact with a date.** Different GO services run different releases, and a
term can be live in one and obsolete in another on the same day. A claim that a term is
obsolete, merged or childless is only as good as the release and the service it was read from.

**Taxon constraints are evolutionary statements.** `only_in` says a feature arose on a branch;
`never_in` says it was lost on one. Treated that way, a constraint is a hypothesis that one
annotation can test, not an administrative block
([Drive: Taxon constraints 2021](https://drive.google.com/open?id=1Z3d8SBz-BWHPV5a9oaniPypZIYzV7VzBwVcleLdpk_c)).

## Rules

### Terms and their meaning

<a id="ont-1"></a>
### ONT-1. Read the definition and the parents, not the label

**Before annotating to a term, migrating to it, or arguing that it fits or does not, read its
current definition and its `is_a`/`part_of` parents. A label change does not change scope.**

GO relabels terms to match community usage or to fix a misleading name, and it records the
old label as a synonym. When a label and definition disagree, the GOC's 2024 ontology call
agreed to keep the community label, add a systematic synonym, and add a curator note not to
annotate to the label ([wiki: Ontology meeting 2024-01-22](https://wiki.geneontology.org/index.php/Ontology_meeting_2024-01-22)).
The definition governs.

*Example.* `GO:0140309` was relabelled "unfolded protein holdase activity". Its definition
still describes a protein carrier that binds an unfolded protein "and escorts it to an
acceptor molecule or to a specific location", and its parent is `GO:0140597` protein carrier
activity (both verified). It fits carrier-holdases such as the small TIMs, SecB and Skp. It
does not fit in-situ holdases such as the small heat shock proteins, which prevent
aggregation in place. Reading the new label as a general holdase term is the error this rule
exists to prevent, and it was made and caught in this repository
([UNFOLDED_PROTEIN_BINDING](../../UNFOLDED_PROTEIN_BINDING.md)).

*Example.* `GO:0102545` now carries the label "B-type glycerophospholipase activity"; older
pages cite it as "phospholipase B activity" ([OVER_ANNOTATION_PATTERNS](../../OVER_ANNOTATION_PATTERNS.md),
pattern 2). The definition, cleavage at both sn-1 and sn-2, is what to check against the
enzyme's data.

The GOC's Tips page makes the same point for parents: `DNA translocase activity` is a kind of
DNA-dependent ATPase, which the label does not reveal
([wiki: Tips to Produce High Quality Annotations](https://wiki.geneontology.org/index.php/Tips_to_Produce_High_Quality_Annotations)).

Provenance: [GOC].

<a id="ont-2"></a>
### ONT-2. Establish a term's state against a named release, from two independent services

**When obsoletion, merging or childlessness is load-bearing for a decision, check it in two
independent services (for example OLS or the GO API, and the release file or local build your
validation uses), and record the date and release you checked.**

Services disagree. QuickGO runs a snapshot ahead of the release PURL, and for a merged
identifier it can silently return the surviving term's record as "not obsolete", so a lookup
appears to confirm a term that has gone. Two endpoints of one service are one check. The
local build used for this document lists `GO:0061753` substrate localization to autophagosome
and `GO:0140355` cargo receptor ligand activity as live while GOA already treats the first
as obsolete and the second has an open obsoletion ticket
([action consistency](../../../docs/action_consistency.md),
[CARGO_RECEPTOR_LIGAND_ACTIVITY_OBSOLETION](../../CARGO_RECEPTOR_LIGAND_ACTIVITY_OBSOLETION.md)).
Two repository audits recorded terms as live after GO had retired them, both because the page
did not move when the ontology did ([ontology changes](../../../docs/ontology_changes.md)).

Attribute an obsoletion to the release that first carried it, and remember that negative
results from a lexical search are not evidence that no term exists: GO search is token-based,
so walk the branch before claiming a gap.

Provenance: [NEW].

### Obsoletions and merges

<a id="ont-3"></a>
### ONT-3. Treat `replaced_by` as a mechanical redirect that you must check

**`replaced_by` says the obsolete term and its target denote the same thing, and tools apply it
automatically. Accept it for your annotation only after checking that the target is in the
right branch for what the gene does. When it is not, record the correct term and flag the
`replaced_by` upstream.**

Noctua and Protein2GO update terms with a `replaced_by` automatically, and QuickGO and AmiGO
repair such annotations on load; `consider` targets need curator review
([wiki: Annotation Conf. Call 2023-04-18](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2023-04-18),
[Drive: Automated Ontology Term Updates in Noctua](https://drive.google.com/open?id=1QrKtMLMjBFoUaceh5UJX5IP_EtqMEx9igsqj_73DrFQ)).
GORULE:0000020 repairs GAF rows the same way. Only one `replaced_by` is allowed per term
([wiki: Obsoleting an Existing Ontology Term](https://wiki.geneontology.org/index.php/Obsoleting_an_Existing_Ontology_Term)),
so a term whose annotations fell into distinct classes cannot be served by one redirect.

*Example (redirect leaves the branch).* `GO:0070680` asparaginyl-tRNAAsn biosynthesis via
transamidation is obsolete with `replaced_by` `GO:0070981` L-asparagine biosynthetic process
(both verified in the local build). The GatCAB transamidase makes Asn-tRNA(Asn), not free
asparagine. The obsolete term's own definition begins "A tRNA aminoacylation process", and its
glutaminyl twin `GO:0070681` is a subclass of `GO:0043039` tRNA aminoacylation (both checked in
the local build). For GatCAB genes the right term is `GO:0043039`, not the redirect
([OVER_ANNOTATION_PATTERNS](../../OVER_ANNOTATION_PATTERNS.md), pattern 9).

*Example (redirect right for most rows, not all).* `GO:0036378` calcitriol biosynthetic
process from calciol is replaced by `GO:1901755` vitamin D3 biosynthetic process, which GO
redefined so that calcitriol is its primary output. That fits the 25-hydroxylases and the
1α-hydroxylase. It does not obviously fit CYP24A1, whose product is the 24-hydroxylated
inactivation metabolite; `GO:0042369` vitamin D catabolic process may be the right home
([CALCITRIOL_BIOSYNTHESIS_OBSOLETION](../../CALCITRIOL_BIOSYNTHESIS_OBSOLETION.md)).

When you accept a redirect, record the `replaced_by` line and the release in your provenance,
and check whether repointing to a parent changes subsumption elsewhere (a module or GO-CAM on
the parent term may now subsume a sibling).

Provenance: [GOC+]. The GOC documents what `replaced_by` does; checking it per annotation, and
flagging a wrong redirect upstream, is ours ([CLAUDE.md](../../../CLAUDE.md)).

<a id="ont-4"></a>
### ONT-4. Treat `consider` as a list of options and triage annotations by mechanism

**When an obsolete term has only `consider` targets, sort its annotations by what each gene
product actually does, and give each class its own destination. Some rows will have no
destination and should be removed.**

`consider` exists because no single term replaces the obsolete one
([wiki: Obsoleting an Existing Ontology Term](https://wiki.geneontology.org/index.php/Obsoleting_an_Existing_Ontology_Term)).
A term goes this way most often because it lumped different mechanisms.

*Example.* `GO:0008139` nuclear localization sequence binding was obsoleted as the same
activity as `GO:0140142` nucleocytoplasmic carrier activity. That is correct for importins
(KPNA2, KPNB1). It is wrong for a protein that binds an NLS in order to mask it (IκBα), and
for nucleoporins, whose annotations belong on `GO:0017056` structural constituent of nuclear
pore ([NLS_BINDING_OBSOLETION](../../NLS_BINDING_OBSOLETION.md)).

*Example.* `GO:0030943` mitochondrion targeting sequence binding was obsoleted "in favor of
more specific molecular functions". TOM20 and TOM22 move to `GO:0140436` mitochondrial
signal sequence receptor activity; the TOM40 channel moves to `GO:0008320` transmembrane
protein transporter activity; TIM22, a carrier-pathway channel whose substrates use internal
signals, may fit neither ([MITOCHONDRION_TARGETING_SEQUENCE_BINDING_OBSOLETION](../../MITOCHONDRION_TARGETING_SEQUENCE_BINDING_OBSOLETION.md)).

Upstream remapping tables are drafts too. The review of `GO:0061753` substrate localization to
autophagosome found two errors in the upstream table and one case (IRGQ) with no adequate
destination term ([SUBSTRATE_LOCALIZATION_TO_AUTOPHAGOSOME_OBSOLETION](../../SUBSTRATE_LOCALIZATION_TO_AUTOPHAGOSOME_OBSOLETION.md)).

Provenance: [GOC].

<a id="ont-5"></a>
### ONT-5. A replacement in another aspect is a `consider`, never a `replaced_by`

**When a biological process is obsoleted because it described a molecular function (or the
reverse), the new term must be offered as `consider`. An annotation cannot be repointed
mechanically across aspects, because the gene-product-to-term relation changes too.**

*Example.* GO obsoleted `GO:0099022` vesicle tethering and four children because tethering is
a binding activity, and minted `GO:7770062` vesicle membrane tethering activity. None of the
five carries a `replaced_by`; the MF is offered through `consider`, and each annotation needs
a curator to choose the transport process the activity is part of. `GO:0099023` vesicle
tethering complex is a cellular-component term and must not be used as the MF replacement
([VESICLE_TETHERING_OBSOLETION](../../VESICLE_TETHERING_OBSOLETION.md),
[ontology changes](../../../docs/ontology_changes.md)). The same shape recurs across the
docking, ER–plasma membrane and mitochondrion–ER tethering obsoletions.

A within-aspect redirect and cross-aspect advice can coexist on one term: GO's tRNA-charging
obsoletions give each amino-acid-specific BP a `replaced_by` to the compartment-level BP
(`GO:0006418` or `GO:0070127`) and name the 1:1 MF (`GO:0004813` alanine-tRNA ligase
activity for the alanine term) in the comment
([AMINO_ACID_ACTIVATION_OBSOLETION](../../AMINO_ACID_ACTIVATION_OBSOLETION.md)).

Provenance: [GOC+]. The GOC has no written rule. A May 2026 ontology developers' call found
none in the documentation, considered that a cross-aspect `replaced_by` could be acceptable in
principle, then concluded that `consider` is safer because automated replacement in GO-CAM
models would need a relation change that only a curator can make
([Drive: Ontology Developers call 2026-05-11](https://drive.google.com/open?id=1LgDHGlk1SEX5fZ0DugEfs_YLPlMxvWmV)).
We make that conclusion a rule.

<a id="ont-6"></a>
### ONT-6. When nothing replaces the term, put the content on what the gene does, or on its partner

**If an obsolete term has no replacement, do not search for the nearest live term. Ask what
the gene product actually does; annotate that if it is not already annotated; and if the
obsolete term described something done to the gene product, the content belongs on the
partner that does it.**

*Example.* `GO:0140355` cargo receptor ligand activity is being retired with no replacement,
because being recognized by a cargo receptor is something done to a protein. For
transcobalamin, the receptor CD320 carries `GO:0038024` cargo receptor activity with the
ligand as input, and the carrier keeps what it does: `GO:0031419` cobalamin binding and
`GO:0015889` cobalamin transport. Two rows should go regardless: a yeast ATG5 IDA and an
orphaned mouse ISO whose human source no longer exists
([CARGO_RECEPTOR_LIGAND_ACTIVITY_OBSOLETION](../../CARGO_RECEPTOR_LIGAND_ACTIVITY_OBSOLETION.md)).

*Example.* GO's 2016 decision on protein oligomerization terms set a class-wide rule: a gene
product that mediates assembly goes to complex assembly with the complex as output; an
assembled subunit gets the complex CC term or a structural or bridging MF; and the annotation
is removed if nothing fits ([Drive: Protein oligomerization obsoletion proposal](https://drive.google.com/open?id=1JxzNwl1fr5Fj-IJy_Fo1lLfAlAQB8IxPDwwYKxIXBZo),
[go-annotation#2521](https://github.com/geneontology/go-annotation/issues/2521)).

Provenance: [GOC+].

<a id="ont-7"></a>
### ONT-7. Migrate an obsolete term in a review with `MODIFY`, everywhere it occurs

**In a review, an existing annotation on an obsolete term is `MODIFY` with the replacement
(when the claim is sound and only the term is wrong), `REMOVE` (when the obsolete term was
the only thing making a wrong claim look right), or `UNDECIDED`. It is never `ACCEPT`. Move
the term out of core functions, modules and notes as well, and do not rewrite the GOA-sourced
term id itself.**

`ACCEPT` means the term is a core function, which contradicts its obsoletion; the
ontology-change checks flag an obsoletion request beside an `ACCEPT` on the same term
([ontology changes](../../../docs/ontology_changes.md)). GOA-sourced
`existing_annotations[].term.id` values are not hard-validated, precisely because GOA lags or
leads the ontology; changing them to satisfy validation destroys provenance. Author-supplied
ids (core functions, NEW rows, module terms) are strictly validated and must move
([CLAUDE.md](../../../CLAUDE.md)).

*Example.* After `GO:0030943` was obsoleted, human TOMM20's IBA and IDA rows moved from
`ACCEPT` to `MODIFY` with `GO:0140436` as replacement, and the core molecular function moved
with them ([MITOCHONDRION_TARGETING_SEQUENCE_BINDING_OBSOLETION](../../MITOCHONDRION_TARGETING_SEQUENCE_BINDING_OBSOLETION.md)).
A retired term's footprint usually reaches beyond the obvious file: gene reviews, modules,
evidence statements, project notes and cached enumerations. Search for the id across all of
them.

When a review decomposes a precomposed "X involved in Y" term, it says where Y went
(`decomposed_into`); see [biological-process.md](biological-process.md) and
[INVOLVED_IN_PRECOMPOSITION](../../INVOLVED_IN_PRECOMPOSITION.md).

Provenance: [NEW].

<a id="ont-8"></a>
### ONT-8. Merges are now obsoletions with `replaced_by`; read old secondary ids accordingly

**Treat a merged-away identifier as an obsolete term whose `replaced_by` is the survivor, and
apply [ONT-3](#ont-3) to it.**

Historically GO merged terms, turning the absorbed term's id into an `alt_id` of the survivor.
In 2023 the annotation call adopted a new procedure: no more merges, only obsoletion with
`replaced_by`, and a plan to convert every existing `alt_id` into an obsolete stanza pointing
to the active term, for consistency with OWL and other OBO ontologies
([wiki: Annotation Conf. Call 2023-04-18](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2023-04-18)).
Noctua had applied merges and `replaced_by` updates to models automatically since April 2022
([Drive: Automated Ontology Term Updates in Noctua](https://drive.google.com/open?id=1QrKtMLMjBFoUaceh5UJX5IP_EtqMEx9igsqj_73DrFQ)).

*Example.* `GO:0008785` alkyl hydroperoxide reductase activity fixed a substrate no known
enzyme is specific for, and was obsoleted with `replaced_by` `GO:0102039` NADH-dependent
peroxiredoxin activity, the new form of a merge
([ALKYL_HYDROPEROXIDE_REDUCTASE_OBSOLETION](../../ALKYL_HYDROPEROXIDE_REDUCTASE_OBSOLETION.md)).
The target names an electron donor; before accepting the redirect for a curated row, check that
the enzyme's characterized donor is NADH.

PAINT handles obsoletions in its monthly update: IBDs on obsoleted terms are obsoleted or
moved to the replacement, and an IBD is obsoleted when every experimental annotation at its
leaves is gone and restored when a new one appears
([Drive: PAINT Pipeline Update 2018](https://drive.google.com/open?id=1HqVWDk-B99U5DA5udeTJqnmbJstOVRI5aQTZ3H9alpo)).

Provenance: [GOC].

<a id="ont-9"></a>
### ONT-9. Fix a wrong annotation at its source; fix a wrong term in the ontology; do not confuse the two

**Incorrect annotations are not a reason to obsolete a term; report them to the group that
made them. A defective term is a reason to request an ontology change, and obsoleting it does
not repair the annotations that used it. A review that finds both records both, separately.**

GO's obsoletion principles say this directly: incorrect annotations should be reported to the
submitting database, and obsoletion is for terms whose meaning is broken
([wiki: Principles for term obsoletion](https://wiki.geneontology.org/index.php/Principles_for_term_obsoletion)).
In this repository, an annotation error is a `source_defects` entry addressed to the
`assigned_by` group or pipeline; a term error is a `proposed_ontology_changes` entry; a
missing term is a `proposed_new_terms` entry
([ontology changes](../../../docs/ontology_changes.md),
[REV-17](reviewing-annotations.md#rev-17)).

Likewise, a definition edit that does not make existing annotations wrong should not trigger
obsoletion; curators use the definition-change reports to refine their own annotations
([wiki: Manager 09Feb11](https://wiki.geneontology.org/index.php/Manager_09Feb11)).

*Example.* `GO:0003400` regulation of COPII vesicle coating was obsoleted because its
annotated genes (SAR1, SEC12, SEC23, SEC16) are parts of coat assembly, not regulators of it.
That was a term problem, and the annotations moved to `GO:0048208`, now labelled COPII vesicle
coat assembly. One human MAPK15 row in the same set was an annotation problem and is slated
for removal, which the obsoletion alone would not have achieved
([COPII_VESICLE_COATING_REGULATION_OBSOLETION](../../COPII_VESICLE_COATING_REGULATION_OBSOLETION.md)).

Provenance: [GOC].

<a id="ont-10"></a>
### ONT-10. Track upstream changes as inbound work, and argue disagreement in writing

**Distinguish a change you are asking the ontology to make from a change the ontology has made
or plans. For an upstream change, record whether you agree, when you last checked its state,
and whether your own content has been migrated. If you disagree, write the argument.**

The failure that actually happens is that the ontology moves and the curated content keeps
citing the retired term. This repository records each change with an `origin`
(`SELF_PROPOSED`, `UPSTREAM_PROPOSED`, `UPSTREAM_COMPLETED`), a `stance` for upstream changes
(`AGREE`, `DISAGREE`, `PARTIALLY_AGREE`, `NEEDS_CONFIRMATION`), the date the term's state was
last verified, and an adoption status for its own affected files. A check fires when a change
has landed and the affected content is still unmigrated
([ontology changes](../../../docs/ontology_changes.md)). A `DISAGREE` with fewer than twenty
words of argument is flagged: asserting disagreement is not raising it.

Provenance: [NEW].

### Requesting and proposing terms

<a id="ont-11"></a>
### ONT-11. Request a new term only when real evidence for a real gene needs it

**Request a term when (a) published evidence for a specific gene product would support an
annotation, (b) no existing term, extension, or GO-CAM pattern can express it, and (c) you can
write a definition with a genus and differentia that places it under a verified parent. A good
request carries all of these.**

A request should state:

| Element | Content |
|---|---|
| Label | Following GO naming conventions (MF labels end in "activity" or "binding") |
| Definition | Genus (the verified parent) plus what distinguishes it, with references; for enzymes, the reaction (Rhea or EC) |
| Parent(s) | Verified `is_a` and, where relevant, `part_of` |
| Gene products | At least one, with the papers that would support the annotation and the evidence code |
| Why existing terms fail | The candidates you checked, by id, and why each is wrong or too broad |
| Taxon scope | Whether the concept is lineage-restricted, and the constraint that follows |
| Annotations affected | What would move to the new term, if anything |

GOC guidance for ticket writers asks for "what is new, what is wrong, why and how to fix it",
with PMIDs ([go-annotation CONTRIBUTING](https://github.com/geneontology/go-annotation/blob/master/CONTRIBUTING.md)),
and the Tips page tells curators to open a go-ontology ticket when a term cannot be found
([wiki: Tips](https://wiki.geneontology.org/index.php/Tips_to_Produce_High_Quality_Annotations)).
New term requests remained a high priority for the ontology group in 2024
([wiki: Ontology meeting 2024-01-22](https://wiki.geneontology.org/index.php/Ontology_meeting_2024-01-22)).

*Example of a request that clears the bar.* The neural crest work proposes *neural plate
border formation* because `GO:0014029` neural crest formation is defined as forming a region
of ectoderm but placed under epithelial-to-mesenchymal transition, and border specifiers (Gbx2,
Msx1, Pax7) build the border without doing EMT. The proposal names the genes, the papers and
a 94-row per-annotation remapping table for GO. The same project considered terms for
regulation of delamination and regulation of crest migration and did not propose them, because
no annotation cleared the evidence bar ([NEURAL_CREST_FORMATION_OBSOLETION](../../NEURAL_CREST_FORMATION_OBSOLETION.md)).

Provenance: [GOC+]. The request contents and the evidence-first test are our sharpening.

<a id="ont-12"></a>
### ONT-12. Do not request terms that GO has decided not to have

**Do not request precomposed "X involved in Y" terms, chemical-specific binding terms,
regulation-of-molecular-function process terms, single-step processes that restate an MF,
terms named for an assay or a phenotype, terms named for a taxon, or substrate-specific
processes whose substrate is already carried by an MF.**

Each class has a current alternative:

| Don't request | Do instead | Basis |
|---|---|---|
| "X involved in Y" | Annotate X; carry Y in GO-CAM or (in GAF) a `part_of` extension | 1,265 such terms already obsoleted, 883 with a GO-CAM comment ([INVOLVED_IN_PRECOMPOSITION](../../INVOLVED_IN_PRECOMPOSITION.md)); scheduled for obsoletion ([Drive: GO rules 2024](https://drive.google.com/open?id=1CmnWtTKkx8Qo3e7XNEFfafZYTGTrJq7DcqRVBdB7lzM)) |
| "<chemical> binding" | `binding` with `has_input` the ChEBI entity | [wiki: Annotation Conf. Call 2020-02-04](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2020-02-04) |
| "regulation of <MF>" processes | The regulator's own MF (enzyme regulator, adaptor) and the regulated process | do-not-annotate and scheduled obsoletion ([Drive: GO rules 2024](https://drive.google.com/open?id=1CmnWtTKkx8Qo3e7XNEFfafZYTGTrJq7DcqRVBdB7lzM)) |
| Single-step processes ("protein methylation") | The MF that performs the step | as above |
| Assay or phenotype terms | The process the assay measures | GO obsoletion reasons list ([wiki: Obsoleting an Existing Ontology Term](https://wiki.geneontology.org/index.php/Obsoleting_an_Existing_Ontology_Term)) |
| Taxon-named subclasses | Subclasses distinguished by structure, composition or mechanism; a taxon constraint if needed | [wiki: Species-Specific Terms](https://wiki.geneontology.org/index.php/Species-Specific_Terms) |
| Substrate-specific BP restating an MF ("alanyl-tRNA aminoacylation") | The generic BP plus the specific MF | [AMINO_ACID_ACTIVATION_OBSOLETION](../../AMINO_ACID_ACTIVATION_OBSOLETION.md) |
| A ligand-named receptor activity with several unrelated receptors | The receptors' own activities with the ligand as input | `GO:0030369` ICAM-3 receptor activity obsoleted ([ICAM3_RECEPTOR_ACTIVITY_OBSOLETION](../../ICAM3_RECEPTOR_ACTIVITY_OBSOLETION.md)) |
| A pathway-variant term distinguished only by intermediates | The parent pathway term, with variants in GO-CAM | Entner–Doudoroff sub-pathways retired to `GO:0061678` ([ENTNER_DOUDOROFF_OBSOLETION](../../ENTNER_DOUDOROFF_OBSOLETION.md)) |

The test behind the last two rows is the one in [OVER_ANNOTATION_PATTERNS](../../OVER_ANNOTATION_PATTERNS.md)
pattern 9: ask what the specific term would assert that its parent and the gene's other
annotations do not. If the answer is a fact already carried in another aspect, the term adds
nothing. Specificity that no other aspect carries (compartment, for example) remains legitimate.

Provenance: [GOC+]. This departs from the older downstream-process guideline, which encouraged
requests such as "BMP signaling involved in cardiac cell differentiation"
([wiki: Annotating downstream processes](https://wiki.geneontology.org/index.php/Annotating_downstream_processes)).

<a id="ont-13"></a>
### ONT-13. In a review, propose a missing term with an NTR placeholder, never an ill-fitting id

**When a gene's core activity has no GO term, record a `proposed_new_terms` entry, point the
core function at it by name, and use `{id: NTR, label: ...}` as the replacement in any
`MODIFY`. Do not put an obsolete or nearly-right term id in a core function to fill the slot.**

A wrong id says something false in a machine-readable field; an NTR placeholder says "not yet
expressible". In this repository a core function with no fitting term sets
`proposed_molecular_function` to the `proposed_name` of a top-level `proposed_new_terms` entry
and leaves `molecular_function` unset; validation checks that the names match and that the
proposal has its own support ([CLAUDE.md](../../../CLAUDE.md)). When GO creates the term, swap
its id in and drop the proposal.

*Example.* `GO:0051082` unfolded protein binding is obsolete; its comment offers `GO:0044183`
protein folding chaperone (which requires assisting folding) or `GO:0140309` (carrier-specific,
[ONT-1](#ont-1)). Neither fits an in-situ holdase. Reviews of small heat shock proteins record
`MODIFY` with `{id: NTR, label: holdase chaperone activity}` and a matching proposal, pending a
GO term ([UNFOLDED_PROTEIN_BINDING](../../UNFOLDED_PROTEIN_BINDING.md)).

*Example.* Once GO minted `GO:7770062`, the TMF1 review moved its core MF from a stand-in term
to the new id and dropped its "vesicle tethering activity" proposal
([VESICLE_TETHERING_OBSOLETION](../../VESICLE_TETHERING_OBSOLETION.md)).

Provenance: [NEW].

<a id="ont-14"></a>
### ONT-14. An ontology gap is not a knowledge gap

**A missing or ill-fitting GO term is an ontology gap: record it as a proposed term, a proposed
ontology change, or a suggested question. A knowledge gap is something nobody knows that only a
new experiment could resolve. Do not file one as the other.**

The test is whether a wet-lab experiment would close the gap. "GO has no term for MHC-I
quality-control autophagy" is closed by an ontology editor; "which receptor delivers MHC-I to
the autophagosome" is closed by an experiment. In this repository a `knowledge_gaps` entry whose
only kind is `ONTOLOGY` or `CURATION` is not allowed; those kinds may appear only beside
`BIOLOGY`. The same separation applies to ND annotations: an ND that persists because no term
fits is `ONTOLOGY_BLOCKED`, not a true gap in knowledge ([CLAUDE.md](../../../CLAUDE.md),
[reviewing-annotations.md](reviewing-annotations.md#rev-12)).

Provenance: [NEW].

<a id="ont-15"></a>
### ONT-15. Propose an obsoletion only for a term whose meaning is broken, with a remapping for every curated row

**Request obsoletion when a term's definition and placement contradict each other, when its
usage is so inconsistent that it has no single meaning, or when it falls in a class GO has
ruled out of scope. Supply a destination for every experimental annotation, and say which rows
should simply go.**

GO's list of obsoletion reasons covers the main cases: unclear definition and inconsistent
usage, precomposed content better as GO-CAM, an assay, a phenotype, an MF stated as a process,
a gene product or protein class, equivalence to another term, and no evidence that the function
exists or is catalysed ([wiki: Obsoleting an Existing Ontology Term](https://wiki.geneontology.org/index.php/Obsoleting_an_Existing_Ontology_Term)).
Restoration of an obsolete term is possible when its original meaning survives
([wiki: Restoring an Obsolete Ontology Term](https://wiki.geneontology.org/index.php/Restoring_an_Obsolete_Ontology_Term)).

*Example.* `GO:0014029` neural crest formation has 1,454 annotations, 91% electronic and 665
from a single ARBA rule. The text defines forming a region of ectoderm while the graph places
it under EMT, so the annotations mix border specifiers, crest specifiers, competence factors
and ribosome-biogenesis genes. The proposal remaps the 84 experimental rows to precise existing
terms or one of two new terms (five rows remain undecided for want of full text), and names the ARBA rule to report to UniProt
([NEURAL_CREST_FORMATION_OBSOLETION](../../NEURAL_CREST_FORMATION_OBSOLETION.md)).

The structured form of such a request in this repository uses KGCL change types, with direct
replacements in `has_direct_replacement` and per-annotation advice in
`has_nondirect_replacement`; KGCL's controlled English has no statement for a non-direct
replacement or a merge, so those are carried in the structured slots
([ontology changes](../../../docs/ontology_changes.md)).

Provenance: [GOC+].

### Taxon scope

<a id="ont-16"></a>
### ONT-16. Know what a taxon constraint says and how it propagates

**`only_in_taxon T` means an annotation is valid only for organisms in T; `never_in_taxon T`
means it is valid everywhere except T. Constraints propagate from a term to its `is_a` and
`part_of` descendants and combine by intersection. They are not propagated over `regulates`.**

*Example.* `GO:0007595` lactation is `only_in` Mammalia; an InterPro2GO IEA that gave it to a
chicken protein was flagged invalid by exactly this reasoning
([wiki: GAF Taxonomy Reasoning](https://wiki.geneontology.org/index.php/GAF_Taxonomy_Reasoning)).
An immune-response term restricted to animals, fungi and plants and a T-cell term restricted to
vertebrates combine to vertebrates for a T-cell-mediated immune response
([Drive: Taxon constraints 2021](https://drive.google.com/open?id=1Z3d8SBz-BWHPV5a9oaniPypZIYzV7VzBwVcleLdpk_c)).

Constraints also arrive from imported ontologies: a term defined by reference to an Uberon or
CL class inherits that class's constraint. Before asking for a constraint, check whether it is
already entailed; editors do this with a DL query on `'in taxon' some T`
([wiki: Adding, Editing, Deleting Taxon Restrictions](https://wiki.geneontology.org/index.php/Adding%2C_Editing%2C_Deleting_Taxon_Restrictions)).
Because propagation stops at `regulates`, a regulation term needs its own constraint: the JAK-STAT
proposal requested one on `GO:0046425` separately from `GO:0007259` for that reason
([TAXON_PATHWAY_VARIANCE](../../TAXON_PATHWAY_VARIANCE.md)).

The 2021 proposal distinguishes global constraints (the term's evolutionary distribution) from
local ones added at a group's request, and recommends that curators propose a local test
together with the global constraint it implies
([Drive: Taxon constraints 2021](https://drive.google.com/open?id=1Z3d8SBz-BWHPV5a9oaniPypZIYzV7VzBwVcleLdpk_c)).

Provenance: [GOC].

<a id="ont-17"></a>
### ONT-17. When an annotation violates a constraint, decide which of the two is wrong

**A non-experimental annotation that violates a taxon constraint is removed, and the cause is
fixed at its source (the PAINT node, the InterPro2GO mapping, the orthology projection). An
experimental annotation that violates one is examined: if the organism really performs the
function, the constraint is too narrow and should be corrected; if not, the annotation is wrong
in its choice of term.**

GORULE:0000013 checks constraints. Non-experimental violations are filtered from GO products;
experimental violations are reported to the assigning group and left in place; NOT annotations
are exempt ([Drive: Taxon Constraints for Signaling Pathways](https://drive.google.com/open?id=117j8ysvt6FpVR0KCeFgrRDjUjm3jVXm8-nNReVU-hEg)).
Filtering hides the error from users without fixing the node or mapping that made it, so a
reviewer should still record the source defect.

*Constraint too narrow.* A re-examination of rare-in-lineage annotations found 38 that break an
existing constraint. Of the 21 terms involved, 14 were annotation errors and 5 constraints
looked too narrow: glutamate-gated calcium channel activity and plasma membrane repair are
restricted to Metazoa although plant GLR3.3 and SYT1 do these things; cholesterol binding is
`never_in` Fungi although CAP proteins bind sterols; sperm axoneme assembly is Metazoa-only
although *Selaginella* makes flagellate sperm ([RAR_MISANNOTATION](../../RAR_MISANNOTATION.md)).

*Annotation wrong.* Histone deacetylase activity on *B. subtilis* AcuC (`never_in` Bacteria)
and nuclear mRNA decapping on bacterial RppH proteins (`only_in` Eukaryota) arrived by IBA from
nodes placed too deep. TreeGrafter adds a further route: it grafts unreviewed proteins onto
PAINT nodes without a taxon check, so one node placed too deep becomes many IEA rows
([RAR_MISANNOTATION](../../RAR_MISANNOTATION.md)).

*A real case where both are partly right.* In 2023, 33 *C. elegans* annotations to
`GO:0007179` transforming growth factor beta receptor signaling pathway were flagged as
violations, although worms have TGF-beta superfamily ligands and receptors. The problem is a
pathway term named after one receptor subfamily in a family whose subfamilies do not map neatly
onto GO's terms ([Drive: Taxon Constraints for Signaling Pathways](https://drive.google.com/open?id=117j8ysvt6FpVR0KCeFgrRDjUjm3jVXm8-nNReVU-hEg)).
Such cases need an ontology fix, not a choice between deleting the worm rows and deleting the
constraint.

Provenance: [GOC+]. The filtering behaviour is GOC; requiring a reviewer to decide which side
is wrong is ours.

<a id="ont-18"></a>
### ONT-18. A pathway named for a component does not exist where the component is absent

**When a lineage runs a pathway without a component that a GO term presupposes, annotate its
genes to the generic sibling that does not presuppose it, and remove inherited rows to the
component-specific term.**

*Example.* *C. elegans* has two STATs and no JAK; *Dictyostelium* has four STATs and no animal
tyrosine kinases. Both inherit `GO:0007259` cell surface receptor signaling pathway via
JAK-STAT by IBA from a STAT family node at the unikont level, because the term was placed where
the STAT family arose while the pathway arose later with the JAK family. The *Dictyostelium*
statA and statC reviews `MODIFY` the row to `GO:0097696` cell surface receptor signaling pathway
via STAT, which presupposes no JAK; the worm rows are `REMOVE`. GO accepted `never_in`
Nematoda on `GO:0007259` and `GO:0046425`, and `only_in` Metazoa on `GO:0007259`, in November
2026 ([TAXON_PATHWAY_VARIANCE](../../TAXON_PATHWAY_VARIANCE.md)).

The constraint fixed the class at once, which is why a constraint on the term is often more
durable than an IRD on each node. Note the knock-on effect: `GO:0007260` tyrosine
phosphorylation of STAT protein now inherits the Metazoa constraint through `part_of`, because
GO applied the constraint without the re-parenting under `GO:0097696` that the proposal had
listed as a prerequisite; the term is already listed for obsoletion upstream.

The same reasoning covers lineage-specific structures: GO distinguishes `GO:0009274`
peptidoglycan-based cell wall, `GO:0009505` plant-type cell wall and `GO:0009277` fungal-type
cell wall under `GO:0005618` cell wall by composition, not by taxon, and the "sensu" style of
naming is deprecated ([wiki: Species-Specific Terms](https://wiki.geneontology.org/index.php/Species-Specific_Terms)).

Provenance: [GOC+].

<a id="ont-19"></a>
### ONT-19. Propose a taxon constraint only with evidence of absence and a measured payoff

**A constraint proposal must name a term that presupposes a component, cite evidence that the
component is absent from the lineage, confirm that GO does not already have the constraint
(directly or by inheritance), and list the annotations it would block and any it would block
wrongly.**

"Absence of evidence" is not enough: cite a primary source stating that the genome lacks the
component, or a reproducible bioinformatics check. A process the lineage merely does
differently does not qualify. Choose the taxon by the evolutionary event, at the highest
defensible rank; GO took the JAK-STAT constraint at Nematoda rather than the *Caenorhabditis*
fallback ([TAXON_PATHWAY_VARIANCE](../../TAXON_PATHWAY_VARIANCE.md),
[Drive: Taxon constraints 2021](https://drive.google.com/open?id=1Z3d8SBz-BWHPV5a9oaniPypZIYzV7VzBwVcleLdpk_c)).

*Example of a proposal with a measured payoff.* `GO:0005118` sevenless binding has no
constraint, while the sevenless signaling pathway is constrained to Arthropoda. 195
InterPro2GO IEAs from one signature carry it, 172 of them on vertebrate proteins (170 in the
GPRC5 family), none of which bind sevenless. The proposal pairs `only_in` Arthropoda with a
curated rule narrowing the mapping. Less certain proposals say so: `never_in` Aves for
cerebral cortex development is flagged as debated because avian pallium homology is contested
([TAXON_PATHWAY_VARIANCE](../../TAXON_PATHWAY_VARIANCE.md)).

Provenance: [NEW], consistent with the 2021 GOC proposal.

<a id="ont-20"></a>
### ONT-20. Do not annotate new rows to flagged terms, and read existing rows on them as review prompts

**Do not make new annotations to terms in `gocheck_do_not_annotate` or `obsoletion_candidate`.
Existing rows on such terms are not wrong by that fact; review them for a specific replacement.**

Since 2024 GO has one do-not-annotate subset, enforced as a warning (GORULE:0000008) in the GOC
pipeline and a filter in GOA's, with Noctua and PAINT blocking new use; its members are high
level or uninformative rather than wrong. The `obsoletion_candidate` subset warns curators at
least two months before a term goes
([wiki: Annotation Conf. Call 2024-03-12](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2024-03-12),
[Drive: GO rules 2024](https://drive.google.com/open?id=1CmnWtTKkx8Qo3e7XNEFfafZYTGTrJq7DcqRVBdB7lzM)).
Obsolete terms may remain in slims, but annotations to them should be filtered from products
([go-annotation#1452](https://github.com/geneontology/go-annotation/issues/1452)).

Provenance: [GOC].

## Decision aid

**An annotation sits on an obsolete term.**

| Situation | Action in a review | Upstream |
|---|---|---|
| `replaced_by` exists, target in the right branch, fits this gene | `MODIFY` to the target | none |
| `replaced_by` exists but leaves the branch or misfits this gene | `MODIFY` to the correct term | flag the redirect ([ONT-3](#ont-3)) |
| Only `consider` targets | Triage by mechanism; `MODIFY` per class ([ONT-4](#ont-4)) | report errors in the remapping table |
| Target is in another aspect | `MODIFY` with a curator-chosen MF/BP and relation ([ONT-5](#ont-5)) | none |
| No replacement; content is something done to the gene | `REMOVE`; check the partner carries it ([ONT-6](#ont-6)) | none |
| No term fits the real activity | `MODIFY` to `NTR`, add a proposal ([ONT-13](#ont-13)) | term request |
| The row was wrong before the obsoletion | `REMOVE` | source defect to the `assigned_by` group ([ONT-9](#ont-9)) |

**An annotation violates a taxon constraint.**

| Evidence | Does the organism plausibly have the function? | Action |
|---|---|---|
| IEA / IBA / ISS / ISO | No | `REMOVE`; source defect at node, mapping or projection |
| IEA / IBA / ISS / ISO | Yes, with evidence | Keep; propose correcting the constraint |
| Experimental | No | `REMOVE` (term choice is wrong); source defect to the curator |
| Experimental | Yes | Keep; propose correcting the constraint |
| Any | The term presupposes a missing component | `MODIFY` to the generic sibling ([ONT-18](#ont-18)) |

**Should I request a term?**

1. Is there gene-specific evidence that would support the annotation? If not, stop.
2. Did you walk the branch (parents, siblings, children), not just a text search? If not, do.
3. Can an existing term plus an extension, or a GO-CAM pattern, express it? If yes, use that.
4. Is it in a class in [ONT-12](#ont-12)? If yes, use the alternative.
5. Can you write genus-differentia with a verified parent? If yes, request it with the contents
   in [ONT-11](#ont-11).

## Common errors

| Error | Example | Fix |
|---|---|---|
| Reading scope from a new label | `GO:0140309` applied to crystallins after its relabel | Read the definition ([ONT-1](#ont-1)) |
| Trusting one service's obsolescence answer | Term written off as obsolete on a QuickGO lookup, later reversed | Two independent services, dated ([ONT-2](#ont-2)) |
| Accepting a mechanical redirect | Asn-tRNA transamidase moved to L-asparagine biosynthesis | Check branch and fit ([ONT-3](#ont-3)) |
| Blanket remap of a `consider` term | Every NLS-binding row moved to carrier activity, including masking proteins and nucleoporins | Triage by mechanism ([ONT-4](#ont-4)) |
| Using a CC as the MF replacement | `GO:0099023` vesicle tethering complex as the tethering MF | Use `GO:7770062` ([ONT-5](#ont-5)) |
| `ACCEPT` on an obsolete term | Core MF still on an obsoleted binding term | `MODIFY`; update core functions ([ONT-7](#ont-7)) |
| Rewriting a GOA term id to pass validation | Obsolete id in `existing_annotations` replaced in place | Keep the id; act in the review |
| Requesting a precomposed term | "BMP signaling involved in cardiac cell differentiation" | Annotate the parts; GO-CAM ([ONT-12](#ont-12)) |
| Ill-fitting id in a core function | Obsolete unfolded protein binding kept as the holdase core MF | NTR proposal ([ONT-13](#ont-13)) |
| Filing an ontology gap as a knowledge gap | "No GO term for X" as a biology gap | `proposed_new_terms` or a question ([ONT-14](#ont-14)) |
| Deleting experimental rows to satisfy a constraint | Plant GLR3.3 channel activity removed as "Metazoa only" | Check whether the constraint is too narrow ([ONT-17](#ont-17)) |
| Keeping a component-presupposing pathway | Worm STAT annotated to JAK-STAT signaling | Generic sibling or `REMOVE` ([ONT-18](#ont-18)) |
| Stale page status | Audit says terms are live after GO retired them | Record and re-check `ontology_state_verified` ([ONT-10](#ont-10)) |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [wiki: Obsoleting an Existing Ontology Term](https://wiki.geneontology.org/index.php/Obsoleting_an_Existing_Ontology_Term) | `replaced_by` when one term replaces the obsolete one; `consider` otherwise; no rule on aspect | Cross-aspect replacements are always `consider` | Automated replacement cannot change the relation; a May 2026 call reached this view but did not document it ([ONT-5](#ont-5)) |
| GOC tooling (Noctua, Protein2GO, GORULE:0000020) | Annotations to terms with `replaced_by` are updated automatically | Accept the redirect only after checking it per annotation; flag wrong redirects upstream | Redirects can leave the branch (`GO:0070680`) or misfit a subset (CYP24A1) ([ONT-3](#ont-3)) |
| [wiki: Annotation Conf. Call 2023-04-18](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2023-04-18) | Proposed that automated replacement makes per-annotation review unnecessary for `replaced_by` | Agree for the bulk of electronic rows; curated rows in a review still get a check | A one-term redirect cannot serve a term whose annotations fell into distinct classes |
| [wiki: Annotating downstream processes](https://wiki.geneontology.org/index.php/Annotating_downstream_processes) (flagged "to be reviewed") | Request "X involved in Y" terms to describe downstream involvement | Never request them; annotate X and model Y | GO has since obsoleted most such terms and lists the rest for obsoletion ([ONT-12](#ont-12)) |
| [wiki: Annotation Conf. Call 2020-02-04](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2020-02-04) | Use `binding` + `has_input` ChEBI instead of new chemical binding terms; criteria for binding terms left for future work | Same; existing chemical binding terms remain usable | The 2020 decision left the criteria open; we do not resolve them here |
| [VESICLE_TETHERING_OBSOLETION](../../VESICLE_TETHERING_OBSOLETION.md) (upstream recommendation relayed) vs [INVOLVED_IN_PRECOMPOSITION](../../INVOLVED_IN_PRECOMPOSITION.md) | GO recommends the new MF with a `part_of` extension to the transport BP; the repository's review schema dropped its extension slot because MF + `part_of(Y)` restates the retired class | In GAF/GPAD, follow GO and use the extension; in this repository's review records, carry Y by reference to a module, GO-CAM or core function | The two sources answer different questions (annotation format vs review record); flagged as an open question |
| [wiki: Principles for term obsoletion](https://wiki.geneontology.org/index.php/Principles_for_term_obsoletion) | Relabelling without a change of meaning keeps the id | Same, and treat a relabel as a prompt to re-read the definition, because labels can drift away from definitions | `GO:0140309`'s new label invites a use its definition excludes ([ONT-1](#ont-1)) |
| [Drive: Taxon Constraints for Signaling Pathways](https://drive.google.com/open?id=117j8ysvt6FpVR0KCeFgrRDjUjm3jVXm8-nNReVU-hEg) (GORULE:0000013) | Experimental violations reported, kept; non-experimental filtered | Filtering is not a fix: record the node or mapping defect; for experimental violations decide whether the constraint or the term choice is wrong | 5 of 21 violated constraints looked too narrow in one re-examination ([ONT-17](#ont-17)) |
| [wiki: GAF Taxonomy Reasoning](https://wiki.geneontology.org/index.php/GAF_Taxonomy_Reasoning) | Constraints do not propagate over `regulates` because inter-species regulation may be valid | Same; therefore request constraints on regulation terms explicitly when they are needed | The JAK-STAT request needed a separate constraint on the regulation term ([ONT-16](#ont-16)) |
| [Drive: Taxon constraints 2021](https://drive.google.com/open?id=1Z3d8SBz-BWHPV5a9oaniPypZIYzV7VzBwVcleLdpk_c) (proposal) | Constraints should be global evolutionary statements; curators propose local tests with a suggested global constraint | Adopt, and require evidence of absence plus a measured payoff | A proposal without counts cannot be weighed against what it would wrongly block ([ONT-19](#ont-19)) |
| [Drive: Changes to viral processes 2017](https://drive.google.com/open?id=1TO6RuYf8C1ANLVQp_mr1bkn_9I_CLtu18KIrPHHgVdE) vs the 2015 viral ontology paper | 2015: viral process terms are agnostic between host and virus; 2017: proposed constraints so viral processes are only viral and host processes only host | Not resolved here; see [multi-organism-and-ncrna.md](multi-organism-and-ncrna.md) | The sources conflict and the 2021 proposal allows only "only in Viruses" for viral-only terms |
| [wiki: Manager 09Feb11](https://wiki.geneontology.org/index.php/Manager_09Feb11) | Do not obsolete on definition edits that leave annotations correct; curators refine from reports | Same, and record when a definition change was checked (`ontology_state_verified`) | Undated statements about term state went stale twice in this repository ([ONT-10](#ont-10)) |
| This repository's earlier practice (`proposed_new_terms` with stand-in ids) | Core functions sometimes held an obsolete or nearly-right id while a term was missing | NTR placeholder with a named proposal; no stand-in ids | A wrong id is a false machine-readable claim ([ONT-13](#ont-13)) |

## Open questions

1. Should GO forbid cross-aspect `replaced_by` in its editor documentation and add a QC check,
   as the May 2026 call suggested might be needed?
2. Should every `replaced_by` be validated against the obsolete term's former parents (a
   redirect outside the old branch would be flagged for review)?
3. In GAF/GPAD, is an MF with a `part_of` BP extension the endorsed replacement for obsoleted
   tethering, docking and similar process terms, given GO's broader move to retire precomposed
   "X involved in Y" content? How should a review record that pattern?
4. GO has no general holdase chaperone term since `GO:0051082` was obsoleted. Should
   `GO:0140309` be redefined to match its label, or a new parent created?
5. Should taxon constraints on pathway terms named after one receptor subfamily (TGF-beta, JAK-STAT)
   be resolved by renaming and regrouping the terms, by constraints, or both?
6. Should TreeGrafter apply GO taxon constraints before grafting unreviewed proteins onto PAINT
   nodes?
7. When a constraint is applied without a prerequisite re-parenting (the `GO:0007260` case), who
   tracks the inherited conflict?
8. Should the GOC publish which release each service (QuickGO, AmiGO, OLS, the PURL) is serving,
   so that curators can cite term state reproducibly?

## Sources

**GO wiki**

- [wiki: Principles for term obsoletion](https://wiki.geneontology.org/index.php/Principles_for_term_obsoletion)
- [wiki: Obsoleting an Existing Ontology Term](https://wiki.geneontology.org/index.php/Obsoleting_an_Existing_Ontology_Term) (edited 2026-08)
- [wiki: Restoring an Obsolete Ontology Term](https://wiki.geneontology.org/index.php/Restoring_an_Obsolete_Ontology_Term) (last reviewed 2019)
- [wiki: Manager 09Feb11](https://wiki.geneontology.org/index.php/Manager_09Feb11)
- [wiki: Annotation Conf. Call 2023-04-18](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2023-04-18) (merge SOP)
- [wiki: Annotation Conf. Call 2024-03-12](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2024-03-12) (do-not-annotate, obsoletion_candidate)
- [wiki: Annotation Conf. Call 2020-02-04](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2020-02-04) (binding + has_input)
- [wiki: Ontology meeting 2024-01-22](https://wiki.geneontology.org/index.php/Ontology_meeting_2024-01-22)
- [wiki: Annotating downstream processes](https://wiki.geneontology.org/index.php/Annotating_downstream_processes) (flagged for review)
- [wiki: Tips to Produce High Quality Annotations](https://wiki.geneontology.org/index.php/Tips_to_Produce_High_Quality_Annotations)
- [wiki: Species-Specific Terms](https://wiki.geneontology.org/index.php/Species-Specific_Terms) (2018 copy of a website page)
- [wiki: Adding, Editing, Deleting Taxon Restrictions](https://wiki.geneontology.org/index.php/Adding%2C_Editing%2C_Deleting_Taxon_Restrictions) (reviewed 2026-10)
- [wiki: GAF Taxonomy Reasoning](https://wiki.geneontology.org/index.php/GAF_Taxonomy_Reasoning) (old implementation; rules still apply)

**GO Consortium Drive**

- [Drive: GOC 2021-05 / Taxon constraints](https://drive.google.com/open?id=1Z3d8SBz-BWHPV5a9oaniPypZIYzV7VzBwVcleLdpk_c) (proposal)
- [Drive: GOC 2023-04 / Taxon Constraints for Signaling Pathways](https://drive.google.com/open?id=117j8ysvt6FpVR0KCeFgrRDjUjm3jVXm8-nNReVU-hEg)
- [Drive: GOC 2017-06 / Changes to viral processes](https://drive.google.com/open?id=1TO6RuYf8C1ANLVQp_mr1bkn_9I_CLtu18KIrPHHgVdE)
- [Drive: Call Recordings / Ontology Developers 2026-05-11](https://drive.google.com/open?id=1LgDHGlk1SEX5fZ0DugEfs_YLPlMxvWmV) (unresolved discussion)
- [Drive: GOC 2022-04 / Automated Ontology Term Updates in Noctua](https://drive.google.com/open?id=1QrKtMLMjBFoUaceh5UJX5IP_EtqMEx9igsqj_73DrFQ)
- [Drive: GOC 2018-10 / PAINT Pipeline Update](https://drive.google.com/open?id=1HqVWDk-B99U5DA5udeTJqnmbJstOVRI5aQTZ3H9alpo)
- [Drive: GOC 2024-05 / GO rules](https://drive.google.com/open?id=1CmnWtTKkx8Qo3e7XNEFfafZYTGTrJq7DcqRVBdB7lzM)
- [Drive: Annotation Reviews / Protein oligomerization obsoletion proposal](https://drive.google.com/open?id=1JxzNwl1fr5Fj-IJy_Fo1lLfAlAQB8IxPDwwYKxIXBZo)

**GitHub issues and files (geneontology/go-annotation)**

- [go-annotation#1452](https://github.com/geneontology/go-annotation/issues/1452) (obsolete ids in slims)
- [go-annotation#2521](https://github.com/geneontology/go-annotation/issues/2521) (oligomerization out of scope)
- [go-annotation CONTRIBUTING](https://github.com/geneontology/go-annotation/blob/master/CONTRIBUTING.md)

**Repository pages**

- [CLAUDE.md](../../../CLAUDE.md) (term-id validation, proposed terms, knowledge gaps, precomposed terms)
- [ontology changes](../../../docs/ontology_changes.md)
- [action consistency](../../../docs/action_consistency.md)
- Obsoletion projects sampled: [VESICLE_TETHERING_OBSOLETION](../../VESICLE_TETHERING_OBSOLETION.md),
  [AMINO_ACID_ACTIVATION_OBSOLETION](../../AMINO_ACID_ACTIVATION_OBSOLETION.md),
  [NLS_BINDING_OBSOLETION](../../NLS_BINDING_OBSOLETION.md),
  [MITOCHONDRION_TARGETING_SEQUENCE_BINDING_OBSOLETION](../../MITOCHONDRION_TARGETING_SEQUENCE_BINDING_OBSOLETION.md),
  [CALCITRIOL_BIOSYNTHESIS_OBSOLETION](../../CALCITRIOL_BIOSYNTHESIS_OBSOLETION.md),
  [CARGO_RECEPTOR_LIGAND_ACTIVITY_OBSOLETION](../../CARGO_RECEPTOR_LIGAND_ACTIVITY_OBSOLETION.md),
  [COPII_VESICLE_COATING_REGULATION_OBSOLETION](../../COPII_VESICLE_COATING_REGULATION_OBSOLETION.md),
  [SUBSTRATE_LOCALIZATION_TO_AUTOPHAGOSOME_OBSOLETION](../../SUBSTRATE_LOCALIZATION_TO_AUTOPHAGOSOME_OBSOLETION.md),
  [NEURAL_CREST_FORMATION_OBSOLETION](../../NEURAL_CREST_FORMATION_OBSOLETION.md),
  [ALKYL_HYDROPEROXIDE_REDUCTASE_OBSOLETION](../../ALKYL_HYDROPEROXIDE_REDUCTASE_OBSOLETION.md),
  [ICAM3_RECEPTOR_ACTIVITY_OBSOLETION](../../ICAM3_RECEPTOR_ACTIVITY_OBSOLETION.md),
  [ENTNER_DOUDOROFF_OBSOLETION](../../ENTNER_DOUDOROFF_OBSOLETION.md)
- [INVOLVED_IN_PRECOMPOSITION](../../INVOLVED_IN_PRECOMPOSITION.md)
- [UNFOLDED_PROTEIN_BINDING](../../UNFOLDED_PROTEIN_BINDING.md)
- [OVER_ANNOTATION_PATTERNS](../../OVER_ANNOTATION_PATTERNS.md)
- [TAXON_PATHWAY_VARIANCE](../../TAXON_PATHWAY_VARIANCE.md)
- [RAR_MISANNOTATION](../../RAR_MISANNOTATION.md)
- [MODULE_TAXON_AUDIT](../../MODULE_TAXON_AUDIT.md) (taxonomic envelope criteria for modules)

GO term ids and labels were checked against the local `sqlite:obo:go` build (2026-11-03).
That build predates some changes described here: it still lists `GO:0140355` and
`GO:0061753` as live, and gives `GO:0046425` its pre-November 2026 label "regulation of
receptor signaling pathway via JAK-STAT" (GO has since inserted "cell surface"). Parentage
claims for `GO:0140309` and `GO:0070127` were checked with `runoak ancestors`.
