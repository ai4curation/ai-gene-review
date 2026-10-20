# PRX2 counterpart analysis

Run the recipes from this directory. Requires the repository's `uv.lock`
(Biopython 1.85) and external MMseqs2 **18-8cc5c** (`mmseqs version`). No new
Python dependencies are needed.

- `just fetch-target` downloads the live reference-proteome FASTA and fresh metadata into the ignored repository cache.
- `just analyze` searches that FASTA and regenerates the saved comparisons.
- `just snapshot` refreshes current UniProt/proteome records, three explicit UniSave versions, and the original ENA record.

The committed query FASTA comes from the preferred UniProt accession in the
record snapshot. Reassess its sequence if refreshing the snapshot. The full
77,340-sequence database is cached rather than committed; its SHA256 and source
release are recorded in comparison.yaml. A future live download can differ from
release 2026_03. Retained candidate sequences permit inspection of the original
alignments even if the live database changes. Do not treat a refreshed report as
a refreshed manual judgment: update the review date and rationale only after
reassessment.

[RESULTS.md](RESULTS.md) contains the manual interpretation. Shared implementation:
`src/ai_gene_review/analysis/record_counterparts.py`.
