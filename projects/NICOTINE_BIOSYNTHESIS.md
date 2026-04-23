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
| `NaMPO1` | Oxidation to the N-methyl-Delta1-pyrrolinium branch intermediate | Classical pathway and Cell minimal set | Sequence-backed candidate mapping |
| `NaUGT1` | Glycosylation branch that produces NG | New Cell 2026 step | Sequence-backed candidate mapping |
| `NaA622` | Ring-condensation branch point | Classical late-step nicotine pathway; retained in Cell model | Launch-ready |
| `NaBBL1`, `NaBBL2` | Late oxidation after condensation | Classical BBL family; `NaBBL2` used in Cell yeast reconstruction | Provisional accession mapping |
| `NaBGL1`, `NaBGL2` | Deglycosylation from NG to nicotine | New Cell 2026 step | BGLU18 candidate jobs launch-ready; older BGLU42 retained as comparator |
| `NaMATE1` | Vacuolar membrane metabolon transporter/export step | New Cell 2026 transport component; required for high yeast production | Sequence-backed candidate mapping |

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
uv run python projects/NICOTINE_BIOSYNTHESIS/launch_review_jobs.py --include-existing --dry-run
uv run python projects/NICOTINE_BIOSYNTHESIS/launch_review_jobs.py
uv run python projects/NICOTINE_BIOSYNTHESIS/launch_review_jobs.py --with-deep-research --deep-research-provider codex
```

Default behavior:

- Runs only rows marked `launch_ready`.
- Resolves paths from the repository root even when invoked outside the repo top level.
- Skips aliases that already have seeded review files unless `--include-existing` is passed.
- Fetches UniProt/GOA/stub review files with stable project aliases.
- Skips unresolved rows but reports them at the end.

## Current Branch Snapshot

This branch is already past pure scaffold stage:

- All 22 current `launch_ready` aliases in `review_jobs.csv` have now been fetched into `genes/NICAT/`.
- All 22 current launched NICAT aliases have now been advanced to `DRAFT` review state.
- The 2026-04-05 mapping dive converted `NaUGT1`, `NaMPO1`, `NaBGL2`, and `NaMATE1`
  from pure accession backlog into fetched sequence-backed candidate rows.
- The same review pass promotes `BGLU18_6` and `BGLU18_1` as the leading `beta-GD`
  anchors and demotes `BGLU42` to a lower-confidence historical comparator.
- `NaNAMNH` is now the main unresolved seed-core accession gap.
- `NaNUP` remains a tracked transport follow-up outside the minimal launch core.

## Accession-Mapping Policy

For several Cell-era names, public resources still expose generic paralog names rather than the
paper's `Na...` symbols. This project therefore uses two layers:

- **Canonical symbol layer** for the biology and project framing.
- **Launch job layer** for the current fetchable accession(s).

If a public accession mapping is ambiguous, review **all plausible paralogs early** rather than
pretending the ambiguity does not exist.

## Mapping Dive (2026-04-05)

A focused mapping pass used the Cell/bioRxiv tobacco locus IDs, the SGN tobacco 2017 proteome,
the SGN *N. attenuata* NIATv7 proteome, the UniProt `NICAT` proteome, and a spot remote BLAST
check for `NaMPO1`.

Current best candidates are:

- `NaMPO1` -> `AMO_3` / `A0A314KPU1`
  Tobacco `Nitab4.5_0000983g0060` (`NtMPO1`) maps strongly to *N. attenuata* primary amine
  oxidase `NIATv7_g14063`, which in UniProt cross-release space best matches `A0A314KPU1`.
- `NaMATE1` -> `DTX40_3` / `A0A314KVN4`
  Tobacco `Nitab4.5_0000884g0030` (`MATE1`) maps cleanly to `NIATv7_g09978`, then to UniProt
  `DTX40_3`.
- `NaUGT1` -> `UGT85A2_0` / `A0A2H4GSI3`
  Tobacco `Nitab4.5_0006222g0020` (`UGT1`) maps strongly to `NIATv7_g26396`, then to UniProt
  `UGT85A2_0`.
- `NaBGL1` -> `BGLU18_6` / `A0A1J6KFZ7`
  Tobacco `beta-GD1` (`Nitab4.5_0000884g0020`) maps best to `NIATv7_g57285`, then to UniProt
  `BGLU18_6`.
- `NaBGL2` -> `BGLU18_1` / `A0A314KWB2`
  Tobacco `beta-GD2` (`Nitab4.5_0000031g0400`) maps best to `NIATv7_g09974`, then to UniProt
  `BGLU18_1`.

Important caveats:

- These are **sequence-backed cross-release mappings**, not official symbol normalizations from
  the Cell paper into current public `NICAT` nomenclature.
- The already-launched `NaBGL1_candidate_BGLU42` row should now be treated as a weaker
  historical comparator, not the best orthology anchor for the paper's `beta-GD` genes.
- `NaNAMNH` remains unresolved: the Cell paper clearly assigns the function, but a stable public
  `NICAT` accession still does not surface cleanly from current annotation resources.

## Immediate Worklist

- [x] Choose a single seed species.
- [x] Add the Cell 2026 paper to the project framing.
- [x] Create canonical pathway list and job queue.
- [x] Launch first-pass review jobs for all current `launch_ready` rows.
- [x] Curate the PMT paralog pair beyond seeded stubs.
- [x] Convert `NaUGT1`, `NaMPO1`, `NaBGL2`, and `NaMATE1` from pure backlog rows into
  sequence-backed candidate jobs.
- [x] Decide that the new `BGLU18` candidates replace `BGLU42` as the primary
  deglycosylase review anchors, while retaining `BGLU42` as a comparator.
- [x] Advance all currently launched NICAT aliases beyond `INITIALIZED`.
- [ ] Resolve a stable public accession for `NaNAMNH`.
- [ ] Revisit whether `NaNUP` belongs in the core transport batch after the minimal metabolon is reviewed.

## Sources

1. Chang L, Xu Z, Deng P, Zhang N, He T, Liu X, He W, Zheng A, Hu W, Pan M, Li W, Halitschke R, Li R, Fan M, Baldwin IT, Zhang Y, Li D. 2026. **Complete biosynthesis of nicotine**. *Cell*. Chris-provided source: `https://www.cell.com/cell/fulltext/S0092-8674(26)00335-1`
   Accessible abstract mirror used during scaffolding: `https://www.lifescience.net/entries/860228/complete-biosynthesis-of-nicotine/`
2. Schwabe BTW, Angstman IM, Vollheyde K, Ingold Z, Li J, Stankevich KS, Spicer CD, Fascione MA, Grogan G, Geu-Flores F, Lichman BR. 2025. **Nicotine biosynthesis completed by cryptic activating glucosylation**. *bioRxiv*. DOI: `10.64898/2025.12.04.692101`
   Full preprint consulted here: `https://www.biorxiv.org/content/10.64898/2025.12.04.692101v1`
   Lab pages confirming the preprint and its emphasis on cryptic glucosylation: `https://lichmanlab.weebly.com/research-articles.html` and `https://lichmanlab.weebly.com/news.html`
3. Xu S, Brockmoller T, Navarro-Quezada A, et al. 2017. **Wild tobacco genomes reveal the evolution of nicotine biosynthesis**. *PNAS*.
   `https://pmc.ncbi.nlm.nih.gov/articles/PMC5468653/`
4. Zhang et al. 2025. **DNA methylation valley as a distinguishing feature occurs in root-specific expressed nicotine-related genes in Nicotiana attenuata**. *Frontiers in Plant Science*.
   `https://pmc.ncbi.nlm.nih.gov/articles/PMC12361153/`
5. Sol Genomics Network FTP. *Nicotiana tabacum* Edwards et al. 2017 proteome.
   `https://ftp.solgenomics.net/genomes/Nicotiana_tabacum/edwards_et_al_2017/annotation/Nitab-v4.5_proteins_Edwards2017.fasta`
6. Sol Genomics Network FTP. *Nicotiana attenuata* genome release v2, annotation v5 proteome.
   `https://ftp.solgenomics.net/genomes/Nicotiana_attenuata/NIATTr2.an5.aa.fa`
7. UniProtKB stream for *Nicotiana attenuata* proteins.
   `https://rest.uniprot.org/uniprotkb/stream?compressed=false&format=fasta&query=organism_name:%22Nicotiana%20attenuata%22`
