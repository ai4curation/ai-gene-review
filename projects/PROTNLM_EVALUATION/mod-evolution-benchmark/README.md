---
title: Human and MOD challenge-set source bundle
autolink_gene_symbols: false
---
# Source bundle

[Selection page](../mod-evolution20.md)

[Choices](selection.csv) · [Joined cohort](cohort.csv) · [Prediction statements](prediction-statements.csv) · [Complete API snapshot](api-snapshot.jsonl.gz) · [Reference searches](reference-searches.jsonl.gz) · [Reference matches](same-gene-references.csv) · [Current sequences](sequences.fasta) · [Published list](published-accessions.tsv.gz) · [Summary](summary.json) · [Checksums](manifest.json) · [Generator](summarize.py)

`selection.csv` records the twenty deliberate choices, review questions, priorities and proposed evolutionary comparisons. Priorities are work order, not predicted error severity. `cohort.csv` joins those choices to frozen source metadata. `prediction-statements.csv` preserves each emitted name, GO term, function paragraph and localization statement with its source object and evidence metadata. The complete API responses retain other fields as well.

`api-snapshot.jsonl.gz` contains HTTP status, retrieval time, URL, complete ProtNLM response and ordinary UniProt record for each accession. All forty requests succeeded. `reference-searches.jsonl.gz` preserves same-species reviewed-record queries, including empty results and ambiguous name hits. `same-gene-references.csv` accepts reference matches only when a MOD identifier is shared. No sequence alignment or functional transfer is implied by that match.

`published-accessions.tsv.gz` is the public accession list retrieved for the pombe availability check on 2026-09-10 UTC. Initial candidate discovery joined this list to the original 28,553-entry XML export; final target statements use the fresh API snapshots in this bundle. Selection is not a complete census of any species and does not establish absence of predictions for other genes.

`sequences.fasta` contains current exact-accession UniProt sequences. ProtNLM responses do not expose their historical input sequence. Do not relabel these sequences as verified original model inputs or replace a prediction target with a longer same-gene record.

Regenerate derived tables and the checksum manifest offline:

```bash
UV_NO_SYNC=1 uv run python projects/PROTNLM_EVALUATION/mod-evolution-benchmark/summarize.py
```

The generator preserves output strings and emits no biological assessments. The five priority investigations and their primary literature leads are on the selection page; evolutionary comparators are proposals awaiting identifier verification, retrieval and analysis.
