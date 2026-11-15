"""Bounded Kdp family reconciliation: exact original identities and source protection."""

import hashlib
import json
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[4]
AUDIT = Path(__file__).resolve().parent
BASE = json.loads((AUDIT / "baseline.json").read_text())
ARCHIVE = json.loads((AUDIT / "historical-scope.json").read_text())


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def without(data, fields):
    return {key: value for key, value in data.items() if key not in fields}


TOP = {
    "PTHR30607": {"notes", "reviewed_by", "review_date"},
    "PTHR43743": {"notes", "reviewed_by", "review_date", "coherence_reason"},
    "PTHR30042": {"notes", "reviewed_by", "review_date", "summary"},
    "PTHR45569": {
        "notes",
        "reviewed_by",
        "review_date",
        "summary",
        "preferred_name",
        "coherence_reason",
    },
    "PTHR48111": {"notes", "reviewed_by", "review_date"},
}
NODE_CHANGES = {
    ("PTHR30042", "GO:0008556"): ("UNRESOLVED", "SOUND"),
    ("PTHR45569", "GO:0005886"): ("SOUND", "UNRESOLVED"),
}
SCOPE_CHANGES = {
    ("PTHR30042", "GO:0008556"): ("UNRESOLVED", "FAMILY_WIDE"),
    ("PTHR45569", "GO:0000155"): ("FAMILY_WIDE", "UNRESOLVED"),
    ("PTHR45569", "GO:0000160"): ("FAMILY_WIDE", "UNRESOLVED"),
    ("PTHR48111", "GO:0055075"): ("SUBFAMILY_ONLY", "UNRESOLVED"),
}
NODE_REASON = {
    ("PTHR30042", "GO:0008556"),
    ("PTHR45569", "GO:0000155"),
    ("PTHR45569", "GO:0005886"),
}
TERM_REASON = set(SCOPE_CHANGES) | {("PTHR30607", "GO:0008556")}
NODE_APPEND = NODE_REASON | {
    (fam, term)
    for fam in ("PTHR30607", "PTHR43743")
    for term in ("GO:0008556", "GO:0071805")
}
TERM_APPEND = {
    ("PTHR30607", "GO:0008556"),
    ("PTHR43743", "GO:0008556"),
    ("PTHR30042", "GO:0008556"),
    ("PTHR45569", "GO:0000155"),
    ("PTHR45569", "GO:0000160"),
}
ledger = []
node_count = 0
term_count = 0
root_baseline = json.loads((AUDIT.parent / "baseline.json").read_text())
for filename, old in BASE["families"].items():
    assert old == root_baseline["families"][filename]["document"], filename
    new = yaml.safe_load((ROOT / filename).read_text())
    fam = old["family_id"].split(":")[1]
    fields = TOP[fam] | {"references", "node_assessments", "term_assessments"}
    assert without(old, fields) == without(new, fields), filename
    assert new["references"][: len(old["references"])] == old["references"]
    for kind, id_field, allowed_reason, allowed_append in (
        ("node_assessments", "asserted_term", NODE_REASON, NODE_APPEND),
        ("term_assessments", "assessed_term", TERM_REASON, TERM_APPEND),
    ):
        assert len(old[kind]) == len(new[kind]), (filename, kind)
        for index, (before, after) in enumerate(zip(old[kind], new[kind])):
            key = fam, before[id_field]["id"]
            assert before[id_field] == after[id_field]
            allowed = set()
            if key in allowed_reason:
                allowed.add(
                    "assessment_reason"
                    if kind == "node_assessments"
                    else "scope_reason"
                )
            if key in allowed_append:
                allowed.add("supported_by")
                original_support = before.get("supported_by", [])
                assert (
                    after["supported_by"][: len(original_support)] == original_support
                )
                assert len(after["supported_by"]) > len(original_support)
            changes = NODE_CHANGES if kind == "node_assessments" else SCOPE_CHANGES
            action = "assessment" if kind == "node_assessments" else "scope"
            if key in changes:
                allowed.add(action)
                assert (before[action], after[action]) == changes[key]
                ledger.append(
                    {
                        "family": fam,
                        "section": kind,
                        "index": index,
                        "term": key[1],
                        "old": before[action],
                        "new": after[action],
                    }
                )
            if kind == "term_assessments" and key == ("PTHR45569", "GO:0000155"):
                allowed.add("member_exceptions")
                assert ARCHIVE["PTHR45569_GO0000155"] == before
                assert "member_exceptions" not in after
                for exception in before["member_exceptions"]:
                    accession = exception["member"]["id"].split(":")[1]
                    assert accession in after["scope_reason"]
            if kind == "term_assessments" and key == ("PTHR48111", "GO:0055075"):
                allowed.add("applicable_subfamilies")
                assert ARCHIVE["PTHR48111_GO0055075"] == before
                assert "applicable_subfamilies" not in after
            assert without(before, allowed) == without(after, allowed), (
                filename,
                kind,
                index,
            )
    node_count += len(old["node_assessments"])
    term_count += len(old["term_assessments"])
    for reference in new["references"]:
        if reference["id"].startswith("PMID:"):
            pmid = reference["id"].split(":")[1]
            text = (ROOT / f"publications/PMID_{pmid}.md").read_text()
            metadata = yaml.safe_load(text.split("---")[1])
            assert reference["title"] == metadata["title"], (fam, pmid)

for filename, digest in BASE["protected"].items():
    assert sha(ROOT / filename) == digest, filename
receipt = json.loads((AUDIT / "source-receipt.json").read_text())
for filename, digest in receipt["receipt_sources"].items():
    assert sha(ROOT / filename) == digest, filename

# Check every newly appended quotation against the actual protected source or analysis.
for filename, old in BASE["families"].items():
    new = yaml.safe_load((ROOT / filename).read_text())
    for section in ("node_assessments", "term_assessments"):
        for before, after in zip(old[section], new[section]):
            for support in after.get("supported_by", [])[
                len(before.get("supported_by", [])) :
            ]:
                reference = support["reference_id"]
                if reference.startswith("PMID:"):
                    source = ROOT / (
                        "publications/PMID_" + reference.split(":")[1] + ".md"
                    )
                else:
                    assert reference.startswith("file:"), reference
                    source = ROOT / reference[5:]
                source_text = re.sub(r"\s+", " ", source.read_text())
                quote = re.sub(r"\s+", " ", support["supporting_text"])
                assert quote in source_text, (filename, reference, quote)
psepk = json.loads(
    (
        ROOT / ".cache/module-audit-logs/kdp-20261107/psepk-consultation/handoff.json"
    ).read_text()
)
for filename, digest in psepk["files"].items():
    assert sha(ROOT / filename) == digest, filename

# Independently verify the reviewed members' current official classification snapshots.
for accession, length in {"P73870": 370, "Q725T9": 379, "Q1J2K3": 365}.items():
    record = json.loads((AUDIT / f"{accession}.json").read_text())
    assert record["primaryAccession"] == accession
    assert record["sequence"]["length"] == length
    crossrefs = record["uniProtKBCrossReferences"]
    assert any(
        row["database"] == "PANTHER" and row["id"] == "PTHR45569:SF1"
        for row in crossrefs
    )
    assert not any(row["type"] == "Transmembrane" for row in record.get("features", []))

result = {
    "families": len(BASE["families"]),
    "ordered_nodes": node_count,
    "ordered_term_assessments": term_count,
    "protected_original_sources": len(BASE["protected"]),
    "prior_psepk_handoff_files_unchanged": len(psepk["files"]),
    "original_support_prefixes_and_seed_payloads_preserved": True,
    "unrelated_nodes_and_scopes_exact": True,
    "historical_exception_and_selector_objects_exact": True,
    "scope_and_verdict_changes": ledger,
}
print(json.dumps(result, indent=2))
