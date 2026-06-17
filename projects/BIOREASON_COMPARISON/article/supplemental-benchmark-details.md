---
title: "Supplemental benchmark and source-availability details for the BioReason-Pro comparison"
autolink_gene_symbols: false
---

# Supplemental benchmark and source-availability details

This supplement documents analyses that are useful for auditability but are not part of the main paper's single BioReason-Pro benchmark story. The main manuscript uses **ARGO139** for all non-VDCL BioReason-Pro results. The views below explain why earlier drafts used multiple denominators and preserve those results for reproducibility.

## S1. Cohort accounting

The main BioReason-Pro benchmark is ARGO139, a fixed 139-gene set listed in `../genes.csv`. ARGO139 is used for both RL narrative review and SFT GO-term review.

**Table S1.** Cohorts emitted by `write_benchmark_sidecars.py`.

| Cohort | Genes | Predictions | Role |
|---|---:|---:|---|
| `argo139_rl_narrative` | 139 | - | Main RL narrative benchmark |
| `argo139_sft_terms` | 139 | 10,697 | Main SFT term benchmark |
| `argo139_sft_terms_hf_catalogue` | 95 | 955 | Cleaner ARGO139 SFT source subset |
| `argo139_sft_terms_web_export` | 44 | 9,742 | ARGO139 genes absent from HF; web source includes ancestor hierarchy |
| `supplement_sft_narrative_hf` | 45 | - | SFT narrative cross-check |
| `supplement_sft_terms_hf_catalogue_140` | 140 | 1,292 | Full HF catalogue view |
| `supplement_sft_terms_union_184` | 184 | 11,034 | ARGO139 plus 45 HF-only genes |
| `supplement_gogpt_overlap_300` | 300 | 8,910 | Separate GO-GPT overlap audit |

The key availability issue is simple: the HuggingFace `wanglab/protein_catalogue` SFT download contained 95/139 ARGO139 genes. The remaining 44 ARGO139 genes were not present in that download, so the main paper fills them from BioReason-Pro SFT web exports. The web exports include many GO ancestor terms, so the source label is retained throughout.

## S2. Supplemental SFT term views

**Table S2.** ARGO139 SFT assessment distribution, repeated from the main paper.

| Source | Genes | Terms | CNN | NPI | COR | LSP | REP | UNC |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| HF catalogue | 95 | 955 | 645 (67.5%) | 101 (10.6%) | 52 (5.4%) | 37 (3.9%) | 21 (2.2%) | 99 (10.4%) |
| Web export | 44 | 9,742 | 2,321 (23.8%) | 42 (0.4%) | 7 (0.1%) | 388 (4.0%) | 1 (0.0%) | 6,983 (71.7%) |
| ARGO139 total | 139 | 10,697 | 2,966 (27.7%) | 143 (1.3%) | 59 (0.6%) | 425 (4.0%) | 22 (0.2%) | 7,082 (66.2%) |

**Table S3.** Terms per gene in the ARGO139 SFT sources.

| Source | Mean terms/gene | Median terms/gene | Max terms/gene |
|---|---:|---:|---:|
| ARGO139 total | 77.0 | 12.0 | 598 |
| HF catalogue | 10.1 | 7.0 | 38 |
| Web export | 221.4 | 212.5 | 598 |

The older 140-gene HF view is still useful because it is the cleanest single-source view, but it is no longer the main benchmark because 45 of those genes are outside ARGO139.

**Table S4.** Supplemental full HF catalogue view: 1,292 terms across 140 genes.

| Assessment | Count | % |
|---|---:|---:|
| CNN | 862 | 66.7 |
| NPI | 149 | 11.5 |
| UNC | 149 | 11.5 |
| COR | 58 | 4.5 |
| LSP | 49 | 3.8 |
| REP | 25 | 1.9 |

The older 184-gene union is the broadest source-availability view, but it combines ARGO139 with 45 HF-only genes and is therefore not a paired benchmark.

**Table S5.** Supplemental 184-gene union: 11,034 terms across ARGO139 plus 45 HF-only genes.

| Assessment | Count | % |
|---|---:|---:|
| CNN | 3,183 | 28.8 |
| NPI | 191 | 1.7 |
| UNC | 7,132 | 64.6 |
| COR | 65 | 0.6 |
| LSP | 437 | 4.0 |
| REP | 26 | 0.2 |

## S3. SFT narrative cross-check

The HuggingFace SFT narrative sample contains 45 proteins, 44 of which have parseable 1-5 correctness/completeness scores. It is not paired to ARGO139 and is not used as a main result. It remains a useful cross-check: SFT narrative scores are lower than RL (correctness 2.9/5 vs. 3.7/5; completeness 2.7/5 vs. 2.9/5), and 7/45 SFT outputs contained fabricated "UniProt Summary" prose for proteins that UniProt describes only as uncharacterized.

## S4. GO-GPT overlap audit

The main paper removes the GO-GPT section because it is a separate 300-gene audit of the upstream GO-GPT predictor, not a paired ARGO139 BioReason-Pro result. The audit remains useful for showing how much apparent agreement changes when the reference set moves from raw GOA to AIGR core biology.

**Table S6.** GO-GPT prediction overlap at three reference levels (300 genes).

| Reference level | Terms in reference | Predictions overlapping | % of 8,910 predictions |
|---|---:|---:|---:|
| Raw GOA | 2,967 | 1,046 | 11.7 |
| Post-AIGR-review | 2,913 | 971 | 10.9 |
| AIGR core functions only | 933 | 210 | 2.4 |

![GO-GPT prediction overlap at three reference levels.](figures/three_level_overlap.png)

GO-GPT emitted 8,910 predictions across 300 genes (mean 29.7 per gene). Raw GOA agreement was 11.7%; agreement with AIGR core functions was only 2.4%. This is a useful illustration of the CAFA-style scoring gap, but it is not used as a main BioReason-Pro benchmark result.

## S5. Reproducibility files

- `../genes.csv`: ARGO139 member list.
- `../argo139-species-counts.csv`: ARGO139 species distribution.
- `../argo139-curation-context-counts.csv`: ARGO139 curation-context summary.
- `../benchmark-cohorts.csv`: cohort-level provenance and sizes.
- `../benchmark-genes.csv`: gene-level benchmark/source provenance.
- `../notebooks/02_prediction_assessments.ipynb`: executable SFT term-assessment notebook.
