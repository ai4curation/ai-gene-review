"""Evidence-qualified capacity audit using the production module circuit engine.

False means this closed evidence panel does not establish the profile, not that a
biological pathway is absent. Product chemistry and experimental constraints are
explicit oracle inputs; the Boolean compiler does not itself encode them.
"""

import copy
import hashlib
import itertools
import json
from pathlib import Path
import re

import yaml

from ai_gene_review.module_logic import compile_node, core_atoms, is_satisfied, iter_atoms

AUDIT = Path(__file__).resolve().parent
ROOT = AUDIT.parents[3]
BASE = AUDIT.parent
MODULE = ROOT / "modules/bacterial_lipoprotein_maturation.yaml"
MEMBERS = {
    "P60955": "ECOLI/lgt", "P00804": "ECOLI/lspA", "P23930": "ECOLI/lnt",
    "Q88CN8": "PSEPK/lgt", "Q88Q91": "PSEPK/lspA", "Q88DN4": "PSEPK/lnt",
    "O34752": "BACSU/lgt", "Q45479": "BACSU/lspA", "P54392": "BACSU/ypjA",
    "Q5LGL3": "BACFN/BF9343_0945", "Q89ZL3": "BACTN/BT_4364",
    "Q2G006": "STAA8/SAOUHSC_00822", "Q2FVF3": "STAA8/SAOUHSC_02761",
    "Q813T3": "BACCR/BC_1526",
}
ROUTES = {
    "lnt": "lnt_n_acylation_step", "lnb": "lnb_n_acylation_step",
    "lnsab": "lnsab_n_acylation_step", "lit": "lit_intramolecular_transfer_step",
    "lhat": "lhat_n_acetylation_step",
}
PRODUCTS = {
    "lnt": "three_long_acyl_chains", "lnb": "three_long_acyl_chains",
    "lnsab": "three_long_acyl_chains", "lit": "lyso_two_long_acyl_chains",
    "lhat": "N_acetyl_two_long_acyl_chains",
}
CORE = {"lgt_diacylglyceryl_transferase", "lspa_signal_peptidase_ii"}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def walk(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)


def refs_in(doc):
    for item in walk(doc):
        for key in ("id", "reference_id", "source_id"):
            ref = item.get(key, "")
            if isinstance(ref, str) and ref.startswith(("file:", "PMID:")):
                yield ref


def resolve(ref):
    if ref.startswith("PMID:"):
        path = ROOT / f"publications/PMID_{ref.split(':')[1]}.md"
    else:
        relative = ref[5:]
        choices = [ROOT / "genes" / relative, ROOT / relative]
        path = next((p for p in choices if p.is_file()), choices[-1])
    assert path.is_file(), ref
    return path


def load_members():
    catalog, closure, sources = {}, {}, {}
    for acc, target in MEMBERS.items():
        gene = target.split("/")[1]
        folder = ROOT / "genes" / target
        path = folder / f"{gene}-ai-review.yaml"
        doc = yaml.safe_load(path.read_text())
        assert doc["id"] == acc and doc["status"] == "COMPLETE"
        raw = folder / f"{gene}-uniprot.txt"
        text = raw.read_text()
        taxon = int(doc["taxon"]["id"].split(":")[1])
        assert int(re.search(r"^OX   NCBI_TaxID=(\d+)", text, re.M)[1]) == taxon
        families = set()
        for database, identifier in re.findall(r"^DR   (PANTHER|InterPro|Pfam|NCBIfam); ([^;]+);", text, re.M):
            families.add(f"{database}:{identifier}")
            if database == "PANTHER":
                families.add(f"PANTHER:{identifier.split(':')[0]}")
        enables, contributes = set(), set()
        for core in doc.get("core_functions", []):
            if core.get("molecular_function"):
                enables.add(core["molecular_function"]["id"])
            if core.get("contributes_to_molecular_function"):
                contributes.add(core["contributes_to_molecular_function"]["id"])
            assert core.get("supported_by"), target
        catalog[acc] = {"taxon": taxon, "families": families, "enables": enables,
                        "contributes": contributes, "qualified": True, "review": str(path.relative_to(ROOT))}
        rows = doc.get("existing_annotations", [])
        closure[acc] = {"review": str(path.relative_to(ROOT)), "sha256": sha(path), "taxon": taxon,
                        "ordered_rows": len(rows), "proposal_rows_present": sum(r["review"]["action"] == "NEW" for r in rows),
                        "active_proposals": sum(r["review"]["action"] == "NEW" and not r.get("retired") for r in rows),
                        "molecular_functions": sorted(enables), "contributions": sorted(contributes),
                        "official_classifications": sorted(families),
                        "evidence_scope": "curated homology and sequence inference" if target.startswith("PSEPK") else "target evidence; see source-specific consultation limits"}
        for p in folder.iterdir():
            if p.is_file():
                sources[str(p.relative_to(ROOT))] = sha(p)
        for ref in refs_in(doc):
            p = resolve(ref)
            sources[str(p.relative_to(ROOT))] = sha(p)
    # These are exact sequence-resolved experimental controls, not new reviewed members.
    bridge = json.loads((BASE / "lnsab-consultation/epidermidis-identity-bridge.json").read_text())
    for gene, key, role, npid in [("SE_0583", "control:AAO04180", "enables", "NP764138"),
                                  ("SE_2027", "control:AAO05668", "contributes", "NP765582")]:
        item = bridge[gene]
        assert item["taxon"] == 176280 and not item["current_gene_review"]
        data = json.loads((BASE / f"lnsab-consultation/{npid}-uniparc.json").read_text())["results"][0]
        assert data["sequence"]["value"] == item["sequence"]["value"]
        families = {f"InterPro:{f['interproGroup']['id']}" for f in data["sequenceFeatures"] if "interproGroup" in f}
        catalog[key] = {"taxon": 176280, "families": families, "enables": set(), "contributes": set(),
                        "qualified": True, "scope": "cellular pairing control only"}
        catalog[key][role].add("GO:0016747")
    # Explicit synthetic inputs test unsafe generalization; none is an accession claim.
    fixtures = {
        "fixture:generic_signal_peptidase": ({"GO:0009003"}, set()),
        "fixture:generic_acyltransferase": ({"GO:0016747"}, set()),
        "fixture:unassayed_LhaT_family_member": ({"GO:0008080"}, {"PANTHER:PTHR40042"}),
    }
    for key, (functions, families) in fixtures.items():
        catalog[key] = {"taxon": 224308 if "LhaT" in key else 83333, "families": families,
                        "enables": functions, "contributes": set(), "qualified": False,
                        "scope": "synthetic hypothesis, not demonstrated activity"}
    return catalog, closure, sources


class Oracle:
    def __init__(self, doc, catalog, case, policy="strict"):
        self.catalog, self.case, self.policy = catalog, case, policy
        self.annotons = {a["id"]: a for node in walk(doc["module"]) for a in node.get("annotons", [])}
        self.pool = {acc: catalog[acc] for acc in case["proteins"] if self.allowed(acc)}
        pair_data = json.loads((BASE / "lnsab-consultation/pairing-evidence.json").read_text())
        convert = {"Sa:Q2G006": "Q2G006", "Sa:Q2FVF3": "Q2FVF3",
                   "Se:AAO04180": "control:AAO04180", "Se:AAO05668": "control:AAO05668"}
        self.pairs = {(convert[c["A"]], convert[c["B"]]): c for c in pair_data["cases"]}

    def allowed(self, acc):
        if self.policy == "ignore_taxon":
            return True
        if self.case["mode"] == "pair_control":
            return self.case["panel_taxon"] == 93061 and acc in {"Q2G006", "Q2FVF3", "control:AAO04180", "control:AAO05668"}
        if self.case["mode"] == "bf_ecoli_rescue":
            return self.case["panel_taxon"] == 83333 and acc in {"P60955", "P00804", "Q5LGL3"}
        return self.catalog[acc]["taxon"] == self.case["panel_taxon"]

    def match(self, participant, acc):
        family = participant.get("family", {})
        ids = {t["id"] for t in [family.get("term"), *family.get("family_terms", [])] if t}
        if ids:
            return bool(ids & self.catalog[acc]["families"])
        reps = {r["term"]["id"].split(":", 1)[1] for r in family.get("representative_members", [])}
        return acc in reps

    def compatible_complex(self, participant, functions):
        units = participant["protein_complex"]["active_units"]
        # The independent source contract requires both named roles in the model.
        assert {u["id"] for u in units} == {"lnsa_catalytic_unit", "lnsb_partner_unit"}, "LnsAB partner requirement erased"
        candidates = []
        for unit in units:
            slot = "enables" if unit["id"] == "lnsa_catalytic_unit" else "contributes"
            candidates.append([acc for acc, record in self.pool.items()
                               if record["qualified"] and self.match(unit["participant"], acc)
                               and functions <= record[slot]])
        if self.policy == "drop_partner_gate":
            return bool(candidates[0])
        for a, b in itertools.product(*candidates):
            observed = self.pairs.get((a, b))
            if not observed:
                continue
            if not observed["cellular_product"] and self.policy != "ignore_compatibility":
                continue
            if self.case["mode"] == "purified":
                if not observed["purified_reconstitution"]:
                    continue
                if self.case.get("pg_donor") or self.policy == "ignore_donors":
                    return True
            elif self.case.get("cellular_environment"):
                return True
        return False

    def __call__(self, atom):
        source = self.annotons[atom.node_id]
        participant = source["participant"]
        functions = set(atom.function_ids)
        if self.policy == "go_only":
            return any(functions <= r["enables"] | r["contributes"] for r in self.pool.values())
        if participant["selector_type"] == "PROTEIN_COMPLEX":
            return self.case["mature_diacyllipoprotein"] and self.compatible_complex(participant, functions)
        selected = [acc for acc, record in self.pool.items()
                    if self.match(participant, acc) and functions <= record["enables"]
                    and (record["qualified"] or (self.policy == "universal_lhat" and atom.node_id == "lhat_n_acetyltransferase"))]
        if not selected:
            return False
        if atom.node_id == "lgt_diacylglyceryl_transferase":
            return self.case["precursor"] and self.case["pg_for_lgt"]
        if atom.node_id == "lspa_signal_peptidase_ii":
            return True  # The required Lgt circuit gate supplies its upstream step.
        if not self.case["mature_diacyllipoprotein"]:
            return False
        if atom.node_id == "lnt_n_acyltransferase":
            return bool(self.case.get("phospholipid_donor") or self.policy == "ignore_donors")
        if atom.node_id == "lnb_n_acyltransferase":
            if self.policy == "force_lnb_pg" and not self.case.get("pg_donor"):
                return False
            return self.case["mode"] != "purified" and bool(self.case.get("cellular_environment"))
        if atom.node_id == "lit_intramolecular_acyltransferase":
            return True  # Existing chain is relocated; no third-chain donor is required.
        if atom.node_id == "lhat_n_acetyltransferase":
            return bool(self.policy == "ignore_donors" or (self.case.get("acetylated_lipid_carrier") and self.case.get("donor_accessible")))
        raise AssertionError(atom.node_id)


def evaluate(doc, catalog, case, policy="strict"):
    oracle = Oracle(doc, catalog, case, policy)
    nodes = {n["id"]: n for n in walk(doc["module"]) if "module_type" in n}
    circuit = compile_node(doc["module"], ROOT / "modules")
    result = {"module": is_satisfied(circuit, oracle)}
    for short, node in ROUTES.items():
        result[short] = is_satisfied(compile_node(nodes[node], ROOT / "modules"), oracle)
    products = {("three_long_acyl_chains" if policy == "collapse_products" else PRODUCTS[r]) for r in ROUTES if result[r]}
    result["terminal_products"] = sorted(products)
    result["complete_products"] = sorted(products) if result["module"] else []
    return result


def compare(expected, actual):
    return {k: {"expected": v, "actual": actual[k]} for k, v in expected.items() if v != actual[k]}


def main():
    doc = yaml.safe_load(MODULE.read_text())
    catalog, closure, source_hashes = load_members()
    baseline = json.loads((BASE / "baseline.json").read_text())
    original_rows = 0
    original_proposals = 0
    initial_accessions = set()
    for path, frozen in baseline["reviews"].items():
        before = frozen["document"]
        initial_accessions.add(before["id"])
        current = yaml.safe_load((ROOT / path).read_text())
        old_rows = before.get("existing_annotations", [])
        new_rows = current.get("existing_annotations", [])
        def payload(row):
            return {k: v for k, v in row.items() if k != "review"}
        assert [payload(r) for r in old_rows] == [payload(r) for r in new_rows[:len(old_rows)]], path
        original_rows += len(old_rows)
        original_proposals += sum(r["review"]["action"] == "NEW" for r in old_rows)
    new_accessions = set(MEMBERS) - initial_accessions - {"P54392"}
    annotation_accounting = {
        "original_ordered_payloads_preserved": original_rows,
        "original_historical_proposals_preserved": original_proposals,
        "reused_LhaT_rows": closure["P54392"]["ordered_rows"],
        "reused_LhaT_historical_proposals": closure["P54392"]["proposal_rows_present"],
        "newly_authored_proposals": sum(closure[a]["proposal_rows_present"] for a in new_accessions),
    }
    assert annotation_accounting == {
        "original_ordered_payloads_preserved": 73, "original_historical_proposals_preserved": 2,
        "reused_LhaT_rows": 2, "reused_LhaT_historical_proposals": 1, "newly_authored_proposals": 13,
    }
    representatives = {m["term"]["id"].split(":", 1)[1] for n in walk(doc["module"]) for m in n.get("representative_members", [])}
    assert representatives == set(MEMBERS), "Exact 14-member closure changed"
    circuit = compile_node(doc["module"], ROOT / "modules")
    assert {a.node_id for a in core_atoms(circuit)} == CORE, "Shared core must not force terminal chemistry"
    assert len(list(iter_atoms(circuit))) == 7
    atom_receipt = [{"id": a.node_id, "members": a.uniprots, "functions": a.function_ids,
                     "families": a.family_ids} for a in iter_atoms(circuit)]
    complex_atom = next(a for a in iter_atoms(circuit) if a.node_id == "lnsab_n_acyltransferase")
    assert not complex_atom.uniprots and not complex_atom.family_ids
    cases = json.loads((AUDIT / "cases.json").read_text())
    results = []
    for case in cases:
        actual = evaluate(doc, catalog, case)
        diff = compare(case["expected"], actual)
        assert not diff, (case["name"], diff)
        results.append({"name": case["name"], "result": "PASS", "capacity": actual,
                        "meaning": "Evidence-qualified capacity in the specified context; not an inference of native flux or pathway absence."})
    mutations = []
    for policy in ["drop_partner_gate", "ignore_compatibility", "universal_lhat", "ignore_donors",
                   "collapse_products", "force_lnb_pg", "go_only", "ignore_taxon"]:
        killed = [c["name"] for c in cases if compare(c["expected"], evaluate(doc, catalog, c, policy))]
        assert killed, f"Surviving mutation: {policy}"
        mutations.append({"mutation": policy, "layer": "external oracle", "detected_by": killed})
    forced = copy.deepcopy(doc)
    lnt_node = next(n for n in walk(doc["module"]) if n.get("id") == ROUTES["lnt"])
    forced["module"]["parts"].append({"order": 4, "node": copy.deepcopy(lnt_node)})
    killed = [c["name"] for c in cases if compare(c["expected"], evaluate(forced, catalog, c))]
    assert killed
    mutations.append({"mutation": "force_lnt_required", "layer": "module circuit", "detected_by": killed})
    erased = copy.deepcopy(doc)
    unit_parent = next(n for n in walk(erased) if "active_units" in n)
    unit_parent["active_units"] = unit_parent["active_units"][:1]
    try:
        evaluate(erased, catalog, next(c for c in cases if c["name"] == "lnsa_alone"))
    except AssertionError as error:
        assert "partner requirement erased" in str(error)
        mutations.append({"mutation": "erase_lnsb_active_unit", "layer": "module source contract", "detected_by": [str(error)]})
    else:
        raise AssertionError("Erased partner escaped independent source contract")
    for ref in refs_in(doc):
        p = resolve(ref)
        source_hashes[str(p.relative_to(ROOT))] = sha(p)
    source_hashes[str(MODULE.relative_to(ROOT))] = sha(MODULE)
    for p in [ROOT / "src/ai_gene_review/module_logic.py", ROOT / "src/ai_gene_review/module_gene_symbols.py",
              BASE / "lnsab-consultation/pairing-evidence.json", BASE / "lnsab-consultation/epidermidis-identity-bridge.json",
              BASE / "lnsab-consultation/NP764138-uniparc.json", BASE / "lnsab-consultation/NP765582-uniparc.json"]:
        source_hashes[str(p.relative_to(ROOT))] = sha(p)
    (AUDIT / "member-closure.json").write_text(json.dumps(closure, indent=2) + "\n")
    (AUDIT / "source-hashes.json").write_text(json.dumps(source_hashes, indent=2) + "\n")
    receipt = {"result": "PASS", "module_sha256": sha(MODULE), "cases": results, "mutations": mutations,
               "production_atoms": atom_receipt, "production_core": sorted(CORE),
               "annotation_accounting": annotation_accounting,
               "member_count": len(closure), "ordered_annotation_rows": sum(r["ordered_rows"] for r in closure.values()),
               "proposal_rows_present": sum(r["proposal_rows_present"] for r in closure.values()),
               "active_proposals": sum(r["active_proposals"] for r in closure.values()),
               "engine_limit": "Complex active_units, compatibility, product chemistry and donors require the external oracle. Bare GO-only matching is unsafe.",
               "native_flux": "No Boolean result is relabeled as measured native flux.", "full_corpus_validation": False}
    (AUDIT / "results.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps({"result": "PASS", "cases": len(cases), "killed_mutations": len(mutations),
                      "members": len(closure), "source_files": len(source_hashes)}))


if __name__ == "__main__":
    main()
