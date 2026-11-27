"""Freeze a scoped additive handoff once; never overwrite earlier receipts."""
import importlib.util
import json
import subprocess
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]


def imported(name):
    spec = importlib.util.spec_from_file_location(name, HERE / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    writer = imported("apply")
    assert not (HERE / "handoff.json").exists()
    proof = imported("verify").verify()
    baseline = json.loads((HERE / "baseline.json").read_text())
    schemas = json.loads((HERE / "schema-checks.json").read_text())
    assert all(row["exit_code"] == 0 for row in schemas)
    ruff = subprocess.run([".venv/bin/ruff", "check", str(HERE)], cwd=ROOT, text=True, capture_output=True, check=True)
    proof["ruff"] = {"exit_code": ruff.returncode, "stdout": ruff.stdout}
    proof["schema_checks"] = [{"target_class": r["target_class"], "exit_code": r["exit_code"]} for r in schemas]
    supersessions = {}
    for path in writer.CURATED + writer.NOTES:
        row = baseline["documents"].get(path) or baseline["notes"][path]
        supersessions[path] = {"before_sha256": row["sha256"], "after_sha256": writer.sha(ROOT / path)}
    changed = set(subprocess.check_output(["git", "diff", "--name-only"], cwd=ROOT, text=True).splitlines())
    assert changed == set(supersessions), changed - set(supersessions)
    dependencies = dict(baseline["protected_sources"])
    dependencies.update(baseline["prior_artifacts"])
    refs = set()

    def walk(value):
        if isinstance(value, dict):
            for key, item in value.items():
                if key in ("id", "reference_id", "source_id") and isinstance(item, str) and item.startswith(("PMID:", "file:")):
                    refs.add(item)
                walk(item)
        elif isinstance(value, list):
            for item in value:
                walk(item)
    for path in baseline["documents"]:
        dependencies[path] = writer.sha(ROOT / path)
        walk(yaml.safe_load((ROOT / path).read_text()))
    for ref in sorted(refs):
        if ref.startswith("PMID:"):
            path = Path("publications") / f"PMID_{ref[5:]}.md"
        else:
            path = Path(ref[5:])
            if not (ROOT / path).exists():
                path = Path("genes") / path
        assert (ROOT / path).is_file(), ref
        dependencies[str(path)] = writer.sha(ROOT / path)
    inherited = []
    for path in sorted(writer.AUDIT.rglob("*handoff*.json")):
        if HERE in path.parents:
            continue
        data = json.loads(path.read_text())
        extra = data.get("source_dependencies", {})
        assert isinstance(extra, dict)
        for dependency, expected in extra.items():
            assert writer.sha(ROOT / dependency) == expected, dependency
            dependencies[dependency] = expected
        inherited.append({"path": str(path.relative_to(ROOT)), "sha256": writer.sha(path), "source_dependencies": len(extra)})
    assert not any(path.startswith(".cache/") for path in dependencies)
    writer.atomic(HERE / "supersessions.json", json.dumps(supersessions, indent=2) + "\n")
    writer.atomic(HERE / "preservation.json", json.dumps(proof, indent=2) + "\n")
    writer.atomic(HERE / "source-closure.json", json.dumps({"status": "PASS", "source_dependencies": dict(sorted(dependencies.items())), "prior_handoff_dependency_union": inherited, "private_capture": "Hash verified locally when available; bounded excerpt/provenance are durable inputs, raw capture is excluded."}, indent=2) + "\n")
    outputs = writer.CURATED + writer.NOTES + json.loads((HERE / "histories.json").read_text()) + [str(p.relative_to(ROOT)) for p in sorted(HERE.iterdir()) if p.is_file() and p.name != "handoff.json"]
    assert len(outputs) == len(set(outputs))
    release = {"status": "FROZEN", "baseline_head": baseline["head"], "scope": "PR6158 bounded chemical boundary/provenance follow-up", "files": {p: writer.sha(ROOT / p) for p in sorted(outputs)}, "source_dependencies": dict(sorted(dependencies.items())), "supersessions": str((HERE / "supersessions.json").relative_to(ROOT)), "checks": proof, "root_followup": ["Regenerate seven gene renders and module render.", "Add a six-atom successor to historical seven-atom coverage checks without rewriting prior receipts.", "Integrate current hash/scope receipts and required validation before publication.", "Keep raw publisher capture and unscoped initial snapshot private."], "no_render_fullrun_commit_or_push": True}
    writer.atomic(HERE / "handoff.json", json.dumps(release, indent=2) + "\n")
    for group in ("files", "source_dependencies"):
        for path, expected in release[group].items():
            assert writer.sha(ROOT / path) == expected, path
    print(json.dumps({"handoff": str((HERE / "handoff.json").relative_to(ROOT)), "sha256": writer.sha(HERE / "handoff.json"), "files": len(outputs), "source_dependencies": len(dependencies), "module_sha256": writer.sha(ROOT / writer.MOD), "checks": proof}, indent=2))


if __name__ == "__main__":
    main()
