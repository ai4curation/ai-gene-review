"""Render the site's landing pages for feedback to resources and for rules.

``pages/feedback/`` collects what this repository sends back to other
resources: proposed ontology changes and new terms, source-record defects,
mapping reviews and rule reviews. Its reports come from the existing exporters
(``export_source_defects``, ``export_ontology_changes``,
``export_proposed_terms``), so the published pages and the TSVs that are sent
upstream are the same data.

``pages/rules/index.html`` lists the annotation rules curated here
(``rules/curated/CR-*.yaml``) beside the reviews of external rules.

Project membership is read from project frontmatter, never listed here: the
``OBSOLETION`` tag selects ontology-change projects and the ``MAPPINGS``
collection selects mapping reviews.
"""

from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path
from typing import Any

import markdown
import yaml

from ai_gene_review.render_modules import _environment, clean_rendered_html
from ai_gene_review.render_projects import collect_project_rows, load_collections
from ai_gene_review.tools import (
    export_ontology_changes,
    export_proposed_terms,
    export_source_defects,
)

TEMPLATES_DIR = Path(__file__).parent / "templates"
OBSOLETION_TAG = "OBSOLETION"
MAPPINGS_COLLECTION = "MAPPINGS"
#: Report states that need no further action, as in ``export_source_defects``.
CLOSED_DEFECTS = ("FIXED", "DECLINED")


def projects_where(projects_dir: Path, key: str, value: str) -> list[dict[str, Any]]:
    """Return top-level projects whose frontmatter list ``key`` contains ``value``.

    Rows come from :func:`collect_project_rows` (slug, title, maturity, ...),
    sorted by title.
    """
    rows = [
        row
        for row in collect_project_rows(projects_dir)
        if value in (row.get(key) or [])
    ]
    return sorted(rows, key=lambda row: str(row["title"]).lower())


def collection_members(projects_dir: Path, collection: str) -> list[dict[str, Any]]:
    """Return a collection's member projects, without the collection's own index page."""
    index = load_collections(projects_dir)[collection]["index"]
    return [
        project
        for project in projects_where(projects_dir, "collections", collection)
        if project["slug"] != index
    ]


def markdown_page(source: Path, title: str, back_href: str, env: Any) -> str:
    """Wrap a generated Markdown report in the site's page template."""
    body = markdown.markdown(
        source.read_text(encoding="utf-8"), extensions=["tables", "fenced_code"]
    )
    html = env.get_template("hub_report.html.j2").render(
        title=title, body=body, back_href=back_href
    )
    return clean_rendered_html(html)


def defect_summary(rows: list[dict[str, str]]) -> list[dict[str, Any]]:
    """Summarise source-defect rows per resource: open count, by confidence.

    >>> rows = [
    ...     {"resource": "UNIPROT", "report_status": "NOT_REPORTED", "confidence": "CONFIRMED"},
    ...     {"resource": "UNIPROT", "report_status": "FIXED", "confidence": "PROBABLE"},
    ...     {"resource": "MGI", "report_status": "", "confidence": "SUSPECTED"},
    ... ]
    >>> [(s["resource"], s["open"], s["total"]) for s in defect_summary(rows)]
    [('UNIPROT', 1, 2), ('MGI', 1, 1)]
    """
    by_resource: dict[str, list[dict[str, str]]] = {}
    for row in rows:
        by_resource.setdefault(row["resource"], []).append(row)
    summary = []
    for resource, subset in by_resource.items():
        open_rows = [r for r in subset if r["report_status"] not in CLOSED_DEFECTS]
        summary.append(
            {
                "resource": resource,
                "total": len(subset),
                "open": len(open_rows),
                "confidence": Counter(r["confidence"] or "UNSTATED" for r in open_rows),
            }
        )
    return sorted(summary, key=lambda s: (-s["total"], s["resource"]))


def _write(path: Path, html: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding="utf-8")
    return path


def render_feedback(
    root: Path = Path("."),
    output_dir: Path = Path("pages/feedback"),
) -> list[Path]:
    """Render the feedback landing page, its reports and TSV downloads."""
    env = _environment(TEMPLATES_DIR / "feedback_index.html.j2")
    written: list[Path] = []

    defects_dir = output_dir / "source-defects"
    defect_rows = export_source_defects.write_outputs(
        root, output_dir / "source-defects.tsv", defects_dir
    )
    for report in sorted(defects_dir.glob("*.md")):
        written.append(
            _write(
                report.with_suffix(".html"),
                markdown_page(
                    report, f"Source defects: {report.stem}", "../index.html", env
                ),
            )
        )

    changes_dir = output_dir / "ontology-changes"
    change_rows = export_ontology_changes.write_outputs(
        root, output_dir / "ontology-changes.tsv", changes_dir
    )
    ontologies = []
    for ontology in sorted({row["ontology"] for row in change_rows}):
        subset = [row for row in change_rows if row["ontology"] == ontology]
        for kind in ("requests", "inbound"):
            report = changes_dir / f"{ontology}-{kind}.md"
            written.append(
                _write(
                    report.with_suffix(".html"),
                    markdown_page(
                        report,
                        f"{ontology} ontology changes: {kind}",
                        "../index.html",
                        env,
                    ),
                )
            )
        ontologies.append(
            {
                "ontology": ontology,
                "total": len(subset),
                "outbound": sum(export_ontology_changes.is_outbound(r) for r in subset),
                "inbound": sum(export_ontology_changes.is_inbound(r) for r in subset),
            }
        )

    terms_tsv = output_dir / "proposed-new-terms.tsv"
    # expand_inputs falls back to paths relative to the working directory when
    # given no inputs, so pass only the directories that exist under root.
    term_inputs = [d for d in (root / "genes", root / "modules") if d.is_dir()]
    export_proposed_terms.export_proposed_terms(
        export_proposed_terms.expand_inputs(term_inputs) if term_inputs else [],
        terms_tsv,
    )
    with terms_tsv.open(encoding="utf-8", newline="") as handle:
        terms = list(csv.DictReader(handle, delimiter="\t"))
    written.append(
        _write(
            output_dir / "proposed-new-terms.html",
            clean_rendered_html(
                env.get_template("proposed_terms.html.j2").render(terms=terms)
            ),
        )
    )

    projects_dir = root / "projects"
    written.append(
        _write(
            output_dir / "index.html",
            clean_rendered_html(
                env.get_template("feedback_index.html.j2").render(
                    defects=defect_summary(defect_rows),
                    open_defects=sum(
                        r["report_status"] not in CLOSED_DEFECTS for r in defect_rows
                    ),
                    ontologies=ontologies,
                    terms=len(terms),
                    term_reviews=len({t["source_path"] for t in terms}),
                    obsoletion_projects=projects_where(
                        projects_dir, "tags", OBSOLETION_TAG
                    ),
                    mapping_projects=collection_members(
                        projects_dir, MAPPINGS_COLLECTION
                    ),
                    mapping_index=load_collections(projects_dir)[MAPPINGS_COLLECTION][
                        "index"
                    ],
                    rule_reviews=len(list(root.glob("rules/arba/*/*-review.yaml"))),
                )
            ),
        )
    )
    return written


def curated_rules(rules_dir: Path) -> list[dict[str, Any]]:
    """Load the curated rules (``CR-*.yaml``) with the fields the index shows."""
    rules = []
    for path in sorted(rules_dir.glob("CR-*.yaml")):
        rule = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        rules.append(
            {
                "id": rule.get("id") or path.stem,
                "title": rule.get("title") or "",
                "status": rule.get("status") or "",
                "path": path,
                "replaces": rule.get("replaces") or [],
                "consequents": rule.get("go_annotations") or [],
                "gene_reviews": len(rule.get("gene_reviews") or []),
            }
        )
    return rules


def render_rules(
    root: Path = Path("."),
    output_dir: Path = Path("pages/rules"),
) -> Path:
    """Render the rules landing page."""
    env = _environment(TEMPLATES_DIR / "rules_hub.html.j2")
    index = output_dir / "index.html"
    rules = curated_rules(root / "rules" / "curated")
    for rule in rules:
        rule["href"] = Path("../..", rule["path"].relative_to(root)).as_posix()
    return _write(
        index,
        clean_rendered_html(
            env.get_template("rules_hub.html.j2").render(
                rules=rules,
                arba_reviews=len(list(root.glob("rules/arba/*/*-review.yaml"))),
                unirule_reviews=len(list(root.glob("rules/unirule/*/*-review.yaml"))),
                has_function_requirements=(
                    root / "projects" / "FUNCTION_REQUIREMENT_RULES.md"
                ).is_file(),
            )
        ),
    )
