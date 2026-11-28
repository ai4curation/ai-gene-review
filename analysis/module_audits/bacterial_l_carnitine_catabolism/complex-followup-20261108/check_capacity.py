"""Run the unchanged biological oracle against the reviewed complex follow-up.

Historical release checks remain in their original directories. This receipt checks
current input bytes and the two follow-up source-payload comparisons instead.
"""

import argparse
import copy
import importlib.util
import json
from pathlib import Path
import re
import subprocess

import yaml

HERE = Path(__file__).resolve().parent
AUDIT = HERE.parent
ROOT = HERE.parents[3]


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run(capture=False):
    engine = load("carnitine_oracle", AUDIT / "capacity/audit_capacity.py")
    engine.FIXTURE = AUDIT / "round2-fixture-location/evidence-fixture.yaml"
    bridge = load("proposal_bridge", AUDIT / "round2-fixture-location/check_followup.py")
    receipt = json.loads((HERE / "receipt.json").read_text())
    preserved = {}
    for gene in ["cbcV", "cbcW"]:
        before = yaml.safe_load((HERE / f"{gene}-before.yaml.txt").read_text())
        after = yaml.safe_load(
            (ROOT / f"genes/PSEAE/{gene}/{gene}-ai-review.yaml").read_text()
        )

        def payload(doc):
            return [
                {k: v for k, v in a.items() if k != "review"}
                for a in doc["existing_annotations"]
            ]

        assert payload(before) == payload(after)
        preserved[gene] = len(payload(after))
    for path in [engine.MODULE, engine.FIXTURE]:
        prior = subprocess.check_output(
            ["git", "show", receipt["base_head"] + ":" + str(path.relative_to(ROOT))],
            cwd=ROOT,
        )
        assert path.read_bytes() == prior, path
    old_closure = engine.input_closure
    original_here = engine.HERE
    engine.HERE = HERE

    def closure(fixture):
        engine.HERE = original_here
        try:
            inputs = old_closure(fixture)
        finally:
            engine.HERE = HERE
        for path in [
            Path(__file__),
            AUDIT / "round2-fixture-location/check_followup.py",
            HERE / "cbcV-before.yaml.txt",
            HERE / "cbcW-before.yaml.txt",
        ]:
            inputs[str(path.relative_to(ROOT))] = engine.digest(path)
        return dict(sorted(inputs.items()))

    def candidates(fixture):
        result = {}
        for accession, member in fixture["members"].items():
            review = yaml.safe_load((ROOT / member["review_path"]).read_text())
            raw = (ROOT / member["raw_path"]).read_text()
            assert review["id"] == accession and re.search(
                r"^AC\s+" + re.escape(accession) + ";", raw, re.M
            )
            functions = bridge.core_functions(review)
            for role in member["roles"]:
                if role in fixture["required_reactions"]:
                    assert fixture["reactions"][role]["go"] in functions, (
                        accession,
                        role,
                    )
            result[accession] = {
                **copy.deepcopy(member),
                "taxon": review["taxon"]["id"],
                "families": [
                    "PANTHER:" + f
                    for f in re.findall(r"^DR   PANTHER; ([^;]+);", raw, re.M)
                ],
                "functions": sorted(functions),
            }
        return result

    def preservation():
        return {
            "scope": "Current follow-up payload preservation, not revalidation of historical release hashes",
            "ordered_source_rows": preserved,
            "module_and_fixture_unchanged_since": receipt["base_head"],
        }

    engine.input_closure = closure
    engine.verify_release_chain = preservation
    engine.load_candidates = candidates
    engine.run(capture_inputs=capture)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--capture-inputs", action="store_true")
    run(parser.parse_args().capture_inputs)
