"""Check structural member requirements, not physiological sufficiency.

The production compiler represents a complex as an atom. The predicate below
requires every named active unit, so isolated CD79 or p110 cannot satisfy the
modeled assembly. Species and isoform alternatives are assessed explicitly.
"""

from pathlib import Path
import json
import yaml
from ai_gene_review.module_logic import compile_node, is_satisfied
from check_module import walk

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent


def main():
    doc = yaml.safe_load((ROOT / "modules/b_cell_receptor_signaling.yaml").read_text())
    objects = {x["id"]: x for x in walk(doc) if "id" in x}
    panel = yaml.safe_load((HERE / "members.yaml.txt").read_text())["members"]
    accession = {(m["organism"], m["gene"]): m["accession"] for m in panel}
    assert not any(x.get("selector_type") == "FAMILY" for x in walk(doc))
    results = []

    def present(selector, available):
        if selector["selector_type"] == "GENE_PRODUCT":
            return selector["gene_product"]["term"]["id"].split(":")[1] in available
        assert selector["selector_type"] == "PROTEIN_COMPLEX"
        return all(
            present(unit["participant"], available)
            for unit in selector["protein_complex"]["active_units"]
        )

    def probe(name, node, available, expected):
        circuit = compile_node(objects[node], ROOT / "modules")
        actual = is_satisfied(
            circuit,
            lambda atom: present(objects[atom.node_id]["participant"], available),
        )
        assert actual == expected, (name, actual, expected)
        results.append(
            {
                "case": name,
                "node": node,
                "available": sorted(available),
                "satisfied": actual,
            }
        )

    core_genes = ["CD79A", "CD79B", "SYK", "BLNK", "PIK3CD", "PIK3R1", "BTK", "PLCG2"]
    core = {accession["human", gene] for gene in core_genes}
    probe(
        "human core without accessory modifiers",
        "b_cell_receptor_signaling",
        core,
        True,
    )
    probe("empty context", "b_cell_receptor_signaling", set(), False)
    for gene in core_genes:
        probe(
            "missing human " + gene,
            "b_cell_receptor_signaling",
            core - {accession["human", gene]},
            False,
        )
    probe(
        "gamma cannot substitute for delta",
        "b_cell_receptor_signaling",
        (core - {accession["human", "PIK3CD"]}) | {accession["human", "PIK3CG"]},
        False,
    )
    probe(
        "mouse kinase cannot substitute for human SYK",
        "b_cell_receptor_signaling",
        (core - {accession["human", "SYK"]}) | {accession["mouse", "Syk"]},
        False,
    )
    for org in ["mouse", "CHICK"]:
        available = {m["accession"] for m in panel if m["organism"] == org}
        probe(
            org + " partial panel is not a complete human circuit",
            "b_cell_receptor_signaling",
            available,
            False,
        )
    for gene in ["CD19", "PIK3AP1", "LYN", "PIK3CG"]:
        probe(
            "human core plus " + gene,
            "b_cell_receptor_signaling",
            core | {accession["human", gene]},
            True,
        )
    probe(
        "CD79A alone is not the heterodimer",
        "human_cd79_step",
        {accession["human", "CD79A"]},
        False,
    )
    probe(
        "p110 alone is not the modeled class IA assembly",
        "human_class_ia_pi3k_step",
        {accession["human", "PIK3CD"]},
        False,
    )
    report = ROOT / ".cache/module-audit-logs/b-cell-route-cases.json"
    report.write_text(json.dumps(results, indent=2) + "\n")
    print(f"{len(results)} species, isoform and complex requirement cases PASS")


if __name__ == "__main__":
    main()
