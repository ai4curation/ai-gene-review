# DERPT/Derp23: reference-proteome assessment

Manually reviewed: 2026-10-18. Preferred Swiss-Prot accession: **L7N6F8**.
Assessment: **CANDIDATE**. Alternative: **A0ABQ8JBE4**.

## Manual interpretation

The leading small chitin-binding protein is a plausible Der p 23 counterpart, but global identity is 75.51% with substitutions and indels. Other chitin-binding proteins are present, and no shared source/target locus cross-reference establishes identity. Retain a candidate pending genomic mapping and gene-model assessment.

The primary accession and existing GO annotations are retained. This assessment
does not transfer annotations or establish that every residue difference is neutral.

## Search and sequence evidence

Searched 14,675 sequences across
UP000887458, returning **4** hits.
MMseqs2 is heuristic; the search is not an exhaustive proof of presence or absence.


| Accession | Global identity, including gaps | Query coverage | Target coverage | Global score |
| --- | --- | --- | --- | --- |
| A0ABQ8JBE4 | 74/98 (75.51%) | 92.22% | 91.21% | 379.0 |
| A0ABQ8JAT2 | 41/328 (12.50%) | 95.56% | 26.54% | 50.5 |
| A0ABQ8JAU3 | 39/597 (6.53%) | 82.22% | 12.74% | -114.5 |
| A0ABQ8JLF8 | 35/1052 (3.33%) | 100.00% | 8.56% | -391.5 |

The [comparison](comparison.yaml) retains every candidate score and metadata;
[candidates.fasta](candidates.fasta) retains all retrieved target sequences.
The top ten have residue-difference lists and detailed alignment files.
[search.tsv](search.tsv) retains the raw search results, including local alignment
coordinates. Long or partial target models must be interpreted using both query
and target coverage rather than a single identity percentage.

## History and database provenance

The [record snapshot](../../Derp23-record-evidence.yaml) contains current primary
and alternative records, reference-proteome metadata,
source URLs, retrieval timestamps and full UniSave versions:

- 09-DEC-2015, entry version 10. Proteomes: none.
- 17-JUN-2020, entry version 26. Proteomes: none.
- 24-JUL-2024, entry version 33. Proteomes: UP000515146.

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
