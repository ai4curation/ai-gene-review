# PRX2: reference-proteome counterpart assessment

Assessment date: 2026-10-18. Preferred accession: **A9PCL4**.

## Manual interpretation

Relationship: **REFERENCE_PROTEOME_EQUIVALENT** to **B9ILP9**.

Retain A9PCL4 as the primary Swiss-Prot accession. B9ILP9 at POPTR_018G083500 is the manually assessed reference-proteome counterpart: 161/162 identical residues, full ungapped coverage, and only N117D. The competing POPTR_001G423500 paralog (A0A2K2CCD0) differs at seven residues. The original EF146010 cDNA is explicitly from Nisqually-1, so a different cultivar cannot explain this pair. This is a sequence-supported locus assignment, not a shared primary-record locus cross-reference; the one-residue discrepancy remains unexplained. No GO annotations are transferred automatically.

ENA source EF146010 identifies cultivar 383-2499 (Nisqually-1), matching the reference cultivar. The sequence discrepancy could reflect allele or sequence/model differences; the records do not establish which explanation applies.

## Observations

The search covered all **77,340** sequences in
UP000006729, UniProt release 2026_03, and returned 5 hits at E <= 1e-5.
Every returned hit was globally aligned. The leading matches by global score are:

| Accession | Identity, including gaps | Substitutions | Gap columns | Query coverage | Global score |
| --- | --- | --- | --- | --- | --- |
| B9ILP9 | 161/162 (99.38%) | 1 | 0 | 100.00% | 823.0 |
| A0A2K2CCD0 | 155/162 (95.68%) | 7 | 0 | 100.00% | 799.0 |
| A0A2K1Y3S9 | 95/218 (43.58%) | 67 | 56 | 100.00% | 433.5 |
| B9IPE5 | 58/203 (28.57%) | 104 | 41 | 100.00% | 232.0 |
| A0A2K1YA50 | 40/162 (24.69%) | 31 | 91 | 43.83% | 126.5 |

The full table, substitutions, source headers, database checksum, retrieval URL,
release, and tool versions are in [comparison.yaml](comparison.yaml). Each
candidate has a saved alignment, and [candidates.fasta](candidates.fasta) preserves
all returned target sequences. [search.tsv](search.tsv) records the raw MMseqs2
results. The [record snapshot](../../PRX2-record-evidence.yaml) independently
verifies current proteome membership and includes ENA EF146010 and UniSave versions
37, 62, 77. None of those archived versions has a Proteomes link.
This does not prove uninterrupted absence or explain UniProt's decisions.

## Methods and limitations

MMseqs2 18-8cc5c used sensitivity 7.5, E-value 1e-5, max-seqs 1000, four threads.
Biopython 1.85 global alignment used BLOSUM62, gap-open -10, gap-extension -0.5,
with terminal gaps penalized. Identity uses all alignment columns, including
gaps. Coverage is the number of paired nongap residues divided by full sequence
length; terminal gaps cannot silently become 100% coverage.

The database search is heuristic. Global ranking distinguishes retrieved matches,
but does not prove unique genomic placement, synteny, hybrid parental origin, or
identical function at every changed residue. No arbitrary identity threshold
automatically creates an equivalence judgment. Conclusions belong here and in
the manually curated review, not in the analysis code.

Sources: [MMseqs2](https://github.com/soedinglab/MMseqs2/tree/18-8cc5c),
[Biopython pairwise alignment documentation](https://biopython.org/docs/1.85/Tutorial/chapter_pairwise.html),
[UniProt entry history](https://www.uniprot.org/help/entry_history).

## Reproducibility checklist

- [x] Shared analysis scripts take explicit sequence paths and output paths; no gene-specific conclusions or hardcoded gene inputs.
- [x] The same analysis was run on four distinct protein inputs (PRX2, WIN6, PAL, MAOX).
- [x] Searches and alignments completed successfully; all returned accessions resolved to target sequences.
- [x] Direct search results, sequences, alignments, comparison metrics, and provenance are retained here.
- [x] Manual interpretation and its uncertainty are recorded separately from computed outputs.

See [README.md](README.md) and the local [justfile](justfile) to rerun.
