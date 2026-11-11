"""Check the explicit nicotinic assemblies, taxa, family members and source quotes.

Run from the repository root with:
  uv run python modules/acetylcholine_signaling-source-analysis/check_receptor_assemblies.py

The generic module circuit compiler represents a complex activity as an atom;
it does not expand active_units. These checks therefore examine the explicitly
curated required subunits directly. Protein presence alone does not establish
native coexpression, assembly, localization, agonist exposure or signaling.
This is a receptor-segment check, not validation of the whole transmission chain.
"""

from pathlib import Path
import json
import re
import yaml

ROOT = Path(__file__).resolve().parents[2]
DOCUMENT = ROOT / "modules/acetylcholine_signaling.yaml"


def walk(x):
    if isinstance(x, dict):
        yield x
        for v in x.values():
            yield from walk(v)
    elif isinstance(x, list):
        for v in x:
            yield from walk(v)


def check():
    doc = yaml.safe_load(DOCUMENT.read_text())
    objects = {x["id"]: x for x in walk(doc) if "id" in x}
    human = objects["nachr_subtype"]["variants"]
    assert len(human) == 12, len(human)
    comparators = [
        objects[x] for x in ("rat_hair_cell_receptor", "chicken_hair_cell_receptor")
    ]
    all_receptors = human + comparators
    assemblies = {}
    family_checks = []
    for n in all_receptors:
        taxon = n["context"]["taxa"][0]["term"]["id"]
        a = n["annotons"][0]
        assert a["function"]["term"]["id"] == "GO:0022848"
        assert a["participant"]["selector_type"] == "PROTEIN_COMPLEX"
        units = a["participant"]["protein_complex"]["active_units"]
        counts = [str(u.get("stoichiometry", "")) for u in units]
        if all(c.isdigit() for c in counts):
            assert sum(map(int, counts)) == 5, (n["id"], counts)
        proteins = []
        for u in units:
            s = u["participant"]
            gp = s["gene_product"]
            symbol = gp["preferred_term"]
            acc = gp["term"]["id"].split(":", 1)[1]
            org = {
                "NCBITaxon:9606": "human",
                "NCBITaxon:10116": "rat",
                "NCBITaxon:9031": "CHICK",
            }[taxon]
            raw = (ROOT / f"genes/{org}/{symbol}/{symbol}-uniprot.txt").read_text()
            assert re.search(r"^AC   " + re.escape(acc) + r";", raw, re.M), (
                org,
                symbol,
                acc,
            )
            assert "NCBI_TaxID=" + taxon.split(":")[1] + ";" in raw
            assert "DR   PANTHER; PTHR18945;" in raw
            assert s["family"]["term"] == {
                "id": "PANTHER:PTHR18945",
                "label": "NEUROTRANSMITTER GATED ION CHANNEL",
            }
            assert s["family"]["representative_members"] == [gp]
            proteins.append(acc)
            family_checks.append((org, symbol, acc))
        assemblies[n["id"]] = set(proteins)
    assert assemblies["nachr_muscle_adult"] == {"P02708", "P11230", "Q07001", "Q04844"}
    assert assemblies["nachr_muscle_fetal"] == {"P02708", "P11230", "Q07001", "P07510"}
    assert len(assemblies["nachr_alpha7"]) == 1
    assert (
        objects["nachr_alpha7"]["annotons"][0]["participant"]["protein_complex"][
            "active_units"
        ][0]["stoichiometry"]
        == "5"
    )
    assert all(len(s) <= 5 for s in assemblies.values())
    cases = []

    def probe(name, available, expected):
        actual = sorted(k for k, v in assemblies.items() if v <= set(available))
        assert actual == sorted(expected), (name, actual, expected)
        cases.append(
            {"case": name, "available": sorted(available), "matched_assemblies": actual}
        )

    probe("empty", set(), [])
    probe(
        "adult muscle without fetal gamma",
        assemblies["nachr_muscle_adult"],
        ["nachr_muscle_adult"],
    )
    probe(
        "fetal muscle without adult epsilon",
        assemblies["nachr_muscle_fetal"],
        ["nachr_muscle_fetal"],
    )
    probe(
        "muscle core missing developmental subunit", {"P02708", "P11230", "Q07001"}, []
    )
    probe(
        "alpha4 beta2 allows two stoichiometries",
        {"P43681", "P17787"},
        ["nachr_alpha4beta2_2_3", "nachr_alpha4beta2_3_2"],
    )
    probe("alpha2 beta2", {"Q15822", "P17787"}, ["nachr_alpha2beta2"])
    probe(
        "alpha4 beta2 with alpha5 supports the accessory alternative",
        {"P43681", "P17787", "P30532"},
        ["nachr_alpha4beta2_2_3", "nachr_alpha4beta2_3_2", "nachr_alpha4beta2_alpha5"],
    )
    probe("alpha6 beta2 without accessory is insufficient", {"Q15825", "P17787"}, [])
    probe(
        "alpha6 beta2 beta3", {"Q15825", "P17787", "Q05901"}, ["nachr_alpha6beta2beta3"]
    )
    probe(
        "alpha3 beta4 without alpha5", {"P32297", "P30926"}, ["nachr_alpha3beta4_base"]
    )
    probe(
        "alpha3 beta4 with alpha5 supports either assembly",
        {"P32297", "P30926", "P30532"},
        ["nachr_alpha3beta4_base", "nachr_alpha3beta4_alpha5"],
    )
    probe("alpha5 beta3 accessories alone", {"P30532", "Q05901"}, [])
    probe("alpha7 homomeric capacity", {"P36544"}, ["nachr_alpha7"])
    probe("human alpha9 alpha10", {"Q9UGM1", "Q9GZZ6"}, ["nachr_alpha9alpha10"])
    probe("rat alpha9 alpha10", {"P43144", "Q9JLB5"}, ["rat_hair_cell_receptor"])
    probe(
        "chicken alpha9 alpha10", {"Q9PTS8", "Q9I8C7"}, ["chicken_hair_cell_receptor"]
    )
    probe("mixed human and rat subunits", {"Q9UGM1", "Q9JLB5"}, [])
    probe("mixed rat and chicken subunits", {"P43144", "Q9I8C7"}, [])
    for ident in ["rat_hair_cell_receptor", "chicken_hair_cell_receptor"]:
        part = next(x for x in doc["module"]["parts"] if x["node"]["id"] == ident)
        assert part["optional"] is True
    # Verify authored quotes independently, including reference findings.
    quotes = set()
    for x in walk(doc):
        ref = x.get("source_id") or x.get("reference_id")
        if ref and ref.startswith("PMID:") and x.get("supporting_text"):
            quotes.add((ref, x["supporting_text"]))
    for r in doc.get("references", []):
        for f in r.get("findings", []):
            if f.get("supporting_text"):
                quotes.add((r["id"], f["supporting_text"]))
    for ref, quote in quotes:
        source = (ROOT / f"publications/PMID_{ref.split(':')[1]}.md").read_text()
        assert " ".join(quote.split()) in " ".join(source.split()), (ref, quote)
    report = {
        "document": str(DOCUMENT.relative_to(ROOT)),
        "scope": "nicotinic receptor assemblies only; module and gene audit still in progress",
        "receptors": len(all_receptors),
        "unique_family_members_verified": len(set(family_checks)),
        "quoted_passages_verified": len(quotes),
        "cases": cases,
    }
    out = ROOT / ".cache/module-audit-logs/acetylcholine-receptor-assembly-checks.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2) + "\n")
    print(
        f"{len(cases)} receptor-assembly cases PASS; {len(set(family_checks))} exact family members; {len(quotes)} source quotes."
    )


if __name__ == "__main__":
    check()
