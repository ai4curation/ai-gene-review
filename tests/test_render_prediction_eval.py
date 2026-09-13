from ai_gene_review.render_prediction_eval import render_prediction_eval


def test_render_prediction_eval_has_no_trailing_whitespace():
    html = render_prediction_eval(
        [
            {
                "id": "P0A6Y8",
                "gene_symbol": "DnaK",
                "taxon": {"label": "Escherichia coli"},
                "predictions": [],
            }
        ]
    )

    assert html.endswith("\n")
    assert all(line == line.rstrip() for line in html.splitlines())
