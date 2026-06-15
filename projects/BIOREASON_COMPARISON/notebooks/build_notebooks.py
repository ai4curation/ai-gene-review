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
manuscript:

- overall mean **Correctness** and **Completeness** (RL: 3.7 / 2.9; SFT: 2.9 / 2.7)
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

rl = bs.parse_narrative_reviews("rl", ROOT)
sft = bs.parse_narrative_reviews("sft", ROOT)
print(f"RL  reviews parsed: {len(rl)}  (skipped: {len(rl.attrs['skipped'])})")
print(f"SFT reviews parsed: {len(sft)} (skipped: {len(sft.attrs['skipped'])})")
if sft.attrs["skipped"]:
    print("  skipped SFT files (no parseable score line):")
    for p in sft.attrs["skipped"]:
        print("   ", p)
rl.head()
"""),
    md("## Overall means\n\nCompare the computed means against the values quoted in the manuscript."),
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
print("\nManuscript values -> RL: correctness 3.7, completeness 2.9 | "
      "SFT: correctness 2.9, completeness 2.7")
"""),
    md("## Table 1 — score distribution (RL, 139 genes)"),
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
    md("## Table 2 — per-organism means\n\nSorted by mean correctness, descending. `n` is the number of reviewed genes per clade."),
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
    md("### Figure: per-organism correctness & completeness\n\nRegenerated from the parsed scores and written next to this notebook. It should match the committed `article/figures/per_organism_scores.png`."),
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
ax.set_title("BioReason-Pro RL: per-organism narrative scores (clades with n>=3)")
ax.legend(loc="upper right")
fig.tight_layout()
outdir = Path("figures"); outdir.mkdir(exist_ok=True)
fig.savefig(outdir / "per_organism_scores.repro.png", dpi=120)
print("saved", outdir / "per_organism_scores.repro.png")
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
# Notebook 2: per-term prediction assessments (de Crecy-Lagard taxonomy)
# --------------------------------------------------------------------------
nb2 = new_notebook(cells=[
    md(r"""
# GO-GPT / BioReason-Pro term-prediction assessments

This notebook audits the per-term prediction assessments stored in
`genes/<species>/<gene>/<gene>-gogpt-leaf-predictions.yaml`. Each predicted GO
term carries a `review.assessment` using the de Crecy-Lagard taxonomy
(COR / CNN / LSP / UNC / PLI / NPI / REP), the same scheme used in the 7-gene
*E. coli* replication and in **Table 5** of the manuscript.

> **Transparency note.** On this branch the prediction YAMLs are the raw web-export
> stubs: every term is still `UNC` ("requires manual assessment"). The
> manually-verified distribution reported as Table 5 (≈67% CNN, 11.5% NPI,
> 4.5% COR) was produced on a separate working branch
> (`feat/bioreason-hf-catalogue`). This notebook deliberately computes the
> distribution **from whatever is on disk** rather than hard-coding Table 5, so
> running it here shows the current (un-reviewed) state, and re-running it on the
> review branch reproduces Table 5 exactly.
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
n_genes = preds[["species", "gene"]].drop_duplicates().shape[0]
print(f"genes with prediction files: {n_genes}")
print(f"total predicted terms:       {len(preds)}")
print("\nsource methods:")
print(preds.source_method.value_counts().to_string())
preds.head()
"""),
    md("## Terms per gene\n\nA genuinely reproducible structural statistic (independent of the manual review state)."),
    code(r"""
per_gene = preds.groupby(["species", "gene"]).size().rename("n_terms")
print(per_gene.describe().round(1).to_string())
print(f"\nmean terms/gene: {per_gene.mean():.1f}")
"""),
    md("## Assessment distribution\n\nOrdered by the de Crecy-Lagard taxonomy, with glosses."),
    code(r"""
counts = preds.assessment.value_counts()
order = [a for a in bs.ASSESSMENT_ORDER if a in counts.index]
order += [a for a in counts.index if a not in bs.ASSESSMENT_ORDER]  # any extras
table = pd.DataFrame({
    "count": [counts[a] for a in order],
    "pct": [round(100 * counts[a] / len(preds), 1) for a in order],
    "meaning": [bs.ASSESSMENT_GLOSS.get(a, "?") for a in order],
}, index=order)
table.index.name = "assessment"
print(table.to_string())
"""),
    code(r"""
fig, ax = plt.subplots(figsize=(9, 4.5))
colors = {"COR": "#1a7f37", "CNN": "#16527a", "LSP": "#7fb2d6",
          "UNC": "#bbbbbb", "PLI": "#e0902a", "NPI": "#b3261e", "REP": "#7a4ea3"}
ax.bar(table.index, table["count"], color=[colors.get(a, "#888") for a in table.index])
for i, (a, row) in enumerate(table.iterrows()):
    ax.text(i, row["count"], f"{row['pct']}%", ha="center", va="bottom", fontsize=9)
ax.set_ylabel("predicted terms")
ax.set_title(f"Assessment distribution of {len(preds)} GO-GPT term predictions "
             f"({n_genes} genes)")
fig.tight_layout()
outdir = Path("figures"); outdir.mkdir(exist_ok=True)
fig.savefig(outdir / "assessment_distribution.repro.png", dpi=120)
print("saved", outdir / "assessment_distribution.repro.png")
plt.show()
"""),
    md(r"""
### Interpreting the result

If the printed distribution above is **100% UNC**, you are on a branch with the
raw web-export stubs and the manual term-level review has not been merged here
(see the transparency note at the top). The cell logic is identical to what
produces Table 5; only the input files differ.
"""),
])

for name, nb in [("01_narrative_scores.ipynb", nb1), ("02_prediction_assessments.ipynb", nb2)]:
    nbf.write(nb, name)
    print("wrote", name)
