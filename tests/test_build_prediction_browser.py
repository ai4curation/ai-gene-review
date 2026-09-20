"""End-to-end build checks for the static, locally browsable prediction catalog."""

import json
from pathlib import Path
import shutil
import subprocess

import pytest

from ai_gene_review.tools.build_prediction_browser import build_prediction_browser


def read_browser_payload(path: Path) -> dict:
    """Execute the shipped script to check the same object the browser consumes."""
    node = shutil.which("node")
    if not node:
        pytest.skip("Node is needed to execute the generated browser payload")
    script = "global.window = {};\n" + path.read_text() + "\nprocess.stdout.write(JSON.stringify(window.predictionData));"
    result = subprocess.run([node, "-"], input=script, text=True, capture_output=True, check=True)
    return json.loads(result.stdout)


def test_build_preserves_empty_outputs_and_complete_evidence(tmp_path: Path) -> None:
    """Build from real sidecars, retaining zero outputs and untruncated rationale."""
    directory = tmp_path / "genes/DROME/Dic4"
    directory.mkdir(parents=True)
    (directory / "Dic4-protnlm-predictions-review.yaml").write_text(
        "gene_symbol: Dic4\nid: QTEST1\nstatus: COMPLETE\n"
        "predictions: []\ndescription: No GO predictions in this source snapshot.\n"
    )
    other = tmp_path / "genes/ECOLI/test"
    other.mkdir(parents=True)
    reason = "An evidence-based rationale that must survive the browser export. " * 8
    (other / "test-predictions-review.yaml").write_text(
        "gene_symbol: test\nid: QTEST2\nstatus: COMPLETE\n"
        "predictions:\n- source_method: DeepECTF\n  source_version: test-run\n"
        "  predicted_term: {id: 'EC:1.1.1.1', label: alcohol dehydrogenase}\n"
        "  predicted_term_type: EC\n  review:\n    assessment: COR\n"
        "    confidence_score: 2\n    summary: " + reason + "\n"
    )
    output = tmp_path / "app/predictions"

    result = build_prediction_browser(tmp_path, output)

    content = (output / "data.js").read_text()
    data = read_browser_payload(output / "data.js")
    assert len(data["sets"]) == 2
    assert len(data["claims"]) == 1
    assert any(row["claim_count"] == 0 for row in data["sets"])
    assert reason.strip() in content
    assert result["sets"] == 2
    assert result["claims"] == 1
    assert "data.js" in (output / "index.html").read_text()
    assert "window.predictionData" in (output / "schema.js").read_text()
    sources = json.loads((output / "source-files.json").read_text())
    assert "genes/DROME/Dic4/Dic4-protnlm-predictions-review.yaml" in sources
    assert all((tmp_path / path).is_file() for path in sources)

    first_build = {path.name: path.read_bytes() for path in output.iterdir()}
    build_prediction_browser(tmp_path, output)
    assert first_build == {path.name: path.read_bytes() for path in output.iterdir()}


def test_compact_payload_preserves_values_and_distinguishes_absent_fields(tmp_path: Path) -> None:
    """Compact repeated keys without truncating text, changing nulls, or pooling scores."""
    from ai_gene_review.tools.build_prediction_browser import encode_prediction_data_js

    records = [
        {"gene_symbol": "α-test", "claim_count": 0, "summary": 'Quoted "text"\nnext line', "optional": None},
        {"gene_symbol": "beta", "claim_count": None, "summary": "full text", "performance_included": False},
    ] * 100
    data = {"sets": records, "claims": [], "metadata": {"schema_version": 1}}
    encoded = encode_prediction_data_js(data)
    path = tmp_path / "data.js"
    path.write_text(encoded)
    assert read_browser_payload(path) == data
    assert len(encoded) < len(json.dumps(data, separators=(",", ":"))) * 0.7
