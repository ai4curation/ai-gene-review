# KT2440 TF candidate census

Start with the generated [coverage report](data/coverage.md), the
[prioritized candidate inventory](data/candidates.tsv), and the
[20-case calibration worklist](data/calibration.tsv). The
[scoped assessments](calibration-review.md) and [importer checks](imodulon/calibration-results.md)
are complete; [four full GO re-reviews](../batches/tf_carbon_utilization_01.md)
and [structured regulatory evidence](regulatory-evidence.md) now follow that initial pass. The
[bacterial regulon evidence workstream](../../TRANSCRIPTION_FACTORS/bacterial-regulon-evidence.md)
sets the biological scope and subsequent curation tasks.

This is a reproducible **discovery and triage inventory**. Its role classes and
main-TF queue are provisional; they do not certify TF activity, target genes,
regulatory sign or ligand specificity. No gene reviews are modified by either
script. No sequence classifier or fresh domain search is run.

## Rebuild

From the repository root, using dependencies in the existing `uv.lock`:

```bash
# Offline rebuild from the committed normalized source snapshots and local reviews.
uv run python projects/P_PUTIDA/build_tf_census.py

# Regression tests for identity and biological scope boundaries.
uv run pytest -q tests/test_putida_tf_census.py tests/test_imodulondb.py

# Re-extract sources from cached downloads; missing downloads are fetched.
uv run python projects/P_PUTIDA/fetch_tf_census_sources.py
```

The local justfile wraps these as `build`, `fetch`, and `check`, for example
`just --justfile projects/P_PUTIDA/tf_census/justfile build` from the repository root.

Both scripts accept explicit input/output paths (`--help`). To refresh external
sources, use a **new cache directory**, review the resulting source changes, then
rebuild; source retrieval does not silently overwrite a cached snapshot. The
PRECISE321 source commit is pinned by default and can be explicitly changed with
`--commit`. Raw downloads, including the approximately 40 MB supplement, stay in
`.cache/putida_tf_census/`; small normalized extracts are committed in `sources/`.

The source manifest records original URLs, download-file timestamps, checksums,
the pinned GitHub commit, selected-field extraction and reuse notes. The build
manifest hashes the metadata, configuration, normalized sources, every inspected
review file, the build script and generated outputs. An altered metadata snapshot
or normalized source fails the build until provenance is reconciled.

## Inputs and identity joins

- **UniProt:** existing July 2026 metadata snapshot for UP000000556,
  NCBITaxon:160488. The unchanged metadata and original retrieval manifest live
  in `../data/`.
- **InterPro/Pfam:** official current-release entry-name catalogs, reduced to
  identifiers present in that metadata. Labels are used for discovery; no new
  sequence-domain assignments are inferred. Missing/retired catalog identifiers
  remain listed in `data/summary.json`.
- **QuickGO:** snapshotted `is_a` closure of GO:0003700 and GO:0016987, plus
  `is_a,part_of` closure of GO:0006355. The sigma branch is tracked separately
  even though it also falls under the current TF branch.
- **RegPrecise:** KT2440 genome 267, including per-regulon TF locus properties.
  RNA regulons are retained as non-protein source records. Explicit multiple-locus
  records create multiple candidates without choosing a target-specific paralog.
- **PRECISE321:** published supplement from
  [modulome_ppu](https://github.com/SBRG/modulome_ppu), commit
  `f63a0dfab124ea9022123ce6227d132f39de0108`. Extracts preserve all 84 module
  assignments (including unassigned modules), unique prior-network regulator
  name/locus pairs, and relevant source gene-table records. The source genome
  accession is retained where supplied. No weights, membership or target edges
  are imported by the census builder. The separate [membership export](imodulon/README.md)
  contains source-defined memberships and weights. Source publication: [Lim et al. 2022](https://doi.org/10.1016/j.ymben.2022.04.004).
- **Existing reviews:** accession and taxon determine the join, not directory or
  symbol. A correctly matched review can contribute an alias, while its original
  spelling and any difference from metadata remain visible.

Resolution uses accession first, then normalized locus (`PP0119` → `PP_0119`),
then a unique case-insensitive alias only when stronger identifiers are absent.
An unknown explicit accession or locus never falls back to a symbol. Ambiguous
aliases remain sets. Module regulator names are resolved through the source TRN
locus table first, then its gene table, then the local unique-alias index.

These are identifier joins across source versions, not sequence-identity checks.
Coordinates and regulatory edges are deliberately not transferred. A regulator
name on a module and a gene belonging to that module are different relationships.
PRECISE321's prior network reuses RegPrecise and literature; these are not
independent confirmations.

## Candidate discovery and classification

[rules.yaml](rules.yaml) contains the inspectable name/domain patterns and specific
signature checks. Discovery takes the union of protein descriptions, transcription
keywords, the GO branches, TF/HTH/DNA-binding/receiver and related domain labels,
external regulator identities, and TF rows in existing reviews. Even a removed
review TF row can trigger inspection; its presence does not endorse that claim.

Broad DNA-binding folds and receiver domains intentionally create uncertain
candidates. Specific labels and architectures assign provisional TF queues;
sigma factors, RNA regulators, nucleoid proteins and transcription cofactors
have separate queues. Named repair/replication or non-transcriptional signaling
proteins can be excluded from the main queue when no conflicting TF signal is
present. Multifunctionality and conflicting signals remain review questions.

Calibration selection never creates an evidence-discovered candidate. The rsmA
methyltransferase and out-of-proteome XylR are controls and have explicit census
membership flags in the calibration table.

Priorities are deterministic, with no confidence score implied:

1. `P0_calibration`: selected calibration cases that occur in the candidate set.
2. `P1_identity_conflict`: unresolved role or source/review naming conflicts.
3. `P2_unreviewed`: provisional main or related regulators without a review.
4. `P3_review_refresh`: remaining candidates with existing reviews.
5. `P4_boundary_audit`: other candidates needing a scope check.

Each candidate keeps its actual signals, role reason, flags, official domain
labels and source family names. Review status, annotation-row counts, PENDING,
UNDECIDED and core-function presence are independent fields. Validators were not
run on all existing reviews; no inferred completeness or validation pass is
assigned. UniProt function PMIDs are literature leads, not newly assessed evidence.

## Initial observations and next work

- Accession joins connect `gacA` to metadata `uvrY` and `cbrB` to an AlgB-named
  record. The scoped assessment supports GacA/CbrB identities with locus-specific
  primary evidence; the original metadata is preserved.
- The two `fur` aliases and three `csrA` aliases demonstrate why symbols cannot
  uniquely identify proteins. RegPrecise/PRECISE321 locus assignments preserve
  the source's Zur-versus-Fur naming without adjudicating metal specificity.
- RegPrecise's RutR2 record has no supplied TF locus and no unique local alias;
  it remains unresolved. MetR and GguR explicitly list multiple loci, which are
  preserved rather than treated as malformed single identifiers.
- The PSEPK-folder XylR review has an accession outside this metadata set and a
  different taxon. It is retained in the review audit and calibration controls,
  outside the KT2440 candidate denominator.

Next: complete full GO reviews using the scoped assessments and checked importer
outputs, and curate structured experimental relationships. CollecTF, PRODORIC, P2TF/P2CS and groovDB
remain additional sources for later evidence acquisition. This inventory does
not establish complete biological coverage of KT2440 TFs.
