"""One-time atomic release; never rewrites an existing frozen handoff."""
import importlib.util
import json
import subprocess
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]


def module(name):
    spec = importlib.util.spec_from_file_location(name, HERE / f"{name}.py")
    loaded = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loaded)
    return loaded


def main():
    writer = module("apply_corrections")
    assert not (HERE / "handoff.json").exists(), "Frozen release exists; do not overwrite"
    result = module("verify").verify()
    baseline = json.loads((HERE / "baseline.json").read_text())
    schemas = json.loads((HERE / "schema-checks.json").read_text())
    assert all(row["exit_code"] == 0 for row in schemas)
    command = [".venv/bin/ruff", "check", str(HERE)]
    ruff = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, check=True)
    result["ruff"] = {"command": command, "exit_code": ruff.returncode, "output": ruff.stdout}
    result["schema_target_classes"] = [r["target_class"] for r in schemas]
    supersessions = {}
    for group in ("documents", "notes"):
        for path, old in baseline[group].items():
            supersessions[path] = {"before_sha256": old["sha256"], "after_sha256": writer.sha(ROOT / path)}
    changed = subprocess.check_output(["git", "diff", "--name-only"], cwd=ROOT, text=True).splitlines()
    exclusions = {"cache/enums/gomolecularactivityenum_d457a56b08d3.csv", "cache/enums/ncbitaxonenum_4c50e6d01753.csv", "cache/go/terms.csv", "cache/ncbitaxon/terms.csv"}
    assert set(changed) - exclusions == set(supersessions), changed
    result["preexisting_unowned_cache_diffs_not_modified"] = sorted(set(changed) & exclusions)
    dependencies = dict(baseline["protected_sources"])
    dependencies.update(baseline["prior_audit_artifacts"])
    refs = set()

    def walk(value):
        if isinstance(value, dict):
            for key, item in value.items():
                if key in ("id", "reference_id") and isinstance(item, str) and item.startswith(("PMID:", "file:")):
                    refs.add(item)
                walk(item)
        elif isinstance(value, list):
            for item in value:
                walk(item)

    for path in baseline["documents"]:
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
    # Include explicit dependency maps from every historical handoff, not only
    # citations in the currently edited core functions. This older audit has none.
    handoffs = []
    for path in sorted(writer.AUDIT.rglob("*handoff*.json")):
        if HERE in path.parents:
            continue
        data = json.loads(path.read_text())
        inherited = data.get("source_dependencies", {})
        assert isinstance(inherited, dict), path
        for dependency, expected in inherited.items():
            assert writer.sha(ROOT / dependency) == expected, dependency
            dependencies[dependency] = expected
        handoffs.append({"path": str(path.relative_to(ROOT)), "sha256": writer.sha(path), "explicit_source_dependency_count": len(inherited)})
    writer.atomic(HERE / "supersessions.json", json.dumps(supersessions, indent=2) + "\n")
    writer.atomic(HERE / "preservation.json", json.dumps(result, indent=2) + "\n")
    writer.atomic(HERE / "source-closure.json", json.dumps({"status": "PASS", "source_dependencies": dict(sorted(dependencies.items())), "direct_reference_count": len(refs), "prior_handoff_dependency_union": handoffs, "scope": "Current direct references, protected source files, all prior audit artifacts and any explicit source_dependencies on historical handoffs. Old handoff files remain byte-identical; their historical output hashes are not silently rewritten."}, indent=2) + "\n")
    histories = json.loads((HERE / "histories.json").read_text())
    outputs = list(supersessions) + histories + [str(p.relative_to(ROOT)) for p in sorted(HERE.iterdir()) if p.is_file() and p.name != "handoff.json"]
    assert len(outputs) == len(set(outputs))
    release = {"status": "FROZEN", "baseline_head": baseline["head"], "scope": "PR6194 bounded second-review scientific corrections", "files": {p: writer.sha(ROOT / p) for p in sorted(outputs)}, "source_dependencies": dict(sorted(dependencies.items())), "supersessions": str((HERE / "supersessions.json").relative_to(ROOT)), "checks": result, "root_followup": ["Regenerate five gene and module HTML files; existing HTML intentionally unchanged.", "Run required focused scientific/semantic checks and full validation when storage permits.", "Account for module hash supersession although Boolean circuit unchanged.", "AcoC current negative ledger remains unenforced by production crosscheck."], "no_remote_writes": True, "no_commit_or_staging": True}
    writer.atomic(HERE / "handoff.json", json.dumps(release, indent=2) + "\n")
    for path, expected in release["files"].items():
        assert writer.sha(ROOT / path) == expected, path
    for path, expected in release["source_dependencies"].items():
        assert writer.sha(ROOT / path) == expected, path
    print(json.dumps({"handoff": str((HERE / "handoff.json").relative_to(ROOT)), "sha256": writer.sha(HERE / "handoff.json"), "files": len(outputs), "source_dependencies": len(dependencies), "preservation": result}, indent=2))


if __name__ == "__main__":
    main()
