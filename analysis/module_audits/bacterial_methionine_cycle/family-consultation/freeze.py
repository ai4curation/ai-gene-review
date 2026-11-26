"""Freeze an exact handoff only after the sole member refresh has completed."""

import hashlib
import json
import os
import re
import subprocess

from run_checks import CACHE, FILES, HERE, ROOT, run


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    assert list((ROOT / ".cache/panther").glob("panther-members-*.tsv")), (
        "Wait for the sole member refresh"
    )
    checks = json.loads((HERE / "checks.json").read_text())
    grounding = run(
        "grounding",
        [
            "uv",
            "run",
            "python",
            "-m",
            "ai_gene_review.validation.family_residue_validator",
            *FILES,
        ],
    )
    assert grounding["exit_code"] == 0
    text = (CACHE / "grounding.log").read_text()
    counts = re.search(r"(\d+) pass, (\d+) fail, (\d+) unresolved", text)
    assert counts
    grounding["counts"] = dict(
        zip(["pass", "fail", "unresolved"], map(int, counts.groups()), strict=True)
    )
    assert grounding["counts"]["fail"] == grounding["counts"]["unresolved"] == 0, text
    checks.append(grounding)
    for i, path in enumerate(json.loads((HERE / "histories.json").read_text())):
        check = run("history-" + str(i + 1), ["just", "validate-history", path])
        assert check["exit_code"] == 0
        checks.append(check)
    check = run(
        "preservation",
        [
            "uv",
            "run",
            "python",
            str((HERE / "check_preservation.py").relative_to(ROOT)),
        ],
    )
    assert check["exit_code"] == 0
    checks.append(check)
    check = run(
        "phylogeny",
        ["uv", "run", "python", str((HERE / "check_phylogeny.py").relative_to(ROOT))],
    )
    assert check["exit_code"] == 0
    checks.append(check)
    expected = {
        n: sha(HERE / n) for n in ["preservation.json", "phylogeny-and-msa.json"]
    }
    for seed in ["1", "2"]:
        for script in ["check_preservation.py", "check_phylogeny.py"]:
            subprocess.run(
                ["uv", "run", "python", str((HERE / script).relative_to(ROOT))],
                cwd=ROOT,
                env={**os.environ, "PYTHONHASHSEED": seed},
                check=True,
                stdout=subprocess.DEVNULL,
            )
        assert expected == {n: sha(HERE / n) for n in expected}, (
            "Nondeterministic evidence output"
        )
    checks.append({"check": "determinism", "hash_seeds": [1, 2], "status": "PASS"})
    check = run("ruff", ["uv", "run", "ruff", "check", str(HERE.relative_to(ROOT))])
    assert check["exit_code"] == 0
    checks.append(check)
    (HERE / "checks.json").write_text(json.dumps(checks, indent=2) + "\n")
    logs = HERE / "checks"
    logs.mkdir(exist_ok=True)
    for p in sorted(CACHE.glob("*.log")):
        (logs / (p.stem + ".txt")).write_bytes(p.read_bytes())
    preservation = json.loads((HERE / "preservation.json").read_text())
    paths = [
        ROOT / p for p in FILES + json.loads((HERE / "histories.json").read_text())
    ]
    paths.append(ROOT / "interpro/panther/PTHR35799/PTHR35799-paint.tsv")
    paths.extend(
        p
        for p in HERE.rglob("*")
        if p.is_file() and "__pycache__" not in p.parts and p.name != "handoff.json"
    )
    handoff = {
        "status": "FROZEN_RELEASED",
        "scope": "Six methionine-cycle family reviews, one normally acquired previously missing LuxS PAINT slice, six generated histories and scoped consultation artifacts; no gene/module/project/protected-source edits.",
        "checks": {
            "status": "PASS",
            "grounding": grounding["counts"],
            "determinism_hash_seeds": [1, 2],
            "crosscheck_limit": "Zero conflicts; zero compared activity judgments. This is not an independent proof of universal chemistry.",
            "quotes_checked": len(preservation["quotes"]),
        },
        "preservation": {
            k: v
            for k, v in preservation.items()
            if k not in ["quotes", "inputs_sha256", "judgment_changes"]
        },
        "files": {str(p.relative_to(ROOT)): sha(p) for p in sorted(set(paths))},
    }
    path = HERE / "handoff.json"
    assert not path.exists(), "Never overwrite a frozen handoff"
    path.write_text(json.dumps(handoff, indent=2) + "\n")
    print("RELEASE", len(paths), "files", sha(path))


if __name__ == "__main__":
    main()
