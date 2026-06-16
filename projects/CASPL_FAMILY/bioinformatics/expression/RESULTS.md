---
title: "Poplar CASPL expression analysis — RESULTS (EBI Expression Atlas)"
---

# Poplar CASPL expression analysis — RESULTS (EBI Expression Atlas)

After the PlantGenIE route proved session-gated (see NOTES.md), the analysis was
completed instead from **EBI Expression Atlas**, whose processed matrices are openly
downloadable and keyed by EnsemblPlants P. trichocarpa IDs (`POPTR_<chr>G<num>v3`),
which map 1:1 from the UniProt `Potri.*` IDs. Reproduce with:

```bash
cd projects/CASPL_FAMILY/bioinformatics/expression
uv run ebi_atlas_analysis.py     # downloads EBI data, writes results/*.tsv
```

12 of the 20 poplar CASPLs (those with a current `Potri.*` model ID) were analyzed.
Two datasets: **E-MTAB-5540** (cold/drought/heat/salt vs control in root, stem xylem,
vascular leaf) and **E-GEOD-81077** (baseline TPM across leaf, phloem, primary root,
shoot apex and xylem cell types).

## Headline findings (real data, hypothesis tests)

### 1. Suberization / endodermis hypothesis (CASPL1B/1D clade) — SUPPORTED
**CASPL1B1 is overwhelmingly root-specific: median 120 TPM in primary root vs ~0 in leaf,
shoot apex, xylem and ~0.6 in phloem.** This is exactly the pattern expected if the poplar
1B clade mirrors the Arabidopsis CASPL1B/1D suberized-endodermis role (the root endodermis
is where suberization occurs). CASPL4D1 is also primary-root–enriched (low overall).
This is the strongest single confirmation of the orthology-based functional transfer.

### 2. Cold / abiotic-stress hypothesis (CASPL4C clade) — SUPPORTED (broader than cold)
**CASPL4C1 is the most stress-responsive CASPL (13 significant contrasts, |log2FC|≥1, p<0.05).**
It is strongly **induced by drought** (stem xylem log2FC **+3.0, p=2e-14**), **heat** (+2.1),
and **salt** (+1.9 root), and **repressed by cold in vascular leaf** (−2.3, p=4e-6; prolonged
−1.8). Its baseline expression is low everywhere (≤2 TPM), consistent with a stress-inducible
gene. CASPL4C2 is salt/heat-induced; CASPL4D1 is drought-induced in xylem (+5.1). So the 4C
clade is genuinely abiotic-stress-coupled in poplar, confirming and broadening the
cold-tolerance role characterized for Arabidopsis AtCASPL4C1 (note: cold direction differs by
tissue — repressed in leaf rather than induced).

### 3. Wood / vascular biology
Several CASPLs are vascular/wood-cell specific at baseline, consistent with the family's role
in poplar wood: **CASPL1F2** peaks in xylem vessels (34 TPM), **CASPL2B2** in xylem fiber cells
(39 TPM), and **CASPL3A1 / CASPL3A2** in phloem (43 / 55 TPM). CASPL2A2 and CASPL2C1 are
leaf-enriched. CASPL1C1 was effectively not expressed (≈0 across all tissues in this atlas).

## Output files
- `results/caspl_stress_log2fc.tsv` — every CASPL × stress-contrast log2FC, p-value, significance.
- `results/caspl_stress_significant.tsv` — significant hits only (|log2FC|≥1, p<0.05).
- `results/caspl_baseline_tpm.tsv` — median TPM per tissue + peak tissue.

## Caveats
- Only the 12 CASPLs with current `Potri.*` IDs were tested; the 8 legacy-`POPTRDRAFT_`-only
  genes need v2→v3 mapping (see NOTES.md / gene_ids.tsv).
- These are RNA-level expression observations (tissue specificity, stress response), suitable as
  IEP-type supporting evidence — they corroborate functional hypotheses but were **not** used to
  add experimental molecular-function GO terms to the reviews.
- Baseline TPM cells are EBI quantile summaries (min,q1,median,q3,max); the median is used.
