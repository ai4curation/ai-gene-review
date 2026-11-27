"""Run the explicitly selected questions without overwriting existing reports.

Each invocation appends an execution record. A prior running or failed attempt
is never automatically restarted; inspect its process and provider state first.
"""
from concurrent.futures import ThreadPoolExecutor
import argparse
import fcntl
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import subprocess
import time
import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
RUNS = HERE / "adjudication-runs"


def run(request):
    organism, gene, slug = (request[k] for k in ("organism", "gene", "slug"))
    key = f"{organism}--{gene}--{slug}"
    state = RUNS / f"{key}.json"
    report = ROOT / "genes" / organism / gene / f"{gene}-hypotheses" / slug / "openscientist.md"
    if request.get("execution") or state.exists():
        print(f"SKIP recorded execution: {key}", flush=True)
        return
    if report.exists():
        print(f"EXISTING report needs incorporation: {key}", flush=True)
        return
    command = ["just", "gene-hypothesis-research", "openscientist", organism, gene,
               "--focus-type", "function-assignment", "--hypothesis", request["hypothesis"], "--slug", slug]
    log = RUNS / f"{key}.log"
    data = dict(gene_file=f"genes/{organism}/{gene}/{gene}-ai-review.yaml",
                term_ids=request["term_ids"], report=str(report.relative_to(ROOT)),
                started=datetime.now(timezone.utc).isoformat(), launcher_pid=os.getpid(),
                command=command, status="starting")
    with log.open("x") as stream:
        data["status"] = "waiting_for_submission_slot"
        state.write_text(json.dumps(data, indent=2) + "\n")
        while True:
            # Bound submissions across separate invocations, so focused follow-ups
            # do not spend the provider's timeout waiting behind our own jobs.
            with (RUNS / ".submission.lock").open("a") as lock:
                fcntl.flock(lock, fcntl.LOCK_EX)
                active = 0
                for candidate in RUNS.glob("*.json"):
                    try:
                        prior = json.loads(candidate.read_text())
                    except json.JSONDecodeError:
                        # Another runner may be publishing its state right now.
                        active += 3
                        continue
                    if prior.get("status") != "running" or not prior.get("pid"):
                        continue
                    try:
                        os.kill(prior["pid"], 0)
                    except ProcessLookupError:
                        continue
                    active += 1
                if active < 3:
                    process = subprocess.Popen(command, cwd=ROOT, stdout=stream, stderr=subprocess.STDOUT)
                    data.update(pid=process.pid, status="running")
                    state.write_text(json.dumps(data, indent=2) + "\n")
                    break
            time.sleep(10)
        print(f"RUNNING {key} pid={process.pid}", flush=True)
        code = process.wait()
    data.update(finished=datetime.now(timezone.utc).isoformat(), exit_code=code,
                status="report_ready" if code == 0 and report.exists() and report.stat().st_size else "failed_needs_inspection")
    state.write_text(json.dumps(data, indent=2) + "\n")
    print(f"{data['status'].upper()} {key}", flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--only", action="append", help="Run only this organism/gene; repeatable")
    args = parser.parse_args()
    RUNS.mkdir(exist_ok=True)
    requests = yaml.safe_load((HERE / "adjudication-requests.yaml").read_text())["requests"]
    if args.only:
        requests = [r for r in requests if f"{r['organism']}/{r['gene']}" in args.only]
    with ThreadPoolExecutor(max_workers=3) as executor:
        list(executor.map(run, requests))
