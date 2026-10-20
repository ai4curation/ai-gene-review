# ORYSJ/PIKM1-TS: reference-proteome assessment

Manually reviewed: 2026-10-18. Preferred Swiss-Prot accession: **B5UBC1**.
Assessment: **CANDIDATE**. Alternative: **Q2QZF2**.

## Manual interpretation

The leading hit is reviewed PIK5-NP, with the synonym PIKM1, but only 58.42% global identity and extensive differences. The source cultivars differ, and the reference record describes Nipponbare lacking AVR-Pik recognition. A related resistance-locus representation is plausible, but copy-number, locus and specificity differences prevent an equivalence assertion.

The primary accession and existing GO annotations are retained. This assessment
does not transfer annotations or establish that every residue difference is neutral.

## Search and sequence evidence

Searched 48,896 sequences across
UP000059680, returning **384** hits.
MMseqs2 is heuristic; the search is not an exhaustive proof of presence or absence.


| Accession | Global identity, including gaps | Query coverage | Target coverage | Global score |
| --- | --- | --- | --- | --- |
| Q2QZF2 | 697/1193 (58.42%) | 94.05% | 95.56% | 3081.0 |
| Q6Z011 | 318/1230 (25.85%) | 77.60% | 91.07% | 748.0 |
| Q943S7 | 300/1188 (25.25%) | 68.24% | 94.55% | 741.0 |
| Q53KR6 | 313/1210 (25.87%) | 81.54% | 93.29% | 727.5 |
| A0A0P0Y455 | 298/1208 (24.67%) | 78.74% | 93.26% | 721.0 |

The [comparison](comparison.yaml) retains every candidate score and metadata;
[candidates.fasta](candidates.fasta) retains all retrieved target sequences.
The top ten have residue-difference lists and detailed alignment files.
[search.tsv](search.tsv) retains the raw search results, including local alignment
coordinates. Long or partial target models must be interpreted using both query
and target coverage rather than a single identity percentage.

## History and database provenance

The [record snapshot](../../PIKM1-TS-record-evidence.yaml) contains current primary
and alternative records, reference-proteome metadata,
source URLs, retrieval timestamps and full UniSave versions:

- 09-DEC-2015, entry version 28. Proteomes: none.
- 11-DEC-2019, entry version 50. Proteomes: none.
- 27-NOV-2024, entry version 64. Proteomes: none.

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
