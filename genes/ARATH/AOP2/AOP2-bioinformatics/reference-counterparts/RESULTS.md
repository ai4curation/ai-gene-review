# ARATH/AOP2: reference-proteome assessment

Manually reviewed: 2026-10-18. Preferred Swiss-Prot accession: **Q945B5**.
Assessment: **LOCUS_COUNTERPART**. Alternative: **Q9ZTA2**.

## Manual interpretation

UniProt explicitly identifies Q9ZTA2 as the Columbia AOP2 allele with a 5-bp deletion leading to a non-functional protein, contrasting the functional Cvi allele Q945B5. The observed sequence differences and length loss are consistent with that curated distinction. Record same-locus correspondence, not equivalent catalytic function.

The primary accession and existing GO annotations are retained. This assessment
does not transfer annotations or establish that every residue difference is neutral.

## Search and sequence evidence

Searched 39,272 sequences across
UP000006548, returning **106** hits.
MMseqs2 is heuristic; the search is not an exhaustive proof of presence or absence.


| Accession | Global identity, including gaps | Query coverage | Target coverage | Global score |
| --- | --- | --- | --- | --- |
| Q9ZTA2 | 390/432 (90.28%) | 92.36% | 100.00% | 1983.5 |
| Q9ZTA1 | 273/441 (61.90%) | 93.06% | 97.81% | 1379.5 |
| Q9ZTA3 | 195/438 (44.52%) | 73.15% | 98.14% | 971.0 |
| Q9C936 | 162/439 (36.90%) | 71.76% | 97.79% | 809.5 |
| Q9C7F0 | 145/445 (32.58%) | 71.53% | 95.96% | 613.0 |

The [comparison](comparison.yaml) retains every candidate score and metadata;
[candidates.fasta](candidates.fasta) retains all retrieved target sequences.
The top ten have residue-difference lists and detailed alignment files.
[search.tsv](search.tsv) retains the raw search results, including local alignment
coordinates. Long or partial target models must be interpreted using both query
and target coverage rather than a single identity percentage.

## History and database provenance

The [record snapshot](../../AOP2-record-evidence.yaml) contains current primary
and alternative records, reference-proteome metadata,
source URLs, retrieval timestamps and full UniSave versions:

- 24-JUN-2015, entry version 46. Proteomes: none.
- 26-FEB-2020, entry version 59. Proteomes: none.
- 27-NOV-2024, entry version 68. Proteomes: none.

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
