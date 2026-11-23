"""Scoped finish with durable per-gene history markers; safe to resume."""

from pathlib import Path
import subprocess
import json

out = Path(__file__).resolve().parent
base = json.loads(
    Path(
        ".cache/module-audit-logs/flavonoid-20261106/bradu-seed-baseline.json"
    ).read_text()
)
marker = out / "history-markers.json"
history = json.loads(marker.read_text()) if marker.exists() else {}
results = {}
for r in base:
    g = r["gene"]
    if g not in history:
        # Record helper output immediately; never repeat a successful scaffold.
        q = subprocess.run(
            [
                "just",
                "new-history",
                "--kind",
                "gene",
                "--organism",
                "BRADU",
                "--slug",
                g,
                "--event",
                "REVIEW",
                "--outcome",
                "changed",
                "--actor-name",
                "codex",
                "--agent-tool",
                "codex",
                "--summary",
                f"Complete evidence-qualified USDA110 {g} review",
                "--sections",
                "description,existing_annotations,core_functions,references,knowledge_gaps,notes",
                "--details",
                "Review every seeded row, preserve machine payloads and raw records, compare frozen HERSS sequences and primary evidence, distinguish inferred reaction class from unknown native substrate and pathway contribution. Genuine Falcon attempt failed403 with no provider report. Focused validation and rendering recorded in bradu-panel audit artifacts.",
            ],
            capture_output=True,
            text=True,
        )
        (out / (g + "-history-helper.log")).write_text(q.stdout + q.stderr)
        if q.returncode:
            raise RuntimeError(q.stdout + q.stderr)
        candidates = [
            line.strip()
            for line in q.stdout.splitlines()
            if line.strip().startswith("history/") and line.strip().endswith(".yaml")
        ]
        if len(candidates) != 1:
            raise RuntimeError("Check helper output before any retry: " + q.stdout)
        history[g] = candidates[0]
        marker.write_text(json.dumps(history, indent=2) + "\n")
    for name, args in [
        ("history", ["just", "validate-history", history[g]]),
        ("render", ["just", "render", "BRADU", g]),
    ]:
        q = subprocess.run(args, capture_output=True, text=True)
        (out / (g + "-" + name + ".log")).write_text(q.stdout + q.stderr)
        results[g + "-" + name] = q.returncode
        print(g, name, q.returncode, flush=True)
    (out / "finish-results.json").write_text(json.dumps(results, indent=2) + "\n")
