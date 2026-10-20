# ORYSJ/RGA4: reference-proteome assessment

Manually reviewed: 2026-10-18. Preferred Swiss-Prot accession: **F7J0M4**.
Assessment: **LOCUS_COUNTERPART**. Alternative: **F7J0M6**.

## Manual interpretation

Both reviewed records represent RGA4 in different rice cultivars, and the reference entry is the leading full-length match. UniProt contrasts AVR-Pia recognition in Aichi asahi/Sasanishiki with its absence in Nipponbare. Record this as a reference-cultivar locus counterpart, not equivalent resistance function; loss of recognition by the RGA4/RGA5 system does not establish that RGA4 alone is inactive.

The primary accession and existing GO annotations are retained. This assessment
does not transfer annotations or establish that every residue difference is neutral.

## Search and sequence evidence

Searched 48,896 sequences across
UP000059680, returning **358** hits.
MMseqs2 is heuristic; the search is not an exhaustive proof of presence or absence.


| Accession | Global identity, including gaps | Query coverage | Target coverage | Global score |
| --- | --- | --- | --- | --- |
| F7J0M6 | 951/1017 (93.51%) | 99.70% | 97.93% | 4845.0 |
| A0A0P0Y1V1 | 434/1030 (42.14%) | 95.88% | 96.56% | 1851.5 |
| Q2QZH9 | 430/1158 (37.13%) | 93.88% | 85.23% | 1698.5 |
| Q2QZJ3 | 410/1083 (37.86%) | 91.47% | 91.28% | 1643.5 |
| Q53NZ3 | 409/1042 (39.25%) | 93.37% | 95.29% | 1617.5 |

The [comparison](comparison.yaml) retains every candidate score and metadata;
[candidates.fasta](candidates.fasta) retains all retrieved target sequences.
The top ten have residue-difference lists and detailed alignment files.
[search.tsv](search.tsv) retains the raw search results, including local alignment
coordinates. Long or partial target models must be interpreted using both query
and target coverage rather than a single identity percentage.

## History and database provenance

The [record snapshot](../../RGA4-record-evidence.yaml) contains current primary
and alternative records, reference-proteome metadata,
source URLs, retrieval timestamps and full UniSave versions:

- 09-DEC-2015, entry version 17. Proteomes: none.
- 12-AUG-2020, entry version 38. Proteomes: none.
- 27-NOV-2024, entry version 48. Proteomes: none.

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
