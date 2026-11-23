"""Evaluate the audited ethanolamine panel, not arbitrary proteomes or growth.

Production compilation supplies protein-role topology. Reviewed exact members,
compatible pairs and explicit experimental conditions supply the oracle. Unknown
means evidence is missing, not biological absence. Single-pass chemistry and
context-specific native growth are deliberately different outputs.
"""

from copy import deepcopy
from pathlib import Path
import argparse
import json
import yaml

from ai_gene_review.module_logic import compile_node, is_satisfied
from ai_gene_review.validation.local_source_text import quote_matches

ROOT = Path(__file__).resolve().parents[2]
SLUG = "bacterial_ethanolamine_uptake_catabolism"
AUDIT = ROOT / "analysis/module_audits" / SLUG
PAIRS = {
    ("P0AEJ6", "P19636"): "ECOLI",
    ("Q88QF1", "Q88QF2"): "PSEPK",
    ("A0A0H3GBB1", "A0A0H3GFM0"): "LISM4",
    ("P19264", "P19265"): "SALTY",
    ("Q9HX03", "Q9HX02"): "PSEAE",
}
EXPECTED = {
    "euth_transport_activity": ("PANTHER:PTHR40089:SF1", "GO:0034228"),
    "apc_ethanolamine_transport_activity": ("InterPro:IPR004757", "GO:0034228"),
    "eute_acetylating_activity": ("PANTHER:PTHR11699:SF68", "GO:0008774"),
    "aldb_acetaldehyde_dehydrogenase_activity": ("PANTHER:PTHR43111:SF1", "GO:0140087"),
    "acetaldehyde_reduction_activity": ("PANTHER:PTHR11496:SF94", "GO:0120542"),
    "eutd_coa_recycling_activity": ("PANTHER:PTHR43356:SF1", "GO:0008959"),
    "acetate_kinase_energy_conservation_activity": (
        "PANTHER:PTHR36169:SF1",
        "GO:0008776",
    ),
    "eutbc_reactivation_activity": ("PANTHER:PTHR32432:SF13", "GO:0008047"),
    "lt2_eutq_cargo_scaffold_activity": ("PANTHER:PTHR36169:SF1", "GO:0140378"),
}
CHEMISTRY = {
    "eutbc_complex_activity": ({"ethanolamine"}, {"acetaldehyde", "ammonium"}),
    "eute_acetylating_activity": (
        {"acetaldehyde", "coenzyme A", "NAD+"},
        {"acetyl-CoA", "NADH", "proton"},
    ),
    "aldb_acetaldehyde_dehydrogenase_activity": (
        {"acetaldehyde", "NAD+", "water"},
        {"acetate", "NADH", "protons"},
    ),
    "acetaldehyde_reduction_activity": (
        {"acetaldehyde", "NADH", "proton"},
        {"ethanol", "NAD+"},
    ),
    "eutd_coa_recycling_activity": (
        {"acetyl-CoA", "phosphate"},
        {"acetyl phosphate", "coenzyme A"},
    ),
    "acetate_kinase_energy_conservation_activity": (
        {"acetyl phosphate", "ADP"},
        {"acetate", "ATP"},
    ),
}


def read(path):
    return yaml.safe_load(path.read_text())


def walk(x):
    if isinstance(x, dict):
        yield x
        for v in x.values():
            yield from walk(v)
    elif isinstance(x, list):
        for v in x:
            yield from walk(v)


def index(doc):
    return {
        n["id"]: n
        for n in walk(doc["module"])
        if "id" in n
        and not n["id"].startswith(
            ("GO:", "UniProtKB:", "PANTHER:", "NCBITaxon:", "InterPro:")
        )
    }


def member_reviews(doc):
    wanted = {
        n["id"][10:]
        for n in walk(doc["module"])
        if str(n.get("id", "")).startswith("UniProtKB:")
    }
    panel = read(AUDIT / "member-panel.yaml")
    docs = {}
    for member in panel["members"]:
        d = read(ROOT / member["review_path"])
        assert d["id"] == member["accession"] and d["status"] == "COMPLETE", member
        docs[d["id"]] = d
    assert wanted <= docs.keys(), ("unreviewed module member", wanted - docs.keys())
    return docs


def reviewed_activity(d, term):
    return any(
        any(
            c.get(k, {}).get("id") == term
            for k in ["molecular_function", "contributes_to_molecular_function"]
        )
        for c in d.get("core_functions", [])
    )


def structural_checks(doc):
    nodes = index(doc)
    parts = doc["module"]["parts"]
    required = {p["node"]["id"] for p in parts if not p.get("optional", False)}
    assert required == {"eutbc_ethanolamine_deamination", "acetaldehyde_oxidation"}
    assert nodes["acetaldehyde_oxidation_routes"]["selection"] == "ONE_OR_MORE"
    assert (
        nodes["ethanolamine_transporter_implementations"]["selection"] == "ONE_OR_MORE"
    )
    assert len(doc["module"]["context"]["conditions"]) >= 3
    assert doc["module"]["context"]["taxa"][0]["term"]["id"] == "NCBITaxon:2"
    for aid, (fam, mf) in EXPECTED.items():
        a = nodes[aid]
        assert a["participant"]["family"]["term"]["id"] == fam, aid
        assert a["function"]["term"]["id"] == mf, aid
        assert any(e.get("supporting_text") for e in a["function"]["evidence"]), aid
    for aid, (inputs, outputs) in CHEMISTRY.items():
        f = nodes[aid]["function"]
        assert {v["preferred_term"] for v in f["substrates"]} == inputs, aid
        assert {v["preferred_term"] for v in f["products"]} == outputs, aid
    units = nodes["eutbc_complex_activity"]["participant"]["protein_complex"][
        "active_units"
    ]
    assert [u["id"] for u in units] == ["eutb_large_subunit", "eutc_small_subunit"]
    assert units[0]["participant"]["family"]["term"]["id"] == "PANTHER:PTHR39329:SF1"
    assert units[1]["participant"]["family"]["term"]["id"] == "PANTHER:PTHR39330"
    members = [
        {
            v["term"]["id"][10:]
            for v in u["participant"]["family"]["representative_members"]
        }
        for u in units
    ]
    assert members == [{p[0] for p in PAIRS}, {p[1] for p in PAIRS}]
    edges = {(e["source"], e["target"]) for e in doc["module"]["connections"]}
    for edge in [
        ("eutbc_ethanolamine_deamination", "acetaldehyde_reduction"),
        ("eutd_coa_recycling", "acetylating_eute_route"),
        ("acetaldehyde_reduction", "acetylating_eute_route"),
        ("eutbc_reactivation", "eutbc_ethanolamine_deamination"),
        ("lt2_eutq_cargo_scaffold", "eutbc_ethanolamine_deamination"),
    ]:
        assert edge in edges, edge
    assert all(e.get("evidence") for e in doc["module"]["connections"])


def oracle(doc, docs, proteins):
    nodes = index(doc)

    def available(atom):
        a = nodes[atom.node_id]
        if atom.node_id == "eutbc_complex_activity":
            units = a["participant"]["protein_complex"]["active_units"]
            pools = [
                {
                    x["term"]["id"][10:]
                    for x in u["participant"]["family"]["representative_members"]
                }
                & proteins
                for u in units
            ]
            return bool(
                atom.function_ids == ("GO:0008851",)
                and any(
                    b in pools[0]
                    and c in pools[1]
                    and reviewed_activity(docs[b], "GO:0008851")
                    and reviewed_activity(docs[c], "GO:0008851")
                    for b, c in PAIRS
                )
            )
        # Exact reviewed representative and activity, not a bare family hit.
        return any(
            p in proteins
            and p in docs
            and all(reviewed_activity(docs[p], mf) for mf in atom.function_ids)
            for p in atom.uniprots
        )

    return available


def evaluate(doc, docs, proteins, endpoint, env):
    nodes = index(doc)
    predicate = oracle(doc, docs, set(proteins))
    profiles = {p["id"]: p for p in read(AUDIT / "endpoint-profiles.yaml")["profiles"]}
    needed = profiles[endpoint]["required_nodes"]
    protein_capacity = all(
        is_satisfied(compile_node(nodes[n]), predicate) for n in needed
    )
    if not protein_capacity:
        return "UNSUPPORTED"
    if endpoint == "reactivation_after_inactivation":
        # Repair is not deamination: no ethanolamine-access or active-bound-cofactor
        # prerequisite. Fresh replacement cofactor is a separate explicit supply.
        if not {"P19264", "P19265"} <= set(proteins):
            return "UNSUPPORTED"
        if not env.get("bound_cofactor_inactivated"):
            return "UNKNOWN"
        if not {"ATP", "Mg2+", "replacement_AdoCbl"} <= set(env.get("supplies", [])):
            return "UNSUPPORTED"
        return "SUPPORTED_CHEMICAL_CAPACITY"
    if env.get("active_cobamide") is False:
        return "UNSUPPORTED"
    if env.get("active_cobamide") is not True:
        return "UNKNOWN"
    access = env.get("access")
    if access == "intracellular_assay":
        access_ok = env.get("system") == "assay"
    elif access == "LT2_diffusion_permissive":
        access_ok = {"P19264", "P19265"} <= set(proteins)
    elif access == "PAO1_Eat_independent_test":
        access_ok = {"Q9HX03", "Q9HX02"} <= set(proteins)
    elif access == "transporter_required":
        access_predicate = predicate
        if env.get("system") == "native":
            pair_taxa = {
                docs[b]["taxon"]["id"] for b, c in PAIRS if {b, c} <= set(proteins)
            }
            if len(pair_taxa) != 1:
                return "UNSUPPORTED"
            same_taxon = {
                p for p in proteins if p in docs and docs[p]["taxon"]["id"] in pair_taxa
            }
            access_predicate = oracle(doc, docs, same_taxon)
        access_ok = is_satisfied(
            compile_node(nodes["ethanolamine_uptake"]), access_predicate
        )
    else:
        return "UNKNOWN"
    if not access_ok:
        return "UNSUPPORTED"
    supplies = {
        "oxidative_acetyl_coa": {"NAD+", "CoA"},
        "oxidative_acetate": {"NAD+"},
        "reductive_ethanol": {"NADH"},
        "acetyl_phosphate_atp": {"NAD+", "CoA", "phosphate", "ADP"},
        "private_cofactor_cycling": {"NAD+", "CoA", "phosphate", "ADP"},
    }.get(endpoint, set())
    if not supplies <= set(env.get("supplies", [])):
        return "UNSUPPORTED"
    if endpoint == "private_cofactor_cycling":
        # These physiological/interaction witnesses are on the LT2 implementation.
        if not {"P19264", "P19265"} <= set(proteins):
            return "UNSUPPORTED"
    if endpoint == "sustained_carbon_utilization":
        # This is an explicit physiological witness, not a gene-list prediction.
        # PMID27325678: native PAO1 WT and delta-eat, pH7,20mM EA carbon tests.
        if (
            env.get("observed_context") == "PAO1_pH7_20mM_EA_carbon"
            and env.get("system") == "native"
            and env.get("genotype") in {"WT", "delta_eat"}
            and access == "PAO1_Eat_independent_test"
            and {"Q9HX03", "Q9HX02", "Q9HX05"} <= set(proteins)
        ):
            return "OBSERVED_IN_SPECIFIED_NATIVE_CONTEXT"
        return "UNKNOWN"
    return "SUPPORTED_CHEMICAL_CAPACITY"


def cofactor_cycle(doc):
    """Check the defined 1:1 oxidative/reductive scheme, not whole-cell flux.

    These coefficients cancel the explicit nicotinamide/CoA carriers and carbon
    intermediates. They do not claim complete atom/charge balance or prove the
    private-pool architecture is universal (Listeria has a different product ratio).
    """
    nodes = index(doc)
    coefficients = {
        "eutbc_complex_activity": 2,
        "eute_acetylating_activity": 1,
        "acetaldehyde_reduction_activity": 1,
        "eutd_coa_recycling_activity": 1,
        "acetate_kinase_energy_conservation_activity": 1,
    }
    net = {}
    for aid, flux in coefficients.items():
        f = nodes[aid]["function"]
        for slot, sign in [("substrates", -1), ("products", 1)]:
            for x in f[slot]:
                net[x["preferred_term"]] = net.get(x["preferred_term"], 0) + sign * flux
    for name in [
        "NAD+",
        "NADH",
        "coenzyme A",
        "acetaldehyde",
        "acetyl-CoA",
        "acetyl phosphate",
    ]:
        assert net[name] == 0, (name, net)
    assert (
        net["ethanolamine"] == -2
        and net["ammonium"] == 2
        and net["ethanol"] == net["acetate"] == net["ATP"] == 1
    )
    return {
        "reaction_coefficients": coefficients,
        "tracked_carrier_and_carbon_balance": net,
        "scope": "Defined one-to-one EutE/EutG scheme; not measured native flux or a universal fermentation ratio.",
    }


def verify_quotes(value, ref=""):
    count = 0
    if isinstance(value, dict):
        ref = value.get("source_id") or value.get("reference_id") or ref
        if str(value.get("id", "")).startswith(("PMID:", "file:")):
            ref = value["id"]
        if value.get("supporting_text"):
            if ref.startswith("PMID:"):
                p = ROOT / "publications" / (ref.replace(":", "_") + ".md")
            elif ref.startswith("file:"):
                p = next(
                    (
                        x / ref[5:]
                        for x in [ROOT / "genes", ROOT]
                        if (x / ref[5:]).exists()
                    ),
                    None,
                )
            else:
                raise AssertionError(("unresolved quotation source", ref))
            assert p and quote_matches(value["supporting_text"], p), (
                ref,
                value["supporting_text"],
            )
            count += 1
        count += sum(verify_quotes(v, ref) for v in value.values())
    elif isinstance(value, list):
        count += sum(verify_quotes(v, ref) for v in value)
    return count


def run(doc, docs):
    structural_checks(doc)
    n = index(doc)
    cases = []
    assay = {
        "system": "assay",
        "access": "intracellular_assay",
        "active_cobamide": True,
        "supplies": ["NAD+", "NADH", "CoA", "phosphate", "ADP"],
    }
    lt2 = {"P19264", "P19265"}
    full = lt2 | {"P41793", "P41795", "P41790", "Q9ZFV5", "Q9ZFV2", "P41796"}

    def case(name, proteins, profile, env, expected):
        actual = evaluate(doc, docs, proteins, profile, env)
        assert actual == expected, (name, actual, expected)
        cases.append({"name": name, "expected": expected, "actual": actual})

    for b, c in PAIRS:
        case(
            "matched nitrogen " + b,
            {b, c},
            "nitrogen_liberation",
            assay,
            "SUPPORTED_CHEMICAL_CAPACITY",
        )
        for missing in [b, c]:
            case(
                "missing chain " + missing,
                {b, c} - {missing},
                "nitrogen_liberation",
                assay,
                "UNSUPPORTED",
            )
    for b, _ in PAIRS:
        for _, c in PAIRS:
            if (b, c) not in PAIRS:
                case(
                    "unverified cross-pair " + b + "/" + c,
                    {b, c},
                    "nitrogen_liberation",
                    assay,
                    "UNSUPPORTED",
                )
    case(
        "no active cofactor",
        lt2,
        "nitrogen_liberation",
        {**assay, "active_cobamide": False},
        "UNSUPPORTED",
    )
    case(
        "unknown active cofactor",
        lt2,
        "nitrogen_liberation",
        {**assay, "active_cobamide": None},
        "UNKNOWN",
    )
    case(
        "unknown access",
        full,
        "nitrogen_liberation",
        {**assay, "access": None},
        "UNKNOWN",
    )
    case(
        "LT2 high-free-substrate without EutH",
        lt2,
        "nitrogen_liberation",
        {**assay, "access": "LT2_diffusion_permissive"},
        "SUPPORTED_CHEMICAL_CAPACITY",
    )
    case(
        "LT2 limiting access without EutH",
        lt2,
        "nitrogen_liberation",
        {**assay, "access": "transporter_required"},
        "UNSUPPORTED",
    )
    case(
        "LT2 limiting access with EutH",
        lt2 | {"P41796"},
        "nitrogen_liberation",
        {**assay, "access": "transporter_required"},
        "SUPPORTED_CHEMICAL_CAPACITY",
    )
    case(
        "LT2 condition not transferable to Listeria",
        {"A0A0H3GBB1", "A0A0H3GFM0"},
        "nitrogen_liberation",
        {**assay, "access": "LT2_diffusion_permissive"},
        "UNSUPPORTED",
    )
    case(
        "nitrogen alone is not oxidation",
        lt2,
        "oxidative_acetyl_coa",
        assay,
        "UNSUPPORTED",
    )
    for profile in [
        "oxidative_acetyl_coa",
        "reductive_ethanol",
        "acetyl_phosphate_atp",
    ]:
        case("LT2 " + profile, full, profile, assay, "SUPPORTED_CHEMICAL_CAPACITY")
    case(
        "EutG not oxidative replacement",
        lt2 | {"P41795"},
        "oxidative_acetyl_coa",
        assay,
        "UNSUPPORTED",
    )
    case(
        "EutE not reductive replacement",
        lt2 | {"P41793"},
        "reductive_ethanol",
        assay,
        "UNSUPPORTED",
    )
    case(
        "missing CoA",
        full,
        "oxidative_acetyl_coa",
        {**assay, "supplies": ["NAD+"]},
        "UNSUPPORTED",
    )
    case(
        "missing NADH",
        full,
        "reductive_ethanol",
        {**assay, "supplies": ["NAD+", "CoA"]},
        "UNSUPPORTED",
    )
    for p in ["P41790", "Q9ZFV5"]:
        case(
            "ATP sequence missing " + p,
            full - {p},
            "acetyl_phosphate_atp",
            assay,
            "UNSUPPORTED",
        )
        case(
            "nitrogen independent of " + p,
            full - {p},
            "nitrogen_liberation",
            assay,
            "SUPPORTED_CHEMICAL_CAPACITY",
        )
    case(
        "EutA not every-turnover prerequisite",
        full - {"Q9ZFV2"},
        "nitrogen_liberation",
        assay,
        "SUPPORTED_CHEMICAL_CAPACITY",
    )
    case(
        "no growth from static complete genes",
        full,
        "sustained_carbon_utilization",
        assay,
        "UNKNOWN",
    )
    case(
        "defined private cofactor cycle",
        full,
        "private_cofactor_cycling",
        assay,
        "SUPPORTED_CHEMICAL_CAPACITY",
    )
    for p in ["P41795", "P41790"]:
        case(
            "private cycle requires " + p,
            full - {p},
            "private_cofactor_cycling",
            assay,
            "UNSUPPORTED",
        )
        case(
            "single-pass oxidation independent of " + p,
            full - {p},
            "oxidative_acetyl_coa",
            assay,
            "SUPPORTED_CHEMICAL_CAPACITY",
        )
    repair = {
        **assay,
        "bound_cofactor_inactivated": True,
        "supplies": ["ATP", "Mg2+", "replacement_AdoCbl"],
    }
    case(
        "EutA repairs damaged holoenzyme",
        lt2 | {"Q9ZFV2"},
        "reactivation_after_inactivation",
        repair,
        "SUPPORTED_CHEMICAL_CAPACITY",
    )
    case(
        "repair without substrate access or active bound cofactor",
        lt2 | {"Q9ZFV2"},
        "reactivation_after_inactivation",
        {**repair, "access": None, "active_cobamide": False},
        "SUPPORTED_CHEMICAL_CAPACITY",
    )
    case(
        "no EutA in repair implementation",
        lt2,
        "reactivation_after_inactivation",
        repair,
        "UNSUPPORTED",
    )
    case(
        "repair needs ATP",
        full,
        "reactivation_after_inactivation",
        {**repair, "supplies": ["Mg2+", "replacement_AdoCbl"]},
        "UNSUPPORTED",
    )
    case(
        "EutA homolog not arbitrary cross-pair",
        {"P0AEJ6", "P19636", "Q9ZFV2"},
        "reactivation_after_inactivation",
        repair,
        "UNSUPPORTED",
    )
    pao1 = {"Q9HX03", "Q9HX02", "Q9HX05"}
    case(
        "PA4022 direct acetate route",
        pao1,
        "oxidative_acetate",
        assay,
        "SUPPORTED_CHEMICAL_CAPACITY",
    )
    case("PA4022 not acylating", pao1, "oxidative_acetyl_coa", assay, "UNSUPPORTED")
    case(
        "foreign EutH is not a native PAO1 access witness",
        pao1 | {"P41796"},
        "oxidative_acetate",
        {**assay, "system": "native", "access": "transporter_required"},
        "UNSUPPORTED",
    )
    case(
        "human ALDH2 not bacterial selector",
        lt2 | {"P05091"},
        "oxidative_acetate",
        assay,
        "UNSUPPORTED",
    )
    case(
        "PduP family hit not EutE",
        lt2 | {"Q9XDN1"},
        "oxidative_acetyl_coa",
        assay,
        "UNSUPPORTED",
    )
    for genotype in ["WT", "delta_eat"]:
        context = {
            **assay,
            "system": "native",
            "access": "PAO1_Eat_independent_test",
            "observed_context": "PAO1_pH7_20mM_EA_carbon",
            "genotype": genotype,
        }
        case(
            "observed PAO1 " + genotype,
            pao1,
            "sustained_carbon_utilization",
            context,
            "OBSERVED_IN_SPECIFIED_NATIVE_CONTEXT",
        )
        case(
            "assay label is not native observation " + genotype,
            pao1,
            "sustained_carbon_utilization",
            {**context, "system": "assay"},
            "UNKNOWN",
        )
        case(
            "ATCC17933 ExaC not PAO1 native witness",
            pao1 - {"Q9HX05"} | {"Q9ZAA1"},
            "sustained_carbon_utilization",
            context,
            "UNKNOWN",
        )
    # Compiler is evaluated independently of the endpoint profile's required nodes.
    circuit = compile_node(doc["module"])
    assert not is_satisfied(circuit, oracle(doc, docs, lt2))
    assert is_satisfied(circuit, oracle(doc, docs, lt2 | {"P41793"}))
    assert is_satisfied(circuit, oracle(doc, docs, full))
    cases.append(
        {
            "name": "production root requires oxidation; optional roles do not replace it",
            "actual": "PASS",
        }
    )
    # Whole-protein activity is separate from a domain-only edited review.
    kinase_only = deepcopy(docs)
    kinase_only["Q9ZFV5"]["core_functions"] = [
        c
        for c in kinase_only["Q9ZFV5"]["core_functions"]
        if c.get("molecular_function", {}).get("id") != "GO:0140378"
    ]
    assert not is_satisfied(
        compile_node(n["lt2_eutq_cargo_scaffold"]), oracle(doc, kinase_only, full)
    )
    assert is_satisfied(
        compile_node(n["acetate_kinase_energy_conservation"]),
        oracle(doc, kinase_only, full),
    )
    cases.append(
        {"name": "kinase evidence does not satisfy scaffold", "actual": "PASS"}
    )
    mutants = []
    for name, change in [
        (
            "make deamination optional",
            lambda m: m["module"]["parts"][1].update(optional=True),
        ),
        (
            "make oxidation optional",
            lambda m: m["module"]["parts"][2].update(optional=True),
        ),
        (
            "make uptake universally required",
            lambda m: m["module"]["parts"][0].update(optional=False),
        ),
        (
            "swap EutG chemistry",
            lambda m: index(m)["acetaldehyde_reduction_activity"]["function"].update(
                products=[{"preferred_term": "acetate"}]
            ),
        ),
        (
            "wrong EutQ scaffold family",
            lambda m: index(m)["lt2_eutq_cargo_scaffold_activity"]["participant"][
                "family"
            ]["term"].update(id="PANTHER:PTHR11496:SF94"),
        ),
        (
            "drop small chain",
            lambda m: index(m)["eutbc_complex_activity"]["participant"][
                "protein_complex"
            ]["active_units"].pop(),
        ),
        (
            "remove recycling edge",
            lambda m: m["module"].update(
                connections=[
                    e
                    for e in m["module"]["connections"]
                    if not (
                        e["source"] == "eutd_coa_recycling"
                        and e["target"] == "acetylating_eute_route"
                    )
                ]
            ),
        ),
        (
            "remove environmental context",
            lambda m: m["module"]["context"].update(conditions=[]),
        ),
    ]:
        m = deepcopy(doc)
        change(m)
        try:
            structural_checks(m)
        except (AssertionError, KeyError):
            mutants.append(name)
        else:
            raise AssertionError(("mutation escaped", name))
    return {
        "capacity_cases": len(cases),
        "mutation_cases": len(mutants),
        "cases": cases,
        "mutations_detected": mutants,
        "cofactor_cycle": cofactor_cycle(doc),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    doc = read(ROOT / "modules" / (SLUG + ".yaml"))
    docs = member_reviews(doc)
    result = run(doc, docs)
    result.update(
        status="PASS",
        reviewed_members=len(docs),
        module_and_profile_quotes=verify_quotes(doc)
        + verify_quotes(read(AUDIT / "endpoint-profiles.yaml")),
        scope="Exact curated panel; chemical capacity and explicitly witnessed native physiology, not arbitrary genome completeness or inferred growth.",
    )
    if args.output:
        args.output.write_text(yaml.safe_dump(result, sort_keys=False, width=100))
    print(
        json.dumps(
            {
                k: v
                for k, v in result.items()
                if k not in ["cases", "mutations_detected"]
            },
            indent=2,
        )
    )
