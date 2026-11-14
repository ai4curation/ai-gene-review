"""Record completed focused checks and freeze an immutable three-gene handoff."""

import hashlib
import json
import os
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
CACHE = (
    ROOT
    / ".cache/module-audit-logs/methionine-cycle-20261107/mes-alternatives-consultation"
)
GENES = [("ACIAD", "ACIAD3523"), ("ACIAD", "ACIAD3524"), ("DEHMC", "cbdbA481")]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    checks = []
    for org, gene in GENES:
        name = org + "-" + gene
        log = (CACHE / (name + "-validate.log")).read_text()
        assert "All validations passed for " + org + "/" + gene in log
        warnings = [line.strip() for line in log.splitlines() if "[WARNING]" in line]
        assert len(warnings) == 1, (name, warnings)
        render = (CACHE / (name + "-render.log")).read_text()
        assert (
            f"genes/{org}/{gene}/{gene}-ai-review.html" in render
            and "Rendered" in render
        )
        paint = (CACHE / (name + "-paint.log")).read_text()
        assert "losses not checked" in paint
        checks.append(
            {
                "gene": org + "/" + gene,
                "validate": "PASS",
                "render": "PASS",
                "warning": warnings[0],
                "paint_lookup": "completed; exact lineage unavailable, no absence claim",
            }
        )
    section_log = (CACHE / "final-record-sections.log").read_text()
    assert "0 mismatched" in section_log and "0 unplaceable" in section_log
    for i, path in enumerate(json.loads((HERE / "histories.json").read_text())):
        result = subprocess.run(
            ["just", "validate-history", path],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        (CACHE / f"history-{i + 1}.log").write_text(result.stdout)
        assert result.returncode == 0
    subprocess.run(
        [
            "uv",
            "run",
            "python",
            str((HERE / "check_preservation.py").relative_to(ROOT)),
        ],
        cwd=ROOT,
        check=True,
    )
    before = sha(HERE / "preservation.json")
    for seed in ["1", "2"]:
        subprocess.run(
            [
                "uv",
                "run",
                "python",
                str((HERE / "check_preservation.py").relative_to(ROOT)),
            ],
            cwd=ROOT,
            env={**os.environ, "PYTHONHASHSEED": seed},
            check=True,
            stdout=subprocess.DEVNULL,
        )
        assert sha(HERE / "preservation.json") == before
    result = subprocess.run(
        ["uv", "run", "ruff", "check", str(HERE.relative_to(ROOT))],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    (CACHE / "ruff.log").write_text(result.stdout)
    assert result.returncode == 0
    (HERE / "checks.json").write_text(
        json.dumps(
            {
                "status": "PASS",
                "genes": checks,
                "histories": 3,
                "record_sections": "0 mismatches",
                "determinism_seeds": [1, 2],
                "ruff": "PASS",
            },
            indent=2,
        )
        + "\n"
    )
    logdir = HERE / "checks"
    logdir.mkdir(exist_ok=True)
    for p in sorted(CACHE.glob("*.log")):
        (logdir / (p.stem + ".txt")).write_bytes(p.read_bytes())
    files = [ROOT / p for p in json.loads((HERE / "histories.json").read_text())]
    for org, gene in GENES:
        files.extend(
            ROOT / f"genes/{org}/{gene}/{gene}{suffix}"
            for suffix in ["-ai-review.yaml", "-notes.md", "-ai-review.html"]
        )
    files.extend(
        p
        for p in HERE.rglob("*")
        if p.is_file() and "__pycache__" not in p.parts and p.name != "handoff.json"
    )
    proof = json.loads((HERE / "preservation.json").read_text())
    handoff = {
        "status": "FROZEN_RELEASED",
        "scope": "Three new MesD/MesX/MesB reviews, notes, renders, generated histories and scoped artifacts; no existing family/module/project/source changes.",
        "checks": json.loads((HERE / "checks.json").read_text()),
        "preservation": {
            k: v
            for k, v in proof.items()
            if k not in ["action_ledger", "quotes", "inputs_sha256"]
        },
        "quote_count": len(proof["quotes"]),
        "files": {str(p.relative_to(ROOT)): sha(p) for p in sorted(set(files))},
    }
    target = HERE / "handoff.json"
    assert not target.exists(), "Never overwrite an immutable handoff"
    target.write_text(json.dumps(handoff, indent=2) + "\n")
    print("RELEASE", len(handoff["files"]), sha(target))


if __name__ == "__main__":
    main()
