"""Finalize pinned baseline, official candidate identities and live overlap audit."""

import concurrent.futures
import hashlib
import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path


P = Path(__file__).resolve().parent


def run(args):
    return subprocess.check_output(args, text=True)


def dump(name, obj):
    (P / name).write_text(json.dumps(obj, indent=2) + "\n")


initial = json.loads((P / "main-snapshot.json").read_text())
head = initial["main_sha"]
live = run(
    ["gh", "api", "repos/ai4curation/ai-gene-review/commits/main", "--jq", ".sha"]
).strip()
assert live == head, (live, head)
old = {x["number"]: x for x in json.loads((P / "open-pr-files.json").read_text())}
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


def files(pr):
    prior = old.get(pr["number"])
    if prior and prior["headRefOid"] == pr["headRefOid"]:
        return {**pr, "files": prior["files"]}
    pages = json.loads(
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
    return {**pr, "files": [f["filename"] for page in pages for f in page]}


with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    current = list(pool.map(files, prs))
dump("final-open-pr-files.json", current)
expanded = json.loads((P / "expanded-overlap.json").read_text())
prefixes = expanded["scope_prefixes"] + ["interpro/panther/PTHR43586/"]
prefixes += [
    f"genes/THET2/{g}/"
    for g in ["mnmA", "iscS", "sufS", "TT_C1727", "TT_C0087", "TT_C1373"]
]
prefixes += [
    p.replace("genes/", "history/genes/")
    for p in prefixes
    if p.startswith("genes/THET2/")
]
hits = []
for pr in current:
    overlap = [
        x
        for x in pr["files"]
        if x == initial["module"] or any(x.startswith(p) for p in prefixes)
    ]
    if overlap:
        hits.append(
            {
                **{k: v for k, v in pr.items() if k != "files"},
                "overlap": sorted(overlap),
            }
        )
dump(
    "final-overlap.json",
    {
        "captured_utc": datetime.now(timezone.utc).isoformat(),
        "main_sha": live,
        "open_pr_count": len(current),
        "scope_prefixes": prefixes,
        "hits": hits,
    },
)
paths = run(["git", "ls-tree", "-r", "--name-only", head]).splitlines()
base = json.loads((P / "expanded-baseline.json").read_text())
relevant = set(base["files"])
relevant.update(x for x in paths if x.startswith("interpro/panther/PTHR43586/"))
pmids = set()
for path in relevant:
    if path.endswith(".yaml"):
        pmids.update(re.findall(r"PMID:(\d+)", run(["git", "show", head + ":" + path])))
relevant.update(
    f"publications/PMID_{n}.md" for n in pmids if f"publications/PMID_{n}.md" in paths
)
base["files"] = {
    x: hashlib.sha256(
        subprocess.check_output(["git", "show", head + ":" + x])
    ).hexdigest()
    for x in sorted(relevant)
}
base["family_review_presence"] = {
    f: f"interpro/panther/{f}/{f}-review.yaml" in paths
    for f in base["relevant_families"] + ["PTHR43586"]
}
base["live_main_verified"] = live
base["normal_publication_cache_count"] = sum(
    x.startswith("publications/") for x in relevant
)
dump("final-baseline.json", base)
candidates = []
for name in [
    "identity-ecoli.json",
    "identity-bacsu.json",
    "identity-thermus-descendants.json",
    "identity-thermus-donors.json",
    "identity-human-trmu.json",
]:
    for x in json.loads((P / name).read_text()).get("results", []):
        genes = x.get("genes", [])
        candidates.append(
            {
                "accession": x["primaryAccession"],
                "entry_name": x["uniProtkbId"],
                "taxon": x["organism"],
                "genes": genes,
                "sequence_length": x["sequence"]["length"],
                "sequence_sha256": hashlib.sha256(
                    x["sequence"]["value"].encode()
                ).hexdigest(),
                "panther": [
                    y
                    for y in x["uniProtKBCrossReferences"]
                    if y["database"] == "PANTHER"
                ],
                "domains": [
                    y
                    for y in x["uniProtKBCrossReferences"]
                    if y["database"] in ["InterPro", "HAMAP"]
                ],
                "source": name,
                "source_sha256": hashlib.sha256((P / name).read_bytes()).hexdigest(),
            }
        )
dump("candidate-identities.json", candidates)
print(
    json.dumps(
        {
            "open_prs": len(current),
            "overlaps": hits,
            "baseline_files": len(relevant),
            "official_candidates_and_controls": len(candidates),
        },
        indent=2,
    )
)
