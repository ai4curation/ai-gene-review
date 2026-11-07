from pathlib import Path
import os
import subprocess
import json
import hashlib
import re
from datetime import datetime, timezone

ROOT = Path("/Users/cjm/worktrees/aigr-nhej-audit-recovery")
OUT = (
    ROOT
    / "analysis/module_audits/bacterial_nonhomologous_end_joining/reacquisition-20261107"
)
OUT.mkdir(exist_ok=False)
ENV = dict(
    os.environ,
    PYTHONDONTWRITEBYTECODE="1",
    UV_PROJECT_ENVIRONMENT="/Users/cjm/orca/workspaces/ai-gene-review/aigr-modules-taxon/.venv",
    UV_NO_SYNC="1",
    PYTHONPATH=str(ROOT / "src"),
)
PANEL = [
    ("PSEAE", "ku", "Q9I1W5"),
    ("PSEAE", "ligD", "Q9I1X7"),
    ("MYCTU", "mku", "P9WKD9"),
    ("MYCTU", "ligD", "P9WNV3"),
    ("BACSU", "ku", "O34859"),
    ("BACSU", "ligd", "O34398"),
]


def run(command, name):
    log = OUT / (name + ".log")
    with log.open("w") as stream:
        result = subprocess.run(
            command, cwd=ROOT, env=ENV, stdout=stream, stderr=subprocess.STDOUT
        )
    receipt = {
        "command": command,
        "exit_code": result.returncode,
        "finished_at": datetime.now(timezone.utc).isoformat(),
    }
    (OUT / (name + ".json")).write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps({"step": name, "exit_code": result.returncode}), flush=True)
    assert result.returncode == 0, name


for organism, gene, accession in PANEL:
    assert not (ROOT / f"genes/{organism}/{gene}/{gene}-ai-review.yaml").exists()
    run(
        [
            "just",
            "fetch-gene",
            organism,
            gene,
            "--uniprot-id",
            accession,
            "--no-fetch-titles",
        ],
        f"{organism}-{gene}-fetch",
    )

pmids = set(
    "14985346 15499016 15520014 16046407 16476729 16497325 17174332 17293412 17376770 17947582 20616014 21255731 22084199 24239356 25355514 26826709 30976810 17938628 30746801 34901162 33078828 40328696 42953966 41957403 42306942 20018881 16023671 12215643 15897197 25942369 36475478 18203718 17496093 33590005".split()
)
for organism, gene, _ in PANEL + [
    ("PSEPK", "ku", "Q88HU8"),
    ("PSEPK", "ligD", "Q88HU3"),
]:
    pmids.update(
        re.findall(
            r"PMID:(\d+)",
            (ROOT / f"genes/{organism}/{gene}/{gene}-ai-review.yaml").read_text(),
        )
    )
sources = {}
for pmid in sorted(pmids):
    relative = f"publications/PMID_{pmid}.md"
    path = ROOT / relative
    if path.exists():
        origin = "existing_cache"
    else:
        existing = subprocess.run(
            ["git", "show", "HEAD:" + relative], cwd=ROOT, capture_output=True
        )
        if existing.returncode == 0:
            path.parent.mkdir(exist_ok=True)
            path.write_bytes(existing.stdout)
            origin = "exact_HEAD_materialization"
        else:
            run(["uv", "run", "ai-gene-review", "fetch-pmid", pmid], "PMID_" + pmid)
            origin = "normal_fetch"
    sources[relative] = {
        "origin": origin,
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
    }
    (OUT / "publication-sources.json").write_text(json.dumps(sources, indent=2) + "\n")
print(
    json.dumps({"seeded_genes": len(PANEL), "publication_sources": len(sources)}),
    flush=True,
)
