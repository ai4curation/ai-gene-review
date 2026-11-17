"""Run focused validation, generated histories and renders sequentially."""

import json
import os
import re
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
ENV = dict(
    os.environ,
    UV_PROJECT_ENVIRONMENT="/Users/cjm/orca/workspaces/ai-gene-review/aigr-modules-taxon/.venv",
    UV_NO_SYNC="1",
    PYTHONPATH=str(ROOT / "src"),
    PYTHONDONTWRITEBYTECODE="1",
)


def run(args, logfile):
    result = subprocess.run(
        args,
        cwd=ROOT,
        env=ENV,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    (HERE / logfile).write_text(result.stdout)
    assert result.returncode == 0, (args, result.stdout[-4000:])
    return {
        "command": args,
        "exit_code": result.returncode,
        "log": str((HERE / logfile).relative_to(ROOT)),
    }, result.stdout


def main():
    assert not (HERE / "handoff.json").exists()
    assert not (HERE / "histories.json").exists(), "Avoid duplicate history creation"
    checks, histories = [], []
    for org, gene in (
        ("PSEAE", "ku"),
        ("PSEAE", "ligD"),
        ("BACSU", "ku"),
        ("BACSU", "ligd"),
    ):
        item, _ = run(["just", "validate", org, gene], f"{org}-{gene}-validate.log")
        checks.append(item)
        item, _ = run(
            ["just", "backfill-record-sections", f"genes/{org}/{gene}", "--dry-run"],
            f"{org}-{gene}-record-sections.log",
        )
        checks.append(item)
        details = (
            "Reconstructed prior documented manual review in a fresh recovery checkout; original historical handoff is not recreated. Manually reviewed every seeded annotation with original ordered payloads intact; no NEW rows or retirements. "
            "Synthesized target-supported DNA end binding, LigD ligation/polymerization and substrate-specific AP/5prime-dRP/PE chemistry. "
            "Distinguished recombinant construct and native strain evidence; preserved target PAINT inheritance without donor-count or missing-assay objections. "
            "Bacillus ligd spelling/raw paths retained with ligD alias; no source cache edits. "
            "Evidence, ontology and preservation receipts: analysis/module_audits/bacterial_nonhomologous_end_joining/pseudomonas-bacillus-recovery-20261107."
        )
        args = [
            "just",
            "new-history",
            "--kind",
            "gene",
            "--organism",
            org,
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
            f"Review {org} {gene} repair functions and inherited annotations",
            "--details",
            details,
            "--sections",
            "description,existing_annotations,references,core_functions,suggested_questions",
        ]
        item, output = run(args, f"{org}-{gene}-history-create.log")
        checks.append(item)
        matches = re.findall(r"history/genes/[^\s]+\.yaml", output)
        assert matches, output
        path = matches[-1]
        histories.append(path)
        (HERE / "histories-in-progress.json").write_text(
            json.dumps(histories, indent=2) + "\n"
        )
        item, _ = run(
            ["just", "validate-history", path], f"{org}-{gene}-history-validate.log"
        )
        checks.append(item)
        item, _ = run(["just", "render", org, gene], f"{org}-{gene}-render.log")
        checks.append(item)
    (HERE / "histories.json").write_text(json.dumps(histories, indent=2) + "\n")
    (HERE / "focused-checks.json").write_text(json.dumps(checks, indent=2) + "\n")
    print(
        json.dumps(
            {"status": "PASS", "checks": len(checks), "histories": histories}, indent=2
        )
    )


if __name__ == "__main__":
    main()
