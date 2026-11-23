"""Run only six scoped checks, with durable command/result records."""

import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import time

OUT = Path(__file__).resolve().parent
ROOT = next(p for p in OUT.parents if (p / "pyproject.toml").exists())
GENES = [("BORPE", f"BP{n}") for n in range(3757, 3762)] + [("PSEAE", "ttg2D")]
ENV = os.environ | {"UV_NO_SYNC": "1", "PYTHONDONTWRITEBYTECODE": "1"}


def run(name, command):
    receipt = OUT / "logs" / f"{name}.json"
    if receipt.exists():
        raise RuntimeError(f"Existing receipt must not be overwritten: {receipt}")
    free = shutil.disk_usage(ROOT).free
    if free < 256 * 1024**2:
        raise RuntimeError(f"Low disk space before {name}: {free}")
    log = OUT / "logs" / f"{name}.log"
    start = time.time()
    print(f"START {name}", flush=True)
    receipt.write_text(json.dumps({"command": command, "started": start, "log": str(log.relative_to(ROOT))}, indent=2) + "\n")
    with log.open("w") as stream:
        result = subprocess.run(command, cwd=ROOT, env=ENV, stdout=stream, stderr=subprocess.STDOUT)
    record = {"command": command, "started": start, "seconds": time.time() - start, "exit_code": result.returncode, "log": str(log.relative_to(ROOT)), "free_before": free, "free_after": shutil.disk_usage(ROOT).free}
    receipt.write_text(json.dumps(record, indent=2) + "\n")
    print(f"END {name}: {result.returncode}", flush=True)
    if result.returncode:
        raise RuntimeError(f"Failed {name}; inspect {log}")
    return log


def main():
    phase = sys.argv[1]
    if phase == "validate":
        for org, gene in GENES:
            run(f"{org}-{gene}-backfill", ["just", "backfill-record-sections", "--dry-run", f"genes/{org}/{gene}/{gene}-ai-review.yaml"])
            run(f"{org}-{gene}-validate", ["just", "validate", org, gene])
    elif phase == "history-render":
        for org, gene in GENES:
            detail = "PR6198 follow-up: preserved all prior ordered annotation payloads, qualifiers and historical NEW lifecycle. Replaced generic summaries and weak evidence attachments with claim-specific source text; distinguished target assays from ortholog inference. "
            if gene == "BP3761":
                detail += "Added one direct structural PE-binding proposal and refined binding core from exact mature-target PDB 11HY/11IF evidence; no native-flux or exclusive-specificity claim. "
            elif gene == "ttg2D":
                detail += "Added target phospholipid-binding and tagged native-host periplasm-location proposals from PMID33837253; no added process annotation or membrane-to-membrane flux claim. "
            elif gene == "BP3760":
                detail += "Replaced four cargo-composition quotations with actual E. coli MlaA-assisted loading evidence, retaining explicit target localization and pathway inference. "
            detail += "Focused gene validation rerun successfully after the historical ENOSPC attempt; logs and preservation proof are in the additive completion-20261107 consultation."
            log = run(f"{org}-{gene}-new-history", ["just", "new-history", "--kind", "gene", "--organism", org, "--slug", gene, "--event", "EDIT", "--outcome", "changed", "--actor-name", "codex", "--agent-tool", "codex", "--pr", "6198", "--sections", "existing_annotations,core_functions,references,notes", "--summary", f"Ground {gene} PR6198 follow-up in target-specific evidence", "--details", detail])
            history = log.read_text().splitlines()[-1].strip()
            assert history.startswith("history/genes/") and (ROOT / history).exists(), history
            (OUT / f"{org}-{gene}-history.json").write_text(json.dumps({"path": history}, indent=2) + "\n")
            run(f"{org}-{gene}-history-validate", ["just", "validate-history", history])
            run(f"{org}-{gene}-render", ["just", "render", org, gene])
    else:
        raise ValueError(phase)


if __name__ == "__main__":
    main()
