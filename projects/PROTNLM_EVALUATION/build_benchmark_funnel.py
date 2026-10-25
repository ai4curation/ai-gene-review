"""Build the benchmark-provenance numbers and figures for the ProtNLM2 evaluation.

Two steps:

``compute``
    Counts every stage from UniProtKB to our cohorts and writes
    ``benchmark-funnel.json``. It needs the live UniProt REST API, the
    published ProtNLM2 accession list, and a full ProtNLM2 API dump made by
    ``fetch_protnlm_api.py`` (``protnlm_api.jsonl``, not committed). How each
    cohort was drawn is curated in ``benchmark-cohorts.yaml``.

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
COHORTS_YAML = HERE / "benchmark-cohorts.yaml"
FIGURES = HERE / "figures"
ACCESSION_LIST_URL = (
    "https://ftp.ebi.ac.uk/pub/contrib/UniProt/ProtNLM2/"
    "List_of_UniProt_accessions_that_have_ProtNLM2_annotations.tsv"
)
UNIPROT_SEARCH = "https://rest.uniprot.org/uniprotkb/search"

# Assessment categories of de Crécy-Lagard et al. 2025, in display order.
CATEGORIES = ["COR", "CNN", "LSP", "UNC", "NPI", "PLI", "REP"]
# How a cohort's eligible pool is counted (see benchmark-cohorts.yaml).
ELIGIBLE_BASES = ("go_or_function", "all", "complement", "none")
# Taxa named in the project prose; their pilot counts are recorded so the text is reproducible.
NAMED_TAXA = {"wheat": 4565, "horse": 9796, "donkey": 9793, "fly": 7227, "human": 9606, "mouse": 10090, "rat": 10116}

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


def count_categories(codes: list[str]) -> dict[str, int]:
    """Count assessment codes, refusing any code outside CATEGORIES.

    >>> count_categories(["COR", "UNC", "COR"])["COR"]
    2
    >>> count_categories(["XYZ"])
    Traceback (most recent call last):
    ...
    ValueError: unknown assessment code 'XYZ'; expected one of COR, CNN, LSP, UNC, NPI, PLI, REP
    """
    counts = {k: 0 for k in CATEGORIES}
    for code in codes:
        if code not in counts:
            raise ValueError(f"unknown assessment code {code!r}; expected one of {', '.join(CATEGORIES)}")
        counts[code] += 1
    return counts


def load_cohort_spec() -> dict:
    return yaml.safe_load(COHORTS_YAML.read_text())


@app.command()
def compute(
    jsonl: Path = typer.Option(..., help="Full ProtNLM2 API dump from fetch_protnlm_api.py"),
    accession_list: Path | None = typer.Option(None, help="Local copy of the published accession list"),
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
    spec = load_cohort_spec()
    spec_ids = {c["id"] for c in spec["cohorts"]}
    unlisted = sorted(set(by_cohort) - spec_ids - set(spec["not_drawn_from_release"]))
    if unlisted:
        raise typer.BadParameter(f"benchmark-summary.json cohorts missing from {COHORTS_YAML.name}: {', '.join(unlisted)}")

    for c in spec["cohorts"]:
        if c.get("eligible", "go_or_function") not in ELIGIBLE_BASES:
            raise typer.BadParameter(f"cohort {c['id']}: eligible must be one of {', '.join(ELIGIBLE_BASES)}")

    mod_taxa = {int(r["taxon_id"]) for r in read_csv(HERE / "mod-evolution-benchmark/cohort.csv")}
    pombe_inventory = read_csv(HERE / "pombe-benchmark/inventory.csv")
    pombe_cohort = read_csv(HERE / "pombe-benchmark/functional-cohort.csv")

    def pool(name: str) -> dict:
        if name == "pilot":
            return pilot
        if name == "mod_species":
            return census(mod_taxa)
        if name == "pombe_export":
            return {"records": len(pombe_inventory), "with_go": None, "with_go_or_function": len(pombe_cohort)}
        if name.startswith("taxon:"):
            return census({int(name.split(":", 1)[1])})
        raise typer.BadParameter(f"unknown pool {name!r} in {COHORTS_YAML.name}")

    cohorts = []
    for c in spec["cohorts"]:
        cohorts.append(
            {
                "id": c["id"],
                "label": c["label"],
                "drawn_from": c["drawn_from"],
                "method": c["method"],
                "detail": c["detail"],
                "pool": pool(c["pool"]),
                "eligible_basis": c.get("eligible", "go_or_function"),
                **cohort_review_fields(c, by_cohort),
            }
        )

    # Benchmark targets that are not among the pilot records with GO or function
    # text: off-list accessions, and listed records with only names/locations/keywords.
    species_of = check_target_count(summary)
    targets = set(species_of)
    off_list = sorted(t for t in targets if t not in taxon_of)
    off_list_by_species: dict[str, int] = {}
    for t in off_list:
        off_list_by_species[species_of[t]] = off_list_by_species.get(species_of[t], 0) + 1
    no_go_or_function = sorted(t for t in targets if t in taxon_of and not any(flags[t]))

    taxon_counts: dict[int, int] = {}
    for t in taxon_of.values():
        taxon_counts[t] = taxon_counts.get(t, 0) + 1
    names = {int(r["Organism (ID)"]): r["Organism"] for r in rows}
    top = sorted(taxon_counts.items(), key=lambda kv: -kv[1])[:10]

    funnel = {
        "built": date.today().isoformat(),
        "api_fetched": date.fromtimestamp(jsonl.stat().st_mtime).isoformat(),
        "uniprot_release": release,
        "review_snapshot": summary["review_snapshot"],
        "uniprotkb": total,
        "swissprot": swissprot,
        "trembl": trembl,
        "pilot": {**pilot, "taxa": len(taxon_counts), "listed_but_not_served": missing},
        "pilot_taxa": {
            "top": [{"taxon": t, "organism": names[t], "records": n} for t, n in top],
            "named": {k: taxon_counts.get(t, 0) for k, t in NAMED_TAXA.items()},
        },
        **summary_fields(summary),
        "prediction_targets_outside_go_set": {
            "total": len(off_list) + len(no_go_or_function),
            "not_on_list": len(off_list),
            "not_on_list_by_species": dict(sorted(off_list_by_species.items(), key=lambda kv: -kv[1])),
            "listed_without_go_or_function": len(no_go_or_function),
        },
        "cohorts": cohorts,
    }
    FUNNEL_JSON.write_text(json.dumps(funnel, indent=2) + "\n")
    typer.echo(f"Wrote {FUNNEL_JSON}")


def check_target_count(summary: dict) -> dict[str, str]:
    """Prediction targets from scope.csv (accession -> species); raise if they disagree with the summary's count."""
    scope = [r for r in read_csv(HERE / "family-curation/scope.csv") if r["role"] == "prediction_target"]
    targets = {r["accession"]: r["species"] for r in scope}
    if len(targets) != summary["prediction_targets"]:
        raise typer.BadParameter(f"scope.csv has {len(targets)} prediction targets, benchmark-summary.json {summary['prediction_targets']}")
    return targets


def summary_fields(summary: dict) -> dict:
    """Top-level fields taken from benchmark-summary.json (the review snapshot)."""
    return {
        "review_snapshot": summary["review_snapshot"],
        "prediction_targets": summary["prediction_targets"],
        "prediction_targets_with_any_review": summary["prediction_targets_with_any_review"],
        "go_counts": {k: summary["go_counts"].get(k, 0) for k in CATEGORIES},
        "narrative_records": len(summary["narrative_reviews"]),
        "narrative_counts": summary["narrative_counts"],
    }


def cohort_review_fields(c: dict, by_cohort: dict) -> dict:
    """Per-cohort counts from the review snapshot; DONKEY40 (post-snapshot) from its own table."""
    stats = by_cohort.get(c["id"])
    if stats is None and not c.get("post_snapshot"):
        raise typer.BadParameter(f"cohort {c['id']} is not in benchmark-summary.json and is not marked post_snapshot")
    if stats:
        go_counts = {k: stats["go_counts"].get(k, 0) for k in CATEGORIES}
        selected = stats["records"]
    else:
        # DONKEY40 was reviewed after the snapshot; its per-claim verdicts live in its own table.
        go_counts = count_categories([r["assessment"] for r in read_csv_tsv(HERE / "donkey40/donkey40_protnlm_vs.tsv")])
        selected = len(yaml.safe_load((HERE / "donkey40/selection.yaml").read_text())["records"])
    return {"selected": selected, "go_claims": sum(go_counts.values()), "go_counts": go_counts, "in_snapshot": stats is not None}


@app.command("refresh-reviews")
def refresh_reviews() -> None:
    """Recompute only the review-derived fields of benchmark-funnel.json.

    The UniProt and API counts are kept as committed, so a new review snapshot
    does not require re-fetching the ProtNLM2 API dump.
    """
    data = json.loads(FUNNEL_JSON.read_text())
    summary = json.loads((HERE / "benchmark-summary.json").read_text())
    by_cohort = {c["cohort"]: c for c in summary["cohorts"]}
    # The outside-GO-set block was computed against scope.csv; a changed target count
    # needs a full `compute` with a fresh API dump.
    check_target_count(summary)
    spec = {c["id"]: c for c in load_cohort_spec()["cohorts"]}
    in_funnel = {c["id"] for c in data["cohorts"]}
    if in_funnel != set(spec):
        raise typer.BadParameter(
            f"{COHORTS_YAML.name} and {FUNNEL_JSON.name} list different cohorts "
            f"(only in {COHORTS_YAML.name}: {sorted(set(spec) - in_funnel)}; "
            f"only in {FUNNEL_JSON.name}: {sorted(in_funnel - set(spec))}); rerun `compute`"
        )
    for c in data["cohorts"]:
        c.update(cohort_review_fields(spec[c["id"]], by_cohort))
    data.update(summary_fields(summary))
    data["built"] = date.today().isoformat()
    FUNNEL_JSON.write_text(json.dumps(data, indent=2) + "\n")
    typer.echo(f"Wrote {FUNNEL_JSON}")


def read_csv_tsv(path: Path) -> list[dict[str, str]]:
    with open(path, newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


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
.c-REP { fill: var(--modify, #b8620f); }
</style>
"""


def fmt(n: int | None) -> str:
    """Thousands separators, or an em dash for a missing value.

    >>> fmt(26856), fmt(None)
    ('26,856', '—')
    """
    return "—" if n is None else f"{n:,}"


def plural(n: int, word: str) -> str:
    """Count plus a noun, pluralised with -s.

    >>> plural(1, "record"), plural(2, "record")
    ('1 record', '2 records')
    """
    return f"{n} {word}" if n == 1 else f"{n} {word}s"


SPECIES_NAMES = {"SCHPO": "S. pombe", "DROME": "fly"}


def species_breakdown(counts: dict[str, int]) -> str:
    """Render per-species counts as prose.

    >>> species_breakdown({"SCHPO": 28, "DROME": 9})
    '28 S. pombe, 9 fly'
    """
    return ", ".join(f"{n} {SPECIES_NAMES.get(sp, sp)}" for sp, n in counts.items())


def text(x: float, y: float, s: str, cls: str = "t", size: float = 14, anchor: str = "start") -> str:
    return f'<text x="{x:.1f}" y="{y:.1f}" class="{cls}" font-size="{size}" text-anchor="{anchor}">{escape(s)}</text>'


def svg(width: int, height: int, body: list[str], title: str) -> str:
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" '
        f'height="{height}" role="img" aria-label="{escape(title)}">'
        f"<title>{escape(title)}</title>{STYLE}" + "".join(body) + "</svg>\n"
    )


def render_funnel(d: dict) -> str:
    outside = d["prediction_targets_outside_go_set"]
    stages = [
        ("UniProtKB", f"release {d['uniprot_release']}", d["uniprotkb"], False),
        ("Unreviewed (TrEMBL)", f"Swiss-Prot is the other {fmt(d['swissprot'])}", d["trembl"], False),
        ("ProtNLM2 public pilot", f"{d['pilot']['taxa']} taxa", d["pilot"]["records"], False),
        ("With GO or function text", "the rest: names, locations, keywords", d["pilot"]["with_go_or_function"], False),
        ("Our prediction targets", f"{d['prediction_targets_with_any_review']} of {d['prediction_targets']} reviewed; {outside['total']} from outside the set above", d["prediction_targets"], True),
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
    # The last stage is not nested inside the one above it, so it gets no connector.
    for i in range(len(geom) - 2):
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
    body.append(
        text(
            20,
            foot + 22,
            f"Targets outside the GO/function set: {outside['not_on_list']} not on the published list "
            f"({species_breakdown(outside['not_on_list_by_species'])}), and {outside['listed_without_go_or_function']} listed with only names, locations or keywords.",
            "t m",
            12.5,
        )
    )
    n_missing = len(d["pilot"]["listed_but_not_served"])
    body.append(
        text(
            20,
            foot + 40,
            f"Counts: UniProt {d['uniprot_release']}; API fetched {d['api_fetched']}; reviews frozen at {d['review_snapshot']['date']}; "
            f"{plural(n_missing, 'listed record')} not served by the API.",
            "t m",
            12.5,
        )
    )
    return svg(width, foot + 54, body, "Funnel from UniProtKB to the ProtNLM2 benchmark cohorts")


def eligible(c: dict) -> int | None:
    """Pool records a cohort could be drawn from, given how it was drawn.

    >>> pool = {"records": 94, "with_go_or_function": 41}
    >>> eligible({"pool": pool, "eligible_basis": "go_or_function"}), eligible({"pool": pool, "eligible_basis": "complement"})
    (41, 53)
    >>> eligible({"pool": pool, "eligible_basis": "all"})
    94
    >>> eligible({"pool": pool, "eligible_basis": "none"}) is None
    True
    """
    basis = c.get("eligible_basis", "go_or_function")
    if basis == "go_or_function":
        return c["pool"]["with_go_or_function"]
    if basis == "all":
        return c["pool"]["records"]
    if basis == "complement":
        return c["pool"]["records"] - c["pool"]["with_go_or_function"]
    if basis == "none":
        return None
    raise ValueError(f"unknown eligible basis {basis!r} for cohort {c.get('id', '?')}")


CHIP = {"census": ("census", "Census"), "hand-picked": ("hand", "Hand-picked"), "ranked rule": ("rule-c", "Ranked rule"), "off-list": ("off", "Census, off-list")}


def render_cohorts(d: dict) -> str:
    width, top, row = 960, 32, 50
    cols = {"pool": 410, "elig": 530, "picked": 610, "chip": 640, "go": 940}
    body = [
        text(cols["pool"], 40, "Records", "t m b", 12, "end"),
        text(cols["elig"], 40, "Eligible", "t m b", 12, "end"),
        text(cols["picked"], 40, "Picked", "t m b", 12, "end"),
        text(cols["chip"], 40, "How picked", "t m b", 12),
        text(cols["go"], 40, "GO claims", "t m b", 12, "end"),
        '<line class="rule" x1="20" y1="48" x2="940" y2="48"/>',
    ]
    for i, c in enumerate(d["cohorts"]):
        y = top + 38 + i * row
        body.append(text(20, y, c["label"], "t b", 14.5))
        body.append(text(20, y + 18, c["drawn_from"], "t m", 12.5))
        body.append(text(cols["pool"], y, fmt(c["pool"]["records"]), "t num", 14, "end"))
        body.append(text(cols["elig"], y, fmt(eligible(c)), "t num", 14, "end"))
        body.append(text(cols["picked"], y, fmt(c["selected"]), "t b num", 14, "end"))
        cls, label = CHIP[c["method"]]
        chip_w = 9 + 6.6 * len(label)
        body.append(f'<rect class="{cls}" x="{cols["chip"]}" y="{y - 15}" width="{chip_w:.0f}" height="19" rx="3"/>')
        body.append(text(cols["chip"] + 5, y - 1, label, "t chip-t", 11.5))
        body.append(text(cols["chip"], y + 18, c["detail"], "t m", 11.5))
        go = fmt(c["go_claims"]) if c["in_snapshot"] else f"{c['go_claims']} (post-snapshot)"
        body.append(text(cols["go"], y, go, "t num" if c["in_snapshot"] else "t m num", 14 if c["in_snapshot"] else 12.5, "end"))
        if i < len(d["cohorts"]) - 1:
            body.append(f'<line class="rule" x1="20" y1="{y + 30}" x2="940" y2="{y + 30}"/>')
    foot = top + 38 + len(d["cohorts"]) * row
    snapshot_picked = sum(c["selected"] for c in d["cohorts"] if c["in_snapshot"])
    body.append(
        text(
            20,
            foot - 4,
            f"Eligible: pool records with GO or function text; whole pool for ARGO-50; records without it for remainder tiers; dash where a tier mixes sources. "
            f"In-snapshot cohorts: {snapshot_picked} memberships, {d['prediction_targets']} distinct targets.",
            "t m",
            12,
        )
    )
    return svg(width, foot + 12, body, "Selection method and size of each ProtNLM2 benchmark cohort")


def render_outcomes(d: dict) -> str:
    rows = [(c["label"], c["go_counts"], False) for c in d["cohorts"] if c["in_snapshot"] and c["go_claims"]]
    rows.append((TOTAL_LABEL, d["go_counts"], False))
    rows += [(f"{c['label']} (later)", c["go_counts"], True) for c in d["cohorts"] if not c["in_snapshot"] and c["go_claims"]]
    width, top, row, bar_x, bar_w = 960, 52, 34, 190, 640
    body = []
    lx = bar_x
    for cat in CATEGORIES:
        body.append(f'<rect class="c-{cat}" x="{lx}" y="16" width="12" height="12" rx="2"/>')
        body.append(text(lx + 17, 27, cat, "t", 12.5))
        lx += 70
    for i, (label, counts, later) in enumerate(rows):
        y = top + i * row + (10 if (label == TOTAL_LABEL or later) else 0) + (10 if later else 0)
        n = sum(counts[c] for c in CATEGORIES)
        body.append(text(20, y + 15, label, "t b" if label == TOTAL_LABEL else ("t m" if later else "t"), 14 if not later else 13))
        x = bar_x
        for cat in CATEGORIES:
            w = bar_w * counts[cat] / n if n else 0
            if w > 0:
                body.append(f'<rect class="c-{cat}" x="{x:.1f}" y="{y}" width="{w:.1f}" height="22"{' opacity="0.55"' if later else ''}/>')
                if w >= 26:
                    body.append(text(x + w / 2, y + 15.5, str(counts[cat]), "t chip-t num", 11.5, "middle").replace("<text ", '<text opacity="0.7" ', 1) if later else text(x + w / 2, y + 15.5, str(counts[cat]), "t chip-t num", 11.5, "middle"))
            x += w
        body.append(text(bar_x + bar_w + 12, y + 15, f"n = {n}", "t m num", 12.5))
    foot = top + len(rows) * row + 40
    nc = d["narrative_counts"]
    body.append(f'<line class="rule" x1="20" y1="{foot}" x2="940" y2="{foot}"/>')
    body.append(
        text(
            20,
            foot + 22,
            "Share of each cohort's GO claims. COR = supported and absent from the target's existing annotation. Rows marked (later) were reviewed after the snapshot and are not in the total.",
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


TOTAL_LABEL = "All in-snapshot cohorts"

RENDERERS = {"benchmark-funnel": render_funnel, "benchmark-cohorts": render_cohorts, "benchmark-outcomes": render_outcomes}


def render_all(d: dict) -> dict[str, str]:
    """Render every figure from a funnel dict, keyed by file stem."""
    return {name: fn(d) for name, fn in RENDERERS.items()}


@app.command()
def render() -> None:
    """Draw the three SVG figures from benchmark-funnel.json."""
    d = json.loads(FUNNEL_JSON.read_text())
    FIGURES.mkdir(exist_ok=True)
    for name, content in render_all(d).items():
        path = FIGURES / f"{name}.svg"
        path.write_text(content)
        typer.echo(f"Wrote {path}")


if __name__ == "__main__":
    app()
