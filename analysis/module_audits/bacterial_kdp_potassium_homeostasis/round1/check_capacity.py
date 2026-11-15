"""Additive round-one execution of the published production-compiler capacity audit.

Reuse its biological gates and controls; update only the activator term, output
location, and explicitly changed review/notes hashes. Historical receipts are not
rewritten. The additional binding-only control tests the new function boundary.
"""

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
ORIGINAL = HERE.parent / "capacity-consultation/check_capacity.py"
OUTPUT = HERE / "capacity"
OUTPUT.mkdir(exist_ok=True)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    baseline = json.loads((HERE / "baseline.json").read_text())
    changed = json.loads((HERE / "changed-curated-paths.json").read_text())
    updates = {}
    for rel in changed:
        p = ROOT / rel
        updates[rel] = digest(p)
        if not rel.startswith("genes/"):
            continue
        notes = p.with_name(p.parent.name + "-notes.md")
        updates[str(notes.relative_to(ROOT))] = digest(notes)
        render = p.with_suffix(".html")
        updates[str(render.relative_to(ROOT))] = digest(render)
    source = ORIGINAL.read_text()
    replacements = {
        "AUDIT = Path(__file__).resolve().parent": "ORIGINAL_AUDIT = Path(__file__).resolve().parent\nAUDIT = ROUND1_OUTPUT",
        'AUDIT / "evidence-gates.json"': 'ORIGINAL_AUDIT / "evidence-gates.json"',
        'AUDIT / "source-quotes.json"': 'ORIGINAL_AUDIT / "source-quotes.json"',
        'AUDIT / "frozen-input-releases.json"': 'ORIGINAL_AUDIT / "frozen-input-releases.json"',
        'DNA = "GO:0000987"': 'DNA = "GO:0001216"',
        "== expected, rel": "== ROUND1_HASH_UPDATES.get(rel, expected), rel",
    }
    for old, new in replacements.items():
        assert old in source, old
        source = source.replace(old, new)
    namespace = {
        "__file__": str(ORIGINAL),
        "__name__": "__round1_capacity__",
        "ROUND1_OUTPUT": OUTPUT,
        "ROUND1_HASH_UPDATES": updates,
    }
    exec(compile(source, str(ORIGINAL), "exec"), namespace)
    panel = namespace["panel"]("ECOLI")
    for record in panel:
        if record["gene"] == "kdpE":
            record["molecular"] = [
                m for m in record["molecular"] if m != "GO:0001216"
            ] + ["GO:0000987"]
    binding_only = namespace["evaluate"](panel)
    assert not binding_only["regulatory"] and not binding_only["module"]
    profiles = next(
        v
        for n in namespace["nodes"](namespace["DOC"]["module"])
        for v in n.get("variant_sets", [])
        if v["id"] == "kdp_regulatory_profiles"
    )
    assert profiles["selection"] == "ONE_OR_MORE"
    proof = {
        "published_head": baseline["head"],
        "unchanged_checker": str(ORIGINAL.relative_to(ROOT)),
        "unchanged_checker_sha256": digest(ORIGINAL),
        "adapter_sha256": digest(Path(__file__)),
        "explicit_source_adaptations": replacements,
        "updated_input_hashes": updates,
        "published_cases_passed": len(namespace["CASES"]),
        "additional_controls": {
            "binding_without_activation": binding_only,
            "regulatory_selection": profiles["selection"],
        },
        "limit": "Production compiler treats these alternatives as OR; the biological non-exclusivity is stated in ONE_OR_MORE metadata, not an XOR enforcement claim.",
    }
    (HERE / "capacity-adapter-proof.json").write_text(
        json.dumps(proof, indent=2) + "\n"
    )
    print(
        json.dumps(
            {
                "published_cases": len(namespace["CASES"]),
                "new_negative_control": "PASS",
                "metadata_control": "PASS",
            }
        )
    )


if __name__ == "__main__":
    main()
