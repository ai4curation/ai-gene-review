"""Render functional compliance diagnostics using the production module template."""

from pathlib import Path
from typing import Any, TypedDict

import pytest

from ai_gene_review.render_modules import _environment, collect_module_stats


class FunctionFinding(TypedDict):
    """Structured finding fields consumed by the rendered QC table."""

    annoton_id: str
    participant_id: str | None
    participant_label: str
    function_id: str | None
    function_label: str
    scope: str
    status: str
    severity: str
    message: str


@pytest.fixture
def template_context() -> dict[str, Any]:
    """Provide a minimal module with the existing derived-QC fields."""
    data = {"id": "MODULE:test", "module": {"id": "test", "label": "Test module"}}
    return {
        "data": data,
        "module": data["module"],
        "stats": collect_module_stats(data),
        "anchor_map": {"synthase": "#annoton-synthase"},
        "qc": {
            "data_qc": {"global_compliance": 100, "missing": []},
            "module_deep_research": {"has_deep_research": False},
            "leaf_nodes_missing_representatives": [],
            "conformance_violations": [],
            "gene_reviews": {"with_review": 0, "total_genes": 0, "genes": []},
        },
    }


def render_context(context: dict[str, Any]) -> str:
    """Use the same Jinja environment and template as module page rendering."""
    path = Path("src/ai_gene_review/templates/module.html.j2")
    return _environment(path).get_template(path.name).render(**context)


def test_function_conformance_renders_support_conflicts_and_gaps(
    template_context: dict[str, Any],
) -> None:
    """Keep noncore support, real conflicts, and uncheckable claims distinct."""
    rows: list[FunctionFinding] = [
        {
            "annoton_id": "synthase",
            "participant_id": "UniProtKB:Q0JF02",
            "participant_label": "Rice synthase",
            "function_id": "GO:0003824",
            "function_label": "catalytic activity",
            "scope": "gene",
            "status": "CORE_SUPPORTED",
            "severity": "info",
            "message": "Represented in core functions.",
        },
        {
            "annoton_id": "synthase",
            "participant_id": "UniProtKB:Q0JF02",
            "participant_label": "Family representative",
            "function_id": "GO:0003824",
            "function_label": "catalytic activity",
            "scope": "family_representative",
            "status": "NON_CORE_SUPPORTED",
            "severity": "info",
            "message": "Supported by a retained noncore annotation.",
        },
        {
            "annoton_id": "synthase",
            "participant_id": "UniProtKB:Q0JF02",
            "participant_label": "Conflicting representative",
            "function_id": "GO:0003824",
            "function_label": "catalytic activity",
            "scope": "family_representative",
            "status": "CONTRADICTED",
            "severity": "error",
            "message": "A retained NOT annotation contradicts this function.",
        },
        {
            "annoton_id": "synthase",
            "participant_id": None,
            "participant_label": "Unresolved enzyme family",
            "function_id": None,
            "function_label": "Unresolved function <detail>",
            "scope": "family",
            "status": "NO_FUNCTION_ID",
            "severity": "warning",
            "message": "No function identifier; support cannot be checked.",
        },
    ]
    template_context["qc"]["function_conformance"] = {
        "rows": rows,
        "counts": {row["status"]: 1 for row in rows},
        "total": 4,
        "core_supported": 1,
        "conflicts": 1,
        "gaps": 1,
    }

    html = render_context(template_context)

    assert "Function consistency and core coverage" in html
    assert "1 gene-function check(s) reflected in core functions" in html
    assert "4 comparison(s)" in html
    assert "1 conflict(s)" in html
    assert "1 evidence or coverage gap(s)" in html
    assert 'href="#annoton-synthase"' in html
    assert 'href="https://www.uniprot.org/uniprotkb/Q0JF02/entry"' in html
    assert 'href="https://amigo.geneontology.org/amigo/term/GO:0003824"' in html
    for row in rows:
        assert f'data-status="{row["status"]}"' in html
        assert row["message"] in html
    assert "Non Core Supported" in html
    assert "Family Representative" in html
    assert "Unresolved function &lt;detail&gt;" in html
    assert "No function ID" in html
    assert "whole family" in html


def test_function_conformance_empty_is_not_an_all_clear(
    template_context: dict[str, Any],
) -> None:
    """An empty check set must explain the lack of coverage."""
    template_context["qc"]["function_conformance"] = {
        "rows": [],
        "counts": {},
        "total": 0,
        "core_supported": 0,
        "conflicts": 0,
        "gaps": 0,
    }

    html = render_context(template_context)

    assert "No functional claims were checked." in html
    assert "0 gene-function check(s) reflected in core functions" not in html


def test_function_conformance_is_optional_for_older_qc(
    template_context: dict[str, Any],
) -> None:
    """Older QC dictionaries can still render without the additional field."""
    html = render_context(template_context)

    assert "Derived QC" in html
    assert "Function consistency and core coverage" not in html


@pytest.mark.parametrize(
    "annoton_id,missing_anchor",
    [
        ("synthase:required_function", "#node-synthase-required-function"),
        ("synthase/unit", "#node-synthase-unit"),
        ("unit", "#node-unit"),
    ],
)
def test_function_conformance_does_not_link_unmapped_assertions(
    template_context: dict[str, Any], annoton_id: str, missing_anchor: str
) -> None:
    """Derived constraint/unit identifiers have no rendered target of their own."""
    template_context["qc"]["function_conformance"] = {
        "rows": [
            {
                "annoton_id": annoton_id,
                "participant_id": "UniProtKB:Q0JF02",
                "participant_label": "Rice synthase",
                "function_id": "GO:0003824",
                "function_label": "catalytic activity",
                "scope": "complex_unit",
                "status": "CORE_SUPPORTED",
                "severity": "info",
                "message": "Represented in core functions.",
            }
        ],
        "core_supported": 1,
        "conflicts": 0,
        "gaps": 0,
        "total": 1,
    }

    html = render_context(template_context)

    assert f"<td>{annoton_id}</td>" in html
    assert f'href="{missing_anchor}"' not in html
