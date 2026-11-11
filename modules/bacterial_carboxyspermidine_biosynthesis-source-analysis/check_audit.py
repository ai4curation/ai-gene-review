"""Verify preserved seeds, reaction grounding and production-compiler panel coverage.

Coverage means the reviewed role panel, not demonstrated native flux or exhaustive
capacity of a genome. Run from the repository root with uv run python this_file.
"""

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path

import yaml

from ai_gene_review.module_logic import compile_node, is_satisfied

ROOT = Path(__file__).resolve().parents[2]
AUDIT = ROOT / "analysis/module_audits/bacterial_carboxyspermidine_biosynthesis"
MODULE = ROOT / "modules/bacterial_carboxyspermidine_biosynthesis.yaml"


def read(path):
    return yaml.safe_load(path.read_text())


def walk(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=AUDIT / "substrate-followup-20261107")
    args = parser.parse_args()
    output = args.output_dir.resolve()
    # Historical receipts remain immutable when current scientific conclusions change.
    assert output != AUDIT.resolve(), "Use an additive result directory, not historical audit outputs"
    output.mkdir(parents=True, exist_ok=True)
    baseline = read(AUDIT / "seed-baseline.yaml")
    panel = read(AUDIT / "member-panel.yaml")
    module = read(MODULE)
    reviews = {}
    actions = Counter()
    added = []
    inherited_new = 0
    preserved = 0
    raw_count = 0
    no_core = []
    for member in baseline["members"]:
        doc = read(ROOT / member["review_path"])
        assert doc["id"] == member["accession"]
        assert doc["taxon"] == member["taxon"]
        assert doc["status"] == "COMPLETE"
        rows = doc.get("existing_annotations", [])
        seeds = member["annotations"]
        assert len(rows) >= len(seeds)
        for row, seed in zip(rows, seeds):
            assert {k: v for k, v in row.items() if k != "review"} == seed["payload"], (
                member["review_path"]
            )
            preserved += 1
            if seed["prior_action"] == "NEW":
                assert row["review"]["action"] == "NEW"
                inherited_new += 1
        for row in rows:
            assert row["review"]["action"] != "PENDING"
            actions[row["review"]["action"]] += 1
        for row in rows[len(seeds) :]:
            assert row["review"]["action"] == "NEW"
            added.append({"review": member["review_path"], "annotation": row})
        for path, digest in member["raw_sha256"].items():
            assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest, (
                path
            )
            raw_count += 1
        if not doc.get("core_functions"):
            no_core.append(member["review_path"])
            assert doc.get("suggested_questions") or doc.get("knowledge_gaps"), member[
                "review_path"
            ]
        reviews[doc["id"]] = doc

    by_acc = {r["accession"]: r for r in panel["reaction_representatives"]}
    nodes = {n["id"]: n for n in walk(module["module"]) if "id" in n}
    annotons = [
        n for n in walk(module["module"]) if "participant" in n and "function" in n
    ]
    assert len(annotons) == 2
    official = {}
    current = None
    for line in (ROOT / "interpro/panther/panther.obo").read_text().splitlines():
        if line.startswith("id: "):
            current = line[4:]
        elif current and line.startswith("name: "):
            official[current] = line[6:]
    reps = {}
    conformance = []
    for annoton in annotons:
        assert annoton.get("evidence") and annoton["function"].get("evidence")
        family = annoton["participant"]["family"]
        assert family["term"]["label"] == official[family["term"]["id"]]
        reps[annoton["id"]] = set()
        for item in family["representative_members"]:
            accession = item["term"]["id"].removeprefix("UniProtKB:")
            assert accession in by_acc and item.get("evidence")
            row = by_acc[accession]
            doc = reviews[accession]
            raw = (
                ROOT
                / f"genes/{row['organism']}/{row['gene']}/{row['gene']}-uniprot.txt"
            )
            assert family["term"]["id"].removeprefix("PANTHER:") in raw.read_text(), (
                accession
            )
            assert doc["taxon"]["id"] == row["taxon"]
            cores = doc.get("core_functions", [])
            if row["role"] == 1:
                assert any(
                    c.get("molecular_function", {}).get("id") == "GO:0102143"
                    for c in cores
                ), accession
                method = "GO:0102143 core"
            else:
                proposals = {
                    p["proposed_name"]: p for p in doc.get("proposed_new_terms", [])
                }
                compatible = []
                for core in cores:
                    proposal = proposals.get(core.get("proposed_molecular_function"))
                    if proposal and "carboxyspermidine" in proposal["proposed_name"]:
                        assert "spermidine" in proposal["proposed_definition"]
                        assert proposal.get("supported_by") or core.get("supported_by")
                        compatible.append(proposal["proposed_name"])
                assert compatible, accession
                method = (
                    "Reviewed proposal explicitly includes carboxyspermidine decarboxylation: "
                    + "; ".join(compatible)
                )
            reps[annoton["id"]].add(accession)
            conformance.append(
                {"accession": accession, "annoton": annoton["id"], "check": method}
            )
    assert set().union(*reps.values()) == set(by_acc)
    for edge in module["module"]["connections"]:
        assert (
            edge.get("evidence") and edge["source"] in nodes and edge["target"] in nodes
        )
    # Neither candidates nor CAPA-specialized comparators are silently promoted.
    for row in panel["reviewed_comparators"]:
        doc = read(
            ROOT / f"genes/{row['organism']}/{row['gene']}/{row['gene']}-ai-review.yaml"
        )
        assert doc["id"] not in by_acc

    cases = []

    def check(name, taxon, present, expected, node=None, repaired_81116=False):
        def available(atom):
            eligible = reps[atom.node_id] & present
            if not repaired_81116:
                eligible -= {"A8FNH9"}
            return any(by_acc[a]["taxon"] == taxon for a in eligible)

        observed = is_satisfied(
            compile_node(nodes[node or module["module"]["id"]]), available
        )
        assert observed == expected, (name, expected, observed)
        cases.append(
            {
                "case": name,
                "taxon": taxon,
                "present": sorted(present),
                "node": node or module["module"]["id"],
                "repaired_81116": repaired_81116,
                "expected": expected,
                "observed": observed,
            }
        )

    panels = {}
    for accession, row in by_acc.items():
        panels.setdefault(row["taxon"], set()).add(accession)
    # Reviewed complete pairs: Vibrio reference, inferred Pseudomonas, native
    # Agrobacterium, and heterologously reconstructed Paracoccus. Do not conflate
    # these evidence levels with four demonstrated native pathways.
    positive = {
        reviews[a]["taxon"]["id"] for a in ["Q9KRL3", "Q88IS1", "A9CG66", "A1B695"]
    }
    for taxon, accessions in sorted(panels.items()):
        check("Reviewed same-taxon panel", taxon, accessions, taxon in positive)
        if taxon in positive:
            for role in [1, 2]:
                keep = {a for a in accessions if by_acc[a]["role"] != role}
                check("Remove reaction " + str(role), taxon, keep, False)
    check("Empty input", reviews["Q9KRL3"]["taxon"]["id"], set(), False)
    check(
        "Cross-species proteins do not complete Bacteroides fragilis",
        reviews["I9VY56"]["taxon"]["id"],
        set(reviews),
        False,
    )
    check(
        "CAPA comparators are not putrescine representatives",
        reviews["A7VSG1"]["taxon"]["id"],
        {"A7VSG1", "A7VSG2"},
        False,
    )
    casdc = "nspc_spermidine_formation"
    check(
        "Unresolved HP_0020 cannot supply the putrescine-specific decarboxylase step",
        reviews["O24865"]["taxon"]["id"],
        {"O24865"},
        False,
        node=casdc,
    )
    check(
        "Helicobacter candidates do not establish the complete putrescine route",
        reviews["O24865"]["taxon"]["id"],
        {"O24865", next(a for a, d in reviews.items() if d["gene_symbol"] == "HP_1507")},
        False,
    )
    check(
        "Canonical K184 is not the assayed active construct",
        reviews["A8FNH9"]["taxon"]["id"],
        {"A8FNH9"},
        False,
        node=casdc,
    )
    check(
        "Repaired E184 construct supplies the assayed decarboxylase step",
        reviews["A8FNH9"]["taxon"]["id"],
        {"A8FNH9"},
        True,
        node=casdc,
        repaired_81116=True,
    )
    sources = {}
    for document in [module, *reviews.values()]:
        for obj in walk(document):
            for key in ["source_id", "reference_id", "original_reference_id", "id"]:
                ref = obj.get(key)
                if isinstance(ref, str) and ref.startswith("PMID:"):
                    path = ROOT / "publications" / (ref.replace(":", "_") + ".md")
                    assert path.exists(), ref
                    sources[ref] = {
                        "path": str(path.relative_to(ROOT)),
                        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                    }
    cited = {
        n["source_id"]
        for n in walk(module)
        if str(n.get("source_id", "")).startswith("PMID:")
    }
    assert cited <= {r["id"] for r in module["references"]}
    assert all(
        r.get("reference_review") and r.get("findings") for r in module["references"]
    )
    result = {
        "reviews_complete": len(reviews),
        "preserved_seed_rows": preserved,
        "inherited_new_rows": inherited_new,
        "newly_proposed_rows": len(added),
        "raw_files_preserved": raw_count,
        "actions": dict(sorted(actions.items())),
        "candidates_without_core": no_core,
        "reaction_representatives": len(by_acc),
        "reaction_conformance_checks": conformance,
        "production_compiler_cases": len(cases),
        "limitation": "Role-panel coverage distinguishes inference, native genetics and heterologous assays; it does not establish native flux or exhaustive genomic capacity. No specific CASDC GO id exists, so proposed reaction text is checked explicitly.",
    }
    for name, data in [
        ("integration-checks.yaml", result),
        ("capacity-results.yaml", {"cases": cases}),
        ("source-closure.yaml", sources),
        ("new-annotations.yaml", added),
    ]:
        destination = output / name
        temporary = destination.with_suffix(destination.suffix + ".tmp")
        temporary.write_text(
            yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=100)
        )
        temporary.replace(destination)
    print(
        json.dumps(
            {k: v for k, v in result.items() if k != "reaction_conformance_checks"},
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
