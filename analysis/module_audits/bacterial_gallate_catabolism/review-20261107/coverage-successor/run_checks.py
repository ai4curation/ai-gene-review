"""Sequential focused checks, immutable input guards and ENOSPC stop."""

import hashlib
import json
import os
import shutil
import subprocess
import tempfile
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
A = HERE.parent.parent


def now():
    return datetime.now(timezone.utc).isoformat()


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def atomic(path, text):
    if shutil.disk_usage(ROOT).free <= 256 * 1024 * 1024:
        raise RuntimeError("STOP: headroom below 256 MiB")
    with tempfile.NamedTemporaryFile(
        dir=path.parent, prefix=".gallate-", delete=False
    ) as stream:
        stream.write(text.encode())
        stream.flush()
        os.fsync(stream.fileno())
        temporary = stream.name
    os.replace(temporary, path)


def main():
    assert not (HERE / "run-state.json").exists(), "Do not restart a recorded run"
    prior_path = HERE.parent / "science-consultation/handoff.json"
    release = json.loads(prior_path.read_text())
    frozen = release["files"] | release["source_dependencies"]
    frozen[str(prior_path.relative_to(ROOT))] = sha(prior_path)
    for path in (
        "modules/bacterial_gallate_catabolism-source-analysis/check_coverage.py",
        str((A / "coverage-results.yaml").relative_to(ROOT)),
        str((A / "coverage-evidence.yaml").relative_to(ROOT)),
    ):
        frozen[path] = sha(ROOT / path)
    for path, expected in frozen.items():
        assert sha(ROOT / path) == expected, path
    atomic(HERE / "frozen-inputs.json", json.dumps(frozen, indent=2) + "\n")
    commands = [
        (
            "coverage",
            [
                ".venv/bin/python",
                "-B",
                str((HERE / "check_coverage.py").relative_to(ROOT)),
            ],
        )
    ]
    for org, gene in [
        ("PSEPK", "galA"),
        ("PSEPK", "galB"),
        ("PSEPK", "galC"),
        ("PSEPK", "galD"),
        ("PSEPK", "galP"),
        ("BURL3", "Bcep18194_C7570"),
        ("SPHSK", "ligK"),
    ]:
        commands.append((f"gene-{org}-{gene}", ["just", "validate", org, gene]))
    commands.extend(
        [
            (
                "module-schema",
                [
                    ".venv/bin/linkml-validate",
                    "--schema",
                    "src/ai_gene_review/schema/gene_review.yaml",
                    "--target-class",
                    "ModuleReview",
                    "modules/bacterial_gallate_catabolism.yaml",
                ],
            ),
            (
                "module-semantic",
                [
                    ".venv/bin/python",
                    "-B",
                    "-m",
                    "ai_gene_review.validation.module_validator",
                    "modules/bacterial_gallate_catabolism.yaml",
                ],
            ),
        ]
    )
    state = {
        "started": now(),
        "status": "RUNNING",
        "checks": [],
        "working_directory": str(ROOT),
        "initial_free_bytes": shutil.disk_usage(ROOT).free,
    }
    atomic(HERE / "run-state.json", json.dumps(state, indent=2) + "\n")
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", UV_NO_SYNC="1")
    for name, command in commands:
        free = shutil.disk_usage(ROOT).free
        if free <= 256 * 1024 * 1024:
            raise RuntimeError("STOP: insufficient headroom before " + name)
        print(
            json.dumps({"starting": name, "free_bytes": free, "command": command}),
            flush=True,
        )
        start = now()
        result = subprocess.run(
            command, cwd=ROOT, env=env, text=True, capture_output=True
        )
        log = result.stdout + "\n--- STDERR ---\n" + result.stderr
        enospc = any(
            marker in log.lower()
            for marker in ("no space left on device", "errno 28", "enospc")
        )
        atomic(HERE / f"{name}.log", log)
        check = {
            "name": name,
            "command": command,
            "started": start,
            "finished": now(),
            "exit_code": result.returncode,
            "enospc": enospc,
            "free_bytes_before": free,
            "free_bytes_after": shutil.disk_usage(ROOT).free,
            "log": str((HERE / f"{name}.log").relative_to(ROOT)),
            "log_sha256": sha(HERE / f"{name}.log"),
        }
        state["checks"].append(check)
        if name == "coverage" and result.returncode == 0:
            parsed = json.loads(result.stdout)
            assert parsed["status"] == "PASS"
            atomic(HERE / "coverage-results.json", json.dumps(parsed, indent=2) + "\n")
        if enospc or result.returncode:
            state["status"] = "INFRASTRUCTURE_FAILURE" if enospc else "FAILED"
            state["finished"] = now()
            atomic(HERE / "run-state.json", json.dumps(state, indent=2) + "\n")
            print(json.dumps(check), flush=True)
            return result.returncode or 1
        atomic(HERE / "run-state.json", json.dumps(state, indent=2) + "\n")
        print(
            json.dumps(
                {
                    "finished": name,
                    "exit_code": result.returncode,
                    "free_bytes": check["free_bytes_after"],
                }
            ),
            flush=True,
        )
    for path, expected in frozen.items():
        assert sha(ROOT / path) == expected, path
    state["status"] = "PASS"
    state["finished"] = now()
    state["frozen_input_count"] = len(frozen)
    atomic(HERE / "run-state.json", json.dumps(state, indent=2) + "\n")
    print(
        json.dumps(
            {"status": "PASS", "checks": len(commands), "frozen_inputs": len(frozen)}
        ),
        flush=True,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
