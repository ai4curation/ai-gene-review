from ai_gene_review.export.browser_payload import compact_browser_row


def test_browser_payload_uses_goref_codename_and_truncates_review_text():
    row = {
        "original_reference_id": "GO_REF:0000117",
        "original_reference_title": "Electronic Gene Ontology annotations created by ARBA machine learning models",
        "review.summary": "S" * 80,
        "review.reason": "R" * 80,
        "review.supporting_text": "kept intact",
        "empty": None,
        "empty_list": [],
    }

    compact = compact_browser_row(row)

    assert compact["original_reference_title"] == "ARBA"
    assert compact["review.summary"] == ("S" * 47) + "..."
    assert compact["review.reason"] == ("R" * 47) + "..."
    assert compact["review.supporting_text"] == "kept intact"
    assert "empty" not in compact
    assert "empty_list" not in compact


def test_browser_payload_truncates_non_goref_reference_titles_to_20_chars():
    row = {
        "original_reference_id": "PMID:12345",
        "original_reference_title": "A very informative publication title",
    }

    compact = compact_browser_row(row)

    assert compact["original_reference_title"] == "A very informativ..."
    assert len(compact["original_reference_title"]) == 20
