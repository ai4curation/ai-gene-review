# Manually curated alternative records

Keep the preferred Swiss-Prot accession in a review's top-level `id`. Use
`alternative_records` to document a manually assessed relationship to another
UniProt accession. It is a list because one preferred record may have more than
one relevant counterpart. This is distinct from `functional_isoforms`, which
describes products and activities rather than database records.

The relationship `REFERENCE_PROTEOME_EQUIVALENT` means the curator
considers the alternative an equivalent representation in the named reference
proteome. A matching protein name or family is insufficient. Evaluate sequence,
locus, taxonomy, and cultivar/strain differences; identical proteins can occur
at distinct loci. A curator can record qualifications in `reason` and in each
evidence item's `description`.

Use `REFERENCE_PROTEOME_CANDIDATE` when a plausible counterpart has supporting
sequence/locus and membership evidence but equivalence remains unresolved. Explain
the competing interpretations and what would resolve them in `reason`. WIN6 is
a worked example: the best matching reference sequence is documented without
asserting that it is the same locus. Neither relationship automatically transfers
GO annotations. Equivalence need not mean literal sequence identity: document all
differences and the basis for distinguishing a counterpart from a paralog.

Use `REFERENCE_PROTEOME_LOCUS_COUNTERPART` for a supported same-locus or
reference-cultivar counterpart with different function or protein integrity.
FRI and AOP2 are explicit active-versus-inactive allele examples; the rice
RGA4 pair documents cultivar-dependent resistance-system differences. RGA5
remains a candidate: target-only locus identifiers do not independently establish
cross-cultivar mapping.
This relationship must not be interpreted as functional equivalence.

If a completed search identifies no sufficiently supported counterpart, use
`reference_proteome_assessments` instead of inventing an alternative accession:

```yaml
reference_proteome_assessments:
- reference_proteomes: [UP000000625]
  status: NO_SUPPORTED_COUNTERPART
  reviewed_on: '2026-10-18'
  reason: No supported counterpart was identified in the documented search.
  evidence: # Required cited PROTEOME_SEARCH and PROTEOME_MEMBERSHIP items
    # See the complete ECOLI/traD worked example.
```

The abbreviated example above omits the required evidence entries; see
[traD](../genes/ECOLI/traD/traD-ai-review.yaml) for a complete validated record.
A negative search is not proof of biological absence. Record the search settings,
competing hits, limits, and relevant plasmid/strain context. For taxa with multiple
reference proteomes, document all searched IDs. The report-wide
[generated assessment report](../projects/ORPHAN_CURATED/COUNTERPARTS.md)
reads the project frontmatter gene list and these curated YAML blocks. Regenerate
its Markdown and CSV with `just project-counterparts`; use
`just project-counterparts --check` to detect stale outputs. The project page
keeps a few illustrative cases rather than a manually maintained inventory.

For complete worked examples, see
[CCOAOMT1](../genes/POPTR/CCOAOMT1/CCOAOMT1-ai-review.yaml) and
[CCOAOMT2](../genes/POPTR/CCOAOMT2/CCOAOMT2-ai-review.yaml). Their primary IDs
remain O65862 and O65922; the alternatives are A0A2K1Z5Q2 and A0A2K2C664.

Each alternative requires:

| Field | Content |
| --- | --- |
| `id` | Alternative primary UniProt accession, without a prefix |
| `relationship` | `REFERENCE_PROTEOME_EQUIVALENT`, `REFERENCE_PROTEOME_LOCUS_COUNTERPART`, or `REFERENCE_PROTEOME_CANDIDATE` |
| `reference_proteome` | The alternative's reference proteome, e.g. `UP000006729` |
| `reviewed_on` | Date of the manual assessment |
| `reason` | Curator's rationale and qualifications |
| `evidence` | Typed claims with `description` and `supported_by` citations |

Evidence types distinguish the parts of the argument:

| Type | What it establishes |
| --- | --- |
| `PROTEOME_SEARCH` | Search scope, returned hits and limitations, including a negative search |
| `SEQUENCE_COMPARISON` | Sequence relationship; report identity and coverage, including differences |
| `LOCUS_MAPPING` | Shared genomic locus or transcript identifiers |
| `PROTEOME_MEMBERSHIP` | Current membership of the alternative in a reference proteome |
| `RECORD_HISTORY` | Dated observations from archived records |
| `CURATION_CONTEXT` | Qualitative context, such as cultivar, assembly, or curator correspondence |

For all alternative-record relationships, `just validate SPECIES GENE` requires membership evidence and at least one of
sequence comparison or locus mapping. History and context alone cannot establish
equivalence. It also rejects self-links, duplicate alternatives, absent citations,
and citations not declared in `references`. Standard quote validation checks
`supporting_text` against the cited source. These checks validate the documented
argument; they do not independently adjudicate its biology.
No-counterpart assessments require cited `PROTEOME_SEARCH` and
`PROTEOME_MEMBERSHIP` evidence and the searched proteome IDs.

No GO annotation is transferred automatically, and neither the review's identity
nor its annotations are reassigned. The orphan-curated report still includes an
eligible primary accession even when a counterpart is documented: its absence
from the proteome remains a useful question for UniProt.

## Evidence snapshots and UniSave

Use current **UniProtKB** records and proteome metadata for membership and locus
cross-references. **UniParc** identifies protein sequences: a shared UniParc ID
supports sequence identity, but does not establish a unique gene or current
proteome membership. **UniSave** is the archive of previous UniProt entry
versions. It can show that a proteome association was present or absent at a
particular release; it is not a log of curators' reasons. Checking three old
versions does not prove uninterrupted absence between those versions.

The [uniprot-orphan-analysis repository](https://github.com/ai4curation/uniprot-orphan-analysis)
captures full API source records, URLs, retrieval timestamps, release headers,
selected UniSave versions, and computed sequence/membership observations.
It also owns the FASTAs, search tables, alignments, and reproduction workflows.
Run the following commands **in that repository**; they do not create a manual
equivalence judgment:

```bash
uv run python projects/ORPHAN_CURATED/fetch_record_evidence.py O65862 A0A2K1Z5Q2 \
  --proteome UP000006729 --history-versions 94 122 132 \
  --output genes/POPTR/CCOAOMT1/CCOAOMT1-record-evidence.yaml

uv run python projects/ORPHAN_CURATED/fetch_record_evidence.py O65922 A0A2K2C664 \
  --proteome UP000006729 --history-versions 90 119 130 \
  --output genes/POPTR/CCOAOMT2/CCOAOMT2-record-evidence.yaml
```

Add `--ena ACCESSION` to include the source nucleotide record and its organism,
cultivar, or strain metadata. That repository's per-gene `RESULTS.md` files
preserve historical interpretations; `comparison.yaml` and alignment files
contain computed observations, and `justfile` recipes reproduce the work.

AI Gene Review retains one compact `GENE-record-evidence.yaml` per gene.
Declare this extract in `references` with a `file:` identifier and cite it from
each evidence item. The extract retains original source line ranges with context,
source release and retrieval metadata, and relevant structured observations.
Each archived source has a SHA-256 digest and a URL pinned to its Git commit.
Full candidate tables and protein sequences stay in the analysis repository.

After committing an analysis, run these commands from its checkout:

```bash
just export-evidence /path/to/ai-gene-review COMMIT
just check-evidence /path/to/ai-gene-review COMMIT
```

The exporter reads the specified Git revision and selects original source lines;
it fails if a review's quotation is absent. `check-evidence` verifies that the
local extracts are reproducible from that revision. Normal review validation
checks the local quotations offline without downloading the archive.

Keep source observations separate from interpretation. When refreshing evidence,
reassess the relationship, date, rationale, and quotations in the same change.
Add the usual curation history record.

The gene HTML renderer displays these relationships and links to their evidence
extracts while continuing to present the preferred accession in the header.

Embedded UniSave `record_text` fields in `*-record-evidence.yaml` are checked
for label-only or unvetted-prediction quotations, just like `*-uniprot.txt` sources.
Compact extracts preserve complete matching fields, including their evidence
tags, for these checks. JSON metadata and computed observations are not
interpreted as flat-file statements.
