"""Deep-dive figures and tables from structured review fields (see extract_structured.py).

Writes figures/{predictions,propagation,evidence_trail}.pdf, generated/tab_agents.tex and
generated/stats_structured.tex (macros). Styling is shared with figures.py.
"""
import os
import sys
import numpy as np
import pandas as pd

sys.path.insert(0, os.path.dirname(__file__))
import figures as base  # noqa: E402  (rcParams, palette, helpers)
plt = base.plt

D, G, F = base.D, base.G, base.F
ASSESS = ["COR", "CNN", "LSP", "UNC", "PLI", "NPI", "REP"]
ALAB = {"COR": "Correct, novel", "CNN": "Correct, not novel", "LSP": "Less precise", "UNC": "Uncertain",
        "PLI": "Wrong paralog", "NPI": "Wrong (non-paralog)", "REP": "Repetition"}
ACOLR = {"COR": "#008300", "CNN": "#1baf7a", "LSP": "#2a78d6", "UNC": "#a7afb5", "PLI": "#e87ba4",
         "NPI": "#eda100", "REP": "#e34948"}
DARK_ON = {"UNC", "PLI", "NPI"}
EV4 = ["IBA", "IEA", "ISO", "ISS"]
RESOURCE = {"UNIPROT": "UniProt", "GO_CENTRAL": "GO Central", "PSEUDOCAP": "PseudoCAP", "REACTOME": "Reactome",
            "FLYBASE": "FlyBase", "INTACT": "IntAct", "OTHER": "Other", "ARUK_UCL": "ARUK-UCL"}
nice = lambda s: str(s).replace("_", " ").lower().capitalize()

macros = {}
def mac(k, v):
    macros[k] = f"{v:,}" if isinstance(v, (int, np.integer)) else (f"{v:.1f}" if isinstance(v, float) else v)

def hbars(ax, s, color=base.SEQ, title=None, fmt="{:,}", raw_labels=False):
    y = np.arange(len(s))
    ax.barh(y, s.values, color=color, height=0.62)
    for yi, v in enumerate(s.values):
        ax.text(v, yi, "  " + fmt.format(v), va="center", fontsize=6.5, color=base.INK2)
    ax.set_yticks(y, [i if raw_labels else nice(i) for i in s.index]); ax.invert_yaxis(); ax.tick_params(axis="y", length=0)
    ax.set_xlim(0, s.max() * 1.25)
    if title: ax.set_title(title)

def predictions():
    P = pd.read_csv(os.path.join(D, "predictions.tsv"), sep="\t")
    P = P[P.assessment.isin(ASSESS)].copy()
    P["method"] = P.source_method.replace({m: "Dark Protein Atlas LLM" for m in P.source_method.unique() if "dashboard" in str(m)})
    big = P.method.value_counts()
    mac("nPredSmall", int(big[big < 20].sum()))
    order = big[big >= 20].index.tolist()
    t = pd.crosstab(P.method, P.assessment).reindex(index=order, columns=ASSESS, fill_value=0)
    p = t.div(t.sum(1), axis=0) * 100
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(7.2, 2.9), gridspec_kw={"width_ratios": [1.45, 1]})
    y = np.arange(len(p)); left = np.zeros(len(p))
    for c in ASSESS:
        w = p[c].values
        a1.barh(y, w, left=left, color=ACOLR[c], edgecolor=base.SURF, linewidth=1, height=0.62, label=ALAB[c])
        for yi, (l, wi) in enumerate(zip(left, w)):
            if wi >= 8:
                a1.text(l + wi / 2, yi, f"{wi:.0f}", ha="center", va="center", fontsize=6.5,
                        color="#0b0b0b" if c in DARK_ON else "#ffffff")
        left += w
    a1.set_yticks(y, [f"{i}  (n={int(n)})" for i, n in zip(p.index, t.sum(1))]); a1.invert_yaxis()
    a1.tick_params(axis="y", length=0); a1.set_xlim(0, 100); a1.set_xticks([0, 25, 50, 75, 100], ["0", "25", "50", "75", "100%"])
    a1.set_title("a  Assessment of predicted terms")
    a1.legend(ncol=4, fontsize=6.5, loc="upper center", bbox_to_anchor=(0.45, -0.14), handlelength=1, columnspacing=0.9)
    err = P[P.assessment.isin(["PLI", "NPI", "REP"])].error_type.dropna().value_counts()
    hbars(a2, err.head(8), color=ACOLR["NPI"], title="b  Error type of incorrect predictions")
    fig.tight_layout(); base.save(fig, "predictions.pdf")
    mac("nPredictions", len(P)); mac("nPredictionFiles", P.file.nunique())
    for c in ASSESS:
        mac("predPct" + c, 100 * (P.assessment == c).mean())
    mac("predPctCorrect", 100 * P.assessment.isin(["COR", "CNN"]).mean())
    mac("predPctWrong", 100 * P.assessment.isin(["PLI", "NPI", "REP"]).mean())

def propagation():
    R = pd.read_csv(os.path.join(D, "propagation.tsv"), sep="\t")
    R["ev"] = np.where(R.evidence_type.isin(EV4), R.evidence_type, "other")
    rc = R.root_cause.value_counts()
    t = pd.crosstab(R.root_cause, R.ev).reindex(index=rc.index, columns=EV4 + ["other"], fill_value=0)
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(7.2, 3.2))
    y = np.arange(len(t)); left = np.zeros(len(t))
    for ev, col in zip(EV4 + ["other"], base.CAT + ["#eda100", "#a7afb5"]):
        a1.barh(y, t[ev].values, left=left, color=col, edgecolor=base.SURF, linewidth=1, height=0.62, label=ev)
        left += t[ev].values
    for yi, v in enumerate(rc.values):
        a1.text(left[yi], yi, f"  {v:,}", va="center", fontsize=6.5, color=base.INK2)
    a1.set_yticks(y, [nice(i) for i in t.index]); a1.invert_yaxis(); a1.tick_params(axis="y", length=0)
    a1.set_xlim(0, left.max() * 1.25); a1.set_title("a  Root cause, by evidence code")
    a1.legend(fontsize=6.5, loc="lower right", handlelength=1)
    fm = R.failure_modes.dropna().str.split("|").explode()
    fm = fm[fm.str.len() > 0].value_counts().head(12)
    hbars(a2, fm, title="b  Failure modes named (rows can name several)")
    fig.tight_layout(); base.save(fig, "propagation.pdf")
    mac("nPropRows", len(R)); mac("nPropGenes", R.gene.nunique())
    ok = R.root_cause.isin(["NO_FAILURE_CORE", "NO_FAILURE_NON_CORE"])
    mac("pctPropNoFailure", 100 * ok.mean())
    mac("pctPropScoping", 100 * (R.root_cause == "TERM_SCOPING_PROBLEM").mean())
    mac("pctPropBad", 100 * (R.root_cause == "PROPAGATION_BAD").mean())
    mac("pctPropSource", 100 * R.root_cause.isin(["SOURCE_BAD", "SOURCE_WEAK_OR_INFERRED", "SOURCE_STALE_OR_MISSING"]).mean())
    for ev in EV4:
        s = R[R.evidence_type == ev]
        mac("pctPropNoFailure" + ev, 100 * s.root_cause.isin(["NO_FAILURE_CORE", "NO_FAILURE_NON_CORE"]).mean())

def evidence_trail():
    S = pd.read_csv(os.path.join(D, "source_defects.tsv"), sep="\t")
    Fr = pd.read_csv(os.path.join(D, "ref_reviews.tsv"), sep="\t")
    fig, axes = plt.subplots(1, 3, figsize=(7.2, 2.7))
    hbars(axes[0], S.defect_type.value_counts().head(8), title="a  Source defects by type")
    res = S.resource.value_counts().head(8)
    res.index = [RESOURCE.get(i, i) for i in res.index]
    hbars(axes[1], res, title="b  By responsible resource", raw_labels=True)
    bad = Fr.correctness.value_counts().drop(["VERIFIED"], errors="ignore")
    hbars(axes[2], bad, color=base.ACOL["REMOVE"], title="c  References not verified")
    fig.tight_layout(); base.save(fig, "evidence_trail.pdf")
    mac("nSourceDefects", len(S)); mac("nSourceDefectGenes", S.gene.nunique())
    mac("nRefReviews", len(Fr)); mac("pctRefVerified", 100 * (Fr.correctness == "VERIFIED").mean())
    for k in ["MISCITED", "WRONG_IDENTIFIER", "DISPUTED", "LOW_QUALITY", "UNVERIFIED"]:
        mac("nRef" + k.title().replace("_", ""), int((Fr.correctness == k).sum()))
    mac("pctDefectWrongTerm", 100 * (S.defect_type == "WRONG_TERM").mean())

def agents():
    H = pd.read_csv(os.path.join(D, "history.tsv"), sep="\t")
    tool = H.agent_tool.fillna("unrecorded").str.lower()
    tool = np.where(tool.str.contains("claude"), "Claude Code", np.where(tool.str.contains("codex"), "Codex",
             np.where(tool.str.contains("antigravity|agy|gemini"), "Antigravity (Gemini)", "unrecorded")))
    m = H.model.fillna("").str.lower()
    fam = np.where(m.str.startswith("claude"), "Claude", np.where(m.str.startswith("gpt"), "GPT",
            np.where(m.str.startswith("gemini"), "Gemini", "not recorded")))
    t = pd.crosstab(pd.Series(tool, name="tool"), pd.Series(fam, name="model"))
    cols = [c for c in ["Claude", "GPT", "Gemini", "not recorded"] if c in t.columns]
    t = t[cols]; t["Total"] = t.sum(1); t = t.sort_values("Total", ascending=False)
    rows = [[i] + [f"{v:,}" for v in r.values] for i, r in t.iterrows()]
    base.write_table("tab_agents.tex", ["Agent tool"] + [{"Claude": "Claude", "GPT": "GPT", "Gemini": "Gemini"}.get(c, "Model not recorded") for c in cols] + ["Records"],
                     rows, "l" + "r" * (len(cols) + 1))
    mac("nHistory", len(H)); mac("nHistoryGenes", H.slug.nunique())
    ts = pd.to_datetime(H.timestamp, errors="coerce", utc=True)
    mac("historyFirst", ts.min().strftime("%B %Y")); mac("historyLast", ts.max().strftime("%B %Y"))

def main():
    predictions(); propagation(); evidence_trail(); agents()
    with open(os.path.join(G, "stats_structured.tex"), "w") as fh:
        fh.write("% generated by scripts/figures_structured.py -- do not edit\n")
        for k, v in sorted(macros.items()):
            fh.write(f"\\newcommand{{\\{k}}}{{{v}}}\n")
    import json
    with open(os.path.join(G, "stats_structured.json"), "w") as fh:
        json.dump(macros, fh, indent=1)
    print(f"structured figures written; {len(macros)} macros")

if __name__ == "__main__":
    main()
