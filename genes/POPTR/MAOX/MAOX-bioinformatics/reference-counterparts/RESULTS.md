# MAOX: reference-proteome counterpart assessment

Assessment date: 2026-10-18. Preferred accession: **P34105**.

## Manual interpretation

Relationship: **REFERENCE_PROTEOME_EQUIVALENT** to **B9ILT5**.

Retain P34105 as the primary Swiss-Prot accession. B9ILT5 at POPTR_018G086700 is the manually assessed reference-proteome counterpart: 584/591 identical residues with full ungapped coverage. Its seven differences are Y53F, H60Q, T84A, I204M, R251K, I413T, and Q457E. It is clearly separated from other malic-enzyme loci in the full-proteome search and global alignments. The original material is hybrid clone 064; sequence equivalence is assessed at the protein/locus level, not as literal identity or proof of parental origin. No GO annotations are transferred automatically.

The primary publication identifies the source material as Populus deltoides x Populus trichocarpa clone 064. ENA X56233 has inconsistent taxonomic text (P.deltoides in its description but P. trichocarpa in its organism field); the publication resolves the experimental source as a hybrid.

## Observations

The search covered all **77,340** sequences in
UP000006729, UniProt release 2026_03, and returned 19 hits at E <= 1e-5.
Every returned hit was globally aligned. The leading matches by global score are:

| Accession | Identity, including gaps | Substitutions | Gap columns | Query coverage | Global score |
| --- | --- | --- | --- | --- | --- |
| B9ILT5 | 584/591 (98.82%) | 7 | 0 | 100.00% | 2997.0 |
| B9GGM4 | 487/649 (75.04%) | 104 | 58 | 100.00% | 2533.5 |
| A0A2K2A764 | 485/600 (80.83%) | 104 | 11 | 99.66% | 2531.5 |
| A0ACC0SW60 | 479/591 (81.05%) | 90 | 22 | 96.28% | 2523.5 |
| B9HE21 | 479/591 (81.05%) | 90 | 22 | 96.28% | 2523.5 |

The full table, substitutions, source headers, database checksum, retrieval URL,
release, and tool versions are in [comparison.yaml](comparison.yaml). Each
candidate has a saved alignment, and [candidates.fasta](candidates.fasta) preserves
all returned target sequences. [search.tsv](search.tsv) records the raw MMseqs2
results. The [record snapshot](../../MAOX-record-evidence.yaml) independently
verifies current proteome membership and includes ENA X56233 and UniSave versions
101, 118, 132. None of those archived versions has a Proteomes link.
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
