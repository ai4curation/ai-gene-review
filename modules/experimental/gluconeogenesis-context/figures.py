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

from matplotlib.colors import ListedColormap  # noqa: E402
from matplotlib.patches import Rectangle  # noqa: E402

from ai_gene_review.module_logic import compile_module_file, is_satisfied  # noqa: E402
from gtex_oracle import load_cache  # noqa: E402
from kegg_oracle import ORGANISMS, load_cache as load_kegg  # noqa: E402
from resolve_abduction import resolve as resolve_abduction  # noqa: E402
from resolve_context import resolve as resolve_tissues  # noqa: E402
from resolve_zonation import HUMAN_TO_MOUSE, resolve as resolve_zones  # noqa: E402
from zonation_oracle import load_profiles, relative_profile  # noqa: E402

ROOT = Path(__file__).resolve().parents[3]
MODULE = ROOT / "modules" / "gluconeogenesis_human.yaml"
MET_MODULE = ROOT / "modules" / "methionine_biosynthesis.yaml"
OUT = ROOT / "projects" / "PATHWAY_SATISFIABILITY"
KOS = ["metA", "metX", "metB", "metC", "metY", "metE", "metH"]

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
    ax.set_xticks(xs)
    ax.set_xticklabels([f"L{i}" for i in xs])
    ax.set_ylabel("G6pc expression\n(fraction of its peak)")
    ax.set_ylim(0, 1.05)
    ax.annotate("pericentral", xy=(1, -0.2), xycoords=("data", "axes fraction"),
                ha="left", fontsize=9, color="#555")
    ax.annotate("periportal", xy=(9, -0.2), xycoords=("data", "axes fraction"),
                ha="right", fontsize=9, color="#555")
    ax.set_title("Gluconeogenesis along the porto-central axis", fontsize=12.5, loc="left", pad=8)
    fig.tight_layout()
    path = OUT / "fig-lobule.svg"
    fig.savefig(path, format="svg", bbox_inches="tight")
    plt.close(fig)
    return path


def _hex_lattice(R: float, s: float):
    """Hex-packed lattice points inside a circle of radius R (Visium-style spots)."""
    import math
    dy = s * math.sqrt(3) / 2
    pts, j, y = [], 0, -R
    while y <= R:
        x = -R + (s / 2 if j % 2 else 0)
        while x <= R:
            if math.hypot(x, y) <= R * 0.99:
                pts.append((x, y))
            x += s
        y += dy
        j += 1
    return pts


def fig_spatial() -> Path:
    """Spatial view: gluconeogenesis retreats to the periportal rim as the gate tightens.

    The liver lobule's canonical radial geometry (central vein at the centre = pericentral;
    portal tracts at the rim = periportal) is tiled with Visium-style spots. Each spot's
    radial position is mapped to one of Halpern 2017's nine zonation layers, and coloured by
    the engine's satisfiability verdict for that layer. Geometry is the idealised lobule;
    colour is the real per-layer result.
    """
    import math
    from matplotlib.patches import RegularPolygon

    thresholds = [0.3, 0.6, 0.9]
    pts = _hex_lattice(1.0, 0.11)
    fig, axes = plt.subplots(1, len(thresholds), figsize=(9.4, 3.7))
    for ax, t in zip(axes, thresholds):
        layers = resolve_zones(str(MODULE), t)["layers"]  # L1 pericentral .. L9 periportal
        sat = [row["satisfiable"] for row in layers]
        for (x, y) in pts:
            r = math.hypot(x, y)
            li = min(8, int(round(r * 8)))          # centre -> L1, rim -> L9
            ax.scatter(x, y, s=26, color=SAT if sat[li] else BLOCK,
                       edgecolor="white", lw=0.3, zorder=2)
        hexv = RegularPolygon((0, 0), numVertices=6, radius=1.06, orientation=0,
                              fill=False, edgecolor="#999", lw=1.2, zorder=1)
        ax.add_patch(hexv)
        ax.scatter(0, 0, s=42, color="#5b6b8c", zorder=3)  # central vein
        ax.set_title(f"gate bar: rel ≥ {t}", fontsize=10)
        ax.set_xlim(-1.25, 1.25)
        ax.set_ylim(-1.3, 1.25)
        ax.set_aspect("equal")
        ax.axis("off")
    axes[0].annotate("central vein", xy=(0, 0), xytext=(0, -1.22),
                     ha="center", va="top", fontsize=8, color="#5b6b8c")
    fig.suptitle("The same axis projected onto the lobule",
                 fontsize=12.5, x=0.02, ha="left", y=1.02)
    fig.tight_layout()
    path = OUT / "fig-spatial.svg"
    fig.savefig(path, format="svg", bbox_inches="tight")
    plt.close(fig)
    return path


def fig_genomes() -> Path:
    """Across genomes: the same engine reconstructs methionine biosynthesis (KEGG)."""
    circuit = compile_module_file(str(MET_MODULE))
    matrix = load_kegg()
    orgs = ["eco", "bsu", "hin", "cgl", "buc", "syn", "mja", "rpr"]
    present = [[1 if matrix.get(o, {}).get(k, False) else 0 for k in KOS] for o in orgs]

    status = []
    for o in orgs:
        def holds(atom, _o=o):
            return bool(atom.gene_symbol) and bool(matrix.get(_o, {}).get(atom.gene_symbol, False))
        status.append("FOUND" if is_satisfied(circuit, holds) else "GAP")

    fig, ax = plt.subplots(figsize=(7.6, 4.2))
    ax.imshow(present, cmap=ListedColormap(["#eeeeee", SAT]), aspect="auto", vmin=0, vmax=1)
    ax.set_xticks(range(len(KOS)))
    ax.set_xticklabels(KOS)
    ax.set_yticks(range(len(orgs)))
    ax.set_yticklabels([f"{ORGANISMS.get(o, o)}" for o in orgs], fontsize=8.5)
    ax.set_xticks([x - 0.5 for x in range(len(KOS) + 1)], minor=True)
    ax.set_yticks([y - 0.5 for y in range(len(orgs) + 1)], minor=True)
    ax.grid(which="minor", color="white", lw=2)
    ax.tick_params(which="minor", length=0)
    for i, s in enumerate(status):
        ax.text(len(KOS) - 0.35, i, s, va="center", ha="left",
                color=(SAT if s == "FOUND" else GATE), fontsize=8.5, fontweight="bold")
    # column-group brackets: acylation | sulfur | methylation
    groups = [(0, 1, "acylation"), (2, 4, "sulfur incorporation"), (5, 6, "methylation")]
    for a, b, label in groups:
        ax.plot([a - 0.4, b + 0.4], [-0.75, -0.75], color="#555", lw=1.1, clip_on=False)
        ax.text((a + b) / 2, -1.0, label, ha="center", va="bottom", fontsize=8, color="#555")
    ax.set_xlim(-0.5, len(KOS) + 1.3)
    ax.set_title("One engine reconstructs methionine biosynthesis across genomes",
                 fontsize=12.5, loc="left", pad=22)
    fig.tight_layout()
    path = OUT / "fig-genomes.svg"
    fig.savefig(path, format="svg", bbox_inches="tight")
    plt.close(fig)
    return path


def fig_abduction() -> Path:
    """A gap is a hypothesis: satisfiability × independent phenotype."""
    short = {"eco": "E. coli", "bsu": "B. subtilis", "cgl": "C. glutamicum",
             "syn": "Synechocystis", "mja": "M. jannaschii", "rpr": "Rickettsia"}
    data = resolve_abduction()
    fig, ax = plt.subplots(figsize=(6.8, 5.2))
    ax.add_patch(Rectangle((-0.05, 0.5), 0.55, 0.6, color="#f3d9cf", zorder=0))  # sat=no, active=yes
    ax.axvline(0.5, color="#ccc", lw=1)
    ax.axhline(0.5, color="#ccc", lw=1)

    quad_labels = [
        (0.22, 1.06, "ABDUCTION TARGET\nmakes it, but a step has no candidate", GATE),
        (0.78, 1.06, "CONSISTENT (active)\nruns, and encoded", SAT),
        (0.22, -0.13, "CONSISTENT (inactive)\ncan't, and doesn't", "#555"),
        (0.78, -0.13, "over-prediction\nencoded, not realised", "#999"),
    ]
    for x, y, t, c in quad_labels:
        ax.text(x, y, t, ha="center", va="center", fontsize=8.5, color=c, fontweight="bold")

    # place organisms, stacking within a quadrant; label sits to the right of the dot
    from collections import defaultdict
    bucket = defaultdict(list)
    for org, r in data.items():
        ab = r["abduction"]
        bucket[(1 if ab.satisfiable else 0, 1 if ab.asserted_active else 0)].append((org, ab))
    for (sx, sy), members in bucket.items():
        n = len(members)
        for i, (org, ab) in enumerate(members):
            yy = (0.82 if sy else 0.35) - (i - (n - 1) / 2) * 0.13
            xx = 0.60 if sx else 0.10
            is_target = ab.classification == "ABDUCTION_TARGET"
            col = GATE if is_target else (SAT if (sy and sx) else "#888")
            ax.scatter([xx], [yy], s=90, color=col, edgecolor="white", lw=1, zorder=3)
            ax.text(xx + 0.035, yy, short.get(org, org), ha="left", va="center",
                    fontsize=8.5, color=col, fontweight="bold", zorder=4)

    ax.set_xlim(-0.05, 1.05)
    ax.set_ylim(-0.2, 1.15)
    ax.set_xticks([0.25, 0.75])
    ax.set_xticklabels(["engine: NOT satisfiable", "engine: satisfiable"])
    ax.set_yticks([0.35, 0.85])
    ax.set_yticklabels(["phenotype:\ncannot make it", "phenotype:\nmakes methionine"], fontsize=8)
    ax.tick_params(length=0)
    for s in ax.spines.values():
        s.set_visible(False)
    ax.set_title("A gap becomes a hypothesis", fontsize=12.5, loc="left", pad=10)
    fig.tight_layout()
    path = OUT / "fig-abduction.svg"
    fig.savefig(path, format="svg", bbox_inches="tight")
    plt.close(fig)
    return path


if __name__ == "__main__":
    for p in (fig_tissues(), fig_lobule(), fig_spatial(), fig_genomes(), fig_abduction()):
        print("wrote", p.relative_to(ROOT))
