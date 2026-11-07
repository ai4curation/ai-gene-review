"""Scoped production conformance, tree recomputation and source closure; no fetch/index build."""

from pathlib import Path
import csv
import gzip
import json
import hashlib
import re
from dataclasses import asdict
import yaml
from ai_gene_review.etl.panther_families import load_obo_names
from ai_gene_review.validation.module_validator import load_paint_index
from ai_gene_review.validation.family_residue_validator import (
    check_panther_ids,
    check_node_assessments,
    check_term_assessment_site_refs,
)
from ai_gene_review.validation.family_gene_crosscheck import (
    index_genes_by_family,
    check_scope_violations,
    check_pruning_conflicts,
    check_family_gene_disagreement,
    check_member_exceptions,
)

A = Path(
    "analysis/module_audits/bacterial_nitrogen_regulatory_pts/family-review-20261107"
)
T = Path(
    "analysis/module_audits/bacterial_nitrogen_regulatory_pts/tree-evidence-20261107"
)
F = ["PTHR46244", "PTHR33705", "PTHR47738"]


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def norm(x):
    return re.sub(r"\s+", " ", x).strip()


source_paths = set()
member_sources = {}
members = {}
for fam in F:
    p = Path(f"interpro/panther/{fam}/{fam}-entries.csv")
    source_paths.add(p)
    for r in csv.DictReader(p.open()):
        if r["subfamily"]:
            members[r["id"]] = r["subfamily"]
            member_sources[r["id"]] = str(p)
for p in Path("genes").glob("*/*/*-uniprot.txt"):
    text = p.read_text()
    m = re.search(r"^AC\s+([^;]+);", text, re.M)
    sf = re.search(r"^DR   PANTHER; (PTHR\d+:SF\d+);", text, re.M)
    if m and sf and sf[1].split(":")[0] in F:
        if m[1] in members:
            assert members[m[1]] == sf[1], ("source disagreement", m[1])
        members[m[1]] = sf[1]
        member_sources[m[1]] = str(p)
        source_paths.add(p)
labels = load_obo_names(Path("interpro/panther/panther.obo"))
paint = load_paint_index(Path("interpro/panther"))
gi = index_genes_by_family(Path("genes"))
gene_inputs = sorted(
    {str(g.review_path) for f in F for g in gi.get("PANTHER:" + f, [])}
)
source_paths.update(Path(p) for p in gene_inputs)
assert len(gene_inputs) == 12
result = {
    "gene_review_inputs": gene_inputs,
    "families": {},
    "quotes_checked": 0,
    "titles_checked": 0,
    "production_checks": [],
    "gene_crosschecks": [],
    "source_dependencies": {},
}
for fam in F:
    p = Path(f"interpro/panther/{fam}/{fam}-review.yaml")
    d = yaml.safe_load(p.read_text())
    checks = (
        check_panther_ids(d, labels, members)
        + check_node_assessments(d, paint)
        + check_term_assessment_site_refs(d)
    )
    result["production_checks"] += [asdict(x) for x in checks]
    assert all(x.outcome.value == "PASS" for x in checks)
    cc = (
        check_scope_violations(d, gi)
        + check_pruning_conflicts(d, gi)
        + check_family_gene_disagreement(d, gi)
        + check_member_exceptions(d, gi)
    )
    result["gene_crosschecks"] += [asdict(x) for x in cc]
    assert all(x.verdict.value != "CONFLICT" for x in cc)
    raw = T / f"{fam}-treeinfo.json.gz"
    comp = T / f"{fam}-compact.json"
    source_paths.update(
        [
            raw,
            comp,
            T / f"{fam}-receipt.json",
            Path(f"interpro/panther/{fam}/{fam}-paint.tsv"),
            Path(f"interpro/panther/{fam}/{fam}-metadata.yaml"),
        ]
    )
    tree = json.loads(gzip.decompress(raw.read_bytes()))["search"]["tree_topology"][
        "annotation_node"
    ]
    compact = json.loads(comp.read_text())
    under = {}
    leafdata = {}

    def visit(n):
        node = n["persistent_id"]
        child = n.get("children", {}).get("annotation_node", [])
        if isinstance(child, dict):
            child = [child]
        if not child:
            a = re.search(r"UniProtKB=([^|]+)", n.get("node_name", ""))
            leafdata[node] = {
                "uniprot": a[1] if a else None,
                "subfamily": n.get("prop_sf_id"),
            }
            return [node]
        ls = [leaf for c in child for leaf in visit(c)]
        under[node] = ls
        return ls

    visit(tree)
    for n in d["node_assessments"]:
        bare = n["node_id"].split(":")[1]
        assert under[bare] == compact["under"][bare]
        for leaf_id in under[bare]:
            assert (
                leafdata[leaf_id]["uniprot"] == compact["leaves"][leaf_id]["uniprot"]
                and leafdata[leaf_id]["subfamily"]
                == compact["leaves"][leaf_id]["subfamily"]
            )
    result["families"][fam] = {
        "node_assessments": len(d["node_assessments"]),
        "term_assessments": len(d["term_assessments"]),
        "tree_descendants_recomputed": True,
        "representative_members": sum(
            len(s["representative_members"]) for s in d["subfamilies"]
        ),
    }
    refs = {r["id"]: r for r in d["references"]}

    def resolve(i):
        if i.startswith("PMID:"):
            return Path("publications/PMID_" + i.split(":")[1] + ".md")
        assert i.startswith("file:")
        n = i.removeprefix("file:")
        return Path(n) if Path(n).is_file() else Path("genes") / n

    for i, r in refs.items():
        f = resolve(i)
        assert f.is_file(), i
        source_paths.add(f)
        if i.startswith("PMID:"):
            title = yaml.safe_load(f.read_text().split("---")[1])["title"]
            assert norm(title) == norm(r["title"])
            result["titles_checked"] += 1

    def walk(x):
        if isinstance(x, dict):
            if "reference_id" in x:
                i = x["reference_id"]
                assert i in refs
                i_path = resolve(i)
                assert norm(x["supporting_text"]) in norm(i_path.read_text()), (
                    fam,
                    i,
                    x["supporting_text"],
                )
                result["quotes_checked"] += 1
            for v in x.values():
                walk(v)
        elif isinstance(x, list):
            for v in x:
                walk(v)

    walk(d)
# Preserve all supplied raw family/tree and completed gene inputs byte-for-byte and mode-for-mode.
protected = json.loads((A / "protected-before.json").read_text())
for p, h in protected.items():
    f = Path(p)
    assert sha(f) == h["sha256"] and oct(f.stat().st_mode & 0o777) == h["mode"], p
source_paths.add(Path("interpro/panther/panther.obo"))
result["source_dependencies"] = {str(p): sha(p) for p in sorted(source_paths)}
result["member_sources"] = {
    m: member_sources[m]
    for f in F
    for s in yaml.safe_load(Path(f"interpro/panther/{f}/{f}-review.yaml").read_text())[
        "subfamilies"
    ]
    for r in s["representative_members"]
    for m in [r["id"].split(":")[1]]
}
result["protected_files_unchanged"] = len(protected)
result["result"] = "PASS"
print(json.dumps(result, indent=2, default=str))
