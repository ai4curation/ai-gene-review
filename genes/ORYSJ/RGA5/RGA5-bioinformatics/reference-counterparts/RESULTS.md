# ORYSJ/RGA5: reference-proteome assessment

Manually reviewed: 2026-10-19. Preferred Swiss-Prot accession: **F7J0N2**.
Assessment: **CANDIDATE**. Alternative: **Q2R8L1**.

## Manual interpretation

The captured evidence does not independently map the Sasanishiki protein to
Nipponbare Os11g0225300 / LOC_Os11g11810. Those locus identifiers locate Q2R8L1
only. The shared RGA5 name and cultivar-dependent AVR-Pia recognition statement
do not establish cross-cultivar locus correspondence at this variable resistance
region. The alignment has 624/1105 paired identities (56.4706%) and 207 gap
columns; its global identity is 47.561%. Retain Q2R8L1 as a candidate pending
independent locus mapping. This supersedes the 2026-10-18 locus-counterpart
assessment, rather than treating a gene name as mapping evidence.

The primary accession and existing GO annotations are retained. This assessment
does not transfer annotations or establish that every residue difference is neutral.

## Search and sequence evidence

Searched 48,896 sequences across
UP000059680, returning **404** hits.
MMseqs2 is heuristic; the search is not an exhaustive proof of presence or absence.


| Accession | Global identity, including gaps | Query coverage | Target coverage | Global score |
| --- | --- | --- | --- | --- |
| Q2R8L1 | 624/1312 (47.56%) | 99.01% | 84.93% | 2768.0 |
| Q2QZJ7 | 472/1270 (37.17%) | 93.73% | 87.17% | 1789.0 |
| A0A0P0Y630 | 434/1165 (37.25%) | 83.60% | 95.01% | 1766.5 |
| Q109S4 | 456/1363 (33.46%) | 94.09% | 80.96% | 1667.0 |
| A0A0N7KSM9 | 373/1119 (33.33%) | 74.82% | 99.64% | 1529.0 |

The [comparison](comparison.yaml) retains every candidate score and metadata;
[candidates.fasta](candidates.fasta) retains all retrieved target sequences.
The top ten have residue-difference lists and detailed alignment files.
[search.tsv](search.tsv) retains the raw search results, including local alignment
coordinates. Long or partial target models must be interpreted using both query
and target coverage rather than a single identity percentage.

## History and database provenance

The [record snapshot](../../RGA5-record-evidence.yaml) contains current primary
and alternative records, reference-proteome metadata,
source URLs, retrieval timestamps and full UniSave versions:

- 09-DEC-2015, entry version 12. Proteomes: none.
- 11-DEC-2019, entry version 31. Proteomes: none.
- 27-NOV-2024, entry version 45. Proteomes: none.

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
