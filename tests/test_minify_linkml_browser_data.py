import json

import pytest

from ai_gene_review.export.browser_payload import (
    DATA_JS_ASSIGNMENT_PREFIX,
    DATA_JS_READY_EVENT,
    encode_browser_data_js,
)
from ai_gene_review.export.annotation_export import AnnotationExporter
from ai_gene_review.tools.minify_linkml_browser_data import minify_data_js


def raw_data_js(data: object) -> str:
    return (
        f"{DATA_JS_ASSIGNMENT_PREFIX}{json.dumps(data, indent=2)};\n"
        f"{DATA_JS_READY_EVENT}\n"
    )


def test_minifier_writes_columnar_data_and_is_idempotent(tmp_path):
    data = [
        {
            "gene_symbol": "GENE1",
            "review.summary": "S" * 80,
            "unused": None,
        },
        {
            "gene_symbol": "GENE2",
            "review.supporting_text": "verbatim evidence",
        },
    ]
    path = tmp_path / "data.js"
    path.write_text(raw_data_js(data), encoding="utf-8")

    size = minify_data_js(path)

    assert path.read_text(encoding="utf-8") == encode_browser_data_js(data)
    assert size == path.stat().st_size
    assert minify_data_js(path) == size


def test_minifier_checks_final_encoded_size_at_conservative_boundary(tmp_path):
    data = [
        {
            "gene_symbol": f"GENE{index}",
            "review.supporting_text": "verbatim evidence",
        }
        for index in range(100)
    ]
    raw = raw_data_js(data)
    encoded_size = len(encode_browser_data_js(data).encode("utf-8"))
    assert len(raw.encode("utf-8")) > encoded_size

    passing_path = tmp_path / "passing-data.js"
    passing_path.write_text(raw, encoding="utf-8")
    assert minify_data_js(passing_path, max_bytes=encoded_size + 1) == encoded_size

    failing_path = tmp_path / "failing-data.js"
    failing_path.write_text(raw, encoding="utf-8")
    with pytest.raises(
        ValueError,
        match=rf"{encoded_size:,} bytes.*{encoded_size:,} bytes",
    ):
        minify_data_js(failing_path, max_bytes=encoded_size)

    assert failing_path.read_text(encoding="utf-8") == raw


def test_direct_exporter_uses_the_same_columnar_writer(tmp_path, monkeypatch):
    data = [
        {"gene_symbol": "GENE1", "review.summary": "accepted"},
        {"gene_symbol": "GENE2", "review.supporting_text": "evidence"},
    ]
    exporter = AnnotationExporter()
    monkeypatch.setattr(exporter, "export_from_files", lambda _paths: data)
    path = tmp_path / "nested" / "data.js"

    count = exporter.export_to_datajs([], path)

    assert count == len(data)
    assert path.read_text(encoding="utf-8") == encode_browser_data_js(data)
