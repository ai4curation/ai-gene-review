import hashlib
import json
import re
import subprocess
from pathlib import Path
import yaml

P = Path(__file__).resolve().parent
base = json.loads((P / "main-snapshot.json").read_text())
head = base["main_sha"]
paths = subprocess.check_output(
    ["git", "ls-tree", "-r", "--name-only", head], text=True
).splitlines()
fams = set()
for raw in P.glob("genes__*-uniprot.txt"):
    fams.update(re.findall(r"DR   PANTHER; (PTHR\d+);", raw.read_text()))
genes = [str(Path(x).parent) + "/" for x in base["reviews"]]
genes += [
    f"genes/ECOLI/{g}/"
    for g in ["iscS", "tusA", "tusB", "tusC", "tusD", "tusE", "mnmA"]
]
genes += [f"genes/BACSU/{g}/" for g in ["yrvO", "iscS1", "mnmA"]]
prefixes = genes + [f"interpro/panther/{f}/" for f in sorted(fams)]
prefixes += ["history/modules/bacterial_mnma_trna_thiolation/"] + [
    g.replace("genes/", "history/genes/") for g in genes
]
relevant = sorted(
    x for x in paths if x == base["module"] or any(x.startswith(p) for p in prefixes)
)
hashes = {
    x: hashlib.sha256(
        subprocess.check_output(["git", "show", head + ":" + x])
    ).hexdigest()
    for x in relevant
}
rows = {}
for x in relevant:
    if x.endswith("-ai-review.yaml"):
        d = yaml.safe_load(subprocess.check_output(["git", "show", head + ":" + x]))
        a = d.get("existing_annotations", [])
        rows[x] = {
            "id": d["id"],
            "rows": len(a),
            "status": d.get("status"),
            "historical_NEW": sum(
                r.get("review", {}).get("action") == "NEW" for r in a
            ),
            "active_NEW": sum(
                r.get("review", {}).get("action") == "NEW" and not r.get("retired")
                for r in a
            ),
        }
(P / "expanded-baseline.json").write_text(
    json.dumps(
        {
            "main_sha": head,
            "relevant_families": sorted(fams),
            "files": hashes,
            "reviews": rows,
        },
        indent=2,
    )
    + "\n"
)
hits = []
for pr in json.loads((P / "open-pr-files.json").read_text()):
    overlap = sorted(
        x
        for x in pr["files"]
        if x == base["module"] or any(x.startswith(p) for p in prefixes)
    )
    if overlap:
        hits.append(
            {**{k: v for k, v in pr.items() if k != "files"}, "overlap": overlap}
        )
(P / "expanded-overlap.json").write_text(
    json.dumps(
        {"open_pr_count": 282, "scope_prefixes": prefixes, "hits": hits}, indent=2
    )
    + "\n"
)
print(json.dumps({"families": sorted(fams), "reviews": rows, "hits": hits}, indent=2))
