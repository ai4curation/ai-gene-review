#!/usr/bin/env python
"""Generate the two report figures from the live engine + committed caches.

Both figures are derived (never hardcoded): the satisfiable/blocked colouring comes
from the same satisfiability engine used everywhere else, run against the committed
GTEx and Halpern-zonation caches. Regenerate:

    uv run --with matplotlib python figures.py

Writes SVGs into projects/PATHWAY_SATISFIABILITY/.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

from gtex_oracle import load_cache  # noqa: E402
from resolve_context import resolve as resolve_tissues  # noqa: E402
from resolve_zonation import HUMAN_TO_MOUSE, resolve as resolve_zones  # noqa: E402
from zonation_oracle import load_profiles, relative_profile  # noqa: E402

ROOT = Path(__file__).resolve().parents[3]
MODULE = ROOT / "modules" / "gluconeogenesis_human.yaml"
OUT = ROOT / "projects" / "PATHWAY_SATISFIABILITY"

SAT = "#2a7f62"      # satisfiable (green)
BLOCK = "#c2c2c2"    # blocked (grey)
GATE = "#b5482e"     # gate / threshold marker (rust)
plt.rcParams.update({"font.size": 10, "svg.fonttype": "none", "axes.spines.top": False,
                     "axes.spines.right": False})


def fig_tissues() -> Path:
    """Across organs: free-glucose output tracks the G6PC1 gate (GTEx v8)."""
    tissues, matrix = load_cache()
    res = resolve_tissues(str(MODULE), 1.0)
    sat = {t for t, v in res["tissues"].items() if v["satisfiable"]}
    g6 = {t: matrix.get("G6PC1", {}).get(t, 0.0) for t in tissues}
    order = sorted(tissues, key=lambda t: g6[t])  # ascending -> highest at top

    fig, ax = plt.subplots(figsize=(6.4, 9.5))
    y = range(len(order))
    ax.barh(list(y), [max(g6[t], 0.03) for t in order],
            color=[SAT if t in sat else BLOCK for t in order],
            edgecolor="none", height=0.72)
    ax.set_yticks(list(y))
    ax.set_yticklabels([t.replace("_", " ") for t in order], fontsize=6.5)
    ax.set_xscale("log")
    ax.set_xlim(0.03, 1000)
    ax.axvline(1.0, color=GATE, ls="--", lw=1.2)
    ax.text(1.08, len(order) * 0.46, "gate: median TPM = 1", color=GATE, fontsize=8,
            rotation=90, va="center", ha="left")
    ax.set_xlabel("G6PC1 median expression (TPM, log scale)")
    ax.set_title("Free-glucose output tracks the G6PC1 gate", fontsize=12.5, loc="left", pad=10)
    fig.tight_layout()
    path = OUT / "fig-tissues.svg"
    fig.savefig(path, format="svg", bbox_inches="tight")
    plt.close(fig)
    return path


def fig_lobule() -> Path:
    """Within one organ: the same gate resolves the liver lobule (Halpern 2017)."""
    res = resolve_zones(str(MODULE), 0.5)
    profiles = load_profiles()
    rel = relative_profile(profiles[HUMAN_TO_MOUSE["G6PC1"]])
    layers = res["layers"]  # L1 pericentral .. L9 periportal
    xs = [row["layer"] for row in layers]
    sat = [row["satisfiable"] for row in layers]

    fig, ax = plt.subplots(figsize=(7.2, 3.6))
    ax.bar(xs, [rel[i] for i in range(len(layers))],
           color=[SAT if s else BLOCK for s in sat], edgecolor="none", width=0.82)
    for row in layers:
        if not row["satisfiable"]:
            ax.text(row["layer"], 0.03, "blocked\n(no G6PC1)", ha="center", va="bottom",
                    fontsize=7, color=GATE)
    ax.set_xticks(xs)
    ax.set_xticklabels([f"L{i}" for i in xs])
    ax.set_ylabel("G6pc expression\n(fraction of its peak)")
    ax.set_xlabel("liver lobule layer")
    ax.set_ylim(0, 1.05)
    ax.annotate("pericentral", xy=(1, -0.22), xycoords=("data", "axes fraction"),
                ha="left", fontsize=8, color="#555")
    ax.annotate("periportal", xy=(9, -0.22), xycoords=("data", "axes fraction"),
                ha="right", fontsize=8, color="#555")
    ax.set_title("The same gate resolves within the liver: gluconeogenesis is periportal",
                 fontsize=12, loc="left", pad=10)
    fig.tight_layout()
    path = OUT / "fig-lobule.svg"
    fig.savefig(path, format="svg", bbox_inches="tight")
    plt.close(fig)
    return path


if __name__ == "__main__":
    for p in (fig_tissues(), fig_lobule()):
        print("wrote", p.relative_to(ROOT))
