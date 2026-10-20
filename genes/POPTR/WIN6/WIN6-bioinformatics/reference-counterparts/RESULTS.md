# WIN6: reference-proteome counterpart assessment

Assessment date: 2026-10-18. Preferred accession: **P16579**.

## Manual interpretation

Relationship: **REFERENCE_PROTEOME_CANDIDATE** to **B9HQY4**.

Retain P16579 as the primary Swiss-Prot accession. B9HQY4 at POPTR_009G141800v4 is the leading candidate, not an established equivalent. It has 317 identical residues across 340 global-alignment columns (16 substitutions and seven gap columns). B9HQZ1 represents a second model of the same locus, while nearby chitinase loci also match strongly. Hybrid H11-11 provenance and the absence of a direct locus cross-reference leave allele, model, and paralog alternatives unresolved. Mapping source genomic record U01661, including flanks, to the reference assembly is needed before promoting this relationship. No GO annotations are transferred automatically.

ENA assigns the original genomic sequence U01661 to Populus trichocarpa x Populus deltoides, strain H11-11, whereas UniProtKB assigns P16579 to taxon 3694. This hybrid origin is relevant even though the live UniProt taxonomy matches the reference species.

## Observations

The search covered all **77,340** sequences in
UP000006729, UniProt release 2026_03, and returned 33 hits at E <= 1e-5.
Every returned hit was globally aligned. The leading matches by global score are:

| Accession | Identity, including gaps | Substitutions | Gap columns | Query coverage | Global score |
| --- | --- | --- | --- | --- | --- |
| B9HQY4 | 317/340 (93.24%) | 16 | 7 | 97.94% | 1788.0 |
| B9HQZ1 | 306/342 (89.47%) | 26 | 10 | 97.65% | 1711.5 |
| A0A2K1Z7S7 | 293/340 (86.18%) | 43 | 4 | 98.82% | 1641.0 |
| A0ACC0SI85 | 291/340 (85.59%) | 39 | 10 | 97.06% | 1626.0 |
| A0A2K1Z7S6 | 291/340 (85.59%) | 39 | 10 | 97.06% | 1617.0 |

The full table, substitutions, source headers, database checksum, retrieval URL,
release, and tool versions are in [comparison.yaml](comparison.yaml). Each
candidate has a saved alignment, and [candidates.fasta](candidates.fasta) preserves
all returned target sequences. [search.tsv](search.tsv) records the raw MMseqs2
results. The [record snapshot](../../WIN6-record-evidence.yaml) independently
verifies current proteome membership and includes ENA U01661 and UniSave versions
109, 128, 138. None of those archived versions has a Proteomes link.
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
