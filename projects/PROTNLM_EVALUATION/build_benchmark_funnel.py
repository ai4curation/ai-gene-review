"""Build the benchmark-provenance numbers and figures for the ProtNLM2 evaluation.

Two steps:

``compute``
    Counts every stage from UniProtKB to our cohorts and writes
    ``benchmark-funnel.json``. It needs the live UniProt REST API, the
    published ProtNLM2 accession list, and a full ProtNLM2 API dump made by
    ``fetch_protnlm_api.py`` (``protnlm_api.jsonl``, not committed).

``render``
    Draws ``figures/benchmark-funnel.svg``, ``figures/benchmark-cohorts.svg``
    and ``figures/benchmark-outcomes.svg`` from ``benchmark-funnel.json`` alone.

    uv run python projects/PROTNLM_EVALUATION/build_benchmark_funnel.py compute --jsonl path/to/protnlm_api.jsonl
    uv run python projects/PROTNLM_EVALUATION/build_benchmark_funnel.py render

The SVGs style themselves through CSS custom properties with light-theme
fallbacks, so they render as plain images on the project page and the deck,
and follow the page theme when inlined into the project brief.
"""

from __future__ import annotations

import csv
import io
import json
import math
import urllib.parse
import urllib.request
from datetime import date
from html import escape
from pathlib import Path

import typer
import yaml

HERE = Path(__file__).parent
FUNNEL_JSON = HERE / "benchmark-funnel.json"
FIGURES = HERE / "figures"
ACCESSION_LIST_URL = (
    "https://ftp.ebi.ac.uk/pub/contrib/UniProt/ProtNLM2/"
    "List_of_UniProt_accessions_that_have_ProtNLM2_annotations.tsv"
)
UNIPROT_SEARCH = "https://rest.uniprot.org/uniprotkb/search"

FLY, HORSE, DONKEY, NEUROSPORA = 7227, 9796, 9793, 367110

# How each cohort was drawn. Counts are derived in compute(); only the
# selection method and its wording are curated here.
COHORTS = [
    {
        "id": "ARGO50",
        "label": "ARGO-50",
        "drawn_from": "whole pilot, 14 taxon groups",
        "method": "hand-picked",
        "detail": "stratified by taxon group and output type",
    },
    {
        "id": "HORSE40",
        "label": "HORSE40",
        "drawn_from": "Equus caballus",
        "method": "hand-picked",
        "detail": "informative claims and biological diversity",
    },
    {
        "id": "FLY41",
        "label": "FLY41",
        "drawn_from": "Drosophila melanogaster",
        "method": "census",
        "detail": "every record with GO or function text",
    },
    {
        "id": "NEUROSPORA20",
        "label": "NEUROSPORA20",
        "drawn_from": "Neurospora crassa",
        "method": "census",
        "detail": "all 16 GO/function records, plus 4 localization cases",
    },
    {
        "id": "POMBE20",
        "label": "POMBE20",
        "drawn_from": "S. pombe, not on the list",
        "method": "off-list",
        "detail": "Swiss-Prot, from the pre-release export",
    },
    {
        "id": "MOD_EVOLUTION20",
        "label": "MOD_EVOLUTION20",
        "drawn_from": "7 model species",
        "method": "hand-picked",
        "detail": "evolutionary questions: substrate, catalysis, complexes",
    },
    {
        "id": "DONKEY40",
        "label": "DONKEY40",
        "drawn_from": "Equus asinus",
        "method": "ranked rule",
        "detail": "most GO terms; needs TreeGrafter and horse IBA",
    },
]

CATEGORIES = ["COR", "CNN", "LSP", "UNC", "NPI", "PLI"]

app = typer.Typer(add_completion=False, help=__doc__)


def uniprot_total(query: str) -> tuple[int, str]:
    url = f"{UNIPROT_SEARCH}?query={urllib.parse.quote(query)}&size=1&fields=accession"
    with urllib.request.urlopen(url, timeout=60) as resp:
        return int(resp.headers["X-Total-Results"]), resp.headers["X-UniProt-Release"]


def read_csv(path: Path) -> list[dict[str, str]]:
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def output_flags(record: dict) -> tuple[bool, bool]:
    """Return (has GO prediction, has function text) for one API record.

    >>> output_flags({"uniProtKBCrossReferences": [{"database": "GO"}], "comments": []})
    (True, False)
    >>> output_flags({"comments": [{"commentType": "FUNCTION"}]})
    (False, True)
    """
    has_go = any(x.get("database") == "GO" for x in record.get("uniProtKBCrossReferences", []))
    has_fn = any(c.get("commentType") == "FUNCTION" for c in record.get("comments", []))
    return has_go, has_fn


@app.command()
def compute(
    jsonl: Path = typer.Option(..., help="Full ProtNLM2 API dump from fetch_protnlm_api.py"),
    accession_list: Path = typer.Option(None, help="Local copy of the published accession list"),
) -> None:
    """Count every stage and write benchmark-funnel.json."""
    total, release = uniprot_total("*")
    swissprot, _ = uniprot_total("reviewed:true")
    trembl, _ = uniprot_total("reviewed:false")

    if accession_list:
        text = accession_list.read_text()
    else:
        with urllib.request.urlopen(ACCESSION_LIST_URL, timeout=120) as resp:
            text = resp.read().decode()
    rows = list(csv.DictReader(io.StringIO(text), delimiter="\t"))
    taxon_of = {r["Entry"]: int(r["Organism (ID)"]) for r in rows}

    flags: dict[str, tuple[bool, bool]] = {}
    with open(jsonl) as f:
        for line in f:
            record = json.loads(line)
            flags[record["primaryAccession"]] = output_flags(record)
    # Listed accessions the API does not serve (HTTP 404 at fetch time); they
    # count as records with no GO or function output.
    missing = sorted(set(taxon_of) - set(flags))
    for acc in missing:
        flags[acc] = (False, False)

    def census(taxa: set[int] | None) -> dict[str, int]:
        accs = [a for a, t in taxon_of.items() if taxa is None or t in taxa]
        return {
            "records": len(accs),
            "with_go": sum(flags[a][0] for a in accs),
            "with_go_or_function": sum(flags[a][0] or flags[a][1] for a in accs),
        }

    pilot = census(None)
    summary = json.loads((HERE / "benchmark-summary.json").read_text())
    by_cohort = {c["cohort"]: c for c in summary["cohorts"]}
    mod_taxa = {int(r["taxon_id"]) for r in read_csv(HERE / "mod-evolution-benchmark/cohort.csv")}
    pombe_inventory = read_csv(HERE / "pombe-benchmark/inventory.csv")
    pombe_cohort = read_csv(HERE / "pombe-benchmark/functional-cohort.csv")

    pools = {
        "ARGO50": pilot,
        "HORSE40": census({HORSE}),
        "FLY41": census({FLY}),
        "NEUROSPORA20": census({NEUROSPORA}),
        "POMBE20": {
            "records": len(pombe_inventory),
            "with_go": None,
            "with_go_or_function": len(pombe_cohort),
        },
        "MOD_EVOLUTION20": census(mod_taxa),
        "DONKEY40": census({DONKEY}),
    }
    donkey_selected = len(yaml.safe_load((HERE / "donkey40/selection.yaml").read_text())["records"])
    # DONKEY40 was reviewed after the snapshot; its per-claim verdicts live in its own table.
    donkey_counts = {k: 0 for k in ["COR", "CNN", "LSP", "UNC", "NPI", "PLI", "REP"]}
    with open(HERE / "donkey40/donkey40_protnlm_vs.tsv", newline="") as f:
        for row in csv.DictReader(f, delimiter="\t"):
            donkey_counts[row["assessment"]] += 1

    cohorts = []
    for c in COHORTS:
        stats = by_cohort.get(c["id"])
        cohorts.append(
            {
                **c,
                "pool": pools[c["id"]],
                "selected": stats["records"] if stats else donkey_selected,
                "go_claims": sum(stats["go_counts"].values()) if stats else sum(donkey_counts.values()),
                "go_counts": stats["go_counts"] if stats else donkey_counts,
                "in_snapshot": stats is not None,
            }
        )

    funnel = {
        "built": date.today().isoformat(),
        "uniprot_release": release,
        "review_snapshot": summary["review_snapshot"],
        "uniprotkb": total,
        "swissprot": swissprot,
        "trembl": trembl,
        "pilot": {**pilot, "taxa": len(set(taxon_of.values())), "listed_but_not_served": missing},
        "prediction_targets": summary["prediction_targets"],
        "prediction_targets_with_any_review": summary["prediction_targets_with_any_review"],
        "go_counts": summary["go_counts"],
        "narrative_records": len(summary["narrative_reviews"]),
        "narrative_counts": summary["narrative_counts"],
        "cohorts": cohorts,
    }
    FUNNEL_JSON.write_text(json.dumps(funnel, indent=2) + "\n")
    typer.echo(f"Wrote {FUNNEL_JSON}")


# ---------------------------------------------------------------- rendering

STYLE = """
<style>
.t { fill: var(--fig-ink, #15201e); font-family: "Source Sans 3", system-ui, -apple-system, Helvetica, Arial, sans-serif; }
.m { fill: var(--muted, #56655f); }
.b { font-weight: 600; }
.num { font-variant-numeric: tabular-nums; }
.box { fill: var(--fig-fill, #e8f1ee); stroke: var(--fig-line, #8fa39c); stroke-width: 1.2; }
.ours { fill: var(--accent, #0e6b66); }
.ours-t { fill: var(--surface, #ffffff); }
.link { fill: var(--fig-fill, #e8f1ee); opacity: .55; }
.rule { stroke: var(--rule, #d6dfdb); stroke-width: 1; fill: none; }
.brk { stroke: var(--fig-line, #8fa39c); stroke-width: 1.5; fill: none; }
.brk-ours { stroke: var(--accent, #0e6b66); stroke-width: 2; fill: none; }
.acc { fill: var(--accent, #0e6b66); }
.census { fill: var(--accept, #1d8a4b); }
.hand { fill: var(--modify, #b8620f); }
.rule-c { fill: var(--new, #1d68b3); }
.off { fill: var(--over, #7657a3); }
.chip-t { fill: var(--surface, #ffffff); font-weight: 600; }
.c-COR { fill: var(--accept, #1d8a4b); } .c-CNN { fill: var(--keep, #4f7c3a); }
.c-LSP { fill: var(--accent, #0e6b66); } .c-UNC { fill: var(--undecided, #6b6f76); }
.c-NPI { fill: var(--remove, #bd3a30); } .c-PLI { fill: var(--over, #7657a3); }
</style>
"""


def fmt(n: int | None) -> str:
    """Thousands separators, or an em dash for a missing value.

    >>> fmt(26856), fmt(None)
    ('26,856', '—')
    """
    return "—" if n is None else f"{n:,}"


def text(x: float, y: float, s: str, cls: str = "t", size: float = 14, anchor: str = "start") -> str:
    return f'<text x="{x:.1f}" y="{y:.1f}" class="{cls}" font-size="{size}" text-anchor="{anchor}">{escape(s)}</text>'


def svg(width: int, height: int, body: list[str], title: str) -> str:
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" '
        f'height="{height}" role="img" aria-label="{escape(title)}">'
        f"<title>{escape(title)}</title>{STYLE}" + "".join(body) + "</svg>\n"
    )


def render_funnel(d: dict) -> str:
    stages = [
        ("UniProtKB", f"release {d['uniprot_release']}", d["uniprotkb"], False),
        ("Unreviewed (TrEMBL)", f"Swiss-Prot is the other {fmt(d['swissprot'])}", d["trembl"], False),
        ("ProtNLM2 public pilot", f"{d['pilot']['taxa']} taxa", d["pilot"]["records"], False),
        ("With GO or function text", "the rest: names, locations, keywords", d["pilot"]["with_go_or_function"], False),
        ("Our prediction targets", f"{d['prediction_targets_with_any_review']} reviewed so far", d["prediction_targets"], True),
    ]
    width, top, row, bar_h = 960, 40, 66, 40
    cx, max_w = 455, 300
    log_max = math.log10(d["uniprotkb"])
    body = [
        text(940, 24, "bar width on a log scale", "t m", 12, "end"),
    ]
    geom = []
    for i, (_, _, n, _) in enumerate(stages):
        w = max_w * math.log10(n) / log_max
        y = top + i * row
        geom.append((cx - w / 2, y, w))
    for i in range(len(geom) - 1):
        x0, y0, w0 = geom[i]
        x1, y1, w1 = geom[i + 1]
        body.append(
            f'<polygon class="link" points="{x0:.1f},{y0 + bar_h} {x0 + w0:.1f},{y0 + bar_h} '
            f'{x1 + w1:.1f},{y1} {x1:.1f},{y1}"/>'
        )
    for (label, sub, n, ours), (x, y, w) in zip(stages, geom):
        cls = "ours" if ours else "box"
        body.append(f'<rect class="{cls}" x="{x:.1f}" y="{y}" width="{w:.1f}" height="{bar_h}" rx="3"/>')
        body.append(text(cx, y + 26, fmt(n), "t b num ours-t" if ours else "t b num", 17, "middle"))
        body.append(text(20, y + 18, label, "t b", 15))
        body.append(text(20, y + 36, sub, "t m", 12.5))

    # Right-hand brackets: who made each cut.
    def bracket(i0: int, i1: int, cls: str, lines: list[str], head: str) -> None:
        y0 = geom[i0][1] + 4
        y1 = geom[i1][1] + bar_h - 4
        x = 640
        body.append(f'<path class="{cls}" d="M{x} {y0} h8 V{y1} h-8"/>')
        mid = (y0 + y1) / 2 - (len(lines) * 16) / 2 + 4
        body.append(text(x + 20, mid, head, "t b acc" if cls == "brk-ours" else "t b", 13.5))
        for k, line in enumerate(lines):
            body.append(text(x + 20, mid + 17 + k * 16, line, "t m", 12.5))

    bracket(1, 2, "brk", ["released by UniProt: ~400 most-searched", "species, TrEMBL only; how entries were", "picked is not documented"], "Chosen upstream")
    bracket(3, 3, "brk", ["ProtNLM2 emitted GO or function text", "for only these records"], "Set by the model's output")
    bracket(4, 4, "brk-ours", ["a species census, or hand-picked"], "Chosen by us")

    foot = top + len(stages) * row + 8
    body.append(f'<line class="rule" x1="20" y1="{foot}" x2="940" y2="{foot}"/>')
    pombe = next(c for c in d["cohorts"] if c["id"] == "POMBE20")
    body.append(
        text(
            20,
            foot + 22,
            f"Not on the list but served by the API: {pombe['pool']['records']} S. pombe Swiss-Prot entries "
            "from the pre-release export (the POMBE20 cohort).",
            "t m",
            12.5,
        )
    )
    body.append(
        text(
            20,
            foot + 40,
            f"Counts: UniProt {d['uniprot_release']}; reviews frozen at {d['review_snapshot']['date']}; "
            f"{len(d['pilot']['listed_but_not_served'])} listed record not served by the API.",
            "t m",
            12.5,
        )
    )
    return svg(width, foot + 54, body, "Funnel from UniProtKB to the ProtNLM2 benchmark cohorts")


CHIP = {"census": ("census", "Census"), "hand-picked": ("hand", "Hand-picked"), "ranked rule": ("rule-c", "Ranked rule"), "off-list": ("off", "Census, off-list")}


def render_cohorts(d: dict) -> str:
    width, top, row = 960, 62, 50
    cols = {"pool": 410, "elig": 530, "picked": 610, "chip": 640, "go": 940}
    o = -30
    body = [
        text(cols["pool"], 70 + o, "Records", "t m b", 12, "end"),
        text(cols["elig"], 70 + o, "GO/function", "t m b", 12, "end"),
        text(cols["picked"], 70 + o, "Picked", "t m b", 12, "end"),
        text(cols["chip"], 70 + o, "How picked", "t m b", 12),
        text(cols["go"], 70 + o, "GO claims", "t m b", 12, "end"),
        f'<line class="rule" x1="20" y1="{top - 14}" x2="940" y2="{top - 14}"/>',
    ]
    for i, c in enumerate(d["cohorts"]):
        y = top + i * row
        body.append(text(20, y + 8, c["label"], "t b", 14.5))
        body.append(text(20, y + 26, c["drawn_from"], "t m", 12.5))
        body.append(text(cols["pool"], y + 8, fmt(c["pool"]["records"]), "t num", 14, "end"))
        body.append(text(cols["elig"], y + 8, fmt(c["pool"]["with_go_or_function"]), "t num", 14, "end"))
        body.append(text(cols["picked"], y + 8, fmt(c["selected"]), "t b num", 14, "end"))
        cls, label = CHIP[c["method"]]
        chip_w = 9 + 6.6 * len(label)
        body.append(f'<rect class="{cls}" x="{cols["chip"]}" y="{y - 7}" width="{chip_w:.0f}" height="19" rx="3"/>')
        body.append(text(cols["chip"] + 5, y + 7, label, "t chip-t", 11.5))
        body.append(text(cols["chip"], y + 26, c["detail"], "t m", 12))
        body.append(text(cols["go"], y + 8, fmt(c["go_claims"]) if c["in_snapshot"] else f"{c['go_claims']} (post-snapshot)", "t num" if c["in_snapshot"] else "t m num", 14 if c["in_snapshot"] else 12.5, "end"))
        if i < len(d["cohorts"]) - 1:
            body.append(f'<line class="rule" x1="20" y1="{y + 38}" x2="940" y2="{y + 38}"/>')
    foot = top + len(d["cohorts"]) * row
    body.append(
        text(
            20,
            foot + 4,
            "Records and GO/function are counts in the released pool the cohort was drawn from. Overlapping cohort members are counted once in project totals.",
            "t m",
            12,
        )
    )
    return svg(width, foot + 20, body, "Selection method and size of each ProtNLM2 benchmark cohort")


def render_outcomes(d: dict) -> str:
    rows = [(c["label"], c["go_counts"]) for c in d["cohorts"] if c["in_snapshot"] and sum(c["go_counts"].values())]
    rows.append(("All cohorts", d["go_counts"]))
    width, top, row, bar_x, bar_w = 960, 52, 34, 190, 640
    body = []
    lx = bar_x
    for cat in CATEGORIES:
        body.append(f'<rect class="c-{cat}" x="{lx}" y="16" width="12" height="12" rx="2"/>')
        body.append(text(lx + 17, 27, cat, "t", 12.5))
        lx += 70
    for i, (label, counts) in enumerate(rows):
        y = top + i * row + (10 if label == "All cohorts" else 0)
        n = sum(counts[c] for c in CATEGORIES)
        body.append(text(20, y + 15, label, "t b" if label == "All cohorts" else "t", 14))
        x = bar_x
        for cat in CATEGORIES:
            w = bar_w * counts[cat] / n
            if w > 0:
                body.append(f'<rect class="c-{cat}" x="{x:.1f}" y="{y}" width="{w:.1f}" height="22"/>')
                if w >= 26:
                    body.append(text(x + w / 2, y + 15.5, str(counts[cat]), "t chip-t num", 11.5, "middle"))
            x += w
        body.append(text(bar_x + bar_w + 12, y + 15, f"n = {n}", "t m num", 12.5))
    foot = top + len(rows) * row + 20
    nc = d["narrative_counts"]
    body.append(f'<line class="rule" x1="20" y1="{foot}" x2="940" y2="{foot}"/>')
    body.append(
        text(
            20,
            foot + 22,
            "Share of each cohort's GO claims. COR means supported and absent from the target's existing annotation, so it is only possible where the target lacks the term.",
            "t m",
            12.5,
        )
    )
    body.append(
        text(
            20,
            foot + 40,
            f"Function paragraphs, {d['narrative_records']} records: paralog confusion (PLI) in {nc['PLI']}, contradicted (NPI) in {nc['NPI']}; GO terms have {d['go_counts']['PLI']} PLI in {sum(d['go_counts'].values())}.",
            "t m",
            12.5,
        )
    )
    return svg(width, foot + 54, body, "Assessment categories of ProtNLM2 GO claims by cohort")


@app.command()
def render() -> None:
    """Draw the three SVG figures from benchmark-funnel.json."""
    d = json.loads(FUNNEL_JSON.read_text())
    FIGURES.mkdir(exist_ok=True)
    for name, fn in [("benchmark-funnel", render_funnel), ("benchmark-cohorts", render_cohorts), ("benchmark-outcomes", render_outcomes)]:
        path = FIGURES / f"{name}.svg"
        path.write_text(fn(d))
        typer.echo(f"Wrote {path}")


if __name__ == "__main__":
    app()
