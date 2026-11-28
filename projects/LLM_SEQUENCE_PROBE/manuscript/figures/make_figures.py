"""Draw the manuscript figures from the committed model outputs. Usage: make_figures.py (no arguments)."""
import collections, json, math, pathlib, statistics
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
HERE = pathlib.Path(__file__).parent; ROOT = HERE.parent.parent
MODELS = [("claude-fable-5-2", "Fable 5.2", "#2a78d6"), ("claude-opus-5-5", "Opus 5.5", "#eb6834"), ("claude-opus-4-6", "Opus 4.6", "#1baf7a")]
INK, MUTED, GRID = "#1a1a19", "#6b6a63", "#e4e3dd"
plt.rcParams.update({"font.size": 8.5, "font.family": "DejaVu Sans", "axes.edgecolor": MUTED, "axes.labelcolor": INK, "xtick.color": INK,
                     "ytick.color": MUTED, "axes.spines.top": False, "axes.spines.right": False, "pdf.fonttype": 42})
def rows(path): return [json.loads(l) for l in open(path)]
def bars(ax, groups, values, ymax, fmt="{:.0f}"):
    w = 0.26
    for k, (mid, label, col) in enumerate(MODELS):
        xs = [i + (k - 1) * w for i in range(len(groups))]
        ax.bar(xs, values[mid], w - 0.03, color=col, label=label, zorder=3)
        for x, v in zip(xs, values[mid]): ax.text(x, v + ymax * 0.015, fmt.format(v), ha="center", va="bottom", fontsize=7, color=INK)
    ax.set_xticks(range(len(groups))); ax.set_xticklabels(groups); ax.set_ylim(0, ymax); ax.tick_params(length=0)
    ax.grid(axis="y", color=GRID, linewidth=0.6, zorder=0); ax.spines["left"].set_visible(False)

# Figure 1: share of sequences called catalytically active, by sequence class
T = {t["accession"]: t for t in json.loads((ROOT / "pseudo/truth.json").read_text())}
classes = [("kinase", "wt", "Kinase\nwild type"), ("kinase", "asp_to_asn", "Kinase\nAsp→Asn"), ("kinase", "lys_to_met", "Kinase\nLys→Met"),
           ("pseudo", "wt", "Natural\npseudokinase"), ("enzyme", "wt", "Other enzyme\nwild type"), ("enzyme", "site_to_ala", "Other enzyme\nsite→Ala")]
vals = {}
for mid, _, _ in MODELS:
    c = collections.Counter(); n = collections.Counter()
    for r in rows(ROOT / f"pseudo/results/{mid}.jsonl"):
        key = (T[r["accession"]]["group"], r["variant"]); n[key] += 1
        c[key] += str((r.get("ans") or {}).get("catalytically_active")).lower() == "yes"
    vals[mid] = [100 * c[(g, v)] / n[(g, v)] for g, v, _ in classes]
fig, ax = plt.subplots(figsize=(6.6, 2.7))
bars(ax, [c[2] for c in classes], vals, 112); ax.set_yticks([0, 25, 50, 75, 100]); ax.set_ylabel("Called catalytically active (%)")
ax.legend(frameon=False, ncol=3, loc="upper center", bbox_to_anchor=(0.5, 1.16))
fig.tight_layout(); fig.savefig(HERE / "fig1_pseudoenzyme.pdf"); plt.close(fig)

# Figure 2: secondary structure and contact precision against deposited structures (ASPRV1 counted once)
S = {t["pdb"]: t for t in json.loads((ROOT / "structure/truth.json").read_text())}
DUP = {"27JP", "27JO", "27IQ"}
def ss(n, h, e):
    s = ["C"] * (n + 1)
    for code, segs in (("H", h), ("E", e)):
        for g in segs or []:
            if isinstance(g, list) and len(g) == 2 and all(isinstance(v, int) for v in g):
                for i in range(max(1, g[0]), min(n, g[1]) + 1): s[i] = code
    return s
q3 = {}; cp = {}; base = collections.defaultdict(list); chance = collections.defaultdict(list)
for mid, _, _ in MODELS:
    q = collections.defaultdict(list); p = collections.defaultdict(list)
    for r in rows(ROOT / f"structure/results/{mid}.jsonl"):
        t = S[r["pdb"]]; a = r.get("ans")
        if r["pdb"] in DUP or not a: continue
        L = len(t["sequence"]); ca = {int(k): v for k, v in t["ca"].items()}; tr, pr = ss(L, t["helices"], t["strands"]), ss(L, a.get("helices"), a.get("strands"))
        q[t["stratum"]].append(100 * sum(tr[i] == pr[i] for i in ca) / len(ca))
        pairs = [x for x in (a.get("contacts") or []) if isinstance(x, list) and len(x) == 2 and all(isinstance(v, int) for v in x)
                 and abs(x[0] - x[1]) >= 24 and x[0] in ca and x[1] in ca]
        if pairs: p[t["stratum"]].append(100 * sum(math.dist(ca[i], ca[j]) < 8 for i, j in pairs) / len(pairs))
        if mid == MODELS[0][0]:
            base[t["stratum"]].append(100 * max(sum(tr[i] == c for i in ca) for c in "HEC") / len(ca))
            obs = sorted(ca); lr = [(i, j) for i in obs for j in obs if j - i >= 24]
            chance[t["stratum"]].append(100 * sum(math.dist(ca[i], ca[j]) < 8 for i, j in lr) / len(lr))
    q3[mid] = [statistics.mean(q[s]) for s in ("novel", "known")]; cp[mid] = [statistics.mean(p[s]) for s in ("novel", "known")]
fig, axs = plt.subplots(1, 2, figsize=(6.6, 2.7))
labels = ["Novel\n(no prior homolog)", "Known\n(prior homologs)"]
for ax, v, ymax, ylab, ref, name in ((axs[0], q3, 100, "Secondary structure accuracy, Q3 (%)", base, "best single\nstate"),
                                     (axs[1], cp, 62, "Long-range contact precision (%)", chance, "chance")):
    bars(ax, labels, v, ymax, "{:.0f}"); ax.set_ylabel(ylab); ax.set_xlim(-0.55, 1.95)
    for i, s in enumerate(("novel", "known")):
        y = statistics.mean(ref[s]); ax.plot([i - 0.42, i + 0.42], [y, y], color=INK, linewidth=1, linestyle=(0, (3, 2)), zorder=4)
    ax.text(1.47, statistics.mean(ref["known"]), name, ha="left", va="center", fontsize=7, color=MUTED)
h, l = axs[0].get_legend_handles_labels(); fig.legend(h, l, frameon=False, ncol=3, loc="upper center")
fig.tight_layout(rect=(0, 0, 1, 0.92)); fig.savefig(HERE / "fig2_structure.pdf"); plt.close(fig)
print({m: [round(x, 1) for x in v] for m, v in vals.items()}); print("Q3", q3); print("contacts", cp); print({k: round(statistics.mean(v), 1) for k, v in base.items()}, {k: round(statistics.mean(v), 1) for k, v in chance.items()})
