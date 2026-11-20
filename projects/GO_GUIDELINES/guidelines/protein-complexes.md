# Protein complexes: GO annotation guidelines

Status: draft v0.1 (2026-11-15) · Part of [GO_GUIDELINES](../../GO_GUIDELINES.md)

**In brief:**

- `part_of` a protein-containing complex needs evidence that the complex exists as a stable
  unit and that this gene product is in it: stringent co-purification, a structure of the
  assembled complex, or purification of a tagged subunit with the complex. A binary
  interaction is not membership.
- Membership is not function. The subunit that performs an activity `enables` it, even inside
  a complex. `contributes_to` is only for an irreducible molecular machine, and only for the
  subunits whose part is in the mechanism.
- Accessory, structural and regulatory subunits get their own molecular function (structural
  constituent, regulator, adaptor) or none. A subunit whose loss abolishes complex activity
  because the complex falls apart has shown necessity, not activity.
- Assembly factors get assembly processes and their own activity, never the mature complex's
  activity. Subunits are not annotated to the assembly of their own complex just because the
  complex fails to form without them.
- Oligomeric state is out of GO's scope. Homodimerization and oligomerization annotations
  record stoichiometry, not function, and are never core.

## Scope

This document covers how gene products are linked to protein-containing complexes in standard
GO annotation and review: complex membership (`part_of`), choice of complex term, binding to a
complex, molecular function of subunits (`enables` versus `contributes_to`), assembly factors,
homo- and hetero-oligomerization, Complex Portal-derived annotations, and how a review records
complex roles in `core_functions`. The modelling of complexes in GO-CAM is summarised in PC-14
and covered fully in [gocam-modeling.md](gocam-modeling.md). The gp2term relations in general
are in [qualifiers-and-negation.md](qualifiers-and-negation.md); binding terms in general in
[molecular-function.md](molecular-function.md); IPI and IDA in
[evidence-codes.md](evidence-codes.md).

## Principles

1. **A complex is a place; an activity belongs to whatever performs it.** GO models a
   complex as a cellular component. Saying a gene product is part of the pyruvate
   dehydrogenase complex (`GO:0045254`) does not say which chemistry it does
   ([wiki: Protein complexes](https://wiki.geneontology.org/index.php/Protein_complexes)).
2. **Users read an MF annotation as "this protein does this".** A list of gene products with
   "protein kinase activity" should not include regulatory subunits that cannot phosphorylate
   anything. The 2020 Complex Working Group made this the central argument: users querying by
   MF expect gene products that perform the activity, and had to consult other databases to
   find out which `contributes_to` subunits were catalytic
   ([Drive: GOC 2021-05 Contributes_to](https://drive.google.com/open?id=1g-2M8XQuINGN6eKVT0Sqm1OsudF_kM2D4jemv-izTks)).
3. **Necessity is not participation.** Knockout of almost any subunit destroys a complex's
   activity. That shows the subunit is needed, which is true of structural parts, assembly
   factors and the substrate alike. Ask which entity performs the step (see the participation
   test in [CLAUDE.md](../../../CLAUDE.md) "Do not add what curators deliberately declined to
   add").
4. **Keep the parts of a machine visible.** CC and BP annotations carry complex context to
   every member; MF annotations carry the division of labour. Flattening the second into the
   first teaches enrichment tools and ML models to predict membership rather than role
   ([PROTEIN_COMPLEX_FUNCTIONS](../../PROTEIN_COMPLEX_FUNCTIONS.md)).

## Rules

<a id="pc-1"></a>

### PC-1. Annotate `part_of` a complex only with evidence that the complex exists as a stable unit and that this gene product is an intrinsic member.

GO defines a protein-containing complex as a stable assembly of two or more macromolecules, at
least one a protein, whose parts function together. Its editors' page accepts stringent
purification followed by detection of the members, and lists as unacceptable on their own:
simple immunoprecipitation, pull-downs from cell extracts without further purification,
colocalization, two-hybrid screens, genetic interaction, and transient enzyme-substrate or
receptor-ligand pairs (unless the pair is needed to assemble a functional complex, as for
dimeric PDGF bridging two receptors)
([wiki: Protein complexes](https://wiki.geneontology.org/index.php/Protein_complexes)).

That page was written to decide which complexes deserve GO terms. We apply the same bar to
annotating a gene product to an existing complex term:

| Evidence | Supports `part_of` the complex? | Code |
|---|---|---|
| Purified complex (tandem affinity, gradient, gel filtration) with the protein identified as a member | yes | IDA |
| Cryo-EM or crystal structure of the assembled complex containing the protein | yes; but a structure of a partial complex does not define the full membership | IDA |
| Immunoprecipitation of a tagged subunit that recovers the defined complex | yes | IDA ([wiki: IDA](https://wiki.geneontology.org/index.php/Inferred_from_Direct_Assay_%28IDA%29)) |
| Binary interaction with one known member (Y2H, pull-down, co-IP from extract) | no; it supports a binding MF, at most `GO:0044877` protein-containing complex binding if the partner is the complex | IPI |
| Co-localization with complex members | no | |
| Homology to a member shown experimentally in another species, with orthology of the protein checked | yes | ISS/ISO/IBA |

*Example.* The BBSome review set replaced dozens of bare `protein binding` IPI rows with
membership of `GO:0034464` BBSome for the eight core subunits, whose membership rests on
purification and cryo-EM of the octamer; the chaperonin-like MKKS, BBS10 and BBS12 were not
given BBSome membership, because they assemble the complex rather than belong to it
([HUMAN_BBSOME](../../HUMAN_BBSOME.md)).

[GOC+] GOC states this bar for term creation; extending it to annotation is ours. The IPI and
IDA pages disagree on the code for complex isolation by co-IP (see Differences).

<a id="pc-2"></a>

### PC-2. Use the most specific complex term that the evidence supports; treat bare `GO:0032991` protein-containing complex as a placeholder to refine; record the organelle separately.

`GO:0032991` says only that the protein is in some complex. When the complex is known, a
`GO:0032991` row on the gene is `MODIFY` to the specific term. If GO has no term for a
physiological complex, request one rather than stopping at the root
([wiki: Protein complexes](https://wiki.geneontology.org/index.php/Protein_complexes), "How to
request").

Three properties of complex terms constrain the choice:

1. **Complex terms are classes, not instances.** GO does not make terms for a particular
   subunit composition in one species; those belong in Complex Portal or the Protein Ontology.
   Complexes differing only by cell type are out of scope.
2. **Subcomplexes and partial complexes are out of scope.** There is no GO term for the
   catalytic core of complex I or of complex IV
   ([Drive: Annotating activities of complexes and subcomplexes](https://drive.google.com/open?id=1TD0w8TNDbzgUoh7M3w3VgpOYYFjDGR55iSrctKMeq1s)).
   Named sectors that exist as terms (for example the ATP synthase F1 and Fo sectors, or
   `GO:0019773` proteasome core complex, alpha-subunit complex) may be used.
3. **Complex terms are species-agnostic and do not imply an organelle.** `GO:0045273`
   respiratory chain complex II (succinate dehydrogenase) has no `part_of` path to mitochondrion,
   because bacteria have it in the plasma membrane. A human SDHB review needs its mitochondrial
   inner membrane row in addition to its complex row; see
   [cellular-component.md](cellular-component.md).

The 2024 ontology meeting reaffirmed that complexes should not be split into cytoplasmic,
mitochondrial and plastid versions
([wiki: Ontology meeting 2024-01-29](https://wiki.geneontology.org/index.php/Ontology_meeting_2024-01-29)).

[GOC+] Point 3 and the MODIFY action are ours.

<a id="pc-3"></a>

### PC-3. A gene product that binds a complex without being part of it gets `GO:0044877` protein-containing complex binding or a specific child, not `part_of` or `located_in` the complex.

`part_of` is the only CC relation for complex terms; `located_in` and `is_active_in` are for
cellular anatomical entities
([wiki: Located in](https://wiki.geneontology.org/index.php/Located_in);
[Drive: Guidelines for P2GO](https://drive.google.com/open?id=1DXdjAuNf7u8CKXYlgW5kyzPgq7vnp-Aai0S5Sh63guc),
which names complex binding for non-members). New subclasses of `GO:0044877` must correspond to
a complex term
([wiki: Guidelines for new Binding terms](https://wiki.geneontology.org/index.php/Guidelines_for_new_Binding_terms)).

*Example.* A fission yeast translation elongation factor carried an IBA `part_of`
`GO:0022627` cytosolic small ribosomal subunit propagated from a budding-yeast source. The
2024 fix removed `part_of`; GO's view was that ribosome binding, not membership, describes a
factor that delivers tRNA to the ribosome
([go-annotation#5574](https://github.com/geneontology/go-annotation/issues/5574);
`GO:0043022` ribosome binding, or `GO:0043024` ribosomal small subunit binding). Keeping a
`located_in` row to the ribosomal subunit, as one curator proposed, uses a relation that the
P2GO table excludes for complex terms.

[GOC]

<a id="pc-4"></a>

### PC-4. Do not infer a molecular function from complex membership, co-purification or loss of complex activity on knockout.

A subunit can be required for a complex's activity without carrying it out. The
Contributes_to checklist asks: can the activity occur without this subunit; can the protein be
annotated to another MF; is the annotation still acceptable without the qualifier
([wiki: Contributes to](https://wiki.geneontology.org/index.php/Contributes_to)). A complex's
link to its MF through `capable_of` cannot be used to annotate subunits, because it does not
say which subunit is active
([wiki: Protein complexes](https://wiki.geneontology.org/index.php/Protein_complexes)).

Loss-of-function data distinguish poorly. Use the repo's attribution rubric
([PROTEIN_COMPLEX_FUNCTIONS](../../PROTEIN_COMPLEX_FUNCTIONS.md)):

| Evidence pattern | Handling |
|---|---|
| Purified subunit has the activity | `enables` on the subunit |
| Active site or cofactor centre lies in the subunit | `enables`, or `contributes_to` if it acts only in the complex (PC-6) |
| Activity requires a stable subcomplex | `contributes_to` for the subcomplex members only |
| Knockout lowers complex activity by destabilising assembly | assembly, stability or structural terms, not the activity |
| Subunit changes rate, specificity or inhibitor response | regulator terms (PC-7) |
| Only membership or co-purification | CC and BP only |

*Example of the error.* The repo's NDUFS4 review ACCEPTs an IMP `enables GO:0008137` NADH
dehydrogenase (ubiquinone) activity row and names `GO:0008137` as NDUFS4's core
`molecular_function`, while its own reason says NDUFS4 is a supernumerary subunit that "supports
the complex-level activity through assembly/stability rather than direct catalysis". Under
this rule the `enables` row is `MODIFY` (or `MARK_AS_OVER_ANNOTATED`), the core function
names complex I membership and assembly, and no `contributes_to` is given unless NDUFS4 is
shown to be in the electron-transfer mechanism.

[GOC+] GOC states the membership rule; the loss-of-function rubric is the repo's.

<a id="pc-5"></a>

### PC-5. The subunit that performs the activity `enables` it, with no qualifier, even when it works inside a complex; homomultimers also `enable`.

`enables` is used for a complex member when the activity is mediated by that gene product and
the other subunits are accessory
([wiki: Enables](https://wiki.geneontology.org/index.php/Enables)). The 2020 Complex Working
Group's "simple rule" is that MF is assigned to the subunit that performs it, and that the
catalytic subunit can be identified in most enzyme complexes: E3 ligases, HDAC and HAT
complexes, kinase complexes
([Drive: GOC 2021-05 Contributes_to](https://drive.google.com/open?id=1g-2M8XQuINGN6eKVT0Sqm1OsudF_kM2D4jemv-izTks);
[go-annotation#2664](https://github.com/geneontology/go-annotation/issues/2664)).

*Examples* (from the GO wiki unless noted):
- STT3 `enables` `GO:0004579` dolichyl-diphosphooligosaccharide-protein glycotransferase
  activity; it is the catalytic subunit of the oligosaccharyltransferase.
- PIGM `enables` `GO:0000030` mannosyltransferase activity; the accessory PIGX is required but
  has no activity, and gets no annotation to it.
- eIF2 gamma `enables` `GO:0003924` GTPase activity; alpha and beta do not.
- PSMB5, whose Thr60 is the active-site nucleophile, `enables` `GO:0004298` threonine-type
  endopeptidase activity; the alpha-ring subunit PSMA1 does not
  ([PROTEIN_COMPLEX_FUNCTIONS](../../PROTEIN_COMPLEX_FUNCTIONS.md), proteasome pilot).
- TOM40 `enables` `GO:0008320` transmembrane protein transporter activity as the channel; TOM22
  and TOM20 enable `GO:0140436` mitochondrial signal sequence receptor activity, not a
  `contributes_to` transporter row
  ([go-annotation#6466](https://github.com/geneontology/go-annotation/issues/6466)).

[GOC]

<a id="pc-6"></a>

### PC-6. Use `contributes_to` only when no single subunit has the activity and the activity is that of an irreducible molecular machine, and give it only to the subunits whose part is in the mechanism.

GO's definition: `contributes_to` links a gene product to an MF executed by a complex "in which
the Molecular Function cannot be ascribed to an individual subunit of that complex. Only the
complex subunits required for the Molecular Function are annotated"
([wiki: Annotation Relations](https://wiki.geneontology.org/index.php/Annotation_Relations)).
Being part of a complex is not sufficient
([wiki: Contributes to](https://wiki.geneontology.org/index.php/Contributes_to)). The cases:

| Case | Example | Who gets `contributes_to` |
|---|---|---|
| Composite active site built from residues of several subunits | ATP citrate lyase of *Chlorobaculum tepidum* (`GO:0003878`); ABC half-transporter heterodimers; thiocyanate hydrolase | every subunit contributing residues |
| Compound activity of the whole complex, a multi-step reaction no subunit performs | succinate dehydrogenase (quinone) activity `GO:0008177` for SDHA, SDHB, SDHC, SDHD ([go-annotation#6414](https://github.com/geneontology/go-annotation/issues/6414)) | each subunit in the reaction path |
| Coupled molecular machine | `GO:0046933` proton-transporting ATP synthase activity, rotational mechanism; `GO:0046961` proton-transporting ATPase activity, rotational mechanism for V-ATPase ([go-annotation#3616](https://github.com/geneontology/go-annotation/issues/3616)) | catalytic, rotor, stator and channel subunits (see PC-7 for others) |
| Polymerase catalytic core | nuclear RNA polymerases: the core subunits contribute to `GO:0003899` DNA-directed RNA polymerase activity; subunits outside the core do not | core only |
| Cofactor-dependent composite ATPase | torsins and their activators ([go-annotation#3865](https://github.com/geneontology/go-annotation/issues/3865)) | the ATPase may take `contributes_to`; the activator takes `GO:0001671` ATPase activator activity |

Ask the checklist question for each subunit separately. If the answer to "can the activity
occur without this subunit?" is yes, it does not contribute.

*Example.* SDHB, SDHC and SDHD reviews in the repo carry a structured `qualifier:
contributes_to` row on `GO:0008177`. Where GOA still ships `enables`, the review marks the GOA
row `MODIFY` and adds a paired `NEW` `contributes_to` row, the pattern the validator accepts
until GOA catches up ([SDH_GP2TERM_CONTRIBUTES_TO](../../SDH_GP2TERM_CONTRIBUTES_TO.md)).

A wiki example gives `contributes_to` on `GO:0001055` RNA polymerase II activity; that term is
now obsolete, so the example should be read with `GO:0003899`.

[GOC]

<a id="pc-7"></a>

### PC-7. Accessory, structural and regulatory subunits get their own MF or none; do not give them `contributes_to` the complex's catalytic activity.

The 2020 Complex Working Group: do not annotate subunits that do not participate in the MF with
`contributes_to`; adaptors, structural roles and regulatory roles have their own MF terms, and
a subunit can be left without an MF. Later tickets applied this to non-catalytic E3 subunits
(substrate adaptors such as F-box proteins take `GO:1990756` ubiquitin-like ligase-substrate
adaptor activity; [go-annotation#2760](https://github.com/geneontology/go-annotation/issues/2760)),
to non-catalytic transporter subunits (ATPase activator and adaptor terms;
[go-annotation#3510](https://github.com/geneontology/go-annotation/issues/3510)), and to
non-catalytic complex members generally (enzyme regulator or protein-RNA adaptor terms;
[go-annotation#3283](https://github.com/geneontology/go-annotation/issues/3283)).

| Subunit role | MF to consider | Example |
|---|---|---|
| Regulatory | `GO:0030234` enzyme regulator activity or a child, with `has_input` the catalytic subunit | PRKAG1 `GO:0019887` protein kinase regulator activity; PRKAA1 `enables` `GO:0004679` AMP-activated protein kinase activity |
| Activator of an ATPase | `GO:0001671` ATPase activator activity | torsin activators |
| Adaptor or bridge | `GO:0060090` molecular adaptor activity; `GO:0030674` protein-macromolecule adaptor activity; `GO:1990756` | F-box and DCAF substrate receptors |
| Structural | a "structural constituent of X" term | PSMA1 `GO:0140756` structural constituent of proteasome; ribosomal proteins `GO:0003735` |
| Unknown | no MF; CC and BP only | many OXPHOS supernumerary subunits |

**The ATP synthase and OXPHOS case.** The Contributes_to wiki says all components of ATP
synthase contribute to `GO:0046933`. The 2026 GO-CAM discussion of OXPHOS complexes I, III and
IV took a narrower view: catalytic-core subunits contribute to the activity, while
supernumerary subunits, which are eukaryote-specific with stabilising, regulatory or assembly
roles, do not
([Drive: Annotating activities of complexes and subcomplexes](https://drive.google.com/open?id=1TD0w8TNDbzgUoh7M3w3VgpOYYFjDGR55iSrctKMeq1s)).
We apply that narrower view to every coupled machine: a subunit `contributes_to` only if its
part is in the mechanism (a catalytic site, an electron-relay group, a substrate or quinone
site, the rotor, the stator or the proton channel). An inhibitor (ATP5IF1) gets regulator terms;
a supernumerary subunit of unknown role gets no MF.

*Examples of the error in the repo.* UQCRC1 is described in its own review as "a non-catalytic
structural core subunit" that "does not directly participate in the Q-cycle redox chemistry",
yet its core `molecular_function` is `GO:0008121` quinol-cytochrome-c reductase activity.
PSMA1's core function carries `contributes_to_molecular_function: GO:0004298`, although the
proteasome pilot concluded that threonine-type endopeptidase activity "should stay with PSMB5
and other catalytic beta subunits"; its `GO:0140756` structural MF is the right core. COX4I1,
a regulatory supernumerary subunit, has a TAS `enables GO:0004129` cytochrome-c oxidase activity
row ACCEPTed with a reason arguing for `contributes_to`. Each should be revised under this rule.

[GOC+] GOC states the principle; the "part in the mechanism" test for machines, and the
narrowing of the ATP synthase example, are ours.

<a id="pc-8"></a>

### PC-8. Annotate subunits to the complex-level activity, not to its substeps; a subunit that catalyses a half-reaction on its own may `enable` the parent term.

For complex II, GO's position in 2026 is that SdhA, SdhB, SdhC and SdhD each contribute to
`GO:0008177`, and the individual reactions (succinate oxidation, electron tunnelling, quinone
reduction) "should not be captured, as they correspond to substeps"
([go-annotation#6357](https://github.com/geneontology/go-annotation/issues/6357)). This keeps
subunits of one machine consistent and avoids inventing MF terms for partial reactions.

There is one principled exception. SDHA, the flavoprotein, can oxidise succinate with an
artificial acceptor in isolation. That is the parent `GO:0000104` succinate dehydrogenase
activity (succinate + acceptor = fumarate + reduced acceptor). `enables GO:0000104` on SDHA is
defensible because the subunit performs that activity on its own, which is the test for
`enables`. The repo treats this as unresolved
([SDH_GP2TERM_CONTRIBUTES_TO](../../SDH_GP2TERM_CONTRIBUTES_TO.md)); see Open questions.

`contributes_to` qualifies MF annotations only. A `contributes_to` on a CC or BP term is a data
error; one 2017 audit found such rows produced by inference pipelines
([go-annotation#1487](https://github.com/geneontology/go-annotation/issues/1487)).

[GOC+]

<a id="pc-9"></a>

### PC-9. When the active subunit of a complex is not known, give no subunit the complex's MF; use CC membership and BP.

"If a gene product is part of a complex and it is unknown which subunit is responsible for the
activity of the complex, do not annotate with a term from the Molecular Function branch"
([wiki: Contributes to](https://wiki.geneontology.org/index.php/Contributes_to)). In GO-CAM the
complex term is then the enabler with no parts listed, and no subunit MF is exported
([Drive: GOC 2025-05 GO-CAM guidelines](https://drive.google.com/open?id=1vF8JCnUM_JqkxgAvVHHl6ntyXpk3tY4y_NAjRjZ3WJE)).
Do not fill the gap with `GO:0005515` protein binding; the repo's protein-binding policy
removes bare protein binding as uninformative
([CLAUDE.md](../../../CLAUDE.md); `src/ai_gene_review/validation/protein_binding_policy.py`).
If the gap is a genuine biological unknown, record a `knowledge_gaps` entry with a
`suggested_experiments` partner.

[GOC]

<a id="pc-10"></a>

### PC-10. Assembly factors get assembly processes and their own activity; they are not `part_of` the mature complex and never receive its activity.

An assembly factor helps build, insert cofactors into, or quality-control a complex but is not
part of the mature active unit. Annotate it to the assembly process, preferably
`GO:0065003` protein-containing complex assembly or a specific child, with a `has_output`
extension naming the complex term, and to its own MF (a chaperone term such as
`GO:0044183` protein folding chaperone, a metallochaperone, a cofactor transferase). This
is the 2019 recommendation for chaperones of complexes
([Drive: Protein oligomerization obsoletion proposal](https://drive.google.com/open?id=1JxzNwl1fr5Fj-IJy_Fo1lLfAlAQB8IxPDwwYKxIXBZo)).

Membership of an assembly intermediate is a real location when GO has a term for it. Do not
annotate an assembly factor to the mature complex's MF unless there is direct evidence that it
stays in the active complex and takes part in the activity
([PROTEIN_COMPLEX_FUNCTIONS](../../PROTEIN_COMPLEX_FUNCTIONS.md), principle 5).

*Example.* SURF1's IEA `enables GO:0004129` cytochrome-c oxidase activity is `REMOVE`; its IBA
`GO:0033617` mitochondrial respiratory chain complex IV assembly is `ACCEPT`; and a `NEW` IPI row
places it in `GO:0062011` mitochondrial respiratory chain complex IV pre-assembly complex
([OXPHOS](../../OXPHOS.md)). The BBSome chaperonins MKKS, BBS10 and BBS12 have `GO:0044183`
as core MF and are not BBSome subunits ([HUMAN_BBSOME](../../HUMAN_BBSOME.md)).

[GOC+]

<a id="pc-11"></a>

### PC-11. Do not annotate a subunit to the assembly of its own complex because the complex fails to form without it; require evidence that it acts on the assembly of other parts.

Many complexes assemble spontaneously and cannot form without most of their subunits. That
makes each subunit necessary for assembly, not an agent of it. The 2018 exocyst case set the
pattern: Exo84 is required for other subunits to join, but it is a subunit, and its PAINT
assembly annotation was removed
([go-annotation#2149](https://github.com/geneontology/go-annotation/issues/2149)); a
placeholder ticket asked groups to look for IMP assembly annotations on complex members for the
same reason ([go-annotation#2213](https://github.com/geneontology/go-annotation/issues/2213)).

The 2020 TAF discussion went the other way for RNA polymerase II preinitiation complex
assembly, after the term definitions were revised to describe the ordered recruitment the
papers measured
([go-annotation#3002](https://github.com/geneontology/go-annotation/issues/3002)). We reconcile
the two by the participation test: a subunit may be annotated to assembly when it is shown to
recruit, nucleate or position other parts (a defined step in an ordered pathway, or an
activity that acts on other subunits), not when the evidence is only that the complex is
absent without it. Its knockout result belongs, at most, to `acts_upstream_of_or_within`
(see [biological-process.md](biological-process.md)).

[GOC+]

<a id="pc-12"></a>

### PC-12. Treat oligomeric state as out of scope: do not propose oligomerization or homodimerization terms, and review existing ones by their evidence.

In 2019 GO decided that "capturing the stoichiometry of protein interactions is not within the
scope of GO" and announced obsoletion of `GO:0051259` protein complex oligomerization and its
children, removal of the InterPro2GO mappings, and deletion of annotations based only on
crystallography
([go-annotation#2521](https://github.com/geneontology/go-annotation/issues/2521)). The guidance
document proposed merging `GO:0042803` protein homodimerization activity into `GO:0042802`
identical protein binding and heterodimerization into protein binding
([Drive: Protein oligomerization obsoletion proposal](https://drive.google.com/open?id=1JxzNwl1fr5Fj-IJy_Fo1lLfAlAQB8IxPDwwYKxIXBZo)).
In the GO release checked for this document, `GO:0051259`, `GO:0042803` and
`GO:0046982` protein heterodimerization activity are all still live. The scope decision stands
regardless.

Review actions for existing rows (adapted from the per-evidence-code review of
`GO:0042803`, [go-annotation#2682](https://github.com/geneontology/go-annotation/issues/2682)):

| Row | Action |
|---|---|
| Crystallography or stoichiometry only (oligomeric state in a structure, no binding experiment) | `REMOVE` |
| IC, TAS or NAS with no experimental self-association | `REMOVE` (check whether an experimental row exists) |
| IMP on a dimerization-defective mutant | keep only if a wild-type experimental row exists; otherwise `UNDECIDED` |
| IPI or IDA showing self-association, function not shown to depend on it | `KEEP_AS_NON_CORE` |
| Self-association shown to be the mechanism of a specific function (dimerization activates a kinase, forms a channel) | `MODIFY` to the specific MF; keep the binding row non-core |
| BP oligomerization row on a protein that mediates the assembly of others (a chaperone) | `MODIFY` to `GO:0065003` with `has_output` (PC-10) |
| BP oligomerization row on a protein that is itself assembled | `REMOVE`, or `MODIFY` to the complex CC term if a physiological complex term exists |

Never propose a `NEW` row on these terms, and never use them as core functions. A homomeric
complex may still be a CC term when it is a physiological functional unit (GO's in-scope
examples include homodimeric alcohol dehydrogenase;
[wiki: Protein complexes](https://wiki.geneontology.org/index.php/Protein_complexes)), and a
homomultimeric enzyme `enables` its activity without `contributes_to` (PC-5).

*Example.* PEX7's homodimerization row was contradicted by its own cited paper, which shows the
WD40 repeats bind the PTS2 signal ([PEROXISOME](../../PEROXISOME.md)). ASCL1's IEA identical
protein binding implies a homodimer for a factor that binds DNA as an obligate heterodimer with
E-proteins ([COSCIENTIST](../../COSCIENTIST.md)).

[GOC+] The scope decision is GOC; the action table and the "never core" rule are ours. In the
repo's reviews (count of 2026-11-15), `GO:0042802` rows are 921 `ACCEPT` and 899
`KEEP_AS_NON_CORE`, and `GO:0042803` rows 289 and 262, with 18 `NEW` `GO:0042803` rows: no
shared rule, and some reviews manufacturing the term this rule forbids.

<a id="pc-13"></a>

### PC-13. Review Complex Portal-derived subunit rows as claims about the subunit; never propagate the complex's MF to its subunits.

Complex Portal (CP) annotates complexes, and GOA copies each complex's BP and CC terms, but not
its MF, to every subunit under `assigned_by: ComplexPortal`, usually as NAS against the
complex's reference ([COMPLEXPORTAL](../../COMPLEXPORTAL.md)). In the repo's reviews 88% of
5,005 such rows survived (95% of CC, 83% of BP), and fewer than 1% were outright wrong. The
failures cluster:

| Pattern | Example | Review action |
|---|---|---|
| Regulation in the wrong direction (the inhibited subunit annotated as the inhibitor) | BAK1 `GO:0090201` negative regulation of release of cytochrome c from mitochondria; DFFB, CED-3 likewise | `REMOVE` or `MODIFY` to the correct sign |
| Downstream or neighbouring process | SDHB `GO:0042776` proton motive force-driven mitochondrial ATP synthesis (complex II pumps no protons) | `MARK_AS_OVER_ANNOTATED` |
| A partner's activity | MBL2 `GO:0006508` proteolysis (the MASPs cleave) | `REMOVE` |
| Promiscuous subunit inheriting every complex's terms | mouse Actb `GO:0000776` kinetochore, from chromatin remodellers containing actin | `MARK_AS_OVER_ANNOTATED` |
| Wrong location for a subunit | yeast CAC2 `GO:0000786` nucleosome (CAF-1 deposits histones, is not in the nucleosome) | `REMOVE` |
| Reference does not cover the subunit | DYNC2H1 male germ cell nucleus, from a dynein-1 paper | `UNDECIDED` or `REMOVE` per the reference rules |

Rows that another group also annotated from the same paper were almost never rejected (2 of
445), so independent corroboration is a useful triage signal.

GOA now also carries annotations with the CP complex itself (`ComplexPortal:CPX-*`) as subject.
This reverses the 2018 Protein Complex Working Group decision that CP identifiers should not be
annotation subjects ([go-annotation#2126](https://github.com/geneontology/go-annotation/issues/2126)).
Gene reviews here are fetched per UniProt accession and see only the subunit layer. Do not copy
an MF from the CPX record to a subunit.

[NEW] Sources: [COMPLEXPORTAL](../../COMPLEXPORTAL.md). The pipeline status (GOA roll-down rule,
the proposal to use IC with a GO_REF instead of the complex's PMID) is from GOA working-group
minutes summarised there and was not independently verified.

<a id="pc-14"></a>

### PC-14. In GO-CAM, use a complex as the enabler only for an emergent activity, list as `has_part` only the subunits that take part, and link subunits to complexes with `part_of`, never MF `occurs_in` a complex.

The 2025 consortium rules
([Drive: GOC 2025-05 GO-CAM guidelines](https://drive.google.com/open?id=1vF8JCnUM_JqkxgAvVHHl6ntyXpk3tY4y_NAjRjZ3WJE)):

1. Whenever possible, give each subunit its own MF and join them in a causal flow (pyruvate
   dehydrogenase); subunits whose MF is unknown may be left out. Exported as `enables`.
2. If several subunits are needed for the MF, the complex term is the enabler and the
   participating subunits are its `has_part`; exported as `contributes_to` for each part.
3. If the active subunit is not known, the complex term is the enabler with no parts; no MF is
   exported.

The Noctua export that turns every listed member into a `contributes_to` row is the main source
of wrong MF annotations on OXPHOS supernumerary subunits; FlyBase removed the complex-level MF
evidence from its OXPHOS models as a workaround. A 2026 proposal would add `has active member`
and `has accessory/structural member` relations so that only active members export MF
([Drive: Annotating activities of complexes and subcomplexes](https://drive.google.com/open?id=1TD0w8TNDbzgUoh7M3w3VgpOYYFjDGR55iSrctKMeq1s);
[Drive: GOC 2026-05 Protein-containing complexes in GO-CAMs](https://drive.google.com/open?id=1KKY3HIzPQJb6b39DiXkfExo9ngucY8uD9NlylwWh-jM)).
Until that exists, list as parts only the subunits that meet PC-6.

GO-CAM QC in 2026 found 92 models stating "MF occurs in protein-containing complex"; the
correct statement is "gene product part of complex"
([go-annotation#6310](https://github.com/geneontology/go-annotation/issues/6310)). The same
applies to standard annotation extensions.

[GOC] See [gocam-modeling.md](gocam-modeling.md).

<a id="pc-15"></a>

### PC-15. In a review's `core_functions`, state the attribution level: the subunit's own activity in `molecular_function`, the machine's activity in `contributes_to_molecular_function` only for direct participants.

The schema's `contributes_to_molecular_function` slot records a complex-level activity the
subunit does not enable alone, with a subunit-specific activity in `molecular_function`
(`src/ai_gene_review/schema/gene_review.yaml`, `CoreFunction`). Use it like this:

| Subunit class | `molecular_function` | `contributes_to_molecular_function` |
|---|---|---|
| Catalytic subunit that works alone | the activity | none |
| Member of an irreducible machine, part of the mechanism | its own part (electron transfer activity, quinone binding, proton channel), if a term exists | the machine's activity |
| Structural subunit | structural constituent term | none |
| Regulatory subunit | regulator term | none |
| Assembly factor | chaperone or other own activity | none |
| Unknown | none (use `locations`, `in_complex`, `directly_involved_in`) | none |

*Example.* PSEPK `sdhC` and `sdhD` put `GO:0008177` in `contributes_to_molecular_function`
only, with no GOA row to correct ([SDH_GP2TERM_CONTRIBUTES_TO](../../SDH_GP2TERM_CONTRIBUTES_TO.md)).

The schema's own description of the slot uses "an accessory subunit of Complex I
contributes_to NADH dehydrogenase activity" as its example. Under PC-7 that example is wrong
for accessory subunits outside the mechanism; the description should be revised (see Open
questions).

[NEW]

<a id="pc-16"></a>

### PC-16. Check propagated complex-activity rows (IBA, ISS, InterPro2GO) for transfer to non-catalytic subunits or paralogs.

PAINT propagates primary annotations as made, including their `contributes_to` qualifier
([go-annotation#5254](https://github.com/geneontology/go-annotation/issues/5254);
[go-annotation#3242](https://github.com/geneontology/go-annotation/issues/3242)). A seed with
the wrong qualifier, or a node that spans catalytic and non-catalytic paralogs, spreads the
error. In the INO80 case, Arp subunits received IBA `contributes_to` helicase activity; the
resolution was to annotate only the catalytic subunit and remove the propagations
([go-annotation#2374](https://github.com/geneontology/go-annotation/issues/2374)). Domain
signatures do the same for obligate heterodimers in which one partner lacks the active site
(PqsB of PqsBC; the actinorhodin chain-length factor, which has no active site;
[OVER_ANNOTATION_PATTERNS](../../OVER_ANNOTATION_PATTERNS.md) pattern 8). In prediction reviews,
this error is `COMPLEX_ACTIVITY_TRANSFER`; see
[phylogenetic-propagation.md](phylogenetic-propagation.md) and
[electronic-annotation.md](electronic-annotation.md).

*Example.* A *P. aeruginosa* Na+/H+ antiporter IBD was seeded by IMP `enables` rows on subunits
that were never mutated; the activity belongs to the complex and should have been
`contributes_to` ([IBA_REVIEW](../../IBA_REVIEW.md), PA1055/PA1057).

[GOC+]

## Decision aid

**Which MF annotation does this complex subunit get?**

1. Is the activity known to be performed by this subunit alone (purified activity, active site
   in this chain, homomultimer of this chain)? → `enables` the activity. Stop.
2. Is the activity that of the complex as a whole, with no single subunit able to perform it
   (composite active site, compound reaction, coupled machine)?
   - No, or unknown which subunit → no MF from the complex; CC `part_of` and BP only (PC-9).
   - Yes → go to 3.
3. Does this subunit's own part sit in the mechanism (catalytic residues, cofactor or relay
   group, substrate or quinone site, rotor, stator, channel)?
   - Yes → `contributes_to` the complex activity, plus its own MF if a term exists.
   - No → its own regulator, adaptor or structural MF, or none (PC-7).
4. Is it present only during assembly or maturation? → assembly BP and own MF (PC-10); no
   complex MF.

**Common hard calls**

| Situation | Call |
|---|---|
| Knockout abolishes complex activity, subunit is supernumerary | no MF from the complex; assembly or stability BP only if the subunit acts on assembly (PC-4, PC-11) |
| Regulatory subunit of a kinase or phosphatase | `GO:0019887` or other regulator term with `has_input` |
| Substrate receptor of a cullin-RING ligase | `GO:1990756`; not `contributes_to` ligase activity |
| Translation factor that binds the ribosome | `GO:0043022`; not `part_of` ribosome |
| Assembly chaperone in a pre-assembly complex | `part_of` the intermediate term if GO has one; assembly BP with `has_output` |
| Two-hybrid hit with one subunit | binding MF (not bare protein binding); not `part_of` |
| Crystal structure shows a tetramer | no oligomerization annotation |
| Complex term exists only for the whole machine, protein is in a core subcomplex | `part_of` the whole complex term |

## Common errors

| Pattern | Example | Fix |
|---|---|---|
| Accessory subunit `enables` the complex activity on knockout evidence | NDUFS4 IMP `enables GO:0008137`, core MF `GO:0008137` | PC-4: MODIFY; core function to membership and assembly |
| Structural subunit carries the complex activity as core | UQCRC1 core `GO:0008121`; PSMA1 `contributes_to GO:0004298` | PC-7: structural MF as core; no `contributes_to` |
| Regulatory subunit `enables` the activity | COX4I1 TAS `enables GO:0004129` ACCEPTed | PC-7: regulator term; MODIFY the row |
| Assembly factor annotated to the mature activity | SURF1 IEA `GO:0004129` | PC-10: REMOVE |
| Subunit annotated to assembly of its own complex | exocyst Exo84 IBA exocyst assembly | PC-11 |
| `contributes_to` for every subunit of a complex with an identifiable catalytic subunit | HDAC complexes, E3 ligases, kinase complexes (2020 audit) | PC-5, PC-7 |
| Non-member annotated `part_of` the complex | elongation factor `part_of` cytosolic small ribosomal subunit | PC-3: complex binding |
| `colocalizes_with` a complex term | about 1,600 rows across groups in 2018 | PC-3; see [CC-2](cellular-component.md#cc-2) |
| Homodimerization from crystallography | oligomeric state read from a structure | PC-12: REMOVE |
| Complex activity propagated to non-catalytic paralogs | INO80 Arp subunits `contributes_to` helicase activity | PC-16 |
| Bare `GO:0032991` when the complex is known | IEA protein-containing complex | PC-2: MODIFY to the specific term |
| Complex row taken to imply the organelle | complex II without a mitochondrion row | PC-2 point 3 |
| CP-derived BP with the regulation sign reversed | BAK1, DFFB, CED-3 | PC-13 |
| Structured qualifier missing where prose argues `contributes_to` | SDHB, SDHD before PR #3223 | PC-6: MODIFY plus paired NEW `contributes_to` row |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [wiki: Contributes to](https://wiki.geneontology.org/index.php/Contributes_to) (reviewed 2023) | All components of ATP synthase are annotated `contributes_to GO:0046933` | `contributes_to` only for subunits whose part is in the mechanism; inhibitors and supernumerary subunits of unknown role get none (PC-7) | Consistent with the wiki's own "only the subunits required" sentence and with the 2026 OXPHOS GO-CAM discussion |
| [Drive: Annotating activities of complexes and subcomplexes](https://drive.google.com/open?id=1TD0w8TNDbzgUoh7M3w3VgpOYYFjDGR55iSrctKMeq1s) (2026, discussion) | Open options: status quo, export no MF, or new active/accessory member relations | Adopt the active-member intent now in curation: list as parts only subunits meeting PC-6 (PC-14) | Avoids waiting for RO relations while preventing wrong exports |
| `gene_review.yaml` `contributes_to_molecular_function` description | "an accessory subunit of Complex I contributes_to NADH dehydrogenase activity" | Accessory subunits outside the mechanism get no `contributes_to` (PC-15) | Contradicts GOC's "being part of a complex is not sufficient" and the repo's own PROTEIN_COMPLEX_FUNCTIONS principle 3 |
| [OXPHOS](../../OXPHOS.md) bottom line | "non-catalytic subunits only contribute" | Only non-catalytic subunits in the mechanism contribute; others get own MF or none | The OXPHOS phrasing reads as licensing `contributes_to` for every subunit, which is how NDUFS4 and COX4I1 rows were accepted |
| [wiki: Protein complexes](https://wiki.geneontology.org/index.php/Protein_complexes) | Evidence bar (no simple IP, pull-down, colocalization or two-hybrid) stated for creating complex terms | Same bar for annotating `part_of` (PC-1) | A term-creation bar that does not apply to annotation lets binary hits become membership |
| [wiki: IPI](https://wiki.geneontology.org/index.php/Inferred_from_Physical_Interaction_%28IPI%29) vs [wiki: IDA](https://wiki.geneontology.org/index.php/Inferred_from_Direct_Assay_%28IDA%29) | IPI page: complex annotations from co-IP or pull-down may use IPI with the bait in WITH; IDA page: tagged-subunit isolation of a complex is IDA, not IPI | IDA for isolation of the defined complex; IPI only for a binary interaction, which does not support `part_of` (PC-1) | The two pages conflict; IDA matches what the assay shows |
| [go-annotation#2126](https://github.com/geneontology/go-annotation/issues/2126) (2018) | CP identifiers should not be annotation subjects | GOA now carries CPX-subject annotations; reviews treat them as complex-level and never transfer their MF (PC-13) | Practice changed after 2018 ([COMPLEXPORTAL](../../COMPLEXPORTAL.md)); the 2020 contributes_to deck already allowed annotating the CP accession "in parallel" |
| [wiki: Contributes to](https://wiki.geneontology.org/index.php/Contributes_to) eIF2 example; [2020 Contributes_to deck](https://drive.google.com/open?id=1g-2M8XQuINGN6eKVT0Sqm1OsudF_kM2D4jemv-izTks) | Add an `occurs_in` extension naming the complex term to subunit MF annotations | Link subunits to complexes with `part_of` only; no MF `occurs_in` complex (PC-14) | [go-annotation#6310](https://github.com/geneontology/go-annotation/issues/6310) (2026) calls MF `occurs_in` complex incorrect in GO-CAM; the same logic applies to extensions |
| [go-annotation#2149](https://github.com/geneontology/go-annotation/issues/2149), [#2213](https://github.com/geneontology/go-annotation/issues/2213) vs [#3002](https://github.com/geneontology/go-annotation/issues/3002) | Subunits should not get assembly of their own complex; but TAF annotations to PIC assembly were kept after definition changes | Assembly BP for a subunit only with evidence that it acts on assembly of other parts (PC-11) | Reconciles the two by the participation test |
| [Drive: Protein oligomerization obsoletion proposal](https://drive.google.com/open?id=1JxzNwl1fr5Fj-IJy_Fo1lLfAlAQB8IxPDwwYKxIXBZo); [#2521](https://github.com/geneontology/go-annotation/issues/2521) | Obsolete oligomerization BP terms; merge homodimerization into identical protein binding | Terms are still live; apply the scope decision in review by evidence, never core, never NEW (PC-12) | The ontology change appears unfinished; the scope rule is what matters for review |
| Same proposal, assembled subunits | Assembled subunits may be re-annotated to `GO:0005515` protein binding or `GO:0030674` | Not bare protein binding; a specific MF or nothing (PC-9, PC-12) | Repo protein-binding policy removes bare `GO:0005515` |
| [Drive: Protein-binding announcement](https://drive.google.com/open?id=1CDLNsl-FgwqdsLP3jTfuA7h3nTdGq_ASEyYyLiTLhWE) (go-ontology#11094, status unclear) | Convert identical protein binding and homodimerization to protein binding + `has_input` the same protein | Not adopted; review per PC-12 | Status of the decision is unclear and the target term is the one the repo removes |
| [wiki: Contributes to](https://wiki.geneontology.org/index.php/Contributes_to) | Examples use `GO:0001055` RNA polymerase II activity and (in the editors' page) `GO:0004738` pyruvate dehydrogenase activity | Read with live terms (`GO:0003899`); the examples need updating | Both terms are obsolete in the current release |
| [SDH_GP2TERM_CONTRIBUTES_TO](../../SDH_GP2TERM_CONTRIBUTES_TO.md) vs [#6357](https://github.com/geneontology/go-annotation/issues/6357) | Repo: SDHA `enables GO:0000104` defensible; GO: all four subunits contribute and substeps are not captured | Complex activity for all; `enables` on a half-reaction parent only when the subunit performs it alone, pending GO decision (PC-8) | GO's answer addresses `GO:0008177`; it does not say whether an independently measurable parent activity counts as a substep |

## Open questions

1. **SDHA and `GO:0000104`.** Is the flavoprotein's isolated succinate oxidation (artificial
   acceptor) an activity of SDHA, to be annotated with `enables` the parent term, or a
   substep excluded by the complex II decision? The answer generalises to any subunit with a
   measurable partial reaction.
2. **Active-member relations.** Will RO add `has active member` and `has accessory/structural
   member` so that GO-CAM exports MF only for active members? Until then, curators carry the
   distinction by hand.
3. **Multi-activity complexes.** The ribosome and proteasome have several activities with
   different active members (peptidyl transferase by rRNA; protease by beta subunits;
   structural roles for others). A per-activity member list is needed; GO has no convention.
4. **Supernumerary subunits with no term.** Many OXPHOS supernumerary subunits have no MF at
   all. Is "structural constituent of respiratory chain complex" (by analogy with
   `GO:0003735` and `GO:0140756`) wanted?
5. **Unfinished obsoletions.** `GO:0051259`, `GO:0042803` and `GO:0046982` were slated for
   obsoletion or merger in 2019 and are still live. GOC should finish or withdraw.
6. **Complex Portal evidence.** Should CP-derived subunit rows use IC with a GO_REF (as the IEA
   working group proposed) rather than NAS against a paper that may not mention the subunit?
7. **Schema text.** The `contributes_to_molecular_function` description in
   `gene_review.yaml` gives an accessory-subunit example that PC-7 rejects; revising it is a
   schema change for the maintainers.
8. **Heteromeric channels of one family.** The 2020 deck asked whether `contributes_to` on
   heteromeric ion channel subunits says anything that `enables` on each subunit does not. No
   decision was recorded.

## Sources

**GO wiki**
- [Protein complexes](https://wiki.geneontology.org/index.php/Protein_complexes) (editors' page, reviewed 2023)
- [Contributes to](https://wiki.geneontology.org/index.php/Contributes_to) (reviewed 2023)
- [Enables](https://wiki.geneontology.org/index.php/Enables)
- [Annotation Relations](https://wiki.geneontology.org/index.php/Annotation_Relations)
- [Part of relation](https://wiki.geneontology.org/index.php/Part_of_relation); [Located in](https://wiki.geneontology.org/index.php/Located_in)
- [Guidelines for new Binding terms](https://wiki.geneontology.org/index.php/Guidelines_for_new_Binding_terms)
- [Inferred from Direct Assay (IDA)](https://wiki.geneontology.org/index.php/Inferred_from_Direct_Assay_%28IDA%29); [Inferred from Physical Interaction (IPI)](https://wiki.geneontology.org/index.php/Inferred_from_Physical_Interaction_%28IPI%29)
- [Ontology meeting 2024-01-29](https://wiki.geneontology.org/index.php/Ontology_meeting_2024-01-29)

**GO Drive (GOC-internal)**
- [Drive: GOC 2021-05/Contributes_to](https://drive.google.com/open?id=1g-2M8XQuINGN6eKVT0Sqm1OsudF_kM2D4jemv-izTks) (Complex Working Group, 2020)
- [Drive: GOC 2025-05/GO-CAM guidelines for protein-containing complexes](https://drive.google.com/open?id=1vF8JCnUM_JqkxgAvVHHl6ntyXpk3tY4y_NAjRjZ3WJE)
- [Drive: Protein Complexes/Annotating activities of complexes and subcomplexes](https://drive.google.com/open?id=1TD0w8TNDbzgUoh7M3w3VgpOYYFjDGR55iSrctKMeq1s) (GO-CAM call, 2026-01-27; discussion)
- [Drive: Annotation Reviews/Protein oligomerization obsoletion proposal](https://drive.google.com/open?id=1JxzNwl1fr5Fj-IJy_Fo1lLfAlAQB8IxPDwwYKxIXBZo) (2019)
- [Drive: Ontology/Protein-binding announcement](https://drive.google.com/open?id=1CDLNsl-FgwqdsLP3jTfuA7h3nTdGq_ASEyYyLiTLhWE) (draft, status unclear)
- [Drive: Annotation guidelines/Annotation relations - Guidelines for P2GO](https://drive.google.com/open?id=1DXdjAuNf7u8CKXYlgW5kyzPgq7vnp-Aai0S5Sh63guc)

**GitHub issues (geneontology/go-annotation)**
- [#1487](https://github.com/geneontology/go-annotation/issues/1487) `contributes_to` on CC terms from inference pipelines
- [#1940](https://github.com/geneontology/go-annotation/issues/1940) no `colocalizes_with` on complexes
- [#2126](https://github.com/geneontology/go-annotation/issues/2126) Complex Portal IDs as subjects (2018)
- [#2149](https://github.com/geneontology/go-annotation/issues/2149), [#2213](https://github.com/geneontology/go-annotation/issues/2213), [#3002](https://github.com/geneontology/go-annotation/issues/3002) assembly terms on subunits
- [#2374](https://github.com/geneontology/go-annotation/issues/2374) INO80 Arp subunits and helicase activity
- [#2521](https://github.com/geneontology/go-annotation/issues/2521), [#2682](https://github.com/geneontology/go-annotation/issues/2682) oligomerization and homodimerization reviews
- [#2664](https://github.com/geneontology/go-annotation/issues/2664), [#3283](https://github.com/geneontology/go-annotation/issues/3283) catalytic versus non-catalytic subunits
- [#2760](https://github.com/geneontology/go-annotation/issues/2760) E3 adaptor subunits
- [#3242](https://github.com/geneontology/go-annotation/issues/3242), [#5254](https://github.com/geneontology/go-annotation/issues/5254) qualifiers in ISS and PAINT
- [#3510](https://github.com/geneontology/go-annotation/issues/3510) non-catalytic transporter subunits
- [#3616](https://github.com/geneontology/go-annotation/issues/3616) V-ATPase
- [#3865](https://github.com/geneontology/go-annotation/issues/3865) torsins and ATPase activators
- [#5574](https://github.com/geneontology/go-annotation/issues/5574) translation factor and the ribosome
- [#6310](https://github.com/geneontology/go-annotation/issues/6310) MF `occurs_in` complex
- [#6357](https://github.com/geneontology/go-annotation/issues/6357) SDHA consistency, substeps
- [#6414](https://github.com/geneontology/go-annotation/issues/6414) succinate dehydrogenase gp2term relations
- [#6466](https://github.com/geneontology/go-annotation/issues/6466) TOM complex subunits

**Repository pages**
- [PROTEIN_COMPLEX_FUNCTIONS](../../PROTEIN_COMPLEX_FUNCTIONS.md) (attribution framework, rubric, proteasome pilot)
- [SDH_GP2TERM_CONTRIBUTES_TO](../../SDH_GP2TERM_CONTRIBUTES_TO.md)
- [COMPLEXPORTAL](../../COMPLEXPORTAL.md)
- [OXPHOS](../../OXPHOS.md); [HUMAN_BBSOME](../../HUMAN_BBSOME.md); [PEROXISOME](../../PEROXISOME.md)
- [OVER_ANNOTATION_PATTERNS](../../OVER_ANNOTATION_PATTERNS.md); [IBA_REVIEW](../../IBA_REVIEW.md); [COSCIENTIST](../../COSCIENTIST.md)
- [CLAUDE.md](../../../CLAUDE.md) (participation test, protein-binding policy, `COMPLEX_ACTIVITY_TRANSFER`)
- `src/ai_gene_review/schema/gene_review.yaml` (`CoreFunction.contributes_to_molecular_function`)
