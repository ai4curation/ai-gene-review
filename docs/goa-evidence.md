# GOA evidence without a GO shorthand

QuickGO can return an annotation with an ECO identifier but a null
`goEvidence`. For example, its CACAO annotation of A5FI22 to GO:0042953,
citing PMID:40050408, supplies ECO:0007744. ECO defines this as combinatorial
computational and experimental evidence used in manual assertion. It is not
an instruction to substitute IMP, ISS, EXP, or ND.

The fetcher preserves the ECO identifier in the TSV's `ECO ID` column and
leaves `GO EVIDENCE CODE` empty. Missing optional display fields are also
serialized as empty cells. When reading a TSV, the validator and seeder use
the supplied GO shorthand if present, otherwise the supplied ECO identifier.
This same value participates in strict annotation matching and repeat seeding.
The TSV itself is not rewritten.

The review schema explicitly accepts `ECO:0007744` as an `evidence_type`.
Other unsupported evidence values still fail schema validation; neither the
parser nor the schema guesses a biological evidence category. Adding another
ECO-only value requires verifying its ontology definition and extending the
schema deliberately.

Sources checked on 2026-11-07:

- [QuickGO annotation response for A5FI22](https://www.ebi.ac.uk/QuickGO/services/annotation/search?geneProductId=A5FI22&includeFields=goName&includeFields=taxonName&includeFields=name&limit=200)
- [OLS ECO:0007744 record](https://www.ebi.ac.uk/ols4/api/ontologies/eco/terms?obo_id=ECO:0007744)

The regression tests cover raw null preservation, preference for an existing
GO shorthand, schema acceptance, strict comparison, repeat seeding, and
rejection of unknown evidence values.
