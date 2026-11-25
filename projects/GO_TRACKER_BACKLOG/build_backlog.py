"""Build the GO tracker backlog catalog (backlog.yaml).

Joins old open issues from the geneontology/go-ontology tracker with the
current GO edit file and this repository's gene folders, so each issue
carries the GO terms it names, their current status, and how many genes in
``genes/`` have GOA rows for them. Nothing is posted to GitHub.

Fetch the issues first (read-only search API; adjust the date as needed):

    gh api -X GET search/issues \\
      -f q='repo:geneontology/go-ontology is:issue is:open created:<2023-01-01' \\
      -f sort=created -f order=asc -f per_page=100 --paginate \\
      --jq '.items[] | {number, title, created_at, updated_at, comments,
            labels: [.labels[].name], body: (.body // "")}' > issues.jsonl

Then:

    python projects/GO_TRACKER_BACKLOG/build_backlog.py \\
      --issues issues.jsonl --obo ../go-ontology/src/ontology/go-edit.obo \\
      --out projects/GO_TRACKER_BACKLOG/backlog.yaml

The issue payload is an input only: do not commit it.
"""

from __future__ import annotations

import argparse
import collections
import datetime as dt
import json
import re
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[2]
TRACKER = "https://github.com/geneontology/go-ontology/issues/"

# Labels marking tracker issues about build, QC, relations, mappings or
# documentation rather than the meaning of terms. Gene review cannot move these.
NON_CONTENT_LABELS = {
    "Infrastructure",
    "QC",
    "documentation",
    "enhancement",
    "relations",
    "xref & mappings",
    "subsets",
    "go2rhea",
    "ontology alignment",
}
GO_ID = re.compile(r"GO[:_](\d{7})")


def parse_obo(path: Path) -> dict[str, dict]:
    """Minimal stanza parser: id, name, namespace, obsolete, parents, alt_ids."""
    terms: dict[str, dict] = {}
    cur: dict | None = None
    with path.open() as fh:
        for raw in fh:
            line = raw.rstrip("\n")
            if line.startswith("["):
                cur = {"parents": [], "alt_ids": [], "obsolete": False} if line == "[Term]" else None
                continue
            if cur is None or ": " not in line:
                continue
            key, val = line.split(": ", 1)
            if key == "id":
                terms[val] = cur
            elif key == "name":
                cur["name"] = val
            elif key == "namespace":
                cur["namespace"] = val
            elif key == "is_obsolete" and val.startswith("true"):
                cur["obsolete"] = True
            elif key == "alt_id":
                cur["alt_ids"].append(val.split()[0])
            elif key == "is_a" or (key == "intersection_of" and val.startswith("GO:")):
                cur["parents"].append(val.split()[0])
            elif key in ("relationship", "intersection_of") and val.startswith("part_of GO:"):
                cur["parents"].append(val.split()[1])
    return terms


def descendants(children: dict[str, set[str]], root: str) -> set[str]:
    seen: set[str] = set()
    stack = [root]
    while stack:
        for kid in children.get(stack.pop(), ()):
            if kid not in seen:
                seen.add(kid)
                stack.append(kid)
    return seen


def index_goa(genes_root: Path) -> tuple[dict[str, set[str]], set[str]]:
    """GO id -> genes (org/GENE) with a GOA row; plus the set of reviewed genes."""
    goa: dict[str, set[str]] = collections.defaultdict(set)
    reviewed: set[str] = set()
    for tsv in sorted(genes_root.glob("*/*/*-goa.tsv")):
        key = f"{tsv.parent.parent.name}/{tsv.parent.name}"
        if tsv.with_name(tsv.name.replace("-goa.tsv", "-ai-review.yaml")).exists():
            reviewed.add(key)
        with tsv.open(errors="replace") as fh:
            next(fh, None)
            for line in fh:
                cols = line.split("\t")
                if len(cols) > 4 and cols[4].startswith("GO:"):
                    goa[cols[4]].add(key)
    return goa, reviewed


def project_citations(projects_root: Path, skip: Path) -> dict[int, list[str]]:
    cited: dict[int, set[str]] = collections.defaultdict(set)
    pattern = re.compile(r"go-ontology/issues/(\d+)")
    for md in projects_root.rglob("*.md"):
        if skip in md.parents or md == skip.with_suffix(".md"):
            continue
        top = md.relative_to(projects_root).parts[0].removesuffix(".md")
        for num in pattern.findall(md.read_text(errors="replace")):
            cited[int(num)].add(top)
    return {k: sorted(v) for k, v in cited.items()}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--issues", type=Path, required=True)
    ap.add_argument("--obo", type=Path, required=True)
    ap.add_argument("--genes", type=Path, default=REPO / "genes")
    ap.add_argument("--projects", type=Path, default=REPO / "projects")
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()

    terms = parse_obo(args.obo)
    alt = {a: tid for tid, t in terms.items() for a in t["alt_ids"]}
    children: dict[str, set[str]] = collections.defaultdict(set)
    for tid, t in terms.items():
        for parent in t["parents"]:
            children[parent].add(tid)
    goa, reviewed = index_goa(args.genes)
    cited = project_citations(args.projects, Path(__file__).resolve().parent)

    rows = []
    for line in args.issues.read_text().splitlines():
        issue = json.loads(line)
        labels = sorted(issue.get("labels") or [])
        text = f"{issue.get('title') or ''}\n{issue.get('body') or ''}"
        named = sorted({f"GO:{n}" for n in GO_ID.findall(text)})
        term_rows = []
        direct: set[str] = set()
        branch: set[str] = set()
        for gid in named:
            tid = alt.get(gid, gid)
            t = terms.get(tid)
            hit = goa.get(gid, set()) | goa.get(tid, set())
            below = set(hit)
            for d in descendants(children, tid) if t else ():
                below |= goa.get(d, set())
            direct |= hit
            branch |= below
            term_rows.append(
                {
                    "id": gid,
                    "label": t.get("name") if t else None,
                    "status": "MISSING" if t is None else ("OBSOLETE" if t["obsolete"] else "CURRENT"),
                    **({"merged_into": tid} if tid != gid else {}),
                    "genes_with_rows": len(hit),
                    "reviewed_genes_with_rows": len(hit & reviewed),
                }
            )
        rows.append(
            {
                "number": issue["number"],
                "url": f"{TRACKER}{issue['number']}",
                "title": (issue.get("title") or "").strip(),
                "created": issue["created_at"][:10],
                "updated": issue["updated_at"][:10],
                "comments": issue.get("comments", 0),
                "labels": labels,
                "scope": "NON_CONTENT" if set(labels) & NON_CONTENT_LABELS else "CONTENT",
                "n_terms_named": len(term_rows),
                # Keep terms that touch a reviewed gene or are no longer current;
                # the rest are counted in n_terms_named only.
                "terms": [t for t in term_rows if t["reviewed_genes_with_rows"] or t["status"] != "CURRENT"],
                "reviewed_genes_direct": len(direct & reviewed),
                "reviewed_genes_including_descendants": len(branch & reviewed),
                "cited_by_projects": cited.get(issue["number"], []),
            }
        )
    rows.sort(key=lambda r: r["number"])
    doc = {
        "generated": dt.date.today().isoformat(),
        "source": "geneontology/go-ontology open issues (GitHub search API)",
        "obo": "go-edit.obo from a geneontology/go-ontology checkout",
        "non_content_labels": sorted(NON_CONTENT_LABELS),
        "n_issues": len(rows),
        "n_content": sum(r["scope"] == "CONTENT" for r in rows),
        "reviewed_genes_in_repo": len(reviewed),
        "issues": rows,
    }
    args.out.write_text(yaml.safe_dump(doc, sort_keys=False, allow_unicode=True, width=100))
    print(f"wrote {args.out}: {len(rows)} issues, {doc['n_content']} content")


if __name__ == "__main__":
    main()
