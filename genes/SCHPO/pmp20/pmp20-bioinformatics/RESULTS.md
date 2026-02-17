# RESULTS: SCHPO/pmp20 thioredoxin-dependent peroxidase activity assessment

## Objective

Assess whether `pmp20` from *Schizosaccharomyces pombe* has plausible thioredoxin-dependent peroxidase activity using reproducible bioinformatics analyses.

## Provenance

Workflow run from:

- `genes/SCHPO/pmp20/pmp20-bioinformatics`

Commands executed:

```bash
just all
just main-extra
uv run scripts/analyze_prx5_phylogeny.py --proteins-json results/main/phylogeny/prx5_proteins.json --target-id ahp1_p38013 --neighbor-count 8 --output-dir results/main/phylogeny_test_ahp1
uv run scripts/analyze_prx5_dimer_template.py --proteins-json results/test_tpx1/proteins.json --target-id tpx1_schpo --template-id prx5_o43099 --template-pdb-id 5J9B --output-dir results/test_tpx1/dimer_tpx1
```

Generated run outputs:

- Main analysis (`pmp20` as target): `results/main/`
- Alternate target/script-validation run (`tpx1`): `results/test_tpx1/`

Primary literature/context source used for expected phenotype:

- `publications/PMID_20356456.md` (reports no thioredoxin-dependent peroxidase activity for PMP20 and weak chaperone activity)

## Checklist

- [x] Confirmed scripts do not use hardcoded gene-specific inputs/outputs (all scripts take CLI paths and table-driven inputs).
- [x] Scripts tested on at least one other input/target (`inputs/proteins-test-tpx1.tsv`; alternate phylogeny target `ahp1_p38013`; alternate dimer target `tpx1_schpo`).
- [x] Analyses completed as expected (`just all` and `just main-extra` completed without errors).
- [x] Direct script results are present in the analysis folder.
- [x] Summary includes provenance and justification with explicit file-backed evidence.

## Key Results

### 1) Control set assembly

`results/main/protein_summary.tsv` captured 4 proteins:

- Target: `pmp20_schpo` (`O14313`)
- Active controls: `tpx1_schpo` (`O74887`), `prdx5_human` (`P30044`), `prx5_o43099` (`O43099`)

All 4 AlphaFold models downloaded successfully (`results/main/structures/alphafold_manifest.tsv`).

### 2) Sequence/catalytic-site evidence (target + controls)

From `results/main/sequence/sequence_cysteine_summary.tsv`:

- `pmp20`: 156 aa, **1 cysteine** total (`C43`), act-site annotated at 43, **no candidate resolving cysteine**.
- Active controls have >=2 cysteines and a candidate resolving cysteine (e.g., `tpx1`: C48/C169; `prdx5_human`: C100/C204).

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

### 4) AlphaFold monomer cysteine geometry (target + controls)

From `results/main/structure/structure_cys_summary.tsv` and `structure_cys_pair_distances.tsv`:

- `pmp20`: model has only one cysteine SG atom (C43), so no Cys-Cys pair geometry is possible in the monomer.
- Active controls contain cysteine pairs in structure models (`tpx1`, `prdx5_human`, `prx5_o43099`).

### 5) Prx5 homolog panel phylogeny and catalytic-state mapping

From `results/main/phylogeny/`:

- Panel size: 27 reviewed eukaryotic Prx5-like proteins (`prx5_panel.tsv`).
- Catalytic-state counts (`prx5_phylogeny_report.json`):
  - `peroxidatic_plus_resolving`: 23
  - `peroxidatic_only`: 4
- `pmp20` class: `peroxidatic_only` (`prx5_catalytic_state.tsv`).
- In top-12 nearest sequence neighbors of `pmp20`, 11 are `peroxidatic_plus_resolving` (`pmp20_neighbor_context.tsv`).
- Neighbor resolving sites align to non-cysteine residues in `pmp20` (commonly `V22`, `V67`, `I146`).

Interpretation: within the Prx5-like panel, `pmp20` is atypical because most homologs retain both peroxidatic and resolving cysteine architecture.

### 6) Template-based dimer interface analysis

Using experimental dimer template `O43099` / PDB `5J9B`:

- Distances in template (`results/main/dimer/dimer_template_sg_distances.tsv`) show cross-chain C(P)-C(R) proximity consistent with disulfide-capable geometry:
  - `A:61` to `B:31` = 2.036 A
  - `A:31` to `B:61` = 2.042 A
- Mapping template catalytic pair onto `pmp20` (`dimer_template_mapping_summary.tsv`):
  - template C(P) position 61 -> `pmp20` `C43`
  - template C(R) position 31 -> `pmp20` `V22`
  - `target_supports_template_like_cp_cr_pair = no`

Interpretation: even where Prx5 dimer templates show plausible intersubunit C(P)-C(R) geometry, `pmp20` lacks a cysteine at the mapped resolving position and cannot support an equivalent pair.

## Validation Run (Script Generality)

- `results/test_tpx1/` confirms baseline pipeline works with `tpx1` as alternate target.
- `results/main/phylogeny_test_ahp1/` confirms phylogeny script works with a non-`pmp20` target ID (`ahp1_p38013`).
- `results/test_tpx1/dimer_tpx1/` confirms dimer-template script runs on alternate target (`tpx1_schpo`).

## Conclusion

Across sequence features, control alignments, Prx5 homolog-panel mapping, and template-based dimer interface mapping, `pmp20` does not show the resolving-cysteine architecture required for canonical thioredoxin-dependent peroxidase cycling.

This computational result is consistent with cached experimental literature in `publications/PMID_20356456.md`.
