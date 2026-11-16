"""Render GO-CAM reviews (``gocams/<id>/<id>-review.yaml``) to HTML.

Each review gets a page at ``pages/gocams/<id>.html`` showing the reviewer's
reading of the model, one row per reviewed activity (annoton), and any source
defects reported against the model. ``pages/gocams/index.html`` lists every
reviewed model with its verdict counts.

Review files carry bare ids. Labels come from the cached model
(``<id>-src.yaml``), whose ``objects`` list maps each id it uses to a label, so
rendering needs no ontology lookup.
"""

from __future__ import annotations

import re
from collections import Counter
from pathlib import Path
from typing import Any, Optional

import yaml

from ai_gene_review.render_modules import (
    _environment,
    clean_rendered_html,
    relative_href,
)

TEMPLATES_DIR = Path(__file__).parent / "templates"
VERDICTS = ("OK", "UNCERTAIN", "WRONG")
MODEL_ID_PATTERN = re.compile(r"gomodel:([0-9a-f]{16})")


def local_model_id(model: str) -> str:
    """Return the bare local id of a GO-CAM model.

    >>> local_model_id("gomodel:568b0f9600000284")
    '568b0f9600000284'
    >>> local_model_id("568b0f9600000284")
    '568b0f9600000284'
    """
    return model.removeprefix("gomodel:")


def model_iri(model: str) -> str:
    """Return the resolvable IRI of a GO-CAM model.

    >>> model_iri("gomodel:568b0f9600000284")
    'https://model.geneontology.org/568b0f9600000284'
    """
    return f"https://model.geneontology.org/{local_model_id(model)}"


def gene_review_path(reference: Optional[str], genes_dir: Path) -> Optional[Path]:
    """Resolve a ``file:<org>/<gene>/<gene>-ai-review.yaml`` reference.

    The reference is relative to ``genes/``. Returns the YAML path, or None
    when there is no reference.

    >>> gene_review_path("file:worm/tir-1/tir-1-ai-review.yaml", Path("genes"))
    PosixPath('genes/worm/tir-1/tir-1-ai-review.yaml')
    >>> gene_review_path(None, Path("genes")) is None
    True
    """
    if not reference:
        return None
    return genes_dir / reference.removeprefix("file:")


def object_labels(src_path: Path) -> dict[str, str]:
    """Map each id in a cached model's ``objects`` list to its label."""
    if not src_path.is_file():
        return {}
    src = yaml.safe_load(src_path.read_text(encoding="utf-8")) or {}
    return {
        obj["id"]: obj["label"]
        for obj in src.get("objects") or []
        if obj.get("id") and obj.get("label")
    }


def verdict_counts(review: dict[str, Any]) -> dict[str, int]:
    """Count activity verdicts, always reporting OK, UNCERTAIN and WRONG.

    >>> verdict_counts({"activity_reviews": [{"verdict": "OK"}, {"verdict": "WRONG"}, {}]})
    {'OK': 1, 'UNCERTAIN': 0, 'WRONG': 1, 'NONE': 1}
    """
    counts = Counter(
        activity.get("verdict") or "NONE"
        for activity in review.get("activity_reviews") or []
    )
    result = {verdict: counts.pop(verdict, 0) for verdict in VERDICTS}
    result.update(sorted(counts.items()))
    return result


def source_defects(review: dict[str, Any]) -> list[dict[str, Any]]:
    """Collect the source defects of every activity, tagged with the activity id.

    >>> source_defects({"activity_reviews": [
    ...     {"activity_id": "a1", "source_defects": [{"defect_type": "WRONG_REFERENCE"}]},
    ...     {"activity_id": "a2"}]})
    [{'defect_type': 'WRONG_REFERENCE', 'activity_id': 'a1'}]
    """
    return [
        {**defect, "activity_id": activity.get("activity_id")}
        for activity in review.get("activity_reviews") or []
        for defect in activity.get("source_defects") or []
    ]


def modules_by_model(modules_dir: Path) -> dict[str, list[Path]]:
    """Map each local model id to the module YAML files that mention it."""
    index: dict[str, list[Path]] = {}
    if not modules_dir.is_dir():
        return index
    for module_file in sorted(modules_dir.rglob("*.yaml")):
        text = module_file.read_text(encoding="utf-8")
        for model_id in sorted(set(MODEL_ID_PATTERN.findall(text))):
            index.setdefault(model_id, []).append(module_file)
    return index


def iter_review_files(gocams_dir: Path) -> list[Path]:
    """Return every ``<id>/<id>-review.yaml`` under ``gocams_dir``, sorted."""
    return sorted(
        path
        for path in gocams_dir.glob("*/*-review.yaml")
        if path.name == f"{path.parent.name}-review.yaml"
    )


def output_path_for_review(review_path: Path, output_dir: Path) -> Path:
    """Return the HTML page path for a review file.

    >>> output_path_for_review(Path("gocams/abc/abc-review.yaml"), Path("pages/gocams"))
    PosixPath('pages/gocams/abc.html')
    """
    return output_dir / f"{review_path.parent.name}.html"


def _module_title(module_file: Path) -> str:
    data = yaml.safe_load(module_file.read_text(encoding="utf-8")) or {}
    return str(data.get("title") or module_file.stem)


def build_page_context(
    review_path: Path,
    output_path: Path,
    genes_dir: Path,
    modules_dir: Path,
    module_index: dict[str, list[Path]],
    pages_modules_dir: Path,
) -> dict[str, Any]:
    """Assemble the template context for one review page."""
    review = yaml.safe_load(review_path.read_text(encoding="utf-8")) or {}
    model_id = local_model_id(str(review.get("model") or review_path.parent.name))
    labels = object_labels(review_path.parent / f"{model_id}-src.yaml")

    def term(curie: Optional[str]) -> Optional[dict[str, str]]:
        if not curie:
            return None
        return {"id": curie, "label": labels.get(curie, "")}

    activities = []
    for activity in review.get("activity_reviews") or []:
        gene_yaml = gene_review_path(activity.get("gene_review"), genes_dir)
        gene_href = None
        if gene_yaml is not None and gene_yaml.is_file():
            gene_href = relative_href(output_path, gene_yaml.with_suffix(".html"))
        activities.append(
            {
                **activity,
                "gene_product_term": term(activity.get("gene_product")),
                "mf_term": term(activity.get("molecular_function")),
                "bp_term": term(activity.get("biological_process")),
                "cc_term": term(activity.get("cellular_component")),
                "gene_review_href": gene_href,
            }
        )

    modules = []
    for module_file in module_index.get(model_id, []):
        page = pages_modules_dir / module_file.relative_to(modules_dir).with_suffix(
            ".html"
        )
        modules.append(
            {
                "title": _module_title(module_file),
                "href": relative_href(output_path, page),
            }
        )

    return {
        "review": review,
        "model_id": model_id,
        "model_iri": model_iri(model_id),
        "activities": activities,
        "counts": verdict_counts(review),
        "defects": source_defects(review),
        "modules": modules,
        "review_href": relative_href(output_path, review_path),
        "index_href": relative_href(output_path, output_path.parent / "index.html"),
    }


def index_row(context: dict[str, Any], page_href: str) -> dict[str, Any]:
    """Summarise a rendered review page for the index table."""
    review = context["review"]
    activities = context["activities"]
    return {
        "model_id": context["model_id"],
        "title": review.get("title") or context["model_id"],
        "taxon": review.get("taxon") or "",
        "status": review.get("status") or "",
        "href": page_href,
        "activities": len(activities),
        "counts": context["counts"],
        "conflicts": sum(1 for a in activities if a.get("consistency") == "CONFLICT"),
        "defects": len(context["defects"]),
        "modules": len(context["modules"]),
    }


def render_all_gocams(
    gocams_dir: Path = Path("gocams"),
    output_dir: Path = Path("pages/gocams"),
    genes_dir: Path = Path("genes"),
    modules_dir: Path = Path("modules"),
    pages_modules_dir: Path = Path("pages/modules"),
) -> list[Path]:
    """Render a page for every GO-CAM review plus an index; return the paths."""
    env = _environment(TEMPLATES_DIR / "gocam_review.html.j2")
    page_template = env.get_template("gocam_review.html.j2")
    index_template = env.get_template("gocam_index.html.j2")
    module_index = modules_by_model(modules_dir)
    index_path = output_dir / "index.html"

    output_dir.mkdir(parents=True, exist_ok=True)
    for stale in output_dir.glob("*.html"):
        stale.unlink()

    rows = []
    written = []
    for review_path in iter_review_files(gocams_dir):
        output_path = output_path_for_review(review_path, output_dir)
        context = build_page_context(
            review_path,
            output_path,
            genes_dir,
            modules_dir,
            module_index,
            pages_modules_dir,
        )
        output_path.write_text(
            clean_rendered_html(page_template.render(**context)), encoding="utf-8"
        )
        written.append(output_path)
        rows.append(index_row(context, relative_href(index_path, output_path)))

    totals: Counter[str] = Counter()
    for row in rows:
        totals.update(row["counts"])
    index_path.write_text(
        clean_rendered_html(
            index_template.render(
                rows=rows,
                totals={verdict: totals[verdict] for verdict in VERDICTS},
                total_defects=sum(row["defects"] for row in rows),
                cached_models=sum(1 for path in gocams_dir.iterdir() if path.is_dir())
                if gocams_dir.is_dir()
                else 0,
            )
        ),
        encoding="utf-8",
    )
    written.append(index_path)
    return written
