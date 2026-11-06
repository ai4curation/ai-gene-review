"""Check this audit's source preservation, grounding, evidence closure and panel capacity.

Run from the repository root with ``uv run python
modules/bacterial_c_di_gmp_signaling-source-analysis/check_audit.py``.
Capacity means coverage by reviewed reference proteins, not experimentally
proven operation of every edge in every strain or exhaustive genomic capacity.
"""

from collections import Counter
import hashlib
import json
from pathlib import Path

import yaml

from ai_gene_review.module_logic import compile_node, is_satisfied

ROOT = Path(__file__).resolve().parents[2]
AUDIT = ROOT / "analysis/module_audits/bacterial_c_di_gmp_signaling"
MODULE = ROOT / "modules/bacterial_c_di_gmp_signaling.yaml"


def walk(value):
    """Yield every mapping in nested YAML data."""
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)


def read(path):
    return yaml.safe_load(path.read_text())


def main():
    baseline = read(AUDIT / "seed-baseline.yaml")
    module = read(MODULE)
    reviews = {}
    original_count = 0
    new_rows = []
    actions = Counter()
    raw_files = 0
    for member in baseline["members"]:
        doc = read(ROOT / member["review_path"])
        assert doc["id"].removeprefix("UniProtKB:") == member["accession"]
        assert doc["status"] == "COMPLETE", member["review_path"]
        old = []
        for annotation in doc.get("existing_annotations", []):
            action = annotation["review"]["action"]
            assert action != "PENDING", member["review_path"]
            actions[action] += 1
            if action == "NEW":
                new_rows.append(
                    {"review": member["review_path"], "annotation": annotation}
                )
            else:
                old.append({k: v for k, v in annotation.items() if k != "review"})
        assert old == member["original_annotations"], member["review_path"]
        original_count += len(old)
        for filename, digest in member["raw_sha256"].items():
            assert (
                hashlib.sha256((ROOT / filename).read_bytes()).hexdigest() == digest
            ), filename
            raw_files += 1
        reviews[member["accession"]] = doc

    annotons = [a for node in walk(module["module"]) for a in node.get("annotons", [])]
    representative_ids = set()
    assignments = []
    for annoton in annotons:
        assert annoton.get("evidence"), annoton["id"]
        family = annoton["participant"]["family"]
        assert family.get("representative_members"), annoton["id"]
        for representative in family["representative_members"]:
            accession = representative["term"]["id"].removeprefix("UniProtKB:")
            representative_ids.add(accession)
            function = annoton.get("function", {}).get("term", {}).get("id")
            if function:
                core = {
                    f.get("molecular_function", {}).get("id")
                    for f in reviews[accession].get("core_functions", [])
                }
                assert function in core, (annoton["id"], accession, function)
            assignments.append(
                {"annoton": annoton["id"], "accession": accession, "function": function}
            )
    assert representative_ids == set(reviews), representative_ids ^ set(reviews)
    assert len(module["module"]["parts"]) >= 3
    assert all(edge.get("evidence") for edge in module["module"]["connections"])

    grounding = read(AUDIT / "taxonomy-family-grounding.yaml")["records"]
    by_acc = {r["accession"]: r for r in grounding}
    official = {}
    current = None
    for line in (ROOT / "interpro/panther/panther.obo").read_text().splitlines():
        if line.startswith("id: "):
            current = line[4:]
        elif current and line.startswith("name: "):
            official[current] = line[6:]
    family_checks = []
    for annoton in annotons:
        family = annoton["participant"]["family"]
        terms = family.get("family_terms", []) + (
            [family["term"]] if "term" in family else []
        )
        for item in terms:
            assert official[item["id"]] == item["label"], item
        for member in family["representative_members"]:
            accession = member["term"]["id"].removeprefix("UniProtKB:")
            known = {
                "PANTHER:" + r["id"]
                for r in by_acc[accession]["panther_cross_references"]
            }
            if terms:
                assert known.intersection(t["id"] for t in terms), (
                    accession,
                    terms,
                    known,
                )
                family_checks.append(
                    {
                        "accession": accession,
                        "matched": sorted(known.intersection(t["id"] for t in terms)),
                    }
                )

    sources = {}
    for document in [module, *reviews.values()]:
        for node in walk(document):
            for key in ["source_id", "reference_id", "original_reference_id", "id"]:
                ref = node.get(key, "")
                if isinstance(ref, str) and ref.startswith("PMID:"):
                    path = ROOT / "publications" / (ref.replace(":", "_") + ".md")
                    assert path.exists(), ref
                    sources[ref] = {
                        "path": str(path.relative_to(ROOT)),
                        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                    }
    module_refs = {r["id"] for r in module["references"]}
    module_cites = {
        n["source_id"]
        for n in walk(module)
        if str(n.get("source_id", "")).startswith("PMID:")
    }
    assert module_cites <= module_refs
    assert all(
        r.get("reference_review") and r.get("findings") for r in module["references"]
    )

    # Exercise the production compiler on the actual required parts, alternatives
    # and optional context. A presence predicate restricts each case to ONE
    # reference-strain panel; combining species is not a native realization.
    required = {"GO:0052621", "GO:0071111", "GO:0035438"}
    panels = {}
    for accession, doc in reviews.items():
        taxon = doc["taxon"]["id"]
        panels.setdefault(taxon, set()).add(accession)
    capacities = []
    cases = []
    nodes = {n["id"]: n for n in walk(module["module"]) if "id" in n}
    representatives = {
        a["id"]: {
            r["term"]["id"].removeprefix("UniProtKB:")
            for r in a["participant"]["family"]["representative_members"]
        }
        for a in annotons
    }

    def check(name, taxon, present, expected, node="bacterial_c_di_gmp_signaling"):
        def available(atom):
            return bool(representatives[atom.node_id] & present & panels[taxon])

        observed = is_satisfied(compile_node(nodes[node]), available)
        assert observed == expected, (name, expected, observed)
        cases.append(
            {
                "case": name,
                "taxon": taxon,
                "node": node,
                "present": sorted(present),
                "expected": expected,
                "observed": observed,
            }
        )
        return observed

    positive_taxa = {"NCBITaxon:83333", "NCBITaxon:224308", "NCBITaxon:224326"}
    for taxon, accessions in sorted(panels.items()):
        covered = {a["function"] for a in assignments if a["accession"] in accessions}
        missing = sorted(required - covered)
        observed = check(
            "Scoped native panel", taxon, accessions, taxon in positive_taxa
        )
        capacities.append(
            {
                "reference_taxon": taxon,
                "members": sorted(accessions),
                "complete_role_panel": observed,
                "missing_functions": missing,
            }
        )
    # Delete the actual proteins assigned to each role and recompile the module;
    # accidental optionalization of a required part must fail these cases.
    perturbations = []
    for taxon in sorted(positive_taxa):
        accessions = panels[taxon]
        for removed in sorted(required):
            deleted = {a["accession"] for a in assignments if a["function"] == removed}
            check(
                "Remove proteins supplying " + removed,
                taxon,
                accessions - deleted,
                False,
            )
            perturbations.append(
                {
                    "reference_taxon": taxon,
                    "removed_function": removed,
                    "complete_role_panel": False,
                }
            )
    check("Empty panel", "NCBITaxon:83333", set(), False)
    check("Optional DdpA alone", "NCBITaxon:257310", {"A0A0H3LMJ1"}, False)
    check(
        "Other species cannot complete the Bordetella panel",
        "NCBITaxon:257310",
        set(reviews),
        False,
    )
    for accession in ["O51338", "O50161"]:
        check(
            "Borrelia retains the alternative PDE without " + accession,
            "NCBITaxon:224326",
            panels["NCBITaxon:224326"] - {accession},
            True,
        )
    for accession in ["P38491", "P96585"]:
        check(
            "Bacillus retains the alternative receptor without " + accession,
            "NCBITaxon:224308",
            panels["NCBITaxon:224308"] - {accession},
            True,
        )
    check(
        "PleD feedback binding is not a dedicated receptor",
        "NCBITaxon:190650",
        {"Q9A5I5"},
        False,
        "c_di_gmp_reception",
    )
    result = {
        "module": str(MODULE.relative_to(ROOT)),
        "original_rows_preserved": original_count,
        "raw_sources_preserved": raw_files,
        "reviews_complete": len(reviews),
        "actions": dict(sorted(actions.items())),
        "annotons_with_family_and_evidence": len(annotons),
        "family_membership_checks": family_checks,
        "panel_capacity": capacities,
        "required_role_perturbations": perturbations,
        "production_compiler_cases_passed": len(cases),
        "limitation": "Reference-protein role coverage is not evidence of all edges operating in each strain; optional DdpA is excluded from the required roles.",
    }
    (AUDIT / "source-closure.yaml").write_text(yaml.safe_dump(sources, sort_keys=True))
    (AUDIT / "new-annotations.yaml").write_text(
        yaml.safe_dump(new_rows, sort_keys=False, allow_unicode=True)
    )
    (AUDIT / "integration-checks.yaml").write_text(
        yaml.safe_dump(result, sort_keys=False)
    )
    (AUDIT / "capacity-results.yaml").write_text(
        yaml.safe_dump({"passed": len(cases), "cases": cases}, sort_keys=False)
    )
    print(
        json.dumps(
            {
                k: v
                for k, v in result.items()
                if k
                not in {
                    "family_membership_checks",
                    "panel_capacity",
                    "required_role_perturbations",
                }
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
