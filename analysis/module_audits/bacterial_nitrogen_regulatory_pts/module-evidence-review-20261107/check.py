"""Read-only verification of the independent draft-review snapshot."""
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    inputs = json.loads((HERE / "inputs.json").read_text())
    failures = []
    for path, digest in inputs.items():
        source = ROOT / path
        if not source.is_file() or sha(source) != digest:
            failures.append(path)
    ledger = json.loads((HERE / "source-ledger.json").read_text())
    quotations = 0
    for item in ledger:
        quote = item.get("quote")
        if quote:
            text = (ROOT / item["path"]).read_text()
            assert " ".join(quote.split()) in " ".join(text.split()), item["id"]
            quotations += 1
    inventory = json.loads((HERE / "citation-inventory.json").read_text())
    for item in inventory:
        assert (ROOT / item["path"]).is_file(), item
    seal = HERE / "handoff.json"
    if seal.exists():
        for path, digest in json.loads(seal.read_text())["files"].items():
            assert sha(ROOT / path) == digest, path
    assert not failures, failures
    assert not any(re.search(r"(?:^|/)__pycache__/|\.pyc$", p) for p in inputs)
    print(json.dumps({"status": "PASS", "inputs": len(inputs),
                      "module_citations": len(ledger), "quotes": quotations,
                      "explicit_PMIDs": len(inventory),
                      "scope": "independent draft review; not final publication closure"}, indent=2))


if __name__ == "__main__":
    main()
