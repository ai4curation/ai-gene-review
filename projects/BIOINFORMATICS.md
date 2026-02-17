# BIOINFORMATICS Case Studies

## Purpose

This document records concrete cases where custom bioinformatics analysis was used to resolve annotation uncertainty in `ai-gene-review`.

Each case links:
- biological question
- reproducible analysis workflow
- key outputs
- impact on curation decisions

## Case Studies

| Case ID | Gene | Species | Question | Outcome |
|---|---|---|---|---|
| BIO-001 | pmp20 | SCHPO (*S. pombe*) | Does pmp20 have thioredoxin-dependent peroxidase activity? | Evidence supports loss of canonical thioredoxin-dependent peroxidase function |

## BIO-001: SCHPO/pmp20 (thioredoxin-dependent peroxidase activity)

### Context

`pmp20` is in the peroxiredoxin family, but automated/domain-based annotations suggested peroxidase activity while literature and curated UniProt comments indicated loss of thioredoxin-dependent activity.

### Curation question

Should GO molecular function terms related to peroxidase/thioredoxin peroxidase activity be retained or removed for `SCHPO/pmp20`?

### Analysis workflow

- Analysis directory: `genes/SCHPO/pmp20/pmp20-bioinformatics`
- Run command: `just all`
- Main run dataset: `genes/SCHPO/pmp20/pmp20-bioinformatics/inputs/proteins.tsv`
- Alternate test dataset (script generality): `genes/SCHPO/pmp20/pmp20-bioinformatics/inputs/proteins-test-tpx1.tsv`

Methods implemented:
1. Collect target + active controls from local UniProt TXT and UniProt REST.
2. Compare cysteine topology and catalytic-site correspondence at sequence level.
3. Map target residues against active-control resolving-cysteine positions by global alignment.
4. Fetch AlphaFold monomer models and compute CYS SG pair geometry summaries.
5. Validate that the same scripts run on an alternate target (`tpx1`).

### Key outputs

- Summary report: `genes/SCHPO/pmp20/pmp20-bioinformatics/RESULTS.md`
- Sequence cysteine summary: `genes/SCHPO/pmp20/pmp20-bioinformatics/results/main/sequence/sequence_cysteine_summary.tsv`
- Target vs active-control mapping: `genes/SCHPO/pmp20/pmp20-bioinformatics/results/main/sequence/target_vs_active_alignment.tsv`
- AlphaFold download manifest: `genes/SCHPO/pmp20/pmp20-bioinformatics/results/main/structures/alphafold_manifest.tsv`
- Structure cysteine summary: `genes/SCHPO/pmp20/pmp20-bioinformatics/results/main/structure/structure_cys_summary.tsv`

### Main findings

- `pmp20` has one cysteine (C43) and no candidate resolving cysteine.
- Active controls show expected multi-cysteine topology with resolving-cysteine candidates.
- Active-control resolving positions do not map to cysteine in `pmp20`.
- AlphaFold monomer model for `pmp20` contains only one cysteine, so no Cys-Cys pair geometry is possible in-model.

### Curation impact

The bioinformatics case study was incorporated into the main review as a `file:` reference:

- `file:SCHPO/pmp20/pmp20-bioinformatics/RESULTS.md`

Updated review file:

- `genes/SCHPO/pmp20/pmp20-ai-review.yaml`

Validation status:

- `just validate SCHPO pmp20` passed (warnings only, no validation errors).

### Caveats

- AlphaFold was used as monomer structure context only; no multimer interface modeling was performed.
- Structural distance metrics are supportive context and not stand-alone activity evidence.

## Template For Future Cases

For each new case, add:
1. Case ID, gene, species, and curation question.
2. Workflow path and exact run commands.
3. Key result files (especially `RESULTS.md`).
4. Clear statement of how outcomes changed curation decisions.
5. Validation status after integrating results into `*-ai-review.yaml`.
