# DERPT/Derp1: reference-proteome assessment

Manually reviewed: 2026-10-18. Preferred Swiss-Prot accession: **P08176**.
Assessment: **CANDIDATE**. Alternative: **A0ABQ8JGY3**.

## Manual interpretation

The full 320-residue query is represented within a much longer 837-residue reference model: 300 identities over 320 paired residues, but only 35.84% identity when all global-alignment columns are counted. The target is labeled MCM2_2/MCM DNA helicase despite peptidase-C1 family evidence. This is a possible fused or otherwise problematic gene model, not an established intact equivalent; retain a candidate for genomic/model review.

The primary accession and existing GO annotations are retained. This assessment
does not transfer annotations or establish that every residue difference is neutral.

## Search and sequence evidence

Searched 14,675 sequences across
UP000887458, returning **22** hits.
MMseqs2 is heuristic; the search is not an exhaustive proof of presence or absence.


| Accession | Global identity, including gaps | Query coverage | Target coverage | Global score |
| --- | --- | --- | --- | --- |
| A0ABQ8JGY3 | 300/837 (35.84%) | 100.00% | 38.23% | 1316.0 |
| A0ABQ8J3M6 | 203/578 (35.12%) | 100.00% | 55.36% | 906.0 |
| A0ABQ8J1K1 | 206/617 (33.39%) | 99.69% | 51.79% | 882.0 |
| A0ABQ8JRE2 | 183/662 (27.64%) | 98.75% | 48.02% | 746.5 |
| A0ABQ8J192 | 137/366 (37.43%) | 99.38% | 87.36% | 614.5 |

The [comparison](comparison.yaml) retains every candidate score and metadata;
[candidates.fasta](candidates.fasta) retains all retrieved target sequences.
The top ten have residue-difference lists and detailed alignment files.
[search.tsv](search.tsv) retains the raw search results, including local alignment
coordinates. Long or partial target models must be interpreted using both query
and target coverage rather than a single identity percentage.

## History and database provenance

The [record snapshot](../../Derp1-record-evidence.yaml) contains current primary
and alternative records, reference-proteome metadata,
source URLs, retrieval timestamps and full UniSave versions:

- 14-OCT-2015, entry version 114. Proteomes: none.
- 07-OCT-2020, entry version 131. Proteomes: none.
- 29-MAY-2024, entry version 142. Proteomes: UP000515146.

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
