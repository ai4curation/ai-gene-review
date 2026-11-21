# KT2440 TF candidate census and review coverage

Generated from the pinned inputs in [build_manifest.json](build_manifest.json). See [methods and limitations](../README.md) and [source provenance](../sources/manifest.json).

**This is a provisional candidate census, not a count of experimentally verified TFs.** Broad discovery intentionally retains uncertain DNA-binding and signaling proteins. Triage exclusions apply to the main work queue and are not GO annotation removals.

- Reference metadata: **5527 proteins**.
- Candidate union: **647 proteins**.
- Existing review files cover **60 candidates**; **587 candidates** have no accession-matched review.
- **27 ambiguous aliases** are retained in [ambiguous_aliases.tsv](ambiguous_aliases.tsv).
- Unresolved external records: **1**; see [source_mappings.tsv](source_mappings.tsv).

## Provisional role queues

| Candidate class | Total | With review file | Without review file |
|---|---:|---:|---:|
| ambiguous_candidate | 141 | 18 | 123 |
| dbtf_candidate | 376 | 19 | 357 |
| nonregulatory_candidate | 18 | 6 | 12 |
| nucleoid_associated_candidate | 12 | 0 | 12 |
| other_signaling_candidate | 7 | 2 | 5 |
| post_transcriptional_regulator_candidate | 5 | 1 | 4 |
| sigma_factor_candidate | 25 | 6 | 19 |
| transcription_machinery_or_cofactor_candidate | 17 | 2 | 15 |
| transcriptional_response_regulator_candidate | 46 | 6 | 40 |

## Discovery signals and source reconciliation

Counts overlap and do not represent independent lines of evidence. PRECISE321_TRN is published prior knowledge, including reused RegPrecise records; PRECISE321_MODULE is a regulator assignment, not gene membership. Exact source combinations are in [summary.json](summary.json).

| Discovery source | Distinct candidate proteins |
|---|---:|
| InterPro | 580 |
| PRECISE321_MODULE | 35 |
| PRECISE321_TRN | 93 |
| Pfam | 434 |
| RegPrecise | 51 |
| existing_review_tf_row | 29 |
| go_sigma | 25 |
| go_tf | 300 |
| go_transcription_regulation | 434 |
| protein_name | 455 |
| uniprot_keyword | 370 |

| External source | Record mapping outcome | Count |
|---|---|---:|
| PRECISE321_MODULE | mapped | 39 |
| PRECISE321_MODULE | no_regulator_assignment | 45 |
| PRECISE321_TRN | mapped | 94 |
| RegPrecise | mapped | 47 |
| RegPrecise | mapped_multiple_loci | 2 |
| RegPrecise | not_protein_record | 6 |
| RegPrecise | unmapped | 1 |

Explicitly listed multiple source loci contribute candidates for each resolved protein; the record does not resolve their individual target specificity. RNA regulons and modules without assigned regulators are retained but do not create protein candidates.

### Unresolved external mappings

- [RegPrecise RutR2](https://regprecise.lbl.gov/regulon.jsp?regulon_id=34747): unmapped; source loci: not supplied.

## Existing review coverage

Inspected **998 review files**. Full-file mapping results are in [review_coverage.tsv](review_coverage.tsv). No gene validators were run for this inventory; `validation_status` is `not_run`. A declared COMPLETE status, zero PENDING rows, or a core-function section does not certify biological accuracy.

- Candidates with PENDING rows: 0.
- Candidates with UNDECIDED rows: 4.
- Candidates with at least one core-function section: 60.

### Reviews outside the accession/taxon join

- xylR (P06519): taxon_mismatch; in reference proteome: False; review taxon: 303.

## Prioritized calibration worklist

Scoped identity/evidence and importer assessments are tracked separately from full GO reviews; see [calibration assessment](../calibration-review.md). The rsmA negative control and out-of-proteome XylR control are excluded from the candidate denominator. Full rationale and paths are in [calibration.tsv](calibration.tsv). 4 cases have a recorded full GO re-review and validation in this workstream.

| Order | Accession | Display name | Locus | Candidate class |
|---:|---|---|---|---|
| 1 | Q88I42 | BenR | PP_3159 | dbtf_candidate |
| 2 | Q88DX2 | cbrB | PP_4696 | transcriptional_response_regulator_candidate |
| 3 | Q88FJ6 | gacA | PP_4099 | transcriptional_response_regulator_candidate |
| 4 | Q88ET0 | fleQ | PP_4373 | dbtf_candidate |
| 5 | Q88PZ2 | ada | PP_0706 | dbtf_candidate |
| 6 | Q88P32 | hexR | PP_1021 | dbtf_candidate |
| 7 | Q88HH7 | ptxS | PP_3380 | dbtf_candidate |
| 8 | P59479 | lexA2 | PP_3116 | dbtf_candidate |
| 9 | Q88JQ2 | PP_2597 | PP_2597 | dbtf_candidate |
| 10 | Q88DR9 | PP_4754 | PP_4754 | dbtf_candidate |
| 11 | Q88E08 | PP_4660 | PP_4660 | dbtf_candidate |
| 12 | Q88ME8 | rpoS | PP_1623 | sigma_factor_candidate |
| 13 | Q88F55 | pvdS | PP_4244 | sigma_factor_candidate |
| 14 | Q88DD3 | hfq | PP_4894 | post_transcriptional_regulator_candidate |
| 15 | Q88G93 | csrA | PP_3832 | post_transcriptional_regulator_candidate |
| 16 | Q88EW2 | cheY | PP_4340 | other_signaling_candidate |
| 17 | Q88EQ8 | flgM | PP_4395 | transcription_machinery_or_cofactor_candidate |
| 18 | Q88GF9 | MvaT | PP_3765 | nucleoid_associated_candidate |
| 19 | Q88QT6 | rsmA | PP_0401 | nonregulatory_candidate |
| 20 | P06519 | xylR |  | outside_reference_proteome |

The full [candidate worklist](candidates.tsv) is sorted by calibration selection, identity/role conflicts, unreviewed regulator candidates, existing-review refresh, then boundary audits. Reasons and source signals are retained per row.

## Coverage limits

- 64 observed domain identifiers could not be resolved in the downloaded current-release catalogs. IDs are listed in summary.json; no replacement IDs were guessed.
- The July 2026 local UniProt snapshot and the 2022 PRECISE321 source gene table are different snapshots. Locus joins resolve identifiers but do not certify sequence identity or functional transfer; no genome coordinates were transferred.
- No sequence classifier, new domain search, systematic literature search, or direct-target/ligand evidence audit was performed. Proteins outside this candidate union may still be undiscovered TFs. Missing database coverage is not negative evidence.
- CollecTF, PRODORIC, P2TF/P2CS and groovDB remain subsequent evidence sources; their coverage is not claimed by this census.
