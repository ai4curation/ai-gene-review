"""Launch the four prepared fly hypotheses once and collect provider outputs.

Requires OPENSCIENTIST_API_KEY in the environment. Refuses an existing local
status file or matching remote hypothesis to prevent accidental duplicate jobs.
Provider reports remain separate from curation judgments.
"""

import json
import os
import subprocess
import time
from pathlib import Path
from datetime import datetime, timezone
import requests

root = Path(__file__).resolve().parents[4]
os.chdir(root)
selection_dir = Path(__file__).resolve().parent
state_path = selection_dir / "run-status.json"
log_dir = Path("/tmp/fly41-openscientist-logs")
log_dir.mkdir(exist_ok=True)
selected = json.loads((selection_dir / "selection.json").read_text())
base = os.environ.get("OPENSCIENTIST_URL", "https://www.openscientist.io").rstrip("/")
headers = {"Authorization": "Bearer " + os.environ["OPENSCIENTIST_API_KEY"]}


def now():
    return datetime.now(timezone.utc).isoformat()


def jobs():
    r = requests.get(base + "/api/v1/jobs", headers=headers, timeout=30)
    r.raise_for_status()
    return r.json()["jobs"]


if state_path.exists():
    raise SystemExit("Refusing duplicate launch: run-status.json already exists")
initial_jobs = jobs()
for s in selected:
    if any(s["hypothesis"] in j.get("research_question", "") for j in initial_jobs):
        raise SystemExit(
            "A matching investigation already exists; inspect remote status before any resubmission: "
            + s["gene"]
        )
baseline = {j["id"] for j in initial_jobs}
state = {
    "started_at": now(),
    "runner_pid": os.getpid(),
    "max_iterations": 3,
    "api_timeout_seconds": 7200,
    "wrapper_timeout_seconds": 8100,
    "jobs": [],
}
processes = []


def save():
    state["last_checked_at"] = now()
    temp = state_path.with_suffix(".tmp")
    temp.write_text(json.dumps(state, indent=2) + "\n")
    temp.replace(state_path)


for s in selected:
    report = root / s["expected_report"]
    if report.exists():
        raise SystemExit("Report already exists: " + str(report))
    log = log_dir / (s["gene"] + ".log")
    env = os.environ.copy()
    env["UV_NO_SYNC"] = "1"
    env["PYTHONUNBUFFERED"] = "1"
    with log.open("w") as out:
        p = subprocess.Popen(
            s["launch_argv"],
            cwd=root,
            env=env,
            stdout=out,
            stderr=subprocess.STDOUT,
            start_new_session=True,
        )
    record = {
        "gene": s["gene"],
        "accession": s["accession"],
        "hypothesis": s["hypothesis"],
        "launched_at": now(),
        "local_pid": p.pid,
        "local_status": "RUNNING",
        "upstream_status": "NOT_YET_CONFIRMED",
        "expected_report": s["expected_report"],
        "log_file": str(log),
    }
    state["jobs"].append(record)
    processes.append(p)
    save()
while True:
    try:
        remote = jobs()
        state.pop("monitor_error", None)
        for item in state["jobs"]:
            matches = [
                j
                for j in remote
                if j["id"] not in baseline
                and item["hypothesis"] in j.get("research_question", "")
            ]
            if len(matches) == 1:
                j = matches[0]
                for k in [
                    "status",
                    "current_iteration",
                    "max_iterations",
                    "created_at",
                    "updated_at",
                ]:
                    if k in j:
                        item["upstream_" + k] = j[k]
                item["job_id"] = j["id"]
            elif len(matches) > 1:
                item["monitor_warning"] = (
                    "Multiple matching upstream jobs; do not resubmit"
                )
    except Exception as e:
        state["monitor_error"] = type(e).__name__
    for item, p in zip(state["jobs"], processes):
        code = p.poll()
        if code is not None:
            item["local_exit_code"] = code
            report = root / item["expected_report"]
            size = report.stat().st_size if report.exists() else 0
            item["report_bytes"] = size
            artifacts = report.parent / "openscientist_artifacts"
            item["artifact_file_count"] = (
                sum(f.is_file() for f in artifacts.rglob("*"))
                if artifacts.exists()
                else 0
            )
            item["local_status"] = (
                "REPORT_DOWNLOADED" if size else "FINISHED_WITHOUT_REPORT"
            )
            item.setdefault("local_finished_at", now())
    save()
    if all(p.poll() is not None for p in processes):
        break
    time.sleep(30)
state["finished_at"] = now()
save()
