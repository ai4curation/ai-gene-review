# THLAR/TFP: reference-proteome assessment

Manually reviewed: 2026-10-18. Preferred Swiss-Prot accession: **G1FNI6**.
Assessment: **EQUIVALENT**. Alternative: **A0AAU9R9U8**.

## Manual interpretation

The leading reference sequence has 97.13% global identity, full target coverage and a short terminal difference, and is separated from other specifier-family hits. This supports a qualified sequence-based counterpart. Its generic epithiospecifier annotation does not independently establish thiocyanate-forming specificity, so functional annotation transfer still requires review.

The primary accession and existing GO annotations are retained. This assessment
does not transfer annotations or establish that every residue difference is neutral.

## Search and sequence evidence

Searched 26,379 sequences across
UP000836841, returning **28** hits.
MMseqs2 is heuristic; the search is not an exhaustive proof of presence or absence.


| Accession | Global identity, including gaps | Query coverage | Target coverage | Global score |
| --- | --- | --- | --- | --- |
| A0AAU9R9U8 | 338/348 (97.13%) | 97.70% | 100.00% | 1819.5 |
| A0AAU9RD64 | 292/349 (83.67%) | 99.71% | 99.71% | 1564.0 |
| A0AAU9T6G1 | 289/348 (83.05%) | 99.43% | 100.00% | 1563.0 |
| A0AAU9RA61 | 289/350 (82.57%) | 99.14% | 99.42% | 1531.0 |
| A0AAU9RWR0 | 274/348 (78.74%) | 99.14% | 100.00% | 1480.0 |

The [comparison](comparison.yaml) retains every candidate score and metadata;
[candidates.fasta](candidates.fasta) retains all retrieved target sequences.
The top ten have residue-difference lists and detailed alignment files.
[search.tsv](search.tsv) retains the raw search results, including local alignment
coordinates. Long or partial target models must be interpreted using both query
and target coverage rather than a single identity percentage.

## History and database provenance

The [record snapshot](../../TFP-record-evidence.yaml) contains current primary
and alternative records, reference-proteome metadata,
source URLs, retrieval timestamps and full UniSave versions:

- 11-NOV-2015, entry version 12. Proteomes: none.
- 11-DEC-2019, entry version 25. Proteomes: none.
- 27-NOV-2024, entry version 36. Proteomes: none.

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
