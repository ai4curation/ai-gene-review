# GOA rows with a missing GO shorthand

QuickGO can return an annotation with an ECO identifier but a null `goEvidence`.
The CACAO A5FI22 / GO:0042953 / PMID:40050408 row supplies ECO:0007744,
"combinatorial computational and experimental evidence used in manual assertion".
This is a statement about that source row, not a claim that every annotation
with this ECO identifier lacks a GO shorthand. The existing LAMBD/stf cache
contains the same ECO identifier with an explicit EXP value, which is retained.

On 2026-11-07, neither ECO's direct nor derived GAF mapping file, nor GO's
ECO usage constraints, contained ECO:0007744. Their exact snapshots are in
`analysis/goa_eco_only_import/review-followup/`. We therefore do not manufacture
an EXP, IMP or ISS source code from another gene's row. Revisit the fallback
when an authoritative mapping or corrected source row becomes available.

The fetcher preserves the ECO identifier in `ECO ID` and the missing shorthand
as an empty `GO EVIDENCE CODE` cell. Null display/sort fields, including date
and GO ID, serialize as empty cells without raising during sorting. The shared
`source_evidence_code` helper strips whitespace, prefers a supplied GO shorthand,
and otherwise preserves the supplied ECO identifier. The validator, seeder and
raw-TSV readers use this helper; no downloaded TSV is rewritten.

The schema explicitly accepts ECO:0007744. Its generated Python enum member is
`EvidenceType.ECOCOLON0007744`. Unknown ECO values still fail schema validation.
Strict matching and repeat seeding retain the literal source identifier, including
its qualifier and reference, rather than silently changing annotation payloads.

For reporting and evidence-support policy, the shared experimental category
includes ECO:0007744 because its definition explicitly includes experimental
evidence. Literature selection, target experimental coverage, orphan-curated
counts and tabular method classification therefore retain it. A broad EXP
compliance rule also applies to this experimental component; this is a coarse
policy category, not an ECO-to-GAF equivalence or an inference of IDA/IMP.
Exports still retain the literal evidence identifier alongside the method group.
The tabular export retains its established `EXP` method label for explicit EXP
rows. Other existing method labels are unchanged; ECO:0007744 receives the
`Experimental` method group without changing its evidence identifier.

Sources checked on 2026-11-07:

- [QuickGO annotation response for A5FI22](https://www.ebi.ac.uk/QuickGO/services/annotation/search?geneProductId=A5FI22&includeFields=goName&includeFields=taxonName&includeFields=name&limit=200)
- [OLS ECO:0007744 record](https://www.ebi.ac.uk/ols4/api/ontologies/eco/terms?obo_id=ECO:0007744)
- [ECO direct GAF mapping](http://purl.obolibrary.org/obo/eco/gaf-eco-mapping.txt)
- [ECO derived GAF mapping](http://purl.obolibrary.org/obo/eco/gaf-eco-mapping-derived.txt)
- [GO ECO usage constraints](https://github.com/geneontology/go-site/blob/master/metadata/eco-usage-constraints.yaml)

Tests cover null sorting, whitespace fallback and explicit-code precedence,
end-to-end seeding/schema/strict matching/idempotence, unknown-value rejection,
experimental literature/coverage/counts/export classification and compliance.
