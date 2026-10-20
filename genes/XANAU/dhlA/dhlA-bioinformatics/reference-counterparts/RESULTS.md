# XANAU/dhlA: reference-proteome assessment

Manually reviewed: 2026-10-18. Preferred Swiss-Prot accession: **P22643**.
Assessment: **NONE**. Alternative: **none asserted**.

## Manual interpretation

Both exact-taxon reference proteomes were searched as a deduplicated union. The leading alpha/beta-hydrolase hits are remote (about 25% global identity) and do not establish haloalkane dehalogenase identity or substrate specificity. The source is strain GJ10; no supported counterpart was identified in either reference proteome.

The primary accession and existing GO annotations are retained. This assessment
does not transfer annotations or establish that every residue difference is neutral.

## Search and sequence evidence

Searched 9,703 sequences across
UP001161920, UP001603991, returning **9** hits.
MMseqs2 is heuristic; the search is not an exhaustive proof of presence or absence.


| Accession | Global identity, including gaps | Query coverage | Target coverage | Global score |
| --- | --- | --- | --- | --- |
| A0ACG3ZSA9 | 90/359 (25.07%) | 83.87% | 84.14% | 191.0 |
| A0ACG2KQT6 | 61/349 (17.48%) | 36.45% | 74.34% | 181.0 |
| A0ACG2KEY1 | 86/351 (24.50%) | 80.65% | 85.91% | 180.0 |
| A0ACG2KF72 | 81/367 (22.07%) | 89.03% | 82.88% | 144.0 |
| A0ACG3ZS98 | 83/376 (22.07%) | 87.42% | 80.42% | 130.5 |

The [comparison](comparison.yaml) retains every candidate score and metadata;
[candidates.fasta](candidates.fasta) retains all retrieved target sequences.
The top ten have residue-difference lists and detailed alignment files.
[search.tsv](search.tsv) retains the raw search results, including local alignment
coordinates. Long or partial target models must be interpreted using both query
and target coverage rather than a single identity percentage.

## History and database provenance

The [record snapshot](../../dhlA-record-evidence.yaml) contains current primary
record, reference-proteome metadata,
source URLs, retrieval timestamps and full UniSave versions:

- 14-OCT-2015, entry version 97. Proteomes: none.
- 02-DEC-2020, entry version 110. Proteomes: none.
- 27-NOV-2024, entry version 122. Proteomes: none.

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
