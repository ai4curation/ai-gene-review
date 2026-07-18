"""Generate the BioReason-Pro stats notebooks with nbformat.

Run with:  uv run python build_notebooks.py
Then execute:  uv run jupyter nbconvert --to notebook --execute --inplace *.ipynb

Keeping the notebook source in a builder script makes the cell contents easy to
review in a normal diff (ipynb JSON is noisy) and guarantees the two notebooks
stay in sync with the shared ``bioreason_stats`` module.
"""
from __future__ import annotations

import nbformat as nbf
from nbformat.v4 import new_code_cell, new_markdown_cell, new_notebook


def md(src: str):
    return new_markdown_cell(src.strip("\n"))


def code(src: str):
    return new_code_cell(src.strip("\n"))


# --------------------------------------------------------------------------
# Notebook 1: narrative correctness / completeness scores (Tables 1 & 2)
# --------------------------------------------------------------------------
nb1 = new_notebook(cells=[
    md(r"""
# BioReason-Pro narrative scores — summary statistics

This notebook recomputes, **from the committed per-gene review files**, the
narrative-evaluation numbers quoted in `projects/BIOREASON_COMPARISON.md` and the
manuscript. ARGO139 is the collected RL cohort; policy exclusions are removed from
the model-performance denominator and retained in the quality audit:

- overall mean **Correctness** and **Completeness**
- Pearson and Spearman association between the independently defined axes
- input-quality and local-reference-status strata
- **Table 1** — score distribution
- **Table 2** — per-organism means
- top performers (5/5 correctness) and critical failures (1/5)
- a regenerated `per_organism_scores.png` figure

Each score is parsed directly from the `- **Correctness**: N/5` /
`- **Completeness**: N/5` lines in
`genes/<species>/<gene>/<gene>-bioreason-{rl,sft}-review.md`. Nothing is
hard-coded; re-running after adding/editing reviews updates every table.
"""),
    code(r"""
import sys
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path.cwd()))
import bioreason_stats as bs

ROOT = bs.find_repo_root()
print("repo root:", ROOT)

all_rl = bs.parse_narrative_reviews("rl", ROOT, include_excluded=True)
rl = bs.parse_narrative_reviews("rl", ROOT)
sft = bs.parse_narrative_reviews("sft", ROOT)
print(f"RL collected reviews parsed: {len(all_rl)}")
print(f"RL performance reviews:      {len(rl)}")
print(f"RL policy exclusions:        {len(rl.attrs['excluded'])}")
for row in rl.attrs["excluded"]:
    print(f"  excluded: {row['species']}/{row['gene']} ({row['exclusion_reason']})")
print(f"SFT reviews parsed: {len(sft)} (skipped: {len(sft.attrs['skipped'])})")
if sft.attrs["skipped"]:
    print("  skipped SFT files (no parseable score line):")
    for p in sft.attrs["skipped"]:
        print("   ", p)
rl.head()
"""),
md("## Overall means and axis association\n\nAll values are computed on the policy-defined performance denominator."),
    code(r"""
def summarise(df, label):
    return dict(
        set=label,
        n=len(df),
        correctness=round(df.correctness.mean(), 2),
        completeness=round(df.completeness.mean(), 2),
    )

overall = pd.DataFrame([summarise(rl, "RL"), summarise(sft, "SFT")])
print(overall.to_string(index=False))
print("\nRL axis association:")
print(f"  Pearson:  {rl.correctness.corr(rl.completeness, method='pearson'):.3f}")
print(f"  Spearman: {rl.correctness.rank().corr(rl.completeness.rank()):.3f}")
"""),
    md("## Input and reference quality strata"),
    code(r"""
print("Input quality in the collected cohort:")
print(all_rl.input_quality.value_counts().to_string())
print("\nLocal AIGR reference status:")
print(all_rl.reference_status.value_counts().to_string())

strata = (
    rl.groupby("input_quality")
      .agg(n=("gene", "size"),
           correctness=("correctness", "mean"),
           completeness=("completeness", "mean"))
      .round(2)
)
print("\nPerformance scores by input-quality stratum:")
print(strata.to_string())
"""),
    md("## Table 1 — RL score distribution (policy-defined performance set)"),
    code(r"""
def distribution(df):
    out = pd.DataFrame(index=[5, 4, 3, 2, 1])
    for axis in ("correctness", "completeness"):
        counts = df[axis].value_counts().reindex([5, 4, 3, 2, 1], fill_value=0)
        pct = (100 * counts / len(df)).round(0).astype(int)
        out[axis] = [f"{c} ({p}%)" for c, p in zip(counts, pct)]
    out.index.name = "score"
    return out

dist = distribution(rl)
print(dist.to_string())
"""),
    md("## Table 2 — per-organism means\n\nSorted by mean correctness, descending. These are descriptive selected-case summaries, not estimates of organism-level performance; case mix and input quality are confounders."),
    code(r"""
per_org = (
    rl.groupby("species")
      .agg(n=("gene", "size"),
           correctness=("correctness", "mean"),
           completeness=("completeness", "mean"))
      .round(1)
      .sort_values("correctness", ascending=False)
)
print(per_org.to_string())
"""),
    md("### Figure: descriptive per-organism correctness & completeness\n\nRegenerated from the parsed scores and written next to this notebook. It should match the committed `article/figures/per_organism_scores.png`."),
    code(r"""
fig_df = per_org[per_org.n >= 3]  # mirror the manuscript figure (multi-gene clades)
x = range(len(fig_df))
w = 0.4
fig, ax = plt.subplots(figsize=(11, 5))
ax.bar([i - w/2 for i in x], fig_df.correctness, width=w, label="Correctness", color="#16527a")
ax.bar([i + w/2 for i in x], fig_df.completeness, width=w, label="Completeness", color="#7fb2d6")
ax.axhline(rl.correctness.mean(), ls="--", lw=1, color="#16527a", alpha=.6)
ax.axhline(rl.completeness.mean(), ls="--", lw=1, color="#7fb2d6", alpha=.8)
for i, (sp, row) in zip(x, fig_df.iterrows()):
    ax.text(i, max(row.correctness, row.completeness) + 0.08, f"n={int(row.n)}",
            ha="center", va="bottom", fontsize=8, color="#555")
ax.set_xticks(list(x)); ax.set_xticklabels(fig_df.index, rotation=30, ha="right")
ax.set_ylim(0, 5.2); ax.set_ylabel("Mean score (1-5)")
ax.set_title("BioReason-Pro RL: selected-case scores by organism (clades with n>=3)")
ax.legend(loc="upper right")
fig.tight_layout()
outdir = Path("figures"); outdir.mkdir(exist_ok=True)
fig.savefig(outdir / "per_organism_scores.repro.png", dpi=120)
paper_outdir = Path("../article/figures"); paper_outdir.mkdir(parents=True, exist_ok=True)
fig.savefig(paper_outdir / "per_organism_scores.png", dpi=180)
print("saved", outdir / "per_organism_scores.repro.png")
print("saved", paper_outdir / "per_organism_scores.png")
plt.show()
"""),
    md("## Top performers and critical failures"),
    code(r"""
top = rl[rl.correctness == 5].sort_values("completeness", ascending=False)
fails = rl[rl.correctness == 1]
print(f"Correctness 5/5: {len(top)} genes")
print(top[["species", "gene", "completeness"]].to_string(index=False))
print(f"\nCorrectness 1/5 (critical failures): {len(fails)} genes")
print(fails[["species", "gene", "completeness"]].to_string(index=False))

both5 = rl[(rl.correctness == 5) & (rl.completeness == 5)]
print(f"\nGenes scoring 5/5 on BOTH axes: {len(both5)} -> "
      f"{list(both5.gene)}  (manuscript: only Uggt1)")
"""),
    md("## SFT vs RL cross-check\n\nThe SFT narrative set scores lower than RL, consistent with the paper's claim that SFT has more hallucinations."),
    code(r"""
sft_dist = distribution(sft)
print("SFT score distribution:")
print(sft_dist.to_string())
print()
print(pd.DataFrame([summarise(rl, "RL"), summarise(sft, "SFT")]).to_string(index=False))
"""),
])

# --------------------------------------------------------------------------
# Notebook 2: per-term SFT prediction assessments (Expert Synthetic Review taxonomy)
# --------------------------------------------------------------------------
nb2 = new_notebook(cells=[
    md(r"""
# BioReason-Pro SFT term-prediction assessments on ARGO95

This notebook checks the per-term prediction assessments stored in
`genes/<species>/<gene>/<gene>-sft-predictions.yaml`. Each predicted GO term
carries a `review.assessment` using the Expert Synthetic Review taxonomy
(COR / CNN / LSP / UNC / PLI / NPI / REP), the same scheme used in
`ESR-ECOLI-DET-Mini` and in the SFT results of the manuscript.

The primary SFT term benchmark is **ARGO95**, the 95-gene ARGO139 subset with
HuggingFace `wanglab/protein_catalogue` SFT GO-term predictions. ARGO139 remains
the 139-gene RL narrative benchmark. The 44 ARGO139 genes absent from the HF
catalogue have BioReason-Pro SFT web exports, but those exports expose a much
larger ancestor-rich GO-term panel and are retained only as a supplemental
source-diagnostic view. The all-source SFT union (ARGO139 plus HF-only genes)
is also retained as a supplemental availability view. The cohort membership is enumerated in
`projects/BIOREASON_COMPARISON/benchmark-cohorts.csv` and
`projects/BIOREASON_COMPARISON/benchmark-genes.csv`.
"""),
    code(r"""
import sys
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path.cwd()))
import bioreason_stats as bs

ROOT = bs.find_repo_root()
preds = bs.load_prediction_assessments(ROOT)
rl_keys = bs.load_rl_benchmark_keys(ROOT)
preds["benchmark_key"] = list(zip(preds.species, preds.gene))
preds["in_rl_benchmark"] = preds["benchmark_key"].isin(rl_keys)
n_genes = preds[["species", "gene"]].drop_duplicates().shape[0]
print(f"genes with prediction files: {n_genes}")
print(f"total predicted terms:       {len(preds)}")
print(f"ARGO139 genes:               {len(rl_keys)}")
print("\nsource methods:")
print(preds.source_method.value_counts().to_string())
print("\nsource versions:")
print(preds.source_version.value_counts().to_string())
preds.head()
"""),
    md("## Primary SFT benchmark: ARGO95\n\nThis is the main denominator for SFT term review. ARGO95 is the HF-catalogue subset nested inside the ARGO139 RL narrative benchmark."),
    code(r"""
primary = preds[preds.in_rl_benchmark].copy()
primary_hf = primary[primary.source_version == "wanglab/protein_catalogue"].copy()
primary_web = primary[primary.source_version != "wanglab/protein_catalogue"].copy()
argo95 = primary_hf.copy()

print("ARGO95 primary SFT benchmark:")
print(f"  genes: {argo95[['species', 'gene']].drop_duplicates().shape[0]}")
print(f"  terms: {len(argo95)}")
print("\nSupplemental mixed-source ARGO139 diagnostic:")
print(f"  genes: {primary[['species', 'gene']].drop_duplicates().shape[0]}")
print(f"  terms: {len(primary)}")
print(f"  HF genes: {primary_hf[['species', 'gene']].drop_duplicates().shape[0]} "
      f"({len(primary_hf)} terms)")
print(f"  web-export genes: {primary_web[['species', 'gene']].drop_duplicates().shape[0]} "
      f"({len(primary_web)} terms)")
print("\nCoverage check:")
hf_gene_keys = set(zip(primary_hf.species, primary_hf.gene))
web_gene_keys = set(zip(primary_web.species, primary_web.gene))
print(f"  ARGO139 genes with HF SFT terms: {len(hf_gene_keys)}")
print(f"  ARGO139 genes absent from HF, diagnostic web export only: {len(web_gene_keys)}")
print(f"  web set equals ARGO139 minus HF: {web_gene_keys == (rl_keys - hf_gene_keys)}")
"""),
    md("## Assessment Distribution\n\nOrdered by the Expert Synthetic Review taxonomy, with glosses. The first table is ARGO95. The mixed-source ARGO139 and web-export tables are diagnostic because the web export includes many ancestor terms."),
    code(r"""
def assessment_table(frame):
    counts = frame.assessment.value_counts()
    order = [a for a in bs.ASSESSMENT_ORDER if a in counts.index]
    order += [a for a in counts.index if a not in bs.ASSESSMENT_ORDER]  # any extras
    table = pd.DataFrame({
        "count": [counts[a] for a in order],
        "pct": [round(100 * counts[a] / len(frame), 1) for a in order],
        "meaning": [bs.ASSESSMENT_GLOSS.get(a, "?") for a in order],
    }, index=order)
    table.index.name = None
    return table

def print_distribution(label, frame):
    table = assessment_table(frame)
    genes = frame[["species", "gene"]].drop_duplicates().shape[0]
    print(f"\n{label} ({genes} genes, {len(frame)} terms):")
    print(table.to_string())
    non_unc = frame[frame.assessment != "UNC"].copy()
    print(f"non-UNC: {len(non_unc)} / {len(frame)} ({100 * len(non_unc) / len(frame):.1f}%)")
    if len(non_unc):
        print("non-UNC distribution:")
        print(assessment_table(non_unc).to_string())
    return table

argo95_table = print_distribution("ARGO95 SFT benchmark, HF catalogue source", argo95)
primary_table = print_distribution("Supplemental mixed-source ARGO139", primary)
primary_web_table = print_distribution("ARGO139, web-export source", primary_web)
"""),
    md("## Terms per gene\n\nThis shows why the source label matters: HF catalogue entries are leaf-ish, while web-export entries include much of the ancestor hierarchy."),
    code(r"""
for label, frame in [
    ("ARGO95, HF source", argo95),
    ("ARGO139, web-export source", primary_web),
    ("Supplemental mixed-source ARGO139", primary),
]:
    per_gene = frame.groupby(["species", "gene"]).size().rename("n_terms")
    print("\n" + label)
    print(per_gene.describe().round(1).to_string())
"""),
    md("## Supplemental Views\n\nThese retain the availability-driven denominators for reproducibility: all current SFT genes, and the full HF catalogue subset."),
    code(r"""
hf = preds[preds.source_version == "wanglab/protein_catalogue"].copy()
web = preds[preds.source_version != "wanglab/protein_catalogue"].copy()
hf_only = hf[~hf.in_rl_benchmark].copy()

print_distribution("Supplemental all-source union, all SFT predictions", preds)
print_distribution("Supplemental HF catalogue subset, all current genes", hf)
print(f"\nHF-only genes outside ARGO139: "
      f"{hf_only[['species', 'gene']].drop_duplicates().shape[0]} "
      f"({len(hf_only)} terms)")
"""),
    code(r"""
fig, ax = plt.subplots(figsize=(9, 4.5))
colors = {"COR": "#1a7f37", "CNN": "#16527a", "LSP": "#7fb2d6",
          "UNC": "#bbbbbb", "PLI": "#e0902a", "NPI": "#b3261e", "REP": "#7a4ea3"}
ax.bar(argo95_table.index, argo95_table["count"],
       color=[colors.get(a, "#888") for a in argo95_table.index])
for i, (a, row) in enumerate(argo95_table.iterrows()):
    ax.text(i, row["count"], f"{row['pct']}%", ha="center", va="bottom", fontsize=9)
ax.set_ylabel("predicted terms")
ax.set_title(f"Assessment distribution of {len(primary_hf)} BioReason-Pro SFT HF terms "
             f"(ARGO95)")
fig.tight_layout()
outdir = Path("figures"); outdir.mkdir(exist_ok=True)
fig.savefig(outdir / "assessment_distribution.repro.png", dpi=120)
paper_outdir = Path("../article/figures"); paper_outdir.mkdir(parents=True, exist_ok=True)
fig.savefig(paper_outdir / "sft_assessment_distribution.png", dpi=180)
print("saved", outdir / "assessment_distribution.repro.png")
print("saved", paper_outdir / "sft_assessment_distribution.png")
plt.show()
"""),
    md(r"""
### Interpreting the result

The primary SFT denominator is ARGO95. The mixed-source ARGO139 and web-export
views should be read as diagnostics because the web export includes the full GO
ancestor hierarchy. The all-source union and all-HF catalogue views are retained
as supplemental review views, not as primary BioReason-Pro benchmarks.
"""),
])

for name, nb in [("01_narrative_scores.ipynb", nb1), ("02_prediction_assessments.ipynb", nb2)]:
    nbf.write(nb, name)
    print("wrote", name)
