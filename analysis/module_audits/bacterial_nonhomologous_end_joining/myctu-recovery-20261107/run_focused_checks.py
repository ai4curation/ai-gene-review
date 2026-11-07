"""One-session helper/history and focused final verification; no source mutation."""

import json
import os
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
A = Path(__file__).resolve().parent
ENV = dict(
    os.environ,
    UV_NO_SYNC="1",
    PYTHONSAFEPATH="1",
    PYTHONDONTWRITEBYTECODE="1",
    PYTHONPATH=str(ROOT / "src"),
    UV_PROJECT_ENVIRONMENT="/Users/cjm/orca/workspaces/ai-gene-review/aigr-modules-taxon/.venv",
)
assert not (A / "focused-results.json").exists(), "Do not duplicate history generation"
results = []
for gene in ["mku", "ligD"]:
    command = [
        "just",
        "new-history",
        "--kind",
        "gene",
        "--organism",
        "MYCTU",
        "--slug",
        gene,
        "--event",
        "REVIEW",
        "--outcome",
        "changed",
        "--actor-name",
        "codex",
        "--agent-tool",
        "codex",
        "--summary",
        "Reconstruct and verify H37Rv Ku/LigD reviews after workspace loss",
        "--details",
        "Reconstructed recorded scientific curation against byte-identical original seeds and raw sources after workspace deletion. Preserved all 55 original ordered annotation payloads, qualifiers and lifecycle; no NEW or retired rows. mku pre-successor YAML exactly matches surviving complete historical output. LigD was replayed from the recovered complete curation script and follow-up corrections, not falsely called recovery of its missing original seal. Fresh validations and renders accompany this new history; historical receipts were not fabricated. Kept direct biochemical capabilities and H37Rv versus CDC1551 construct/assay limits. Details and source provenance: analysis/module_audits/bacterial_nonhomologous_end_joining/myctu-recovery-20261107.",
        "--sections",
        "description,existing_annotations,core_functions,references",
    ]
    run = subprocess.run(
        command, cwd=ROOT, env=ENV, capture_output=True, text=True, check=False
    )
    log = A / "logs" / f"{gene}-history-create.log"
    log.write_text(run.stdout + run.stderr)
    results.append(
        {
            "command": command,
            "exit_code": run.returncode,
            "log": str(log.relative_to(ROOT)),
        }
    )
    assert run.returncode == 0
    history = next(
        x.strip() for x in run.stdout.splitlines() if x.startswith("history/")
    )
    for label, command in [
        ("validation-final", ["just", "validate", "MYCTU", gene]),
        ("history-validation", ["just", "validate-history", history]),
        ("render", ["just", "render", "MYCTU", gene]),
    ]:
        log = A / "logs" / f"{gene}-{label}.log"
        with log.open("w") as stream:
            run = subprocess.run(
                command,
                cwd=ROOT,
                env=ENV,
                stdout=stream,
                stderr=subprocess.STDOUT,
                check=False,
            )
        results.append(
            {
                "command": command,
                "exit_code": run.returncode,
                "log": str(log.relative_to(ROOT)),
            }
        )
        (A / "focused-results.json").write_text(json.dumps(results, indent=2) + "\n")
        print(gene, label, run.returncode, flush=True)
        if run.returncode:
            raise SystemExit(run.returncode)
