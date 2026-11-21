"""Read-only verification of the four full reviews and two bounded comparator edits.

Run from repository root with uv run python <this path>.
The two baseline documents were captured before scientific edits.
"""
from collections import Counter
from hashlib import sha256
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[4]
AUDIT = Path(__file__).resolve().parent


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def main():
    originals = yaml.safe_load((AUDIT.parent / "baseline.yaml").read_text())
    comparators = yaml.safe_load((AUDIT / "yeast-baseline.yaml").read_text())
    result = yaml.safe_load((AUDIT / "preservation.yaml").read_text())
    reviews = originals["reviews"] | comparators["reviews"]
    sources = originals["protected_sha256"] | comparators["protected_sha256"]
    rows = 0
    for path, baseline in reviews.items():
        doc = yaml.safe_load((ROOT / path).read_text())
        annotations = doc["existing_annotations"]
        payloads = [{k: v for k, v in row.items() if k != "review"} for row in annotations]
        assert payloads == baseline["annotation_payloads"], path
        assert digest(ROOT / path) == result["reviews"][path]["current_review_sha256"], path
        assert dict(Counter(a["review"]["action"] for a in annotations)) == result["reviews"][path]["actions"]
        if path in originals["reviews"]:
            assert doc["status"] == "COMPLETE", path
        else:
            assert doc["status"] == result["reviews"][path]["status"], path
        for index, action in enumerate(baseline.get("actions", [])):
            if action == "NEW":
                assert annotations[index]["review"]["action"] == action, (path, index)
        rows += len(payloads)
    for path, expected in sources.items():
        assert digest(ROOT / path) == expected, path
    for path, expected in result["new_publications_sha256"].items():
        assert digest(ROOT / path) == expected, path
    assert rows == 86
    assert len(sources) == 29
    print(f"PASS: {len(reviews)} reviews, {rows} original ordered payloads, {len(sources)} protected sources; no added rows.")


if __name__ == "__main__":
    main()
