#!/usr/bin/env python3
"""Render the ARO->GO SSSOM mapping set as a self-contained HTML page for curators.

The page explains how a row propagates (which ARO relation it follows), shows for every GO row how
many CARD-cross-referenced UniProt entries it reaches and how many would gain a new annotation,
says why a row yields zero, and states the CARD/ARO release each row was checked against. Gap rows
(``sssom:NoTermFound``) are listed with links to the drafted GO term requests.

Usage::

    uv run python projects/ANTIMICROBIAL_RESISTANCE/render_sssom_html.py \
        --sssom projects/ANTIMICROBIAL_RESISTANCE/aro2go.sssom.yaml \
        --stats projects/ANTIMICROBIAL_RESISTANCE/data/mapping_row_stats.tsv \
        -o projects/ANTIMICROBIAL_RESISTANCE/aro2go.html
"""
from __future__ import annotations

import csv
import html
import re
import sys
from pathlib import Path

import typer
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from aro_release import DEFAULT_CACHE, AroOntology, Release  # noqa: E402

CARD = "https://card.mcmaster.ca/aro/{num}"
AMIGO = "https://amigo.geneontology.org/amigo/term/{go}"
REPO_BLOB = "https://github.com/ai4curation/ai-gene-review/blob/main/projects/ANTIMICROBIAL_RESISTANCE/"
REQUEST_RE = re.compile(r"go_term_requests/([a-z0-9-]+)\.md")

CSS = """
:root{--fg:#222;--muted:#666;--bg:#fff;--panel:#f6f8fa;--line:#e1e4e8;--link:#0366d6;--ok:#1a7f37;--warn:#9a6700}
@media (prefers-color-scheme: dark){:root{--fg:#e6e6e6;--muted:#a0a0a0;--bg:#161b22;--panel:#1f262e;
--line:#30363d;--link:#58a6ff;--ok:#3fb950;--warn:#d29922}}
body{font-family:-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;margin:2rem auto;max-width:1150px;
padding:0 1rem;color:var(--fg);background:var(--bg);line-height:1.45}
h1{font-size:1.6rem}h2{margin-top:2rem;border-bottom:2px solid var(--line);padding-bottom:.3rem}
.summary{background:var(--panel);border:1px solid var(--line);border-radius:8px;padding:.8rem 1.1rem;margin:1rem 0}
.tablewrap{overflow-x:auto}
table{border-collapse:collapse;width:100%;font-size:.9rem;margin:.6rem 0}
th,td{border:1px solid var(--line);padding:.45rem .6rem;text-align:left;vertical-align:top}
th{background:var(--panel)}
code{background:var(--panel);padding:.05rem .3rem;border-radius:4px;font-size:.9em}
a{color:var(--link);text-decoration:none}a:hover{text-decoration:underline}
.enables{color:var(--ok);font-weight:600}.related{color:var(--warn)}
.num{text-align:right;font-variant-numeric:tabular-nums}.muted{color:var(--muted);font-size:.9rem}
.why{color:var(--muted);font-size:.85em}
"""


def aro_link(aro_id: str, label: str) -> str:
    num = aro_id.split(":")[1]
    return f'<a href="{CARD.format(num=num)}" target="_blank"><code>{html.escape(aro_id)}</code></a> {html.escape(label)}'


def go_link(go_id: str, label: str) -> str:
    return f'<a href="{AMIGO.format(go=go_id)}" target="_blank"><code>{html.escape(go_id)}</code></a> {html.escape(label)}'


def propagation_axis(onto: AroOntology, subject: str) -> str:
    """How a row on ``subject`` reaches genes: ``participates_in`` for mechanism terms, else ``is_a``.

    A term is on the mechanism axis when some ARO term has a participates_in edge into it or into
    one of its is_a descendants.

    >>> from aro_release import MINI_OBO
    >>> onto = AroOntology.from_obo_text(MINI_OBO)
    >>> propagation_axis(onto, "ARO:10"), propagation_axis(onto, "ARO:2")
    ('participates_in', 'is_a')
    """
    mechanism_targets: set[str] = set()
    for targets in onto.participates_in.values():
        for t in targets:
            mechanism_targets |= onto.isa_ancestors_or_self(t)
    return "participates_in" if subject in mechanism_targets else "is_a"


def why_zero(stats: dict[str, int]) -> str:
    """Explain a row's counts in words.

    >>> why_zero({"matched": 0, "new": 0, "already": 0, "redundant": 0})
    'no CARD-cross-referenced UniProt entry reaches this term (or a more specific mapped term gives the same GO term)'
    >>> why_zero({"matched": 48, "new": 0, "already": 48, "redundant": 0})
    'all 48 matched entries already carry the GO term'
    >>> why_zero({"matched": 5, "new": 0, "already": 0, "redundant": 5})
    'all 5 matched entries already carry a more specific GO term'
    >>> why_zero({"matched": 9, "new": 4, "already": 5, "redundant": 0})
    ''
    """
    if stats["new"]:
        return ""
    if not stats["matched"]:
        return (
            "no CARD-cross-referenced UniProt entry reaches this term "
            "(or a more specific mapped term gives the same GO term)"
        )
    if stats["already"] == stats["matched"]:
        return f"all {stats['matched']} matched entries already carry the GO term"
    if stats["redundant"] == stats["matched"]:
        return f"all {stats['matched']} matched entries already carry a more specific GO term"
    return f"the {stats['matched']} matched entries already carry the term or a more specific one"


def read_stats(path: Path) -> dict[tuple[str, str], dict[str, int]]:
    with path.open(newline="") as fh:
        return {
            (r["subject_id"], r["object_id"]): {k: int(r[k]) for k in ("matched", "new", "already", "redundant")}
            for r in csv.DictReader(fh, delimiter="\t")
        }


def main(
    sssom: Path = typer.Option(..., help="ARO->GO SSSOM mapping file"),
    stats: Path = typer.Option(..., help="mapping_row_stats.tsv from annotation_gain_report.py --out-stats"),
    output: Path = typer.Option(..., "-o", "--output"),
    aro_cache: Path = typer.Option(DEFAULT_CACHE, help="Fetched CARD release (just fetch-aro)"),
) -> None:
    """Render aro2go.sssom.yaml as a curator-facing HTML page."""
    release = Release(aro_cache)
    release.require()
    onto = AroOntology.from_obo(release.obo)
    doc = yaml.safe_load(sssom.read_text())
    mappings = doc["mappings"]
    go_rows = [m for m in mappings if str(m["object_id"]).startswith("GO:")]
    gap_rows = [m for m in mappings if m["object_id"] == "sssom:NoTermFound"]
    row_stats = read_stats(stats)
    checked_against = doc["subject_source_version"]
    total_new = sum(v["new"] for v in row_stats.values())
    reviewed = sum(1 for m in mappings if m.get("reviewer_label"))

    parts = [
        "<!doctype html><html lang=en><head><meta charset=utf-8>",
        "<meta name=viewport content='width=device-width,initial-scale=1'>",
        "<title>ARO to GO mappings</title>",
        f"<style>{CSS}</style></head><body>",
        "<h1>ARO → GO mappings (antimicrobial resistance)</h1>",
        f"<p class=muted>Mapping set version {html.escape(str(doc['mapping_set_version']))}, generated from "
        f"<a href='{REPO_BLOB}aro2go.sssom.yaml'><code>aro2go.sssom.yaml</code></a>. Every ARO id and label "
        f"was checked against <b>{html.escape(checked_against)}</b> (<code>just check-aro-release</code>); "
        "every GO id and label by <code>just validate-mappings</code>. ARO ids link to CARD, GO ids to AmiGO.</p>",
        "<div class=summary>",
        f"<b>{len(go_rows)}</b> GO mapping rows &middot; <b>{len(gap_rows)}</b> recorded GO gaps &middot; "
        f"<b>{reviewed}</b> rows reviewed by the CARD curation team &middot; <b>{total_new:,}</b> candidate new "
        "GO annotations for UniProt entries with a CARD cross-reference "
        f"(<a href='ANNOTATION_GAIN.html'>annotation-gain report</a>; "
        f"<a href='FAMILY_COVERAGE.html'>coverage of every CARD AMR gene family</a>).",
        "</div>",
        "<h2>How propagation works</h2>",
        "<p>A mapping row is asserted on one ARO term and applies to genes (determinant terms) below it. "
        "ARO joins the two kinds of term that rows are written on by different relations, so propagation "
        "follows two paths:</p><ul>",
        "<li><b>Gene families</b> (e.g. <code>ARO:3000001</code> beta-lactamase) apply to the family and "
        "every <code>is_a</code> descendant: CTX-M-15 is_a CTX-M beta-lactamase is_a … beta-lactamase. "
        "Reported as <code>exact</code> or <code>narrower</code>.</li>",
        "<li><b>Resistance mechanisms</b> (e.g. <code>ARO:0001004</code> antibiotic inactivation) are not "
        "ancestors of any gene. A family is linked to a mechanism by <code>participates_in</code> "
        "(RO:0000056), and mechanisms nest by <code>is_a</code>, so a mechanism row applies to every gene "
        "that reaches it by <code>is_a* ∘ participates_in ∘ is_a*</code>. Reported as "
        "<code>participates_in</code>. Until 2026-11-27 only the first path was implemented, so every "
        "mechanism row reached zero genes; the CARD team pointed this out.</li></ul>",
        "<p>Other ARO relations are deliberately not followed: <code>confers_resistance_to_antibiotic</code> "
        "and <code>confers_resistance_to_drug_class</code> point to the drug (a chemical), "
        "<code>part_of</code>/<code>has_part</code> join complex subunits and gene clusters, and the "
        "regulation relations join regulators to their targets. None of them makes a gene a member of a "
        "mapped family or a participant in a mapped mechanism.</p>",
        "<p>When several mapped terms give the same GO term to an entry, the entry is credited to the most "
        "specific one (exact, then narrower, then participates_in). That is one reason a row can show "
        "zero; the other is that the entries it reaches already carry the term. Each row says which.</p>",
        "<p><b>enables</b> rows (green) claim every family member has the activity; <b>related match</b> "
        "rows (amber) are broader or cover a minority of members that may differ. Candidate annotations "
        "are leads for curators, not assertions.</p>",
        "<h2>GO mapping rows</h2><div class=tablewrap><table><thead><tr>"
        "<th>ARO term</th><th>propagates along</th><th>predicate</th><th>GO term</th><th class=num>conf.</th>"
        "<th class=num>entries matched</th><th class=num>new</th><th>reviewed by</th><th>justification</th>"
        "</tr></thead><tbody>",
    ]
    for m in sorted(go_rows, key=lambda r: (propagation_axis(onto, r["subject_id"]), r["subject_id"], r["object_id"])):
        st = row_stats[(m["subject_id"], m["object_id"])]
        pred_cls = "enables" if m["predicate_id"] == "RO:0002327" else "related"
        why = why_zero(st)
        parts.append(
            "<tr>"
            f"<td>{aro_link(m['subject_id'], m['subject_label'])}</td>"
            f"<td><code>{propagation_axis(onto, m['subject_id'])}</code></td>"
            f"<td><span class='{pred_cls}'>{html.escape(m['predicate_label'])}</span></td>"
            f"<td>{go_link(m['object_id'], m['object_label'])}</td>"
            f"<td class=num>{m['confidence']:.2f}</td>"
            f"<td class=num>{st['matched']:,}</td>"
            f"<td class=num>{st['new']:,}" + (f"<div class=why>{html.escape(why)}</div>" if why else "") + "</td>"
            f"<td>{html.escape(', '.join(m.get('reviewer_label') or [])) or '—'}</td>"
            f"<td>{html.escape(m.get('comment') or '')}</td>"
            "</tr>"
        )
    parts.append("</tbody></table></div>")

    parts.append(
        "<h2>Recorded GO gaps</h2><p class=muted>ARO families with no suitable GO molecular-function term, "
        "recorded with <code>sssom:NoTermFound</code>. Where a request has been drafted it is linked; drafts "
        "are not filed.</p><div class=tablewrap><table><thead><tr><th>ARO term</th><th>reviewed by</th>"
        "<th>why no mapping</th><th>GO term request</th></tr></thead><tbody>"
    )
    for m in sorted(gap_rows, key=lambda r: r["subject_id"]):
        comment = m.get("comment") or ""
        match = REQUEST_RE.search(comment)
        request = f"<a href='go_term_requests/{match.group(1)}.html'>draft</a>" if match else "—"
        parts.append(
            f"<tr><td>{aro_link(m['subject_id'], m['subject_label'])}</td>"
            f"<td>{html.escape(', '.join(m.get('reviewer_label') or [])) or '—'}</td>"
            f"<td>{html.escape(comment)}</td><td>{request}</td></tr>"
        )
    parts.append("</tbody></table></div>")
    parts.append(
        f"<h2>Review history</h2><p>{html.escape(doc.get('comment', ''))}</p>"
        "<p class=muted>Where the curated mapping should live and how it should track ARO releases is "
        "discussed in <a href='MAPPING_HOME_OPTIONS.html'>the options note</a>.</p></body></html>"
    )
    output.write_text("\n".join(parts) + "\n")
    typer.echo(f"# wrote {output} ({len(go_rows)} mappings, {len(gap_rows)} gaps)")


if __name__ == "__main__":
    typer.run(main)
