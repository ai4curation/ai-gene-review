# Expanded human DeepTMHMM2 panel

This run extends the earlier SPTLC2/DPM1 pilot to 31 canonical human sequences:
the 23 S20 proteins with existing repository reviews, plus eight controls from
outside that S20 subset. Thus 29 proteins are newly run locally, and two are
repeated controls. The panel contains 16,266 residues.

Additional controls were selected before prediction from cached UniProt records
and existing gene reviews:

| Gene | Expected broad properties from those sources |
|---|---|
| EGFR | Cleavable signal peptide, one transmembrane helix, plasma-membrane receptor |
| CFTR | Twelve transmembrane helices, plasma-membrane anion channel |
| TOMM40 | Nineteen-strand mitochondrial outer-membrane beta barrel |
| CALR | Signal peptide; soluble mature protein in the ER lumen |
| SPTLC1 | One transmembrane helix; ER-membrane SPT subunit |
| GAPDH | No constitutive transmembrane segment; cytosolic glycolytic enzyme with additional context-dependent locations |
| INS | Signal peptide in the full preproinsulin precursor; secreted mature hormone |
| COX4I1 | Mitochondrial transit peptide and one inner-membrane helix |

These are sanity checks, not a blind accuracy benchmark. Training-set exclusion
and family independence were not established. S20 is itself selected for unusual
predictions. The stored UniProt TRANSMEM features are a comparison source, not
universal ground truth: the preceding audit identified errors in several records.

## Reproduce

First install the parent benchmark's locked environment and checkpoints, as
described in its README. Then run from this directory, sequentially to avoid
competing inference workloads:

```sh
just prepare
just api
just cli
just precision
just summarize
```

The API benchmark uses the existing singleton-unbatching adapter, two repeats,
eight CPU threads, a fixed PyTorch seed and the full five-member ensemble.
The unmodified upstream CLI is run once with batch size 1 and the same models,
thread count and device. This panel does not request marginals or plotting.
Per-sequence API times exclude export, whereas process times include startup
and export. Peak RSS is cumulative within each process. Neither pathway reuses
ESM embeddings between repeats.

The three-case `precision` diagnostic repeats COQ5, SPTLC1 and TOMM40 with
`--cpu-autocast`, enabling the CLI's precision policy only for task-model
inference. ESM embeddings still use FP32. This optional flag was added to the
benchmark harness after the main panel revealed small API/CLI differences; its
default is false and the original API behavior is unchanged. The diagnostic's
timings and predictions are separate from the main 31-protein measurements.

`../panel_tools.py` accepts arbitrary target lists, repository/organism/taxon
arguments, manifests, prediction directories and comparison tables. It verifies
human taxonomy, standard amino acids and unique accessions when preparing input;
it checks sequence hashes, prediction coverage, repeat consistency and CLI/API
agreement when summarizing. See `targets.tsv`, `inputs.tsv`, `inputs.fasta`,
`summary.tsv`, `summary.json` and raw `api/` and `cli/` results.

The S20 comparison tests exact IF, RE, signal and transit-peptide coordinates
against the supplied workbook, ignoring compartment labels. S20 does not supply
sequence hashes, so coordinate agreement is not proof of identical input
sequences. Full sequences and hashes for this run are retained in the manifest.
Generic inside/outside labels on non-TM outputs do not establish compartments.

Source code is pinned to DeepTMHMM2 commit
`526f6c60f93c0868c7315413da8e669d12373cc3`; dependencies are in the parent
`pyproject.toml` and `uv.lock`. Model and source-file provenance is recorded in
`provenance.json`. Biological interpretation and measured costs belong in
`RESULTS.md`, not in the analysis scripts. No gene annotation is changed merely
because of this panel's predictions.
