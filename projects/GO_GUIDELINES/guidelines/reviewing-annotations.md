# Reviewing existing annotations: GO annotation guidelines

Status: draft v0.1 (2026-11-15) · Part of [GO_GUIDELINES](../../GO_GUIDELINES.md)

**In brief:**

- A review judges claims about the gene product, not evidence rows. Rows that share a term
  are one claim; their actions must agree, and `REMOVE` is never a way to deduplicate them.
- Pick the action by what it says about the claim: `REMOVE` means "probably false", `MODIFY`
  means "this row's own evidence supports a better term", `MARK_AS_OVER_ANNOTATED` means
  "goes beyond the evidence", `KEEP_AS_NON_CORE` means "true, precise, peripheral".
- Do not overrule an experimental annotation whose full text you have not read. Use
  `UNDECIDED`, and never infer "wrong gene" from a cached title or abstract.
- Necessity is not participation. Being required for a process, consumed by it, or measured
  by its assay does not make a gene product part of it.
- When the error lives upstream (wrong gene, wrong paper, wrong mapping, retracted source),
  record it as a structured source defect addressed to whoever can fix it.
- Every row's reasoning must be specific to that term and backed by a verbatim quote from an
  independent source; boilerplate and self-citation of the GOA file are not review.

## Scope

This document covers the audit of an existing body of GO annotations for one gene product:
the GOA/MOD rows, PAINT IBA rows, electronic rows and NOT rows that a curator inherits. It
says how to classify each row, how to keep the classification consistent, when to defer, and
how to record problems that need fixing at the source. It also covers consortium review
tickets (obsoletion-driven and rule-driven reviews in the `go-annotation` tracker) and the GO
rules (gorules) that run on every load.

It does not repeat the term-choice rules for each aspect; those live in
[molecular-function.md](molecular-function.md), [biological-process.md](biological-process.md),
[cellular-component.md](cellular-component.md) and the other sibling documents. Ontology
change (obsoletion, merges, term requests, taxon constraints) is in
[ontology-change-and-taxa.md](ontology-change-and-taxa.md). How to read a phylogenetic
inference before challenging it is in [phylogenetic-propagation.md](phylogenetic-propagation.md),
and pipeline-specific failure modes are in [electronic-annotation.md](electronic-annotation.md).

The action vocabulary used throughout (`ACCEPT`, `KEEP_AS_NON_CORE`, `MODIFY`,
`MARK_AS_OVER_ANNOTATED`, `TOO_GENERAL`, `REMOVE`, `UNDECIDED`, `NEW`) is the
`ActionEnum` of this repository's review schema. A GOC curator working in Noctua or
Protein2GO has fewer verbs (keep, edit, delete, add NOT), but the distinctions below still
decide which of those to do.

## Principles

**GO is a model of current knowledge, not an archive.** The GOC's own best-practice page
says curators should not hesitate to remove older annotations that conflict with what is now
known ([wiki: Tips to Produce High Quality Annotations](https://wiki.geneontology.org/index.php/Tips_to_Produce_High_Quality_Annotations)).
A review is the place where that happens deliberately, one claim at a time.

**Evidence codes are not quality scores.** The consortium said so explicitly in 2007 and
removed the code hierarchy ([Drive: evCode-summary (archived)](https://drive.google.com/open?id=1qZm_e_wnfu_yUAg7qbwrJpYwyRRNqD_7)).
An IEA can be right and an IDA can be wrong. A review weighs what each row asserts and what
supports it, then reaches one verdict per claim.

**The reviewer sees less than the curator did.** Experimental annotations were made from full
text; a reviewer often has only an abstract. Humility about what you cannot see is a rule,
not a courtesy ([REV-8](#rev-8)).

**Errors propagate, so fix them at the source.** A wrong seed annotation or mapping is copied
by PAINT, Ensembl Compara, InterPro2GO and ARBA. The 2018 QC call argued that error fixing
should be treated like fixing software bugs, because one fix can clear many species at once
([wiki: QCQA call 2018-03-20](https://wiki.geneontology.org/index.php/QCQA_call_2018-03-20)).
A review that only cleans its own file leaves the cause in place.

**A review must be auditable.** Another curator should be able to read one row's reason and
quote and reach, or dispute, the same verdict.

## Rules

<a id="rev-1"></a>
### REV-1. Judge the claim, not the row; rows sharing a term get consistent actions

**Rows with the same GO term (and compatible qualifiers) are one claim. Their actions may
differ in emphasis but must not contradict each other, and `REMOVE` must not be used to keep
the "best" evidence code and discard the rest.**

GOA often carries one term from several sources, for example IBA, IEA and NAS for one
complex membership. These are independent lines of evidence for one claim. `REMOVE` asserts
that the claim is unlikely to be true, so removing the IEA while accepting the IDA says the
claim is both true and false. The machine-checkable version of this rule is the action
consistency table ([action consistency](../../../docs/action_consistency.md)), which also
handles hierarchy: keeping a positive annotation to `GO:0005929` cilium while keeping a NOT on
an ancestor of it is a contradiction, because a positive annotation entails its ancestors and
a NOT entails its descendants.

*Example.* Fission yeast Gaa1 carries `GPI-anchor transamidase complex` from more than one
source (IBA, IEA and NAS; see `genes/SCHPO/gaa1`). A review that accepts the
IBA and removes the IEA "as redundant" fails consistency; the right record accepts (or keeps) all three, with one
argument. The redundancy itself is not an error
([OVER_ANNOTATION_PATTERNS](../../OVER_ANNOTATION_PATTERNS.md), pattern 5).

The one sanctioned exception is bare `GO:0005515` protein binding, which the protein-binding
policy removes as uninformative even beside accepted rows ([REV-13](#rev-13)).

When GOA holds a positive row and a NOT row for the same term from different papers, decide:
`REMOVE` or `UNDECIDED` one side, or, if both hold in different contexts (NOT in roots,
positive in shoots), record a per-annotation `consistency_exception` with the reason.

Provenance: [GOC+]. The GOC asks curators to look at existing annotations for consistency
([wiki: Tips](https://wiki.geneontology.org/index.php/Tips_to_Produce_High_Quality_Annotations));
the claim-level framing and the formal consistency table are ours
([CLAUDE.md](../../../CLAUDE.md), [action consistency](../../../docs/action_consistency.md)).

<a id="rev-2"></a>
### REV-2. Choose the action by what it says about the claim

**Each action is a distinct statement. Use the one whose statement you can defend, and make
the `reason` argue that statement and no other.**

| Action | What it asserts | Typical evidence |
|---|---|---|
| `ACCEPT` | True, and part of the gene's core function | Direct evidence, coherent with the whole picture |
| `KEEP_AS_NON_CORE` | True and as precise as warranted, but peripheral | Developmental or pleiotropic roles, real secondary activities |
| `MODIFY` | The idea is right; this row's own evidence supports a better term | A paper that names the ligand; a sign error (`positive` vs `negative regulation`) |
| `MARK_AS_OVER_ANNOTATED` | Not false, but beyond what the evidence supports | An in vitro activity of unknown relevance; a phenotype read as a process |
| `TOO_GENERAL` | True but uninformative, because a specific asserted term entails it | `GO:0016020` membrane beside an accepted specific membrane term |
| `REMOVE` | Unlikely to be true | Contradicted function; demonstrably wrong mapping; over-propagation |
| `UNDECIDED` | Cannot judge with the evidence available | Inaccessible full text; genuinely conflicting data |

Two failure modes recur. The first is an action that contradicts its own reason: `ACCEPT` or
`KEEP_AS_NON_CORE` on a row whose reason argues the term is too general. The second is using
`REMOVE` for "I prefer another row" or "true but vague". Neither is a judgement about truth.

Provenance: [NEW]. The GOC's curation tools offer keep, edit, delete and NOT; the graded
vocabulary is this repository's ([CLAUDE.md](../../../CLAUDE.md)).

<a id="rev-3"></a>
### REV-3. A correct but general term is `MODIFY` only when this row's evidence supports the specific term

**If a row's term is true but less specific than the evidence allows, `MODIFY` it to the
specific descendant, and only when this row's own evidence supports that descendant. If the
row's evidence stops at the general term, keep the row. Reserve `TOO_GENERAL` for terms that
are imprecise on their own once a specific term is asserted elsewhere.**

A paper that identifies tachykinin NK3 ligand binding supports `GO:0016498` neuromedin K
receptor activity; an InterPro2GO row from a generic GPCR signature supports only
`GO:0004930` G protein-coupled receptor activity. The InterPro row is not `MODIFY` (its
evidence cannot reach the descendant) and it is not `TOO_GENERAL` (GPCR activity is a
respectably specific term): keep it. `TOO_GENERAL` is for `GO:0016020` membrane beside an
accepted `GO:0005886` plasma membrane, where the broad term answers no question by itself.
When several descendants are supported, as for a pleiotropic gene, list all of them as
replacements rather than choosing one.

Root organelle terms are an exception: `GO:0005739` mitochondrion and the other four root
organelles stay as they are when supported, and the sub-compartment is added as a new row,
not substituted ([cellular-component.md](cellular-component.md),
[ORGANELLES](../../ORGANELLES.md)).

Lateral corrections are a separate, older use of `MODIFY`: a sign error, or a BP that should
have been a different process, takes a replacement that is not a descendant.

Provenance: [NEW]. This is a maintainer ruling of 2026-11-14, made after two reviews in one
batch read the action vocabulary two opposite ways for the same kind of row. It narrows
`TOO_GENERAL` and does not retroactively condemn earlier reviews
([CLAUDE.md](../../../CLAUDE.md)). It departs from the over-annotation catalogue, which
recommends "REMOVE or MODIFY" for broad enzyme terms
([OVER_ANNOTATION_PATTERNS](../../OVER_ANNOTATION_PATTERNS.md), pattern 2); see the
Differences table.

<a id="rev-4"></a>
### REV-4. Separate core from peripheral before deciding anything else

**Write down the gene product's core activity, location and process first. `ACCEPT` is for
rows that state that core; true, precise rows outside it are `KEEP_AS_NON_CORE`.**

A review that starts row by row drifts toward accepting everything that is not wrong. The GOC
recommends a gene-centric or pathway-centric pass rather than paper-by-paper curation, and
"less is more": select the terms that capture the essence of the function
([wiki: Tips](https://wiki.geneontology.org/index.php/Tips_to_Produce_High_Quality_Annotations)).
The Fall 2024 consortium sessions on highly annotated genes (mouse *Ctnnb1*, *C. elegans*
*daf-16*, human MTOR) made the same point from the other end: review the annotation set first,
then worry about how it is displayed
([Drive: Highly annotated genes, daf-16](https://drive.google.com/open?id=1YhRirPCkc9Pl0gOC3Mhc5Zn0VK8SGHEOO-BeI6pwAGk),
[Drive: Highly annotated genes, MTOR](https://drive.google.com/open?id=1Ha8AyFN9WndsT6UPPUnMYawzdn-dnqCG)).

*Example.* For DAF-16, a FOXO transcription factor that shuttles between cytoplasm and
nucleus, the review proposed removing the remaining cytoplasm and cytosol rows because the
cellular component is where the product is active, and DAF-16 is inactive in the cytoplasm
([Drive: daf-16](https://drive.google.com/open?id=1YhRirPCkc9Pl0gOC3Mhc5Zn0VK8SGHEOO-BeI6pwAGk)).
In this repository's vocabulary, those rows would be `MARK_AS_OVER_ANNOTATED` if the
localization is real but not where the function acts, and `KEEP_AS_NON_CORE` only if the
cytoplasmic pool does something.

Provenance: [GOC+]. Core-function focus is GOC guidance; the explicit core/non-core split per
row is ours.

<a id="rev-5"></a>
### REV-5. The conclusion, not the assay; the direct role, not its downstream effects

**A row whose term names the assay readout, or a downstream consequence of the core
activity, is over-annotation. Mark it `MARK_AS_OVER_ANNOTATED`, or `REMOVE` it when direct
evidence later showed the gene acts elsewhere.**

GOC examples: a scratch "wound healing" assay measures `GO:0048870` cell motility, not
`GO:0042060` wound healing; DNA fragmentation and caspase activation are readouts of
apoptosis, not evidence of a direct role in it
([wiki: Tips](https://wiki.geneontology.org/index.php/Tips_to_Produce_High_Quality_Annotations)).
The downstream-process guideline gives the canonical removal: yeast spliceosome components
had been annotated to translation from mutant phenotypes, and those rows were removed once the
splicing role was shown, because translation defects are expected when ribosomal transcripts
are spliced ([wiki: Annotating downstream processes](https://wiki.geneontology.org/index.php/Annotating_downstream_processes)).

The pattern "gene affects X, X affects Y, gene annotated to Y" is the commonest source of
pleiotropic over-annotation ([OVER_ANNOTATION_PATTERNS](../../OVER_ANNOTATION_PATTERNS.md),
pattern 4). For a hub gene, expect most developmental and disease-adjacent process rows to
fall here. Do not remove them merely for being downstream; ask whether the row's evidence
shows the gene acting in the process. The rules for phenotype-derived process rows are in
[biological-process.md](biological-process.md).

Provenance: [GOC].

<a id="rev-6"></a>
### REV-6. Catalytic rows on pseudoenzymes, substrates and accessory subunits

**Remove electronic catalytic rows when the protein lacks the catalytic machinery. Read
"is phosphorylated" and "stimulates the activity of" as the opposite of "has the activity".
Give a complex's catalytic activity only to the subunit that carries the active site.**

Domain signatures predict activity from fold, and folds outlive catalysis. Three shapes recur:

- *Pseudoenzymes.* A JmjC, P450, thiolase or HKD fold whose active-site residues are gone.
  Fission yeast Epe1 carries IEA rows for `GO:0016491` oxidoreductase activity and
  `GO:0051213` dioxygenase activity from its JmjC domain; its iron-binding triad is
  non-canonical and no demethylation has been detected, so the electronic rows are `REMOVE`
  ([CONTESTED_FUNCTION](../../CONTESTED_FUNCTION.md)). Its two PomBase experimental rows for
  `GO:0032454` histone H3K9 demethylase activity are `UNDECIDED`, not `REMOVE`, because they
  rest on in vivo genetics the reviewer cannot fully re-read ([REV-8](#rev-8)).
- *Substrate read as enzyme.* Human CREB1 carries an IDA for `GO:0006468` protein
  phosphorylation; CREB1 is phosphorylated by kinases and is not one. RASA1 carries a TAS for
  `GO:0003924` GTPase activity; it stimulates Ras GTPase activity and has none itself
  ([TOP_NOTS](../../TOP_NOTS.md), Tier 1).
- *Accessory subunit given the complex's activity.* SURF1, a cytochrome oxidase assembly
  factor, carries an IEA for `GO:0004129` cytochrome-c oxidase activity. The activity
  belongs to the catalytic subunits; non-catalytic partners get `contributes_to` at most, and
  assembly factors get nothing ([protein-complexes.md](protein-complexes.md)).

An experimental row of the substrate kind (CREB1) can be removed despite its code, because the
error is in the reading of the result, not in the result: the paper shows CREB1 phosphorylated,
which no one disputes. Say so in the reason, and quote the paper.

Where the absent activity is likely to be re-predicted, propose a NOT ([REV-14](#rev-14)).

Provenance: [GOC+]. The `contributes_to` convention and the ban on IPI for catalytic activity
(GORULE:0000007, [go-annotation#2131](https://github.com/geneontology/go-annotation/issues/2131))
are GOC; the pseudoenzyme handling is ours ([CONTESTED_FUNCTION](../../CONTESTED_FUNCTION.md),
[OVER_ANNOTATION_PATTERNS](../../OVER_ANNOTATION_PATTERNS.md), patterns 3 and 8).

<a id="rev-7"></a>
### REV-7. Measured activity is not automatically function

**For an enzyme activity that was assayed but is weak or promiscuous, decide whether the
protein evolved to catalyse it: a genuine secondary activity is `KEEP_AS_NON_CORE`; real in
vitro activity of unknown relevance is `MARK_AS_OVER_ANNOTATED`; noise-level activity of a
paralog, when a dedicated enzyme for the reaction exists in the organism, is `REMOVE`, even on
an IDA row.**

There is no numeric cutoff. State the judgement in the reason: what the kcat/Km or relative
rate was, what the physiological enzyme is, and whether any in vivo evidence links the gene to
the reaction. GOC precedent agrees on the principle that only physiologically relevant
reactions are annotated: EC-to-GO mappings for non-physiological reactions were removed while
the EC number was kept, and transpeptidation by gamma-glutamyltransferase was treated as an
assay artefact of a hydrolase ([go-annotation#1519](https://github.com/geneontology/go-annotation/issues/1519),
[go-annotation#1324](https://github.com/geneontology/go-annotation/issues/1324)).

Provenance: [GOC+]. The three tiers are ours ([CLAUDE.md](../../../CLAUDE.md),
[ENZYME_SPECIFICITY](../../ENZYME_SPECIFICITY.md)).

<a id="rev-8"></a>
### REV-8. Do not overrule an experimental curator from evidence you have not seen

**Never `REMOVE` an experimental row, or call it "wrong gene", "paralog mix-up" or "name
confusion", because the cached title or abstract is about something else. If you cannot verify
the evidence, use `UNDECIDED`; if the function is clearly right for the gene, `ACCEPT` and
defer.**

Curators who made an IDA, IMP, IGI or IPI read the full text. Many of this repository's
cached publications are abstract-only, and a paper's title often foregrounds one gene or a
paralog while the figures also assay the gene in question. Before asserting mis-attribution,
check the GO term's definition (an apparent mismatch is often a reading error: `G protein
activity` covers small GTPases) and the organism actually stated in the abstract. Reserve
confident "this paper is about organism X" caveats for cases the cached text states outright.

`REMOVE` on an experimental row remains correct in three cases: the function is contradicted
by later evidence; the row misreads an uncontested result ([REV-6](#rev-6), CREB1); or the
term's definition or a taxon constraint excludes the organism, which makes the error a term
choice rather than a reading of data. The RAR re-examination applied exactly this split to 958
kingdom-level candidates: 379 experimental rows were deferred to the curator and only those
excluded by definition or constraint were called wrong
([RAR_MISANNOTATION](../../RAR_MISANNOTATION.md)).

A deferral is not silence. Record why you could not decide and what would decide it (the
figure you could not see, the experiment that is missing).

Provenance: [NEW]. GOC guidance tells curators to remove annotations based on invalidated
hypotheses and to file a ticket against another group's errors
([wiki: Tips](https://wiki.geneontology.org/index.php/Tips_to_Produce_High_Quality_Annotations));
it does not address reviewers working without full text. Our rule adds the restraint
([CLAUDE.md](../../../CLAUDE.md)).

<a id="rev-9"></a>
### REV-9. Challenge an electronic or phylogenetic row by arguing with its source

**An IEA or IBA row may be removed on biological grounds, but the argument must address what
produced it: the InterPro2GO mapping and the signature's scope, the UniRule or ARBA condition
set, or the PAINT node at which the function was placed.**

For an IBA, the question is whether the target sits inside the clade that inherited the
function, and whether there is target-specific evidence of loss. Donor count is not strength:
a node seeded by one well-characterized gene can be sound, and the target appearing in its own
WITH/FROM is expected, not circular ([phylogenetic-propagation.md](phylogenetic-propagation.md),
[IBA_REVIEW](../../IBA_REVIEW.md)). For an InterPro2GO row, ask whether the mapped term holds for every
member of the signature; if not, the defect belongs to InterPro ([REV-17](#rev-17)).

*Example.* *C. elegans* STA-1 and STA-2 inherit `GO:0007259` cell surface receptor signaling
pathway via JAK-STAT by IBA from a STAT node that spans unikonts, but the worm has no JAK. The
rows are `REMOVE`, and the durable fix was a taxon constraint on the term, which GO added in
November 2026 ([TAXON_PATHWAY_VARIANCE](../../TAXON_PATHWAY_VARIANCE.md),
[ONT-17](ontology-change-and-taxa.md#ont-17)).

Provenance: [GOC+]. GOC rules on IEA age (GORULE:0000029) and IBA provenance (GORULE:0000026)
govern the pipeline ([Drive: GO rules update 2023](https://drive.google.com/open?id=1BAti-J62GG1ajan2sVK7M3Vzw6ZQol3syA-soAjiQjI));
the requirement to argue with the node or mapping is ours.

<a id="rev-10"></a>
### REV-10. Necessity is not participation

**A gene product is involved in a process only if it does some of the work: catalyses a step,
or supplies structure or chemistry that a step depends on. Being required for the process,
consumed by it, or the thing it acts on is not participation.**

Knockout abolishes the outcome; rescue restores it. Both are equally true of a substrate. A GAF
row cannot distinguish necessity evidence from participation evidence, so ask explicitly which
entity performs the step. The 2018 QC call listed "annotating a cargo or target to a process"
among the recurring error classes
([wiki: QCQA call 2018-03-20](https://wiki.geneontology.org/index.php/QCQA_call_2018-03-20)).

*Example.* `GO:0002003` angiotensin maturation is a subclass of `GO:0016486` peptide hormone
processing (verified). It is annotated to the proteases (REN, ACE, ACE2 and others) and to no
angiotensinogen in human, mouse or rat. A review that proposed it for AGT as a missing
annotation was wrong: AGT supplies no residue beyond the cleaved bond and catalyses nothing.
The convention has principled exceptions where the substrate does work: thyroglobulin is a
scaffold for thyroid hormone generation, fibrin a cofactor in fibrinolysis, C3 the chemistry
of complement activation ([CLAUDE.md](../../../CLAUDE.md), worked example from
`genes/human/AGT`).

Apply the same test to existing rows: a `REMOVE` or `MARK_AS_OVER_ANNOTATED` is due when the
only evidence is necessity and the gene is the cargo, substrate or target.

Provenance: [NEW], sharpening the GOC's downstream-process and cargo guidance.

<a id="rev-11"></a>
### REV-11. `NEW` is the one action that manufactures a claim; hold it to a higher bar

**Propose a new annotation only with direct evidence of the gene doing the work, after naming
the entity that performs the step, running a comparator check, reading the term's parents and
checking existing GO-CAM models. Never propose a term that is an ancestor or descendant of
another proposed or existing term on the gene.**

The comparator check turns "the curators missed it" into a falsifiable prediction: name two or
three gene products in the same role relative to the same kind of process and see whether they
carry the term. A systematic absence across species and MODs is a convention to identify, not
a twenty-year oversight. INS is absent from insulin processing; POMC, GCG and PENK are absent
from peptide hormone processing; APP is absent from amyloid-beta formation. All three absences
say the same thing: the processing term belongs to the enzymes ([REV-10](#rev-10)).

A GO-CAM that includes the gene in a different role is a curator decision to argue with
explicitly, not a gap. When a substrate relationship needs to be machine-readable, it goes on
the enzyme as `has_input`, raised as a suggested question rather than asserted on the
substrate.

A limitation of this repository's tooling: `NEW` is rejected for any term already in the gene's
GOA, even when the existing row is electronic and the reviewer has species-specific
experimental evidence. Record such an upgrade in the existing row's `reason` and `supported_by`.

Provenance: [GOC+]. GOC guidance asks for few, informative annotations; the participation test
and comparator check are ours ([CLAUDE.md](../../../CLAUDE.md)).

<a id="rev-12"></a>
### REV-12. An ND row is a statement about the literature

**`ACCEPT` an ND root-term row when no literature on this gene product, in this species,
identifies a function in that aspect, and cite the search. Remove it (or `MODIFY` it) only when
such literature exists, quoting the paper.**

ND (`GO_REF:0000015`) says a curator searched and found nothing to annotate. GORULE:0000011
restricts ND to the three root terms and the roots to ND
([Drive: GO rules update 2023](https://drive.google.com/open?id=1BAti-J62GG1ajan2sVK7M3Vzw6ZQol3syA-soAjiQjI)).
IBA, ISO, ISS or IEA rows in the same aspect are not literature on the gene and do not make an
ND stale. A bare protein-binding IPI does not either; an ortholog paper does not; an NAS or a
Reactome TAS on the gene itself does. `KEEP_AS_NON_CORE`, `MARK_AS_OVER_ANNOTATED` and
`TOO_GENERAL` are never used on an ND, and a `NEW` ND is never proposed. Record why there is
no data (`nd_case`), and pair a true gap with a biology knowledge gap
([evidence-codes.md](evidence-codes.md), [NO_DATA](../../NO_DATA.md)).

Provenance: [GOC+].

<a id="rev-13"></a>
### REV-13. Remove bare protein binding; look for the informative function behind it

**A row on `GO:0005515` protein binding identifies no function. Remove it under the
protein-binding policy, and where the interaction evidence supports something informative (an
adaptor, a ligase-binding, a receptor-binding or a complex-binding term), propose that instead.**

The GOC recommends avoiding protein binding when more precise annotations can be made
([wiki: Tips](https://wiki.geneontology.org/index.php/Tips_to_Produce_High_Quality_Annotations)),
decided that protein binding should not be propagated by PAINT
([go-annotation#2097](https://github.com/geneontology/go-annotation/issues/2097)), filters NOT
annotations to binding and protein binding (GORULE:0000002), and was implementing a filter for
ISS and IEA binding rows in 2024 (GORULE:0000005)
([Drive: GO rules 2024](https://drive.google.com/open?id=1CmnWtTKkx8Qo3e7XNEFfafZYTGTrJq7DcqRVBdB7lzM)).
Descendants such as enzyme binding are informative and follow the normal rules. Projects with
their own standing instructions (the ClinGen Mendelian project) may keep supported generic
binding as non-core when nothing more specific is evidenced. Details:
[molecular-function.md](molecular-function.md).

Provenance: [GOC+].

<a id="rev-14"></a>
### REV-14. A NOT must exclude the function; propose NOTs where errors will recur

**Keep an existing NOT only when its negative result rules the function out, not when it
merely failed to detect it. Where a review removes a pipeline-predicted activity the protein
demonstrably lacks, consider proposing a NOT, since only a NOT stops the prediction from
returning.**

*Example.* ARL3 carried `NOT|located_in` `GO:0005929` cilium from an overexpression screen of
tagged GTPases in serum-starved cells. That showed tagged ARL3 is not enriched in cilia under
one condition; ARL3-GTP is made inside the cilium by its ciliary GEF, and endogenous ARL3
stains cilia. The NOT was removed ([TOP_NOTS](../../TOP_NOTS.md), NOT_NOTs section).

`REMOVE` on a NOT row doubts the negative claim without asserting the positive one, so removing
both a term and its NOT is consistent. `TOO_GENERAL` is never used on a NOT: a NOT on a broad
term is the strongest negative claim. GO taxon constraints do not apply to NOT annotations
([Drive: Taxon Constraints for Signaling Pathways](https://drive.google.com/open?id=117j8ysvt6FpVR0KCeFgrRDjUjm3jVXm8-nNReVU-hEg)).
The NOT candidates from pseudoenzymes and "is phosphorylated" misreadings (DnaJ proteins and
ATP binding, UEV domains and E2 activity) are listed in [TOP_NOTS](../../TOP_NOTS.md); none has
yet been verified and submitted. See [qualifiers-and-negation.md](qualifiers-and-negation.md).

Provenance: [GOC+]. The IEA working group lists NOT-aware logic blocks as a desirable pipeline
mechanism ([Drive: Mechanisms for decreasing erroneous & overkill of annotations](https://drive.google.com/open?id=10xAYIWTCFyN2bzxBnijErWf9CTsuX5N4jBI7GVLB9KM));
the exclusion test is ours.

<a id="rev-15"></a>
### REV-15. A retraction is a source failure; scope the response to the evidence line

**Flag a retracted reference, cite the notice, and then ask what rests on it. If the retracted
paper is the sole evidence for an annotation, the row becomes `UNDECIDED` or a proposed
`REMOVE` with the retraction cited and sent upstream. Do not mass-remove a gene's annotations
because one paper was retracted.**

Retractions are issued for image duplication, statistics, misconduct and honest error, and a
notice often affirms part of the work. An expression of concern questions a record without
withdrawing it; an erratum is usually benign. The first full scan of this repository (25,088
distinct PMIDs) found 7 retracted papers, 4 of them under a GO annotation, and none supporting
an accepted core function: the recorded actions were `REMOVE` (TP53, a `GO:0005515` IPI),
`KEEP_AS_NON_CORE` (mouse Mtor, BACE1) and `UNDECIDED` (STAT3), each reached on biological
grounds before the retraction was known ([RETRACTIONS](../../RETRACTIONS.md)).

Procedure: set `is_invalid: true` with `correctness: DISPUTED` and the notice in
`review_notes`; add the notice as its own reference; then sort citation sites. A citation in
the reference list only is bibliographic cleanup. A `supporting_text` quote from a retracted
paper must not be load-bearing; find independent support. An `original_reference_id` is the
real case: look for independent corroboration and say so in the reason if it exists.
Retraction status changes after a review is written, so the check must be re-run, not done once.

Provenance: [GOC+]. The GOC discussed handling retractions in December 2023 and specified
GORULE:0000022 to filter annotations to retracted publications; its implementation was on hold
pending a way to query external sources during the pipeline run
([wiki: Annotation Conf. Call 2023-12-12](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2023-12-12),
[wiki: Ontology meeting 2023-12-11](https://wiki.geneontology.org/index.php/Ontology_meeting_2023-12-11),
[Drive: GO rules 2024](https://drive.google.com/open?id=1CmnWtTKkx8Qo3e7XNEFfafZYTGTrJq7DcqRVBdB7lzM)).
We recommend against a blanket filter; see Differences.

<a id="rev-16"></a>
### REV-16. A miscitation is a defect in the citation, not in the biology; key it on the citation

**When an annotation's reference resolves to a different paper (`WRONG_IDENTIFIER`) or the
right paper does not say what it is cited for (`MISCITED`), keep GOA's
`original_reference_id`, record the finding in `reference_review`, judge the claim on whatever
real evidence exists, and check where else the same citation is used.**

Validators check that a title matches its PMID and that a quote occurs in the paper. A wrong
PMID imported together with its own title passes both. Bad citations are rarely confined to one
gene: they are copied across paralogs and complex partners. Seven of the twenty distinct
`WRONG_IDENTIFIER` citations in this repository's register affect more than one gene, and 26 of
27 such rows came from GOA rather than from reviews here ([MISCITATION_AUDIT](../../MISCITATION_AUDIT.md)).

Failure modes seen: an off-by-one symbol (a `protein farnesylation` IDA on COX17 citing a COX10
paper; the term is wrong even for COX10, which farnesylates heme), paralog substitution
(ELOVL1, ELOVL2 and ELOVL3 citing a paper that cloned "HELO1", i.e. ELOVL5), symbol collision
(ADPRH citing a paper whose "ARH1" is a different gene), and wholly unrelated papers. Spread is
a triage queue, not a verdict: the ELOVL5 paper is correctly cited on ELOVL5.

For a deleted duplicate PMID, record the verified canonical identifier in
`reference_review.replacement` and quote the canonical paper under its own id. A fetch failure
alone establishes neither replacement nor retraction ([reference curation](../../../docs/reference_curation.md)).
When P2 contradicts a finding in P1, record it on P1's finding (`finding_review`, `DISPUTED` or
`OVERTURNED`) rather than condemning the whole paper.

Provenance: [NEW]. The GOC's ticket guidelines ask for specifics and PMIDs in correction
requests ([go-annotation CONTRIBUTING](https://github.com/geneontology/go-annotation/blob/master/CONTRIBUTING.md));
the citation-keyed register is ours.

<a id="rev-17"></a>
### REV-17. Record upstream errors as structured source defects, addressed to whoever can fix them

**When the error is in the source record, add a `source_defects` entry that names the defect
type, the responsible resource, the asserted and corrected values, a confidence and a
self-contained explanation. The review action says what this repository does; the defect says
what the source should do.**

The resource is the group that can make the fix, which is usually not GOA:

| The fix changes... | Resource |
|---|---|
| a curated GAF row | the `assigned_by` group (MGI, TAIR, SGD, UniProt...) |
| the content of an InterPro2GO mapping or a signature description | `INTERPRO`, naming the mapping in `record` |
| GOA's application of a correct mapping (a 51-residue fragment that got the row) | `GOA_EBI` |
| a term on a PANTHER node propagated by TreeGrafter | `PANTHER` |
| a PAINT IBD/IBA assertion | `GO_CENTRAL` |
| a term's label, definition or placement | `GOC` |
| a GO-CAM activity | `GO_CAM`, with the activity id in `record` |

*Example.* A GO-CAM gave an H4K5 acetyltransferase activity `enabled_by` SCL27, a GRAS
protein that shares the alias HAM1 with the MYST acetyltransferase HAM1; the cited papers study
the MYST protein. The defect is `WRONG_GENE_PRODUCT`, `slot: enabled_by`, `REPOINT` from
AT2G45160 to AT5G64610, `cause: SYMBOL_COLLISION`, `confidence: CONFIRMED`
([source defects](../../../docs/source_defects.md)).

Typed causes make patterns countable: `OVER_PROPAGATION` (fix the node, not the inherited
rows), `SCOPE_OVER_REACH` (a mapping applied across a taxon boundary), `LABEL_WITHOUT_DEFINITION`,
`SPECULATION_AS_ASSERTION` ("may function as" became an assertion), and `PRACTICE_CHANGE` (a
dated cohort sharing one convention, fixable in bulk). The mapping-versus-row distinction has
been reopened repeatedly in practice; check the filing whenever the fix is a mapping, whatever
the row's `assigned_by` says.

Provenance: [GOC+]. The GOC routes UniProt keyword and HAMAP issues to UniProt and GOA issues
to GOA ([go-annotation CONTRIBUTING](https://github.com/geneontology/go-annotation/blob/master/CONTRIBUTING.md)),
and asks curators to file tickets against other groups' errors
([wiki: Tips](https://wiki.geneontology.org/index.php/Tips_to_Produce_High_Quality_Annotations)).
The structured record is ours.

<a id="rev-18"></a>
### REV-18. Every row needs term-specific reasoning and independent, verbatim support

**Each row's `summary` and `reason` must be about that term, and each `supporting_text` must be
a verbatim quote from a source that independently supports the claim. Boilerplate reasons,
placeholder quotes, the gene's own GOA file and restated UniProt labels are not support.**

A generation pass once filled every row of mouse Fyn, Egfr, Grb2, Cbl and Egf with a handful of
templated reasons and a placeholder quote ("deep research report reviewed for GO term
specificity..."). The action labels looked plausible and carried no curation; Fyn also held
contradictory `REMOVE`/`ACCEPT` pairs on its core terms. All were re-reviewed, and the detector
now runs as a smell test ([REVIEW_QUALITY_AUDIT](../../REVIEW_QUALITY_AUDIT.md)).

What does not count:

- the gene's `-goa.tsv` (it says what is annotated, never why it is true; citing it is a
  blocking error), or another gene's GOA file as comparator evidence (argue comparators in prose);
- UniProt protein names, EC numbers, keywords and `DR GO` lines, which restate annotations;
- UniProt statements whose only evidence is an ARBA rule, submitter import (`ECO:0000313`) or a
  machine-generated name, which repeat a prediction;
- the protein existence level, as support for `ACCEPT`, `NEW` or a core function;
- your own notes or a deep-research summary as if it were literature.

Curated UniProt text tied to a publication, family classification and sequence-analysis
features (signal peptides, TM helices) are valid support for what they say
([CLAUDE.md](../../../CLAUDE.md)).

Provenance: [NEW].

<a id="rev-19"></a>
### REV-19. Know what the gorules already enforce, and do not mistake passing them for review

**Treat a gorule failure on a row as a prompt to review it; treat a gorule pass as no evidence
of correctness. Understand which rules filter and which only warn.**

GO rules run when GAF or GPAD files are loaded. Errors are filtered from GO products; warnings
are reported and kept; some failures are repaired automatically, notably obsolete terms with a
`replaced_by` (GORULE:0000020) and aspect mismatches (GORULE:0000028)
([wiki: GO Central QC Procedure](https://wiki.geneontology.org/index.php/GO_Central_%28GOC%29_QC_Procedure),
[Drive: GO rules update 2023](https://drive.google.com/open?id=1BAti-J62GG1ajan2sVK7M3Vzw6ZQol3syA-soAjiQjI)).
Rules a reviewer meets most often:

| Rule | Check | Outcome |
|---|---|---|
| GORULE:0000002 | NOT annotations to binding and protein binding | filter |
| GORULE:0000007 | IPI used for catalytic activity or its descendants | filter |
| GORULE:0000008 | annotation to a `gocheck_do_not_annotate` term | warning |
| GORULE:0000011 | ND only on root terms, roots only with ND | filter |
| GORULE:0000013 | taxon constraint violation | non-experimental filtered; experimental reported, kept |
| GORULE:0000020 | obsolete or merged term with `replaced_by` | repair |
| GORULE:0000029 | IEA older than one year (warning) or three years (filter) | warning/filter |
| GORULE:0000022 | reference retracted | specified; implementation on hold (2023-24) |

The `gocheck_do_not_annotate` subset absorbed the former do-not-manually-annotate subset in
2024 and holds terms that are not wrong but uninformative (`GO:0005488` binding,
`GO:0006810` transport, `GO:0050896` response to stimulus); an `obsoletion_candidate` subset
gives early warning of terms about to go ([wiki: Annotation Conf. Call 2024-03-12](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2024-03-12)).
A row on a do-not-annotate term is usually `MODIFY` (if the evidence supports a specific term)
or `MARK_AS_OVER_ANNOTATED`.

Provenance: [GOC].

<a id="rev-20"></a>
### REV-20. An obsoletion-driven review ticket is a review of claims, not a find-and-replace

**When a `go-annotation` review ticket lists your group's annotations to a term being
obsoleted, decide each row on its biology: some move to the suggested term, some to a different
term, and some are deleted because the obsolete term was the only thing making them look right.**

The standard ticket names the obsoletion reason, links the ontology ticket, attaches a
spreadsheet of experimental annotations by group and lists the mappings (InterPro2GO, UniProt
keywords, UniRule) to review
([go-annotation issue template](https://github.com/geneontology/go-annotation/blob/master/.github/ISSUE_TEMPLATE/annotation-review-for-obsoletion.md)).
Groups get at least seven days after notification, longer for large re-annotation
([wiki: Obsoleting an Existing Ontology Term](https://wiki.geneontology.org/index.php/Obsoleting_an_Existing_Ontology_Term)).
Precedents show the range of outcomes: `colocalizes_with` on complex terms became complex
binding or was removed when no interaction evidence existed
([go-annotation#1940](https://github.com/geneontology/go-annotation/issues/1940)); `occurs_at`
extensions were moved per pattern, and Pfam targets dropped
([go-annotation#2584](https://github.com/geneontology/go-annotation/issues/2584)). How to
choose among the obsolete term's `replaced_by` and `consider` targets is in
[ontology-change-and-taxa.md](ontology-change-and-taxa.md#ont-3).

Provenance: [GOC].

## Decision aid

Work through these in order for each row; stop at the first that applies.

| Question | If yes |
|---|---|
| Is the term bare `GO:0005515`? | `REMOVE` under the policy; propose an informative MF if evidence allows ([REV-13](#rev-13)) |
| Is it an ND on a root term? | Apply [REV-12](#rev-12): `ACCEPT` with search cited, or stale |
| Is it a NOT? | Keep only if the result excludes the function ([REV-14](#rev-14)) |
| Is the gene the substrate, cargo, target or a non-catalytic subunit? | `REMOVE` or `MARK_AS_OVER_ANNOTATED` ([REV-6](#rev-6), [REV-10](#rev-10)) |
| Experimental row, and you lack the full text or the abstract is about another gene? | `UNDECIDED` or defer-`ACCEPT`; never "wrong gene" ([REV-8](#rev-8)) |
| Is the claim contradicted by better evidence? | `REMOVE`; propose NOT if pipelines will re-predict it |
| Electronic/IBA row outside the clade or signature scope where it holds? | `REMOVE`; record the source defect at the node or mapping ([REV-9](#rev-9), [REV-17](#rev-17)) |
| Does the term name an assay readout or a downstream effect? | `MARK_AS_OVER_ANNOTATED` ([REV-5](#rev-5)) |
| Assayed activity of doubtful physiological relevance? | Tiers in [REV-7](#rev-7) |
| True, but this row's evidence supports a specific descendant? | `MODIFY` with that descendant ([REV-3](#rev-3)) |
| True, imprecise on its own, and a specific asserted term entails it? | `TOO_GENERAL` |
| True, as precise as warranted, and part of the core? | `ACCEPT` |
| True, as precise as warranted, peripheral? | `KEEP_AS_NON_CORE` |
| Is the reference retracted or miscited? | Act on the citation first ([REV-15](#rev-15), [REV-16](#rev-16)), then judge the claim on the remaining evidence |

Then check the set: same-term rows consistent, no positive term kept beside a NOT on it or an
ancestor, every `MODIFY` replacement supported by that row's evidence, core functions matching
the `ACCEPT` rows.

## Common errors

| Error | Example | Fix |
|---|---|---|
| `REMOVE` used to deduplicate | IEA removed beside an accepted IDA on the same term | Same action family on all rows ([REV-1](#rev-1)) |
| `REMOVE` on a true but broad term | `GO:0016787` hydrolase activity removed beside a specific phospholipase term | `MODIFY` if the row's evidence supports the child; otherwise keep ([REV-3](#rev-3)) |
| Action contradicts reason | `ACCEPT` with a reason saying the term is too general | Change the action to match the argument |
| Overruling the curator from a title | IDA called a paralog mix-up because the cached abstract names the paralog | `UNDECIDED` ([REV-8](#rev-8)) |
| Substrate given the enzyme's process | angiotensinogen proposed for angiotensin maturation | Name who performs the step ([REV-10](#rev-10)) |
| "Is phosphorylated" read as kinase activity | CREB1 protein phosphorylation IDA | `REMOVE`, quote the paper ([REV-6](#rev-6)) |
| Assembly factor given the complex activity | SURF1 cytochrome-c oxidase activity | `REMOVE`; consider NOT |
| Retraction triggers wholesale removal | every row on a gene removed after one notice | Scope to the evidence line ([REV-15](#rev-15)) |
| Mapping defect filed against GOA | IPR mapping scope filed as `GOA_EBI` with no `record` | `INTERPRO`, name the mapping ([REV-17](#rev-17)) |
| Boilerplate reasoning | same reason and placeholder quote on 200 rows | Re-review row by row ([REV-18](#rev-18)) |
| Citing the GOA file as support | `supported_by` pointing at `GENE-goa.tsv` | Quote the paper or record behind the row |
| Stale ND removed because an IBA exists | ND on MF removed "as an IBA now covers MF" | `ACCEPT`; IBA is not literature on the gene ([REV-12](#rev-12)) |
| Uninformative tissue CC on a shuttling factor | cytoplasm rows on an inactive cytoplasmic pool | `MARK_AS_OVER_ANNOTATED` ([REV-4](#rev-4)) |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [wiki: Tips to Produce High Quality Annotations](https://wiki.geneontology.org/index.php/Tips_to_Produce_High_Quality_Annotations) | Remove annotations based on invalidated hypotheses; GO is not an archive | Same, but a reviewer without full text must not remove experimental rows on suspicion; use `UNDECIDED` | Many cached sources are abstract-only, and titles often foreground a paralog that the figures do not ([REV-8](#rev-8)) |
| GOC curation tools (Noctua, Protein2GO) | Keep, edit, delete, or add NOT | A graded vocabulary that separates false, over-reaching, broad, peripheral and undecidable | "Delete" conflates distinct judgements; the distinction matters for upstream feedback ([REV-2](#rev-2)) |
| [OVER_ANNOTATION_PATTERNS](../../OVER_ANNOTATION_PATTERNS.md), pattern 2 | Broad enzyme terms: "REMOVE or MODIFY to more specific child terms" | `MODIFY` only if this row's evidence supports the child; otherwise keep; never `REMOVE` a true term | 2026-11-14 maintainer ruling; `REMOVE` asserts falsehood ([REV-3](#rev-3)) |
| `ActionEnum` docstring for `TOO_GENERAL` (repo schema) | Term true but entailed by a more specific asserted term | Same, narrowed to terms imprecise on their own (membrane); a respectable term such as GPCR activity is kept | Two reviews read the docstring in opposite ways; earlier reviews are not retroactively defective ([CLAUDE.md](../../../CLAUDE.md)) |
| [OVER_ANNOTATION_PATTERNS](../../OVER_ANNOTATION_PATTERNS.md), pattern 1 | Remove protein binding "when more specific functional annotations exist or when interactions are from HTP screens" | Remove bare `GO:0005515` regardless; look for the informative MF; project-specific exceptions documented | Policy now term-level rather than conditional ([REV-13](#rev-13)) |
| [Drive: GO rules 2024](https://drive.google.com/open?id=1CmnWtTKkx8Qo3e7XNEFfafZYTGTrJq7DcqRVBdB7lzM) (GORULE:0000022) | Filter annotations to retracted publications | Flag the citation; act only on rows whose sole evidence is the retracted paper; `UNDECIDED` or a proposed `REMOVE` sent upstream | None of the four retraction-backed annotations found here was a core function, and notices often affirm part of a paper ([REV-15](#rev-15)) |
| [wiki: QCQA call 2018-03-20](https://wiki.geneontology.org/index.php/QCQA_call_2018-03-20) | Need "a list of blacklisted papers and retractions" | A periodic retraction scan with citation-site attribution, separating retraction, expression of concern and erratum | A blacklist cannot tell a reference-list citation from an annotation's sole evidence ([RETRACTIONS](../../RETRACTIONS.md)) |
| [wiki: Annotating downstream processes](https://wiki.geneontology.org/index.php/Annotating_downstream_processes) (flagged "to be reviewed") | Annotate to the experimental evidence, using judgement about core genes; request "X involved in Y" terms for downstream effects | Downstream rows are over-annotation unless the evidence shows participation; do not request precomposed terms | GO has obsoleted 1,265 "X involved in Y" terms, 883 with a comment pointing to GO-CAM ([INVOLVED_IN_PRECOMPOSITION](../../INVOLVED_IN_PRECOMPOSITION.md)) ([REV-5](#rev-5), [ONT-12](ontology-change-and-taxa.md#ont-12)) |
| GOC evidence-code documentation (2007 onward) | Evidence codes are not quality measures | Agree, and extend: rows sharing a term are one claim and get one verdict | The code-agnostic view has to reach the review actions, or reviewers remove IEAs to "clean up" ([REV-1](#rev-1)) |
| [Drive: Taxon Constraints for Signaling Pathways](https://drive.google.com/open?id=117j8ysvt6FpVR0KCeFgrRDjUjm3jVXm8-nNReVU-hEg) (GORULE:0000013) | Experimental violations are reported and kept | A reviewer may call an experimental row wrong when the definition or constraint excludes the organism, after checking the constraint is not too narrow | The error is then a term choice, not a reading of data ([REV-8](#rev-8), [ONT-17](ontology-change-and-taxa.md#ont-17)) |
| [MISCITATION_AUDIT](../../MISCITATION_AUDIT.md) (internal) vs GOC ticket practice | GOC tickets correct one row at a time | Key citation defects on the citation, and check every gene that cites it | One bad PMID is usually copied across paralogs and partners ([REV-16](#rev-16)) |
| [TOP_NOTS](../../TOP_NOTS.md) and GOC practice | NOT annotations are made from published negative results | Also review existing NOTs: a failure to detect is not exclusion, and 11 of 295 NOTs here were overturned | A weak NOT blocks correct positive annotations ([REV-14](#rev-14)) |

Sources disagree internally in two places. Our own over-annotation catalogue predates the
2026-11-14 ruling on `TOO_GENERAL`/`MODIFY` and still says "REMOVE or MODIFY"; the ruling
governs. And the GOC's Tips page tells curators to remove outdated annotations while the GOC's
own QC rule keeps experimental taxon-constraint violations; both are reasonable, and this
document resolves them by letting the reviewer remove only when the error is in the term choice.

## Open questions

1. Should the GOC adopt a graded review vocabulary in its tools (at least separating "false"
   from "true but uninformative"), so that review outcomes can be fed back without collapsing to
   delete?
2. GORULE:0000022: should annotations whose only evidence is a retracted paper be filtered,
   flagged, or left to the assigning group? We recommend flag-and-review.
3. Is there a principled cutoff for "noise-level" promiscuous activity ([REV-7](#rev-7)), or
   must it stay a stated judgement?
4. How should a reviewer express "the term is right, but the evidence code understates
   species-specific experimental evidence"? This repository's tooling cannot record it as
   `NEW`, and the GAF has no upgrade mechanism.
5. Should NOT annotations be proposed systematically for pseudoenzymes whose active-site loss is
   structurally established, even without a published negative assay?
6. Display versus annotation for highly annotated genes: if the annotation set is correct but
   overwhelming, is the fix a better review or a better display? The 2024 sessions left this open.
7. Should IBA rows that duplicate a gene's own experimental annotation be shown to users, given
   that they are correct by construction?

## Sources

**GO wiki**

- [wiki: Tips to Produce High Quality Annotations](https://wiki.geneontology.org/index.php/Tips_to_Produce_High_Quality_Annotations) (reviewed 2025-11)
- [wiki: Annotating downstream processes](https://wiki.geneontology.org/index.php/Annotating_downstream_processes) (flagged for review)
- [wiki: GO Central (GOC) QC Procedure](https://wiki.geneontology.org/index.php/GO_Central_%28GOC%29_QC_Procedure)
- [wiki: Annotation Conf. Call 2024-03-12](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2024-03-12) (do-not-annotate subsets)
- [wiki: Annotation Conf. Call 2023-12-12](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2023-12-12) (retractions)
- [wiki: Ontology meeting 2023-12-11](https://wiki.geneontology.org/index.php/Ontology_meeting_2023-12-11) (GORULE:0000022 on hold)
- [wiki: QCQA call 2018-03-20](https://wiki.geneontology.org/index.php/QCQA_call_2018-03-20)
- [wiki: Obsoleting an Existing Ontology Term](https://wiki.geneontology.org/index.php/Obsoleting_an_Existing_Ontology_Term)

**GO Consortium Drive**

- [Drive: GOC 2023-10 / GO rules update](https://drive.google.com/open?id=1BAti-J62GG1ajan2sVK7M3Vzw6ZQol3syA-soAjiQjI)
- [Drive: GOC 2024-05 / GO rules](https://drive.google.com/open?id=1CmnWtTKkx8Qo3e7XNEFfafZYTGTrJq7DcqRVBdB7lzM)
- [Drive: GOC 2023-04 / Taxon Constraints for Signaling Pathways](https://drive.google.com/open?id=117j8ysvt6FpVR0KCeFgrRDjUjm3jVXm8-nNReVU-hEg)
- [Drive: GOC Fall 2024 / Highly annotated genes, C. elegans daf-16](https://drive.google.com/open?id=1YhRirPCkc9Pl0gOC3Mhc5Zn0VK8SGHEOO-BeI6pwAGk)
- [Drive: GOC Fall 2024 / Highly annotated genes, MTOR](https://drive.google.com/open?id=1Ha8AyFN9WndsT6UPPUnMYawzdn-dnqCG)
- [Drive: IEA WG 2025-10 / Mechanisms for decreasing erroneous & overkill of annotations](https://drive.google.com/open?id=10xAYIWTCFyN2bzxBnijErWf9CTsuX5N4jBI7GVLB9KM) (suggestions, not adopted rules)
- [Drive: old GOC minutes / evCode-summary](https://drive.google.com/open?id=1qZm_e_wnfu_yUAg7qbwrJpYwyRRNqD_7) (archived, 2007)

**GitHub issues and files (geneontology/go-annotation)**

- [go-annotation#1324](https://github.com/geneontology/go-annotation/issues/1324) (assay-artefact activity)
- [go-annotation#1519](https://github.com/geneontology/go-annotation/issues/1519) (non-physiological EC mappings)
- [go-annotation#1940](https://github.com/geneontology/go-annotation/issues/1940) (`colocalizes_with` on complexes)
- [go-annotation#2097](https://github.com/geneontology/go-annotation/issues/2097) (no PAINT protein binding)
- [go-annotation#2131](https://github.com/geneontology/go-annotation/issues/2131) (GORULE:0000007)
- [go-annotation#2584](https://github.com/geneontology/go-annotation/issues/2584) (`occurs_at` review)
- [go-annotation CONTRIBUTING](https://github.com/geneontology/go-annotation/blob/master/CONTRIBUTING.md)
- [go-annotation issue template: annotation review for obsoletion](https://github.com/geneontology/go-annotation/blob/master/.github/ISSUE_TEMPLATE/annotation-review-for-obsoletion.md)

**Repository pages**

- [CLAUDE.md](../../../CLAUDE.md) (review guidelines, curator deference, NEW bar, ND, IBA, references)
- [action consistency](../../../docs/action_consistency.md)
- [source defects](../../../docs/source_defects.md)
- [reference curation](../../../docs/reference_curation.md)
- [OVER_ANNOTATION_PATTERNS](../../OVER_ANNOTATION_PATTERNS.md)
- [REVIEW_QUALITY_AUDIT](../../REVIEW_QUALITY_AUDIT.md)
- [RETRACTIONS](../../RETRACTIONS.md)
- [MISCITATION_AUDIT](../../MISCITATION_AUDIT.md)
- [CONTESTED_FUNCTION](../../CONTESTED_FUNCTION.md)
- [TOP_NOTS](../../TOP_NOTS.md)
- [RAR_MISANNOTATION](../../RAR_MISANNOTATION.md)
- [TAXON_PATHWAY_VARIANCE](../../TAXON_PATHWAY_VARIANCE.md)
- [ORGANELLES](../../ORGANELLES.md)

GO term ids and labels were checked against the local `sqlite:obo:go` build (2026-11-03); the
subclass claim for `GO:0002003` under `GO:0016486` was checked with `runoak ancestors`.
