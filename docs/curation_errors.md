# Recording curation errors

Sometimes an annotation is wrong because its cited paper was misread, not because
the paper is wrong or the gene lacks the function. `review.action` says what to do
with the row now (usually `REMOVE` or `MODIFY`), and `review.reason` explains why in
prose. `review.curation_error` adds a structured record of the mistake, so that:

- errors can be counted by type across reviews;
- each one can be reported to the database that made it (`responsible_source`);
- the text the annotation appears to rest on is quoted and checked.

## How it differs from neighbouring fields

| Field | Judges | Example |
|---|---|---|
| `reference_review.correctness` | the paper as a whole | `MISCITED`: the PMID is right but the paper never supports how it is cited |
| `finding_review` | one finding in the paper | a result later overturned |
| `propagation_review` | an inherited (IBA/ISS/IEA) annotation | a donor in the wrong paralog subfamily |
| `curation_error` | how this annotation used its paper | an introduction sentence curated as IMP |

A sound paper misread by a curator keeps `reference_review.correctness: VERIFIED`;
the error belongs to the annotation, so record it on the annotation.

## Error types (`CurationErrorTypeEnum`)

- `BACKGROUND_CLAIM_CURATED`: the annotation rests on a sentence restating earlier
  work, not on the paper's own experiments. It often sits in the abstract, so the
  manuscript section alone does not reveal it.
- `NO_SUPPORTING_CONTENT`: the paper says nothing that supports the term for this
  gene product, even as background.
- `WRONG_GENE_OR_HOMONYM`: the evidence concerns another gene, paralog, homeolog,
  splice product or name-sharing protein.
- `EVIDENCE_CODE_MISMATCH`: the paper supports the term, but not with the kind of
  experiment the evidence code asserts.
- `OVERINTERPRETED_RESULT`: a real experiment that does not establish the term,
  for example overexpression read as participation, or a negative result under
  redundancy read as a NOT.
- `OTHER`: explain in `review.reason`.

## Example

```yaml
- term:
    id: GO:0014029
    label: neural crest formation
  evidence_type: IMP
  original_reference_id: PMID:17724611
  negated: true
  review:
    action: REMOVE
    reason: ...
    curation_error:
      error_type: OVERINTERPRETED_RESULT
      responsible_source: UniProt
      misread_text:
      - reference_id: PMID:17724611
        supporting_text: Knockdown studies showed that Xhairy2a seems not to function in the neural crest
        reference_section_type: ABSTRACT
      evidence_reference_ids:
      - PMID:25997789
      report_status: NOT_REPORTED
```

`misread_text` quotes are validated like any other quote: they must be verbatim
substrings of the cached publication. Give each one its `reference_section_type`.
`evidence_reference_ids` names the paper(s) that actually hold the evidence, when
known, such as the earlier work a background sentence cites. Update
`report_status` (`REPORTED`, `FIXED_UPSTREAM`, `DECLINED_UPSTREAM`) and
`report_url` once the error has been sent upstream.

For annotations reviewed outside a gene review, as in the GO:0014029 obsoletion
remapping (`projects/NEURAL_CREST_FORMATION_OBSOLETION/remapping.tsv`), the same
enum fills a `source_error` column, next to a `reference_section_type` column for
the quoted text.
