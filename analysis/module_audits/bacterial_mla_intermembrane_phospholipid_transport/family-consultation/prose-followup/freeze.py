"""Freeze the additive release without rewriting any initial manifest."""

import hashlib
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    if (HERE / "handoff.json").exists():
        raise RuntimeError("Already frozen")
    subprocess.run(["uv", "run", "ruff", "check", str(HERE)], cwd=ROOT, check=True)
    subprocess.run(
        ["uv", "run", "python", str(HERE / "check.py")], cwd=ROOT, check=True
    )
    checks = json.loads((HERE / "checks.json").read_text())
    assert all(x["exit_code"] == 0 for x in checks)
    histories = json.loads((HERE / "histories.json").read_text())
    assert len(histories) == 3
    changes = json.loads((HERE / "changes.json").read_text())
    files = {
        str(p.relative_to(ROOT)): sha(p)
        for p in sorted(HERE.rglob("*"))
        if p.is_file() and "__pycache__" not in p.parts
    }
    files.update({r["path"]: sha(ROOT / r["path"]) for r in histories})
    files.update({r["path"]: r["after_sha256"] for r in changes})
    result = {
        "status": "FROZEN_RELEASED",
        "supersedes": json.loads((HERE / "prior-release.json").read_text()),
        "scope": "Only three family review hashes superseded;12 exact prose fields;all enums,PAINT,source evidence and member identities unchanged",
        "files": dict(sorted(files.items())),
        "replacement_hashes": [
            {k: r[k] for k in ["path", "before_sha256", "after_sha256"]}
            for r in changes
        ],
        "checks": "PASS schema/terms/references/grounding/crosscheck/preservation/3histories/Ruff",
        "release_ownership": True,
    }
    (HERE / "handoff.json").write_text(json.dumps(result, indent=2) + "\n")
    print("FROZEN", len(files), "files", sha(HERE / "handoff.json"))
    print(json.dumps(result["replacement_hashes"], indent=2))


if __name__ == "__main__":
    main()
