# Annotation extensions: GO annotation guidelines

Status: draft v0.1 (2026-11-15) · Part of [GO_GUIDELINES](../../GO_GUIDELINES.md)

**In brief:**

- An extension narrows the GO term. "Term plus extension" must name a subclass of the term, and the annotation must stay true if the extension is deleted. Extensions do not express conditions, negation or causal chains.
- Use only a small set of relations: `has_input` / `has_output` for the specific molecular target or product, `occurs_in` for where an MF or BP happens, `part_of` for the process an MF serves or the cell a CC sits in, `happens_during` for a phase or life stage, and the `results_in_...` family for developmental processes. Do not use `has_regulation_target`, `occurs_at`, `has_direct_input`, `activated_by`, `independent_of` or chained relations in new annotations.
- An extension that restates the term is noise. Do not add `has_input` hexose to hexokinase activity, `occurs_in` T cell to T cell receptor signaling, or `part_of` phosphorylation to kinase activity.
- `part_of(Y)` is not a home for a retired "X involved in Y" term. If GO obsoleted the precomposition and asked for a GO-CAM, put Y in a model, the gene's core functions, or nowhere.
- A standard annotation is one line with one evidence and no nested or causal extensions. Anything that needs two linked activities is a GO-CAM.
- In this repository the cached GOA file has no extension column, so read the row's extension in QuickGO or GOA before calling it too general.

## Scope

This document covers annotation extensions on standard GO annotations: GAF column 16 and the GPAD 2.0 extension column, written as `relation(ID)` with comma for "and" and pipe for "or". It covers their purpose, the relations allowed for each aspect and the ontologies they draw on, the choice between an extension and a new precomposed term, how extensions relate to GO-CAM, how to review rows that carry them, and the history of the allowed-relation list.

Out of scope: the gene product-to-term relation in column 4 (see [qualifiers-and-negation.md](qualifiers-and-negation.md)); relations between activities in GO-CAM (see [gocam-modeling.md](gocam-modeling.md)); `with/from` usage (see [evidence-codes.md](evidence-codes.md)); term-request policy in general (see [ontology-change-and-taxa.md](ontology-change-and-taxa.md)).

## Principles

**Extensions are post-composition.** The GO cannot hold a term for every substrate, cell type or stage, so the annotation can build the class at curation time: "protein serine/threonine kinase activity *with input* MCM2" is a class nobody has to request. The 2014 description of extensions presents them as recording effector-target relationships (substrates, regulation targets, localisation dependencies) and spatial and temporal context ([PMID:24885854](https://europepmc.org/article/MED/24885854), "A method for increasing expressivity of Gene Ontology annotations using a compositional approach").

**The extension modifies the term, not the gene product.** The extension field extends the GO term in column 5 and does not extend the gene product ([Drive: Annotation Extension Sept 2017 (GOC Cambridge)](https://drive.google.com/open?id=0B_c5g4FezmhfVElqaU9vT2lwbEk)). Because the term plus extension is a class, it can be "folded" into a named term later. When GO adds the precomposed term, the annotation maps forward without curator work ([wiki: Column 16: Function x Process x Component extensions](https://wiki.geneontology.org/index.php/Column_16%3A_Function_x_Process_x_Component_extensions)). Any extension that cannot fold, because it states a condition or a negation, is malformed. That is why `independent_of` and `in_absence_of` were deprecated ([wiki: Annotation Extension Relation:independent of](https://wiki.geneontology.org/index.php/Annotation_Extension_Relation%3Aindependent_of)).

**Context is not exclusivity.** `occurs_in(CL:0000746 cardiac muscle cell)` says that in this experiment the activity was seen in cardiac muscle cells. It does not say the activity happens only there, and a missing extension does not say it happens everywhere ([wiki: Annotation Extension: Capturing cell and tissue types](https://wiki.geneontology.org/index.php/Annotation_Extension%3A_Capturing_cell_and_tissue_types)).

**Standard annotations and GO-CAMs are separate data models.** As of 2026 GO is separating the two stores. A standard annotation has evidence cardinality 1, may carry independent (pipe) and dependent (comma) extensions, and has no nested extensions. Chained extensions such as `regulates_o_occurs_in` that cannot be flattened will be archived ([Drive: GO-CAMs and standard annotations in Noctua (Fall 2026 GOC)](https://drive.google.com/open?id=1CY1Py4e9jTSXDn_mircd-C3aVLHqNJ2x3BvH90EKFj8)). Extensions have become the contextual layer of a single statement, and mechanisms belong in models.

## The allowed relations

Ids were checked against RO with `runoak -i sqlite:obo:ro info`. "Allowed" reflects the Noctua Standard Annotation Editor (SAE) specification and the 2022 relation review ([Drive: SAE - Annotation Extension Relations specs](https://drive.google.com/open?id=1mBzbiqey0fyFUhWtKE5UKvIPNvpJ2Kx1XNkPgCPorpc); [Drive: Annotation Extension Relations - 2022-09-09](https://drive.google.com/open?id=13MOVlRD1_iBJyw7whO7lK0KTCaLW0dbbtcpgGOthKqA)), reconciled with the wiki relation pages.

| Relation | Id | On | Range (filler) | Use for |
|---|---|---|---|---|
| `has_input` | RO:0002233 | MF, BP | Gene/gene product id (UniProtKB, MOD, RNAcentral, PR), CHEBI chemical entity, GO:0032991 complex | The specific molecular target: enzyme substrate, binding partner, transcription factor target gene, the regulated gene product for a regulator activity |
| `has_output` | RO:0002234 | MF, BP | CHEBI, complex, gene product | The specific product of a reaction or process |
| `occurs_in` | BFO:0000066 | MF, BP | GO CC (GO:0110165 cellular anatomical structure), CL, UBERON, species anatomy (EMAPA, FBbt, WBbt, ZFA, PO...) | Where the activity or the whole process takes place |
| `part_of` | BFO:0000050 | MF | GO BP | The process an activity is a step in |
| `part_of` | BFO:0000050 | CC (not complexes) | CL, UBERON, species anatomy | The cell or tissue in which the component sits |
| `happens_during` | RO:0002092 | MF (BP: see Differences) | GO:0044848 biological phase descendants, UBERON:0000105 life cycle stage descendants, plant development stages | The phase or stage when the activity occurs |
| `existence_overlaps`, `existence_starts_and_ends_during` | RO:0002490, RO:0002491 | CC | GO BP, life stage | The stage or process during which a localisation is observed. Successors to the legacy `exists_during` |
| `results_in_development_of`, `..._formation_of`, `..._morphogenesis_of`, `..._maturation_of`, `..._growth_of` and siblings | e.g. RO:0002296 | BP | CL, UBERON, species anatomy | The structure a developmental process acts on |
| `transports_or_maintains_localization_of` | RO:0002313 | MF, BP | Gene product, complex, chemical | The cargo of a transport or localisation process |
| `has_target_start_location`, `has_target_end_location` | RO:0002338, RO:0002339 | MF, BP | GO CC, anatomy | Origin and destination of a transport |
| `acts_on_population_of` | RO:0012003 | BP | CL, organism | The population acted on, e.g. a cell type whose proliferation is controlled |
| `adjacent_to`, `overlaps` | — | CC | anatomy | Rare refinements of a location |

**Not for new annotations.**

| Relation | Status | Replace with |
|---|---|---|
| `occurs_at` | Deprecated 2019 ([go-annotation#2584](https://github.com/geneontology/go-annotation/issues/2584)) | `occurs_in` for GO CC or CL fillers; for SO motifs, a specific DNA-binding term with `has_input` the gene, or drop; drop Pfam fillers |
| `has_direct_input` | Merged into `has_input` (2020) ([wiki: Annotation Conf. Call 2020-02-04](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2020-02-04); [go-annotation#2076](https://github.com/geneontology/go-annotation/issues/2076)) | `has_input` |
| `activated_by`, `inhibited_by` | Retired 2019 ([wiki: Annotation Conf. Call 2019-11-19](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2019-11-19)) | A binding annotation for the regulator plus a causal link in GO-CAM; for a binding term, `has_input` the bound entity; drop it if the mechanism is unknown |
| `independent_of`, `in_absence_of` | Deprecated (hidden negation, does not fold) | Nothing |
| `has_regulation_target` | Legacy, ambiguous; GOC's own description calls it "very general" ([Drive: Annotation Extension Sept 2017](https://drive.google.com/open?id=0B_c5g4FezmhfVElqaU9vT2lwbEk)); converted to `has_input` on import ([wiki: Noctua MOD Imports](https://wiki.geneontology.org/index.php/Noctua_MOD_Imports)); absent from the SAE list | `has_input` on the regulation term |
| `has_agent` | Under review since 2020; no replacement agreed ([wiki: Ontology meeting 2020-08-24](https://wiki.geneontology.org/index.php/Ontology_meeting_2020-08-24)) | `occurs_in` or `acts_on_population_of` where one fits; otherwise a GO-CAM |
| `regulates_o_occurs_in` and other chains | To be archived in the 2026 data-store split | A GO-CAM |
| Causal relations (`causally_upstream_of...`, `directly_positively_regulates`...) in extensions | Allowed by the SAE but flagged "Causal - can we remove from AE?" in the 2022 review; `causally_upstream_of_or_within` is never to be used directly ([wiki: Causally upstream of or within](https://wiki.geneontology.org/index.php/Causally_upstream_of_or_within)) | A GO-CAM |

## Rules

<a id="ae-1"></a>

### AE-1. An extension must narrow the term, so that the annotation stays true without it. Do not use extensions for conditions, negation or exclusivity.

**Rationale.** Folding works only if term plus extension is a subclass of the term. "Protein localization to nucleus `happens_during` mitotic anaphase" folds to a term that would be a child of GO:0034504 protein localization to nucleus ([wiki: Happens during](https://wiki.geneontology.org/index.php/Happens_during)). "Positive regulation of NF-kappaB signaling `independent_of` peptidase activity" folds to nothing.

**Test.** Delete the extension. If the remaining annotation is false, the extension was carrying the claim. Usually that means a NOT or condition was hidden in it, and the row is wrong. If the annotation is true but now says less, the extension is legitimate.

**Corollary.** Never combine an extension with NOT ([QN-12](qualifiers-and-negation.md#qn-12)).

**Provenance.** [GOC]. [wiki: Annotation Extension Relation:independent of](https://wiki.geneontology.org/index.php/Annotation_Extension_Relation%3Aindependent_of); [wiki: Elements of an annotation](https://wiki.geneontology.org/index.php/Elements_of_an_annotation).

<a id="ae-2"></a>

### AE-2. Use comma for facts that hold together and pipe for independent statements. Make separate annotations for alternative substrates or targets.

**Rationale.** A comma group is one class: "calcium ion sequestering activity, `occurs_in` sarcoplasmic reticulum, `occurs_in` cardiac muscle cell". A pipe gives independent extensions on the same term. Several `has_input` fillers in one comma group mean several inputs *of one reaction*. An enzyme with alternative substrates, or a transcription factor with several targets, needs one annotation (or one pipe-separated group) per target ([wiki: Has input](https://wiki.geneontology.org/index.php/Has_input)).

**Example.** CASQ2 (O14958) `enables` GO:0140314 calcium ion sequestering activity, `occurs_in`(GO:0016529 sarcoplasmic reticulum), `occurs_in`(CL:0000746 cardiac muscle cell), IMP, PMID:16908766 ([wiki: Occurs in](https://wiki.geneontology.org/index.php/Occurs_in)). Nested locations go in one comma group. Distinct locations go in separate groups.

**Provenance.** [GOC]. [Drive: Noctua Standard Annotations evidence splitting](https://drive.google.com/open?id=1p2pwOCovVbX61bQspUcptSt2pkA3OSzDHulOpQhZElQ); [Drive: Annotation Extension Sept 2017](https://drive.google.com/open?id=0B_c5g4FezmhfVElqaU9vT2lwbEk).

<a id="ae-3"></a>

### AE-3. Use `has_input` for the specific, physiologically relevant molecular target that the term does not already name: a substrate, a binding partner, a target gene, or the gene product a regulator acts on.

**What to capture.**

- Enzyme substrates more specific than the term. Human DGKA `enables` GO:0004143 ATP-dependent diacylglycerol kinase activity, `has_input` 1-O-palmityl-2-acetyl-sn-glycerol (CHEBI:75936 in the wiki example), IDA, PMID:22627129.
- Protein substrates. Human CDC7 phosphorylates MCM2 (PMID:15668232): GO:0004674 protein serine/threonine kinase activity `has_input` MCM2.
- Binding partners. Use the specific binding child when one exists. Otherwise use GO:0005515 protein binding or GO:0005488 binding with `has_input` the partner. Since the 2020 decision, chemical binding is annotated as GO:0005488 binding `has_input` the ChEBI entity rather than by requesting a new precomposed binding term ([wiki: Annotation Conf. Call 2020-02-04](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2020-02-04)).
- Target genes of transcription regulators, on both the MF and the "regulation of transcription" BP row. Standard annotations are not linked, so an input stated on the MF cannot be inferred for the BP.
- The regulated gene product of a regulator activity. In `genes/human/FXN` the reviewed annotation of FXN `enables` GO:0008047 enzyme activator activity carries `has_input`(UniProtKB:Q9Y697, cysteine desulfurase NFS1) from PMID:38627381. That is the pattern the wiki gives for regulatory subunits ([wiki: Contributes to](https://wiki.geneontology.org/index.php/Contributes_to), regulatory and catalytic subunits).

**What not to capture.**

- An input already in the term label or definition (GO:0004396 hexokinase activity `has_input` D-hexose).
- Currency metabolites: ATP for a kinase, NAD+ for a dehydrogenase. GO keeps only the reaction participants that carry the biological specificity, unlike Rhea, which lists them all ([Drive: GP2term and extensions (2021)](https://drive.google.com/open?id=128U6g91Iv2ej9pcgTSGOowbhjp4GwGXmE4gDTiue1Cc)).
- Cofactors and metal ions, and the "X" of an "X-dependent" activity (calcium for a calcium-dependent kinase).
- Assay analogues and artificial substrates. The input is the biological one.
- Sequence Ontology terms ([go-annotation#2584](https://github.com/geneontology/go-annotation/issues/2584)).

**`has_input` versus `with/from`.** `with/from` names the sequence that supports the evidence. `has_input` names the physiological target. A mouse protein shown to bind the human orthologue of its partner gets IPI `with`(human partner) and `has_input`(mouse partner) ([wiki: Has input](https://wiki.geneontology.org/index.php/Has_input); [wiki: Annotating binding](https://wiki.geneontology.org/index.php/Annotating_binding)).

**Direct contact is not required.** An enzyme assay implies contact with the substrate, and no separate interaction assay is needed. The 2018-2020 has_direct_input review ended with a single relation for both cases ([go-annotation#2076](https://github.com/geneontology/go-annotation/issues/2076)).

**Provenance.** [GOC]; the FXN worked example is ours.

<a id="ae-4"></a>

### AE-4. Use `has_output` only for a specific product the term does not already name, and only for a single reaction.

**Rationale and example.** DGKA's product in PMID:22627129 is captured together with its input in one annotation. Multiple outputs are allowed only when they belong to the same reaction ([wiki: Has output](https://wiki.geneontology.org/index.php/Has_output)). The same exclusions as for `has_input` apply: no currency metabolites, no products named in the term.

**Primary input and output.** GO has discussed moving annotations to `has_primary_input` (RO:0004009) and `has_primary_output` (RO:0004008) ([Drive: Harmonizing use of input/output relations in GO (Fall 2024 GOC)](https://drive.google.com/open?id=1GUfrZgxeal3L99v3BCRs4yyrsq_D8yGwq8RwNuQ6OMs)). A separate documentation review decided "for now" to keep only `has_input` and `has_output`, used for the primary entity ([Drive: Review & update Noctua documentation](https://drive.google.com/open?id=13MWyxdfcS78dYz9hg61R4ZS4ydp3OY8Y16LAb3xD3Ug)). Whichever label is used, the semantics are the same: capture only the primary participant.

**Provenance.** [GOC+] (the semantics-over-label reading is ours).

<a id="ae-5"></a>

### AE-5. Use `occurs_in` for the place where an MF happens, or where *every* step of a BP happens. Choose a location that places the activity unambiguously, and do not restate the term.

**Rule detail.**

- MF: the compartment, cell or tissue where the activity was observed. Human LIG3 isoform 1 `enables` GO:0003909 DNA ligase activity `occurs_in`(GO:0005739 mitochondrion), IDA, PMID:24674627.
- BP: only if every MF that is part of the process occurs in that location ([wiki: Occurs in](https://wiki.geneontology.org/index.php/Occurs_in)). A signalling pathway that starts at the plasma membrane and ends in the nucleus does not `occurs_in` the nucleus.
- Do not restate the term. GO:0050852 T cell receptor signaling pathway already `occurs_in` CL:0000084 T cell in the ontology.
- Prefer a location that resolves to one compartment. GO:0000785 chromatin is not `part_of` the nucleus in GO, because prokaryotes have chromatin too, so `occurs_in` chromatin does not say "nuclear". GO:0000228 nuclear chromosome does ([GOCAM_COMPARTMENTS](../../GOCAM_COMPARTMENTS.md)).
- Do not infer a cell type from an immortalised cell line. Treat the line as an experimental tool ([wiki: Annotation Extension: Capturing cell and tissue types](https://wiki.geneontology.org/index.php/Annotation_Extension%3A_Capturing_cell_and_tissue_types)). A HEK293 experiment does not support `occurs_in` kidney epithelial cell.
- An `occurs_in`(GO CC) on an MF is evidence for `is_active_in` that CC, by the property chain `enables o occurs_in` ([wiki: Is active in](https://wiki.geneontology.org/index.php/Is_active_in)). Make the CC annotation too. Inferences GOC-OWL drew from BP `occurs_in` turned out unreliable, because curators had written `occurs_in` where `regulates_o_occurs_in` was meant ([go-annotation#1487](https://github.com/geneontology/go-annotation/issues/1487)).

**Provenance.** [GOC+]. The compartment-resolution and cell-line points sharpen existing guidance using repo findings.

<a id="ae-6"></a>

### AE-6. On CC annotations, use `part_of` with a cell or anatomy term for the cell or tissue in which the component sits, and an existence relation for the stage.

**Examples.** A gene product in GO:0031966 mitochondrial membrane of a spermatocyte: `part_of`(CL:0000017 spermatocyte). *S. pombe* Clp1 at the spindle pole body in interphase: the legacy form was `exists_during`(GO:0051329 mitotic interphase) ([wiki: Supplying temporal location information](https://wiki.geneontology.org/index.php/Annotation_Extension_field%3A_Supplying_temporal_location_information_to_a_GO_annotation)). `exists_during` is not in RO. Current tooling uses `existence_overlaps` (RO:0002490) or `existence_starts_and_ends_during` (RO:0002491).

**Not for complexes.** The SAE allows only existence relations on protein-containing-complex terms. A complex is not "part of" a cell type in this sense.

**Provenance.** [GOC+] (the relation names are updated to the SAE list).

<a id="ae-7"></a>

### AE-7. Use `happens_during` only for a biological phase or life stage, never for a process that merely coincides.

**Rationale.** `happens_during` was once used to attach a co-occurring process when the gene product's role in it was unclear. The wiki has withdrawn that use. A function that is definitely part of a process takes `part_of`. One that only coincides with a process gets no extension ([wiki: Happens during](https://wiki.geneontology.org/index.php/Happens_during)).

**Allowed fillers.** Descendants of GO:0044848 biological phase (for example GO:0000090 mitotic anaphase, GO:0000084 mitotic S phase) and of UBERON:0000105 life cycle stage, or a species stage ontology.

**Provenance.** [GOC].

<a id="ae-8"></a>

### AE-8. Use `part_of`(BP) on an MF to say which process the activity serves. Make the matching BP annotation as a separate row, and do not add a `part_of` the ontology already entails.

**Rule detail.** `enables` GO:0003924 GTPase activity `part_of`(GO:0048011 neurotrophin TRK receptor signaling pathway) should come with a separate `involved_in` GO:0048011 row, so users who ignore column 16 lose nothing. Not: GO:0016301 kinase activity `part_of`(GO:0016310 phosphorylation). It is harmless but adds nothing, because the ontology already links them ([wiki: Column 16: Function x Process x Component extensions](https://wiki.geneontology.org/index.php/Column_16%3A_Function_x_Process_x_Component_extensions)).

**Provenance.** [GOC].

<a id="ae-9"></a>

### AE-9. Do not use `part_of(Y)` to rebuild a precomposed "X involved in Y" term that GO has obsoleted for GO-CAM.

**Rationale.** `involved_in` X with `part_of`(Y) is exactly GO's logical definition of the retired class. GO:0061740 protein targeting to lysosome involved in chaperone-mediated autophagy is defined as GO:0006622 protein targeting to lysosome `and part_of some` GO:0061684 chaperone-mediated autophagy. GO has obsoleted more than 1,200 such terms, 883 with a comment saying the term should be captured as a GO-CAM model. Writing the same class as an extension undoes the obsoletion in different syntax ([INVOLVED_IN_PRECOMPOSITION](../../INVOLVED_IN_PRECOMPOSITION.md)).

**What to do instead.** When you MODIFY a precomposed term to its genus X, record where Y went in `review.decomposed_into` ([CLAUDE.md](../../../CLAUDE.md)): `gocam_associations` or `module_associations` when Y is a mechanism with a model, `in_core_functions` when Y is central to the gene, or `context_dropped: true` when Y is peripheral or was itself the over-annotation. The repo briefly had a `proposed_replacement_extensions` slot for X plus `part_of`(Y). It was removed on 2026-10-25 because it restated the retired class, duplicated the model link and fed nothing downstream.

**Boundary.** [AE-8](#ae-8) still applies to an activity `part_of` a process that GO has not retired and that is an ordinary BP. The rule targets the precompositions GO itself sent to GO-CAM.

**Provenance.** [NEW]. GOC guidance (AE-8) permits `part_of`(BP) in general. The restriction comes from the obsoletion comments and the repo decision.

<a id="ae-10"></a>

### AE-10. Prefer an extension for target-, cell-type- and stage-specific context. Request a precomposed term only for a recognised biological concept that is not an arbitrary cross-product.

**Decision rule.**

| Situation | Choose |
|---|---|
| The concept is a standard scientific term used independently of any one gene (B cell differentiation, mitochondrial translational elongation) | Precomposed term. Request it if absent |
| Specificity is a particular substrate, partner or target gene | Extension (`has_input`). Never a gene-specific term |
| A chemical binding activity | GO:0005488 binding `has_input` CHEBI, per the 2020 decision, unless a binding term already exists |
| Location or cell type of a general process, with no recognised name (plastid translational elongation, as it stood in the wiki example) | Extension (`occurs_in`). Request a term if the combination becomes a recognised concept; the annotation will fold forward |
| A process "involved in" another process, or an MF "involved in" a BP | Neither. Use a GO-CAM ([AE-9](#ae-9)) |
| A broad readout term that is uninformative without context (cell population proliferation) | Extension is required. Without one, refine the term or remove the row |

**Example.** GO:0070125 mitochondrial translational elongation exists, `is_a` GO:0006414 translational elongation and `occurs_in` GO:0005739 mitochondrion, so use it rather than GO:0006414 `occurs_in` mitochondrion. For the plastid case the wiki recommended GO:0006414 `occurs_in`(GO:0009536 plastid) over co-annotating GO:0032544 plastid translation, because co-annotation does not link the two.

**Mandatory extensions.** gorule-0000051 warns when certain terms lack an extension ([Drive: Feedback on GO rules (FlyBase copy)](https://drive.google.com/open?id=1AiEBQGA37oyyoFmDYNexYOlDIwqPHnMvAESIVqgjxFM)). When GO proposed making GO:0008283 cell population proliferation do-not-annotate, curators objected that it is useful with a cell-type extension, and the outcome was to require one ([go-annotation#2204](https://github.com/geneontology/go-annotation/issues/2204)).

**Provenance.** [GOC+]. [wiki: Column 16: Function x Process x Component extensions](https://wiki.geneontology.org/index.php/Column_16%3A_Function_x_Process_x_Component_extensions); [wiki: Annotation Conf. Call 2020-02-04](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2020-02-04); [go-annotation#2204](https://github.com/geneontology/go-annotation/issues/2204).

<a id="ae-11"></a>

### AE-11. Keep extensions to what a single statement can hold. Causal, chained or multi-activity knowledge goes in a GO-CAM.

**Rationale.** GO is separating standard annotations from GO-CAMs. A standard annotation is one GAF or GPAD line, one evidence, independent or dependent extensions and no nesting. Chained relations will be archived, and groups are encouraged to rebuild that knowledge as true GO-CAMs ([Drive: GO-CAMs and standard annotations in Noctua (Fall 2026 GOC)](https://drive.google.com/open?id=1CY1Py4e9jTSXDn_mircd-C3aVLHqNJ2x3BvH90EKFj8); [Drive: Evidence unwinding meeting (2026-01-20)](https://drive.google.com/open?id=1IsQ9cY3eJCkmpU6VAlJiinrm_Bztt_VZcKv98QPjsX8)). The 2022 relation review already proposed removing causal relations from extensions.

**Rule detail.**

- "A regulates B's activity": a GO-CAM edge, not `directly_positively_regulates` in column 16 of A's binding annotation. The 2019 `activated_by` reannotation used that pattern ([wiki: Annotation Conf. Call 2019-11-19](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2019-11-19)). Read rows that already carry it as legacy GO-CAM fragments.
- "Regulates transcription of gene G in cell type C": one standard annotation with `has_input`(G),`occurs_in`(C) is fine, because that is a single statement.
- When a standard-annotation extension and a GO-CAM say different things about the same gene, the GO-CAM is the more specific model. Check whether the extension is a stale import ([gocam-modeling.md](gocam-modeling.md)).

**Provenance.** [GOC+].

<a id="ae-12"></a>

### AE-12. An extension needs the same evidence as the annotation. Do not expect or invent extensions on propagated rows.

**Rationale.** The extension is part of the claim, so the cited reference must support it. ISS, ISO, IBA and IEA pipelines do not carry extensions: "Currently annotation extensions are not being propagated" ([Drive: GP2term and extensions (2021)](https://drive.google.com/open?id=128U6g91Iv2ej9pcgTSGOowbhjp4GwGXmE4gDTiue1Cc)). MGI's rat-to-mouse ISO filters do not import them either ([Drive: MGI ISO rat filters](https://drive.google.com/open?id=1lx65V8ikyofnkDdwojm6fhHZ801ET1Z9)). A gene-product filler in a transferred extension would name a gene in the source species, which is wrong for the target.

**Rule detail.** A manually transferred extension needs the target-species filler, such as the orthologous substrate, and a curator's judgement that the orthologous relationship holds.

**Provenance.** [GOC].

<a id="ae-13"></a>

### AE-13. Before judging a row, read its extension in QuickGO or GOA. The repository's cached GOA file does not include one.

**Rationale (repo-specific).** `GENE-goa.tsv` has 16 columns and no extension column. `fetch_goa_data` deduplicates byte-identical projected rows, so annotations that differ only in their extension collapse into one row. A reviewer who sees "GO:0005515 protein binding, IPI" or "GO:0008283 cell population proliferation, IMP" cannot tell whether the curator added `has_input` or `acts_on_population_of`, which is often what makes the row informative.

**Procedure.**

1. Look up the row in QuickGO, which shows extensions, before marking a broad term TOO_GENERAL or MARK_AS_OVER_ANNOTATED, or MODIFYing it to a specific child.
2. Record a verified extension in the row's `extensions` list (predicate as an RO or BFO CURIE, which `ROTermEnum` checks, plus a term id and label), as `genes/human/FXN` does for NFS1.
3. Where one TSV row stands for several GOA rows with different extensions, say so in `reason`. The review action applies to all of them only if the argument does.

**Provenance.** [NEW]. A tooling gap. Mirrors the repo's known WITH/FROM collapse in stub seeding.

<a id="ae-14"></a>

### AE-14. When reviewing, judge an extension like the term: keep it if it holds, fix its relation if that is legacy, and remove it if it restates the term or encodes a condition.

| Finding | Action |
|---|---|
| Extension true and informative | ACCEPT the row and record the extension |
| Legacy relation with a direct successor (`occurs_at` → `occurs_in`, `has_direct_input` → `has_input`, `has_regulation_target` → `has_input`) | ACCEPT the claim and note the relation update in `reason` |
| Extension restates the term | ACCEPT the row and note that the extension is redundant (not an error in the claim) |
| Extension carries a condition or hidden negation | Judge the bare annotation. If it is false without the extension, REMOVE |
| Extension makes the claim false (wrong substrate, wrong cell type) but the bare term holds | MODIFY with corrected `extensions` |
| Extension re-encodes a retired precomposition | MODIFY per [AE-9](#ae-9) with `decomposed_into` |

**Provenance.** [NEW].

## Decision aid

**Which relation?**

| You want to say... | Relation | Filler |
|---|---|---|
| The kinase phosphorylates protein P | `has_input` | UniProtKB id of P |
| The transporter moves chemical C | `has_input`, or `transports_or_maintains_localization_of` on a BP | CHEBI |
| The enzyme makes product M | `has_output` | CHEBI |
| The activity happens in the mitochondrion | `occurs_in` | GO CC |
| ...in cardiac muscle cells | `occurs_in` | CL |
| The process happens in a tissue (all steps) | `occurs_in` | UBERON / species anatomy |
| The protein sits in the nucleus of spermatocytes | `part_of` on the CC row | CL |
| The localisation is seen in interphase | `existence_overlaps` | GO BP / phase |
| The activity occurs in mitotic anaphase | `happens_during` | GO:0044848 descendant |
| The activity is a step in pathway P | `part_of` on the MF row, plus an `involved_in` P row | GO BP |
| A regulates B's activity | No extension. Use a GO-CAM | — |
| The process does not need X | No extension. Use nothing | — |

**Extension or term?** See the table in [AE-10](#ae-10).

## Common errors

| Error | Example | Fix |
|---|---|---|
| Restating the term | GO:0004396 hexokinase activity `has_input` hexose | Drop the extension |
| Currency metabolite or cofactor as input | kinase `has_input` ATP; enzyme `has_input` Zn2+ | Drop it |
| Assay analogue as input | Artificial peptide substrate | Use the physiological substrate or none |
| `occurs_in` on a multi-compartment BP | Signalling pathway `occurs_in` nucleus | Move `occurs_in` to the MF row of the nuclear step |
| Cell type inferred from a cell line | HeLa experiment → `occurs_in` cervical epithelial cell | Drop it |
| `happens_during` a co-occurring process | X `happens_during` DNA repair | `part_of` if a step, otherwise drop |
| NOT with extension | NOT kinase activity `has_input` B | Drop the NOT row ([QN-12](qualifiers-and-negation.md#qn-12)) |
| Retired precomposition re-encoded | protein targeting to lysosome `part_of` chaperone-mediated autophagy | `decomposed_into` ([AE-9](#ae-9)) |
| Condition as extension | `independent_of`, `in_absence_of` | Judge the bare row |
| `has_input` on BP inferred from the MF | Expecting the BP "regulation of transcription" to inherit the MF's target | Add the input to the BP row explicitly |
| Errors in published examples | Wiki `occurs_in` example annotates ATP13A2 with `enables` on a BP and uses the now-obsolete CL:0002609; the LIG3 table shows UniProtKB:P23743 (DGKA) as the object | Use `involved_in` for BP. Check every example id before copying it |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [wiki: Column 16: Function x Process x Component extensions](https://wiki.geneontology.org/index.php/Column_16%3A_Function_x_Process_x_Component_extensions) | `part_of`(BP) on an MF is the standard way to link function and process | Still allowed, but never to rebuild a precomposition GO retired for GO-CAM ([AE-9](#ae-9)) | GO's obsoletion comments ask for a model, and `part_of`(Y) restates the retired class |
| Same page; [wiki: Annotation Extension: Capturing cell and tissue types](https://wiki.geneontology.org/index.php/Annotation_Extension%3A_Capturing_cell_and_tissue_types) | Example GO:0007242 "intracellular signaling cascade"; temporal example GO:0007067 | Both ids no longer resolve in the current GO build. Use current terms | Examples went stale |
| [wiki: Happens during](https://wiki.geneontology.org/index.php/Happens_during) (BP example) vs [Drive: Annotation Extension Relations - 2022-09-09](https://drive.google.com/open?id=13MOVlRD1_iBJyw7whO7lK0KTCaLW0dbbtcpgGOthKqA) (BP `happens_during`: N) and [Drive: SAE specs](https://drive.google.com/open?id=1mBzbiqey0fyFUhWtKE5UKvIPNvpJ2Kx1XNkPgCPorpc) (BP: Y) | Sources disagree on whether BP may carry `happens_during` | Allow it on MF. On BP, use it only for phases and stages and expect tooling differences | The wiki's own example is BP; the 2022 table says no; the SAE allows it. GOC should decide |
| [wiki: Annotation Extension field: Supplying temporal location information](https://wiki.geneontology.org/index.php/Annotation_Extension_field%3A_Supplying_temporal_location_information_to_a_GO_annotation) | `exists_during` for CC stage | `existence_overlaps` / `existence_starts_and_ends_during` | `exists_during` is not in RO ([wiki: Happens during](https://wiki.geneontology.org/index.php/Happens_during)); the SAE uses the RO pair |
| [Drive: Annotation Extension Sept 2017](https://drive.google.com/open?id=0B_c5g4FezmhfVElqaU9vT2lwbEk) and legacy rows | `has_regulation_target` allowed, "use something more specific" | Not for new annotations. `has_input` on the regulation term | Ambiguous; imports already convert it; absent from the SAE |
| [wiki: Annotation Conf. Call 2019-11-19](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2019-11-19) | Replace `activated_by` with binding plus `directly_positively_regulates` in the extension | Put the causal link in a GO-CAM | Causal extensions flagged for removal (2022); chained and nested extensions to be archived (2026) |
| [Drive: Harmonizing input/output relations (Fall 2024)](https://drive.google.com/open?id=1GUfrZgxeal3L99v3BCRs4yyrsq_D8yGwq8RwNuQ6OMs) vs [Drive: Review & update Noctua documentation](https://drive.google.com/open?id=13MWyxdfcS78dYz9hg61R4ZS4ydp3OY8Y16LAb3xD3Ug) | Convert to `has_primary_input/output` vs keep `has_input/has_output` for now | Capture only the primary participant, under either label | The semantics agree even though the labels differ |
| [wiki: Elements of an annotation](https://wiki.geneontology.org/index.php/Elements_of_an_annotation) vs gorule-0000053 deprecation | NOT forbidden with extensions vs "will not be implemented" | No NOT with extensions | See [qualifiers-and-negation.md](qualifiers-and-negation.md#differences-from-prior-guidance) |
| [wiki: Column 16](https://wiki.geneontology.org/index.php/Column_16%3A_Function_x_Process_x_Component_extensions) | Add a "redundant" bare annotation "sometimes" | Always add the bare BP row for an MF `part_of`(BP), and the CC row for an MF `occurs_in`(CC) | "Sometimes" gave no test. Users who ignore column 16 lose information otherwise |
| [wiki: Annotation Extension: Capturing cell and tissue types](https://wiki.geneontology.org/index.php/Annotation_Extension%3A_Capturing_cell_and_tissue_types) | Use the cell-type ontology for context | Also prefer `occurs_in` fillers that resolve to one compartment (nuclear chromosome, not chromatin) | Repo analysis of GO-CAMs found chromatin locations that reach no compartment ([GOCAM_COMPARTMENTS](../../GOCAM_COMPARTMENTS.md)) |
| [go-annotation#2204](https://github.com/geneontology/go-annotation/issues/2204) | Proposal to make cell population proliferation do-not-annotate | Allowed with a required extension | The thread's own outcome; restated as a general rule for readout terms |
| None (gap) | No guidance on reviewing extensions | Action table ([AE-14](#ae-14)) and the cache caveat ([AE-13](#ae-13)) | Reviewers working from the repo's GOA cache cannot see extensions |

## Open questions

1. **`happens_during` on BP.** The wiki, the 2022 relation review and the SAE disagree.
2. **Causal relations in extensions.** The SAE still allows `causally_upstream_of...` and `regulates` on BP and MF extensions, while the 2022 review asked whether to remove them. Will standard annotations lose them in the 2026 data-store split?
3. **`has_agent` replacement.** Cell-cell adhesion annotations used `has_agent` for the cell type ([go-annotation#2047](https://github.com/geneontology/go-annotation/issues/2047); [wiki: Ontology meeting 2020-08-24](https://wiki.geneontology.org/index.php/Ontology_meeting_2020-08-24)). No replacement has been agreed.
4. **Which terms require an extension?** gorule-0000051 exists, but the list of terms it covers is not in our sources.
5. **Primary input labels.** Will GO move existing standard annotations to `has_primary_input` and `has_primary_output`, and should reviews then rewrite predicates?
6. **Repo tooling.** Should `fetch-gene` request extensions from QuickGO and stop collapsing rows that differ only in extension? That would make [AE-13](#ae-13) unnecessary.
7. **ChEBI fillers.** The 2020 decision to post-compose chemical binding raised concerns about curators navigating ChEBI. Is a curated ChEBI subset for annotation tools still planned?

## Sources

**GO wiki**
- [wiki: Annotation Relations](https://wiki.geneontology.org/index.php/Annotation_Relations) (reviewed 2023-09-05)
- [wiki: Has input](https://wiki.geneontology.org/index.php/Has_input); [wiki: Has output](https://wiki.geneontology.org/index.php/Has_output); [wiki: Occurs in](https://wiki.geneontology.org/index.php/Occurs_in) (reviewed 2021-10-07); [wiki: Happens during](https://wiki.geneontology.org/index.php/Happens_during); [wiki: Is active in](https://wiki.geneontology.org/index.php/Is_active_in)
- [wiki: Column 16: Function x Process x Component extensions](https://wiki.geneontology.org/index.php/Column_16%3A_Function_x_Process_x_Component_extensions)
- [wiki: Annotation Extension: Capturing cell and tissue types](https://wiki.geneontology.org/index.php/Annotation_Extension%3A_Capturing_cell_and_tissue_types)
- [wiki: Annotation Extension field: Supplying temporal location information](https://wiki.geneontology.org/index.php/Annotation_Extension_field%3A_Supplying_temporal_location_information_to_a_GO_annotation)
- [wiki: Annotation Extension Relation:independent of](https://wiki.geneontology.org/index.php/Annotation_Extension_Relation%3Aindependent_of) (deprecated)
- [wiki: Causally upstream of or within](https://wiki.geneontology.org/index.php/Causally_upstream_of_or_within)
- [wiki: Annotating binding](https://wiki.geneontology.org/index.php/Annotating_binding) (proposal, 2020)
- [wiki: Contributes to](https://wiki.geneontology.org/index.php/Contributes_to); [wiki: Elements of an annotation](https://wiki.geneontology.org/index.php/Elements_of_an_annotation)
- [wiki: Annotation Conf. Call 2019-11-19](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2019-11-19); [wiki: Annotation Conf. Call 2020-02-04](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2020-02-04)
- [wiki: Noctua MOD Imports](https://wiki.geneontology.org/index.php/Noctua_MOD_Imports); [wiki: Ontology meeting 2020-08-24](https://wiki.geneontology.org/index.php/Ontology_meeting_2020-08-24)

**GO Consortium Drive**
- [Drive: Use of relations for GO annotation - GP2term and extensions (2021)](https://drive.google.com/open?id=128U6g91Iv2ej9pcgTSGOowbhjp4GwGXmE4gDTiue1Cc)
- [Drive: SAE - Annotation Extension Relations specs](https://drive.google.com/open?id=1mBzbiqey0fyFUhWtKE5UKvIPNvpJ2Kx1XNkPgCPorpc)
- [Drive: Annotation Extension Relations - 2022-09-09](https://drive.google.com/open?id=13MOVlRD1_iBJyw7whO7lK0KTCaLW0dbbtcpgGOthKqA)
- [Drive: Annotation Extension Sept 2017 (GOC Cambridge)](https://drive.google.com/open?id=0B_c5g4FezmhfVElqaU9vT2lwbEk)
- [Drive: GO-CAMs and standard annotations in Noctua (Fall 2026 GOC)](https://drive.google.com/open?id=1CY1Py4e9jTSXDn_mircd-C3aVLHqNJ2x3BvH90EKFj8)
- [Drive: Evidence unwinding meeting with curators (2026-01-20)](https://drive.google.com/open?id=1IsQ9cY3eJCkmpU6VAlJiinrm_Bztt_VZcKv98QPjsX8)
- [Drive: Noctua Standard Annotations evidence splitting](https://drive.google.com/open?id=1p2pwOCovVbX61bQspUcptSt2pkA3OSzDHulOpQhZElQ)
- [Drive: Harmonizing use of input/output relations in GO (Fall 2024 GOC)](https://drive.google.com/open?id=1GUfrZgxeal3L99v3BCRs4yyrsq_D8yGwq8RwNuQ6OMs)
- [Drive: Review & update Noctua documentation](https://drive.google.com/open?id=13MWyxdfcS78dYz9hg61R4ZS4ydp3OY8Y16LAb3xD3Ug)
- [Drive: Feedback on GO rules (FlyBase copy)](https://drive.google.com/open?id=1AiEBQGA37oyyoFmDYNexYOlDIwqPHnMvAESIVqgjxFM)
- [Drive: MGI ISO rat filters](https://drive.google.com/open?id=1lx65V8ikyofnkDdwojm6fhHZ801ET1Z9)

**GitHub issues (geneontology/go-annotation)**
- [go-annotation#1487](https://github.com/geneontology/go-annotation/issues/1487) (GOC-OWL inferences from extensions)
- [go-annotation#2047](https://github.com/geneontology/go-annotation/issues/2047) (cell types for adhesion terms)
- [go-annotation#2076](https://github.com/geneontology/go-annotation/issues/2076) (has_input vs has_direct_input)
- [go-annotation#2204](https://github.com/geneontology/go-annotation/issues/2204) (cell population proliferation)
- [go-annotation#2584](https://github.com/geneontology/go-annotation/issues/2584) (occurs_at deprecation)

**Papers**
- [PMID:24885854](https://europepmc.org/article/MED/24885854) A method for increasing expressivity of Gene Ontology annotations using a compositional approach (2014)

**Repository**
- [CLAUDE.md](../../../CLAUDE.md) (decomposing precomposed terms; `decomposed_into`)
- [INVOLVED_IN_PRECOMPOSITION](../../INVOLVED_IN_PRECOMPOSITION.md); [GOCAM_COMPARTMENTS](../../GOCAM_COMPARTMENTS.md)
- Gene review cited: `genes/human/FXN` (GO:0008047 with `has_input` NFS1)
- Code: `src/ai_gene_review/etl/gene.py` (`fetch_goa_data` row collapse); `src/ai_gene_review/schema/gene_review.yaml` (`AnnotationExtension`, `ROTermEnum`)
