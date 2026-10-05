"""A core function with a proposed MF (no GO term yet) still shows its activity."""

from pathlib import Path

from bs4 import BeautifulSoup

from ai_gene_review.render import enrich_gene_data, render_html

TEMPLATE = (
    Path(__file__).parents[1] / "src/ai_gene_review/templates/gene_review.html.j2"
)


def _core_function_term_rows(core_function: dict) -> list[str]:
    data = enrich_gene_data({"gene_symbol": "TEST", "core_functions": [core_function]})
    soup = BeautifulSoup(render_html(data, TEMPLATE), "html.parser")
    return [
        group.get_text(" ", strip=True)
        for group in soup.select(".core-function-terms .function-term-group")
    ]


def test_proposed_molecular_function_is_rendered_as_proposed() -> None:
    rows = _core_function_term_rows(
        {
            "description": "Holds unfolded clients",
            "proposed_molecular_function": "holdase chaperone activity",
        }
    )
    assert rows == ["Molecular Function: holdase chaperone activity (proposed)"]


def test_go_molecular_function_still_rendered() -> None:
    rows = _core_function_term_rows(
        {
            "description": "Folds clients",
            "molecular_function": {"id": "GO:0044183", "label": "protein folding chaperone"},
        }
    )
    assert rows == ["Molecular Function: protein folding chaperone"]


def test_contributes_to_molecular_function_is_rendered() -> None:
    rows = _core_function_term_rows(
        {
            "description": "Positions a complex",
            "contributes_to_molecular_function": {
                "id": "GO:0044183",
                "label": "protein folding chaperone",
            },
        }
    )
    assert rows == ["Contributes To MF: protein folding chaperone"]
