# SNIPE Bioinformatics: Architecture-Aware Feature Analysis

## Goal

Identify data-driven feature combinations that can support an architecture-aware rule for SNIPE-like proteins, especially:

- focal domain: `IPR025280` (SNIPE associated domain)
- catalytic partner domains (for example, GIY-YIG-like partner domains)
- membrane-targeting features (N-terminal TM-like segments and membrane-associated accessory domains)

## Script

- `scripts/analyze_interpro_architecture.py`

The script is parameterized and does not hardcode entry IDs or output paths.

## Reproducible Runs

From this directory:

```bash
just analyze-ipr025280
just analyze-control
just all
```

## Outputs

Per run, outputs are written to `results/<ENTRY>/`:

- `architecture_table.tsv`: IDA architectures and prevalence
- `architecture_domains.tsv`: representative-domain coordinates per architecture
- `representative_extra_features.tsv`: TMhelix/signal peptide features on representatives
- `domain_metadata.tsv`: domain names/descriptions for observed accessions
- `cooccurring_domain_weighted.tsv`: weighted prevalence of co-occurring domains
- `nterm_tm_heuristic_by_ida.tsv`: N-terminal TM-like heuristic by architecture
- `nterm_tm_heuristic_overall.tsv`: overall N-terminal TM-like signal
- `summary.json`: compact run summary

## Notes

- The N-terminal TM-like signal is a sequence heuristic and is explicitly not a replacement for TMHMM.
- Extra-feature calls for representative proteins are retrieved from InterPro API `?extra_features`.
