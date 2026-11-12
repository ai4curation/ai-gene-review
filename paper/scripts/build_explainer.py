"""Build paper/explainer/index.html, the living explainer for the AIGR paper.

Reads generated/stats.json (from compute_stats.py), the deep-dive .tex files and
main.log, so every corpus number matches the manuscript. Hand-written narrative
(claims, plans) lives in this file; update it as the paper moves.
Run: uv run python scripts/build_explainer.py
"""
import datetime, html, json, os, re, subprocess

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
S = json.load(open(os.path.join(ROOT, "generated", "stats.json")))
M, T = S["macros"], S["tables"]
ACTIONS = ["ACCEPT", "KEEP_AS_NON_CORE", "MODIFY", "TOO_GENERAL", "MARK_AS_OVER_ANNOTATED", "REMOVE", "UNDECIDED"]
ALABEL = {"ACCEPT": "Accept", "KEEP_AS_NON_CORE": "Keep as non-core", "MODIFY": "Modify", "TOO_GENERAL": "Too general",
          "MARK_AS_OVER_ANNOTATED": "Over-annotated", "REMOVE": "Remove", "UNDECIDED": "Undecided"}
ACLASS = {a: "a-" + a.lower().replace("_", "-") for a in ACTIONS}
e = html.escape

def row(table, label):
    return next(r for r in T[table] if r["label"] == label)

# ---------------------------------------------------------------- deep dives
# (file stem, short claim, headline, headline source). Headline numbers marked
# "corpus" come from stats.json; "project" ones are copied from project pages and
# still need re-deriving by script.
ipr = row("tab_action_by_iea_pipeline", "InterPro2GO")
DD = [
 ("01_assay_to_function", "Evidence codes say an experiment was done, not how close its readout is to the protein's own activity.",
  f"IEP rows: {M['accIEP']}% accepted, {M['rejIEP']}% rejected. Molecular readouts support a function term 77% of the time, phenotype readouts 8%.", "corpus + project"),
 ("02_iba_seeds", "Tree-based propagation mostly works; when it fails, one wrong seed annotation reaches every descendant.",
  f"IBA accepted {M['accIBA']}%, on a par with IDA ({M['accIDA']}%). 21 of 109 sole-seed P. aeruginosa proteins carry a wrong seed.", "corpus + project"),
 ("03_projection", "Outside model organisms almost everything is projected from orthologs, carrying context the target lineage lacks.",
  f"ISO accepted {M['accISO']}% vs IBA {M['accIBA']}%. Naked mole rat: 1 experimental annotation among ~335,000.", "corpus + project"),
 ("04_keywords", "UniProt keyword mappings read 'regulates' or 'active during' as 'takes part in'.",
  "79–100% of reviewed eukaryotic process keyword rows were over-annotations. GOA retired the pipeline in April 2026.", "project"),
 ("05_domain_mappings", "A domain tells you the kind of function, not which one; rules built on domains spread that guess.",
  f"InterPro2GO rows: {ipr['MODIFY']}% modified, the highest of any pipeline. Of ARBA rows not kept, 62% were true but uninformative.", "corpus + project"),
 ("06_pseudoenzymes_complexes", "Catalytic activity lands on proteins that don't perform it: dead enzymes and non-catalytic subunits.",
  "250 candidate NOT annotations mined from removal reasons across 19 species.", "project"),
 ("07_enzyme_specificity", "Right enzyme class, wrong substrate, chain length or metal; and real reactions with no GO term at all.",
  "68% of the 297 characterised reactions of human P450s reach no GO term.", "project"),
 ("08_regulation_sign", "Right gene, right process, opposite direction.",
  "Seed census: 35 sign-reversal corrections on 25 genes.", "project"),
 ("09_obsoletion", "Obsoleting a term is easy; moving its annotations needs a decision per row, which agentic review supplies.",
  "30 term-obsoletion projects; unfolded protein binding reassigned across 148 genes before both source terms were obsoleted.", "project"),
 ("10_citations", "A citation can pass every check and still be wrong, and annotations outlive retracted papers.",
  "Of 290 pairs flagged by a 2020 misannotation study, 216 have since left GOA; the review overturns one of the study's calls.", "project"),
 ("11_entities", "Annotation assumes one entry is one real protein; fused gene models and isoforms break that.",
  "26 of 58 over-long R. toruloides entries are fusions of 2–4 neighbouring genes.", "project"),
 ("12_predictors", "Predictors copy or learn GO, so they reproduce its error classes, and GO-scored benchmarks reward them.",
  "eggNOG-mapper recovers 44% of core functions for a newly sequenced species; BioReason-Pro: 23 of 955 terms correct and new.", "project"),
]

def tex_to_text(s):
    s = re.sub(r"\\(textit|emph|textbf)\{([^}]*)\}", r"\2", s)
    return s.replace("\\_", "_").replace("---", "—").replace("--", "–").replace("\\", "")

dd_html = []
for stem, claim, headline, src in DD:
    tex = open(os.path.join(ROOT, "sections", "deepdives", stem + ".tex")).read()
    title = tex_to_text(re.search(r"\\subsection\{(.*?)\}\\label", tex).group(1))
    todos, projs = tex.count("\\todo{"), tex.count("\\proj{")
    num = int(stem[:2])
    state = "needs data" if todos else "drafted"
    dd_html.append(f'''<article class="dd">
  <div class="dd-head"><span class="dd-num">{num:02d}</span><h3>{e(title)}</h3></div>
  <p class="dd-claim">{e(claim)}</p>
  <p class="dd-stat">{e(headline)}</p>
  <div class="dd-meta"><span class="chip src">{e(src)}</span><span class="chip {'warn' if todos else 'ok'}">{state}</span>
  <span class="chip plain">{projs} project numbers to re-derive</span><span class="chip plain">{todos} TODO</span></div>
</article>''')

# ---------------------------------------------------------------- charts
def stacked(table, labels=None, title=""):
    rows = T[table] if labels is None else [row(table, l) for l in labels]
    lw, bw, bh, gap, top = 210, 470, 22, 10, 6
    h = top + len(rows) * (bh + gap) + 24
    out = [f'<svg viewBox="0 0 {lw + bw + 20} {h}" role="img" aria-label="{e(title)}" class="chart">']
    for i, r in enumerate(rows):
        y = top + i * (bh + gap)
        out.append(f'<text x="{lw - 10}" y="{y + 11}" class="lab" text-anchor="end">{e(r["label"])}</text>')
        out.append(f'<text x="{lw - 10}" y="{y + 22}" class="sub" text-anchor="end">n = {r["n"]:,}</text>')
        x = lw
        for a in ACTIONS:
            w = bw * r[a] / 100
            if w > 0:
                out.append(f'<rect x="{x:.1f}" y="{y}" width="{w:.1f}" height="{bh}" class="{ACLASS[a]}"><title>{ALABEL[a]}: {r[a]}%</title></rect>')
                if w > 30:
                    out.append(f'<text x="{x + w / 2:.1f}" y="{y + 15}" class="in" text-anchor="middle">{r[a]:.0f}</text>')
            x += w
    yb = top + len(rows) * (bh + gap) + 4
    for t in (0, 25, 50, 75, 100):
        xx = lw + bw * t / 100
        out.append(f'<line x1="{xx}" x2="{xx}" y1="{top - 2}" y2="{yb - 4}" class="grid"/><text x="{xx}" y="{yb + 12}" class="sub" text-anchor="middle">{t}%</text>')
    out.append("</svg>")
    return "\n".join(out)

legend = "".join(f'<span class="lg"><i class="sw {ACLASS[a]}"></i>{ALABEL[a]}</span>' for a in ACTIONS)
EG = ["Experimental", "High-throughput", "Author/curator statement", "Phylogenetic (IBA)", "Sequence/orthology", "Electronic (IEA)"]
chart_eg = stacked("tab_action_by_egroup", EG, "Review actions by evidence class")
chart_iea = stacked("tab_action_by_iea_pipeline", None, "Review actions by electronic pipeline")
chart_aspect = stacked("tab_action_by_aspect", ["MF", "BP", "CC"], "Review actions by GO aspect")

def table_html(table):
    head = "<tr><th>Source</th><th>n</th>" + "".join(f"<th>{ALABEL[a]}</th>" for a in ACTIONS) + "</tr>"
    body = "".join("<tr><td>" + e(r["label"]) + f"</td><td>{r['n']:,}</td>" + "".join(f"<td>{r[a]:.1f}</td>" for a in ACTIONS) + "</tr>" for r in T[table])
    return f'<div class="tw"><table><thead>{head}</thead><tbody>{body}</tbody></table></div>'

# ---------------------------------------------------------------- status
def sh(cmd):
    try: return subprocess.check_output(cmd, cwd=ROOT, shell=True, text=True).strip()
    except Exception: return ""
commit = sh("git rev-parse --short HEAD") or "uncommitted"
pages = re.search(r"\((\d+) pages", open(os.path.join(ROOT, "main.log")).read()) if os.path.exists(os.path.join(ROOT, "main.log")) else None
alltex = sh("cat main.tex sections/*.tex sections/deepdives/*.tex")
n_todo, n_proj = alltex.count("\\todo{"), alltex.count("\\proj{")

# Figures and tables: (name, state). Update as they land.
FIGS = [
 ("Fig. 1: how one annotation is made, three provenance routes (TikZ)", "done"),
 ("Fig. 2: the review system, from fetch to upstream reports (TikZ)", "done"),
 ("Fig. 3: corpus composition by clade and by evidence class and aspect", "done"),
 ("Fig. 4: review actions by evidence class", "done"),
 ("Fig. 5: rejected vs modified rates by evidence code and pipeline", "done"),
 ("Fig. 6: review actions by clade", "done"),
 ("Fig. 7: experimental annotation outcome by annotation date", "done"),
 ("Fig. 8: deep-dive panels (experimental codes, ISO, keywords, domain pipelines)", "done"),
 ("Corpus composition by campaign type", "planned"),
 ("Per-pipeline error rates scaled to all of UniProt-GOA", "planned"),
 ("Predictor outcomes aligned with the deep-dive error classes", "planned"),
 ("Figures for the project-based deep dives (IBA seeds, obsoletion, citations, ...)", "planned"),
 ("Table 1: corpus composition by evidence class and aspect", "done, GOA share planned"),
 ("Tables: actions by evidence class, pipeline, aspect, annotating group", "done"),
 ("Table: GO terms with the highest rejection rate", "done"),
 ("Supplement: actions by code, taxon folder, clade; protein binding", "done"),
]
figs_html = "".join(f'<li><span class="chip {"ok" if s == "done" else "warn" if "done" in s else "plain"}">{e(s)}</span>{e(n)}</li>' for n, s in FIGS)

NEXT = [
 ("Show the calls are right", "Expert grading of a stratified sample of about 500 decisions. Self-consistency (≈99.7% on re-review) is not accuracy."),
 ("Remaining figures", "Campaign-type breakdown, GOA-wide extrapolation, predictor figure, and figures for the project-based deep dives."),
 ("Reconcile keyword numbers", "Corpus-wide keyword2GO rejection (14–24%) is far below the SPKW project subsets (79–100%); state the selection."),
 ("Re-derive project numbers", f"{n_proj} numbers are still copied from project pages; each needs a script under paper/scripts/."),
 ("Gene selection", "Not a random sample: report results by campaign type (whole proteome, thematic, term audit)."),
 ("Extrapolate", "Multiply per-pipeline error rates by current UniProt-GOA volumes."),
 ("References", "refs.bib holds placeholders only; every entry to be looked up, never written from memory."),
]
next_html = "".join(f"<li><strong>{e(a)}.</strong> {e(b)}</li>" for a, b in NEXT)

vals = {
 "NREVIEWS": M["nReviews"], "NANN": M["nAnn"], "NANNNOPB": M["nAnnNoPB"], "NTAXA": M["nOrgFolders"], "NREFS": M["nRefs"],
 "NNEW": M["nNew"], "NPB": M["nPB"], "PCTPB": M["pctPB"], "CHANGED": M["pctChangedNoPB"], "REJECTED": M["pctRejectedNoPB"],
 "ACCEPT": M["pctAcceptNoPB"], "NONCORE": M["pctKeepAsNonCoreNoPB"], "MODIFY": M["pctModifyNoPB"], "TOOGEN": M["pctTooGeneralNoPB"],
 "OVER": M["pctMarkAsOverAnnotatedNoPB"], "REMOVE": M["pctRemoveNoPB"], "UNDEC": M["pctUndecidedNoPB"], "PBMOD": M["pbModify"],
 "ACCIBA": M["accIBA"], "ACCIDA": M["accIDA"], "ACCISO": M["accISO"], "ACCIEP": M["accIEP"], "REJIEP": M["rejIEP"],
 "DEEPDIVES": "\n".join(dd_html), "CHART_EG": chart_eg, "CHART_IEA": chart_iea, "CHART_ASPECT": chart_aspect,
 "LEGEND": legend, "TABLE_GROUP": table_html("tab_action_by_assigned_by"), "FIGS": figs_html, "NEXT": next_html,
 "COMMIT": commit, "PAGES": pages.group(1) if pages else "?", "NTODO": n_todo, "NPROJ": n_proj,
 "BUILT": datetime.date.today().isoformat(),
}
tpl = open(os.path.join(ROOT, "explainer", "template.html")).read()
for k, v in vals.items():
    tpl = tpl.replace("{{" + k + "}}", str(v))
assert "{{" not in tpl, re.findall(r"\{\{\w+\}\}", tpl)
open(os.path.join(ROOT, "explainer", "index.html"), "w").write(tpl)
print("wrote explainer/index.html")
