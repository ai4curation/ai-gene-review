# GO-CAM modelling: GO annotation guidelines

Status: draft v0.1 (2026-11-15) · Part of [GO_GUIDELINES](../../GO_GUIDELINES.md)

**In brief:**

- The unit of a GO-CAM is the activity: one molecular function, enabled by one gene product (or, for an emergent activity, one complex), occurring in one location, as part of one process chain. Make a second node for the same gene product only when the function, input, location, process or timing differs.
- Choose a causal relation in three steps: relationship type (regulation, provides input for, constitutively upstream, removes input for, or undetermined), then sign, then directness. When the mechanism is unknown, use `causally upstream of, positive/negative effect`. Do not let a phenotype stand in for a mechanism.
- "Directly" means two successive activities of different gene products, with no activity in between, the upstream one acting on the enabler of the downstream one. Transcriptional and miRNA control is always indirect. If a small molecule carries the effect, model the molecule.
- `has input` names what the activity acts on: the substrate, the target gene, the effector a receptor activates, the partners an adaptor bridges. It never names a receptor's ligand, a cofactor, a currency metabolite or an assay reagent. Where a ChEBI product links two steps, use `has output` and `has input` rather than `provides input for`.
- Every location must resolve to a real compartment, and a material-flow edge must not jump a membrane without the transporter or secretion step that crosses it.
- A model produces standard annotations. Before choosing an enabler or a relation, know which GAF/GPAD rows it will generate, and give every asserted edge its own evidence.

## Scope

This document covers how to build and how to review GO Causal Activity Models
(GO-CAMs). It sets out what an activity unit is, how molecular functions are
typed and linked by causal relations, how inputs, outputs, locations and
processes are attached, how complexes are represented, how evidence attaches
to edges, and how standard annotations are derived from a model.

It does not repeat the term-choice rules for molecular functions in general
([molecular-function.md](molecular-function.md)), for complexes in standard
annotation ([protein-complexes.md](protein-complexes.md)), or for annotation
extensions ([annotation-extensions.md](annotation-extensions.md)). Many GO-CAM
relations (`has input`, `occurs in`, `part of`) are also extension relations,
and the rules here agree with those documents. Relations that exist only in
GO-CAM (the MF-to-MF causal relations) are treated fully here.

In this repository GO-CAMs are read-only. We cache production models
(`gocams/<id>/<id>-src.yaml`), index their activities (`gocams/index.tsv`),
lint them (`just gocam-lint`, [gocam_lint](../../../docs/gocam_lint.md)),
check their compartments (`just gocam-compartments`,
[GOCAM_COMPARTMENTS](../../GOCAM_COMPARTMENTS.md)) and record assessments in
`gocams/<id>/<id>-review.yaml` (`GoCamReview`, with the workflow in
[the gocam-curation skill](../../../.claude/skills/gocam-curation/SKILL.md)).
The rules apply equally to a curator building a model in Noctua and to a
reviewer judging one.

## Principles

A GO-CAM states a mechanism. Each node is a claim that a named gene product
carries out a named activity; each edge is a claim that one activity affects
another in a stated way. A standard annotation says a gene product is
"involved in" a process; a model says what it does there and what happens
next. The extra expressiveness is only worth having if each edge means one
thing, so the causal relations are deliberately few and the choice between
them is driven by mechanism.

A model is also a source of standard annotations. Noctua exports GPAD rows
from models by reasoning over the graph, so a modelling shortcut (a complex
as enabler, a direct edge that implies binding) becomes a row in GOA that
other people review without seeing the model. Modelling choices therefore
have to survive two readings: as a pathway, and as the gene-level rows it
produces.

Specificity should reflect the biological conclusion, not the experimental
set-up. The consortium's modelling guideline puts it plainly: capture a target,
location or time only when it is "biologically important", and keep models as
general as the biology allows
([Drive: GO-CAM modeling guidelines](https://drive.google.com/open?id=1DS2ObQc1EVcQKAHjKNt-0jzFCSSVLDQ4Osm-1dsTwdA)).

## Rules

<a id="cam-1"></a>

### CAM-1. Model activities, not genes: each activity unit has one function, one enabler, one location chain and one process chain.

An activity unit is an instance of a GO molecular function class, linked to:
the gene product that carries it out (`enabled by`, RO:0002333); where it
happens (`occurs in`, BFO:0000066, one GO cellular component term, optionally
nested `part of` a cell type and an anatomical structure); the process it
contributes to (`part of`, BFO:0000050, one biological process, which may
itself be nested `part of` a larger process); optionally what it acts on
(`has input`, RO:0002233) and what it produces (`has output`, RO:0002234); and
optionally when it happens (`happens during`, RO:0002092, with a GO
biological phase or a developmental stage term).

Each level holds one term. If an activity seems to be part of two unrelated
processes, it is two activities, or one of the processes is a context of the
other and belongs in the nesting.

*Rationale.* This is the shape all consortium specifications share, from the
2016 curation documentation to the 2025 workshop decks. It is what makes the
model decomposable into standard annotations.

*Example.* In the *C. elegans* intestinal immunity model `568b0f9600000284`,
PMK-1 enables `GO:0004707` MAP kinase activity, occurs in `GO:0005829`
cytosol, and is part of `GO:0140367` antibacterial innate immune response;
ATF-7 enables `GO:0000981` DNA-binding transcription factor activity, RNA
polymerase II-specific, occurring in `GO:0005634` nucleus, in the same process.

*Provenance:* [GOC]. Sources:
[Drive: GO-CAM modeling guidelines](https://drive.google.com/open?id=1DS2ObQc1EVcQKAHjKNt-0jzFCSSVLDQ4Osm-1dsTwdA);
[Drive: GO-CAM Curation Documentation](https://drive.google.com/open?id=18ihslb7prB6CWtu2yjF-pMHZBTY1-AdXJAu-ZyuyXS4).

<a id="cam-2"></a>

### CAM-2. Give a gene product a second activity node only when the function, input, location, process or time differs.

A protein that is phosphorylated, moves, or changes partners does not
automatically get a new node. Create one when at least one of these differs:
the MF term; the `has input`; the `occurs in` chain; the `part of` chain; the
`happens during` value. Otherwise reuse the node.

The converse also holds: do not chain two nodes of one gene product with a
causal edge to represent an activation state (inactive kinase, then active
kinase). A state change caused by another gene product is an incoming edge on
one node. `gocam-lint` reports such chains as `same_gene_chain` (WARNING when
the MF repeats in one location) and duplicate nodes as `duplicate_activity`.

*Example.* A receptor tyrosine kinase that both binds its ligand and
phosphorylates an adaptor is one node, `GO:0004714` transmembrane receptor
protein tyrosine kinase activity, with `has input` the adaptor; the ligand
arrives on an incoming causal edge (CAM-5, CAM-8). A kinase that phosphorylates
two different substrates in two different processes is two nodes.

*Provenance:* [GOC] for the five criteria; [GOC+] for the ban on activation-state
chains, which the guideline implies but does not state. Sources:
[Drive: GO-CAM modeling guidelines](https://drive.google.com/open?id=1DS2ObQc1EVcQKAHjKNt-0jzFCSSVLDQ4Osm-1dsTwdA);
[gocam_lint](../../../docs/gocam_lint.md).

<a id="cam-3"></a>

### CAM-3. The enabler is the gene product that performs the activity; use a complex as enabler only for an emergent activity, and never the root complex term.

Apply the 2025 consortium rules for complexes in this order:

1. If a subunit performs the activity, that subunit is the enabler. Assign
   functions to the other subunits whose activity is known and link them in a
   causal flow (substrate adaptor, scaffold, catalytic subunit). Leave out
   subunits whose activity is unknown; their membership belongs in standard
   CC annotations to the complex term.
2. If several subunits are needed to form the active unit (a shared active
   site, a ligand pocket built from two chains, a heteromeric channel), the
   enabler is the most specific GO protein-containing complex term, with
   `has part` naming only the subunits that contribute.
3. If the active subunit is unknown, the complex term is the enabler and no
   `has part` is added.

Never use `GO:0032991` protein-containing complex itself as an enabler. If no
complex term of the right granularity exists, request one.

*Rationale.* The export depends on the case. Case 1 yields `GP enables MF`
for the active subunit. Case 2 is meant to yield `contributes_to` rows for each
`has part` member (not yet implemented in 2025). Case 3 yields no MF row at
all. A model that lists every member of a complex as `has part` will, once
case 2 export works, give the catalytic function to structural and accessory
subunits, which is exactly the over-annotation the complex working group set
out to stop ([PROTEIN_COMPLEX_FUNCTIONS](../../PROTEIN_COMPLEX_FUNCTIONS.md)).

*Example.* Case 1 in the 2025 deck: in the `GO:0031464` Cul4A-RING E3
ubiquitin ligase complex, DCAF12 enables `GO:1990756` ubiquitin-like
ligase-substrate adaptor activity, with the substrate as input, and the export
is "DCAF12 enables ubiquitin ligase-substrate adaptor activity". The cullin and
RING subunits get their own activities in the flow. For the pyruvate
dehydrogenase complex (`GO:0045254`), the three catalytic components each have
their own function (`GO:0004739` pyruvate dehydrogenase (acetyl-transferring)
activity, `GO:0004742` dihydrolipoyllysine-residue acetyltransferase activity,
`GO:0004148` dihydrolipoyl dehydrogenase (NADH) activity), linked by
`provides input for` because the lipoyl intermediate is protein-bound
(CAM-6).

*Provenance:* [GOC] for the three cases and the export table; [GOC+] for the
ban on `GO:0032991` (asked but not settled in the 2025 deck) and for limiting
`has part` to contributing subunits (the deck's Case 4 flags the problem but
gives no rule). Sources:
[Drive: 2025 GO-CAM guidelines for protein-containing complexes](https://drive.google.com/open?id=1vF8JCnUM_JqkxgAvVHHl6ntyXpk3tY4y_NAjRjZ3WJE);
[Drive: Contributes_to (2021 GOC)](https://drive.google.com/open?id=1g-2M8XQuINGN6eKVT0Sqm1OsudF_kM2D4jemv-izTks);
[Drive: GO-CAM modelling calls 2020-2022](https://drive.google.com/open?id=1rA1RiHst8e9tulY0zeua96WJSG2lKNS9VFWhDCWW2Ps).

<a id="cam-4"></a>

### CAM-4. Type each activity by the role it plays in the flow; a bare binding term is not an activity.

The MF term must say what the gene product does to the next step. Use these
role terms, each with its standard context:

| Role | MF term | `has input` | Outgoing edge |
|---|---|---|---|
| Protein ligand | `GO:0048018` receptor ligand activity or a child | its receptor | directly positively regulates the receptor activity |
| Receptor | `GO:0038023` signaling receptor activity or a child | the effector it acts on, not the ligand | directly positively regulates the effector |
| Coreceptor | `GO:0015026` coreceptor activity | the protein it acts on | as for receptor |
| Adaptor | `GO:0060090` molecular adaptor activity or a child | the two or more molecules it brings together | directly positively regulates, or constitutively upstream of, the downstream activity; provides input for when it brings an enzyme to its substrate |
| Sequestering protein | `GO:0140313` molecular sequestering activity, usually `GO:0140311` protein sequestering activity | the sequestered molecule | directly negatively regulates the sequestered molecule's activity; BP is part of negative regulation of that molecule's process |
| DNA-binding TF | a child of `GO:0000981`, e.g. `GO:0001228` or `GO:0001227` | the target gene | indirectly positively or negatively regulates the target's activity (CAM-9) |
| Enzyme | the catalytic activity | the substrate (CAM-5) | as the mechanism requires |

A binding term (`GO:0005515` protein binding, `GO:0005488` binding) has no
causal consequence, so it cannot carry an outgoing regulatory edge with any
meaning. If the binding is the mechanism, find the role: adaptor,
sequestering, inhibitor or activator, receptor, ligand. If no role term fits,
the binding belongs in a standard annotation, not in the model. An adaptor
with a single input is a warning sign that adaptor is the wrong term.

*Rationale.* `gocam-lint` found 56 binding-MF and 521 generic-MF warnings over
2,037 cached models (November 2026). Most are activities whose role the paper
does establish.

*Example.* CAV1 enables `GO:0140311` protein sequestering activity with `has
input` TLR4, directly negatively regulates TLR4 receptor activity, and is part
of negative regulation of the TLR4 pathway (MF guidelines, 2026 revision).
TYROBP enables molecular adaptor activity, bridging the virion receptor SIGLEC1 and the downstream PTPN11, whose scaffolding activity it activates.

*Provenance:* [GOC] for the role table; [GOC+] for the rule that a binding
term may not carry a causal edge. Sources:
[Drive: MF guidelines for GO-CAM (copy, reviewed 2026-03)](https://drive.google.com/open?id=1DWvc_g5yH4S8-Tc2rPtaAyPOIkYzITagK1sXysj0CY4);
[Drive: GO-CAM Curation Documentation](https://drive.google.com/open?id=18ihslb7prB6CWtu2yjF-pMHZBTY1-AdXJAu-ZyuyXS4);
[wiki: Annotation Conf. Call 2019-11-19](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2019-11-19).

<a id="cam-5"></a>

### CAM-5. `has input` names what the activity acts on; the ligand of a receptor is upstream, not input.

Correct fillers: the substrate of an enzyme; the target gene of a
transcription factor (the gene identifier, not "DNA" or a promoter region); the
effector a receptor activates; the molecules an adaptor bridges; the molecule a
sequestering protein holds; the cargo of a transporter. A ligand `has input`
its receptor. More than one input on one node means several substrates of one
reaction; an enzyme with alternative substrates gets one node per substrate
when the distinction matters.

Do not capture: an input already stated by the term (`GO:0004396` hexokinase
activity does not need `has input` D-hexose); currency metabolites (ATP for a
kinase); cofactors and metal ions; chemical analogues or other assay
conditions; the activating molecule of an "X-dependent" activity (calcium for
a calcium-dependent kinase). Direct physical interaction need not be shown
separately; an enzyme assay implies it.

A small-molecule ligand has no MF, because chemicals are not annotated. Link
it to the receptor activity with `is small molecule activator of` (RO:0012005)
or `is small molecule inhibitor of` (RO:0012006), not as the receptor's input.

*Rationale.* Putting the ligand on the receptor's input reverses the causal
flow: the ligand acts on the receptor. The linter rule `receptor_ligand_input`
found nine such models.

*Example.* Insulin enables receptor ligand activity, `has input` INSR, and
directly positively regulates INSR `GO:0005009` insulin receptor activity,
whose own input is the downstream effector it phosphorylates, not insulin
(the insulin signalling example in the MF guidelines). For a GPCR
activated by succinate, succinate `is small molecule activator of` the
receptor activity.

*Provenance:* [GOC]. Sources:
[wiki: Has input](https://wiki.geneontology.org/index.php/Has_input);
[Drive: MF guidelines for GO-CAM](https://drive.google.com/open?id=1DWvc_g5yH4S8-Tc2rPtaAyPOIkYzITagK1sXysj0CY4);
[gocam-curation has-input reference](../../../.claude/skills/gocam-curation/references/has-input.md).

<a id="cam-6"></a>

### CAM-6. Link metabolic steps through the ChEBI product; use `provides input for` only when the intermediate is a macromolecule or has no ChEBI entry.

When an upstream activity's product is the next activity's substrate and the
product is in ChEBI, write `[upstream] has output [ChEBI]` and `[downstream]
has input [ChEBI]`. The reasoner derives the causal link. Use `provides input
for` (RO:0002413) only when the intermediate is a modified protein or RNA, or a
chemical with no ChEBI identifier.

*Rationale.* Explicit molecules make the model checkable against Rhea and
Reactome reactions and make transport steps visible. A bare `provides input
for` hides what moves between the steps, and hence whether it crosses a
membrane (CAM-14).

*Example.* In canonical glycolysis (`GO:0061621`), hexokinase `has output`
CHEBI:61548 D-glucopyranose 6-phosphate(2-), which is the `has input` of
`GO:0004347` glucose-6-phosphate isomerase activity. In contrast, AKT1
phosphorylates RAC1, and phosphorylated RAC1 (no ChEBI entry) is the input of
FBXL19's substrate-adaptor activity, so AKT1's activity `provides input for`
FBXL19's (model `63d320cd00001536`, PMID:23512198).

*Provenance:* [GOC]. This reverses older documentation that named `provides
input for` as the metabolic-pathway relation (see Differences). Sources:
[wiki: Provides input for (reviewed 2023)](https://wiki.geneontology.org/index.php/Provides_input_for);
[Drive: GO-CAM Curation Documentation](https://drive.google.com/open?id=18ihslb7prB6CWtu2yjF-pMHZBTY1-AdXJAu-ZyuyXS4).

<a id="cam-7"></a>

### CAM-7. Choose the causal relation by relationship type, then sign, then directness.

Use the 2022 decision tree. First decide what kind of relationship holds:

| Relationship | Test | Relation(s) |
|---|---|---|
| Regulation | The upstream activity conditionally controls the downstream one. | `directly positively regulates` RO:0002629; `directly negatively regulates` RO:0002630; `indirectly positively regulates` RO:0002407; `indirectly negatively regulates` RO:0002409 |
| Provides input | The upstream activity makes a molecule the downstream one uses (CAM-6). | `provides input for` RO:0002413 |
| Constitutively upstream | The upstream activity is normally present and required, and does not control (CAM-10). | `constitutively upstream of` RO:0012009 |
| Removes input | Both act on the same input; the upstream one makes it unavailable (CAM-11). | `removes input for` RO:0012010 |
| Undetermined | Too little data to name a mechanism. | `causally upstream of, positive effect` RO:0002304; `causally upstream of, negative effect` RO:0002305 |

For regulation, then choose the sign, then directness (CAM-8). Always state a
sign when the data show one. Do not use the unsigned parents (`regulates`
RO:0002211, `positively regulates` RO:0002213, `negatively regulates`
RO:0002212, `causally upstream of` RO:0002411) in new models.

Edges read subject to object: the subject is the activity whose output changes
the other's rate. A reversed edge is QC flag `INCORRECT_DIRECTIONALITY`; a
wrong sign is `WRONG_CAUSAL_SIGN`.

*Provenance:* [GOC] for the tree; [GOC+] for the ban on unsigned parents (the
tree offers no path to them; older guidance and the repository skill still name
`positively regulates` RO:0002213 as the indirect relation). Sources:
[Drive: New Causal Relations Decision Tree for VPE (2022-12-20)](https://drive.google.com/open?id=1ODFtV2aEeUeOUDs8dupre-3hUJchLFMMu-kChPKR1Oc);
[Drive: GO-CAM modeling guidelines](https://drive.google.com/open?id=1DS2ObQc1EVcQKAHjKNt-0jzFCSSVLDQ4Osm-1dsTwdA).

<a id="cam-8"></a>

### CAM-8. Use a "directly" relation only between successive activities of different gene products, where the upstream activity acts on the downstream enabler; route small-molecule effects through the molecule.

A direct regulation edge requires all of the following:

1. No activity intervenes between the two.
2. The upstream activity acts on the enabler of the downstream activity
   (phosphorylation, cleavage, binding that changes its state), so the
   downstream gene product is the upstream activity's `has input`.
3. The two activities have different enablers.
4. The mechanism is known. A knockdown phenotype, an epistasis result or a
   co-immunoprecipitation does not establish it.

If an enzyme regulates another activity by making or destroying a small
molecule, do not draw a direct edge between the two proteins. Write the
enzyme's `has output` ChEBI term and link that molecule to the downstream
activity with `is small molecule activator of` or `is small molecule inhibitor
of`. If the molecule is not in ChEBI, use `indirectly positively/negatively
regulates`.

A compound function within one gene product (ligand binding that switches on a
kinase domain) is one node with the compound MF term, not two nodes joined by a
direct edge.

*Rationale.* In GO, "directly" means direct physical interaction, and the
reasoner uses that meaning: an MF that directly regulates another MF is
inferred to be a `GO:0098772` molecular function regulator activity, and the
pair is inferred to bind. A direct edge from cGAS to STING would therefore
assert that the two proteins bind, which is not the mechanism (the enzyme makes
a second messenger). The February 2020 annotation call restricted direct
relations to activities of different gene products for the same reason. The
2023 relation page allows "directly" for small-molecule effects, which
conflicts with the reasoner rule; routing the effect through the molecule
satisfies both.

*Example.* In the EGF-MAPK example on the relation's wiki page, each MAP
kinase kinase activity (`GO:0004708`) directly positively regulates the MAP
kinase activity (`GO:0004707`) of its substrate. (The page cites model
`6348a65d00001727`; the cached model with that id is now a REG3A
inflammation model, so cite models by content as well as id.) For cGAS, `GO:0061501` 2',3'-cyclic GMP-AMP
synthase activity `has output` cGAMP, and cGAMP is the small-molecule activator
of STING's activity.

*Provenance:* [GOC+]. Sources:
[wiki: Directly positively regulates (reviewed 2023)](https://wiki.geneontology.org/index.php/Directly_positively_regulates);
[wiki: Annotation Conf. Call 2020-02-04](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2020-02-04);
[Drive: Regulation Notes, 2020 GO-CAM Jamboree](https://drive.google.com/open?id=1mAIocbi6UvG_zbfCrWOUrneia3vl2XkjVPM39tmSx40);
[go-annotation#1979](https://github.com/geneontology/go-annotation/issues/1979);
[gocam-curation causal-relations reference](../../../.claude/skills/gocam-curation/references/causal-relations.md).

<a id="cam-9"></a>

### CAM-9. Control through gene expression is always indirect; the regulator's input is the target gene and its process names the mechanism.

A DNA-binding transcription factor, a transcription coregulator, a miRNA or a
substrate-specific splicing factor controls the amount of the downstream gene
product. Its edge to the target's activity is `indirectly positively
regulates` or `indirectly negatively regulates`, because transcription,
processing and translation lie in between. Its `has input` is the target gene,
and its `part of` process is the regulation term that names the mechanism, for
most eukaryotic TFs a child of `GO:0006357` regulation of transcription by RNA
polymerase II, such as `GO:0045944` positive regulation of transcription by RNA
polymerase II. Its location is `GO:0005634` nucleus, or better a resolvable
nuclear sub-compartment (CAM-13).

*Rationale.* A direct edge from a TF to a cytoplasmic enzyme says the TF acts
on the enzyme protein. `gocam-lint` flags these (`transcription_direct_edge`)
and the compartment check flags the ones that cross the nuclear envelope.

*Example.* Two of the six compartment-crossing ERRORs in the cached corpus are
transcriptional repressors that "directly" regulate secreted proteins
(`568b0f9600000284`, `632cf60a00000169`); both edges should be indirect.

*Provenance:* [GOC]. Sources:
[Drive: MF guidelines for GO-CAM, TF section](https://drive.google.com/open?id=1DWvc_g5yH4S8-Tc2rPtaAyPOIkYzITagK1sXysj0CY4);
[Drive: Regulation Notes, 2020 GO-CAM Jamboree](https://drive.google.com/open?id=1mAIocbi6UvG_zbfCrWOUrneia3vl2XkjVPM39tmSx40);
[gocam_lint](../../../docs/gocam_lint.md).

<a id="cam-10"></a>

### CAM-10. Use `constitutively upstream of` for required housekeeping steps, not regulation.

When an upstream activity is needed for a downstream one but runs at an
approximately constant rate and is not how the cell controls the downstream
activity, use `constitutively upstream of`. Typical cases: maturation
processing, lipid modification, folding or trafficking steps that every copy of
the downstream protein needs. An enzyme that modifies a protein as part of its
trafficking is not a regulator of that protein's activity: it acts in a
different place and does not set the amount or activity of its target.

*Example.* ZDHHC9 palmitoylates NRAS (`GO:0019706` protein-cysteine
S-palmitoyltransferase activity); palmitoylation is needed for NRAS
`GO:0003925` G protein activity at the membrane, but is not the switch, so the
edge is `constitutively upstream of` (model `635b1e3e00001677`, PMID:26493479).

*Provenance:* [GOC]. Sources:
[wiki: Constitutively upstream of](https://wiki.geneontology.org/index.php/Constitutively_upstream_of);
[Drive: Regulation Notes, 2020 GO-CAM Jamboree](https://drive.google.com/open?id=1mAIocbi6UvG_zbfCrWOUrneia3vl2XkjVPM39tmSx40).

<a id="cam-11"></a>

### CAM-11. Use `removes input for` only for a switch in which the upstream activity uses up the downstream activity's input site.

`removes input for` applies when both activities act on the same site of the
same target, and the upstream modification makes the site unavailable: the
histone code, the ubiquitin code, CpG methylation blocking TF binding. It does
not apply to an inducible enzyme that degrades a substrate in order to regulate
a pathway; that is regulation.

*Example.* KMT5A (`GO:0140944` histone H4K20 monomethyltransferase activity)
methylates H4K20 and so removes the input of TONSL's `GO:0140566` histone
reader activity, which binds unmethylated H4K20 (model `623d156d00000817`,
PMID:27338793).

*Provenance:* [GOC]. Source:
[wiki: Removes input for](https://wiki.geneontology.org/index.php/Removes_input_for).

<a id="cam-12"></a>

### CAM-12. Connect an activity to a process by a causal edge only when the mechanism is unknown; otherwise use `part of`.

If the activity is a step of the process, it is `part of` that process. If it
is a step of the regulation of the process, it is `part of` the regulation
term (`part of` positive regulation of X), not causally upstream of X. If the
activity is known to act before the process but its target is unknown, use
`causally upstream of, positive/negative effect`. If only a mutant effect is
known, use `causally upstream of or within` with a sign. A model should end in
an activity that regulates an activity of the next model, or in a regulation
term, not in a causal edge to a vague process.

Do not draw causal edges between two processes; process order follows from the
edges between their activities.

*Provenance:* [GOC]. Sources:
[Drive: GO-CAM modeling guidelines](https://drive.google.com/open?id=1DS2ObQc1EVcQKAHjKNt-0jzFCSSVLDQ4Osm-1dsTwdA);
[wiki: Causally upstream of or within](https://wiki.geneontology.org/index.php/Causally_upstream_of_or_within).

<a id="cam-13"></a>

### CAM-13. Give each activity one location that resolves to a distinct compartment.

`occurs in` takes a GO cellular component term that is not a protein-containing
complex (the complex belongs in the enabler). The term should resolve, through
`is_a`/`part_of`, to one compartment: cytosol, nuclear lumen, a membrane, a
lumen, the extracellular region. Prefer the precise term:

- Use `GO:0000228` nuclear chromosome rather than `GO:0000785` chromatin. In GO,
  chromatin is part of chromosome and chromosome is not part of nucleus
  (prokaryotes have chromosomes), so "chromatin" places the activity nowhere.
  This is the largest single source of unresolved locations: 293 activities in
  104 cached models.
- Name the membrane (plasma membrane, ER membrane), not `GO:0016020` membrane.
- For a transmembrane receptor, use `GO:0005886` plasma membrane, even though
  the catalytic domain faces one side.
- Add a cell type or anatomy only when the specificity is shown to matter, and
  never use a cell type term as the `occurs in` itself.
- For a symbiont activity inside a host, use the host term (`GO:0030430` host
  cell cytoplasm, `GO:0042025` host cell nucleus); see
  [MO-7](multi-organism-and-ncrna.md#mo-7).

*Rationale.* A location that resolves nowhere cannot be checked against
anything, and coarse terms (`cytoplasm`, `nucleus`) hide whether an edge
crosses a membrane.

*Example.* In BMP9 signalling (`600ced8500002343`), SMAD1 transcription factor
activity occurs in chromatin; the location that says what is meant is nuclear
chromosome.

*Provenance:* [GOC] for one location and no complexes; [NEW] for the
resolvability requirement and the nuclear-chromosome preference. Sources:
[Drive: GO-CAM modeling guidelines](https://drive.google.com/open?id=1DS2ObQc1EVcQKAHjKNt-0jzFCSSVLDQ4Osm-1dsTwdA);
[GOCAM_COMPARTMENTS](../../GOCAM_COMPARTMENTS.md);
[gocam-curation compartments reference](../../../.claude/skills/gocam-curation/references/compartments.md).

<a id="cam-14"></a>

### CAM-14. A material-flow edge must not cross a membrane without the activity that crosses it; a regulation edge may join compartments only if the regulated protein moves.

Classify each edge by the distance between its two locations. Two activities
in the same or adjacent compartments (sharing a boundary) can be linked
directly. For anything farther apart:

- A **material-flow edge** (`provides input for`, or a shared `has output` /
  `has input` molecule) means the molecule itself moves. Add the transporter,
  channel, translocon or secretion step, or say why it is absent.
- A **direct regulation edge** means the two proteins touch. It may join
  distant compartments only when the downstream protein is known to occupy a
  compartment next to the regulator and then moves (JAK1 touches STAT3 at the
  membrane; STAT3 then acts in the nucleus).
- A direct edge from an interior space to the exterior (cytosol to
  extracellular region) is an error unless one of these applies.

*Example.* In the IL-1β model `59cc772c00000000`, CASP1 cysteine-type
endopeptidase activity (`GO:0004197`) in `GO:0005829` cytosol directly
positively regulates IL1B `GO:0005125` cytokine activity in `GO:0005576`
extracellular region. The cleavage is direct, but the release step (gasdermin
D pore, `GO:0022829` wide pore channel activity) is missing; the model should
route the cytokine through it.

*Provenance:* [NEW]. The GOC documents say nothing about compartment adjacency;
the rule comes from this repository's spatial model. Sources:
[GOCAM_COMPARTMENTS](../../GOCAM_COMPARTMENTS.md);
[gocam_lint, compartment topology](../../../docs/gocam_lint.md).

<a id="cam-15"></a>

### CAM-15. Every asserted edge carries its own evidence: one ECO class and one reference per evidence instance, supporting that edge.

Each triple a curator asserts (enabled by, occurs in, part of, has input, each
causal edge) needs an ECO class and a reference. A causal edge's evidence must
show the causal relation, not merely the existence of the two activities; an
edge that cites exactly the references of its upstream enabler
(`edge_evidence_copied`) usually has not been checked. Electronic evidence from
UniProt keyword, UniProt subcellular location and UniPathway mappings may no
longer support Noctua assertions (2025). Where several papers support one
triple, record them as separate evidence instances, as the 2026 evidence
unwinding project does for standard annotations. NOT on an edge states evidence
against it.

*Rationale.* Missing evidence is the most common lint warning: 1,836 causal
edges in the cached corpus have none. The GPAD export drops a candidate
annotation if any asserted triple in its explanation lacks evidence, so
unevidenced edges also silently remove standard annotations.

*Provenance:* [GOC] for evidence per triple and the IEA restriction; [GOC+] for
the requirement that edge evidence address the edge. Sources:
[Drive: GO-CAM Curation Documentation](https://drive.google.com/open?id=18ihslb7prB6CWtu2yjF-pMHZBTY1-AdXJAu-ZyuyXS4);
[Drive: GO-CAM to GPAD and GPAD to GO-CAM (2019)](https://drive.google.com/open?id=1AgkJqA4-V0HG0SaDiNO9ENTxaQC_1HwsmwyhyHhuxog);
[Drive: Evidence unwinding meeting 2026-01-20](https://drive.google.com/open?id=1IsQ9cY3eJCkmpU6VAlJiinrm_Bztt_VZcKv98QPjsX8);
[go-annotation#6085](https://github.com/geneontology/go-annotation/issues/6085).

<a id="cam-16"></a>

### CAM-16. A model is a module: include the activities specific to its process, reuse general machinery by reference, and link models through a shared activity.

A model should cover one process, or a few closely interacting ones (a
pathway and its regulation). Activities that recur in many models (the
transcription machinery, the proteasome, nuclear import) belong in their own
models; refer to them with a process term in the `part of` chain or as a
process the model's last activity regulates. To link two pathway models, end
the first and start the second with the same activity: same gene product, MF,
location and process, and optionally the same input. Instances are not shared
across models.

A model with no causal edges is a set of standard annotations, not a GO-CAM,
and should be curated (and reviewed) as such. `small_model` (two or fewer
activities) and `orphan_activity` lint findings are prompts to check this.

*Provenance:* [GOC] for modules and reuse; [GOC+] for the linking convention,
which is a 2021 draft; [GOC+] for the no-edges rule, which follows the 2026
evidence-unwinding binning of standard versus GO-CAM models. Sources:
[Drive: GO-CAM modeling guidelines](https://drive.google.com/open?id=1DS2ObQc1EVcQKAHjKNt-0jzFCSSVLDQ4Osm-1dsTwdA);
[Drive: Convention for Linking GO-CAMs (draft)](https://drive.google.com/open?id=1iXgErHVojMFtbteiquzfJw76kPPs851XRVC558VdtGI);
[Drive: Evidence unwinding meeting 2026-01-20](https://drive.google.com/open?id=1IsQ9cY3eJCkmpU6VAlJiinrm_Bztt_VZcKv98QPjsX8).

<a id="cam-17"></a>

### CAM-17. Know the standard annotations your model will export, and review exported rows against the model.

The export flattens the reasoned graph. The rules that matter to curators:

| Model content | Exported row |
|---|---|
| gene product `enabled by` an MF node | GP enables MF |
| complex enabler with `has part` members | each member contributes_to MF (not yet implemented, 2025) |
| complex enabler, no `has part` | no MF row |
| MF `part of` BP | GP involved_in BP, MF context as extension |
| MF `occurs in` CC | GP is_active_in CC |
| `has input`, `occurs in` on the MF | extensions on the MF row |
| root MF with a causal edge to a BP | GP acts_upstream_of_or_within (or a signed child) BP |
| MF-to-MF causal edge | not exported as an extension; may yield an inferred MF regulator row |
| root term | exported only with ND evidence |
| do-not-annotate term | filtered |

Nested context (a BP `part of` a BP that has its own context) is not
exportable as an extension; the export keeps the primary chain only. When a
reviewed GAF row comes from a Noctua model, judge the row as you would any
other, but look at the model to see what the curator asserted; a wrong row is
often a modelling shortcut (CAM-3, CAM-8) rather than a wrong claim.

*Provenance:* [GOC] for the export behaviour; [GOC+] for the review practice.
Sources:
[Drive: GO-CAM to GPAD and GPAD to GO-CAM (2019)](https://drive.google.com/open?id=1AgkJqA4-V0HG0SaDiNO9ENTxaQC_1HwsmwyhyHhuxog);
[Drive: Standard annotations from triples specification (draft)](https://drive.google.com/open?id=1UwTDxUslfXEgdn4flcz1oBNKILtz3-alX5O_bcLtgLk);
[Drive: Standard annotation GO-CAM criteria notes](https://drive.google.com/open?id=1vmP4fqTl4Sc2AaCTI2OG3WuKYBBs5dhItiYC9yloees);
[Drive: 2025 GO-CAM guidelines for protein-containing complexes](https://drive.google.com/open?id=1vF8JCnUM_JqkxgAvVHHl6ntyXpk3tY4y_NAjRjZ3WJE).

<a id="cam-18"></a>

### CAM-18. In pathway imports, the enabler is the active unit, not the catalyst entity as drawn.

Reactome-derived models must map each catalyst to the gene product that
performs the reaction. When Reactome's catalyst is a set or complex of
modified forms of one gene product (cleavage fragments of a caspase, for
example), the active unit is the parent gene product from which all forms
derive. Reactome binding and dissociation events are not activities; they hide
an enabler (the adaptor or regulator that organises the complex) or a
consequence (the activation the binding causes). Black-box events that
associate a TF with expression of a target map to a gene-expression process,
not to an MF.

*Example.* For Reactome complex R-HSA-350870 (caspase-3), the active unit is
CASP3 1-277, the precursor of the active fragments; fixing this repaired 42
converted reactions (2025 notes).

*Provenance:* [GOC+]. Sources:
[Drive: Complex active units notes, 2025-07](https://drive.google.com/open?id=19GdhwjKWXGzkxBIL0eVxrdDvgzunW542DGkbD9W-1c8);
[Drive: molecular binding cleanup notes](https://drive.google.com/open?id=1ns86kSOMZsL84SLFQ60Bobl3t-0WNDa59oAhhc-JLsI);
[Drive: Conversion rules for manuscript](https://drive.google.com/open?id=1SEj8BCjKa6ZFp4xEhRlGvCAEhZjlq880);
[REACTOME](../../REACTOME.md).

<a id="cam-19"></a>

### CAM-19. When reviewing, check each activity against the gene review, and treat a model as one curator's assertion, not as evidence.

For each activity in a `GoCamReview`, record a verdict (`OK`, `UNCERTAIN`,
`WRONG`), any QC flags, and consistency with the gene's review
(`CONSISTENT`, `MORE_SPECIFIC`, `MORE_GENERAL`, `RELATED`, `CONFLICT`,
`NOT_IN_REVIEW`, `NO_GENE_REVIEW`). Consistency judges the function: a correct
function with a wrong edge is `CONSISTENT` plus `WRONG_CAUSAL_SIGN`, not
`CONFLICT`. Anchor every non-trivial verdict in verbatim text from the cited
paper.

The converse applies in gene reviews. A GO-CAM activity is not a reason to
accept a GAF row, and absence of a gene from a model is not a reason to remove
one. But a curator who modelled a pathway, included the gene, and gave it a
different role than a proposed `NEW` term made a decision to argue with
explicitly; check `gocams/index.tsv` before proposing a process term (see the
AGT example in [CLAUDE.md](../../../CLAUDE.md)). When a review decomposes a
precomposed "X involved in Y" term, record a GO-CAM that models Y in
`decomposed_into: gocam_associations`
([INVOLVED_IN_PRECOMPOSITION](../../INVOLVED_IN_PRECOMPOSITION.md)).

*Provenance:* [NEW]. Sources:
[gocam-curation skill](../../../.claude/skills/gocam-curation/SKILL.md);
[qc-and-consistency reference](../../../.claude/skills/gocam-curation/references/qc-and-consistency.md);
[CLAUDE.md](../../../CLAUDE.md).

## Decision aid

**Choosing the edge between activity A (upstream) and activity B.**

| Question | Answer | Relation |
|---|---|---|
| Is A's product B's substrate? | yes, product in ChEBI | A `has output` X; B `has input` X |
| | yes, product is a modified macromolecule | `provides input for` |
| Do A and B act on the same site, A first? | yes | `removes input for` |
| Is A required but constant, not a control point? | yes | `constitutively upstream of` |
| Does A control B? | via B's protein, nothing between, different enablers | `directly positively/negatively regulates` |
| | via a small molecule A makes or destroys | A `has output` X; X `is small molecule activator/inhibitor of` B |
| | via gene expression, or other intervening steps | `indirectly positively/negatively regulates` |
| None of the above is known | effect sign known | `causally upstream of, positive/negative effect` |

**Choosing the enabler for a complex activity.**

| Situation | Enabler | `has part` | Export |
|---|---|---|---|
| One subunit carries the activity | that subunit | none | enables |
| Active site spans subunits | specific complex term | contributing subunits only | contributes_to (pending) |
| Active subunit unknown | specific complex term | none | none |
| No specific complex term exists | request one; meanwhile case 3 with the nearest specific term | none | none |

**Placing a location.**

| Term in hand | Use instead |
|---|---|
| `GO:0000785` chromatin, chromosome sub-terms | `GO:0000228` nuclear chromosome (eukaryotes) |
| `GO:0016020` membrane | the named membrane |
| `GO:0005737` cytoplasm | `GO:0005829` cytosol, or the organelle |
| a CL cell type | a CC term nested `part of` the cell type |
| a complex term | move it to the enabler |

## Common errors

| Error | How it shows | Fix |
|---|---|---|
| Ligand as receptor input | receptor `has input` its ligand (`receptor_ligand_input`) | ligand node `has input` receptor and directly positively regulates it; small-molecule ligands via `is small molecule activator of` |
| TF directly regulates a protein | `transcription_direct_edge`; nucleus to cytoplasm crossing | `indirectly positively/negatively regulates`; TF `has input` target gene |
| Binding as the activity | `binding_mf` | name the role (adaptor, sequestering, inhibitor) or drop the node |
| Generic MF | `generic_mf` (`kinase activity`, `catalytic activity`) | the specific activity the paper shows |
| Activation-state chain | `same_gene_chain`, `duplicate_activity` | one node; incoming edge carries the activation |
| Direct edge across a membrane | `compartment_crossing` ERROR | add the transport or secretion step |
| Unresolvable location | chromatin, cell junction, a CL term as `occurs in` | nuclear chromosome; name the side of the junction; nest the cell type |
| Phenotype as mechanism | direct edge supported only by knockdown | `causally upstream of` with sign, or omit |
| Every complex member as `has part` | contributes_to for structural subunits (on export) | only the subunits that form the active unit |
| Edge with no evidence | `missing_evidence` | add ECO and reference that show the edge |
| Copied edge evidence | `edge_evidence_copied` | find the experiment that shows the causal link |
| Model split from one paper | `near_duplicate_models` | merge, or make each model a distinct process |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [Drive: GO-CAM modeling guidelines](https://drive.google.com/open?id=1DS2ObQc1EVcQKAHjKNt-0jzFCSSVLDQ4Osm-1dsTwdA) (undated, open comments) | Use "regulates" for known but non-direct control, with the mechanism named in the first `part of` BP. | Use the signed `indirectly positively/negatively regulates` (RO:0002407, RO:0002409); keep naming the mechanism in the BP (CAM-7, CAM-9). | The 2022 decision tree has no path to unsigned relations; reviewers of the guideline asked for signed children. |
| [gocam-curation causal-relations reference](../../../.claude/skills/gocam-curation/references/causal-relations.md) (repo) | Lists `positively regulates` RO:0002213 / `negatively regulates` RO:0002212 as the indirect relations, alongside the explicit indirect ones. | Treat RO:0002213/RO:0002212 as legacy parents; new or corrected edges use RO:0002407/RO:0002409. | RO:0002213 is the parent of the direct relation, so it does not assert indirectness. |
| [Drive: GO-CAM Curation Documentation](https://drive.google.com/open?id=18ihslb7prB6CWtu2yjF-pMHZBTY1-AdXJAu-ZyuyXS4) (c. 2016) | `provides input for` is the relation for metabolic pathways, where one activity makes a small molecule for the next. | Link through the ChEBI product with `has output`/`has input`; reserve `provides input for` for macromolecular or non-ChEBI intermediates (CAM-6). | Follows the 2023 relation page; explicit molecules are checkable. |
| [wiki: Directly positively regulates](https://wiki.geneontology.org/index.php/Directly_positively_regulates) (2023) vs [wiki: Annotation Conf. Call 2020-02-04](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2020-02-04) | The relation page allows a direct edge when the upstream activity makes or degrades a small-molecule regulator. The 2020 call fixed "directly" as direct physical interaction, with a reasoner rule that infers binding. | Route small-molecule effects through the molecule (`has output`, `is small molecule activator/inhibitor of`); no direct protein-to-protein edge (CAM-8). | The two sources conflict; a direct edge under the reasoner rule asserts a binding that did not happen. |
| [Drive: Regulation Notes, 2020 Jamboree](https://drive.google.com/open?id=1mAIocbi6UvG_zbfCrWOUrneia3vl2XkjVPM39tmSx40) vs [wiki: Annotation Conf. Call 2020-02-04](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2020-02-04) | The Jamboree notes allow a regulatory edge between two MFs of the same gene product (unfolded protein binding regulates kinase activity). The February 2020 call limits "directly regulates" to activities of different gene products. | One node with the compound MF for a single gene product; no causal edges between nodes of the same gene product to represent its internal switch (CAM-2, CAM-8). | Self-edges create spurious MF-regulator inferences and the `same_gene_chain` pattern. |
| [Drive: New Causal Relations Decision Tree](https://drive.google.com/open?id=1ODFtV2aEeUeOUDs8dupre-3hUJchLFMMu-kChPKR1Oc) | Gives `indirectly positively regulates` as "RO:00002407". | RO:0002407 (verified). | Typo in the deck; the extra digit makes an invalid CURIE. |
| [Drive: GO-CAM modeling guidelines](https://drive.google.com/open?id=1DS2ObQc1EVcQKAHjKNt-0jzFCSSVLDQ4Osm-1dsTwdA) | Location may be "transmembrane"; a reviewer comment points to GO:0044214. | `GO:0005886` plasma membrane for transmembrane receptors (CAM-13). | GO:0044214 "spanning component of plasma membrane" is obsolete. |
| [Drive: GO-CAM modeling guidelines](https://drive.google.com/open?id=1DS2ObQc1EVcQKAHjKNt-0jzFCSSVLDQ4Osm-1dsTwdA) | When no single subunit carries the activity, the complex is the enabler and each gene product has a `part of` relation to the activity. | Complex enabler with `has part` only for contributing subunits, or no `has part` when the active subunit is unknown (CAM-3). | Supersedes the earlier form; matches the 2025 rules and their export mapping. |
| [Drive: GO-CAM modelling calls, 2022-02-15](https://drive.google.com/open?id=1rA1RiHst8e9tulY0zeua96WJSG2lKNS9VFWhDCWW2Ps) | Proposed `GO:0032991` "or children" as allowed complex enablers. | Never the root term (CAM-3). | The 2025 deck asks whether the root should be disallowed; an enabler of "some complex" says nothing about who acts. |
| [gocam-curation complexes reference](../../../.claude/skills/gocam-curation/references/complexes.md) (repo) | Case 3, shared activity: "represent the relevant contributing subunits". | Represent the complex as enabler with the contributing subunits as `has part` (CAM-3). | The repo phrasing could be read as one node per subunit, which would export `enables` for each. |
| [Drive: 2025 complexes deck](https://drive.google.com/open?id=1vF8JCnUM_JqkxgAvVHHl6ntyXpk3tY4y_NAjRjZ3WJE), Case 4 | Notes that listing inactive members as `has part` will export contributes_to, "should not be allowed but we have no way to identify these". | `has part` is limited to subunits that form the active unit; reviewers flag violations as `COMPLEX_SUBUNIT_REPRESENTATION`. | Closes the gap the deck identified, at the curation step rather than in software. |
| [Drive: GO-CAM Curation Documentation](https://drive.google.com/open?id=18ihslb7prB6CWtu2yjF-pMHZBTY1-AdXJAu-ZyuyXS4) | Location: any GO CC term except complexes. | Location must resolve to a distinct compartment; chromatin becomes nuclear chromosome (CAM-13). | GO's chromatin has no `part_of` path to nucleus; 293 activities in 104 models resolve nowhere. |
| None (GOC documents silent) | No rule about compartments joined by an edge. | Material-flow edges may not skip a membrane; direct regulation may join compartments only if the target moves (CAM-14). | The repo compartment model found 54 unexplained direct edges, mostly missing transporters. |
| [Drive: MF guidelines for GO-CAM](https://drive.google.com/open?id=1DWvc_g5yH4S8-Tc2rPtaAyPOIkYzITagK1sXysj0CY4), adaptor section | The adaptor's outgoing edge is "directly positively regulates or constitutively upstream of"; a second example uses `provides input for`. | All three, chosen by mechanism: control (direct regulation), required scaffold (constitutively upstream), enzyme brought to substrate (provides input for) (CAM-4). | The section states two options and illustrates a third; the decision rule makes the choice explicit. |
| [wiki: Annotation Conf. Call 2019-11-19](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2019-11-19) | Re-annotate `activated by`/`inhibited by` extensions as a binding annotation that directly regulates the activity; a decoy receptor "enables protein binding, directly negatively regulates receptor activity". | Use the role term (`GO:0140311` protein sequestering activity for decoys, an activator or inhibitor term for direct regulators), not bare binding (CAM-4). | Sequestering and regulator terms now exist; binding terms cannot carry causal meaning. |
| [Drive: Complex active units notes, 2025-07](https://drive.google.com/open?id=19GdhwjKWXGzkxBIL0eVxrdDvgzunW542DGkbD9W-1c8) | Asks why CASP3 is annotated to cysteine-type endopeptidase activity, calling it "a well-known aspartic-type endopeptidase". | Keep `GO:0004197` cysteine-type endopeptidase activity for caspases. | Caspases are cysteine proteases that cleave after aspartate; the aside confuses substrate specificity with catalytic class. |
| [Drive: Convention for Linking GO-CAMs](https://drive.google.com/open?id=1iXgErHVojMFtbteiquzfJw76kPPs851XRVC558VdtGI) (draft) | Draft, with open questions on metabolic and signalling cases. | Adopt the shared-activity convention as "should" (CAM-16). | It is the only written convention and matches PomBase practice; leave its open questions open. |

## Open questions

1. **Complex context for a subunit's activity.** The 2025 deck proposes a
   relation stating that an activity is performed by a subunit while in a named
   complex (KAT8 in the MSL versus NSL complex). Until it exists, a subunit
   active in two complexes can only be modelled as two nodes differing in
   process. Should GO-CAM add `part of` (complex) on the activity, or a
   dedicated relation?
2. **Contributes_to export.** Case 2 export is not implemented. Until it is,
   emergent activities produce no MF rows. Should curators also make standard
   contributes_to annotations by hand in the meantime?
3. **Compound functions.** Nuclear receptors, receptor kinases and
   ligand-gated channels combine binding and a downstream activity. The 2020
   call noted that their logical definitions were under review. Should these
   ever be split into sub-activities joined by `has part`, as the 2016
   documentation allowed?
4. **Chromatin.** Should GO add a `part_of` path from chromatin to nucleus for
   eukaryotes (via a taxon-specific class), or should curators be required to
   use nuclear chromosome? The repo rule (CAM-13) assumes the latter.
5. **Small-molecule regulators.** If GOC prefers the 2023 relation-page reading
   (direct edges for small-molecule effects), the binding inference attached to
   "directly" needs to be dropped. This needs a decision from the ontology and
   software groups together.
6. **Host and symbiont activities in one model.** Models such as
   `62b4ffe300002385` (Shigella OspC3 inactivating human CASP4) put activities of
   two organisms in one graph. The location chain can nest a host organism, but
   there is no agreed way to record the interacting taxon on exported rows
   ([MO-8](multi-organism-and-ncrna.md#mo-8)).
7. **Standard versus GO-CAM models.** The evidence-unwinding project will bin
   "mixed" models. Should a model with one causal edge and many unconnected
   standard annotations be split?

## Sources

**GO Consortium Drive**

- [GO-CAM modeling guidelines](https://drive.google.com/open?id=1DS2ObQc1EVcQKAHjKNt-0jzFCSSVLDQ4Osm-1dsTwdA)
- [GO-CAM specifications / GO-CAM Curation Documentation](https://drive.google.com/open?id=18ihslb7prB6CWtu2yjF-pMHZBTY1-AdXJAu-ZyuyXS4)
- [GO-CAM specifications / Copy of MF guidelines for GO-CAM](https://drive.google.com/open?id=1DWvc_g5yH4S8-Tc2rPtaAyPOIkYzITagK1sXysj0CY4) (a copy; the original "MF guidelines for GO-CAM" is canonical)
- [2025-05 GOC meeting / GO-CAM guidelines for protein-containing complexes](https://drive.google.com/open?id=1vF8JCnUM_JqkxgAvVHHl6ntyXpk3tY4y_NAjRjZ3WJE)
- [Noctua VPE / New Causal Relations Decision Tree (2022-12-20)](https://drive.google.com/open?id=1ODFtV2aEeUeOUDs8dupre-3hUJchLFMMu-kChPKR1Oc)
- [2020 GO-CAM Jamboree / Regulation Notes](https://drive.google.com/open?id=1mAIocbi6UvG_zbfCrWOUrneia3vl2XkjVPM39tmSx40)
- [2021-05 GOC / Contributes_to](https://drive.google.com/open?id=1g-2M8XQuINGN6eKVT0Sqm1OsudF_kM2D4jemv-izTks)
- [2019-02 Hackathon / GO-CAM to GPAD and GPAD to GO-CAM](https://drive.google.com/open?id=1AgkJqA4-V0HG0SaDiNO9ENTxaQC_1HwsmwyhyHhuxog)
- [Standard annotations from triples and GO-CAM annotations specifications (draft)](https://drive.google.com/open?id=1UwTDxUslfXEgdn4flcz1oBNKILtz3-alX5O_bcLtgLk)
- [Standard annotation GO-CAM criteria notes](https://drive.google.com/open?id=1vmP4fqTl4Sc2AaCTI2OG3WuKYBBs5dhItiYC9yloees)
- [Evidence Unwinding Project / 2026-01-20 meeting](https://drive.google.com/open?id=1IsQ9cY3eJCkmpU6VAlJiinrm_Bztt_VZcKv98QPjsX8)
- [Convention for Linking GO-CAMs (draft)](https://drive.google.com/open?id=1iXgErHVojMFtbteiquzfJw76kPPs851XRVC558VdtGI)
- [GO-CAM Modeling Agenda and Minutes, 2020-2022](https://drive.google.com/open?id=1rA1RiHst8e9tulY0zeua96WJSG2lKNS9VFWhDCWW2Ps)
- [Reactome2GO / Complex active units 2025-07 notes](https://drive.google.com/open?id=19GdhwjKWXGzkxBIL0eVxrdDvgzunW542DGkbD9W-1c8)
- [Reactome2GO / molecular binding cleanup notes](https://drive.google.com/open?id=1ns86kSOMZsL84SLFQ60Bobl3t-0WNDa59oAhhc-JLsI)
- [Reactome and Pathway Mapping / Conversion Rules for Manuscript](https://drive.google.com/open?id=1SEj8BCjKa6ZFp4xEhRlGvCAEhZjlq880)

**GO wiki**

- [Provides input for](https://wiki.geneontology.org/index.php/Provides_input_for)
- [Removes input for](https://wiki.geneontology.org/index.php/Removes_input_for)
- [Constitutively upstream of](https://wiki.geneontology.org/index.php/Constitutively_upstream_of)
- [Directly positively regulates](https://wiki.geneontology.org/index.php/Directly_positively_regulates)
- [Has input](https://wiki.geneontology.org/index.php/Has_input)
- [Causally upstream of or within](https://wiki.geneontology.org/index.php/Causally_upstream_of_or_within)
- [Annotation Conf. Call 2019-11-19](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2019-11-19)
- [Annotation Conf. Call 2020-02-04](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2020-02-04)

**GitHub issues**

- [go-annotation#1979](https://github.com/geneontology/go-annotation/issues/1979) (cGAS: enzyme versus regulator of the viral life cycle)
- [go-annotation#6085](https://github.com/geneontology/go-annotation/issues/6085) (IEA sources no longer allowed in Noctua)

**Papers cited in source examples** (as cited by the wiki pages; not re-read here)

- [PMID:23512198](https://europepmc.org/article/MED/23512198) (AKT1, RAC1 and FBXL19)
- [PMID:26493479](https://europepmc.org/article/MED/26493479) (ZDHHC9 and NRAS palmitoylation)
- [PMID:27338793](https://europepmc.org/article/MED/27338793) (TONSL reads H4K20me0)

**Repository pages**

- [CLAUDE.md](../../../CLAUDE.md)
- [gocam-curation skill](../../../.claude/skills/gocam-curation/SKILL.md) and its references ([causal relations](../../../.claude/skills/gocam-curation/references/causal-relations.md), [has input](../../../.claude/skills/gocam-curation/references/has-input.md), [complexes](../../../.claude/skills/gocam-curation/references/complexes.md), [compartments](../../../.claude/skills/gocam-curation/references/compartments.md), [QC and consistency](../../../.claude/skills/gocam-curation/references/qc-and-consistency.md))
- [GOCAM_COMPARTMENTS](../../GOCAM_COMPARTMENTS.md)
- [gocam_lint](../../../docs/gocam_lint.md)
- [REACTOME](../../REACTOME.md)
- [EXECUTABLE_MODELS](../../EXECUTABLE_MODELS.md) (modules as the curated wiring that models are generated from)
- [PROTEIN_COMPLEX_FUNCTIONS](../../PROTEIN_COMPLEX_FUNCTIONS.md)
- [INVOLVED_IN_PRECOMPOSITION](../../INVOLVED_IN_PRECOMPOSITION.md)
- Cached models cited: `568b0f9600000284`, `632cf60a00000169`, `600ced8500002343`, `59cc772c00000000`, `63d320cd00001536`, `623d156d00000817`, `62b4ffe300002385` (under `gocams/`); `635b1e3e00001677` is cited from the wiki and is not in the local cache, and `6348a65d00001727` is cited by the wiki for an EGF-MAPK model but the cached model with that id has different content.
