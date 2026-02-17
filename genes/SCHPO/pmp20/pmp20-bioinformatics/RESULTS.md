# RESULTS: SCHPO/pmp20 thioredoxin-dependent peroxidase activity assessment

## Objective

Assess whether `pmp20` from *Schizosaccharomyces pombe* has plausible thioredoxin-dependent peroxidase activity using reproducible bioinformatics analyses (control-calibrated sequence and structure checks).

## Provenance

Workflow run from:

- `genes/SCHPO/pmp20/pmp20-bioinformatics`

Command executed:

```bash
just all
```

Generated run outputs:

- Main analysis (`pmp20` as target): `results/main/`
- Script-validation run (`tpx1` as target): `results/test_tpx1/`

Primary literature/context source used for expected phenotype:

- `publications/PMID_20356456.md` (reports no thioredoxin-dependent peroxidase activity for PMP20 and weak chaperone activity)

## Checklist

- [x] Confirmed scripts do not use hardcoded gene-specific inputs/outputs (all scripts take CLI paths and table-driven inputs).
- [x] Scripts tested on at least one other input (`inputs/proteins-test-tpx1.tsv` with `tpx1` as alternate target).
- [x] Analyses completed as expected (`just all` completed without errors).
- [x] Direct script results are present in the analysis folder (`results/main/` and `results/test_tpx1/`).
- [x] Summary includes provenance and justification with explicit file-backed evidence.

## Key Results

### 1) Control set assembly

`results/main/protein_summary.tsv` captured 4 proteins:

- Target: `pmp20_schpo` (`O14313`)
- Active controls: `tpx1_schpo` (`O74887`), `prdx5_human` (`P30044`), `prx5_o43099` (`O43099`)

All 4 AlphaFold models downloaded successfully (`results/main/structures/alphafold_manifest.tsv`).

### 2) Sequence/catalytic-site evidence

From `results/main/sequence/sequence_cysteine_summary.tsv`:

- `pmp20`: 156 aa, **1 cysteine** total (`C43`), act-site annotated at 43, **no candidate resolving cysteine**.
- Active controls all have >=2 cysteines and a candidate resolving cysteine (e.g., `tpx1`: C48/C169; `prdx5_human`: includes C100/C204).

Peroxidatic-window comparison (11 aa anchors):

- `pmp20`: `AFTPPCSSQVP`
- `tpx1`: `DFTFVCPTEIV`
- `prdx5_human`: `AFTPGCSKTHL`
- `prx5_o43099`: `AFTPVCSARHV`

Interpretation: `pmp20` retains a peroxidatic-site-like local motif region but lacks a second cysteine needed for canonical thioredoxin-dependent peroxiredoxin cycling.

### 3) Alignment-to-active-controls evidence

From `results/main/sequence/target_vs_active_alignment.tsv`:

- Active-control peroxidatic positions map to `pmp20` residue `C43`.
- Active-control resolving positions do **not** map to cysteine in `pmp20`:
  - vs `tpx1` resolving C169 -> gap
  - vs `prdx5_human` resolving C204 -> `I146`
  - vs `prx5_o43099` resolving C31 -> `V22`

Interpretation: comparative mapping supports loss of resolving-cysteine equivalence in `pmp20`.

### 4) Structure-level cysteine geometry

From `results/main/structure/structure_cys_summary.tsv` and `structure_cys_pair_distances.tsv`:

- `pmp20`: structure has only one cysteine SG atom (C43), so no Cys-Cys pair geometry exists.
- Active controls contain cysteine pairs in structure models (`tpx1`, `prdx5_human`, `prx5_o43099`).

Important caveat:

- AlphaFold models are monomeric predictions; inter-subunit catalytic disulfides expected in some peroxiredoxins are not guaranteed to appear as close SG-SG distances in these single-chain models. Therefore, distance thresholds are supportive context, not stand-alone functional proof.

## Validation Run (Script Generality)

`results/test_tpx1/` confirms scripts run on alternate target input with the same pipeline. `tpx1` is correctly reported with two cysteines and a candidate resolving cysteine (`results/test_tpx1/sequence/sequence_cysteine_summary.tsv`).

## Conclusion

Based on this bioinformatics workflow, `pmp20` does not show sequence/structural features consistent with canonical thioredoxin-dependent peroxidase activity, primarily because no resolving cysteine is detected by direct sequence inventory or by alignment to active controls.

This computational result is consistent with cached experimental literature in `publications/PMID_20356456.md`.
