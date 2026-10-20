# MEDTR/NORK: reference-proteome assessment

Manually reviewed: 2026-10-18. Preferred Swiss-Prot accession: **Q8L4H4**.
Assessment: **EQUIVALENT**. Alternative: **A9YWR7**.

## Manual interpretation

The reference sequence is exactly identical across all 925 residues. G7KGF4 is an additional shorter model with 902 identical residues, but A9YWR7 represents the complete primary sequence. The kinase-family search reached its 1000-hit cap; this does not weaken the observed full-length identity but prevents claiming exhaustive paralog retrieval.

The primary accession and existing GO annotations are retained. This assessment
does not transfer annotations or establish that every residue difference is neutral.

## Search and sequence evidence

Searched 57,093 sequences across
UP000002051, returning **1000** hits.
MMseqs2 is heuristic; the search is not an exhaustive proof of presence or absence.
The 1000-hit retrieval cap was reached, so exhaustive paralog retrieval cannot be claimed.

| Accession | Global identity, including gaps | Query coverage | Target coverage | Global score |
| --- | --- | --- | --- | --- |
| A9YWR7 | 925/925 (100.00%) | 100.00% | 100.00% | 4791.0 |
| G7KGF4 | 902/925 (97.51%) | 97.51% | 100.00% | 4651.0 |
| A0A072VL02 | 334/998 (33.47%) | 92.00% | 92.10% | 1152.0 |
| G7J2J5 | 334/1008 (33.13%) | 91.57% | 91.08% | 1150.0 |
| G7L1Q0 | 328/1001 (32.77%) | 92.54% | 91.85% | 1128.5 |

The [comparison](comparison.yaml) retains every candidate score and metadata;
[candidates.fasta](candidates.fasta) retains all retrieved target sequences.
The top ten have residue-difference lists and detailed alignment files.
[search.tsv](search.tsv) retains the raw search results, including local alignment
coordinates. Long or partial target models must be interpreted using both query
and target coverage rather than a single identity percentage.

## History and database provenance

The [record snapshot](../../NORK-record-evidence.yaml) contains current primary
and alternative records, reference-proteome metadata,
source URLs, retrieval timestamps and full UniSave versions:

- 11-NOV-2015, entry version 79. Proteomes: none.
- 07-OCT-2020, entry version 105. Proteomes: none.
- 27-NOV-2024, entry version 119. Proteomes: none.

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
