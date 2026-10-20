# TOXGO/SAG1: reference-proteome assessment

Manually reviewed: 2026-10-18. Preferred Swiss-Prot accession: **P13664**.
Assessment: **EQUIVALENT**. Alternative: **A0A7J6K396**.

## Manual interpretation

The reference SRS29B sequence is exactly identical across all 336 residues to reviewed SAG1. The full-proteome comparison separates it from other SAG-related proteins. This supports an equivalent protein representation while preserving the experimentally curated SAG1 accession.

The primary accession and existing GO annotations are retained. This assessment
does not transfer annotations or establish that every residue difference is neutral.

## Search and sequence evidence

Searched 8,261 sequences across
UP000557509, returning **37** hits.
MMseqs2 is heuristic; the search is not an exhaustive proof of presence or absence.


| Accession | Global identity, including gaps | Query coverage | Target coverage | Global score |
| --- | --- | --- | --- | --- |
| A0A7J6K396 | 336/336 (100.00%) | 100.00% | 100.00% | 1740.0 |
| A0A7J6K383 | 103/391 (26.34%) | 94.35% | 85.22% | 317.5 |
| A0A7J6JYP4 | 107/396 (27.02%) | 96.73% | 84.42% | 299.5 |
| A0A7J6K1T8 | 110/399 (27.57%) | 95.54% | 83.59% | 292.0 |
| A0A7J6K4H1 | 114/442 (25.79%) | 92.86% | 74.64% | 284.5 |

The [comparison](comparison.yaml) retains every candidate score and metadata;
[candidates.fasta](candidates.fasta) retains all retrieved target sequences.
The top ten have residue-difference lists and detailed alignment files.
[search.tsv](search.tsv) retains the raw search results, including local alignment
coordinates. Long or partial target models must be interpreted using both query
and target coverage rather than a single identity percentage.

## History and database provenance

The [record snapshot](../../SAG1-record-evidence.yaml) contains current primary
and alternative records, reference-proteome metadata,
source URLs, retrieval timestamps and full UniSave versions:

- 09-DEC-2015, entry version 84. Proteomes: none.
- 02-DEC-2020, entry version 97. Proteomes: none.
- 22-FEB-2023, entry version 102. Proteomes: none.

These samples do not establish continuous membership/absence, the precise date of
a change, or UniProt's reason. Older proteome IDs are distinguished from the
current reference-proteome selection.

## Methods and reproducibility

MMseqs2 18-8cc5c: sensitivity 7.5, E-value 1e-5, max-seqs 1000, four threads.
Biopython 1.85 global BLOSUM62 alignment: gap-open -10, extension -0.5, terminal
gaps penalized. Identity divides identical residues by all alignment columns;
coverage divides paired nongap residues by the full query or target length.
The full database checksum, source release, URL and command are in comparison.yaml.
Multiple reference-proteome FASTAs are deduplicated by accession, rejecting any
conflicting sequences rather than choosing one silently.

- [x] Shared scripts take explicit inputs and outputs and contain no gene-specific biological conclusions.
- [x] The workflow was run on multiple unrelated protein inputs across taxa.
- [x] Search and alignment completed; every returned target resolved to the input FASTA.
- [x] Direct observations and query/candidate sequences are retained.
- [x] Manual interpretation and limitations are separate from computed observations.

See [README.md](README.md) and [justfile](justfile). Methods:
[MMseqs2](https://github.com/soedinglab/MMseqs2/tree/18-8cc5c),
[Biopython](https://biopython.org/docs/1.85/Tutorial/chapter_pairwise.html),
[UniSave](https://www.uniprot.org/help/entry_history).
