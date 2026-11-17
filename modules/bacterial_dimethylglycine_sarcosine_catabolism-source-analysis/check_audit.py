"""Check curated panel capacity, unresolved branches and frozen source payloads.

Topology is evaluated by the production module engine. The oracle independently
requires exact curated role, taxon, family architecture and live supported core.
False means insufficient evidence in this panel, not genomic absence or flux.
The historical C-83 enzyme cannot be predicted until its sequence is identified.
"""

from collections import Counter
from copy import deepcopy
import hashlib
from pathlib import Path
import re
import yaml
from ai_gene_review.module_logic import compile_node, is_satisfied, _atom_from_annoton
from ai_gene_review.validation.local_source_text import quote_matches

ROOT = Path(__file__).resolve().parents[2]
SLUG = "bacterial_dimethylglycine_sarcosine_catabolism"
AUDIT = ROOT / "analysis/module_audits" / SLUG
IDENTITIES = {
    "PSEPK": {
        "Q88R24": "DgcA",
        "Q88R23": "DgcB",
        "Q88R22": "EtfA",
        "Q88R21": "EtfB",
        "Q88R09": "SoxA",
        "Q88R11": "SoxB",
        "Q88R10": "SoxD",
        "Q88R08": "SoxG",
    },
    "CHRI1": {
        "Q1QYW1": "DgcA",
        "Q1QYW0": "DgcB",
        "Q1QYV9": "EtfA",
        "Q1QYV8": "EtfB",
        "Q1QYV1": "SoxA",
        "Q1QYV3": "SoxB",
        "Q1QYV2": "SoxD",
        "Q1QYV0": "SoxG",
    },
    "CORS9": {"Q50LF0": "SoxA", "Q50LF2": "SoxB", "Q50LF1": "SoxD", "Q50LE9": "SoxG"},
    "ARTST": {"P40873": "MSOX"},
    "ARTGO": {"Q9AGP8": "DMGO"},
}
TAXA = {
    "PSEPK": "NCBITaxon:160488",
    "CHRI1": "NCBITaxon:290398",
    "CORS9": "NCBITaxon:31944",
    "ARTST": "NCBITaxon:68999",
    "ARTGO": "NCBITaxon:1665",
}
ROLES = {
    "dgca_dehydrogenase_activity": "DgcA",
    "dgcb_ferredoxin_activity": "DgcB",
    "dimethylglycine_catabolism_etf_alpha": "EtfA",
    "dimethylglycine_catabolism_etf_beta": "EtfB",
    "soxa_subunit": "SoxA",
    "soxb_subunit": "SoxB",
    "soxd_subunit": "SoxD",
    "soxg_subunit": "SoxG",
    "monomeric_sarcosine_oxidase_activity": "MSOX",
    "dmgo_dimethylglycine_oxidase_activity": "DMGO",
}
FAMILIES = {
    "DgcA": {"PANTHER:PTHR43656", "Pfam:PF07992"},
    "DgcB": {"PANTHER:PTHR43255", "InterPro:IPR021872"},
    "EtfA": {"PANTHER:PTHR43153"},
    "EtfB": {"PANTHER:PTHR21294"},
    "SoxA": {"NCBIfam:TIGR01372"},
    "SoxB": {"NCBIfam:TIGR01373"},
    "SoxD": {"NCBIfam:TIGR01374"},
    "SoxG": {"NCBIfam:TIGR01375"},
    "MSOX": {"PANTHER:PTHR10961:SF7"},
    "DMGO": {"PANTHER:PTHR43757:SF11"},
}
DMGO_PROPOSAL = "tetrahydrofolate-coupled dimethylglycine oxidase activity"


def read(path):
    return yaml.safe_load(path.read_text())


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


def source_path(ref):
    if ref.startswith("PMID:"):
        return ROOT / "publications" / ("PMID_" + ref.split(":")[1] + ".md")
    if ref.startswith("file:"):
        return next(
            (
                base / ref[5:]
                for base in (ROOT / "genes", ROOT)
                if (base / ref[5:]).is_file()
            ),
            None,
        )
    return None


def verify_quotes(value, inherited=None):
    count = 0
    if isinstance(value, dict):
        ref = value.get("reference_id") or value.get("source_id") or inherited
        if str(value.get("id", "")).startswith(("PMID:", "file:")):
            ref = value["id"]
        if value.get("supporting_text"):
            path = source_path(ref or "")
            assert path and path.is_file(), ("missing quoted source", ref)
            assert quote_matches(value["supporting_text"], path), (
                ref,
                value["supporting_text"],
            )
            count += 1
        for child in value.values():
            count += verify_quotes(child, ref)
    elif isinstance(value, list):
        count += sum(verify_quotes(child, inherited) for child in value)
    return count


def load_panel():
    base = read(AUDIT / "seed-baseline.yaml")
    counts, actions, panel, hashes = Counter(), Counter(), {}, {}
    for m in base["members"]:
        p = ROOT / m["review_path"]
        d = read(p)
        rows = d.get("existing_annotations", [])
        assert d["status"] == "COMPLETE" and d["id"] == m["accession"]
        assert d["taxon"]["id"] == m["taxon_id"] and len(rows) == len(m["annotations"])
        for original, row in zip(m["annotations"], rows):
            assert {k: v for k, v in row.items() if k != "review"} == original[
                "payload"
            ], p
            if original["prior_action"] == "NEW":
                assert row["review"]["action"] == "NEW"
                counts["inherited_NEW"] += 1
            assert row["review"]["action"] != "PENDING"
            actions[row["review"]["action"]] += 1
        raw = p.with_name(m["gene"] + "-uniprot.txt").read_text()
        families = {
            db + ":" + ident
            for db, ident in re.findall(
                r"^DR\s+(PANTHER|Pfam|NCBIfam|InterPro); ([^;]+);", raw, re.M
            )
        }
        cores = deepcopy(d.get("core_functions", []))
        for core in cores:
            core["_supported"] = any(
                (sp := source_path(x.get("reference_id", ""))) and sp.is_file()
                for x in core.get("supported_by", [])
            )
        panel[d["id"]] = {
            "organism": m["organism"],
            "taxon": m["taxon_id"],
            "cores": cores,
            "families": families,
            "proposals": d.get("proposed_new_terms", []),
        }
        counts.update(
            complete_reviews=1, historical_rows=len(rows), current_rows=len(rows)
        )
        hashes[m["review_path"]] = sha(p)
    for p, digest in base["protected_sha256"].items():
        assert sha(ROOT / p) == digest, p
        counts["provider_files" if "-deep-research" in p else "raw_files"] += 1
    for p, digest in base["protected_family_source_sha256"].items():
        assert sha(ROOT / p) == digest, p
    assert counts == Counter(
        complete_reviews=22,
        historical_rows=96,
        current_rows=96,
        inherited_NEW=28,
        provider_files=6,
        raw_files=44,
    ), counts
    assert set(panel) == {a for ids in IDENTITIES.values() for a in ids}
    return panel, counts, actions, hashes


def core_support(record, role):
    cores = [c for c in record["cores"] if c.get("_supported")]
    enabled = {
        c["molecular_function"]["id"] for c in cores if c.get("molecular_function")
    }
    contributes = {
        c["contributes_to_molecular_function"]["id"]
        for c in cores
        if c.get("contributes_to_molecular_function")
    }
    if role in {"DgcA", "DgcB", "MSOX"}:
        return {"DgcA": "GO:0016645", "DgcB": "GO:0009055", "MSOX": "GO:0008115"}[
            role
        ] in enabled
    if role.startswith("Etf"):
        return "GO:0009055" in contributes
    if role.startswith("Sox"):
        return "GO:0016647" in contributes
    if role == "DMGO":
        return any(
            c.get("proposed_molecular_function") == DMGO_PROPOSAL for c in cores
        ) and any(
            p["proposed_name"] == DMGO_PROPOSAL and p.get("supported_by")
            for p in record["proposals"]
        )
    return False


# Independent chemical signatures from the primary reaction evidence. Generic GO
# ancestry and correct protein identity cannot excuse a different net reaction.
CHEMISTRY = {
    "dgca_dehydrogenase_activity": (
        {
            "N,N-dimethylglycine",
            "water",
            "oxidized electron acceptor (physiological identity unresolved)",
        },
        {
            "sarcosine",
            "formaldehyde",
            "reduced electron acceptor (physiological identity unresolved)",
        },
        "GO:0016645",
    ),
    "dmgo_dimethylglycine_oxidase_activity": (
        {"N,N-dimethylglycine", "tetrahydrofolate", "oxygen"},
        {"sarcosine", "5,10-methylenetetrahydrofolate", "hydrogen peroxide"},
        None,
    ),
    "soxabdg_complex_activity": (
        {"sarcosine", "tetrahydrofolate", "oxygen"},
        {"glycine", "5,10-methylenetetrahydrofolate", "hydrogen peroxide"},
        None,
    ),
    "monomeric_sarcosine_oxidase_activity": (
        {"sarcosine", "oxygen", "water"},
        {"glycine", "formaldehyde", "hydrogen peroxide"},
        "GO:0008115",
    ),
}


def chemistry_supported(node):
    expected = CHEMISTRY.get(node["id"])
    if not expected:
        return True
    function = node.get("function", {})
    return (
        {x.get("preferred_term") for x in function.get("substrates", [])} == expected[0]
        and {x.get("preferred_term") for x in function.get("products", [])}
        == expected[1]
        and function.get("term", {}).get("id") == expected[2]
    )


def declared_functions_supported(atom, record, role):
    enabled = {
        c["molecular_function"]["id"]
        for c in record["cores"]
        if c.get("_supported") and c.get("molecular_function")
    }
    contributions = {
        c["contributes_to_molecular_function"]["id"]
        for c in record["cores"]
        if c.get("_supported") and c.get("contributes_to_molecular_function")
    }
    supported = enabled | contributions if role.startswith(("Sox", "Etf")) else enabled
    return set(atom.function_ids) <= supported


def evaluate(doc, panel, context, target, present=None):
    nodes = {x["id"]: x for x in walk(doc["module"]) if "id" in x}
    present = set(IDENTITIES[context]) if present is None else set(present)
    taxon = TAXA[context]

    def match(atom):
        if atom.node_id == "sequence_unplaced_sarcosine_dehydrogenase_activity":
            return False  # no defensible sequence-to-biochemical-role bridge
        role = ROLES[atom.node_id]
        return any(
            a in atom.uniprots
            and a in IDENTITIES[context]
            and IDENTITIES[context][a] == role
            and panel[a]["organism"] == context
            and panel[a]["taxon"] == taxon
            and FAMILIES[role] <= panel[a]["families"]
            and set(atom.family_ids) <= panel[a]["families"]
            and core_support(panel[a], role)
            and declared_functions_supported(atom, panel[a], role)
            for a in present
        )

    def predicate(atom):
        node = nodes[atom.node_id]
        if not chemistry_supported(node):
            return False
        complex_ = node.get("participant", {}).get("protein_complex")
        if complex_:
            return bool(complex_.get("active_units")) and all(
                match(_atom_from_annoton(unit)) for unit in complex_["active_units"]
            )
        return match(atom)

    node = nodes[target]
    if "participant" in node:
        node = {"id": target + "_probe", "annotons": [node]}
    return is_satisfied(compile_node(node), predicate)


def main():
    panel, counts, actions, hashes = load_panel()
    doc = read(ROOT / "modules" / (SLUG + ".yaml"))
    quote_count = verify_quotes(doc)
    cases = []

    def check(
        name, expected, context, target=SLUG, current=None, model=None, present=None
    ):
        observed = evaluate(model or doc, current or panel, context, target, present)
        assert observed == expected, (name, observed, expected)
        cases.append({"case": name, "expected": expected, "observed": observed})

    for org in IDENTITIES:
        check(org + " full panel", org in {"PSEPK", "CHRI1"}, org)
        check(
            org + " first step",
            org in {"PSEPK", "CHRI1", "ARTGO"},
            org,
            "dimethylglycine_to_sarcosine",
        )
        check(org + " second step", org != "ARTGO", org, "sarcosine_to_glycine")
        check(
            org + " unplaced historical branch cannot be predicted",
            False,
            org,
            "sequence_unplaced_sarcosine_dehydrogenase_variant",
        )
        target = (
            SLUG
            if org in {"PSEPK", "CHRI1"}
            else (
                "dimethylglycine_to_sarcosine"
                if org == "ARTGO"
                else "sarcosine_to_glycine"
            )
        )
        for a in IDENTITIES[org]:
            check(
                org + " remove " + a,
                False,
                org,
                target,
                present=set(IDENTITIES[org]) - {a},
            )
            changed = deepcopy(panel)
            changed[a]["cores"] = []
            check(org + " remove live core " + a, False, org, target, current=changed)
            changed = deepcopy(panel)
            changed[a]["families"] = set()
            check(
                org + " remove family evidence " + a,
                False,
                org,
                target,
                current=changed,
            )
            changed = deepcopy(panel)
            changed[a]["taxon"] = "NCBITaxon:9606"
            check(org + " reject wrong taxon " + a, False, org, target, current=changed)
    # A beta active site, generic oxidoreductase, or false representative cannot replace a complex.
    check(
        "CORS9 SoxB alone", False, "CORS9", "sarcosine_to_glycine", present={"Q50LF2"}
    )
    changed = deepcopy(panel)
    for c in changed["Q50LF2"]["cores"]:
        c.pop("contributes_to_molecular_function", None)
    check(
        "SoxB cofactor binding alone is insufficient",
        False,
        "CORS9",
        "sarcosine_to_glycine",
        current=changed,
    )
    changed = deepcopy(panel)
    changed["Q9AGP8"]["proposals"] = []
    check(
        "DMGO folate-free GO alone does not prove THF-coupled route",
        False,
        "ARTGO",
        "dimethylglycine_to_sarcosine",
        current=changed,
    )
    changed = deepcopy(doc)
    for x in walk(changed):
        if x.get("id") == "soxa_subunit":
            x["participant"]["family"]["representative_members"] = [
                {
                    "term": {
                        "id": "UniProtKB:Q50LF2",
                        "label": "Sarcosine oxidase subunit beta",
                    }
                }
            ]
    check(
        "Wrong alpha exemplar cannot be rescued by beta site",
        False,
        "CORS9",
        "sarcosine_to_glycine",
        model=changed,
    )
    check(
        "Cross-species pooling does not prove an ARTGO native complete route",
        False,
        "ARTGO",
        present=set(panel),
    )
    for node_id, org, target in [
        ("dgca_dehydrogenase_activity", "PSEPK", "dimethylglycine_to_sarcosine"),
        (
            "dmgo_dimethylglycine_oxidase_activity",
            "ARTGO",
            "dimethylglycine_to_sarcosine",
        ),
        ("soxabdg_complex_activity", "CORS9", "sarcosine_to_glycine"),
        ("monomeric_sarcosine_oxidase_activity", "ARTST", "sarcosine_to_glycine"),
    ]:
        for field in ["substrates", "products"]:
            changed = deepcopy(doc)
            node = next(x for x in walk(changed) if x.get("id") == node_id)
            node["function"][field] = [{"preferred_term": "unrelated chemical"}]
            check(
                node_id + " reject changed " + field, False, org, target, model=changed
            )
        changed = deepcopy(doc)
        node = next(x for x in walk(changed) if x.get("id") == node_id)
        node["function"]["term"] = {"id": "GO:0005524", "label": "ATP binding"}
        check(node_id + " reject unrelated MF", False, org, target, model=changed)
    out = {
        "status": "PASS",
        "case_count": len(cases),
        "cases": cases,
        "counts": dict(counts),
        "actions": dict(actions),
        "module_quote_checks": quote_count,
        "review_sha256": hashes,
        "module_sha256": sha(ROOT / "modules" / (SLUG + ".yaml")),
        "limits": [
            "Panel capacity is not native flux or exhaustive genome coverage.",
            "C-83 historical SDH has no gene/family mapping and is never predicted from generic MF.",
            "No cross-species pooling establishes a native ARTGO downstream route.",
            "Artificial dye turnover does not prove physiological acceptor identity.",
        ],
    }
    (AUDIT / "capacity-results.yaml").write_text(
        yaml.safe_dump(out, sort_keys=False, width=100)
    )
    print(
        f"PASS: {len(cases)} capacity cases; {quote_count} module quotes; {dict(counts)}"
    )


if __name__ == "__main__":
    main()
