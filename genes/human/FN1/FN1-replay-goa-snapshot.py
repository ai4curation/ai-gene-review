"""Verify FN1's additive TSV using the repository exporter, entirely offline.

Run from the repository root with its existing environment:
    python genes/human/FN1/FN1-replay-goa-snapshot.py

The archived QuickGO objects are the input, never the authored review. This
replays their projection; it does not authenticate the upstream service or
reconstruct the extension fields omitted by the TSV format. Nothing is written.
"""

from contextlib import redirect_stdout
import hashlib
import io
import json
from pathlib import Path
from unittest.mock import patch

from ai_gene_review.etl.gene import fetch_goa_data


def verify_snapshot(directory: Path) -> dict:
    archive = json.loads((directory / "FN1-source-contexts.json").read_text())
    contexts = archive["current_quickgo_original_contexts"]
    if [item["raw_index"] for item in contexts] != list(range(222)):
        raise ValueError("Expected the 222 archived source objects in original order")
    raw = [item["object"] for item in contexts]
    if any(row["geneProductId"] != "UniProtKB:P02751" or row["taxonId"] != 9606
           for row in raw):
        raise ValueError("Archived source target identity differs from human FN1")
    snapshots = [item for item in archive["source_snapshots"]
                 if item["kind"] == "current_quickgo_repository_projection"]
    if len(snapshots) != 1:
        raise ValueError("Expected exactly one additive projection record")
    snapshot = snapshots[0]
    if snapshot["filename"] != "FN1-goa-20261031.tsv":
        raise ValueError("Unexpected additive snapshot filename")

    class Response:
        def __init__(self, results):
            self.results = results

        def raise_for_status(self):
            pass

        def json(self):
            return {"numberOfHits": len(raw), "results": self.results}

    def archived_response(url, *, params, headers, timeout):
        expected = [
            ("geneProductId", "UniProtKB:P02751"),
            ("includeFields", "goName"), ("includeFields", "taxonName"),
            ("includeFields", "name"), ("limit", "200"),
        ]
        page = dict(params).get("page", "1")
        if page == "2":
            expected.append(("page", "2"))
        if (url != "https://www.ebi.ac.uk/QuickGO/services/annotation/search"
                or params != expected or page not in ("1", "2")
                or headers != {"Accept": "application/json"} or timeout != 30):
            raise ValueError("Exporter request contract changed; inspect before replay")
        return Response(raw[:200] if page == "1" else raw[200:])

    # Only the HTTP response boundary is replaced. Sorting, projection and
    # byte-identical TSV deduplication remain the genuine repository code.
    with patch("ai_gene_review.etl.gene.requests.get", side_effect=archived_response) as request:
        with redirect_stdout(io.StringIO()):
            projected = fetch_goa_data("UniProtKB:P02751").encode("utf-8")
    if request.call_count != 2:
        raise ValueError("Exporter did not consume both archived response pages")
    actual = (directory / snapshot["filename"]).read_bytes()
    digest = hashlib.sha256(actual).hexdigest()
    if (actual != projected or actual != snapshot["text"].encode("utf-8")
            or len(actual) != snapshot["bytes"] or digest != snapshot["sha256"]
            or len(actual.splitlines()) - 1 != snapshot["data_row_count"]):
        raise ValueError("Additive snapshot differs from archived raw projection or recorded bytes")
    return {"raw_contexts": len(raw), "tsv_rows": len(actual.splitlines()) - 1,
            "sha256": digest, "network_requests": 0, "files_written": 0}


if __name__ == "__main__":
    print(json.dumps(verify_snapshot(Path(__file__).resolve().parent), indent=2))
