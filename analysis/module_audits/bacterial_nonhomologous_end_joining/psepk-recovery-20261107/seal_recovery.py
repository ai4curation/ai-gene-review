"""Seal freshly verified reconstruction, without recreating the lost old seal."""

import hashlib
import json
import stat
from pathlib import Path
import yaml

A = Path(
    "analysis/module_audits/bacterial_nonhomologous_end_joining/psepk-recovery-20261107"
)


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def write(name, value):
    (A / name).write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n")


assert not (A / "handoff.json").exists(), "Use an additive successor after sealing."
before = json.loads((A / "before.json").read_text())
protected = {}
for path, old in before["files"].items():
    if path.endswith(("-ai-review.yaml", "-notes.md", "-ai-review.html")):
        continue
    assert sha(path) == old["sha256"], path
    assert oct(stat.S_IMODE(Path(path).stat().st_mode)) == old["mode"], path
    protected[path] = old
files = []
deps = {}
references = {}
counts = {}
for gene in ["ku", "ligD"]:
    path = Path(f"genes/PSEPK/{gene}/{gene}-ai-review.yaml")
    d = yaml.safe_load(path.read_text())
    old = before["reviews"][gene]
    payload = lambda data: [
        {k: v for k, v in row.items() if k != "review"}
        for row in data["existing_annotations"]
    ]
    assert payload(d) == payload(old), gene
    assert d == old, "Recovery verification changed reviewed science unexpectedly"
    counts[gene] = {
        "rows": len(d["existing_annotations"]),
        "machine_rows": sum(
            r["review"]["action"] != "NEW" for r in d["existing_annotations"]
        ),
        "historical_NEW": sum(
            r["review"]["action"] == "NEW" for r in d["existing_annotations"]
        ),
        "retired_historical_NEW": sum(
            bool(r.get("retired")) for r in d["existing_annotations"]
        ),
        "new_authored_rows": 0,
        "full_review_content_unchanged_since_reconstruction": True,
    }
    for suffix in ["ai-review.yaml", "notes.md", "ai-review.html"]:
        files.append(f"genes/PSEPK/{gene}/{gene}-{suffix}")
    for ref in d["references"]:
        rid = ref["id"]
        if rid.startswith("PMID:"):
            p = Path("publications") / (rid.replace(":", "_") + ".md")
        elif rid.startswith("file:"):
            v = rid[5:]
            p = Path(v) if Path(v).exists() else Path("genes") / v
        else:
            references[rid] = {"external_method_identifier": True}
            continue
        assert p.is_file(), p
        deps[str(p)] = sha(p)
        references[rid] = {"path": str(p), "sha256": sha(p)}
    assert (
        f"All validations passed for PSEPK/{gene}"
        in (A / f"validate-{gene}.log").read_text()
    )
    assert "No issues found" in (A / f"history-{gene}.log").read_text()
    assert "Rendered" in (A / f"render-{gene}.log").read_text()
files += [
    "history/genes/PSEPK/ku/2026-11-07T164409Z-codex-eb9e0c.yaml",
    "history/genes/PSEPK/ligD/2026-11-07T164409Z-codex-5a629b.yaml",
]
for name in ["Sharaev2022-English.html", "Sharaev2022-English-recovery-receipt.json"]:
    p = A.parent / "literature-acquisition-20261107" / name
    deps[str(p)] = sha(p)
# Parent-owned recovered/fresh ontology records are optional only until root confirms their path.
if (A / "additional-dependencies.json").exists():
    for p in json.loads((A / "additional-dependencies.json").read_text()):
        deps[p] = sha(p)
write(
    "preservation-proof.json",
    {
        "counts": counts,
        "protected_raw_provider_files": protected,
        "all_ordered_payloads_qualifiers_and_retirement_flags_preserved": True,
        "no_new_science": True,
    },
)
write("source-closure.json", {"references": references, "missing_cited_files": []})
files += [
    str(p)
    for p in sorted(A.iterdir())
    if p.is_file() and p.name not in ["handoff.json", "stage-paths.json"]
]
paths = sorted(set(files) | {str(A / "handoff.json"), str(A / "stage-paths.json")})
write("stage-paths.json", paths)
hashes = {p: sha(p) for p in paths if p != str(A / "handoff.json")}
write(
    "handoff.json",
    {
        "type": "Fresh recovery verification seal; not a recovered historical handoff",
        "historical_handoff_not_recreated": "dc58fd628c45cf0cb98d98f746c3fec9cf5be4ecff397b27900a3369070dc9e2",
        "files": hashes,
        "source_dependencies": deps,
        "counts": counts,
        "checks": {
            "full_focused_gene_validations": 2,
            "fresh_history_validations": 2,
            "renders": 2,
            "full_corpus_validation": False,
        },
        "warnings": [
            "No annotations reference available deep research files (ku-deep-research-openscientist.md)",
            "No annotations reference available deep research files (ligD-deep-research-openscientist.md)",
        ],
        "stage_path_count": len(paths),
    },
)
print(
    json.dumps(
        {
            "handoff": str(A / "handoff.json"),
            "sha256": sha(A / "handoff.json"),
            "stage_paths": len(paths),
            "source_dependencies": len(deps),
        },
        indent=2,
    )
)
