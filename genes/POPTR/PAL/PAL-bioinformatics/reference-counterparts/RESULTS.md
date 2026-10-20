# PAL: reference-proteome counterpart assessment

Assessment date: 2026-10-18. Preferred accession: **P45730**.

## Manual interpretation

Relationship: **REFERENCE_PROTEOME_EQUIVALENT** to **A0A2K1XD28**.

Retain P45730 as the primary Swiss-Prot accession. A0A2K1XD28 at POPTR_016G091100 is the manually assessed reference-proteome counterpart: 714/715 identical residues with full ungapped coverage and only R22L. The next full-length family match, A0A2K2A1A8 at POPTR_006G126800, has 32 substitutions and one gap column. The source sequence is from a P. trichocarpa x P. deltoides hybrid; the counterpart assignment is inferred from the sequence comparison and does not establish the parental origin or cause of R22L. No GO annotations are transferred automatically.

Both the Swiss-Prot source citation and ENA L11747 identify a P. trichocarpa x P. deltoides hybrid. The reference proteome is Nisqually. Hybrid provenance makes a small sequence difference plausible but does not itself establish locus identity.

## Observations

The search covered all **77,340** sequences in
UP000006729, UniProt release 2026_03, and returned 8 hits at E <= 1e-5.
Every returned hit was globally aligned. The leading matches by global score are:

| Accession | Identity, including gaps | Substitutions | Gap columns | Query coverage | Global score |
| --- | --- | --- | --- | --- | --- |
| A0A2K1XD28 | 714/715 (99.86%) | 1 | 0 | 100.00% | 3652.0 |
| A0A2K2A1A8 | 682/715 (95.38%) | 32 | 1 | 99.86% | 3492.0 |
| A0ACC0SF52 | 612/717 (85.36%) | 97 | 8 | 99.16% | 3136.0 |
| A0A2K1ZBC0 | 608/715 (85.03%) | 103 | 4 | 99.44% | 3126.0 |
| A0A3N7FNR6 | 602/717 (83.96%) | 107 | 8 | 99.16% | 3090.0 |

The full table, substitutions, source headers, database checksum, retrieval URL,
release, and tool versions are in [comparison.yaml](comparison.yaml). Each
candidate has a saved alignment, and [candidates.fasta](candidates.fasta) preserves
all returned target sequences. [search.tsv](search.tsv) records the raw MMseqs2
results. The [record snapshot](../../PAL-record-evidence.yaml) independently
verifies current proteome membership and includes ENA L11747 and UniSave versions
97, 113, 124. None of those archived versions has a Proteomes link.
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
