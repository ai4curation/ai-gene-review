"""Check the scoped DsbAB mechanism against curated evidence and frozen seeds.

The production compiler tests required/alternative topology. Exact, independently
curated pair witnesses add partner compatibility; false means unsupported by this
audit, not impossible chemistry. This is not a whole-genome pathway predictor.
"""

from pathlib import Path
from copy import deepcopy
from itertools import product
import argparse
import hashlib
import json
import yaml
from ai_gene_review.module_logic import compile_node, is_satisfied, iter_atoms
from ai_gene_review.validation.local_source_text import quote_matches

ROOT = Path(__file__).resolve().parents[2]
SLUG = "bacterial_dsbab_oxidative_folding"
AUDIT = ROOT / "analysis/module_audits" / SLUG
# Independent expected role, family and activity assignments from source review.
LEAVES = {
    "dsbb_oxidative_folding_component": (
        "B",
        "PANTHER:PTHR36570:SF3",
        "GO:0016672",
        {"P59345", "P59344"},
    ),
    "ecoli_dsbb_oxidative_folding_component": (
        "B",
        "PANTHER:PTHR36570:SF2",
        "GO:0016672",
        {"P0A6M2"},
    ),
    "pa14_dsbb1": ("B", "PANTHER:PTHR36570:SF2", "GO:0016672", {"Q02TM7"}),
    "pa14_dsbb2": ("B", "PANTHER:PTHR36570:SF3", "GO:0016672", {"Q02EA7"}),
    "bacillus_bdbc": ("B", "PANTHER:PTHR43469:SF1", "GO:0015035", {"O32217"}),
    "campylobacter_dsbb": ("B", None, "GO:0015035", {"A8FLS4"}),
    "dsba_disulfide_oxidoreductase": (
        "A",
        "PANTHER:PTHR35891:SF2",
        "GO:0015035",
        {"P0AEG4", "Q88RK2", "Q02DM0"},
    ),
    "bacillus_bdbd": ("A", "PANTHER:PTHR13887:SF14", "GO:0015035", {"O32218"}),
    "campylobacter_dsba": (
        "A",
        "PANTHER:PTHR35891:SF3",
        "GO:0015035",
        {"A0A1J6PBD5", "A0A1J6UFJ6"},
    ),
    "pa14_dsba2_comparator": (
        "COMPARATOR",
        "PANTHER:PTHR13887:SF56",
        "GO:0015035",
        {"A0A0H2ZG77"},
    ),
}
PAIRS = {
    ("P0AEG4", "P0A6M2"),
    ("Q88RK2", "P59345"),
    ("Q88RK2", "P59344"),
    ("Q02DM0", "Q02TM7"),
    ("Q02DM0", "Q02EA7"),
    ("O32218", "O32217"),
    ("A0A1J6PBD5", "A8FLS4"),
    ("A0A1J6UFJ6", "A8FLS4"),
}


def read(path):
    return yaml.safe_load(path.read_text())


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def walk(x):
    if isinstance(x, dict):
        yield x
        for v in x.values():
            yield from walk(v)
    elif isinstance(x, list):
        for v in x:
            yield from walk(v)


def source(ref):
    if ref.startswith("PMID:"):
        return ROOT / "publications" / ("PMID_" + ref[5:] + ".md")
    if ref.startswith("file:"):
        return next(
            (p / ref[5:] for p in [ROOT / "genes", ROOT] if (p / ref[5:]).is_file()),
            None,
        )
    return None


def quotes(x, inherited=""):
    count = 0
    if isinstance(x, dict):
        ref = x.get("reference_id") or x.get("source_id") or inherited
        if str(x.get("id", "")).startswith(("PMID:", "file:")):
            ref = x["id"]
        if x.get("supporting_text"):
            path = source(ref)
            assert (
                path and path.is_file() and quote_matches(x["supporting_text"], path)
            ), ("quote", ref, x["supporting_text"])
            count += 1
        count += sum(quotes(v, ref) for v in x.values())
    elif isinstance(x, list):
        count += sum(quotes(v, inherited) for v in x)
    return count


def panel():
    seeds = read(AUDIT / "seed-baseline.yaml")
    docs, original, current, added, inherited = {}, 0, 0, [], 0
    for m in seeds["members"]:
        d = read(ROOT / m["review_path"])
        assert (
            d["status"] == "COMPLETE"
            and d["id"] == m["accession"]
            and d["taxon"] == m["taxon"]
        )
        old, new = m["original_rows"], d.get("existing_annotations", [])
        assert len(new) >= len(old)
        for a, b in zip(old, new):
            assert {k: v for k, v in a.items() if k != "review"} == {
                k: v for k, v in b.items() if k != "review"
            }, m["review_path"]
            if a["review"]["action"] == "NEW":
                assert b["review"]["action"] == "NEW"
                inherited += 1
        for row in new[len(old) :]:
            assert row["review"]["action"] == "NEW"
            added.append({"accession": d["id"], "term": row["term"]["id"]})
        assert all(r["review"]["action"] != "PENDING" for r in new)
        original += len(old)
        current += len(new)
        docs[d["id"]] = d
    for p, h in seeds["protected_raw_sha256"].items():
        assert digest(ROOT / p) == h, p
    assert (
        len(docs) == 14
        and original == 78
        and current == 92
        and len(added) == 14
        and inherited == 2
    )
    archive = (
        ROOT / "genes/CAMJ8/dsbB/dsbB-source-analysis/A8FLS4-unisave-v50-uniprot.txt"
    )
    assert (
        digest(archive)
        == "ca6094e8a57bc78de2c90284127aabd15cf07066e31097a5ed00d9e57a124d20"
    )
    assert (ROOT / "genes/CAMJ8/dsbB/dsbB-uniprot.txt").read_bytes() == b""
    return docs, {
        "members": 14,
        "original_rows": original,
        "current_rows": current,
        "inherited_NEW": inherited,
        "additions": added,
        "raw_files_unchanged": 28,
        "explicit_archive_unchanged": True,
    }


def structure(doc, docs):
    root = doc["module"]
    parts = root["parts"]
    assert {p["node"]["id"] for p in parts if not p.get("optional")} == {
        "dsbb_dsbA_reoxidation",
        "dsba_substrate_oxidation",
    }
    assert next(p for p in parts if p["node"]["id"] == "pa14_dsba2_context")["optional"]
    assert {
        (c["source"], c["target"], c["connection_type"]) for c in root["connections"]
    } == {
        ("dsbb_dsbA_reoxidation", "dsba_substrate_oxidation", "PROVIDES_INPUT_FOR"),
        ("dsba_substrate_oxidation", "dsbb_dsbA_reoxidation", "PROVIDES_INPUT_FOR"),
    }
    assert all(c.get("evidence") for c in root["connections"])
    leaves = {n["id"]: n for n in walk(root) if n.get("id") in LEAVES}
    assert set(leaves) == set(LEAVES)
    for i, (role, family, mf, members) in LEAVES.items():
        a = leaves[i]
        assert a["function"]["term"]["id"] == mf and a.get("evidence"), i
        f = a["participant"]["family"]
        assert f.get("term", {}).get("id") == family, i
        assert {
            r["term"]["id"].removeprefix("UniProtKB:")
            for r in f["representative_members"]
        } == members, i
        for accession in members:
            cores = [
                c
                for c in docs[accession]["core_functions"]
                if c.get("molecular_function", {}).get("id") == mf
            ]
            assert cores and any(c.get("supported_by") for c in cores), (accession, mf)
        if role == "B":
            assert {x["term"]["id"] for x in a["locations"]} == {"GO:0005886"}
        if i == "bacillus_bdbd":
            assert {x["term"]["id"] for x in a["locations"]} == {"GO:0005886"}
        if i == "pa14_dsba2_comparator":
            assert not a.get("processes") and not a.get("locations")
        substances = {
            x["preferred_term"].lower()
            for field in ["substrates", "products"]
            for x in a["function"].get(field, [])
        }
        assert "oxygen" not in substances
        if mf == "GO:0016672":
            assert {"quinone", "quinol"} <= substances
        if i in {"bacillus_bdbc", "campylobacter_dsbb"}:
            assert not substances & {"quinone", "quinol", "menaquinone", "ubiquinone"}
    circuit = compile_node(root)
    assert {a.node_id for a in iter_atoms(circuit)} == set(LEAVES)
    return circuit


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    doc = read(ROOT / "modules" / (SLUG + ".yaml"))
    docs, preservation = panel()
    circuit = structure(doc, docs)
    witnesses = read(AUDIT / "compatible-pairs.yaml")
    assert {
        (p["substrate_oxidase"], p["membrane_relay"]) for p in witnesses["pairs"]
    } == PAIRS
    assert all(
        p.get("supported_by") and p.get("support_level") for p in witnesses["pairs"]
    )
    cases = []

    def evaluate(name, present, expected):
        topology = is_satisfied(circuit, lambda a: bool(set(a.uniprots) & present))
        expected_topology = bool((a_set - {"A0A0H2ZG77"}) & present) and bool(
            b_set & present
        )
        assert topology == expected_topology, (
            "topology",
            name,
            topology,
            expected_topology,
        )
        compatible = any({a, b} <= present for a, b in PAIRS)
        actual = topology and compatible
        assert actual == expected, (name, actual, expected)
        cases.append(
            {
                "case": name,
                "present": sorted(present),
                "topology": topology,
                "compatible_pair": compatible,
                "supported_capacity": actual,
            }
        )

    a_set = {
        m
        for role, _, _, members in LEAVES.values()
        if role in {"A", "COMPARATOR"}
        for m in members
    }
    b_set = {
        m for role, _, _, members in LEAVES.values() if role == "B" for m in members
    }
    for a, b in sorted(product(a_set, b_set)):
        evaluate(f"pair:{a}:{b}", {a, b}, (a, b) in PAIRS)
    for a, b in sorted(PAIRS):
        evaluate(f"no-relay:{a}:{b}", {a}, False)
        evaluate(f"no-oxidase:{a}:{b}", {b}, False)
    evaluate("all-reviewed-members", a_set | b_set, True)
    evaluate("no-dsbb-relays", a_set, False)
    evaluate("no-substrate-oxidases", b_set, False)
    evaluate("VKOR-plus-dsba-does-not-supply-dsbb", {"P0AEG4", "O33272"}, False)
    evaluate("PA14-both-relays-with-A1", {"Q02DM0", "Q02TM7", "Q02EA7"}, True)
    evaluate(
        "PA14-A2-with-both-relays-is-biochemical-comparator",
        {"A0A0H2ZG77", "Q02TM7", "Q02EA7"},
        False,
    )
    mutations = []
    for name in [
        "make-recycling-optional",
        "make-A2-required",
        "invent-Campylobacter-PANTHER",
        "give-Bacillus-Gram-negative-periplasm",
    ]:
        altered = deepcopy(doc)
        if name == "make-recycling-optional":
            altered["module"]["parts"][0]["optional"] = True
        elif name == "make-A2-required":
            altered["module"]["parts"][2]["optional"] = False
        else:
            target = next(
                n
                for n in walk(altered)
                if n.get("id")
                == (
                    "campylobacter_dsbb"
                    if name.startswith("invent")
                    else "bacillus_bdbd"
                )
            )
            if name.startswith("invent"):
                target["participant"]["family"]["term"] = {
                    "id": "PANTHER:PTHR36570:SF2"
                }
            else:
                target["locations"] = [{"term": {"id": "GO:0030288"}}]
        try:
            structure(altered, docs)
        except AssertionError:
            mutations.append({"case": name, "rejected": True})
        else:
            raise AssertionError(("mutation accepted", name))
    result = {
        "scope": "Scoped representative capacity plus exact partner evidence; false does not assert biological incompatibility.",
        "module_sha256": digest(ROOT / "modules" / (SLUG + ".yaml")),
        "preservation": preservation,
        "quotes_checked": quotes(doc) + quotes(witnesses),
        "capacity_cases": cases,
        "structural_mutations": mutations,
        "case_count": len(cases) + len(mutations),
    }
    out = AUDIT / "capacity-results.yaml"
    if args.check:
        assert read(out) == result, (
            "Recorded results differ; inspect the scientific change before updating."
        )
    else:
        out.write_text(yaml.safe_dump(result, sort_keys=False, width=100))
    print(
        json.dumps(
            {
                "cases": result["case_count"],
                "quotes": result["quotes_checked"],
                "preservation": preservation,
            }
        )
    )


if __name__ == "__main__":
    main()
