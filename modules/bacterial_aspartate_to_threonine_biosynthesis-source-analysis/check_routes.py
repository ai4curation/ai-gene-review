"""Check native capacity, fused domains, LysC chains and reaction resources.

Uses the production Boolean compiler with an explicit native-product/chain oracle.
The compiler itself does not infer taxonomy, expand complex subunits or propagate
metabolites. Tests describe the sampled model, not universal organism viability.
"""

from pathlib import Path
import yaml
from ai_gene_review.module_logic import compile_node, is_satisfied

ROOT = Path(__file__).resolve().parents[2]
SLUG = "bacterial_aspartate_to_threonine_biosynthesis"
DATA = ROOT / "analysis/module_audits" / SLUG


def walk(x):
    if isinstance(x, dict):
        yield x
        for v in x.values():
            yield from walk(v)
    elif isinstance(x, list):
        for v in x:
            yield from walk(v)


def main():
    doc = yaml.safe_load((ROOT / "modules" / f"{SLUG}.yaml").read_text())
    panel = yaml.safe_load((DATA / "members.yaml").read_text())
    products = {(m["organism"], m["gene"]): m["accession"] for m in panel}
    species = {m["accession"]: m["organism"] for m in panel}
    species.update({"P26512-1": "CORGL", "P26512-2": "CORGL"})
    inventory = {
        org: {a for a, o in species.items() if o == org}
        for org in set(species.values())
    }
    nodes = {n["id"]: n for n in walk(doc["module"]) if "id" in n}
    activities = {
        a["id"]: a for n in walk(doc["module"]) for a in n.get("annotons", [])
    }
    required = {}
    for key, a in activities.items():
        # Only selected gene products count. Family exemplars are metadata.
        chosen = {
            n["gene_product"]["term"]["id"].split(":", 1)[1]
            for n in walk(a["participant"])
            if "gene_product" in n
        }
        assert chosen and chosen <= set(species), (key, chosen)
        assert len({species[p] for p in chosen}) == 1, (key, "mixed native assembly")
        required[key] = chosen
    external = {
        "ATP",
        "NADPH",
        "water",
        "pyridoxal 5'-phosphate",
        "L-phosphoserine",
        "L-homoserine",
    }
    cases = []

    def check(name, node, org, present, expected, resources=None):
        available = external if resources is None else resources

        def holds(atom):
            key = atom.node_id
            a = activities[key]
            need = required[key]
            inputs = {
                s["preferred_term"]
                for s in a["function"].get("substrates", [])
                + a["function"].get("cofactors", [])
            }
            # Homoserine is internal to full routes; external at the isolated ThrH boundary.
            resource_need = inputs & external
            if key != "pseae_thrh_phosphotransfer":
                resource_need.discard("L-homoserine")
            return (
                need <= present
                and all(species[p] == org for p in need)
                and resource_need <= available
            )

        observed = is_satisfied(compile_node(nodes[node]), holds)
        assert observed == expected, (name, expected, observed)
        cases.append(
            dict(
                case=name,
                node=node,
                organism=org,
                present=sorted(present),
                resources=sorted(available),
                expected=expected,
                observed=observed,
            )
        )

    full = doc["module"]["id"]
    check("Empty panel cannot synthesize threonine", full, "ECOLI", set(), False)
    for org in ["PSEPK", "ECOLI", "CORGL"]:
        check(org + " complete native route", full, org, inventory[org], True)
        check(
            org + " cannot use ATP as replacement for NADPH",
            full,
            org,
            inventory[org],
            False,
            external - {"NADPH"},
        )
        check(
            org + " cannot dispense with ATP",
            full,
            org,
            inventory[org],
            False,
            external - {"ATP"},
        )
        check(
            org + " terminal PLP cofactor required",
            full,
            org,
            inventory[org],
            False,
            external - {"pyridoxal 5'-phosphate"},
        )
    for gene in ["PP_4473", "asd__Q88LE4", "hom", "thrB", "thrC"]:
        present = inventory["PSEPK"] - {products["PSEPK", gene]}
        check(
            "PSEPK canonical " + gene + " cannot be rescued by disputed paralogs",
            full,
            "PSEPK",
            present,
            False,
        )
        check(
            "Foreign proteins do not rescue missing PSEPK " + gene,
            full,
            "PSEPK",
            present | (set(species) - inventory["PSEPK"]),
            False,
        )
    for gene in ["asd__Q88LE2", "PP_0664", "PP_0662"]:
        check(
            "PSEPK does not require unresolved " + gene,
            full,
            "PSEPK",
            inventory["PSEPK"] - {products["PSEPK", gene]},
            True,
        )
    for gene in ["thrA", "metL", "lysC"]:
        check(
            "ECOLI alternative capacity after loss of " + gene,
            full,
            "ECOLI",
            inventory["ECOLI"] - {products["ECOLI", gene]},
            True,
        )
    check(
        "LysC cannot replace either HDH domain",
        full,
        "ECOLI",
        inventory["ECOLI"] - {products["ECOLI", "thrA"], products["ECOLI", "metL"]},
        False,
    )
    check(
        "ThrA alone supplies both nonadjacent domains with Asd ThrB ThrC",
        full,
        "ECOLI",
        {products["ECOLI", g] for g in ["thrA", "asd", "thrB", "thrC"]},
        True,
    )
    check(
        "MetL alone supplies both nonadjacent domains with Asd ThrB ThrC",
        full,
        "ECOLI",
        {products["ECOLI", g] for g in ["metL", "asd", "thrB", "thrC"]},
        True,
    )
    for gene in ["asd", "thrB", "thrC"]:
        check(
            "ECOLI fused enzymes do not bypass " + gene,
            full,
            "ECOLI",
            inventory["ECOLI"] - {products["ECOLI", gene]},
            False,
        )
    lysc_units = activities["corgl_lysc_ak"]["participant"]["protein_complex"][
        "active_units"
    ]
    assert {
        unit["participant"]["gene_product"]["term"]["id"]: unit["stoichiometry"]
        for unit in lysc_units
    } == {"UniProtKB:P26512-1": "2", "UniProtKB:P26512-2": "2"}
    check(
        "CORGL lysC deletion removes both alternative-initiation products",
        full,
        "CORGL",
        inventory["CORGL"] - {"P26512", "P26512-1", "P26512-2"},
        False,
    )
    for chain in ["P26512-1", "P26512-2"]:
        check(
            "CORGL assembly requires chain " + chain,
            full,
            "CORGL",
            inventory["CORGL"] - {chain},
            False,
        )
    for gene in ["asd", "hom", "thrB", "thrC"]:
        check(
            "CORGL requires " + gene,
            full,
            "CORGL",
            inventory["CORGL"] - {products["CORGL", gene]},
            False,
        )
    check(
        "PSEAE ThrH does not establish a complete PAO1 route",
        full,
        "PSEAE",
        inventory["PSEAE"],
        False,
    )
    comparator = "pseae_thrh_comparator"
    check(
        "PSEAE ThrH supported isolated phosphotransfer",
        comparator,
        "PSEAE",
        inventory["PSEAE"],
        True,
    )
    check(
        "ThrH requires phosphoserine donor",
        comparator,
        "PSEAE",
        inventory["PSEAE"],
        False,
        external - {"L-phosphoserine"},
    )
    check(
        "ThrH can phosphorylate without ATP",
        comparator,
        "PSEAE",
        inventory["PSEAE"],
        True,
        external - {"ATP"},
    )
    check(
        "ThrH requires its homoserine acceptor",
        comparator,
        "PSEAE",
        inventory["PSEAE"],
        False,
        external - {"L-homoserine"},
    )
    check(
        "PSEAE ThrH not native PSEPK capacity",
        comparator,
        "PSEPK",
        inventory["PSEAE"],
        False,
    )
    # Check the explicit sequential links have a matching principal intermediate.
    for route in doc["module"]["variant_sets"][0]["variants"]:
        assert len(route["parts"]) == 5 and len(route["connections"]) == 4
        ordered = [
            part["node"]["id"]
            for part in sorted(route["parts"], key=lambda p: p["order"])
        ]
        assert {
            (edge["source"], edge["target"]) for edge in route["connections"]
        } == set(zip(ordered, ordered[1:]))
        for edge in route["connections"]:
            src = [
                a for n in walk(nodes[edge["source"]]) for a in n.get("annotons", [])
            ]
            dst = [
                a for n in walk(nodes[edge["target"]]) for a in n.get("annotons", [])
            ]
            for a in src:
                for b in dst:
                    assert (
                        a["function"]["products"][0]["preferred_term"]
                        == b["function"]["substrates"][0]["preferred_term"]
                    )
    # A global inventory is not a fourth native species implementation.
    check(
        "Unrepresented taxon not rescued by a cross-species inventory",
        full,
        "BACSU",
        set(species),
        False,
    )
    report = {
        "passed": len(cases),
        "cases": cases,
        "reaction_continuity_edges_checked": 12,
        "scope": "Native capacity under stated supplied-resource assumptions; not measured physiological flux.",
    }
    (DATA / "route-results.yaml").write_text(yaml.safe_dump(report, sort_keys=False))
    print(
        f"{len(cases)} native route, chain, fusion and resource cases passed; 12 continuity edges checked"
    )


if __name__ == "__main__":
    main()
