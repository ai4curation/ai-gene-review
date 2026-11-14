from pathlib import Path
import os
import subprocess
import json
import datetime

w = Path("/private/tmp/aigr-nitrogen-pts-taxon-audit")
root = Path("/Users/cjm/orca/workspaces/ai-gene-review/aigr-modules-taxon")
c = (
    w
    / "analysis/module_audits/bacterial_nitrogen_regulatory_pts/control-reviews-20261107"
)
env = os.environ.copy()
env.update(
    UV_PROJECT_ENVIRONMENT=str(root / ".venv"),
    UV_NO_SYNC="1",
    PYTHONPATH=str(w / "src"),
    PYTHONDONTWRITEBYTECODE="1",
)
rows = []
for gene in ["ptsI", "ptsH"]:
    cmd = [
        "just",
        "new-history",
        "--kind",
        "gene",
        "--organism",
        "ECOLI",
        "--slug",
        gene,
        "--event",
        "CREATE",
        "--outcome",
        "changed",
        "--summary",
        "Review carbohydrate PTS control " + gene,
        "--actor-name",
        "codex",
        "--agent-tool",
        "codex",
        "--details",
        "Review all fetched annotation rows and native molecular functions while preserving ordered source payloads, qualifiers and raw records. Distinguish carbohydrate phosphotransfer and target-specific regulatory activities from nitrogen-relay family membership; no NEW rows.",
    ]
    r = subprocess.run(cmd, cwd=w, env=env, capture_output=True, text=True)
    (c / f"ECOLI-{gene}-history-create.log").write_text(r.stdout + r.stderr)
    assert r.returncode == 0
    h = next(
        line
        for line in r.stdout.splitlines()
        if line.startswith("history/") and line.endswith(".yaml")
    )
    for label, cmd in [
        ("validate", ["just", "validate", "ECOLI", gene]),
        ("history", ["just", "validate-history", h]),
        ("render", ["just", "render", "ECOLI", gene]),
    ]:
        with (c / f"ECOLI-{gene}-{label}.log").open("w") as f:
            r = subprocess.run(cmd, cwd=w, env=env, stdout=f, stderr=subprocess.STDOUT)
        rows.append(
            {
                "gene": gene,
                "check": label,
                "command": cmd,
                "exit_code": r.returncode,
                "history": h,
            }
        )
        print(gene, label, r.returncode, flush=True)
    (c / "ecoli-check-progress.json").write_text(json.dumps(rows, indent=2) + "\n")
(c / "ecoli-checks.json").write_text(
    json.dumps(
        {
            "completed_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "checks": rows,
        },
        indent=2,
    )
    + "\n"
)
