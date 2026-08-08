import json
import shutil
import subprocess

import pytest

from ai_gene_review.export.browser_payload import (
    DATA_JS_ASSIGNMENT_PREFIX,
    DATA_JS_READY_EVENT,
    columnar_browser_rows,
    compact_browser_row,
    compact_browser_rows,
    encode_browser_data_js,
)


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


def test_columnar_browser_rows_round_trip_compacted_objects():
    data = [
        {
            "gene_symbol": "GÉNE1",
            "count": 0,
            "enabled": False,
            "__proto__": {"polluted": True},
            "constructor": "safe",
            "nested": {"values": [None, []]},
            "empty_string": "",
            "optional": None,
            "empty_list": [],
        },
        {
            "gene_symbol": "GENE2",
            "review.supporting_text": "verbatim evidence",
        },
    ]

    columns, rows = columnar_browser_rows(data)
    reconstructed = [
        {
            columns[index]: value
            for index, value in enumerate(row)
            if value is not None
        }
        for row in rows
    ]

    assert reconstructed == compact_browser_rows(data)
    assert rows[0][-1] == ""
    assert rows[1][columns.index("review.supporting_text")] == "verbatim evidence"


def test_columnar_browser_rows_handles_empty_datasets_and_rows():
    assert columnar_browser_rows([]) == ([], [])
    assert columnar_browser_rows([{}]) == ([], [[]])


def test_encoded_browser_data_retains_legacy_fallback_for_non_row_data():
    data = {"message": "héllo"}

    assert encode_browser_data_js(data) == (
        f"{DATA_JS_ASSIGNMENT_PREFIX}"
        '{"message":"héllo"};\n'
        f"{DATA_JS_READY_EVENT}\n"
    )


def test_encoded_browser_data_uses_one_shared_copy_of_each_column_name():
    data = [
        {
            "gene_symbol": f"GENE{index}",
            "review.supporting_text": "searchable evidence",
        }
        for index in range(100)
    ]
    encoded = encode_browser_data_js(data)
    compact = compact_browser_rows(data)
    row_oriented = (
        f"{DATA_JS_ASSIGNMENT_PREFIX}"
        f"{json.dumps(compact, separators=(',', ':'))};\n"
        f"{DATA_JS_READY_EVENT}\n"
    )

    assert encoded.count('"gene_symbol"') == 1
    assert encoded.count('"review.supporting_text"') == 1
    assert len(encoded.encode("utf-8")) < len(row_oriented.encode("utf-8"))


def test_encoded_browser_data_reconstructs_objects_before_ready_event():
    node = shutil.which("node")
    if node is None:
        pytest.skip("Node.js is required to execute the generated browser payload")

    data = [
        {
            "gene_symbol": "GÉNE1",
            "count": 0,
            "enabled": False,
            "__proto__": {"polluted": True},
            "constructor": "safe",
            "nested": {"values": [None, []]},
            "empty_string": "",
            "optional": None,
            "empty_list": [],
        },
        {
            "gene_symbol": "GENE2",
            "review.supporting_text": "verbatim evidence",
        },
    ]
    script = (
        "global.window=globalThis;"
        "global.Event=class Event{constructor(type){this.type=type}};"
        "const events=[];"
        "window.dispatchEvent=event=>events.push({"
        "type:event.type,rowCount:window.searchData.length});"
        f"{encode_browser_data_js(data)}"
        "process.stdout.write(JSON.stringify({"
        "data:window.searchData,events,"
        "ordinaryPrototype:Object.getPrototypeOf(window.searchData[0])"
        "===Object.prototype,"
        "prototypePolluted:Boolean(({}).polluted)}));"
    )

    result = subprocess.run(
        [node, "-e", script],
        check=True,
        capture_output=True,
        text=True,
    )
    output = json.loads(result.stdout)

    assert output["data"] == compact_browser_rows(data)
    assert output["events"] == [
        {"type": "searchDataReady", "rowCount": len(data)}
    ]
    assert output["ordinaryPrototype"] is True
    assert output["prototypePolluted"] is False
