# ARATH/FRI: reference-proteome assessment

Manually reviewed: 2026-10-18. Preferred Swiss-Prot accession: **P0DH90**.
Assessment: **LOCUS_COUNTERPART**. Alternative: **Q67Z93**.

## Manual interpretation

UniProt explicitly links active FRI from cv. H51 to the inactive Columbia allele Q67Z93. The reference protein covers only part of the full active sequence; curated cautions attribute inactivity to loss-of-function mutations. This is a same-locus counterpart, not functional equivalence.

The primary accession and existing GO annotations are retained. This assessment
does not transfer annotations or establish that every residue difference is neutral.

## Search and sequence evidence

Searched 39,272 sequences across
UP000006548, returning **6** hits.
MMseqs2 is heuristic; the search is not an exhaustive proof of presence or absence.


| Accession | Global identity, including gaps | Query coverage | Target coverage | Global score |
| --- | --- | --- | --- | --- |
| Q67Z93 | 311/609 (51.07%) | 51.56% | 100.00% | 1403.0 |
| Q67ZB3 | 146/684 (21.34%) | 79.31% | 86.56% | 300.5 |
| Q9C6S2 | 126/631 (19.97%) | 74.06% | 95.35% | 261.0 |
| Q9LUV4 | 133/650 (20.46%) | 80.62% | 92.29% | 258.0 |
| Q9FFF1 | 132/653 (20.21%) | 69.95% | 90.64% | 207.5 |

The [comparison](comparison.yaml) retains every candidate score and metadata;
[candidates.fasta](candidates.fasta) retains all retrieved target sequences.
The top ten have residue-difference lists and detailed alignment files.
[search.tsv](search.tsv) retains the raw search results, including local alignment
coordinates. Long or partial target models must be interpreted using both query
and target coverage rather than a single identity percentage.

## History and database provenance

The [record snapshot](../../FRI-record-evidence.yaml) contains current primary
and alternative records, reference-proteome metadata,
source URLs, retrieval timestamps and full UniSave versions:

- 11-NOV-2015, entry version 21. Proteomes: none.
- 12-AUG-2020, entry version 36. Proteomes: none.
- 24-JAN-2024, entry version 43. Proteomes: none.

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
