"""Verify round-one source preservation and rerun the independent capacity oracle.

The original published checker and receipts remain immutable. Exact proposed
chemistry can satisfy its GO-genus consistency check only when its named proposal,
definition, parent and evidence match; independent member evidence still controls
whether the reaction is established.
"""

import argparse
import copy
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import re
import subprocess
import tarfile

import yaml

from ai_gene_review.validation.local_source_text import quote_matches, resolve_local_source
from ai_gene_review.validation.supporting_text import build_supporting_text_validator

HERE = Path(__file__).resolve().parent
AUDIT = HERE.parent
ROOT = HERE.parents[3]
BASELINE = HERE / "baseline.json"
OLD = AUDIT / "capacity/audit_capacity.py"
PROPOSAL = {
    "proposed_name": "3-dehydrocarnitine:acetyl-CoA trimethylamine transferase activity",
    "proposed_definition": "Catalysis of the reaction: 3-dehydrocarnitine + acetyl-CoA = N,N,N-trimethylglycyl-CoA + acetoacetate.",
    "parent": "GO:0016747",
    "supporting_reference": "file:PSEAE/cdhC/cdhC-uniprot.txt",
    "supporting_text": "Reaction=3-dehydrocarnitine + acetyl-CoA = N,N,N-trimethylglycyl-CoA + acetoacetate;",
}
CHANGED_GENES = {
    "RHIME/bcoG", "RHIME/bcoE-bcoF", "PSEPK/PP_0303", "PSEAE/cbcV", "PSEAE/cbcW"
}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def historical_bytes(baseline):
    """Compare published audit receipts and preexisting histories to Git objects."""
    prefixes = [str(AUDIT.relative_to(ROOT)),
                "history/modules/bacterial_l_carnitine_catabolism"]
    prefixes += ["history/genes/" + gene for gene in sorted(CHANGED_GENES)]
    # Only ask git-archive for paths that existed at publication; new histories remain additive.
    names = subprocess.check_output(
        ["git", "ls-tree", "-r", "--name-only", baseline["head"], "--", *prefixes],
        cwd=ROOT, text=True).splitlines()
    assert names and str(OLD.relative_to(ROOT)) in names
    blob = subprocess.check_output(["git", "archive", baseline["head"], "--", *names], cwd=ROOT)
    verified = {}
    with tarfile.open(fileobj=io.BytesIO(blob)) as archive:
        for member in archive.getmembers():
            if not member.isfile():
                continue
            expected = hashlib.sha256(archive.extractfile(member).read()).hexdigest()
            assert digest(ROOT / member.name) == expected, (member.name, "published historical bytes changed")
            verified[member.name] = expected
    return verified



def module_quote_preservation(baseline):
    """Only six occurrences of three approved quote expansions may differ."""
    current = yaml.safe_load((ROOT / "modules/bacterial_l_carnitine_catabolism.yaml").read_text())
    prior = copy.deepcopy(baseline["module"])
    expected = {
        "The first catabolic step is catalysed by": "The first catabolic step is catalysed by the L-(-)-carnitine dehydrogenase.",
        "Carnitine can be transported into the cell or acquired from": "Carnitine can be transported into the cell or acquired from metabolic precursors, where it can serve directly as a compatible solute for stress protection or be metabolized through one of a few distinct pathways as a nutrient source.",
        "the GB intermediate represents a": "In these choline catabolizers, the GB intermediate represents a metabolic decision point to determine whether GB is catabolized or stored as an osmo- and stress protectant.",
    }
    validator, _ = build_supporting_text_validator(ROOT / "publications")
    changes = []

    def visit(value, reference=None, path=""):
        if isinstance(value, dict):
            reference = value.get("source_id") or value.get("reference_id") or reference
            if value.get("id", "").startswith("PMID:"):
                reference = value["id"]
            quote = value.get("supporting_text")
            if quote in expected:
                replacement = expected[quote]
                result = validator.validate(replacement, reference)
                assert result.is_valid and not result.skipped, (path, result)
                changes.append({"path": path + "/supporting_text", "reference": reference,
                                "before": quote, "after": replacement})
                value["supporting_text"] = replacement
            for key, child in value.items():
                visit(child, reference, path + "/" + key)
        elif isinstance(value, list):
            for index, child in enumerate(value):
                visit(child, reference, path + "/" + str(index))
    visit(prior)
    assert len(changes) == 6
    assert prior == current, "Module changed beyond the six approved quotation occurrences"
    return changes


def current_preservation():
    baseline = json.loads(BASELINE.read_text())
    retirements = {
        ("genes/RHIME/bcoG/bcoG-ai-review.yaml", "GO:0016747"),
        ("genes/RHIME/bcoE-bcoF/bcoE-bcoF-ai-review.yaml", "GO:0042413"),
    }
    assert len(baseline["published_closure_sha256"]) == 255
    historical = historical_bytes(baseline)
    quote_changes = module_quote_preservation(baseline)
    identities = {}
    for path, term in retirements:
        matches = [(i, row) for i, row in enumerate(baseline["reviews"][path]["document"]["existing_annotations"])
                   if row["term"]["id"] == term and row["review"]["action"] == "NEW"]
        assert len(matches) == 1, (path, term, "retirement identity ambiguous")
        index, row = matches[0]
        identities[(path, index)] = term
    seen = set()
    counts = {"reviews": 0, "ordered_rows": 0, "historical_NEW": 0, "active_NEW": 0}
    actions = []
    for path, prior in baseline["reviews"].items():
        before = prior["document"]
        now = yaml.safe_load((ROOT / path).read_text())
        assert now["status"] == "COMPLETE", path
        assert (before["id"], before["taxon"]) == (now["id"], now["taxon"]), path
        old_rows, new_rows = before["existing_annotations"], now["existing_annotations"]
        assert len(old_rows) == len(new_rows), path
        counts["reviews"] += 1
        for index, (old, new) in enumerate(zip(old_rows, new_rows, strict=True)):
            counts["ordered_rows"] += 1
            payload = {k: copy.deepcopy(v) for k, v in new.items() if k != "review"}
            original = {k: v for k, v in old.items() if k != "review"}
            key = (path, old["term"]["id"])
            if (path, index) in identities:
                assert not old.get("retired") and payload.pop("retired") is True, key
                seen.add(key)
            assert payload == original, (path, index, "source payload changed")
            action = new["review"]["action"]
            assert action != "PENDING" and new["review"].get("reason"), (path, index)
            if old["review"]["action"] == "NEW":
                assert action == "NEW", (path, index, "historical proposal lost")
                counts["historical_NEW"] += 1
                counts["active_NEW"] += not new.get("retired", False)
            else:
                assert action != "NEW", (path, index, "new proposal manufactured")
            if action != old["review"]["action"]:
                actions.append({"path": path, "index": index, "before": old["review"]["action"], "after": action})
    assert seen == retirements
    assert counts == {"reviews": 14, "ordered_rows": 146, "historical_NEW": 11, "active_NEW": 6}, counts
    for path, expected in baseline["protected_sources_sha256"].items():
        assert digest(ROOT / path) == expected, path
    for path, prior in baseline["families"].items():
        expected = prior if isinstance(prior, str) else prior["sha256"]
        assert digest(ROOT / path) == expected, path
    allowed = {f"genes/{gene}/{gene.split('/')[-1]}-{suffix}" for gene in CHANGED_GENES
               for suffix in ["ai-review.yaml", "ai-review.html", "notes.md"]}
    allowed.update({"modules/bacterial_l_carnitine_catabolism.yaml",
                    "pages/modules/bacterial_l_carnitine_catabolism.html",
                    "modules/bacterial_l_carnitine_catabolism-notes.md"})
    updates = {}
    preserved = 0
    for path, expected in baseline["published_closure_sha256"].items():
        actual = digest(ROOT / path)
        if actual != expected:
            assert path in allowed, (path, "unreviewed published-input change")
            updates[path] = {"before_sha256": expected, "after_sha256": actual}
        else:
            preserved += 1
    for label in ["core-consultation", "pseae-consultation"]:
        handoff = HERE / label / "handoff.json"
        release = json.loads(handoff.read_text())
        files = release.get("files", release.get("files_sha256"))
        assert isinstance(files, dict), handoff
        for path, expected in files.items():
            assert digest(ROOT / path) == expected, path
    return {"status": "PASS", **counts, "retired_NEW": counts["historical_NEW"] - counts["active_NEW"],
            "historical_files_sha256": historical,
            "module_quote_changes": quote_changes,
            "new_retirements": sorted(seen), "action_changes": actions,
            "protected_sources": len(baseline["protected_sources_sha256"]),
            "unchanged_published_inputs": preserved, "authorized_updates": updates,
            "baseline_sha256": digest(BASELINE)}


def core_functions(review):
    functions = {core[slot]["id"] for core in review.get("core_functions", [])
                 for slot in ["molecular_function", "contributes_to_molecular_function"] if core.get(slot)}
    for core in review.get("core_functions", []):
        if not core.get("proposed_molecular_function"):
            continue
        # This finite reviewed-panel bridge is deliberately not a universal mapper.
        assert review["id"] == "Q88R31", review["id"]
        assert not core.get("molecular_function")
        assert core["proposed_molecular_function"] == PROPOSAL["proposed_name"]
        matches = [p for p in review.get("proposed_new_terms", [])
                   if p["proposed_name"] == core["proposed_molecular_function"]]
        assert len(matches) == 1
        term = matches[0]
        assert " ".join(term["proposed_definition"].split()) == PROPOSAL["proposed_definition"]
        assert term.get("proposed_parent", {}).get("id") == PROPOSAL["parent"]
        for supports in [core.get("supported_by", []), term.get("supported_by", [])]:
            exact = [item for item in supports
                     if item.get("reference_id") == PROPOSAL["supporting_reference"]
                     and " ".join(item.get("supporting_text", "").split()) == PROPOSAL["supporting_text"]]
            assert exact, "Exact proposed chemistry lacks its independently grounded catalytic quotation"
            source = resolve_local_source(PROPOSAL["supporting_reference"], ROOT)
            assert source and quote_matches(PROPOSAL["supporting_text"], source)

        functions.add(PROPOSAL["parent"])
    return functions


def run(capture=False):
    spec = importlib.util.spec_from_file_location("published_carnitine_capacity", OLD)
    engine = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(engine)
    preservation = current_preservation()
    (HERE / "preservation.json").write_text(json.dumps(preservation, indent=2) + "\n")
    old_closure = engine.input_closure
    old_here = engine.HERE
    engine.HERE = HERE

    def closure(fixture):
        engine.HERE = old_here
        try:
            inputs = old_closure(fixture)
        finally:
            engine.HERE = HERE
        for path in [Path(__file__), BASELINE, HERE / "preservation.json",
                     HERE / "core-consultation/handoff.json", HERE / "pseae-consultation/handoff.json"]:
            inputs[str(path.relative_to(ROOT))] = digest(path)
        inputs.update(preservation["historical_files_sha256"])
        # Preserve closure breadth as well as verifying the old hashes: every published
        # input is a current frozen input, even if the original oracle did not consume it.
        published = json.loads(BASELINE.read_text())["published_closure_sha256"]
        for path in published:
            inputs[path] = digest(ROOT / path)
        for path in [ROOT / "pages/modules/bacterial_l_carnitine_catabolism.html",
                     ROOT / "modules/bacterial_l_carnitine_catabolism-notes.md"]:
            assert path.is_file(), path
            inputs[str(path.relative_to(ROOT))] = digest(path)
        for path in (ROOT / "history/modules/bacterial_l_carnitine_catabolism").glob("*.yaml"):
            inputs[str(path.relative_to(ROOT))] = digest(path)
        for label in ["core-consultation", "pseae-consultation"]:
            release = json.loads((HERE / label / "handoff.json").read_text())
            for path in release.get("files", release.get("files_sha256", {})):
                inputs[path] = digest(ROOT / path)
        return dict(sorted(inputs.items()))

    def candidates(fixture):
        result = {}
        for accession, member in fixture["members"].items():
            review = yaml.safe_load((ROOT / member["review_path"]).read_text())
            raw = (ROOT / member["raw_path"]).read_text()
            assert review["id"] == accession and re.search(r"^AC\s+" + re.escape(accession) + ";", raw, re.M)
            functions = core_functions(review)
            for role in member["roles"]:
                if role in fixture["required_reactions"]:
                    assert fixture["reactions"][role]["go"] in functions, (accession, role)
            result[accession] = {**copy.deepcopy(member), "taxon": review["taxon"]["id"],
                                 "families": ["PANTHER:" + f for f in re.findall(r"^DR   PANTHER; ([^;]+);", raw, re.M)],
                                 "functions": sorted(functions)}
        return result

    engine.input_closure = closure
    engine.verify_release_chain = lambda: preservation
    engine.load_candidates = candidates
    engine.run(capture_inputs=capture)
    review = yaml.safe_load((ROOT / "genes/PSEPK/PP_0303/PP_0303-ai-review.yaml").read_text())
    assert PROPOSAL["parent"] in core_functions(review)
    detected = []
    for defect in ["missing_proposal", "wrong_name", "wrong_parent", "wrong_chemistry", "missing_evidence",
                   "missing_term_evidence", "irrelevant_evidence", "fabricated_quote", "wrong_target", "duplicate_proposal"]:
        mutated = copy.deepcopy(review)
        if defect == "missing_proposal":
            mutated["proposed_new_terms"] = []
        elif defect == "wrong_name":
            mutated["core_functions"][0]["proposed_molecular_function"] = "unestablished activity"
        elif defect == "wrong_parent":
            mutated["proposed_new_terms"][0]["proposed_parent"]["id"] = "GO:0016289"
        elif defect == "wrong_chemistry":
            mutated["proposed_new_terms"][0]["proposed_definition"] = "Hydrolysis of betainyl-CoA."
        elif defect == "missing_evidence":
            mutated["core_functions"][0]["supported_by"] = []
        elif defect == "missing_term_evidence":
            mutated["proposed_new_terms"][0]["supported_by"] = []
        elif defect == "irrelevant_evidence":
            mutated["core_functions"][0]["supported_by"] = [{"reference_id": "PMID:19919675"}]
        elif defect == "fabricated_quote":
            mutated["core_functions"][0]["supported_by"][0]["supporting_text"] = "Unverified reaction."
        elif defect == "wrong_target":
            mutated["id"] = "Q9HTH7"
        else:
            mutated["proposed_new_terms"].append(copy.deepcopy(mutated["proposed_new_terms"][0]))
        try:
            core_functions(mutated)
        except AssertionError:
            detected.append(defect)
        else:
            raise AssertionError("Undetected proposed-activity defect: " + defect)
    (HERE / "proposed-core-guards.json").write_text(json.dumps({"status": "PASS", "detected": detected}, indent=2) + "\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--capture-inputs", action="store_true")
    run(parser.parse_args().capture_inputs)
