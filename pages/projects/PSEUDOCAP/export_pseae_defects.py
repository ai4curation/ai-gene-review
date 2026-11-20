"""Write the PseudoCAP project's upstream defect reports.

Collects the ``source_defects`` recorded in the *P. aeruginosa* PAO1 gene
reviews (``genes/PSEAE``) and writes one Markdown report per resource into
``projects/PSEUDOCAP/defects/``, using the repository's own exporter so the
format matches ``just export-source-defects``.

Usage::

    uv run python projects/PSEUDOCAP/export_pseae_defects.py
"""

from __future__ import annotations

from pathlib import Path

from ai_gene_review.tools.export_source_defects import collect, render_report

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent / "defects"


def main() -> None:
    rows = [r for r in collect(ROOT) if r["source_path"].startswith("genes/PSEAE/")]
    OUT.mkdir(exist_ok=True)
    for old in OUT.glob("*.md"):
        old.unlink()
    for resource in sorted({r["resource"] for r in rows}):
        subset = [r for r in rows if r["resource"] == resource]
        (OUT / f"{resource}.md").write_text(render_report(resource, subset), encoding="utf-8")
        print(f"{resource}: {len(subset)}")


if __name__ == "__main__":
    main()
