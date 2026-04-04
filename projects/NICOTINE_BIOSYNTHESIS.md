---
species: [NICAT]
sidecars:
  genes: NICOTINE_BIOSYNTHESIS/genes.csv
  review_jobs: NICOTINE_BIOSYNTHESIS/review_jobs.csv
---
# Nicotine Biosynthesis Project

> **Editor Brief (2026-04-04):**
> Seed this project in *Nicotiana attenuata* (`NICAT`), not *N. tabacum*. The April 2, 2026
> Cell paper from Chris directly completes nicotine biosynthesis in *N. attenuata*, identifies
> the newly required glycosylation and deglycosylation steps, and provides a minimal
> heterologous reconstruction path. This species also has strong prior pathway/evolution
> literature and a well-used ecological/genomic model system in the repo's target domain.
> The project starts from a conservative core pathway set, keeps regulators out of the seed
> enzyme list, and explicitly separates canonical literature genes from accession-backed
> review jobs where current public annotation still lags the paper nomenclature.

## Goal

Review the core genes required to synthesize nicotine in one defensible Nicotiana species,
starting from a pathway-focused seed set that can be expanded only when the literature clearly
demands it.

This project owns three things:

1. The canonical single-species nicotine pathway gene list.
2. The review-job table used to fetch/create gene review stubs.
3. The accession-resolution backlog for Cell-era names that are not yet normalized in public
   annotation resources.

## Why *Nicotiana attenuata*

*N. attenuata* is the best seed species because it now has:

- A direct "complete biosynthesis of nicotine" paper in the target species.
- Older pathway/evolution work already centered on *N. attenuata* rather than only cultivated
  tobacco.
- Root-expression and ecology literature that helps distinguish core biosynthetic genes from
  housekeeping paralogs and pathway regulators.

I am **not** seeding this in *N. tabacum* even though tobacco is the familiar nicotine species,
because the new Cell paper's mechanistic closure is in *N. attenuata*, and forcing a
cross-species translation at project start would add avoidable paralog/orthology noise.

## Selection Rules

Include a gene in the seed set only if at least one of these is true:

- The Cell 2026 paper directly assigns a catalytic or transport role in nicotine biosynthesis.
- Earlier *N. attenuata* pathway literature already places it in the root-specific nicotine
  branch.
- A paralog-disambiguation review is required to decide which duplicated copy is the real
  pathway member.

Exclude from the initial seed set:

- Pure regulators unless they are needed later for pathway-control follow-up.
- General wound/jasmonate response genes that are upstream of many defenses.
- Transport or storage genes with only indirect nicotine associations unless the literature
  puts them into the biosynthetic/metabolon core.

## Core Pathway Seed Set

### Included now

| Canonical gene | Role in pathway | Why included | Current launch state |
|---|---|---|---|
| `NaAO2` | Pyridine branch entry from aspartate | Prior *N. attenuata* pathway literature; retained after Cell update | Provisional accession mapping |
| `NaNAMNH` | NAMN hydrolase supplying nicotinic acid | New Cell 2026 step | Pending accession mapping |
| `NaQPT2` | Pyridine branch quinolinate phosphoribosyltransferase | Prior root-specific pathway literature; still relevant after Cell update | Provisional accession mapping |
| `NaODC1`, `NaODC2` | Pyrrolidine precursor supply | Prior pathway literature and root-specific expression | Provisional accession mapping |
| `NaPMT1.1`, `NaPMT1.2` | N-methylputrescine formation | Core classical nicotine pathway; `NaPMT1` used in Cell yeast reconstruction | Launch-ready |
| `NaMPO1` | Oxidation to the N-methyl-Delta1-pyrrolinium branch intermediate | Classical pathway and Cell minimal set | Pending accession mapping |
| `NaUGT1` | Glycosylation branch that produces NG | New Cell 2026 step | Pending accession mapping |
| `NaA622` | Ring-condensation branch point | Classical late-step nicotine pathway; retained in Cell model | Launch-ready |
| `NaBBL1`, `NaBBL2` | Late oxidation after condensation | Classical BBL family; `NaBBL2` used in Cell yeast reconstruction | Provisional accession mapping |
| `NaBGL1`, `NaBGL2` | Deglycosylation from NG to nicotine | New Cell 2026 step | One candidate launch-ready, one pending |
| `NaMATE1` | Vacuolar membrane metabolon transporter/export step | New Cell 2026 transport component; required for high yeast production | Pending accession mapping |

### Keep as follow-up, not seed-core

| Gene | Why not in seed-core |
|---|---|
| `NaNUP` | Transport-associated and likely important, but not part of the minimal Cell metabolon. Track as follow-up once the catalytic core is underway. |
| `NaERF1-like`, `NaMYC2` | Important regulators, but this project should first settle the enzyme/transport core before broadening into control logic. |
| `NaAO1`, `NaQPT1`, `NaQS` | Useful housekeeping/parallel-pathway comparators, but not part of the initial core nicotine review list. |

## Cell Paper Impact

The incoming paper materially changes the project framing:

- It strengthens the species choice in favor of *N. attenuata*.
- It upgrades glycosylation and deglycosylation from side chemistry to pathway-core steps.
- It makes `NaMATE1` a core transport gene rather than a peripheral transport annotation.
- It argues that the minimal heterologous production set is:
  `NaODC`, `NaPMT1`, `NaMPO`, `NaUGT1`, `NaA622`, `NaBBL2`, `NaBGL1`, and `NaMATE1`.
- It also supports keeping the upstream pyridine branch (`NaAO2`, `NaNAMNH`, `NaQPT2`) in
  scope for a complete species review rather than only reviewing the minimal yeast set.

## Review Orchestration

Two sidecars drive execution:

- `projects/NICOTINE_BIOSYNTHESIS/genes.csv`
  Canonical literature-facing pathway list and inclusion rationale.
- `projects/NICOTINE_BIOSYNTHESIS/review_jobs.csv`
  Accession-backed job queue plus explicit pending rows where public annotation still trails
  the literature.

Launch jobs with:

```bash
uv run python projects/NICOTINE_BIOSYNTHESIS/launch_review_jobs.py --dry-run
uv run python projects/NICOTINE_BIOSYNTHESIS/launch_review_jobs.py
uv run python projects/NICOTINE_BIOSYNTHESIS/launch_review_jobs.py --with-deep-research --deep-research-provider codex
```

Default behavior:

- Runs only rows marked `launch_ready`.
- Fetches UniProt/GOA/stub review files with stable project aliases.
- Skips unresolved rows but reports them at the end.

## Accession-Mapping Policy

For several Cell-era names, public resources still expose generic paralog names rather than the
paper's `Na...` symbols. This project therefore uses two layers:

- **Canonical symbol layer** for the biology and project framing.
- **Launch job layer** for the current fetchable accession(s).

If a public accession mapping is ambiguous, review **all plausible paralogs early** rather than
pretending the ambiguity does not exist.

## Immediate Worklist

- [x] Choose a single seed species.
- [x] Add the Cell 2026 paper to the project framing.
- [x] Create canonical pathway list and job queue.
- [ ] Resolve public accessions for `NaNAMNH`, `NaUGT1`, `NaMPO1`, `NaBGL2`, and `NaMATE1`.
- [ ] Launch first-pass review jobs for all `launch_ready` rows.
- [ ] Revisit whether `NaNUP` belongs in the core transport batch after the minimal metabolon is reviewed.

## Sources

1. Chang L, Xu Z, Deng P, Zhang N, He T, Liu X, He W, Zheng A, Hu W, Pan M, Li W, Halitschke R, Li R, Fan M, Baldwin IT, Zhang Y, Li D. 2026. **Complete biosynthesis of nicotine**. *Cell*. Chris-provided source: `https://www.cell.com/cell/fulltext/S0092-8674(26)00335-1`
   Accessible abstract mirror used during scaffolding: `https://www.lifescience.net/entries/860228/complete-biosynthesis-of-nicotine/`
2. Xu S, Brockmoller T, Navarro-Quezada A, et al. 2017. **Wild tobacco genomes reveal the evolution of nicotine biosynthesis**. *PNAS*.
   `https://pmc.ncbi.nlm.nih.gov/articles/PMC5468653/`
3. Zhang et al. 2025. **DNA methylation valley as a distinguishing feature occurs in root-specific expressed nicotine-related genes in Nicotiana attenuata**. *Frontiers in Plant Science*.
   `https://pmc.ncbi.nlm.nih.gov/articles/PMC12361153/`

