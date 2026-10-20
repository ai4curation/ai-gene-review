# MEDTR/DMI1: reference-proteome assessment

Manually reviewed: 2026-10-18. Preferred Swiss-Prot accession: **Q6RHR6**.
Assessment: **EQUIVALENT**. Alternative: **G7IN96**.

## Manual interpretation

The reference sequence is exactly identical across all 882 residues and is separated from CASTOR-like paralogs. Primary-record genomic cross-references provide additional mapping context. This supports equivalent DMI1 protein representation; the broad pollux-like target label is not a separate functional assertion.

The primary accession and existing GO annotations are retained. This assessment
does not transfer annotations or establish that every residue difference is neutral.

## Search and sequence evidence

Searched 57,093 sequences across
UP000002051, returning **13** hits.
MMseqs2 is heuristic; the search is not an exhaustive proof of presence or absence.


| Accession | Global identity, including gaps | Query coverage | Target coverage | Global score |
| --- | --- | --- | --- | --- |
| G7IN96 | 882/882 (100.00%) | 100.00% | 100.00% | 4495.0 |
| A0A072VE48 | 694/882 (78.68%) | 79.93% | 100.00% | 3461.0 |
| D6C5X5 | 515/898 (57.35%) | 91.61% | 98.06% | 2465.5 |
| A0A072UFV9 | 447/883 (50.62%) | 67.91% | 99.83% | 2101.5 |
| A0A072U5M3 | 413/898 (45.99%) | 74.60% | 97.63% | 1864.5 |

The [comparison](comparison.yaml) retains every candidate score and metadata;
[candidates.fasta](candidates.fasta) retains all retrieved target sequences.
The top ten have residue-difference lists and detailed alignment files.
[search.tsv](search.tsv) retains the raw search results, including local alignment
coordinates. Long or partial target models must be interpreted using both query
and target coverage rather than a single identity percentage.

## History and database provenance

The [record snapshot](../../DMI1-record-evidence.yaml) contains current primary
and alternative records, reference-proteome metadata,
source URLs, retrieval timestamps and full UniSave versions:

- 09-DEC-2015, entry version 56. Proteomes: none.
- 07-OCT-2020, entry version 83. Proteomes: none.
- 27-NOV-2024, entry version 95. Proteomes: none.

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
