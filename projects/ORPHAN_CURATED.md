---
title: "Orphan Curated: Swiss-Prot entries outside reference proteomes"
maturity: IN_PROGRESS
autolink_gene_symbols: false
tags: [PIPELINE]
species: [ARATH, BACAN, BREDI, CHLRE, DERPT, DICDI, ECOLI, FULFL, MEDTR, MOOTH, NICAT, OCTVU, ORYSJ, PENCH, POPTR, PSEPK, STAHA, STAWA, STECR, STRTR, THLAR, TOXGO, XANAU]
genes: [STRTR/cas10, OCTVU/DDO, STAWA/cfr, CHLRE/CP12, POPTR/PRX2, ORYSJ/PIKM1-TS, STECR/nas-8, ORYSJ/RGA4, ORYSJ/RGA5, THLAR/TFP, DERPT/Derp23, POPTR/CCOAOMT1, POPTR/CCOAOMT2, STAHA/lnuA, PSEPK/xylR, DERPT/Derp1, ECOLI/traD, BREDI/opd, ARATH/FRI, TOXGO/SAG1, PENCH/aatA, POPTR/WIN6, ECOLI/traC, FULFL/AVR9, XANAU/dhlA, POPTR/MAOX, ECOLI/traB, POPTR/PAL, THLAR/CYP71B1, DERPT/Derp2, FULFL/AVR4, BACAN/ermJ, MOOTH/acsD, DICDI/chlA, MEDTR/DMI1, MEDTR/NORK, NICAT/NaPMT1.1, ARATH/AOP2, THLAR/matK]
---

# Orphan Curated

Identify Swiss-Prot accessions in our gene-review set that are outside every
reference proteome for their exact NCBI taxon. These are candidates for feedback
to UniProt and for checking our choice of accession. Preserve visibility of the
GO annotations attached to these curated entries, particularly experimental and
other non-IEA annotations that reference-proteome-only workflows could overlook.

The starting example is six reviewed *Populus trichocarpa* accessions absent from
[UP000006729](https://www.uniprot.org/proteomes/UP000006729): A9PCL4 (local PRX2),
P16579 (WIN6), O65862 (CCOAOMT1), O65922 (CCOAOMT2), P45730 (PAL), and P34105
(local MAOX). All six also lack any Proteomes cross-reference in UniProt release
2026_03. The local gene labels PRX2 and MAOX do not imply that UniProt supplies
those gene names.

## Reports and commands

- [Repository-wide issue-ready Markdown](ORPHAN_CURATED/reports/orphan-curated.md)
- [Repository-wide CSV](ORPHAN_CURATED/reports/orphan-curated.csv)
- [Generated counterpart assessments](ORPHAN_CURATED/COUNTERPARTS.md)
- [Generated counterpart assessment CSV](ORPHAN_CURATED/counterpart-assessments.csv)
- [POPTR issue-ready Markdown](ORPHAN_CURATED/reports/POPTR/orphan-curated.md)
- [POPTR CSV](ORPHAN_CURATED/reports/POPTR/orphan-curated.csv)

```bash
just project-counterparts                 # render frontmatter genes from curated YAML
just project-counterparts --check         # fail if the generated reports are stale
just orphan-curated                       # audit membership; both CSV and Markdown
just orphan-curated --format csv
just orphan-curated --format markdown
just orphan-curated --refresh              # refresh live UniProt API data
just orphan-curated --offline              # reuse previously fetched API data
just orphan-curated --species POPTR --output-dir projects/ORPHAN_CURATED/reports/POPTR
```

The counterpart Markdown and CSV are generated from this page’s `genes` frontmatter
and each gene review’s `alternative_records` or `reference_proteome_assessments`.
Edit those YAML blocks and regenerate; the report contains the current counts,
rationales, dates, and evidence links. Species-qualified frontmatter entries keep
the cohort unambiguous. Missing reviews fail the build; genes without assessments
are shown explicitly. The renderer does not make new curation decisions.

For the membership audit, the default destination is `projects/ORPHAN_CURATED/reports/`. A species-filtered
run uses that same destination unless `--output-dir` is supplied, so use a separate
directory to retain both the full report and a species subset. The command writes
`orphan-curated.csv` and/or `orphan-curated.md`. The Markdown contains absolute
links to UniProt entries, proteomes, taxonomy, QuickGO annotations, and the review
and GOA source files; it can be pasted directly into a GitHub issue.

## Selection and evidence accounting

The input set is all primary `genes/*/*/*-ai-review.yaml` files, including drafts
and pending reviews. Multiple review files for one accession count as one entry.
RNAcentral identifiers are counted separately and excluded. A local UniProt entry
name is resolved to an accession only when it matches the cached flat file's ID
line, using that file's primary AC; the original identifier is retained and the
resolution is reported. Unresolved or merged accessions require follow-up.
The report verifies current Swiss-Prot status, taxonomy and Proteomes membership
through the UniProt API. The exact live taxon must have a proteome classified as
reference, and the accession must belong to none of that taxon's reference
proteomes. Membership in an ordinary non-reference proteome does not exclude a
candidate. The `Reference proteome` keyword in an old local flat file is not used
as the final membership test.

The summary separately counts unreviewed entries, unresolved accessions, and
Swiss-Prot entries for taxa without an exact-taxon reference proteome. The latter
are excluded from the candidate table: a species or strain that is not a reference
taxon is expected to lack this membership. A reference proteome on the parent
species or a different strain does not qualify the entry. Failed API requests or
incomplete pagination stop the run rather than turning missing data into absence.

GO statistics come from the original cached `*-goa.tsv` files, not from proposed
NEW annotations or review actions. The report counts annotation rows by evidence
code, non-IEA rows, experimental rows, and NOT rows. Non-IEA includes phylogenetic
and computational inference and is not synonymous with experimental evidence.
Exact duplicate rows across duplicate review caches are counted once per accession;
different evidence for the same term remains distinct. Isoform GOA rows belonging
to the accession are included. Missing GOA is unknown, not zero. The CSV includes
per-entry distinct term counts, cache status, source paths, SHA-256 hashes, and
annotation-date ranges.

API responses are cached under `.cache/orphan-curated/` for seven days. Retrieval
dates and UniProt releases are shown in both formats. `--refresh` replaces query
caches; `--offline` requires the relevant queries to have been fetched previously
and permits older caches. Mixed UniProt releases require a refresh. GOA caches
are never modified by this report: these statistics are a mixed-time snapshot,
not a fresh QuickGO census.

## Why might this happen?

Swiss-Prot curation and membership in a genome-derived proteome are distinct.
[UniProt's proteome documentation](https://www.uniprot.org/help/proteome) describes
genome-based proteomes and additional manual review for experimentally supported
proteins that cannot be mapped to the current assembly. For these six POPTR
entries, UniProt's reason for exclusion has not been established. The
[generated counterpart report](ORPHAN_CURATED/COUNTERPARTS.md) records our
sequence/locus assessments and their limitations.

An absent accession is not proof that its biological gene, sequence, or annotations
are absent, and it is not evidence that Swiss-Prot will delete the entry. This
project measures candidate coverage gaps, not unique annotation loss. A TrEMBL
counterpart would warrant comparing sequences, locus identifiers, and GO evidence;
it would not by itself justify switching our reviewed accession.

Related: [Proteome Removal](PROTEOME_REMOVAL.md) concerns removal of unreviewed
entries, a separate problem.

---

# STATUS

- [x] Implement a reusable `just orphan-curated` target with CSV and Markdown output.
- [x] Verify the six POPTR candidates against live UniProt.
- [x] Count original cached GOA evidence with explicit unknown-data handling.
- [x] Run the repository-wide audit and retain both reports with source provenance.
- [x] Investigate reference-proteome locus/sequence counterparts for the six POPTR entries.
- [x] Curate the two CCOAOMT counterparts while retaining their Swiss-Prot IDs.
- [x] Populate PRX2, PAL, and MAOX equivalents and the unresolved WIN6 candidate.
- [x] Assess all 33 remaining accessions across the other 22 taxa, retaining primary IDs.
- [x] Distinguish equivalents, locus counterparts, candidates, and searches with no supported counterpart.
- [ ] Map WIN6 source genomic record U01661 and flanks to distinguish locus/model/parental alternatives.
- [ ] Compare GO coverage on any verified counterpart; distinguish shared and unique assertions.
- [ ] Submit the reviewed candidate report to UniProt and record their explanations.
- [ ] Consider surfacing reference-proteome status routinely during gene review.

# NOTES

## Illustrative cases

The full inventory, counts, and evidence are in the
[generated counterpart report](ORPHAN_CURATED/COUNTERPARTS.md). These examples
illustrate why a single similarity threshold cannot decide how to treat an orphan
curated entry:

- **[CCOAOMT1](../genes/POPTR/CCOAOMT1/CCOAOMT1-ai-review.yaml): equivalent records.**
  Identical protein sequences and a shared transcript support the counterpart
  assignment despite different source cultivars. Keeping the Swiss-Prot ID
  preserves the connection to the curated record.
- **[FRI](../genes/ARATH/FRI/FRI-ai-review.yaml): same locus, different allele activity.**
  The reference cultivar has an inactive allele. A locus counterpart must not be
  treated as a functionally equivalent protein or an automatic GO transfer target.
- **[NaPMT1.1](../genes/NICAT/NaPMT1.1/NaPMT1.1-ai-review.yaml): near identity is insufficient.**
  A PMT1/PMT3 naming and locus discrepancy remains unresolved despite a very close
  sequence match, so the alternative remains a candidate.
- **[CP12](../genes/CHLRE/CP12/CP12-ai-review.yaml): observed membership change.**
  Sampled UniSave versions show a reference-proteome link followed by its absence.
  This establishes a historical change, but does not explain UniProt's decision.
- **[chlA](../genes/DICDI/chlA/chlA-ai-review.yaml): no supported counterpart.**
  A search without a supported match is worth following up, particularly alongside
  historical proteome membership. It does not prove genomic absence.

## Reproducing the underlying analysis

The gene YAML holds the current curated decisions. Full source snapshots,
FASTA files, search results, alignments, and reproduction workflows live in
[uniprot-orphan-analysis](https://github.com/ai4curation/uniprot-orphan-analysis).
Its historical batch-import manifest is provenance, not a second source for
current report content.

Each gene retains one compact `GENE-record-evidence.yaml` extract here. It contains
the cited original source lines with context, relevant observations, source
release and retrieval metadata, SHA-256 digests, and links pinned to an immutable
analysis commit. Existing quote validation runs offline against these extracts.
Full records and sequences remain available through the pinned archive links.
See [alternative-record documentation](../docs/alternative_records.md) for the
schema and evidence requirements.

Run the batch sequence analysis **in the analysis repository**:

```bash
just analyze --fetch --exclude-species POPTR
```

It generates observations only and retains existing comparisons unless `--rerun`
is supplied. `--accession ACCESSION` limits the run. After committing an analysis,
use that repository's `just export-evidence /path/to/ai-gene-review COMMIT` and
`just check-evidence /path/to/ai-gene-review COMMIT` to update and verify the
compact extracts. The exporter fails if a cited quotation is absent from the
archived source; it does not copy review claims into evidence.

Manual reassessment is required after refreshing any source. Regenerate the
linked reports here with `just project-counterparts` after updating the gene
YAML. Comparing counterpart GO coverage remains a separate follow-up.
