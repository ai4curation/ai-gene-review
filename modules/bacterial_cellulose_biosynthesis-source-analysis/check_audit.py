"""Check preserved reviews and evidence-scoped cellulose machinery coverage.

Run from the repository root. Capacity is evaluated only for the reviewed panel;
it is not an exhaustive genome scan or a prediction of native expression/output.
Unresolved required roles deliberately remain false, reported as abduction targets.
"""

from collections import Counter
import hashlib
from pathlib import Path
import re

import yaml

from ai_gene_review.module_logic import compile_node, is_satisfied

ROOT = Path(__file__).resolve().parents[2]
AUDIT = ROOT / "analysis/module_audits/bacterial_cellulose_biosynthesis"


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
    baseline = read(AUDIT / "seed-baseline.yaml")
    module = read(ROOT / "modules/bacterial_cellulose_biosynthesis.yaml")
    records = {}
    actions = Counter()
    preserved = inherited = added = raw_count = 0
    no_core = []
    donor_process_checked = []
    for member in baseline["members"]:
        review = read(ROOT / member["review_path"])
        assert review["status"] == "COMPLETE", member["review_path"]
        assert review["id"] == member["accession"]
        assert review["taxon"] == member["taxon"]
        rows = review.get("existing_annotations", [])
        assert len(rows) >= len(member["annotations"])
        for seed, row in zip(member["annotations"], rows):
            assert {k: v for k, v in row.items() if k != "review"} == seed["payload"]
            preserved += 1
            if seed["prior_action"] == "NEW":
                assert row["review"]["action"] == "NEW"
                inherited += 1
        for row in rows:
            assert row["review"]["action"] != "PENDING"
            actions[row["review"]["action"]] += 1
        for row in rows[len(member["annotations"]) :]:
            assert row["review"]["action"] == "NEW"
            added += 1
        for path, digest in member["raw_sha256"].items():
            assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest, (
                path
            )
            raw_count += 1
        raw = ROOT / member["review_path"].replace("-ai-review.yaml", "-uniprot.txt")
        text = raw.read_text()
        families = set()
        for db, ident in re.findall(
            r"^DR\s+(PANTHER|InterPro|Pfam); ([^;]+);", text, re.M
        ):
            families.add(f"{db}:{ident}")
        functions = set()
        for row in rows:
            decision = row["review"]
            if decision["action"] in {"ACCEPT", "NEW", "KEEP_AS_NON_CORE"}:
                functions.add(row["term"]["id"])
            if decision["action"] == "MODIFY":
                functions.update(
                    x["id"] for x in decision.get("proposed_replacement_terms", [])
                )
        for core in review.get("core_functions", []):
            for slot in ["molecular_function", "contributes_to_molecular_function"]:
                if core.get(slot):
                    functions.add(core[slot]["id"])
        # Compare the same catalytic claim across the panel, not just rows
        # within one review. Product-pathway coverage must survive refinement.
        catalytic_core = any(core.get("molecular_function", {}).get("id") == "GO:0016760"
                             for core in review.get("core_functions", []))
        if catalytic_core:
            donor_rows = [row for row in rows if row["term"]["id"] == "GO:0006011"]
            if donor_rows:
                assert all(row["review"]["action"] == "ACCEPT" for row in donor_rows)
                core_processes = {term["id"] for core in review.get("core_functions", [])
                                  for term in core.get("directly_involved_in", [])}
                assert "GO:0006011" in core_processes, member["review_path"]
                assert {"GO:0030244", "GO:0090540"} & functions, member["review_path"]
                donor_process_checked.append(member["review_path"])
        raw_functions = {a["payload"]["term"]["id"] for a in member["annotations"]
                         if a["prior_action"] != "NEW"}
        records[member["accession"]] = {"families": families, "functions": functions,
                                         "frozen_goa_functions": raw_functions,
                                         "genus": review["taxon"]["label"].split()[0]}
        if not review.get("core_functions"):
            no_core.append(member["review_path"])
    provider_proof = read(AUDIT / "provider-source-preservation.yaml")
    assert len(donor_process_checked) == 5
    for path, digest in provider_proof["files"].items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest, path
    nodes = {n["id"]: n for n in walk(module["module"]) if "id" in n}
    unknown = {
        "typeIII_unresolved_envelope_passage_unknown_realizer",
        "cyanobacterial_unresolved_envelope_passage_unknown_realizer",
    }
    for ident in unknown:
        assert ident in nodes and not nodes[ident].get("participant")
    cases = []
    scoped_route = nodes["bcsB_bcsC_envelope_route"]
    allowed_genera = {item["term"]["label"] for item in scoped_route["context"]["taxa"]}
    assert allowed_genera == {"Pseudomonas", "Cereibacter", "Komagataeibacter"}
    scoped_annotons = {item["id"] for item in walk(scoped_route) if "participant" in item}

    def check(
        name, present, expected, node=None, interpretation="panel machinery coverage",
        family_scan=False, enforce_context=True, function_source="reviewed"
    ):
        def holds(atom):
            if atom.node_id in unknown:
                return False
            candidates = set(present) if family_scan else set(atom.representative_uniprots) & set(present)
            for accession in candidates:
                record = records[accession]
                if (enforce_context and atom.node_id in scoped_annotons
                        and record["genus"] not in allowed_genera):
                    continue
                if atom.family_ids and not set(atom.family_ids) & record["families"]:
                    continue
                if not set(atom.domain_ids) <= record["families"]:
                    continue
                functions = record["functions"] if function_source == "reviewed" else record["frozen_goa_functions"]
                if not set(atom.function_ids) <= functions:
                    continue
                return True
            return False

        node = node or module["module"]["id"]
        result = is_satisfied(compile_node(nodes[node]), holds)
        assert result == expected, (name, expected, result)
        cases.append(
            {
                "case": name,
                "node": node,
                "present": sorted(present),
                "expected": expected,
                "observed": result,
                "interpretation": interpretation,
                "function_source": function_source,
            }
        )

    check("Family-only Ecoli BC matches the generic route without context", {"P37652", "P37650"},
          True, "bcsB_bcsC_envelope_route", family_scan=True, enforce_context=False,
          interpretation="Negative control: family predicates alone do not enforce taxon applicability")
    check("External context oracle rejects Ecoli bypass of its BcsQ route", {"P37652", "P37650"},
          False, "bcsB_bcsC_envelope_route", family_scan=True,
          interpretation="Context-oracle contract, not a claim that the compiler enforces taxa")
    polymerase = "bcsA_cellulose_polymerization_step"
    for accession in ["E5RST0", "A0ABM5R5V5"]:
        check("Frozen GOA alone leaves " + accession + " cellulose activity unresolved",
              {accession}, False, polymerase, function_source="frozen_goa",
              interpretation="The positive reviewed-function case depends on the evidence-backed MODIFY proposal; raw GOA does not yet carry GO:0016760.")
    check("KT2440 reviewed ABC architecture", {"Q88JL4", "Q88JL3", "Q88JL1"}, True)
    check(
        "KT2440 polymerase alone does not establish envelope machinery",
        {"Q88JL4"},
        False,
    )
    check("KT2440 missing BcsB", {"Q88JL4", "Q88JL1"}, False)
    check("KT2440 missing BcsC", {"Q88JL4", "Q88JL3"}, False)
    ecoli = {"P37653", "P37652", "P37650", "P0DP92"}
    check(
        "Ecoli intact Q assembly compatible",
        ecoli,
        True,
        interpretation="Intact/repaired Q scenario, not a native K12 expression claim",
    )
    check("Ecoli ABC without intact Q is insufficient", ecoli - {"P0DP92"}, False)
    check(
        "K12 pseudogene fragment cannot replace intact Q",
        (ecoli - {"P0DP92"}) | {"P37655"},
        False,
    )
    check(
        "C58 typeIII mechanism unresolved",
        {"A9CEZ7", "Q7CS46", "Q8U4V1"},
        False,
        interpretation="ABDUCTION_TARGET; observed cellulose production is not contradicted",
    )
    check("C58 polymerase recognized", {"A9CEZ7"}, True, polymerase)
    check(
        "Authentic RKN polymerase survives lack of IPR003919",
        {"E5RST0"},
        True,
        polymerase,
    )
    check(
        "RKN polymerase alone cannot explain extracellular output",
        {"E5RST0"},
        False,
        interpretation="ABDUCTION_TARGET; native synthesis is experimentally supported",
    )
    check(
        "BP1 accessory comparators cannot close RKN mechanism",
        {"E5RST0", "Q8DKF6", "Q8DHP3"},
        False,
        interpretation="Artificial mixed-strain panel still cannot satisfy unknown transport",
    )
    check("Rhodobacter polymerase recognized", {"Q3J125"}, True, polymerase)
    check(
        "Rhodobacter BcsB recognized without PANTHER assignment",
        {"Q3J126"},
        True,
        "bcsB_periplasmic_synthase_support_step",
    )
    check(
        "Rhodobacter assayed AB not a full export inventory",
        {"Q3J125", "Q3J126"},
        False,
    )
    check("TypeI BcsA polymerase recognized", {"P19449"}, True, polymerase)
    check(
        "BcsD structural role needs no invented MF",
        {"P37719"},
        True,
        "bcsD_glucan_organization",
    )
    check(
        "Streptomyces CslA polymerase recognized without canonical PilZ",
        {"A0ABM5R5V5"},
        True,
        polymerase,
    )
    check(
        "Streptomyces assayed CslA GlxA complex",
        {"A0ABM5R5V5", "P0DYA0"},
        True,
        interpretation="Demonstrated cellulose synthesis in vitro; native TK24 output not established",
    )
    check("Streptomyces CslA without GlxA lacks modeled support", {"A0ABM5R5V5"}, False)
    check("GlxA alone is not a polymerase", {"P0DYA0"}, False)
    check(
        "GlxA contributes without an invented domain identifier",
        {"P0DYA0"},
        True,
        "glxA_synthase_support_step",
    )
    saved_functions = records["A0ABM5R5V5"]["functions"]
    records["A0ABM5R5V5"]["functions"] = set()
    check(
        "Synthetic family-only GT2 match cannot establish cellulose chemistry",
        {"A0ABM5R5V5"},
        False,
        polymerase,
        interpretation="Predicate perturbation, not a claim that the real CslA lacks activity",
    )
    records["A0ABM5R5V5"]["functions"] = saved_functions
    result = {
        "complete_reviews": len(records),
        "preserved_seed_rows": preserved,
        "inherited_new_rows": inherited,
        "new_rows": added,
        "preserved_raw_files": raw_count,
        "preserved_provider_artifacts": len(provider_proof["files"]),
        "actions": dict(actions),
        "reviews_without_asserted_core": no_core,
        "production_compiler_cases": len(cases),
        "catalytic_donor_process_consistency": donor_process_checked,
        "limitation": "Reviewed-panel machinery coverage; unresolved native routes are abduction targets, not biological negatives.",
    }
    (AUDIT / "integration-checks.yaml").write_text(
        yaml.safe_dump(result, sort_keys=False, width=105)
    )
    (AUDIT / "capacity-results.yaml").write_text(
        yaml.safe_dump(cases, sort_keys=False, width=105)
    )
    print(yaml.safe_dump(result, sort_keys=False))


if __name__ == "__main__":
    main()
