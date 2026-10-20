# THLAR/matK: reference-proteome assessment

Manually reviewed: 2026-10-18. Preferred Swiss-Prot accession: **Q9GF35**.
Assessment: **EQUIVALENT**. Alternative: **A0A1U9RZH7**.

## Manual interpretation

The leading full-length chloroplast maturase-K sequence has 98.21% global identity, eight substitutions and one gap column. Other hits are much shorter maturase fragments. This supports a qualified sequence-based counterpart while preserving the source sequence and documenting the differences.

The primary accession and existing GO annotations are retained. This assessment
does not transfer annotations or establish that every residue difference is neutral.

## Search and sequence evidence

Searched 26,379 sequences across
UP000836841, returning **6** hits.
MMseqs2 is heuristic; the search is not an exhaustive proof of presence or absence.


| Accession | Global identity, including gaps | Query coverage | Target coverage | Global score |
| --- | --- | --- | --- | --- |
| A0A1U9RZH7 | 495/504 (98.21%) | 99.80% | 100.00% | 2584.0 |
| A0AAU9S9N0 | 328/504 (65.08%) | 67.26% | 100.00% | 1576.0 |
| A0AAU9RVA4 | 286/504 (56.75%) | 58.33% | 100.00% | 1307.0 |
| A0AAU9RVL4 | 178/504 (35.32%) | 36.71% | 100.00% | 721.0 |
| A0AAU9S109 | 130/504 (25.79%) | 26.79% | 100.00% | 455.0 |

The [comparison](comparison.yaml) retains every candidate score and metadata;
[candidates.fasta](candidates.fasta) retains all retrieved target sequences.
The top ten have residue-difference lists and detailed alignment files.
[search.tsv](search.tsv) retains the raw search results, including local alignment
coordinates. Long or partial target models must be interpreted using both query
and target coverage rather than a single identity percentage.

## History and database provenance

The [record snapshot](../../matK-record-evidence.yaml) contains current primary
and alternative records, reference-proteome metadata,
source URLs, retrieval timestamps and full UniSave versions:

- 07-JAN-2015, entry version 46. Proteomes: none.
- 11-DEC-2019, entry version 51. Proteomes: none.
- 22-FEB-2023, entry version 53. Proteomes: none.

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
