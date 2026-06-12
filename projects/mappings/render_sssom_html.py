#!/usr/bin/env python3
"""Render the ARO->GO SSSOM mapping set as a self-contained HTML page for curators.

Produces a table of the GO mappings (with CARD/AmiGO hyperlinks) and a table of the recorded GO
gaps (sssom:NoTermFound). If the annotation-gain candidate TSV is supplied, a "UniProt entries
gaining" count is shown per mapping.

Usage::

    uv run python projects/mappings/render_sssom_html.py \
        --sssom projects/mappings/aro2go.sssom.yaml \
        --gain-tsv projects/mappings/data/candidate_new_annotations.tsv \
        -o projects/mappings/aro2go.html
"""
from __future__ import annotations

import argparse
import csv
import html
from collections import Counter
from datetime import date
from pathlib import Path

import yaml

CARD = "https://card.mcmaster.ca/aro/{num}"
AMIGO = "https://amigo.geneontology.org/amigo/term/{go}"

CSS = """
body{font-family:-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;margin:2rem auto;max-width:1100px;
padding:0 1rem;color:#222;line-height:1.45}
h1{font-size:1.6rem}h2{margin-top:2rem;border-bottom:2px solid #eee;padding-bottom:.3rem}
.summary{background:#f6f8fa;border:1px solid #e1e4e8;border-radius:8px;padding:.8rem 1.1rem;margin:1rem 0}
table{border-collapse:collapse;width:100%;font-size:.92rem;margin:.6rem 0}
th,td{border:1px solid #e1e4e8;padding:.45rem .6rem;text-align:left;vertical-align:top}
th{background:#f6f8fa}tr:nth-child(even){background:#fbfcfd}
code{background:#f3f4f6;padding:.05rem .3rem;border-radius:4px;font-size:.9em}
a{color:#0366d6;text-decoration:none}a:hover{text-decoration:underline}
.rel-exact{color:#1a7f37;font-weight:600}.rel-narrower{color:#9a6700}
.pred{color:#555;font-size:.85em}.gain{text-align:right;font-variant-numeric:tabular-nums}
.muted{color:#666;font-size:.9rem}
"""


def aro_link(aro_id: str, label: str) -> str:
    num = aro_id.split(":")[1]
    return f'<a href="{CARD.format(num=num)}" target="_blank"><code>{html.escape(aro_id)}</code></a> {html.escape(label)}'


def go_link(go_id: str, label: str) -> str:
    return f'<a href="{AMIGO.format(go=go_id)}" target="_blank"><code>{html.escape(go_id)}</code></a> {html.escape(label)}'


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--sssom", type=Path, required=True)
    ap.add_argument("--gain-tsv", type=Path, default=None, help="candidate_new_annotations.tsv (optional)")
    ap.add_argument("-o", "--output", type=Path, required=True)
    args = ap.parse_args(argv)

    doc = yaml.safe_load(args.sssom.read_text())
    mappings = doc.get("mappings", [])
    go_rows = [m for m in mappings if str(m.get("object_id", "")).startswith("GO:")]
    gap_rows = [m for m in mappings if m.get("object_id") == "sssom:NoTermFound"]

    gain_by_aro: Counter = Counter()
    total_candidates = 0
    if args.gain_tsv and args.gain_tsv.exists():
        with args.gain_tsv.open() as fh:
            for r in csv.DictReader(fh, delimiter="\t"):
                gain_by_aro[r["mapped_aro_id"]] += 1
                total_candidates += 1

    show_gain = bool(gain_by_aro)
    parts = [
        "<!doctype html><html lang=en><head><meta charset=utf-8>",
        "<meta name=viewport content='width=device-width,initial-scale=1'>",
        "<title>ARO → GO mappings</title>",
        f"<style>{CSS}</style></head><body>",
        "<h1>ARO → GO mappings (antimicrobial resistance)</h1>",
        f"<p class=muted>Generated {date.today().isoformat()} from "
        "<code>aro2go.sssom.yaml</code>. CARD/ARO ids link to card.mcmaster.ca; GO ids link to AmiGO.</p>",
        "<div class=summary>",
        f"<b>{len(go_rows)}</b> GO mappings &middot; <b>{len(gap_rows)}</b> recorded GO gaps "
        "(no suitable GO term). Propagation is <b>exact-or-narrower</b>: a mapping applies to any gene "
        "whose ARO assignment is the mapped term or a narrower (is_a descendant) ARO term.",
    ]
    if show_gain:
        parts.append(
            f"<br>Applied to UniProt: <b>{total_candidates:,}</b> candidate new GO annotations across "
            "CARD-cross-referenced entries (see <code>ANNOTATION_GAIN.md</code>)."
        )
    parts.append("</div>")

    # Mappings table
    parts.append("<h2>GO mappings</h2><table><thead><tr>"
                 "<th>ARO term</th><th>predicate</th><th>GO term</th>"
                 + ("<th class=gain>UniProt new</th>" if show_gain else "")
                 + "<th>notes</th></tr></thead><tbody>")
    for m in sorted(go_rows, key=lambda r: r["subject_id"]):
        pred = m.get("predicate_label", m["predicate_id"])
        # enables / exactMatch = specific (high confidence); relatedMatch = broader-but-propagatable
        specific = m["predicate_id"] in ("RO:0002327", "skos:exactMatch")
        pred_cls = "rel-exact" if specific else "rel-narrower"
        gain_cell = f"<td class=gain>{gain_by_aro.get(m['subject_id'], 0):,}</td>" if show_gain else ""
        parts.append(
            "<tr>"
            f"<td>{aro_link(m['subject_id'], m.get('subject_label',''))}</td>"
            f"<td><span class='{pred_cls}'>{html.escape(pred)}</span></td>"
            f"<td>{go_link(m['object_id'], m.get('object_label',''))}</td>"
            f"{gain_cell}"
            f"<td>{html.escape(m.get('comment','') or '')}</td>"
            "</tr>"
        )
    parts.append("</tbody></table>")

    # Gaps table
    parts.append("<h2>Recorded GO gaps (new-term-request candidates)</h2>"
                 "<p class=muted>ARO families with no suitable GO molecular-function term, recorded in the "
                 "mapping file via <code>sssom:NoTermFound</code>.</p>"
                 "<table><thead><tr><th>ARO term</th><th>why no mapping</th></tr></thead><tbody>")
    for m in sorted(gap_rows, key=lambda r: r["subject_id"]):
        parts.append(
            f"<tr><td>{aro_link(m['subject_id'], m.get('subject_label',''))}</td>"
            f"<td>{html.escape(m.get('comment','') or '')}</td></tr>"
        )
    parts.append("</tbody></table></body></html>")

    args.output.write_text("\n".join(parts))
    print(f"# wrote {args.output} ({len(go_rows)} mappings, {len(gap_rows)} gaps)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
