# Gene product-to-term relations and negation: GO annotation guidelines

Status: draft v0.1 (2026-11-15) · Part of [GO_GUIDELINES](../../GO_GUIDELINES.md)

**In brief:**

- Every annotation has a relation. MF: `enables`, or `contributes_to` only for a subunit of an irreducible molecular machine. BP: `involved_in` only when the gene product's own activity is a step in the process; otherwise one of the `acts_upstream_of...` relations, with a direction wherever the data give one. CC: `located_in` for where the product was seen, `is_active_in` for where its activity was shown, `part_of` only for protein-containing complexes. Do not use `colocalizes_with` for new annotations.
- A wrong relation is a wrong claim, even when the term is right. When reviewing, correct the relation as a structured field. Do not fix it in prose, and do not remove the term.
- A NOT says the gene product lacks a property that a reader would otherwise expect it to have, and an experiment (or loss of key residues) tested for that property and found it absent. A negative or inconclusive result, "not required for", "not found in" and "expression unchanged" do not support a NOT.
- A NOT applies to the term and to every descendant of it. Put it on the most general term the evidence excludes and no higher, and never on an ancestor of a term the gene product positively has.
- A NOT carries no extension and is never made to binding. It needs a positive annotation in the same aspect (the ND root if nothing else is known).
- A NOT on a pseudoenzyme blocks the IBA and IEA rows that would otherwise reassert the lost activity. Removing those rows one review at a time does not.

## Scope

This document covers the relation slot of a standard GO annotation (GAF 2.2 column 4 and GPAD 2.0 relation column, the "gp2term relation" or "qualifier") and the negation flag that can accompany it (`NOT|<relation>`). It covers when to make a NOT annotation, how NOT annotations interact with the ontology and with phylogenetic propagation, and how reviewers should judge existing NOT rows and conflicting positive/NOT pairs.

Out of scope: the relations used *inside* annotation extensions and between GO-CAM activities (see [annotation-extensions.md](annotation-extensions.md) and [gocam-modeling.md](gocam-modeling.md)); evidence codes (see [evidence-codes.md](evidence-codes.md)), except where a code constrains the relation or the NOT; the choice between a process and its regulation (see [regulation-and-signaling.md](regulation-and-signaling.md)); complex membership as such (see [protein-complexes.md](protein-complexes.md)); PAINT procedure beyond its NOT logic (see [phylogenetic-propagation.md](phylogenetic-propagation.md)).

## Principles

**The relation is part of the claim.** "SDHB enables succinate dehydrogenase (quinone) activity" and "SDHB contributes to succinate dehydrogenase (quinone) activity" are different statements, and only the second is true. Enrichment tools can filter on the relation, and GO-CAM imports turn it into model structure. A relation that is right in the reviewer's prose but wrong in the file is wrong in every downstream use.

**Relations encode how much is known about mechanism.** `involved_in` claims that the gene product's molecular activity is a step in the process. `acts_upstream_of_or_within` claims only that perturbing the gene product affects the process. Most phenotype-derived process annotations support the second and not the first. Being explicit about this is the reason GAF 2.2 exists ([Drive: Draft GAF 2.2 documentation for gp2term relations](https://drive.google.com/open?id=1Jbpm1l5xjSabywE6ulIflujcESkdkQvlVI7bECgLbtw); see also [Drive: Legacy Annotations and New Qualifiers](https://drive.google.com/open?id=1VJx9mJMvWfUEVF9vCmwhDY2NwgvHsWf3tRgKFluZLa8)).

**GO is open-world, and NOT is the closed-world exception.** The absence of an annotation says nothing. A NOT annotation is the only way to state in GO that a property is absent, so it should be reserved for cases where that statement is both tested and useful: where a reader, a homology pipeline or a prediction method would otherwise assume the property is there ([wiki: Elements of an annotation](https://wiki.geneontology.org/index.php/Elements_of_an_annotation); [Drive: Response to "evaluate GO prediction methods" Q from Biostars 2023](https://drive.google.com/open?id=1EodZspmExNTEu8c9Gzs6wpUZ4RWwj3aMlmk3TyAc4Bs)).

**Positive claims propagate up and NOT claims propagate down.** A positive annotation to a term entails the same annotation to its `is_a` and `part_of` ancestors. A NOT annotation entails NOT to every descendant. Every scope rule for NOT follows from this asymmetry.

## The relation table

All relations are from the Relations Ontology (RO) or BFO. Ids were checked against RO with `runoak -i sqlite:obo:ro info`. "Default" is the relation GO rule gorule-0000061 applies when none is asserted. The defaults differ between sources; see [QN-3](#qn-3) and the Differences table.

| Aspect | Relation (GAF 2.2 token) | Id | Use when | Minimum evidence |
|---|---|---|---|---|
| MF | `enables` (default) | RO:0002327 | The gene product itself carries out the activity, alone, as a homomer, or as the catalytic subunit of a complex | Any MF-capable evidence (IDA, IMP on activity, IKR for NOT, IBA, IEA, ISS...) |
| MF | `contributes_to` | RO:0002326 | The activity belongs to a complex and cannot be assigned to this subunit or to a smaller set of subunits that includes it | An assay of the complex plus a reason the subunit is part of the active unit (shared active site, required core subunit) |
| BP | `involved_in` | RO:0002331 | The gene product's MF is a step in the process (`part_of`) | Knowledge of the MF and of its place in the process; an MF annotation `part_of` the BP in the ontology also qualifies |
| BP | `acts_upstream_of_or_within` | RO:0002264 | Perturbation affects the process and the mechanism is unknown; direction unknown | IMP, IGI, phenotype-derived evidence |
| BP | `acts_upstream_of_or_within, positive effect` | RO:0004032 | As above; loss reduces the process (or gain increases it) | As above, with direction |
| BP | `acts_upstream_of_or_within, negative effect` | RO:0004033 | As above; loss increases the process | As above, with direction |
| BP | `acts_upstream_of` | RO:0002263 | Mechanism known; the activity occurs before the process, is not a step in it, and does not regulate it | Mechanistic evidence placing the activity outside the process |
| BP | `acts_upstream_of, positive effect` | RO:0004034 | As above, and required for the process to occur | As above |
| BP | `acts_upstream_of, negative effect` | RO:0004035 | As above, and it prevents or reduces the process | As above |
| CC | `located_in` (default for non-complex CC) | RO:0001025 | The product was detected in a cellular anatomical structure (GO:0110165) or virion component (GO:0044423) | IDA, HDA, ISS, IEA... |
| CC | `is_active_in` | RO:0002432 | The product carries out its MF in that structure (`enables` composed with `occurs_in`) | A localisation plus evidence that the activity occurs there |
| CC | `part_of` (default for complexes) | BFO:0000050 | The product is a subunit of a protein-containing complex (GO:0032991 and descendants) | IDA/IPI on complex composition, ISS, IBA... |
| CC | `colocalizes_with` | RO:0002325 | Deprecated. Not for new annotations | n/a |

Sources: [wiki: Annotation Relations](https://wiki.geneontology.org/index.php/Annotation_Relations) (reviewed 2023-09-05); [Drive: Annotation relations - Guidelines for P2GO](https://drive.google.com/open?id=1DXdjAuNf7u8CKXYlgW5kyzPgq7vnp-Aai0S5Sh63guc); [Drive: Use of relations for GO annotation - GP2term and extensions (2021)](https://drive.google.com/open?id=128U6g91Iv2ej9pcgTSGOowbhjp4GwGXmE4gDTiue1Cc).

Any of these can be negated (`NOT|enables`, `NOT|involved_in`, `NOT|located_in`...).

## Rules

### Relations

<a id="qn-1"></a>

### QN-1. Every annotation must carry an explicit relation that matches its aspect and term type.

**Rationale.** Since GAF 2.2 and GPAD 2.0, column 4 always holds a relation. A relation from the wrong aspect, or `located_in`/`is_active_in` on a complex term, is malformed. gorule-0000061 repairs some cases, but repair is not the same as a curator's statement.

**Rule detail.** MF terms take `enables` or `contributes_to`. BP terms take `involved_in` or one of the six `acts_upstream_of...` relations. CC terms below GO:0032991 protein-containing complex take `part_of`. Other CC terms take `located_in` or `is_active_in`. Protein complexes are not annotation subjects for `part_of GO:0032991` or its descendants (gorule-0000039): a complex is not a member of itself, so annotate the individual proteins.

**Example.** A row "UniProtKB:Q15526 SURF1 `located_in` GO:0005739 mitochondrion" is well-formed. "SDHB `located_in` respiratory chain complex II" is not: complex membership is `part_of`.

**Provenance.** [GOC]. [wiki: Annotation Relations](https://wiki.geneontology.org/index.php/Annotation_Relations); [wiki: Located in](https://wiki.geneontology.org/index.php/Located_in); [Drive: Feedback on GO rules (FlyBase copy)](https://drive.google.com/open?id=1AiEBQGA37oyyoFmDYNexYOlDIwqPHnMvAESIVqgjxFM).

<a id="qn-2"></a>

### QN-2. Use `contributes_to` only when no single subunit, or smaller subset of subunits, can be said to carry out the activity. Annotate every catalytic-core subunit this way, and no accessory subunit.

**Rationale.** `contributes_to` exists for "irreducible molecular machines" ([wiki: Contributes to](https://wiki.geneontology.org/index.php/Contributes_to)). Being part of a complex is not enough. Applied too freely, `contributes_to` gives every structural or regulatory subunit its complex's catalytic activity, a pattern the repo's [TOP_NOTS](../../TOP_NOTS.md) worklist finds repeatedly (assembly factors such as SURF1 carrying GO:0004129 cytochrome-c oxidase activity).

**The test** (three questions, adapted from the wiki checklist):

1. Is the activity a property of the complex and not of one subunit? If one subunit has it alone, that subunit `enables` it and the others get no annotation to that term.
2. Is this subunit part of the active unit? Look for a shared active site, an essential core role, or a rotary or channel mechanism that needs the subunit. A regulatory, assembly or scaffolding subunit is not part of the active unit. Give it its own activity instead (GO:0060090 molecular adaptor activity, GO:0098772 molecular function regulator activity or a child, GO:0030234 enzyme regulator activity) together with `part_of` the complex.
3. Is it unknown which subunit carries the activity? Then make no MF annotation to any subunit. Annotate the complex membership (CC) and the process (BP).

**Examples.**

- *Succinate dehydrogenase.* No subunit catalyses the whole succinate-to-quinone reaction, so SDHA, SDHB, SDHC and SDHD each `contributes_to` GO:0008177 succinate dehydrogenase (quinone) activity. That is the agreed outcome of [go-annotation#6414](https://github.com/geneontology/go-annotation/issues/6414), worked in the repo's [SDH_GP2TERM_CONTRIBUTES_TO](../../SDH_GP2TERM_CONTRIBUTES_TO.md). The parent GO:0000104 succinate dehydrogenase activity needs a separate judgement, because the flavoprotein SDHA can run the succinate half-reaction alone. `enables` GO:0000104 may be right for SDHA and wrong for the other three.
- *ATP synthase.* Every subunit of the F1, F0 and stator sectors `contributes_to` GO:0046933 proton-transporting ATP synthase activity, rotational mechanism ([wiki: Contributes to](https://wiki.geneontology.org/index.php/Contributes_to)).
- *ATP citrate lyase* from *Chlorobaculum tepidum*: both subunits supply active-site residues, neither is active alone, and both `contributes_to` GO:0003878 ATP citrate synthase activity.
- *Not contributes_to.* In the PIGM-PIGX complex only PIGM `enables` GO:0000030 mannosyltransferase activity. PIGX is required but has no activity of its own. eIF2gamma `enables` GO:0003924 GTPase activity, and eIF2alpha and eIF2beta get no GTPase annotation at all.

**Provenance.** [GOC+]. The test restates the wiki. The sharpening is the accessory-subunit alternative and the "unknown subunit, no MF" branch, which the wiki states but which annotators often skip. [wiki: Contributes to](https://wiki.geneontology.org/index.php/Contributes_to); [wiki: Enables](https://wiki.geneontology.org/index.php/Enables); [Drive: Contributes_to (GOC 2021)](https://drive.google.com/open?id=1g-2M8XQuINGN6eKVT0Sqm1OsudF_kM2D4jemv-izTks); [SDH_GP2TERM_CONTRIBUTES_TO](../../SDH_GP2TERM_CONTRIBUTES_TO.md).

<a id="qn-3"></a>

### QN-3. Use `involved_in` only when the gene product's own activity is a step in the process. Use an `acts_upstream_of...` relation for every other causal link, and treat a BP row with no stated relation as `acts_upstream_of_or_within`.

**Rationale.** The repo's participation test (see [CLAUDE.md](../../../CLAUDE.md), "Do not add what curators deliberately declined to add") reads: a gene product is `involved_in` a process only if it does some of the work of that process. Necessity, the kind of evidence a knockout gives, does not meet this test. Mutant phenotypes support `acts_upstream_of_or_within` with a direction. `involved_in` needs to know what the product does and where that activity sits in the process.

The default needs a decision because the sources disagree. The current wiki marks `acts_upstream_of_or_within` as the default BP relation, the least specific one that is always true. The 2021 Protein2GO training and the GOA export defaults use `involved_in`. The 2018 GAF 2.2 draft left the choice to each contributing group. PAINT assigns `involved_in` to every IBD and IBA, whatever relation the seed annotations carried ([wiki: 5 May 2020 PAINT Conference Call](https://wiki.geneontology.org/index.php/5_May_2020_PAINT_Conference_Call)). We recommend reading an unqualified BP annotation as `acts_upstream_of_or_within`, which is the only reading that cannot be false. A curator asserting `involved_in` must be able to name the MF.

**Rule detail.**

- `involved_in`: you can state the MF, and the MF is `part_of` the process, either in the ontology (transporter activity `part_of` transport) or by evidence that places the activity as a step.
- `acts_upstream_of_or_within, positive effect` / `negative effect`: the default for phenotype-based BP annotation. Always pick a direction when the data show one. The bare relation is a grouping relation and should be rare ([wiki: Acts upstream of or within](https://wiki.geneontology.org/index.php/Acts_upstream_of_or_within)).
- `acts_upstream_of, positive/negative effect`: the mechanism is known, the activity comes earlier, and it is neither a step nor a regulator. Example: an enzyme that produces a precursor consumed by a later, separate process.
- A gene product that regulates X is `involved_in` "regulation of X", not `acts_upstream_of` X. Do not stack a direction relation on a regulation term (`acts_upstream_of, positive effect` "positive regulation of X"): the term already states the direction. This answers the question left open in [go-annotation#2377](https://github.com/geneontology/go-annotation/issues/2377).

**Examples.**

- NEDD4 `enables` GO:0004842 ubiquitin-protein transferase activity on RNA polymerase II and is `involved_in` GO:0006511 ubiquitin-dependent protein catabolic process ([wiki: Involved in](https://wiki.geneontology.org/index.php/Involved_in)).
- A transcription factor whose knockout reduces T cell numbers, with no target genes identified, is `acts_upstream_of_or_within, positive effect` of the relevant differentiation process, not `involved_in`.
- *IBA reading.* An IBA `involved_in` row inherits that relation from PAINT's default, not from its seeds. If every seed is an IMP phenotype, treat the IBA as `acts_upstream_of_or_within` when judging participation (see [phylogenetic-propagation.md](phylogenetic-propagation.md)).

**Provenance.** [NEW] for the default reading and the IBA caveat; [GOC] for the relation definitions. [wiki: Annotation Relations](https://wiki.geneontology.org/index.php/Annotation_Relations); [wiki: Acts upstream of](https://wiki.geneontology.org/index.php/Acts_upstream_of); [Drive: Annotation relations - Guidelines for P2GO](https://drive.google.com/open?id=1DXdjAuNf7u8CKXYlgW5kyzPgq7vnp-Aai0S5Sh63guc); [Drive: Heuristics for gp2term relations](https://drive.google.com/open?id=1GSLdTrBVdSyaWU4R0L3M0Y-rrNRW22aoYFBh_nwAwC0); [go-annotation#2377](https://github.com/geneontology/go-annotation/issues/2377).

<a id="qn-4"></a>

### QN-4. Use `is_active_in` only when the evidence places the activity, not just the protein, in the location. Otherwise use `located_in`.

**Rationale.** `is_active_in` is defined by the property chain `enables o occurs_in`. It is the stronger claim and the one GO-CAM needs. A GFP fusion or a proteomics hit supports `located_in`. An activity assay on a purified compartment, or a function that only makes sense on one side of a membrane (a matrix enzyme whose substrate exists only in the matrix), supports `is_active_in`.

**Rule detail.** A protein seen in transit (secretory proteins in the ER, receptors passing through the endomembrane system) is not active there. Do not use `is_active_in` for transit compartments, and use `located_in` for them only when the repo's organelle rules allow it ([ORGANELLES](../../ORGANELLES.md), rule 7: "transit is not residence"). The 2023 Padua breakout drew the same line for `colocalizes_with` rows on GO:0012505 endomembrane system: receptors trafficked through the endomembrane system and not active there should not have that localisation captured.

**Entailment** (as used by the repo's [action consistency](../../../docs/action_consistency.md) checks): `is_active_in` X entails `located_in` X, and `part_of` complex entails `located_in` the complex's location. `located_in` entails neither.

**Example.** CED-3 `is_active_in` GO:0005829 cytosol, because the caspase acts there ([wiki: Is active in](https://wiki.geneontology.org/index.php/Is_active_in)). If a protein is also seen at GO:0005635 nuclear envelope by immunofluorescence and no activity is shown there, that row is `located_in` at most.

**Provenance.** [GOC+]. [wiki: Is active in](https://wiki.geneontology.org/index.php/Is_active_in); [wiki: Located in](https://wiki.geneontology.org/index.php/Located_in); [Drive: Reviewing colocalizes_with annotations (2023)](https://drive.google.com/open?id=1T9ww92HdP291B7tbeqAD91xvTPxdwwjM9bHJwh6d56o).

<a id="qn-5"></a>

### QN-5. Do not make new `colocalizes_with` annotations. When reviewing one, convert it to `is_active_in` or `located_in` if the evidence supports that, or remove it.

**Rationale.** Curators have read `colocalizes_with` in at least three ways: transient localisation, low assay resolution, and echoing a paper's wording ("X colocalizes with Y"). GO has marked it deprecated ([wiki: Colocalizes with](https://wiki.geneontology.org/index.php/Colocalizes_with), last reviewed 2018). The repo schema's enum still describes it as "weaker than located_in", which is a reading GO no longer endorses.

**Conversion.**

| What the evidence shows | Convert to |
|---|---|
| The product acts there, even transiently | `is_active_in` (use an extension or GO-CAM for timing) |
| The product is a resident there, activity not shown | `located_in` |
| The product passes through on the way to its site of action | Remove (not a location claim) |
| The paper says "colocalizes with marker M" as a localisation method | Judge the localisation itself and apply the rows above |
| Resolution too low to place it at the term's granularity | `located_in` a coarser term the assay can resolve (a root organelle is acceptable; see [ORGANELLES](../../ORGANELLES.md)) |

**Review action.** If the term is kept with a different relation, MODIFY the row and add a relation-only NEW row ([QN-7](#qn-7)). If the location does not hold, REMOVE it.

**Provenance.** [GOC+]. GO deprecated the relation but published no conversion procedure; the table is ours. [wiki: Colocalizes with](https://wiki.geneontology.org/index.php/Colocalizes_with); [Drive: Reviewing colocalizes_with annotations (2023)](https://drive.google.com/open?id=1T9ww92HdP291B7tbeqAD91xvTPxdwwjM9bHJwh6d56o); [wiki: 31 Aug 2021 PAINT Conference Call](https://wiki.geneontology.org/index.php/31_Aug_2021_PAINT_Conference_Call) (IBA for GO:0005635 nuclear envelope that had been withheld only because of a `colocalizes_with` mismatch).

<a id="qn-6"></a>

### QN-6. Judge the relation together with the term. Positive annotations entail ancestors only through relations that carry up.

**Rationale.** Positive claims propagate up the ontology with their relation, and some relations entail weaker ones. A consistency check that ignores relations reports false conflicts, such as `ACCEPT located_in` the axoneme next to `REMOVE is_active_in` the cilium, and misses real ones.

**Entailment table** (from the repo's `action_consistency.py`, which encodes GO's property chains):

| A positive row with... | ...also asserts, for the same or an ancestor term |
|---|---|
| `is_active_in` | `located_in` |
| `part_of` (complex) | `located_in` |
| `enables` or `contributes_to` an MF that is `part_of` a BP | `involved_in` (hence `acts_upstream_of_or_within`) that BP |
| `involved_in` | `acts_upstream_of_or_within` |
| `acts_upstream_of, positive effect` | `acts_upstream_of`; `acts_upstream_of_or_within, positive effect`; `acts_upstream_of_or_within` |
| `acts_upstream_of, negative effect` | the negative-effect analogues |
| `contributes_to` | not `enables` |

**Example.** An ACCEPTed `contributes_to` GO:0008177 row does not support `enables` GO:0000104. An ACCEPTed `involved_in` GO:0006303 double-strand break repair via nonhomologous end joining row does entail `involved_in` GO:0006281 DNA repair, so a REMOVE of a GO:0006281 row on the same gene needs an argument that the NHEJ row is also wrong.

**Provenance.** [GOC+]. The property chains are GOC's; using them for review consistency is the repo's addition. [action consistency](../../../docs/action_consistency.md); [wiki: Is active in](https://wiki.geneontology.org/index.php/Is_active_in).

<a id="qn-7"></a>

### QN-7. When reviewing, correct a wrong relation as a structured relation change. Do not REMOVE a right term because its relation is wrong.

**Rationale.** A review judges claims. "SDHB enables GO:0008177" is false and "SDHB contributes_to GO:0008177" is true. The term is sound, so removing the row loses the true claim. Correcting it only in prose leaves the file asserting the false one: the repo's SDH audit found five reviews arguing for `contributes_to` in prose while only two rows carried it in the structured field.

**Procedure (repo).** Mark the existing row `MODIFY`, say in `reason` that only the relation changes, and add one `NEW` row with the same term and the corrected `qualifier`. Validation accepts this relation-only pattern, which [PR #3223](https://github.com/ai4curation/ai-gene-review/pull/3223) established for SDHB and SDHD. Apply the same pattern to `involved_in` → `acts_upstream_of_or_within, positive effect`, to `colocalizes_with` → `located_in`, and to `enables` → `contributes_to`.

**Provenance.** [NEW]. GO has no review procedure for relation-only corrections. [SDH_GP2TERM_CONTRIBUTES_TO](../../SDH_GP2TERM_CONTRIBUTES_TO.md); [CLAUDE.md](../../../CLAUDE.md).

### NOT annotations

<a id="qn-8"></a>

### QN-8. Make a NOT annotation only when an experiment tested for the property and found it absent, or when the key residues for it are lost (IKR), and only when a reader would otherwise expect the property.

**Rationale.** The NOT qualifier is for absence that has been shown. Negative and inconclusive results do not show absence. The problem has been on record since go-annotation issue #3 (2003): a curator annotated NOT Golgi-to-vacuole transport because a mutant showed no missorting of one cargo, which means "not required for this assay", not "not involved". The documentation contradicted itself for another fifteen years. It suggested NOT for "our favorite protein is not found in the nucleus" until that example was removed in 2019 ([go-annotation#2237](https://github.com/geneontology/go-annotation/issues/2237)). The current wiki states the rule plainly ([wiki: Elements of an annotation](https://wiki.geneontology.org/index.php/Elements_of_an_annotation), reviewed 2026-03).

**Supports a NOT:**

- An activity assay on adequate protein that detects no activity where the family predicts one, ideally with a positive control. Example: CRY2 NOT GO:0000719 photoreactive repair, where a photolyase homologue lacks repair activity ([NOT_ANNOTATION_USAGE](../../NOT_ANNOTATION_USAGE.md)). Another: COQ8B NOT GO:0004672 protein kinase activity, because the family "lacks canonical protein kinase activity in trans" (PMID:27499294, cited in `genes/human/COQ8B`).
- Loss of catalytic residues established phylogenetically, using IKR (ECO:0000320 phylogenetic determination of loss of key residues evidence used in manual assertion). An IKR row must be a NOT (gorule-0000042).
- An antimicrobial-killing assay negative for one class of target, for a peptide active against another class. These are close to activity negatives.

**Does not support a NOT:**

- "Not required for" a process (knockout has no phenotype): redundancy and assay sensitivity are the usual explanations.
- "Not detected in" a location in a localisation experiment that found the protein elsewhere ([wiki: Elements of an annotation](https://wiki.geneontology.org/index.php/Elements_of_an_annotation)).
- Expression unchanged after a stimulus: IEP evidence never supports a NOT. The repo audit found 169 IEP-only NOT rows in GOA, 82% of them "NOT response to..." terms ([NOT_ANNOTATION_USAGE](../../NOT_ANNOTATION_USAGE.md)).
- An abundance result. FGFR4 NOT GO:1903412 response to bile acid (IMP, PMID:19085950) rests only on bile acid not changing FGFR4 protein level. The repo review REMOVEs it.
- Absence that nobody expected. A NOT that rules out a property no reader would have assumed adds nothing.

**Provenance.** [GOC] for the core rule; [NEW] for the explicit IEP exclusion. [wiki: Elements of an annotation](https://wiki.geneontology.org/index.php/Elements_of_an_annotation); [go-annotation#3](https://github.com/geneontology/go-annotation/issues/3); [go-annotation#2237](https://github.com/geneontology/go-annotation/issues/2237); [NOT_ANNOTATION_USAGE](../../NOT_ANNOTATION_USAGE.md).

<a id="qn-9"></a>

### QN-9. A NOT negates the term and all its descendants. Place it on the most general term the evidence excludes, and never on an ancestor of a term the gene product positively has.

**Rationale.** "NOT enables GO:0004672 protein kinase activity" also means NOT GO:0004674 protein serine/threonine kinase activity (which `is_a` GO:0004672), and NOT every other child. A NOT placed too high therefore contradicts any positive annotation below it, even one from a different paper.

**Example (DNA polymerase alpha, [go-annotation#1761](https://github.com/geneontology/go-annotation/issues/1761)).** Human POLA1 (P09884) carried NOT rows to excision-repair processes (PMID:1730053, PMID:1508673) and also a NOT to the parent "DNA synthesis involved in DNA repair", while PMID:11470886 showed a role in double-strand break repair. GO:1904161 DNA synthesis involved in UV-damage excision repair `is_a` GO:0000731 DNA synthesis involved in DNA repair, and GO:0006303 double-strand break repair via nonhomologous end joining `is_a` GO:0006281 DNA repair. The NOT on the parent was the logical error. The fix moved the NOTs to the specific excision-repair children (GO:1904161, GO:0006289 nucleotide-excision repair) and kept the positive NHEJ annotation. Both papers stayed valid.

**Choosing the level.** Ask what the experiment excluded. A kinase-dead mutant shown to bind its substrate excludes catalysis (GO:0004672), not binding. A protein that keeps phospholipid binding but has lost calcium dependence gets NOT GO:0005544 calcium-dependent phospholipid binding while keeping GO:0005543 phospholipid binding. This is the Syt8 case from PAINT, PTHR10024 ([wiki: 16 December 2014 PAINT Conference Call](https://wiki.geneontology.org/index.php/16_December_2014_PAINT_Conference_Call)).

**Repo check.** The [action consistency](../../../docs/action_consistency.md) rules warn when a kept NOT row is on the same term as, or an ancestor of, a kept positive row. When it fired it found ARL6 NOT `cilium` against `axoneme`, DNM1L NOT `endoplasmic reticulum` against `endoplasmic reticulum membrane`, and APP NOT `dendrite` against `dendritic spine`.

**Provenance.** [GOC+]. GOC states downward propagation. The placement procedure is ours. [wiki: Elements of an annotation](https://wiki.geneontology.org/index.php/Elements_of_an_annotation); [go-annotation#1761](https://github.com/geneontology/go-annotation/issues/1761).

<a id="qn-10"></a>

### QN-10. A positive and a NOT annotation to the same term may coexist only when the literature genuinely conflicts or the claims concern different gene products (isoforms). The reviewer must reconcile each pair in writing and narrow the NOT where the conflict is only apparent.

**Rationale.** GO allows the pair. It has been confirmed on the tracker ([go-annotation#1761](https://github.com/geneontology/go-annotation/issues/1761)) and in the wiki ("Both positive and NOT statements can be used in cases where there is conflicting experimental findings"). But as a pair of logical statements they cannot both be true of the same entity, so each pair is either a real dispute, a scope mismatch or an isoform difference.

**Resolution procedure.**

1. *Isoform.* If one row was made on an isoform (`isoform: P19544-1`), record the isoform on both. The pair is then consistent. The 2022 PAINT review found that many mammalian NOT-versus-IBA conflicts came from NOTs made on splice variants ([Drive: Review NOT annotation in PAINT (2022)](https://drive.google.com/open?id=1Db0k2fuFzWYNoiHVGamYlJuhPm3bAku0)).
2. *Scope.* If the NOT excludes a general form of the activity and the positive shows a specific form, the NOT is too broad. Move it to the descendant the evidence excludes ([QN-9](#qn-9)). If no descendant expresses the distinction, keep both, explain the distinction in each `reason`, and record an ontology gap.
3. *Real conflict.* Decide which result is better supported (methods, replication, later papers). Keep that row. REMOVE the other only if the later evidence refutes it; otherwise mark it UNDECIDED. Do not resolve the conflict by deleting the NOT simply because a positive exists.

**Worked example (COQ8B).** `genes/human/COQ8B` has `enables` GO:0004672 protein kinase activity (IDA, PMID:38425362: COQ3 is phosphorylated by reconstructed ancestral COQ8B in vitro) and `NOT enables` GO:0004672 (IDA, PMID:27499294: no canonical kinase activity in trans). The review keeps both and reconciles them in prose: the NOT concerns general activity in trans, the positive one substrate. GO cannot express the distinction. NOT with a `has_input` extension is disallowed ([QN-12](#qn-12)), and no GO term describes "kinase activity on general substrates in trans". This is an expressivity gap, not a curation error.

**Provenance.** [GOC+]. Coexistence is GOC policy; the three-way procedure is ours. [wiki: Elements of an annotation](https://wiki.geneontology.org/index.php/Elements_of_an_annotation); [go-annotation#1761](https://github.com/geneontology/go-annotation/issues/1761); [ISOFORMS](../../ISOFORMS.md); [CLAUDE.md](../../../CLAUDE.md) (isoform and negation tracking).

<a id="qn-11"></a>

### QN-11. A NOT to a molecular function is the strongest use of the qualifier. A NOT to a process needs evidence that the gene product was unable to do the process's work.

**Rationale.** The repo audit of all 10,622 GOA NOT rows (2026-10-01) found the useful end of NOT concentrated in MF: 4,664 MF rows, 3,405 of them catalytic, mostly IBA, IDA and IKR. These are pseudoenzymes and diverged paralogues. Process NOTs drift toward phenotype and expression nulls. UniProt CAUTION notes follow the same split: 19.5% of reviewed proteins with an MF NOT carry a loss-of-activity CAUTION, against 1.9% of proteins whose NOTs are only to processes or locations ([NOT_ANNOTATION_USAGE](../../NOT_ANNOTATION_USAGE.md)).

**Rule detail.** A process NOT is acceptable when it is really an activity negative stated as a process. CRY2 NOT photoreactive repair is one. So is "NOT response to X" for a receptor shown not to bind and transduce X. "NOT response to X" for an abundance or expression null is not acceptable.

**Provenance.** [NEW], drawn from the repo audit's draft guidance; GOC has no aspect-specific bar. [NOT_ANNOTATION_USAGE](../../NOT_ANNOTATION_USAGE.md).

<a id="qn-12"></a>

### QN-12. Do not attach an annotation extension to a NOT annotation.

**Rationale.** An extension narrows the term, so "NOT X has_input(Y)" would claim only that the product does not do X *to Y*. In practice curators have used it to mean "under these conditions X does not happen", which hides a condition inside a negation. That is the reason GO deprecated `independent_of` and `in_absence_of` ([wiki: Annotation Extension Relation:independent of](https://wiki.geneontology.org/index.php/Annotation_Extension_Relation%3Aindependent_of)). The current wiki forbids NOT with extensions ([wiki: Elements of an annotation](https://wiki.geneontology.org/index.php/Elements_of_an_annotation)), and a reply on [go-annotation#2326](https://github.com/geneontology/go-annotation/issues/2326) says this is enforced through error logs. GO's rule registry nevertheless records gorule-0000053 ("NOT annotation should not have extension") as *deprecated, will not be implemented*. The stated reason is that negated extended annotations are logically well-formed ([Drive: Feedback on GO rules (FlyBase copy)](https://drive.google.com/open?id=1AiEBQGA37oyyoFmDYNexYOlDIwqPHnMvAESIVqgjxFM)). We follow the wiki.

**Example.** A kinase active on substrate A and inactive on substrate B: annotate `enables` GO:0004672 with `has_input`(A). Do not add NOT GO:0004672 `has_input`(B). If inactivity on B matters biologically, say so in a GO-CAM or in prose.

**Provenance.** [GOC] (wiki), noting the conflicting rule registry. See Differences.

<a id="qn-13"></a>

### QN-13. Do not make NOT annotations to binding terms.

**Rationale.** gorule-0000002 filters NOT annotations to GO:0005515 protein binding, and the 2024 rules update extended the filter to GO:0005488 binding ([Drive: GO rules (2024-05 GOC meeting)](https://drive.google.com/open?id=1CmnWtTKkx8Qo3e7XNEFfafZYTGTrJq7DcqRVBdB7lzM)). Failure to bind one partner in one assay is not a property worth negating, and the bare binding terms are uninformative even when positive. A specific binding term with a functional consequence can still be negated when a reader would expect it. Example: NOT GO:0005544 calcium-dependent phospholipid binding for a synaptotagmin that has lost its calcium-binding residues.

**Provenance.** [GOC+]. GOC filters GO:0005515 and GO:0005488. Allowing specific binding children is our reading of where the rule stops.

<a id="qn-14"></a>

### QN-14. A NOT needs a positive annotation in the same aspect, the ND root if nothing else is known. A NOT row does not make an ND row stale.

**Rationale.** A NOT says what the product does not do and nothing about what it does. The ND wiki requires a positive annotation alongside every NOT, using the root term with ND when nothing else is known ([wiki: ND evidence code](https://wiki.geneontology.org/index.php/No_biological_Data_available_%28ND%29_evidence_code)). The repo's ND policy ([CLAUDE.md](../../../CLAUDE.md); [NO_DATA](../../NO_DATA.md)) asks whether literature on the gene *identifies a function* in the aspect. A NOT identifies an absence, so it does not make a co-existing ND stale, any more than a bare protein-binding IPI does.

**Example.** A pseudokinase with `NOT enables` GO:0004672 (IKR) and no known activity should also carry GO:0003674 molecular_function (ND). Accept the ND row if the literature search shows no positive function.

**Provenance.** [GOC] for the pairing; [GOC+] for the ND-staleness reading.

<a id="qn-15"></a>

### QN-15. Use NOT to stop propagation of a lost activity, and know how PAINT treats NOT.

**Rationale.** A REMOVE in one review cleans one row, and the next IEA or IBA run reasserts it. A NOT filed upstream, together with an IKR or IRD loss on the PAINT node, stops the reassertion ([TOP_NOTS](../../TOP_NOTS.md)). Reviewers need the PAINT logic to read the IBA rows they meet.

**PAINT logic, current and historical.**

- *2014 rules* ([wiki: 11 MAR 2014 PAINT Conference Call](https://wiki.geneontology.org/index.php/11_MAR_2014_PAINT_Conference_Call)): a NOT propagates only to the term annotated, never to parents. When positive and NOT experimental annotations meet at the same level, or a positive on a specific term meets a NOT on a general one, the NOT is ignored and the positive propagates. A positive general term still propagates into a clade where a specific child is blocked. Experimental NOTs inside a clade did not stop propagation automatically, but conflicting leaves were silently skipped.
- *2021 change* ([wiki: 31 Aug 2021 PAINT Conference Call](https://wiki.geneontology.org/index.php/31_Aug_2021_PAINT_Conference_Call)): the PAINT tool propagates IBA to leaves that carry a conflicting experimental NOT and highlights the conflict, and the curator must block it with IKR or IRD. The call recorded concerns about curation load and agreed to keep the older script-based release until conflicts could be reviewed. Which behaviour produces a given release has to be checked against the PAINT README.
- *Loss codes.* Use IKR (ECO:0000320) when the residues that define the activity are lost, and IRD (ECO:0000321 rapid divergence from ancestral sequence evidence used in manual assertion) for divergence without a residue-level explanation ([go-annotation#2109](https://github.com/geneontology/go-annotation/issues/2109)). An IRD produces no leaf row, so the repo tool `gene_paint_losses` lists the losses on a gene's lineage for review.
- *Conflict sources* ([Drive: Review NOT annotation in PAINT (2022)](https://drive.google.com/open?id=1Db0k2fuFzWYNoiHVGamYlJuhPm3bAku0)): among paralogues after a duplication, conflicts usually mean rapid divergence or loss of active sites, and PAINT should place a loss. In mammals they usually mean an isoform-based NOT ([QN-10](#qn-10)). Within one gene, they should be resolved at literature curation.

**Review procedure.** When an IBA contradicts a curated NOT on the same gene, do not ACCEPT the IBA by deference ([CLAUDE.md](../../../CLAUDE.md), IBA section). Check whether the NOT is isoform-scoped. If it is not, and the NOT is sound, REMOVE the IBA row and record the needed IKR or IRD as the PAINT fix (`paint_action: ADD_IKR` or `ADD_IRD` in a family review). The `Hyal2` case in [NAKED_MOLE_RAT](../../NAKED_MOLE_RAT.md), a virus-receptor term propagated from a donor set that contains a curated NOT for the same term, is the pattern.

**Proposing a new NOT (repo).** A review cannot file a NOT upstream directly. When a REMOVE rests on demonstrated absence (pseudoenzyme, catalytic residues lost, assay-negative), say so in `reason` with the evidence. The [TOP_NOTS](../../TOP_NOTS.md) scan collects such rows as candidates for submission.

**Provenance.** [GOC] for the PAINT rules; [GOC+] for the review procedure.

<a id="qn-16"></a>

### QN-16. Review an existing NOT row as a claim of absence: ACCEPT, MODIFY (narrow the term or fix the isoform), REMOVE or UNDECIDED. Do not mark it non-core, over-annotated or too general.

**Rationale.** Core and non-core describe functions, and a NOT is not a function. "Over-annotated" and "too general" have no clear meaning for a negation. A NOT on a general term is the *strongest* negation, so a broad NOT is an error of scope that MODIFY should fix. The rule mirrors the repo's ND rule. The repo's reviews have been deferential so far: of 270 negated rows in 174 reviews, 223 were ACCEPTed, 20 UNDECIDED, 16 KEEP_AS_NON_CORE and 8 REMOVEd ([NOT_ANNOTATION_USAGE](../../NOT_ANNOTATION_USAGE.md)).

**Rule detail.**

- ACCEPT when [QN-8](#qn-8) is met and the term is at the right level.
- MODIFY to a descendant when the NOT is too high ([QN-9](#qn-9)), or to add the isoform.
- REMOVE when the evidence is a negative or inconclusive result, an expression or abundance null, or a non-expected absence.
- UNDECIDED when the full text cannot be checked and the abstract does not settle it. The repo's rule against overruling curators from abstracts applies to NOTs too.

**Provenance.** [NEW]. See Open questions.

## Decision aid

**Picking a relation**

| Question | Yes | No |
|---|---|---|
| MF: does this subunit alone (or as a homomer) carry the activity? | `enables` | next |
| MF: is it part of an irreducible active core with the other subunits? | `contributes_to` (all core subunits) | Give the accessory subunit its own MF (adaptor, regulator), or no MF |
| BP: can you name the MF, and is it a step in the process? | `involved_in` | next |
| BP: does the gene regulate the process through a known MF? | `involved_in` "regulation of X" | next |
| BP: is the mechanism known and the activity outside the process? | `acts_upstream_of, positive/negative effect` | `acts_upstream_of_or_within, positive/negative effect` |
| CC: is the term a protein-containing complex? | `part_of` | next |
| CC: was the activity shown in the location? | `is_active_in` | `located_in` (or nothing, if only in transit) |

**Should this be a NOT?**

| Evidence | NOT? |
|---|---|
| Activity assay negative, with a reason to expect activity (family, domain, paralogue) | Yes, to the MF |
| Catalytic residues lost, shown on an alignment | Yes, IKR |
| Knockout has no phenotype for process P | No |
| Not detected in compartment C | No |
| Expression or abundance unchanged after stimulus S | No, never with IEP |
| Inactive on substrate B, active on substrate A | No NOT. Use the positive with `has_input`(A) |
| Isoform 2 lacks the activity of isoform 1 | Yes, NOT on isoform 2 with the isoform id |
| Does not bind partner Y | No (binding NOT filtered) |

## Common errors

| Error | How to recognise it | Fix |
|---|---|---|
| `enables` on a non-catalytic subunit for the complex's activity | Subunit is regulatory, scaffold or assembly factor (SURF1 with GO:0004129) | REMOVE, and give it its own MF, or `contributes_to` if it is in the core |
| `contributes_to` on every member of a large complex | Annotation lists peripheral or regulatory subunits | REMOVE from non-core subunits |
| `involved_in` from a mutant phenotype | IMP or IGI only, no MF known | MODIFY to `acts_upstream_of_or_within` with direction (relation-only pattern) |
| Direction relation stacked on a regulation term | `acts_upstream_of, positive effect` "positive regulation of X" | MODIFY to `involved_in` the regulation term |
| `is_active_in` a transit compartment | Secretory or plasma-membrane protein `is_active_in` ER or Golgi | MODIFY to `located_in`, or REMOVE per [ORGANELLES](../../ORGANELLES.md) |
| `located_in` a complex | CC term below GO:0032991 | MODIFY relation to `part_of` |
| NOT from a negative result | "not required", "no phenotype" | REMOVE |
| NOT from IEP | Evidence IEP, term "response to..." | REMOVE |
| NOT on an ancestor of a positive term | Consistency warning (DNM1L NOT ER vs ER membrane) | MODIFY the NOT down to the excluded sibling |
| NOT with an extension | Column 16 non-empty on a NOT row | Remove the extension. If the NOT is then false, REMOVE it |
| Relation fixed only in prose | Review text argues for `contributes_to`, structured row still `enables` | MODIFY plus NEW relation-only row |
| Repo schema misreading | The `AnnotationQualifierEnum` description says `acts_upstream_of` is "acts upstream of or within" | Use the RO definitions in the table above. The enum text is wrong (see Open questions) |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [wiki: Annotation Relations](https://wiki.geneontology.org/index.php/Annotation_Relations) vs [Drive: GP2term deck (2021)](https://drive.google.com/open?id=128U6g91Iv2ej9pcgTSGOowbhjp4GwGXmE4gDTiue1Cc), [Drive: GAF 2.2 migration (2021)](https://drive.google.com/open?id=1E9Fd38LPle2RcQgbJ9kzF3vjC81lMqSeFIQRUFPTxsE) and [Drive: Draft GAF 2.2 documentation](https://drive.google.com/open?id=1Jbpm1l5xjSabywE6ulIflujcESkdkQvlVI7bECgLbtw) | Wiki: BP default is `acts_upstream_of_or_within`. Protein2GO and GOA: default `involved_in`. GAF 2.2 draft: each group chooses | Read an unqualified BP row as `acts_upstream_of_or_within`. Assert `involved_in` only with a nameable MF | The sources conflict. Only the weakest relation is always true, and the GOA default inflates phenotype-based rows into participation claims |
| [wiki: 5 May 2020 PAINT Conference Call](https://wiki.geneontology.org/index.php/5_May_2020_PAINT_Conference_Call) | PAINT ignores seed relations; all IBA BP rows are `involved_in` | Reviewers read an IBA `involved_in` no more strongly than its seeds | Otherwise IBA turns `acts_upstream_of_or_within` seeds into participation claims |
| [wiki: Colocalizes with](https://wiki.geneontology.org/index.php/Colocalizes_with) | Deprecated, "existing annotations are under review"; no procedure | Conversion table ([QN-5](#qn-5)); no new rows | GO gave no procedure, and reviewers meet these rows now |
| Repo schema `AnnotationQualifierEnum` | `colocalizes_with` "weaker than located_in"; `acts_upstream_of` described as "upstream of or within" | RO definitions; `colocalizes_with` deprecated | Schema text predates or misreads GO |
| [wiki: Elements of an annotation](https://wiki.geneontology.org/index.php/Elements_of_an_annotation) and [go-annotation#2326](https://github.com/geneontology/go-annotation/issues/2326) vs gorule-0000053 status ([Drive: Feedback on GO rules](https://drive.google.com/open?id=1AiEBQGA37oyyoFmDYNexYOlDIwqPHnMvAESIVqgjxFM)) | Wiki: no NOT with extensions. Rule registry: the rule forbidding it is deprecated, "will not be implemented" | No NOT with extensions | The wiki is newer (2026) and the safer reading. Hidden conditions inside negations do not fold |
| Old qualifier documentation, quoted in [go-annotation#2237](https://github.com/geneontology/go-annotation/issues/2237) | NOT may be used when a paper says "not found in the nucleus" | Never for "not found in" | Removed by GO in 2019; restated here because legacy rows of this kind persist |
| [wiki: Elements of an annotation](https://wiki.geneontology.org/index.php/Elements_of_an_annotation) | No aspect distinction for NOT | MF NOTs are the strongest. Process NOTs need a test of the process's work. IEP never supports a NOT | Repo audit: process NOTs from expression nulls are the main misuse (169 IEP-only rows) |
| [wiki: 11 MAR 2014 PAINT Conference Call](https://wiki.geneontology.org/index.php/11_MAR_2014_PAINT_Conference_Call) vs [wiki: 31 Aug 2021 PAINT Conference Call](https://wiki.geneontology.org/index.php/31_Aug_2021_PAINT_Conference_Call) | 2014: conflicting leaves skipped silently. 2021 tool: IBA propagated to conflicting leaves unless blocked by IKR or IRD, with the old script kept for release | Treat an IBA contradicting a curated NOT as a review flag and resolve it explicitly ([QN-15](#qn-15)) | Which rule produced a release varies, so the row has to be checked |
| [wiki: Contributes to](https://wiki.geneontology.org/index.php/Contributes_to) | RNA polymerase II example uses GO:0001055 | Use a current term. GO:0001055 is now obsolete ("obsolete RNA polymerase II activity" in the local GO build) | Example term obsoleted |
| [go-annotation#2109](https://github.com/geneontology/go-annotation/issues/2109) | IRD used to "block" propagation even when residue loss is known | IKR when residues are lost, IRD only for divergence without residue evidence | IKR carries the reason, and gorule-0000042 requires NOT on it |
| None (gap) | No guidance on review actions for NOT rows | ACCEPT, MODIFY, REMOVE, UNDECIDED only ([QN-16](#qn-16)) | "Non-core" and "over-annotated" are undefined for a negation |
| None (gap) | No procedure for relation-only corrections | MODIFY plus NEW with the corrected qualifier ([QN-7](#qn-7)) | Keeps the true claim and makes the correction machine-readable |

## Open questions

1. **BP default.** Should GOC make `acts_upstream_of_or_within` the export default for BP rows that carry no asserted relation, including GOA's legacy rows and PAINT IBAs? That would make the files match the wiki.
2. **Scoped negation.** The COQ8B case (no activity in trans, activity on one substrate) cannot be expressed: NOT with `has_input` is disallowed and no term carries the distinction. Should GO allow NOT with `has_input` for the narrow substrate case that [go-annotation#2326](https://github.com/geneontology/go-annotation/issues/2326) proposed, or create terms, or accept the gap?
3. **gorule-0000053.** The rule registry and the wiki disagree on NOT with extensions. Which one governs pipelines?
4. **NOT on specific binding children.** gorule-0000002 covers GO:0005515 and GO:0005488. Are children such as GO:0005544 calcium-dependent phospholipid binding in or out?
5. **PAINT release behaviour.** Which propagation rule (2014 silent skip, or 2021 propagate-and-block) produces current IBA releases? Reviewers cannot tell from the row.
6. **Repo schema.** The `AnnotationQualifierEnum` descriptions should be corrected to the RO definitions, and `colocalizes_with` marked deprecated. That is a schema change and needs its own PR.
7. **Review actions on NOT rows.** [QN-16](#qn-16) excludes KEEP_AS_NON_CORE for NOTs. Sixteen existing repo rows use it. A sweep is a separate pass, and the validator could warn, as `nd_policy` does for ND rows.
8. **Proposing NOT in a review.** The repo has no structured way to propose a new NOT annotation, since `NEW` adds positive claims. Should the schema allow `NEW` with `negated: true` under the [QN-8](#qn-8) bar, or should NOT proposals stay in TOP_NOTS?

## Sources

**GO wiki**
- [wiki: Annotation Relations](https://wiki.geneontology.org/index.php/Annotation_Relations) (reviewed 2023-09-05)
- [wiki: Elements of an annotation](https://wiki.geneontology.org/index.php/Elements_of_an_annotation) (reviewed 2026-03-29)
- [wiki: Enables](https://wiki.geneontology.org/index.php/Enables); [wiki: Contributes to](https://wiki.geneontology.org/index.php/Contributes_to); [wiki: Involved in](https://wiki.geneontology.org/index.php/Involved_in); [wiki: Acts upstream of](https://wiki.geneontology.org/index.php/Acts_upstream_of); [wiki: Acts upstream of or within](https://wiki.geneontology.org/index.php/Acts_upstream_of_or_within); [wiki: Is active in](https://wiki.geneontology.org/index.php/Is_active_in); [wiki: Located in](https://wiki.geneontology.org/index.php/Located_in); [wiki: Colocalizes with](https://wiki.geneontology.org/index.php/Colocalizes_with)
- [wiki: ND evidence code](https://wiki.geneontology.org/index.php/No_biological_Data_available_%28ND%29_evidence_code)
- [wiki: Annotation Extension Relation:independent of](https://wiki.geneontology.org/index.php/Annotation_Extension_Relation%3Aindependent_of) (deprecated)
- [wiki: 11 MAR 2014 PAINT Conference Call](https://wiki.geneontology.org/index.php/11_MAR_2014_PAINT_Conference_Call); [wiki: 16 December 2014 PAINT Conference Call](https://wiki.geneontology.org/index.php/16_December_2014_PAINT_Conference_Call); [wiki: 5 May 2020 PAINT Conference Call](https://wiki.geneontology.org/index.php/5_May_2020_PAINT_Conference_Call); [wiki: 31 Aug 2021 PAINT Conference Call](https://wiki.geneontology.org/index.php/31_Aug_2021_PAINT_Conference_Call)

**GO Consortium Drive**
- [Drive: Annotation relations - Guidelines for P2GO](https://drive.google.com/open?id=1DXdjAuNf7u8CKXYlgW5kyzPgq7vnp-Aai0S5Sh63guc)
- [Drive: Use of relations for GO annotation - GP2term and extensions (2021)](https://drive.google.com/open?id=128U6g91Iv2ej9pcgTSGOowbhjp4GwGXmE4gDTiue1Cc)
- [Drive: Draft GOC GAF 2.2 documentation for gp2term relations](https://drive.google.com/open?id=1Jbpm1l5xjSabywE6ulIflujcESkdkQvlVI7bECgLbtw) (draft); [Drive: Heuristics for gp2term relations](https://drive.google.com/open?id=1GSLdTrBVdSyaWU4R0L3M0Y-rrNRW22aoYFBh_nwAwC0); [Drive: Legacy Annotations and New Qualifiers](https://drive.google.com/open?id=1VJx9mJMvWfUEVF9vCmwhDY2NwgvHsWf3tRgKFluZLa8)
- [Drive: Contributes_to (GOC 2021)](https://drive.google.com/open?id=1g-2M8XQuINGN6eKVT0Sqm1OsudF_kM2D4jemv-izTks)
- [Drive: Response to "evaluate GO prediction methods" Q from Biostars 2023](https://drive.google.com/open?id=1EodZspmExNTEu8c9Gzs6wpUZ4RWwj3aMlmk3TyAc4Bs) (draft reply)
- [Drive: March 2021 migration to GAF2.2 and GPAD2.0](https://drive.google.com/open?id=1E9Fd38LPle2RcQgbJ9kzF3vjC81lMqSeFIQRUFPTxsE)
- [Drive: Review NOT annotation in PAINT (2022 GOC meeting)](https://drive.google.com/open?id=1Db0k2fuFzWYNoiHVGamYlJuhPm3bAku0)
- [Drive: Reviewing colocalizes_with annotations (2023 Padua breakout)](https://drive.google.com/open?id=1T9ww92HdP291B7tbeqAD91xvTPxdwwjM9bHJwh6d56o)
- [Drive: Feedback on GO rules (FlyBase copy)](https://drive.google.com/open?id=1AiEBQGA37oyyoFmDYNexYOlDIwqPHnMvAESIVqgjxFM)
- [Drive: GO rules (2024-05 GOC meeting)](https://drive.google.com/open?id=1CmnWtTKkx8Qo3e7XNEFfafZYTGTrJq7DcqRVBdB7lzM)

**GitHub issues (geneontology/go-annotation)**
- [go-annotation#3](https://github.com/geneontology/go-annotation/issues/3) (use of NOT, 2003)
- [go-annotation#1761](https://github.com/geneontology/go-annotation/issues/1761) (POLA1 NOT scope)
- [go-annotation#2109](https://github.com/geneontology/go-annotation/issues/2109) (IKR vs IRD)
- [go-annotation#2237](https://github.com/geneontology/go-annotation/issues/2237) (NOT documentation)
- [go-annotation#2326](https://github.com/geneontology/go-annotation/issues/2326) (NOT with extensions)
- [go-annotation#2377](https://github.com/geneontology/go-annotation/issues/2377) (BP qualifiers)
- [go-annotation#6414](https://github.com/geneontology/go-annotation/issues/6414) (SDH `contributes_to`)

**Repository**
- [CLAUDE.md](../../../CLAUDE.md) (participation test for NEW, isoform and negation tracking, ND policy, IBA reading)
- [NOT_ANNOTATION_USAGE](../../NOT_ANNOTATION_USAGE.md); [TOP_NOTS](../../TOP_NOTS.md); [SDH_GP2TERM_CONTRIBUTES_TO](../../SDH_GP2TERM_CONTRIBUTES_TO.md); [ISOFORMS](../../ISOFORMS.md); [ORGANELLES](../../ORGANELLES.md); [NO_DATA](../../NO_DATA.md); [IBA_REVIEW](../../IBA_REVIEW.md); [PAINT](../../PAINT.md); [NAKED_MOLE_RAT](../../NAKED_MOLE_RAT.md)
- [action consistency](../../../docs/action_consistency.md)
- Gene reviews cited: `genes/human/COQ8B`, `genes/human/FGFR4`
