"""Check curated component coverage, not automatic proteome or native-flux prediction.

The production circuit exposes family and function identifiers. Curated retained
claims supply activities, and explicit rules supply same-protein fusion and
same-strain pairing. This is a consistency check, not independent verification
of experiments; free-text architecture is not enforced by the compiler.
"""
from copy import deepcopy
from pathlib import Path
import hashlib
import json
import re

import yaml

from ai_gene_review.module_logic import compile_module, is_satisfied, iter_atoms

ROOT = Path(__file__).resolve().parents[2]
AUDIT = ROOT / "analysis/module_audits/bacterial_fused_puta_proline_catabolism"
MODULE = ROOT / "modules/bacterial_fused_puta_proline_catabolism.yaml"
TRANSPORT = "putp_activity"
PRODH = "puta_prodh_activity"
GSALDH = "puta_p5cdh_activity"
FUNCTION = {TRANSPORT: "GO:0005298", PRODH: "GO:0004657", GSALDH: "GO:0003842"}
SPECIES = ["PSEPK", "ECOLI", "SALTY", "BRADU", "SINMM", "GEOSL", "9CORY", "HELPG"]


def curated_functions(review):
    """Expose retained claims without using core status as a truth/evidence score.

    The returned provenance records curation decisions, not independently checked
    assays. Historical/proposed NEW rows are not treated as retained GOA claims.
    """
    origins = {}
    for index, row in enumerate(review.get("existing_annotations", [])):
        if row.get("retired") or row.get("negated"):
            continue
        decision = row["review"]
        action = decision["action"]
        terms = ([row["term"]] if action in {"ACCEPT", "KEEP_AS_NON_CORE"} else
                 decision.get("proposed_replacement_terms", []) if action == "MODIFY" else [])
        for term in terms:
            if term["id"].startswith("GO:"):
                origins.setdefault(term["id"], []).append(dict(
                    kind="reviewed_annotation", row_index=index, action=action,
                    evidence_type=row["evidence_type"],
                    original_reference_id=row.get("original_reference_id")))
    for index, core in enumerate(review.get("core_functions", [])):
        term = core.get("molecular_function")
        if term:
            origins.setdefault(term["id"], []).append(dict(kind="core_synthesis", core_index=index))
    return origins


def check_claim_extraction():
    """Counterfactual curation fixtures; none is a new biological assertion."""
    term = dict(id="GO:0004657", label="proline dehydrogenase activity")
    row = dict(term=term, evidence_type="IEA", review=dict(action="ACCEPT"))
    checks = 0
    for action in ["ACCEPT", "KEEP_AS_NON_CORE", "MODIFY"]:
        fixture = deepcopy(row)
        fixture["review"] = dict(action=action, proposed_replacement_terms=[term])
        assert term["id"] in curated_functions(dict(existing_annotations=[fixture]))
        checks += 1
    for flag in ["retired", "negated"]:
        fixture = deepcopy(row)
        fixture[flag] = True
        assert not curated_functions(dict(existing_annotations=[fixture]))
        checks += 1
    for action in ["REMOVE", "UNDECIDED", "MARK_AS_OVER_ANNOTATED", "NEW"]:
        fixture = deepcopy(row)
        fixture["review"]["action"] = action
        assert not curated_functions(dict(existing_annotations=[fixture]))
        checks += 1
    assert term["id"] in curated_functions(dict(core_functions=[dict(molecular_function=term)]))
    return checks + 1


def load_evidence():
    proteins = {}
    sources = {}
    for species in SPECIES:
        for gene in (["putA", "putP"] if species in ["PSEPK", "ECOLI", "HELPG"] else ["putA"]):
            base = ROOT / "genes" / species / gene
            rp = base / f"{gene}-ai-review.yaml"
            up = base / f"{gene}-uniprot.txt"
            review = yaml.safe_load(rp.read_text())
            assert review["status"] == "COMPLETE"
            text = up.read_text()
            families = []
            for namespace, identifier in re.findall(r"^DR   (InterPro|PANTHER); ([^;]+);", text, re.M):
                families.append(namespace + ":" + identifier)
            origins = curated_functions(review)
            functions = set(origins)
            # These eight individually reviewed PutAs have both active sites.
            # This assertion is checked against the reviewed claims, not inferred
            # from the PANTHER label or a generic aldehyde-dehydrogenase hit.
            fused = gene == "putA"
            if fused:
                assert {"GO:0004657", "GO:0003842"} <= functions, rp
            proteins[review["id"]] = dict(system=species, families=families,
                                          functions=sorted(functions), fused=fused,
                                          claim_origins=origins)
            for p in [rp, up]:
                sources[str(p.relative_to(ROOT))] = hashlib.sha256(p.read_bytes()).hexdigest()
    for acc, function in [("P39634", "GO:0003842"), ("P07275", "GO:0003842"),
                          ("P16256", None), ("P32705", None)]:
        p = AUDIT / "family-controls" / f"{acc}.json"
        data = json.loads(p.read_text())
        families = [x["database"] + ":" + x["id"] for x in data["uniProtKBCrossReferences"]
                    if x["database"] in ["InterPro", "PANTHER"]]
        # PanF/ActP are family-exclusion controls; no unrelated activity id
        # is needed or asserted here. Their substrates are curated in PTHR48086.
        proteins[acc] = dict(system="CONTROL", families=families,
                            functions=[function] if function else [], fused=False)
        sources[str(p.relative_to(ROOT))] = hashlib.sha256(p.read_bytes()).hexdigest()
    return proteins, sources


def run(doc, proteins, enforce_fusion=True, enforce_pairing=True, enforce_activity=True):
    circuit = compile_module(doc)
    atoms = {a.node_id: a for a in iter_atoms(circuit)}
    assert set(atoms) == set(FUNCTION)
    for part in doc["module"]["parts"][1:]:
        participant = part["node"]["annotons"][0]["participant"]
        assert participant["required_domain"]["preferred_term"] == "Fused PRODH and GSALDH catalytic domains in one PutA polypeptide"

    def matches(key, p):
        a = atoms[key]
        return bool(set(a.family_ids) & set(p["families"])) and (
            not enforce_activity or FUNCTION[key] in p["functions"]) and (
            not enforce_fusion or key == TRANSPORT or p["fused"])

    def component(key, available):
        return any(matches(key, proteins[p]) for p in available)

    def coverage(available):
        # One and the same enzyme must satisfy both oxidative leaves. A union
        # of unrelated single-function proteins is not a fused PutA instance.
        for put in available:
            candidates = [p for p in available if not enforce_pairing or
                          proteins[p]["system"] == proteins[put]["system"]]
            if is_satisfied(circuit, lambda a: matches(a.node_id, proteins[put])
                            if enforce_fusion and a.node_id != TRANSPORT
                            else any(matches(a.node_id, proteins[p]) for p in candidates)):
                return True
        return False

    rows = []
    def check(case, observed, expected):
        assert observed == expected, (case, observed, expected)
        rows.append(dict(case=case, observed=observed, expected=expected))
    for species in SPECIES:
        panel = {p for p, v in proteins.items() if v["system"] == species}
        check(species + "_matched_component_coverage", coverage(panel), species in ["PSEPK", "ECOLI", "HELPG"])
        for key in [PRODH, GSALDH]:
            check(species + "_" + key, component(key, panel), True)
    for a, p in [("Q88D80", "Q88D81"), ("P09546", "P07117"), ("B5Z6C1", "B5Z6C0")]:
        check(a + "_without_transporter", coverage({a}), False)
        check(p + "_without_enzyme", coverage({p}), False)
    for acc in ["P39634", "P07275"]:
        for key in [PRODH, GSALDH]:
            check(acc + "_not_fused_" + key, component(key, {acc}), False)
    for acc in ["P16256", "P32705"]:
        check(acc + "_not_proline_transporter", component(TRANSPORT, {acc}), False)
    check("unverified_cross_strain_pair", coverage({"P09546", "Q88D81"}), False)
    check("empty", coverage(set()), False)
    # Explicit counterfactuals probe constraints independently of family names.
    # They are not biological assertions about new natural proteins.
    for key in ["synthetic_split_prodh", "synthetic_split_gsaldh", "synthetic_no_activity",
                "synthetic_inactive_prodh", "synthetic_inactive_gsaldh"]:
        check(key + "_cannot_complete", coverage({key, "P07117"}), False)
    check("split_union_cannot_replace_one_protein", coverage({"synthetic_split_prodh", "synthetic_split_gsaldh", "P07117"}), False)
    return rows


def main():
    doc = yaml.safe_load(MODULE.read_text())
    proteins, sources = load_evidence()
    for key, functions, fused in [("synthetic_split_prodh", ["GO:0004657"], False),
                                  ("synthetic_split_gsaldh", ["GO:0003842"], False),
                                  ("synthetic_inactive_prodh", ["GO:0003842"], True),
                                  ("synthetic_inactive_gsaldh", ["GO:0004657"], True),
                                  ("synthetic_no_activity", [], True)]:
        proteins[key] = dict(system="ECOLI", families=["InterPro:IPR025703"], functions=functions, fused=fused)
    cases = run(doc, proteins)
    mutations = []
    for name, options in [("ignore_same_polypeptide", {"enforce_fusion": False}),
                          ("pool_unmatched_strains", {"enforce_pairing": False}),
                          ("family_without_activity", {"enforce_activity": False})]:
        try:
            run(doc, proteins, **options)
        except AssertionError:
            mutations.append(name)
        else:
            raise AssertionError("Constraint mutation not detected: " + name)
    for index in [0, 1, 2]:
        mutant = deepcopy(doc)
        mutant["module"]["parts"][index]["optional"] = True
        try:
            run(mutant, proteins)
        except AssertionError:
            mutations.append("optional_step_" + str(index))
        else:
            raise AssertionError("Optional step mutation not detected")
    result = dict(status="PASS", check_kind="curation_coverage_consistency",
                  claim_extraction_checks=check_claim_extraction(),
                  required_activity_claim_origins={acc: {term: origins for term, origins in
                      p.get("claim_origins", {}).items() if term in FUNCTION.values()}
                      for acc, p in proteins.items() if p.get("claim_origins")},
                  cases=cases, case_count=len(cases), mutations_rejected=mutations,
                  source_sha256=sources, module_sha256=hashlib.sha256(MODULE.read_bytes()).hexdigest(),
                  native_flux_asserted=False,
                  limits=["Activities are reviewed claims (ACCEPT, KEEP_AS_NON_CORE, MODIFY replacements, or core synthesis), not independently verified assays. NEW proposals, retired and negated rows are excluded.",
                          "Evidence strength differs by target and source; matching coverage does not imply matching experimental support. See round1-review-response.md and the member reviews.",
                          "HELPG coverage is comparative inference, not a G27 assay.",
                          "Component-only panels lack a reviewed matched transporter, not necessarily a transporter in nature.",
                          "Same-protein and strain constraints are explicit evidence-oracle rules, not automatic free-text interpretation.",
                          "Synthetic fixtures are counterfactuals, not accession-level claims."])
    (AUDIT / "capacity-results.json").write_text(json.dumps(result, indent=2) + "\n")
    print(f"PASS: {len(cases)} curation-coverage checks; {len(mutations)} mechanism mutations rejected; {result['claim_extraction_checks']} claim-extraction checks")


if __name__ == "__main__":
    main()
