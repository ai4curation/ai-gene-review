---
title: "BIOINFORMATICS Case Studies"
maturity: SCOPING
tags: [PIPELINE]
---

# BIOINFORMATICS Case Studies

## Purpose

This document records concrete cases where custom bioinformatics analysis was used to resolve annotation uncertainty in `ai-gene-review`.

Each case links:
- biological question
- reproducible analysis workflow
- key outputs
- impact on curation decisions

## Hypothesis-Linked OpenScientist Workflow

Gene function assignments can be treated as focused hypotheses before they are
accepted, removed, or converted into suggested experiments. The current CLI path
is:

```bash
just gene-hypothesis-list <organism> <gene>
just gene-hypothesis-research <provider> <organism> <gene> --annotation-term-id <GO_ID> --as-function-hypothesis --dry-run
```

Hypothesis reports are written under:

```text
genes/<organism>/<gene>/<gene>-hypotheses/<hypothesis-slug>/<provider>.md
```

When the source review cites a local bioinformatics result such as
`file:<organism>/<gene>/<gene>-bioinformatics/RESULTS.md`, the hypothesis prompt
withholds that local analysis from OpenScientist. This keeps the run blinded so
OpenScientist can independently explore the hypothesis that gene `G` has
function `F`. After the run, compare the OpenScientist report against the local
`RESULTS.md` to see whether the independent search converged with, refined, or
contradicted the older analysis.

Use this distinction:

- **OpenScientist-only hypothesis search**: blinded exploration of whether gene
  `G` has function `F`, using seed review context but not local holdout
  bioinformatics results or prior curation rationales.
- **Bioinformatics workflow plus OpenScientist**: sequence, structure, domain,
  phylogeny, or localization claims where local computation is part of the
  post-run comparison and final evidence trail.

## Case Studies

| Case ID | Gene | Species | Question | Outcome |
|---|---|---|---|---|
| BIO-001 | pmp20 | SCHPO (*S. pombe*) | Does pmp20 have thioredoxin-dependent peroxidase activity? | Evidence supports loss of canonical thioredoxin-dependent peroxidase function |
| BIO-002 | Epe1 | SCHPO (*S. pombe*) | Does the JmjC domain support histone demethylase/oxidoreductase activity? | Bioinformatics and literature support treating Epe1 as a non-catalytic chromatin regulator |

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

## BIO-002: SCHPO/Epe1 (JmjC demethylase activity)

### Context

`Epe1` contains a JmjC-family domain, which can trigger automated histone
demethylase, dioxygenase, oxidoreductase, and metal-binding annotations. The
review instead treats Epe1 as a non-catalytic anti-silencing factor that acts in
heterochromatin regulation through Swi6/HP1-associated chromatin mechanisms.

### Curation question

Should JmjC-derived GO molecular-function annotations such as histone demethylase
activity be removed for `SCHPO/Epe1`?

### Existing workflow

- Analysis directory: `genes/SCHPO/Epe1/Epe1-bioinformatics`
- Summary report: `genes/SCHPO/Epe1/Epe1-bioinformatics/RESULTS.md`
- Review file: `genes/SCHPO/Epe1/Epe1-ai-review.yaml`

Hypothesis search candidates can be listed with:

```bash
just gene-hypothesis-list SCHPO Epe1
```

The histone-demethylase function assignment hypothesis can be staged with:

```bash
just gene-hypothesis-research openscientist SCHPO Epe1 \
  --annotation-term-id GO:0032452 \
  --as-function-hypothesis \
  --dry-run \
  -- --param use_hypotheses=true
```

Expected output path for a real run:

```text
genes/SCHPO/Epe1/Epe1-hypotheses/function-hypothesis-go-0032452/openscientist.md
```

### Current findings

- Epe1 is a JmjC-domain protein, but the accessible literature and local
  bioinformatics report support a pseudo-demethylase interpretation.
- Existing review decisions remove JmjC-derived catalytic activity annotations
  and retain chromatin/heterochromatin regulatory annotations.
- This case is the biological pilot for treating a function assignment as an
  explicit OpenScientist hypothesis.

### Caveats

- The Epe1 bioinformatics folder is older and less reusable than the pmp20
  workflow. Use `pmp20-bioinformatics` as the engineering template for new
  reproducible analyses.
- The OpenScientist report should be run blind to the existing local
  `RESULTS.md`; compare the report against the older bioinformatics result after
  generation.

## Template For Future Cases

For each new case, add:
1. Case ID, gene, species, and curation question.
2. Workflow path and exact run commands.
3. Key result files (especially `RESULTS.md`).
4. Clear statement of how outcomes changed curation decisions.
5. Validation status after integrating results into `*-ai-review.yaml`.
6. If applicable, the `gene-hypothesis-research` command and output path for the
   OpenScientist hypothesis report.
