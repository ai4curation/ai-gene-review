"""Paper figures (figures/*.pdf) and extra tables (generated/tab_*.tex).

Reads paper/data/*.tsv (see extract_annotations.py, extract_goa_meta.py).
All summaries exclude GO:0005515 protein binding unless stated.
Palette validated with the dataviz skill's validate_palette.js (light mode).
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
D, G, F = (os.path.join(ROOT, x) for x in ("data", "generated", "figures"))

ACTIONS = ["ACCEPT", "KEEP_AS_NON_CORE", "MODIFY", "TOO_GENERAL", "MARK_AS_OVER_ANNOTATED", "REMOVE", "UNDECIDED"]
ALABEL = {"ACCEPT": "Accept", "KEEP_AS_NON_CORE": "Keep as non-core", "MODIFY": "Modify", "TOO_GENERAL": "Too general",
          "MARK_AS_OVER_ANNOTATED": "Over-annotated", "REMOVE": "Remove", "UNDECIDED": "Undecided"}
# light-mode action palette (validated: band, chroma, CVD >= 8, normal-vision >= 15); undecided is a deliberate neutral
ACOL = {"ACCEPT": "#008300", "KEEP_AS_NON_CORE": "#1baf7a", "MODIFY": "#2a78d6", "TOO_GENERAL": "#e87ba4",
        "MARK_AS_OVER_ANNOTATED": "#eda100", "REMOVE": "#e34948", "UNDECIDED": "#a7afb5"}
DARK_TEXT_ON = {"MARK_AS_OVER_ANNOTATED", "TOO_GENERAL", "UNDECIDED"}
CAT = ["#2a78d6", "#eb6834", "#1baf7a"]          # reference categorical slots 1-3
SEQ = "#2a78d6"                                   # single-series hue
INK, INK2, GRID, SURF = "#1f2328", "#5b6168", "#e1e0d9", "#ffffff"

plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 8, "axes.edgecolor": "#c3c2b7", "axes.labelcolor": INK2,
    "xtick.color": INK2, "ytick.color": INK, "axes.spines.top": False, "axes.spines.right": False,
    "axes.titlesize": 9, "axes.titleweight": "bold", "axes.titlelocation": "left", "legend.frameon": False,
    "pdf.fonttype": 42,
})

EXP = {"EXP", "IDA", "IPI", "IMP", "IGI", "IEP"}
HTP = {"HTP", "HDA", "HMP", "HGI", "HEP"}
PHYLO = {"IBA", "IBD", "IRD", "IKR"}
SEQS = {"ISS", "ISO", "ISA", "ISM", "IGC", "RCA"}
AUTH = {"TAS", "NAS", "IC"}
EG = ["Experimental", "High-throughput", "Author/curator statement", "Phylogenetic (IBA)",
      "Sequence/orthology", "Electronic (IEA)"]
def egroup(e):
    for name, s in (("Experimental", EXP), ("High-throughput", HTP), ("Phylogenetic (IBA)", PHYLO),
                    ("Sequence/orthology", SEQS), ("Author/curator statement", AUTH)):
        if e in s:
            return name
    return {"IEA": "Electronic (IEA)", "ND": "No data (ND)"}.get(e, "Other")
GOREF = {"GO_REF:0000002": "InterPro2GO", "GO_REF:0000003": "EC2GO", "GO_REF:0000041": "UniPathway2GO",
         "GO_REF:0000043": "UniProt keyword2GO", "GO_REF:0000044": "UniProt subcell. location2GO",
         "GO_REF:0000104": "UniRule", "GO_REF:0000107": "Ensembl Compara", "GO_REF:0000108": "GO logical inference",
         "GO_REF:0000116": "Rhea2GO", "GO_REF:0000117": "ARBA", "GO_REF:0000118": "TreeGrafter",
         "GO_REF:0000120": "Combined automated (UniProt)"}
# label offsets (points) for evidence codes and pipelines in the crowded low-rate corner
OFFSETS = {"IDA": (-14, -6), "IMP": (-16, 4), "IPI": (14, -2), "IGI": (12, 8), "TAS": (-14, -12), "IBA": (14, -10),
           "EXP": (8, -6), "HTP": (-12, 10), "ISS": (-14, 12), "IC": (14, 4), "ISA": (12, 12),
           "Combined automated (UniProt)": (6, 6), "UniProt subcell. location2GO": (6, -7), "UniPathway2GO": (6, 2),
           "Rhea2GO": (6, 3), "EC2GO": (6, 0)}
CLADES = ["Human", "Other mammals", "Other animals", "Fungi", "Plants and algae", "Protists",
          "Bacteria", "Archaea", "Viruses and phages"]

def load():
    a = pd.read_csv(os.path.join(D, "annotations.tsv"), sep="\t", low_memory=False)
    m = pd.read_csv(os.path.join(D, "goa_meta.tsv"), sep="\t", dtype=str)
    a = a[a.action.isin(ACTIONS)].merge(m, on=["id", "term_id", "evidence_type", "reference"], how="left")
    a["egroup"] = a.evidence_type.map(egroup)
    a["pipeline"] = np.where(a.evidence_type == "IEA", a.reference.map(GOREF).fillna("other"), None)
    a["rejected"] = a.action.isin(["REMOVE", "MARK_AS_OVER_ANNOTATED"])
    a["modified"] = a.action.isin(["MODIFY", "TOO_GENERAL"])
    a["year"] = pd.to_numeric(a.date.str[:4], errors="coerce")
    return a

def pct(df, by, order=None, min_n=0):
    t = pd.crosstab(df[by], df.action).reindex(columns=ACTIONS, fill_value=0)
    n = t.sum(1)
    p = t.div(n, axis=0) * 100
    p["n"] = n
    p = p[p.n >= min_n]
    return p.reindex([o for o in order if o in p.index]) if order else p.sort_values("n", ascending=False)

def stacked(ax, p, title=None, label_min=7):
    y = np.arange(len(p))
    left = np.zeros(len(p))
    for act in ACTIONS:
        w = p[act].values
        ax.barh(y, w, left=left, color=ACOL[act], edgecolor=SURF, linewidth=1.0, height=0.68, label=ALABEL[act])
        for yi, (l, wi) in enumerate(zip(left, w)):
            if wi >= label_min:
                ax.text(l + wi / 2, yi, f"{wi:.0f}", ha="center", va="center", fontsize=6.5,
                        color="#0b0b0b" if act in DARK_TEXT_ON else "#ffffff")
        left += w
    ax.set_yticks(y, [f"{i}  (n={int(n):,})" for i, n in zip(p.index, p.n)])
    ax.invert_yaxis(); ax.set_xlim(0, 100); ax.set_xticks([0, 25, 50, 75, 100], ["0", "25", "50", "75", "100%"])
    ax.tick_params(axis="y", length=0)
    if title: ax.set_title(title)

def action_legend(fig, y=0.0):
    h = [plt.Rectangle((0, 0), 1, 1, color=ACOL[a]) for a in ACTIONS]
    fig.legend(h, [ALABEL[a] for a in ACTIONS], ncol=7, loc="lower center", bbox_to_anchor=(0.5, y),
               fontsize=7, handlelength=1, columnspacing=1.2)

def save(fig, name):
    fig.savefig(os.path.join(F, name), bbox_inches="tight"); plt.close(fig)

def latex_esc(s):
    return str(s).replace("&", r"\&").replace("_", r"\_").replace("%", r"\%")

def write_table(name, header, rows, colspec):
    with open(os.path.join(G, name), "w") as fh:
        fh.write("% generated by scripts/figures.py -- do not edit\n")
        fh.write(f"\\begin{{tabular}}{{{colspec}}}\\toprule\n" + " & ".join(header) + r" \\ \midrule" + "\n")
        for r in rows:
            fh.write(" & ".join(latex_esc(c) for c in r) + r" \\" + "\n")
        fh.write("\\bottomrule\n\\end{tabular}\n")

def main():
    os.makedirs(F, exist_ok=True)
    a = load()
    b = a[a.term_id != "GO:0005515"]

    # ---- Fig: corpus composition
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.2, 2.9), gridspec_kw={"width_ratios": [1, 1.25]})
    genes = b.groupby("clade").id.nunique().reindex(CLADES).fillna(0)
    rows_ = b.clade.value_counts().reindex(CLADES).fillna(0)
    y = np.arange(len(CLADES))
    ax1.barh(y, rows_.values, color=SEQ, height=0.6)
    for yi, (r, g) in enumerate(zip(rows_.values, genes.values)):
        ax1.text(r, yi, f"  {int(r):,} ({int(g):,} genes)", va="center", fontsize=6.5, color=INK2)
    ax1.set_yticks(y, CLADES); ax1.invert_yaxis(); ax1.set_xlim(0, rows_.max() * 1.6)
    ax1.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"{v/1000:.0f}k"))
    ax1.set_xlabel("annotations reviewed"); ax1.set_title("a  Annotations by clade"); ax1.tick_params(axis="y", length=0)
    comp = pd.crosstab(b.egroup, b.aspect).reindex(index=EG, columns=["MF", "BP", "CC"], fill_value=0)
    left = np.zeros(len(comp)); y = np.arange(len(comp))
    for asp, col in zip(["MF", "BP", "CC"], CAT):
        ax2.barh(y, comp[asp].values, left=left, color=col, edgecolor=SURF, linewidth=1.0, height=0.6, label=asp)
        left += comp[asp].values
    for yi, tot in enumerate(left):
        ax2.text(tot, yi, f"  {int(tot):,}", va="center", fontsize=6.5, color=INK2)
    ax2.set_yticks(y, EG); ax2.invert_yaxis(); ax2.set_xlim(0, left.max() * 1.25); ax2.tick_params(axis="y", length=0)
    ax2.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"{v/1000:.0f}k"))
    ax2.set_xlabel("annotations reviewed"); ax2.set_title("b  By evidence class and GO aspect")
    ax2.legend(loc="lower right", fontsize=7, title=None, handlelength=1)
    fig.tight_layout(); save(fig, "corpus_composition.pdf")

    # ---- Fig: actions by evidence class (replaces compute_stats version)
    fig, ax = plt.subplots(figsize=(7.2, 2.6))
    stacked(ax, pct(b, "egroup", EG)); fig.tight_layout(rect=(0, 0.08, 1, 1)); action_legend(fig)
    save(fig, "action_by_evidence.pdf")

    # ---- Fig: actions by clade
    fig, ax = plt.subplots(figsize=(7.2, 3.0))
    stacked(ax, pct(b, "clade", CLADES)); fig.tight_layout(rect=(0, 0.07, 1, 1)); action_legend(fig)
    save(fig, "action_by_clade.pdf")

    # ---- Fig: rejected vs modified, evidence codes and IEA pipelines
    codes = b.groupby("evidence_type").agg(n=("action", "size"), rej=("rejected", "mean"), mod=("modified", "mean"))
    codes = codes[codes.n >= 400] * [1, 100, 100]
    pipes = b[b.evidence_type == "IEA"].groupby("pipeline").agg(n=("action", "size"), rej=("rejected", "mean"), mod=("modified", "mean"))
    pipes = pipes[(pipes.n >= 400) & (pipes.index != "other")] * [1, 100, 100]
    allrej, allmod = b.rejected.mean() * 100, b.modified.mean() * 100
    REJC, MODC = ACOL["REMOVE"], ACOL["MODIFY"]
    fig, axes = plt.subplots(1, 2, figsize=(7.2, 3.6), sharex=True)
    for ax, df, title in ((axes[0], codes, "a  Evidence codes"), (axes[1], pipes, "b  Electronic pipelines (IEA)")):
        df = df.sort_values("rej")
        y = np.arange(len(df))
        ax.axvline(allrej, color=REJC, lw=0.8, ls=(0, (3, 3)), zorder=1)
        ax.axvline(allmod, color=MODC, lw=0.8, ls=(0, (3, 3)), zorder=1)
        ax.hlines(y, np.minimum(df.rej, df["mod"]), np.maximum(df.rej, df["mod"]), color=GRID, lw=1.5, zorder=1)
        ax.scatter(df["mod"], y, s=30, color=MODC, edgecolor=SURF, linewidth=1, zorder=3, label="modified or too general")
        ax.scatter(df.rej, y, s=30, color=REJC, edgecolor=SURF, linewidth=1, zorder=3, label="removed or over-annotated")
        ax.set_yticks(y, [f"{i}  (n={int(n):,})" for i, n in zip(df.index, df.n)]); ax.tick_params(axis="y", length=0)
        ax.set_title(title); ax.set_xlabel("% of rows"); ax.grid(axis="x", color=GRID, lw=0.5); ax.set_axisbelow(True)
        ax.set_xlim(0, 36)
    h, l = axes[0].get_legend_handles_labels()
    fig.legend(h, l, ncol=2, loc="lower center", bbox_to_anchor=(0.5, 0), fontsize=7)
    fig.text(0.5, -0.04, "dashed lines: corpus means", ha="center", fontsize=6.5, color=INK2)
    fig.tight_layout(rect=(0, 0.06, 1, 1)); save(fig, "rates_dotplot.pdf")

    # ---- Fig: annotation date vs outcome (experimental codes)
    e = b[b.evidence_type.isin(EXP) & b.year.between(2003, 2025)]
    yr = e.groupby("year").agg(n=("action", "size"), acc=("action", lambda s: (s == "ACCEPT").mean() * 100),
                               rej=("rejected", "mean"), noncore=("action", lambda s: (s == "KEEP_AS_NON_CORE").mean() * 100))
    yr["rej"] *= 100
    fig, ax = plt.subplots(figsize=(4.6, 2.6))
    for col, key, lab in ((CAT[0], "acc", "Accepted"), (CAT[1], "noncore", "Kept as non-core"), (CAT[2], "rej", "Rejected")):
        ax.plot(yr.index, yr[key], color=col, lw=2, marker="o", ms=3)
        ax.text(yr.index[-1] + 0.4, yr[key].iloc[-1], lab, color=INK, fontsize=7, va="center")
    ax.set_xlim(2003, 2029); ax.set_ylim(0, 80); ax.set_ylabel("% of experimental rows"); ax.grid(axis="y", color=GRID, lw=0.5)
    ax.set_xlabel("GOA annotation date (last modified)")
    fig.tight_layout(); save(fig, "experimental_by_year.pdf")

    # ---- Fig: deep-dive panels
    fig, axes = plt.subplots(2, 2, figsize=(7.2, 4.8))
    stacked(axes[0, 0], pct(b[b.aspect == "BP"], "evidence_type", ["IDA", "IPI", "IMP", "IGI", "IEP"], min_n=100), "a  Experimental codes, biological process")
    iso = b[b.evidence_type == "ISO"].copy()
    iso["org"] = iso.organism.map({"rat": "Rat", "mouse": "Mouse", "SCHPO": "S. pombe"})
    stacked(axes[0, 1], pct(iso.dropna(subset=["org"]), "org", ["Rat", "Mouse", "S. pombe"]), "b  ISO (orthology transfer) by target organism")
    kw = b[(b.evidence_type == "IEA") & (b.reference == "GO_REF:0000043")].copy()
    kw["dom"] = np.where(kw.clade.isin(["Bacteria", "Archaea"]), "Prokaryotes",
                np.where(kw.clade == "Viruses and phages", "Viruses and phages", "Eukaryotes"))
    kw["da"] = kw.dom + " " + kw.aspect.fillna("?")
    stacked(axes[1, 0], pct(kw, "da", [f"{d} {x}" for d in ["Eukaryotes", "Prokaryotes", "Viruses and phages"] for x in ["MF", "BP"]], min_n=50),
            "c  UniProt keyword2GO by domain and aspect")
    dm = b[b.pipeline.isin(["InterPro2GO", "ARBA", "TreeGrafter"])].copy()
    dm["pa"] = dm.pipeline + " " + dm.aspect.fillna("?")
    order = [f"{p} {s}" for p in ["InterPro2GO", "ARBA", "TreeGrafter"] for s in ["MF", "BP", "CC"]]
    stacked(axes[1, 1], pct(dm, "pa", order, min_n=100), "d  Domain and rule pipelines by aspect")
    fig.tight_layout(rect=(0, 0.05, 1, 1)); action_legend(fig)
    save(fig, "deepdive_panels.pdf")

    # ---- Tables
    rows = []
    tot = len(b)
    for g in EG + ["No data (ND)"]:
        s = b[b.egroup == g]
        if not len(s): continue
        asp = s.aspect.value_counts()
        rows.append([g, f"{len(s):,}", f"{100 * len(s) / tot:.1f}", f"{asp.get('MF', 0):,}", f"{asp.get('BP', 0):,}",
                     f"{asp.get('CC', 0):,}", f"{s.id.nunique():,}"])
    write_table("tab_composition.tex", ["Evidence class", "Rows", r"\% of corpus", "MF", "BP", "CC", "Genes"], rows, "lrrrrrr")

    t = b.groupby(["term_id", "term_label"]).agg(n=("action", "size"), rejn=("rejected", "sum"),
                                                 rej=("rejected", "mean"), mod=("modified", "mean"),
                                                 code=("evidence_type", lambda s: s.value_counts().index[0]),
                                                 genes=("id", "nunique"))
    t = t[(t.n >= 100) & (t.genes >= 30)].sort_values("rej", ascending=False).head(20)
    write_table("tab_top_rejected_terms.tex", ["GO term", "Label", "Rows", "Genes", "Rejected", r"\% rej.", r"\% mod.", "Top code"],
                [[i, l, f"{r.n:,}", f"{r.genes:,}", f"{int(r.rejn):,}", f"{100 * r.rej:.1f}", f"{100 * r['mod']:.1f}", r.code]
                 for (i, l), r in t.iterrows()], "llrrrrrl")

    pc = pct(b, "clade", CLADES)
    write_table("tab_action_by_clade.tex", ["Clade", "$n$"] + [ALABEL[x] for x in ACTIONS],
                [[i, f"{int(r.n):,}"] + [f"{r[x]:.1f}" for x in ACTIONS] for i, r in pc.iterrows()], "lrrrrrrrr")
    print("figures and tables written")

if __name__ == "__main__":
    main()
