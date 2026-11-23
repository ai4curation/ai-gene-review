"""Verify immutable original rows/sources, proposal lifecycle, and current quotations."""

import hashlib
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[4]
OUT = Path(__file__).resolve().parent
AUDIT = OUT.parent


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path):
    return yaml.safe_load(path.read_text())


def walk(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)


def normalized(text):
    return " ".join(text.split())


def source_path(reference):
    if reference.startswith("PMID:"):
        return ROOT / ("publications/PMID_" + reference.split(":")[1] + ".md")
    if reference.startswith("file:"):
        relative = reference.removeprefix("file:")
        gene = ROOT / "genes" / relative
        return gene if gene.exists() else ROOT / relative
    return None


def main():
    baseline = load(AUDIT / "baseline.yaml")
    before = load(OUT / "before.yaml")
    rows = 0
    proposals = 0
    genes = []
    quote_count = 0
    quoted_sources = {}
    for name, prior in before["reviews"].items():
        current = load(ROOT / name)
        original = prior["document"]
        payload = [
            {k: v for k, v in row.items() if k != "review"}
            for row in current["existing_annotations"]
        ]
        assert payload == baseline["existing_annotation_rows"][name], name
        assert len(payload) == len(original["existing_annotations"])
        assert current["status"] == "COMPLETE", name
        actions = Counter()
        for i, annotation in enumerate(current["existing_annotations"]):
            action = annotation["review"]["action"]
            actions[action] += 1
            if original["existing_annotations"][i]["review"]["action"] == "NEW":
                assert action == "NEW"
                assert annotation.get("retired") == original["existing_annotations"][
                    i
                ].get("retired")
                proposals += 1
        quoted_objects = list(walk(current))
        for ref in current.get("references", []):
            for finding in ref.get("findings", []):
                if finding.get("supporting_text"):
                    quoted_objects.append({**finding, "reference_id": ref["id"]})
        for obj in quoted_objects:
            quote = obj.get("supporting_text")
            reference = obj.get("reference_id") or obj.get("id")
            if not quote or not reference:
                continue
            path = source_path(reference)
            assert path and path.exists(), (name, reference)
            assert not path.name.endswith("-goa.tsv"), (name, reference)
            text = path.read_text()
            # UniProt uses a two-letter tag on each wrapped line.
            if path.name.endswith("-uniprot.txt"):
                text += "\n" + "\n".join(
                    line[5:] if len(line) > 5 and line[2:5] == "   " else line
                    for line in text.splitlines()
                )
            assert normalized(quote) in normalized(text), (name, reference, quote)
            quoted_sources[str(path.relative_to(ROOT))] = sha(path)
            quote_count += 1
        rows += len(payload)
        genes.append(
            {
                "path": name,
                "rows": len(payload),
                "actions": dict(actions),
                "sha256": sha(ROOT / name),
            }
        )
    for path, expected in before["protected"].items():
        assert sha(ROOT / path) == expected, path
    supplemental = load(OUT / "supplemental-originals.yaml")
    for path, expected in supplemental["protected_sources_and_old_histories"].items():
        assert sha(ROOT / path) == expected, path
    for path, evidence in supplemental["append_only_notes"].items():
        prefix = (ROOT / path).read_bytes()[: evidence["original_bytes"]]
        assert hashlib.sha256(prefix).hexdigest() == evidence["original_sha256"], path
    readonly_rows = 0
    for name in [
        "genes/ECOLI/iscS/iscS-ai-review.yaml",
        "genes/PSEPK/iscS/iscS-ai-review.yaml",
    ]:
        current = load(ROOT / name)
        payload = [
            {k: v for k, v in row.items() if k != "review"}
            for row in current["existing_annotations"]
        ]
        assert payload == baseline["existing_annotation_rows"][name]
        readonly_rows += len(payload)
    report = {
        "result": "PASS",
        "owned_reviews": len(genes),
        "owned_original_rows": rows,
        "owned_historical_NEW_active": proposals,
        "added_rows": 0,
        "retired_rows": 0,
        "readonly_IscS_reviews": 2,
        "readonly_IscS_rows": readonly_rows,
        "all_eight_original_rows": rows + readonly_rows,
        "protected_sources_and_readonly_reviews": len(before["protected"]),
        "protected_sha256": before["protected"],
        "additional_original_sources_and_histories": supplemental[
            "protected_sources_and_old_histories"
        ],
        "append_only_notes_verified": len(supplemental["append_only_notes"]),
        "review_supported_by_quotes": quote_count,
        "quoted_source_sha256": quoted_sources,
        "genes": genes,
        "paint_limit": "All six target accessions are absent from their cached PAINT trees; no lineage loss check was possible, despite the command's generic concluding message.",
        "provider_attempts": "Six actual Falcon attempts failed403; no generated report fabricated.",
    }
    (OUT / "preservation.yaml").write_text(
        yaml.safe_dump(report, sort_keys=False, width=100)
    )
    print(
        f"PASS: {len(genes)} reviews, {rows} owned rows, {proposals} historical NEW, {readonly_rows} read-only IscS rows, {quote_count} quotations"
    )


if __name__ == "__main__":
    main()
