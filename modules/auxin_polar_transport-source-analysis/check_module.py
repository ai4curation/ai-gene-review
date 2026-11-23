"""Bounded real validator and biological route checks for the curated transport module.
Run from the repository root: uv run python modules/auxin_polar_transport-source-analysis/check_module.py
No full PANTHER membership index is built. Membership is independently read from
normally fetched UniProt records; ontology labels and biological conformance use
the production validator. Reports are written only under .cache.
"""

from pathlib import Path
import json
import re
import yaml
from ai_gene_review.validation.module_validator import (
    validate_module_file,
    iter_evidence_snippets,
)
from ai_gene_review.module_logic import (
    compile_module_file,
    enumerate_routes,
    is_satisfied,
)

PANEL = [
    "ARATH/AUX1",
    "ARATH/PIN1",
    "ARATH/PIN2",
    "ARATH/ABCB19",
    "ARATH/PID",
    "ARATH/D6PK",
    "ARATH/PIN3",
    "ARATH/LAX3",
    "ARATH/ABCB1",
    "ARATH/ABCB4",
    "ARATH/FKBP42",
    "ARATH/NRT1.1",
    "ORYSJ/PIN2",
    "ORYSJ/OsAUX1",
    "PHYPA/PINA",
    "PHYPA/PINB",
    "MARPO/MpPIN1",
]

mapping = {}
gene_index = {}
for key in PANEL:
    org, g = key.split("/")
    p = Path(f"genes/{org}/{g}/{g}-ai-review.yaml")
    d = yaml.safe_load(p.read_text())
    raw = p.with_name(g + "-uniprot.txt").read_text()
    families = re.findall(r"^DR   PANTHER; ([^;]+);", raw, re.M)
    mapping[d["id"]] = next((x for x in families if ":SF" in x), families[0])
    gene_index[d["id"]] = p
path = Path("modules/auxin_polar_transport.yaml")
r = validate_module_file(path, member_index=mapping, gene_index=gene_index)
snippets = list(iter_evidence_snippets(yaml.safe_load(path.read_text())))
assert len(snippets) >= 10, len(snippets)
# Module validator checks PMID/DOI snippets. Independently verify stable URL
# excerpts too, using only normally generated local caches and exact text.
unique_quotes = set()


def quote_walk(x):
    if isinstance(x, dict):
        ref = x.get("source_id")
        if ref and x.get("supporting_text"):
            unique_quotes.add((ref, x["supporting_text"]))
        for v in x.values():
            quote_walk(v)
    elif isinstance(x, list):
        for v in x:
            quote_walk(v)


quote_walk(yaml.safe_load(path.read_text()))
for ref, quote in unique_quotes:
    if ref.startswith("PMID:"):
        source = Path("publications/PMID_" + ref[5:] + ".md")
    elif ref.startswith("url:"):
        found = [
            p
            for p in Path("publications").glob("url_*.md")
            if ("reference_id: " + ref) in p.read_text()[:2000]
        ]
        assert len(found) == 1, (ref, found)
        source = found[0]
    else:
        continue
    assert " ".join(quote.split()) in " ".join(source.read_text().split()), (ref, quote)
report = {
    "evidence_snippets_checked": len(snippets),
    "unique_local_quotes_verified": len(unique_quotes),
    "errors": r.errors,
    "warnings": r.warnings,
    "member_mapping": mapping,
    "valid": r.is_valid,
}
log = Path(".cache/module-audit-logs")
log.mkdir(parents=True, exist_ok=True)
(log / "auxin-polar-module-validation.json").write_text(
    json.dumps(report, indent=2) + "\n"
)
for e in r.errors:
    print("ERROR:", e)
for w in r.warnings:
    print("WARNING:", w)
print("Production module validator:", r.is_valid)
c = compile_module_file(path)
cases = [
    ("empty", set(), False),
    ("Arabidopsis root outer stream", {"Q96247", "Q9LU77"}, True),
    ("Arabidopsis lateral-root emergence", {"Q9S7Z8", "Q9CA25"}, True),
    ("Arabidopsis PIN1 ABCB19 cooperation", {"Q9C6B8", "Q9LJX0"}, True),
    ("Native D6PK PIN3 mechanism", {"Q9FG74", "Q9S7Z8"}, True),
    ("Native PID PIN1 mechanism", {"O64682", "Q9C6B8"}, True),
    ("Native TWD1 ABCB1 mechanism", {"Q9LDC0", "Q9ZR72"}, True),
    (
        "TWD1 and ABCB19 alone are not an independently modeled complete mechanism",
        {"Q9LDC0", "Q9LJX0"},
        False,
    ),
    ("Rice sampled segment is insufficient", {"Q5N892", "Q651V6"}, False),
    ("Moss PINA alone", {"Q5TK28"}, False),
    ("Moss PINB alone", {"A9RN82"}, False),
    ("Both moss exporters", {"Q5TK28", "A9RN82"}, False),
    ("Marchantia exporter alone", {"A0A2R6WHW5"}, False),
    ("All bryophyte comparators", {"Q5TK28", "A9RN82", "A0A2R6WHW5"}, False),
    ("Optional ABCB4 and NRT1.1 only", {"O80725", "Q05085"}, False),
    ("Rice influx plus Arabidopsis PIN2 does not combine", {"Q5N892", "Q9LU77"}, False),
    ("Arabidopsis AUX1 plus rice PIN2 does not combine", {"Q96247", "Q651V6"}, False),
    (
        "Rice segment plus bryophyte export still insufficient",
        {"Q5N892", "Q651V6", "Q5TK28", "A9RN82", "A0A2R6WHW5"},
        False,
    ),
    ("Kinase alone", {"Q9FG74"}, False),
    ("PIN1 alone", {"Q9C6B8"}, False),
    ("TWD1 alone", {"Q9LDC0"}, False),
    ("All sampled members", set(gene_index), True),
]
checks = []
for name, acc, expected in cases:
    actual = is_satisfied(c, lambda a: a.uniprot in acc)
    checks.append(
        {
            "case": name,
            "accessions": sorted(acc),
            "expected": expected,
            "actual": actual,
        }
    )
    assert actual == expected, (name, expected, actual)
routes = enumerate_routes(c)
unique = {frozenset(a.node_id for a in route): route for route in routes}
minimal = [
    route for ids, route in unique.items() if not any(other < ids for other in unique)
]
assert len(minimal) == 6, len(minimal)
assert all(len(x) == 2 for x in minimal)
assert all(len(x) >= 2 for x in routes)
(log / "auxin-polar-module-route-checks.json").write_text(
    json.dumps(
        {
            "cases": checks,
            "expanded_route_count": len(routes),
            "minimal_route_count": len(minimal),
            "minimal_routes": [[a.node_id for a in route] for route in minimal],
        },
        indent=2,
    )
    + "\n"
)
print(
    f"{len(checks)} route cases PASS; {len(minimal)} minimal two-activity mechanisms ({len(routes)} expansions including optional branches). Context is a biological precondition, not inferred from protein presence."
)
raise SystemExit(0 if r.is_valid else 1)
