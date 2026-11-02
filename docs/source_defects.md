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
| `defect_type` | yes | `WRONG_GENE_PRODUCT`, `WRONG_REFERENCE`, `WRONG_TERM`, `WRONG_EVIDENCE_CODE`, `MISSING_NEGATION`, `WRONG_WITH_FROM`, `WRONG_QUALIFIER`, `WRONG_CAUSAL_RELATION`, `MISSING_ISOFORM`, `OTHER` |
| `resource` | yes | Who must fix it. For a GOA row this is the `assigned_by` group (`TAIR`, `MGI`, ...), not GOA. A GO-CAM model is `GO_CAM`. |
| `record` | no | Id of the defective record when it is not the enclosing annotation. |
| `slot` | no | The field holding `asserted_value`, in the source's own terms: `enabled_by` or `has_input` for a GO-CAM activity; `DB_Object_ID`, `DB:Reference`, `With/From`, `Evidence_Code` or `Qualifier` for a GAF row. |
| `requested_change` | no | `REPOINT` (replace with `corrected_value`), `DELETE_VALUE` (drop the value, keep the record), `DELETE_ROW`, `ADD` (add `corrected_value`, which the record lacks), or `CHECK` (the right change depends on information we could not see; the explanation gives the alternatives). |
| `asserted_value` | yes | What the source says now, as a CURIE (`AGI_LocusCode:AT2G45160`, `PMID:32213638`). For `requested_change: ADD` nothing wrong is asserted, so this names the record that lacks the value (the same CURIE as `record`, e.g. `UniProtKB:Q96PV0` for a missing isoform); group `ADD` rows separately when analysing asserted values. |
| `corrected_value` / `corrected_label` | no | What it should say, when known. Leave unset when the value is wrong but the right one is unknown. |
| `cause` | no | `SYMBOL_COLLISION`, `LEGACY_ALIAS`, `IDENTIFIER_TRANSPOSITION`, `SEQUENCE_MISMAPPING`, `CONTAMINANT`, `OTHER`, `UNKNOWN` |
| `confidence` | yes | `CONFIRMED` (file as a correction), `PROBABLE` (file as a query), `SUSPECTED` |
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

## Generating reports

```bash
just export-source-defects
```

This writes `reports/source-defects.tsv`, with one row per defect, and
`reports/source-defects/<RESOURCE>.md`, with one report per resource listing
the defects that are not yet `FIXED` or `DECLINED`. These outputs are
generated and git-ignored: do not commit them. Each one aggregates every
review in the repository, so a committed copy would conflict between any two
PRs that touch a defect. The `source_defects` blocks in the reviews are the
record. Generate the reports when you need them. Filing a report is a
manual step. When it is done, set `report_status: REPORTED` and
`report_url`, and set `FIXED` once a re-fetch shows the correction.

This complements `reference_review` (see [Reference Curation](reference_curation.md)),
which judges the *reference* itself. When a correct paper is attached badly
(the wrong gene, a wrong WITH/FROM, a missing NOT), the reference is
`VERIFIED` and the defect belongs here.
