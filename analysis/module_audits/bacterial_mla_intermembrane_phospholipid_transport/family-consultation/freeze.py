"""Freeze a checked, deterministic release; refuse to overwrite an existing handoff."""

import hashlib
import json
import os
import shutil
import subprocess
from pathlib import Path

import yaml
from ai_gene_review.validation.supporting_text import build_supporting_text_validator

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
CACHE = ROOT / ".cache/module-audit-logs/mla-20261107/family-consultation"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    if (HERE / "handoff.json").exists():
        raise RuntimeError(
            "Frozen handoff exists; use an additive supersession, never overwrite"
        )
    checks = json.loads((HERE / "checks.json").read_text())
    assert all(x["exit_code"] == 0 for x in checks)
    grounding = (CACHE / "grounding.log").read_text()
    assert "142 pass, 0 fail, 0 unresolved" in grounding
    histories = json.loads((HERE / "histories.json").read_text())
    assert len(histories) == 6 and all(
        x["validation_exit_code"] == 0 for x in histories
    )
    subprocess.run(
        ["uv", "run", "ruff", "check", str(HERE.relative_to(ROOT))],
        cwd=ROOT,
        check=True,
    )
    snapshots = []
    for seed in ["1", "2"]:
        subprocess.run(
            ["uv", "run", "python", str(HERE / "check_preservation.py")],
            cwd=ROOT,
            env={**os.environ, "PYTHONHASHSEED": seed},
            check=True,
            capture_output=True,
        )
        snapshots.append(
            {n: sha(HERE / n) for n in ["quotes.json", "preservation.json"]}
        )
    assert snapshots[0] == snapshots[1]
    (HERE / "determinism.json").write_text(
        json.dumps(
            {"status": "PASS", "hash_seeds": [1, 2], "outputs": snapshots[0]}, indent=2
        )
        + "\n"
    )
    preservation = json.loads((HERE / "preservation.json").read_text())
    inputs = dict(preservation["inputs_sha256"])
    external = []
    for name in ["existing-review-consultation", "new-member-consultation"]:
        path = HERE.parent / name / "handoff.json"
        d = json.loads(path.read_text())
        for source, h in d["files"].items():
            assert sha(ROOT / source) == h, source
        external.append(
            {
                "path": str(path.relative_to(ROOT)),
                "sha256": sha(path),
                "files_verified": len(d["files"]),
            }
        )
        inputs[str(path.relative_to(ROOT))] = sha(path)
    members = json.loads((HERE / "target-membership.json").read_text())
    assert len(members) == 18
    for row in members:
        assert sha(ROOT / row["source"]) == row["source_sha256"]
        inputs[row["source"]] = row["source_sha256"]
        org, gene = row["gene"].split("/")
        review = f"genes/{org}/{gene}/{gene}-ai-review.yaml"
        inputs[review] = sha(ROOT / review)
    manual = [
        (
            "27529189",
            "Within this complex, MlaD forms an SDS-resistant hexamer via its soluble domain, and we demonstrate that this domain binds PLs.",
        ),
        (
            "34873038",
            "such anterograde movement is instead abolished by ATP hydrolysis",
        ),
        ("28388411", "using biolayer interferometry"),
        (
            "33837253",
            "can carry two diacyl glycerophospholipids as well as one cardiolipin",
        ),
        ("32602838", "can be rescued by overexpression of either WT MlaB or MlaF"),
        ("36518166", "we were not able to identify an MlaB homologue in B. pertussis"),
        (
            "36642182",
            "Fatty acids and cholesterol are imported across the Mtb cell wall via the dedicated Mce1 and Mce4 transporters, respectively.",
        ),
        (
            "20128927",
            "We focused on representatives from three groups (membrane and related proteins (emrK, yrbB), cytosolic enzymes (ycjU), and regulators (ycjW, ybcM)). In each case, complementation was observed (Fig. 3).",
        ),
    ]
    validator, _ = build_supporting_text_validator(ROOT / "publications")
    findings = []
    for pm, q in manual:
        result = validator.validate(q, "PMID:" + pm)
        assert result.is_valid and not result.skipped, (pm, result.message)
        path = ROOT / f"publications/PMID_{pm}.md"
        meta = yaml.safe_load(path.read_text().split("---", 2)[1])
        assert meta["full_text_available"] is True
        inputs[str(path.relative_to(ROOT))] = sha(path)
        findings.append(
            {
                "reference": "PMID:" + pm,
                "title": meta["title"],
                "access": "FULL_CACHED_PRIMARY",
                "supporting_text": q,
                "source_sha256": sha(path),
                "manual_scope": "See evidence.md; quotation presence is not an automatic biological judgment.",
            }
        )
    (HERE / "manual-reference-findings.json").write_text(
        json.dumps(findings, indent=2) + "\n"
    )
    (HERE / "input-closure.json").write_text(
        json.dumps(
            {
                "external_releases": external,
                "inputs_sha256": dict(sorted(inputs.items())),
            },
            indent=2,
        )
        + "\n"
    )
    logs = HERE / "logs"
    logs.mkdir(exist_ok=True)
    for path in sorted(CACHE.glob("*.log")):
        shutil.copyfile(path, logs / path.name)
    files = {}
    for path in sorted(HERE.rglob("*")):
        if path.is_file() and "__pycache__" not in path.parts:
            files[str(path.relative_to(ROOT))] = sha(path)
    for f in json.loads((HERE / "trees-compact.json").read_text()):
        path = ROOT / f"interpro/panther/{f}/{f}-review.yaml"
        files[str(path.relative_to(ROOT))] = sha(path)
    for row in histories:
        files[row["path"]] = sha(ROOT / row["path"])
    result = {
        "status": "FROZEN_RELEASED",
        "scope": "Six Mla family reviews, generated histories and family-consultation artifacts only",
        "files": dict(sorted(files.items())),
        "checks": {
            "schema": "PASS",
            "terms": "PASS",
            "references": "PASS",
            "family_gene_crosscheck": "PASS; zero conflicts or unresolved",
            "grounding": {"PASS": 142, "FAIL": 0, "UNRESOLVED": 0},
            "histories": 6,
            "structured_quotes": 51,
            "additional_manual_primary_quotes": 8,
            "ruff": "PASS",
            "preservation": "PASS",
            "determinism": "PASS",
        },
        "preserved": {
            "original_PAINT_payloads": 21,
            "unrelated_node_objects_exact": 11,
            "old_history_files": 14,
            "protected_source_files": 48,
            "original_exception_objects_archived": 13,
        },
        "limitations": [
            "Activity scope is distinct from verified classification; exact positive role/cargo/compartment/interface gates remain required.",
            "Current TGD1 negative ledger is not production-consumed; the exact live LOSS_SUPPORTED PAINT node remains.",
            "Reference trees omit most new/KT2440 target leaves; missing leaves do not prove absence of losses or functions.",
            "No full-corpus validation or native whole-route flux claim.",
        ],
        "release_ownership": True,
    }
    (HERE / "handoff.json").write_text(json.dumps(result, indent=2) + "\n")
    print("FROZEN", len(files), "files", sha(HERE / "handoff.json"))


if __name__ == "__main__":
    main()
