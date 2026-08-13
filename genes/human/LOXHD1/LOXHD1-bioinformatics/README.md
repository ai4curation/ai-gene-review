# LOXHD1 PLAT-repeat and isoform analysis

## Objective

This analysis maps the alternative-sequence features in the curated UniProt
record for human LOXHD1 (Q8IVV2) onto its annotated PLAT repeats and quantifies
pairwise sequence identity among those repeats. It addresses two narrow
questions that the flat record does not summarize explicitly:

1. Which PLAT repeats are retained, lost, partially deleted, or sequence-altered
   in each named UniProt isoform?
2. Are the 15 annotated PLAT segments detectably homologous to one another at
   the primary-sequence level?

The analysis does **not** infer catalytic activity from sequence. Absence of an
annotated catalytic domain or motif is not proof that a protein is
nonenzymatic.

## Inputs and provenance

- `../LOXHD1-uniprot.txt`: project-cached UniProtKB/Swiss-Prot record, entry
  version 161 (10 June 2026), sequence version 4.
- `../../LOX/LOX-uniprot.txt`: an independently curated human protein used as
  a negative control for selecting domains whose note contains `PLAT`.
- `../../GLRX3/GLRX3-uniprot.txt`: an independently curated multidomain human
  protein used as a positive control with `Glutaredoxin` as the repeat label.

Input hashes and the Python version are recorded in each `summary.json`.

## Method

`analyze_uniprot_architecture.py` parses the UniProt flat file rather than using
gene-specific coordinates. It:

- validates the parsed sequence length against the UniProt `ID` line;
- extracts every `DOMAIN` and `VAR_SEQ` feature;
- assigns `LOST`, `PARTIAL`, `ALTERED`, or `RETAINED` to each selected repeat in
  each named isoform based only on coordinate overlap and feature text;
- globally aligns every selected repeat pair with a deterministic dynamic
  programming alignment (match +1, mismatch 0, gap -1), then reports exact
  residue identity divided by aligned length.

The pairwise identities measure divergence among repeats within one human
protein. They are not ortholog conservation estimates.

## Reproduction

No third-party Python packages are required; the script uses Python's standard
library. Python 3.10.9 is pinned in `.python-version`, and `uv --no-project`
runs that interpreter without creating a local environment; the dependency-free
`pyproject.toml` and `uv.lock` record the project metadata. From this directory:

```bash
just all
just check
```

To analyze another UniProt flat file without changing code:

```bash
just analyze /path/to/record.txt /path/to/output PLAT
```

## Outputs

- `results/domains.tsv`: all annotated domains and repeat-selection flag.
- `results/isoform_repeat_effects.tsv`: coordinate-derived state of each PLAT
  repeat in each named isoform.
- `results/repeat_pairwise_identity.tsv`: all pairwise PLAT-repeat identities.
- `results/summary.json`: counts, identity range, input hash, and provenance.
- `control-results/lox-negative/`: the same outputs for the LOX negative
  control.
- `control-results/glrx3-positive/`: outputs for a GLRX3 positive control that
  exercises selection and pairwise comparison of two repeated domains.

Data source: the project-cached UniProtKB/Swiss-Prot flat records listed above.
