# pmp20-bioinformatics

Reproducible analyses for assessing whether `SCHPO/pmp20` plausibly supports thioredoxin-dependent peroxidase activity.

## Scope

This workflow implements three analysis layers:

1. Build a calibrated protein set (target + active controls).
2. Sequence-level catalytic-site and cysteine topology comparison.
3. AlphaFold structure cysteine geometry checks.

No script contains hardcoded gene-specific outputs. All scripts take input files/paths as arguments.

## Inputs

- `inputs/proteins.tsv`: main run with `pmp20` as target.
- `inputs/proteins-test-tpx1.tsv`: alternate run used to test script generality (`tpx1` as target).

Each input row defines:

- `source_type=local_uniprot_txt` with a path to a UniProt text record already in repo, or
- `source_type=uniprot_accession` to fetch from UniProt REST.

## Run

From this directory:

```bash
just all
```

Or step-by-step:

```bash
just setup
just main
just test
```

## Outputs

Main run outputs under `results/main/`:

- `protein_summary.tsv`, `proteins.json`, `proteins.fasta`
- `sequence/sequence_cysteine_summary.tsv`
- `sequence/target_vs_active_alignment.tsv`
- `structures/alphafold_manifest.tsv`
- `structure/structure_cys_summary.tsv`
- `structure/structure_cys_pair_distances.tsv`

Test run outputs under `results/test_tpx1/` with the same structure.

## Notes

- AlphaFold models are retrieved through the AlphaFold API endpoint for each accession.
- Structural distances are SG-SG distances between cysteine residues in monomer models.
- Biological interpretation belongs in `RESULTS.md`, not in scripts.
