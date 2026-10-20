# OCTVU/DDO: reference-proteome assessment

Manually reviewed: 2026-10-18. Preferred Swiss-Prot accession: **A0A7E6FSU6**.
Assessment: **NONE**. Alternative: **none asserted**.

## Manual interpretation

The four returned oxidase-family hits have only about 25-27% global identity and incomplete query coverage. They do not establish a D-aspartate oxidase counterpart; a D-amino-acid oxidase-like label is not evidence of matching substrate specificity. No supported counterpart was identified by this search.

The primary accession and existing GO annotations are retained. This assessment
does not transfer annotations or establish that every residue difference is neutral.

## Search and sequence evidence

Searched 29,931 sequences across
UP001162480, returning **4** hits.
MMseqs2 is heuristic; the search is not an exhaustive proof of presence or absence.


| Accession | Global identity, including gaps | Query coverage | Target coverage | Global score |
| --- | --- | --- | --- | --- |
| A0AA36BXI5 | 93/341 (27.27%) | 68.45% | 97.87% | 341.0 |
| A0AA36BZ05 | 88/338 (26.04%) | 69.64% | 99.15% | 330.0 |
| A0AA36B7D0 | 87/342 (25.44%) | 65.77% | 97.36% | 327.0 |
| A0AA36B6T0 | 42/336 (12.50%) | 31.55% | 100.00% | 28.0 |

The [comparison](comparison.yaml) retains every candidate score and metadata;
[candidates.fasta](candidates.fasta) retains all retrieved target sequences.
The top ten have residue-difference lists and detailed alignment files.
[search.tsv](search.tsv) retains the raw search results, including local alignment
coordinates. Long or partial target models must be interpreted using both query
and target coverage rather than a single identity percentage.

## History and database provenance

The [record snapshot](../../DDO-record-evidence.yaml) contains current primary
record, reference-proteome metadata,
source URLs, retrieval timestamps and full UniSave versions:

- 27-NOV-2024, entry version 16. Proteomes: UP000515154.

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
