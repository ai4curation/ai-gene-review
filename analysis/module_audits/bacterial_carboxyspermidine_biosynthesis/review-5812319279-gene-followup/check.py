"""Read-only checks for the five-gene PR 6089 follow-up; no cache writes."""
import hashlib
import json
import re
import subprocess
from pathlib import Path

import yaml

AUDIT = Path(__file__).resolve().parent
ROOT = AUDIT.parents[3]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def quotes(value, reference=None):
    if isinstance(value, dict):
        reference = value.get("reference_id", reference)
        if "findings" in value:
            reference = value.get("id", reference)
        if value.get("supporting_text"):
            yield reference, value["supporting_text"]
        for child in value.values():
            yield from quotes(child, reference)
    elif isinstance(value, list):
        for child in value:
            yield from quotes(child, reference)


def main():
    before = json.loads((AUDIT / "before.json").read_text())
    row_count = proposal_count = quote_count = 0
    changes = []
    for name, frozen in before["reviews"].items():
        path = ROOT / name
        doc = yaml.safe_load(path.read_text())
        rows = doc["existing_annotations"]
        payloads = [{k: v for k, v in row.items() if k != "review"} for row in rows]
        assert payloads == frozen["ordered_payloads"], name
        row_count += len(rows)
        proposal_count += sum(row["review"]["action"] == "NEW" for row in rows)
        for i, (old, row) in enumerate(zip(frozen["actions"], rows)):
            if old == "NEW":
                assert row["review"]["action"] == "NEW", (name, i)
            if old != row["review"]["action"]:
                changes.append([name, i, old, row["review"]["action"]])
        notes = name.replace("-ai-review.yaml", "-notes.md")
        old_notes = subprocess.check_output(
            ["git", "show", before["head"] + ":" + notes], cwd=ROOT
        )
        assert (ROOT / notes).read_bytes().startswith(old_notes), notes
        for reference, quote in quotes(doc):
            quote_count += 1
            if reference.startswith("PMID:"):
                source = ROOT / "publications" / ("PMID_" + reference[5:] + ".md")
            else:
                assert reference.startswith("file:"), reference
                source = ROOT / "genes" / reference[5:]
                if not source.exists():
                    source = ROOT / reference[5:]
            text = source.read_text()
            candidates = [text]
            if source.name.endswith("-uniprot.txt"):
                candidates.append("\n".join(
                    re.sub(r"^(CC   |DR   |FT   )", "", line)
                    for line in text.splitlines()
                ))
            assert any(" ".join(quote.split()) in " ".join(s.split())
                       for s in candidates), (name, reference, quote)
    for name, digest in before["protected_sources"].items():
        assert sha(ROOT / name) == digest, name
    print(json.dumps({
        "result": "PASS",
        "reviews": len(before["reviews"]),
        "ordered_payloads_preserved": row_count,
        "active_historical_NEW_preserved": proposal_count,
        "retirements_or_added_rows": 0,
        "protected_sources_preserved": len(before["protected_sources"]),
        "quotation_occurrences_checked": quote_count,
        "notes_append_only": True,
        "action_changes": changes,
        "limits": ("Local payload/source/quotation checks; not schema, term, "
                  "reference-title or history validation.")
    }, indent=2))


if __name__ == "__main__":
    main()
