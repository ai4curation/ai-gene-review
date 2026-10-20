# STECR/nas-8: reference-proteome assessment

Manually reviewed: 2026-10-18. Preferred Swiss-Prot accession: **D2KBH9**.
Assessment: **EQUIVALENT**. Alternative: **A0A4U8UYW6**.

## Manual interpretation

The 418-residue reference protein differs by one residue across full ungapped coverage (99.76% identity), with a large separation from other metallopeptidase hits. This supports a qualified sequence-based counterpart assessment. The source protein is from strain Breton; the origin and biological effect of the single residue difference are not established.

The primary accession and existing GO annotations are retained. This assessment
does not transfer annotations or establish that every residue difference is neutral.

## Search and sequence evidence

Searched 35,146 sequences across
UP000298663, returning **44** hits.
MMseqs2 is heuristic; the search is not an exhaustive proof of presence or absence.


| Accession | Global identity, including gaps | Query coverage | Target coverage | Global score |
| --- | --- | --- | --- | --- |
| A0A4U8UYW6 | 417/418 (99.76%) | 100.00% | 100.00% | 2249.0 |
| A0A4U5N1Z8 | 177/446 (39.69%) | 80.86% | 92.35% | 827.5 |
| A0A4U5N298 | 178/446 (39.91%) | 80.38% | 92.31% | 819.0 |
| A0A4U5M467 | 164/494 (33.20%) | 91.63% | 83.44% | 604.0 |
| A0A4U8UWC9 | 160/553 (28.93%) | 90.67% | 73.74% | 566.0 |

The [comparison](comparison.yaml) retains every candidate score and metadata;
[candidates.fasta](candidates.fasta) retains all retrieved target sequences.
The top ten have residue-difference lists and detailed alignment files.
[search.tsv](search.tsv) retains the raw search results, including local alignment
coordinates. Long or partial target models must be interpreted using both query
and target coverage rather than a single identity percentage.

## History and database provenance

The [record snapshot](../../nas-8-record-evidence.yaml) contains current primary
and alternative records, reference-proteome metadata,
source URLs, retrieval timestamps and full UniSave versions:

- 09-DEC-2015, entry version 30. Proteomes: none.
- 02-DEC-2020, entry version 51. Proteomes: none.
- 27-NOV-2024, entry version 56. Proteomes: none.

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
