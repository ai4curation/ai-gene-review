"""Read-only exact preservation and production-circuit equivalence checks."""

import copy
import hashlib
import itertools
import json
from pathlib import Path

import yaml
from ai_gene_review.module_logic import compile_module, is_satisfied, iter_atoms

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
MOD = "modules/bacterial_gallate_catabolism.yaml"
CAND = "genes/BURL3/Bcep18194_C7570/Bcep18194_C7570-ai-review.yaml"
SOURCE = "file:analysis/module_audits/bacterial_gallate_catabolism/review-20261107/publisher-evidence.md"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def normalized(text):
    return " ".join(text.split())


def verify():
    baseline = json.loads((HERE / "baseline.json").read_text())
    documents = {
        p: yaml.safe_load((ROOT / p).read_text()) for p in baseline["documents"]
    }
    rows = new_rows = retired = 0
    changed_reviews = []
    for path, old in baseline["documents"].items():
        if path == MOD:
            continue
        before, after = old["document"], documents[path]
        if before != after:
            changed_reviews.append(path)
        assert len(before["existing_annotations"]) == len(after["existing_annotations"])
        for i, (a, b) in enumerate(
            zip(before["existing_annotations"], after["existing_annotations"])
        ):
            assert {k: v for k, v in a.items() if k != "review"} == {
                k: v for k, v in b.items() if k != "review"
            }, (path, i)
            expected = (
                "UNDECIDED"
                if path == CAND and a["term"]["id"] == "GO:0019748"
                else a["review"]["action"]
            )
            assert b["review"]["action"] == expected, (path, i)
            rows += 1
            if a["review"]["action"] == "NEW":
                assert a == b, (path, i)
                new_rows += 1
                retired += bool(a.get("retired"))
        a, b = copy.deepcopy(before), copy.deepcopy(after)
        if path.startswith("genes/PSEPK/"):
            assert b["references"][-1]["id"] == SOURCE
            b["references"].pop()
            ar = next(r for r in a["references"] if r["id"] == "PMID:21219457")
            br = next(r for r in b["references"] if r["id"] == "PMID:21219457")
            assert br["reference_review"]["review_notes"].startswith(
                ar["reference_review"]["review_notes"]
            )
            br["reference_review"]["review_notes"] = ar["reference_review"][
                "review_notes"
            ]
            if "/galP/" in path:
                for i in (0, 2):
                    assert (
                        b["existing_annotations"][i]["review"]["supported_by"].pop()[
                            "reference_id"
                        ]
                        == SOURCE
                    )
                assert (
                    b["core_functions"][0]["supported_by"].pop()["reference_id"]
                    == SOURCE
                )
        elif path == CAND:
            ar, br = (
                a["existing_annotations"][3]["review"],
                b["existing_annotations"][3]["review"],
            )
            assert a["existing_annotations"][3]["term"]["id"] == "GO:0019748"
            assert "proposed_replacement_terms" not in br
            ar.pop("proposed_replacement_terms")
            for field in ("action", "reason", "summary"):
                ar.pop(field)
                br.pop(field)
            assert (
                br["supported_by"]
                .pop()["reference_id"]
                .endswith("burkholderia-consultation.ontology.json")
            )
            assert (
                b["references"]
                .pop()["id"]
                .endswith("burkholderia-consultation.ontology.json")
            )
        elif "/ligK/" in path:
            a["suggested_questions"][0].pop("question")
            b["suggested_questions"][0].pop("question")
        assert a == b, path
    original = baseline["documents"][MOD]["document"]
    current = documents[MOD]
    archived = json.loads((HERE / "galp-model-archive.json").read_text())
    assert archived["optional_part"] == original["module"]["parts"][0]
    assert archived["connection"] == original["module"]["connections"][0]
    a, b = copy.deepcopy(original), copy.deepcopy(current)
    a["module"]["parts"].pop(0)
    a["module"]["connections"].pop(0)
    for field in ("description", "notes"):
        a.pop(field)
        b.pop(field)
    a["knowledge_gaps"][0].pop("boundary")
    b["knowledge_gaps"][0].pop("boundary")
    for pmid in ("PMID:31075306", "PMID:38064205"):
        ar = next(r for r in a["references"] if r["id"] == pmid)
        br = next(r for r in b["references"] if r["id"] == pmid)
        assert ar["reference_review"]["relevance"] == "HIGH"
        assert br["reference_review"]["relevance"] == "MEDIUM"
        ar["reference_review"]["relevance"] = "MEDIUM"
    assert b["references"].pop()["id"] == SOURCE
    assert a == b, "Unexpected module science delta"
    old_circuit, new_circuit = compile_module(original), compile_module(current)
    old_atoms = {x.node_id for x in iter_atoms(old_circuit)}
    new_atoms = {x.node_id for x in iter_atoms(new_circuit)}
    assert old_atoms - new_atoms == {"galp_outer_membrane_porin"}
    assert len(new_atoms) == 6
    comparisons = 0
    for flags in itertools.product((False, True), repeat=len(new_atoms)):
        active = {name for name, flag in zip(sorted(new_atoms), flags) if flag}
        expected = is_satisfied(new_circuit, lambda atom: atom.node_id in active)
        for galp in (False, True):
            actual = is_satisfied(
                old_circuit,
                lambda atom: atom.node_id in active
                or (galp and atom.node_id == "galp_outer_membrane_porin"),
            )
            assert actual == expected, (active, galp)
            comparisons += 1
    for group in ("protected_sources", "prior_artifacts"):
        for path, expected in baseline[group].items():
            assert sha(ROOT / path) == expected, path
    for path, old in baseline["notes"].items():
        assert (ROOT / path).read_text().startswith(old["text"].rstrip() + "\n\n"), path
    provenance_path = (
        ROOT
        / "analysis/module_audits/bacterial_gallate_catabolism/review-20261107/publisher-provenance.json"
    )
    provenance = json.loads(provenance_path.read_text())
    assert sha(ROOT / provenance["excerpt_path"]) == provenance["excerpt_sha256"]
    private_capture = ROOT / provenance["capture_path"]
    capture_check = "unavailable private capture; durable excerpt/provenance checked"
    if private_capture.exists():
        assert sha(private_capture) == provenance["capture_sha256"]
        capture_check = (
            "local private capture hash verified; never a durable source dependency"
        )
    source = (ROOT / provenance["excerpt_path"]).read_text()
    quote_count = 0

    def walk(value):
        nonlocal quote_count
        if isinstance(value, dict):
            if value.get("reference_id") == SOURCE and "supporting_text" in value:
                assert normalized(value["supporting_text"]) in normalized(source)
                quote_count += 1
            if value.get("id") == SOURCE:
                for finding in value.get("findings", []):
                    assert normalized(finding["supporting_text"]) in normalized(source)
                    quote_count += 1
            for item in value.values():
                walk(item)
        elif isinstance(value, list):
            for item in value:
                walk(item)

    for doc in documents.values():
        walk(doc)
    histories = json.loads((HERE / "histories.json").read_text())
    assert len(histories) == 10
    for path in histories:
        record = yaml.safe_load((ROOT / path).read_text())
        assert record["session"]["actors"][0]["name"] == "codex"
        assert (ROOT / record["target"]["path"]).exists()
    return {
        "status": "PASS",
        "review_count": len(documents) - 1,
        "original_ordered_rows_preserved": rows,
        "historical_NEW_preserved": new_rows,
        "historical_retired_preserved": retired,
        "new_rows_added": 0,
        "changed_reviews": changed_reviews,
        "source_files_preserved": len(baseline["protected_sources"]),
        "prior_artifacts_preserved": len(baseline["prior_artifacts"]),
        "history_count": len(histories),
        "bounded_quote_uses_verified": quote_count,
        "capture_check": capture_check,
        "production_compiler_checks": {
            "remaining_catalytic_atoms": 6,
            "exhaustive_old_new_comparisons": comparisons,
            "meaning": "Removing the optional porin preserves required catalytic satisfiability for every Boolean assignment; this is not a new biological capacity proof.",
        },
        "action_change": {
            "gene": "BURL3/Bcep18194_C7570",
            "row": 3,
            "term": "GO:0019748",
            "before": "MODIFY",
            "after": "UNDECIDED",
            "withdrawn_replacement": "GO:0019396",
        },
        "limits": [
            "The historical seven-atom coverage checker is preserved but must receive an additive six-atom successor before rerunning.",
            "Reaction identity still requires the existing explicit chemistry gate; native same-strain flux is not implied by a synthetic KA1/SYK-6 panel.",
            "No render, full validation, source refresh or download.",
        ],
    }


if __name__ == "__main__":
    print(json.dumps(verify(), indent=2))
