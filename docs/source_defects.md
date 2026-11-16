# Source defects: recording errors that live upstream

A review sometimes finds that the error is in the **source record**, not in
this repository's understanding. Examples:

- an annotation or GO-CAM activity attached to the wrong gene ("that gene,
  not this gene"), often through a shared symbol or a legacy alias;
- an annotation keyed to a reference that does not support it;
- an experimental evidence code on a review or meeting report, or a missing `NOT`;
- an isoform established in the literature that the reviewed UniProt entry does
  not list.

The review `action` says what this repository does with the claim (for
example `REMOVE` or `UNDECIDED`). `source_defects` says what the **source**
should fix, in a form from which a report to that resource can be generated.

## Where it goes

- Gene reviews: `existing_annotations[].review.source_defects`. The defective
  record is the GOA/MOD row described by the enclosing annotation, so `record`
  is usually left unset.
- GO-CAM reviews: `activity_reviews[].source_defects`. Set `record` to the
  activity id.
- Functional isoforms: `functional_isoforms[].source_defects`, for a defect in
  the source's record of that isoform. Set `record` to the UniProt accession.
- Cited source text: `references[].reference_review.source_defects`, for an
  error in a source's own curated text: a MOD gene description (cited as its
  `-deep-research-<mod>.md` file) or a UniProt FUNCTION or other comment (cited
  as the `-uniprot.txt` file). Set `record` to the source record (`WB:WBGene...`,
  `UniProtKB:...`) and `slot` to the field (`MOD_provided_gene_description`,
  `CC:FUNCTION`). Use `WRONG_STATEMENT` for a claim the literature contradicts,
  `OUTDATED_STATEMENT` for one that has been superseded ("novel protein", "no
  obvious function in RNAi assays"), and `MISSING_STATEMENT` for content the
  source has lost or omits. For the first two, `asserted_value` is the
  offending sentence copied verbatim from the cited file, run-together words
  included, and `requested_change` is `CHECK`, with the explanation saying what
  the text should say. Validation warns when the value is not found in the file
  (`statement_defect_not_in_source`). For `MISSING_STATEMENT`, as for
  `MISSING_ISOFORM`, nothing wrong is asserted: `asserted_value` repeats
  `record` and `requested_change` is `ADD`. An error in an Alliance *automated* description
  usually comes from the GO annotations it is generated from. Record it on
  those annotation rows, not on the text, unless the text itself is the fault
  (for example, function sentences lost between releases, which is
  `resource: ALLIANCE`).

## Fields

| Field | Required | Meaning |
|---|---|---|
| `defect_type` | yes | `WRONG_GENE_PRODUCT`, `WRONG_REFERENCE`, `WRONG_TERM`, `WRONG_EVIDENCE_CODE`, `MISSING_NEGATION`, `WRONG_WITH_FROM`, `WRONG_QUALIFIER`, `WRONG_CAUSAL_RELATION`, `WRONG_STATEMENT`, `OUTDATED_STATEMENT`, `MISSING_STATEMENT`, `MISSING_ISOFORM`, `DUPLICATE_ASSERTION`, `OTHER` |
| `resource` | yes | Who must fix it. For a GOA row this is the `assigned_by` group (`TAIR`, `MGI`, ...), not GOA. A GO-CAM model is `GO_CAM`. Pipelines and non-MOD resources have their own values too - see [Choosing a resource](#choosing-a-resource). |
| `record` | no | Id of the defective record when it is not the enclosing annotation. |
| `slot` | no | The field holding `asserted_value`, in the source's own terms: `enabled_by` or `has_input` for a GO-CAM activity; `DB_Object_ID`, `DB:Reference`, `With/From`, `Evidence_Code` or `Qualifier` for a GAF row. |
| `requested_change` | no | `REPOINT` (replace with `corrected_value`), `DELETE_VALUE` (drop the value, keep the record), `DELETE_ROW`, `ADD` (add `corrected_value`, which the record lacks), or `CHECK` (the right change depends on information we could not see; the explanation gives the alternatives). |
| `asserted_value` | yes | What the source says now, as a CURIE (`AGI_LocusCode:AT2G45160`, `PMID:32213638`). For `requested_change: ADD` nothing wrong is asserted, so this names the record that lacks the value (the same CURIE as `record`, e.g. `UniProtKB:Q96PV0` for a missing isoform); group `ADD` rows separately when analysing asserted values. |
| `corrected_value` / `corrected_label` | no | What it should say, when known. Leave unset when the value is wrong but the right one is unknown. |
| `cause` | no | `SYMBOL_COLLISION`, `LEGACY_ALIAS`, `IDENTIFIER_TRANSPOSITION`, `SEQUENCE_MISMAPPING`, `CONTAMINANT`, `OVER_PROPAGATION`, `SCOPE_OVER_REACH`, `LABEL_WITHOUT_DEFINITION`, `SPECULATION_AS_ASSERTION`, `PRACTICE_CHANGE`, `OTHER`, `UNKNOWN`. The first five are gene-identity confusions; the next five are pipeline and process mechanisms - see [Choosing a cause](#choosing-a-cause). |
| `confidence` | yes | `CONFIRMED` (file as a correction), `PROBABLE` (file as a query), `SUSPECTED` |
| `severity` | no | How much it matters if nobody fixes it: `MISLEADING`, `IMPRECISE`, `COSMETIC`. See [Severity is not confidence](#severity-is-not-confidence). |
| `explanation` | yes | Self-contained text a curator at the resource can act on. |
| `supported_by` | no | Verbatim quotes, checked like any other `supporting_text`. |
| `report_status` / `report_url` | no | `NOT_REPORTED` (default), `REPORTED`, `ACKNOWLEDGED`, `FIXED`, `DECLINED`, plus a link once filed. |

## Example: "that gene, not this gene"

```yaml
source_defects:
- defect_type: WRONG_GENE_PRODUCT
  resource: GO_CAM
  record: gomodel:67e5e74400000148/67e5e74400000172
  slot: enabled_by
  requested_change: REPOINT
  asserted_value: AGI_LocusCode:AT2G45160      # SCL27, alias HAM1 (HAIRY MERISTEM 1)
  corrected_value: AGI_LocusCode:AT5G64610     # HAM1, MYST acetyltransferase
  corrected_label: HAM1, MYST histone acetyltransferase 1 (UniProtKB:Q9FLF7)
  cause: SYMBOL_COLLISION
  confidence: CONFIRMED
  explanation: >-
    The H4K5 acetyltransferase activity is enabled_by SCL27, a GRAS protein
    that shares the HAM1 alias; the cited papers study MYST HAM1 (AT5G64610).
```

## Example: an isoform missing from UniProt

The literature describes four SynGAP C-terminal isoforms, and only alpha1 carries
the PDZ ligand that binds PSD-95. None of the four isoforms in the reviewed
entry Q96PV0 has that C-terminus, although RefSeq and two unreviewed UniProtKB
entries do. The functional isoform maps to those sequences (`REFSEQ_PROTEIN`,
`UNIPROTKB_UNREVIEWED`), and its defect asks UniProt to add the isoform:

```yaml
functional_isoforms:
- id: SYNGAP1_ALPHA1
  maps_to:
  - type: REFSEQ_PROTEIN
    ids: [NP_001123538.1]
  source_defects:
  - defect_type: MISSING_ISOFORM
    resource: UNIPROT
    record: UniProtKB:Q96PV0
    requested_change: ADD
    asserted_value: UniProtKB:Q96PV0
    corrected_value: RefSeq:NP_001123538.1
    confidence: CONFIRMED
    explanation: >-
      None of the entry's four isoforms ends in the alpha1 C-terminus (-QTRV).
```

A functional isoform with no `UNIPROT_ISOFORM` mapping is one that the reviewed
entry does not contain. When a paper only *numbers* residues on a non-displayed
isoform, nothing in UniProt is wrong: record that with `residue_mappings` on
the finding instead (see `CLAUDE.md`, Isoform and Negation Tracking).

## Severity is not confidence

`confidence` is how sure the reviewer is that the record is wrong. `severity` is
how much it matters that it stays wrong. They are independent axes: a defect can
be `CONFIRMED` and `COSMETIC` (a duplicated row, verified by eye) or `SUSPECTED`
and `MISLEADING` (an annotation that may name the wrong gene, which would send
anyone reading it to the wrong protein). Do not use one for the other, and do
not reach for `severity` to express doubt.

`severity` is optional, and leaving it unset is the normal state: it means the
consequence has not been assessed, which is *not* the same as `IMPRECISE`. Set
it when you have a view the worklist's reasons cannot derive — which is the
point of the field, since every other input to the ranking is already in the
record.

| value | the consequence of leaving it |
|---|---|
| `MISLEADING` | The record makes a claim a reader or a pipeline will act on and that is false: the wrong entity, the opposite of the evidence, an analysis sent to unrelated biology. Fixing it changes conclusions. |
| `IMPRECISE` | The claim is defensible but less accurate than the evidence supports: an over-broad term, a qualifier overstating a subunit's role, an evidence code stronger than the experiment. Fixing it sharpens the record without changing what anyone would conclude. |
| `COSMETIC` | The substance is right and the defect is bookkeeping: a duplicated assertion, a mis-keyed reference whose intended paper is unambiguous, a stale label beside a correct identifier. |

In the worklist a set `severity` overrides the position the reasons derive:
`MISLEADING` sorts above every unassessed defect and `COSMETIC` below every one.
`IMPRECISE` shares the default band, so recording it states that the consequence
was assessed and is ordinary without moving the defect — which is worth saying,
because it stops the next reader assuming nobody looked.

## Generating reports

```bash
just export-source-defects
```

This writes three things, all generated and git-ignored: do not commit them.
Each aggregates every review in the repository, so a committed copy would
conflict between any two PRs that touch a defect. The `source_defects` blocks in
the reviews are the record. Generate the reports when you need them.

| output | contents |
|---|---|
| `reports/source-defects.tsv` | one row per recorded instance, with the grouping and ranking columns (`group_id`, `group_rank`, `group_size`, `group_reasons`, `group_severity`) so the data can be queried |
| `reports/source-defects/<RESOURCE>.md` | the defects for one resource that are not yet `FIXED` or `DECLINED` — the material that is sent upstream |
| `reports/source-defects/WORKLIST.md` | every open defect once, grouped and ordered worst first across all resources |

Filing a report is a manual step. When it is done, set `report_status:
REPORTED` and `report_url`, and set `FIXED` once a re-fetch shows the
correction.

## The worklist: grouping and ranking

### One item per fix, not per review

The same upstream defect is recorded independently by every review that trips
over it, so the instance count is a fact about our reviewing, not about the
resource. The worklist groups instances on the **fix** — who must change what,
in which field of which record, from what, to what:

```
resource  defect_type  record  slot  asserted_value  corrected_value  requested_change
```

Everything else on a row is either context that varies across the instances of
one fix (the gene, the GO term, the evidence code, the reference) or a judgement
about it (`confidence`, `cause`, `severity`, `explanation`), which is aggregated
across the group instead. An item is what gets filed: many rows of one
convention problem are one ticket.

Each field of the key earns its place against the corpus. Dropping `record`
merges two wrong references on one GO-CAM activity; dropping `slot` merges a
wrong term in an activity's `part_of` with one in its `has_input`; dropping
`corrected_value` merges two reviews proposing *different* replacements for the
same term, which hides a disagreement rather than recording it; dropping
`requested_change` merges "delete this row" with "repoint it". `asserted_value`
is kept beside `record`, not displaced by it, for the GO-CAM activity whose two
bad references are two defects.

**The key's limit is worth knowing.** A GOA-row defect has no `record` of its own
— the enclosing annotation identifies it, which is why the field is left unset —
so a group of such defects keyed on a generic `asserted_value` (a qualifier, an
evidence code) is a *class* of row-level asks rather than one upstream edit. Each
item therefore reports what it spans (how many gene products, how many annotated
terms) and how many distinct explanations its instances wrote, so a reader can
tell the two apart. Over-splitting is recoverable — a maintainer bundles two
items into one ticket, as one already did for two separate defects on LCMT1 —
whereas over-merging hides a disagreement, so the key errs towards splitting.

### Ranked by named reasons, not a score

There is no weighted score and no coefficients. Each item carries a small set of
reasons that are independently true or false of it, printed beside it with the
ground for each, and the order is lexicographic over those reasons:

1. a curator-set **`severity`**, as described above.
2. **`propagates`** — one fix corrects every record that inherits it, rather than
   one row. True when the resource's records are inherited (`INTERPRO` mappings,
   `PANTHER` node associations, and `GOC`, where the defect is in a term and the
   fix reaches every annotation using it), or when the defect's own `cause` says
   it spread. `GOC` is gated on the resource and not additionally on
   `defect_type: WRONG_TERM`, because by this field's own definition a `GOC`
   defect *is* an ontology defect, and in fact only one of the six committed
   `GOC` rows carries that type — the other five are bad definitions, placements
   and an EC class, all filed `OTHER` because the `defect_type` enum has no value
   for them. `GO_CENTRAL` is deliberately not in that resource set: it is
   PAINT's own IBD/IBA curation, not a pipeline (see [Choosing a
   resource](#choosing-a-resource)); a PAINT row that did over-propagate says so
   in its `cause` and is picked up that way. The cause limb requires every
   mechanism the instances *identified* to be a spreading one — `UNKNOWN` and an
   absent cause are silence, `OTHER` is a different mechanism that was
   identified, so it counts against. Without that, the corpus's largest group
   (55 UniProt qualifier rows, 5 of which say `SCOPE_OVER_REACH` and 27 of which
   name other mechanisms) would claim that one fix corrects all 55.
3. **`instances: N`**, descending — how many reviews recorded the same fix. More
   than one means systematic rather than a one-off.
4. **`misattributed`** — `WRONG_GENE_PRODUCT` or `MISSING_NEGATION`: the record
   asserts something false about a *different* entity, or the opposite of the
   evidence, rather than being imprecise about the right one.
5. **`confirmed`** — a tiebreaker only. Certainty decides *how* to file a defect
   (a correction rather than a query); it is not how much the defect matters,
   which is what `severity` is for, so it never outranks the reasons above it.
6. the grouping key, so the order is total and the file is stable between runs.

Reasons 2 and 3 are both breadth — how many records one fix corrects — and
breadth is what a worklist orders by, so they come before the kind of wrongness
and before certainty. An item with no reason at all is a single, unconfirmed,
non-propagating defect, and the worklist says so rather than leaving its position
unexplained.

Defects whose every instance has already been filed (`REPORTED`,
`ACKNOWLEDGED`) are listed in a trailing section instead of the queue: they need
chasing, not filing, and leaving them in the ranking would dilute it. `FIXED` and
`DECLINED` instances are dropped before grouping, as they are from the
per-resource reports, so a group's instance count is the work that remains.

## Choosing a resource

`resource` names who must fix the defect, which for a GOA row is normally the
`assigned_by` group. Three groups of values are easy to confuse:

- **Pipelines, not annotations.** A term that is wrong on an InterPro signature
  or a PANTHER node is wrong for every protein that inherits it, so the fix is
  upstream of any gene. Use `INTERPRO` for the InterPro2GO mappings behind
  `GO_REF:0000002` and for signature descriptions, and `PANTHER` for a family or
  ancestral-node GO association propagated by TreeGrafter (`GO_REF:0000118`).
- **`INTERPRO` is not `GOA_EBI`.** Ask what the fix changes. The *content* of a
  mapping - its GO term, its qualifier, the signatures it covers - or the
  signature's own description is `INTERPRO`, and stays `INTERPRO` however the
  row reached the gene: a defect that says "check the IPRnnnnnn mapping" is an
  InterPro defect even when the row carrying it is IEA from GOA, and it should
  name the mapping in `record:`. `GOA_EBI` is GOA's own curation: the row, not
  the mapping. `worm/dpm-1` is the clean case, and its structured fields say so
  more plainly than its prose - `defect_type: WRONG_GENE_PRODUCT`,
  `slot: DB_Object_ID`, `requested_change: REPOINT`, `UniProtKB:U4PF58` ->
  `UniProtKB:Q9TYJ7`. The mapping is not wrong; GOA applied it to a 51-residue
  fragment, and only GOA can repoint the row. (Its explanation also suggests a
  minimum-coverage requirement before InterPro2GO transfer, which is a change
  to the pipeline - also GOA's, and also not the mapping's content.) This split
  is easy to reopen. It was closed corpus-wide in #6027, and reopened twice
  while that PR waited to merge, in reviews that had carried no defects at all.
  As of `485113c854`: `ECOLI/pssA` and `PSEPK/pssA` each file two `GOA_EBI`
  defects asking that the IPR016270 PGS1 mapping be suppressed for the type-I
  PssA members - that is mapping scope, so `INTERPRO` - and none of the four
  names the mapping in `record:`. The same shape sits on IPR006327, filed
  `INTERPRO` with a `record:` in `XANCP/fruA` but `GOA_EBI` with none in
  `RHOCA/fruA` and `AZOBR/fruA1`, each of which also carries a correctly-filed
  `INTERPRO` defect on that very mapping. So check the filing whenever a
  defect's fix is a mapping, whatever the row's `assigned_by` says.
- **`PANTHER` is not `GO_CENTRAL`.** `GO_CENTRAL` is PAINT's own IBD/IBA
  curation. A term can sit on a PANTHER node without PAINT ever asserting it,
  and the two are fixed in different places; a gene can carry rows from both.
- **`GOC` is for the ontology, not an annotation.** When the defect is in a term
  itself - its label, definition, or placement in the graph - the annotations
  using it may all be reasonable. That is a `GOC` defect.

`OTHER` remains correct for a resource with no value, and the explanation must
then name it. It is *not* the right choice for a resource that does have a
value: a defect filed as `OTHER` when `CACAO` or `ECOLIWIKI` would have fit is
invisible to that resource's report, which is the whole point of the field.

## Choosing a cause

`cause` is optional and records the mechanism, not the defect. The first five
values are all gene-identity confusions - the wrong gene got the annotation.
The pipeline and process mechanisms are different in kind: the annotation is on
the intended gene and something else went wrong.

- `OVER_PROPAGATION` - the evidence is real somewhere but was spread past the
  clade, family or node where it holds. Fix the seed or the node, not the
  inherited rows.
- `SCOPE_OVER_REACH` - a mapping correct for some members was applied outside
  that scope, most often across a taxon boundary.
- `LABEL_WITHOUT_DEFINITION` - the term's label was read and its definition was
  not, including near-miss labels in unrelated parts of the graph.
- `SPECULATION_AS_ASSERTION` - a hedge in the source ("may function as") became
  an assertion.
- `PRACTICE_CHANGE` - a curation programme's convention changed, so a dated
  cohort shares a defect that is not a per-row judgement. Give the date range
  and row count; these are fixable in bulk.

Use `OTHER` when the mechanism is identifiable but unlisted, and `UNKNOWN` when
it is not identifiable at all. Prefer naming a mechanism where one fits: a
typed cause is what makes a pattern countable across resources.

This complements `reference_review` (see [Reference Curation](reference_curation.md)),
which judges the *reference* itself. When a correct paper is attached badly
(the wrong gene, a wrong WITH/FROM, a missing NOT), the reference is
`VERIFIED` and the defect belongs here.
