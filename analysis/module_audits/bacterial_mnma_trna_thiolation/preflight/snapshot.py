from pathlib import Path
import subprocess
import json
import hashlib
import concurrent.futures
import yaml

P = Path(".cache/module-audit-logs/mnma-preflight-20261107")


def run(cmd):
    return subprocess.check_output(cmd, text=True)


head = run(["git", "rev-parse", "origin/main"]).strip()
module = "modules/bacterial_mnma_trna_thiolation.yaml"
text = run(["git", "show", head + ":" + module])
(P / "module.yaml").write_text(text)
paths = run(["git", "ls-tree", "-r", "--name-only", head]).splitlines()
doc = yaml.safe_load(text)
acc = set()
fams = set()


def walk(v):
    if isinstance(v, dict):
        if v.get("id", "").startswith("UniProtKB:"):
            acc.add(v["id"].split(":")[1])
        if v.get("id", "").startswith("PANTHER:PTHR"):
            fams.add(v["id"].split(":")[1])
        for child in v.values():
            walk(child)
    elif isinstance(v, list):
        for child in v:
            walk(child)


walk(doc)
reviews = {}
families = {}
for path in paths:
    if (
        path.startswith("genes/")
        and path.endswith("-ai-review.yaml")
        and any(
            "/" + s + "/" in path
            for s in [
                "iscS",
                "tusA",
                "tusB",
                "tusC",
                "tusD",
                "tusE",
                "mnmA",
                "PP_3994",
                "PP_3995",
                "yrvO",
            ]
        )
    ):
        s = run(["git", "show", head + ":" + path])
        d = yaml.safe_load(s)
        if d.get("id") in acc:
            reviews[path] = {
                "accession": d["id"],
                "status": d.get("status"),
                "rows": len(d.get("existing_annotations", [])),
                "sha256": hashlib.sha256(s.encode()).hexdigest(),
            }
            (P / (path.replace("/", "__"))).write_text(s)
# Incorporate actual PANTHER classifications from module target raw records.
for review_path in reviews:
    gene = review_path.split("/")[-2]
    raw_path = "/".join(review_path.split("/")[:-1]) + "/" + gene + "-uniprot.txt"
    raw = run(["git", "show", head + ":" + raw_path])
    (P / (raw_path.replace("/", "__"))).write_text(raw)
    import re

    fams.update(re.findall(r"DR   PANTHER; (PTHR[0-9]+);", raw))
for fam in sorted(fams):
    path = f"interpro/panther/{fam}/{fam}-review.yaml"
    if path in paths:
        s = run(["git", "show", head + ":" + path])
        families[path] = {"sha256": hashlib.sha256(s.encode()).hexdigest()}
        (P / (fam + "-review.yaml")).write_text(s)
initial = {
    "main_sha": head,
    "module": module,
    "module_sha256": hashlib.sha256(text.encode()).hexdigest(),
    "accessions": sorted(acc),
    "reviews": reviews,
    "families": families,
    "history_paths": [
        p
        for p in paths
        if p.startswith("history/modules/bacterial_mnma_trna_thiolation/")
    ],
}
(P / "main-snapshot.json").write_text(json.dumps(initial, indent=2) + "\n")
prs = json.loads(
    run(
        [
            "gh",
            "pr",
            "list",
            "--state",
            "open",
            "--limit",
            "1000",
            "--json",
            "number,title,url,headRefOid",
        ]
    )
)
(P / "open-prs.json").write_text(json.dumps(prs, indent=2) + "\n")


def fetch(pr):
    data = json.loads(
        run(
            [
                "gh",
                "api",
                f"repos/ai4curation/ai-gene-review/pulls/{pr['number']}/files?per_page=100",
                "--paginate",
                "--slurp",
            ]
        )
    )
    files = [x["filename"] for page in data for x in page]
    return {**pr, "files": files}


allfiles = list(concurrent.futures.ThreadPoolExecutor(max_workers=6).map(fetch, prs))
(P / "open-pr-files.json").write_text(json.dumps(allfiles, indent=2) + "\n")
owned = {module, *reviews, *families}
prefixes = [str(Path(x).parent) + "/" for x in [*reviews, *families]]


def overlaps(files):
    return sorted(
        x
        for x in files
        if x == module
        or any(x.startswith(prefix) for prefix in prefixes)
        or x.startswith("history/modules/bacterial_mnma_trna_thiolation/")
    )


hits = [
    {
        **{k: v for k, v in x.items() if k != "files"},
        "overlap": overlaps(x["files"]),
    }
    for x in allfiles
    if overlaps(x["files"])
]
(P / "overlap.json").write_text(
    json.dumps(
        {"open_pr_count": len(prs), "exact_scope": sorted(owned), "hits": hits},
        indent=2,
    )
    + "\n"
)
print(
    json.dumps(
        {
            "reviews": len(reviews),
            "families": len(families),
            "prs": len(prs),
            "overlap": hits,
        }
    )
)
