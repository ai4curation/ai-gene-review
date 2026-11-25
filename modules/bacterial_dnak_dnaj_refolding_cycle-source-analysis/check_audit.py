"""Bounded DnaK-cycle capacity and immutable-payload audit.

The production boolean compiler determines AND/OR/optional topology. An independent
oracle requires an exact reviewed member, the role-specific MF and family, and a
curated compatible trio. False is lack of evidence for this defined implementation,
not absence of all refolding. Assay-only controls deliberately have no accessions.
Run with --check to verify without rewriting the deterministic result artifact.
"""

from collections import Counter
from copy import deepcopy
from itertools import product
from pathlib import Path
import argparse
import hashlib
import re
import yaml
from ai_gene_review.module_logic import compile_node, is_satisfied, iter_atoms
from ai_gene_review.validation.local_source_text import quote_matches

ROOT = Path(__file__).resolve().parents[2]
SLUG = "bacterial_dnak_dnaj_refolding_cycle"
AUDIT = ROOT / "analysis/module_audits" / SLUG
ROLE_ATOMS = {
    "dnaj_atpase_activation": ("dnaj", "GO:0001671"),
    "thermus_dnaj_client_handling": ("dnaj", "GO:0044183"),
    "dnak_atp_dependent_chaperone": ("dnak", "GO:0140662"),
    "grpe_nucleotide_exchange_factor": ("grpe", "GO:0000774"),
}
REQUIRED_NODES = {
    "dnaj_client_delivery",
    "dnak_client_remodeling",
    "grpe_nucleotide_exchange",
}
IDENTITIES = {
    "P0A6Y8": ("ECOLI", "dnak"),
    "P08622": ("ECOLI", "dnaj"),
    "P09372": ("ECOLI", "grpe"),
    "Q88DU2": ("PSEPK", "dnak"),
    "Q88DU3": ("PSEPK", "dnaj"),
    "Q88DU1": ("PSEPK", "grpe"),
    "P9WMJ9": ("MYCTU", "dnak"),
    "P9WNV9": ("MYCTU", "dnaj"),
    "P9WNV7": ("MYCTU", "dnaj"),
    "P9WMT5": ("MYCTU", "grpe"),
    "Q56235": ("THET8", "dnak"),
    "Q56237": ("THET8", "dnaj"),
    "Q56236": ("THET8", "grpe"),
    "P77527": ("THET8", "dafa"),
}
TAXA = {
    "ECOLI": "NCBITaxon:83333",
    "PSEPK": "NCBITaxon:160488",
    "MYCTU": "NCBITaxon:83332",
    "THET8": "NCBITaxon:300852",
}
FAMILIES = {
    "dnak": {"PANTHER:PTHR19375", "Pfam:PF00012"},
    "dnaj": {"PANTHER:PTHR43096", "Pfam:PF00226"},
    "grpe": {"PANTHER:PTHR21237", "Pfam:PF01025"},
}
# Independent reviewed implementation identities; no family-wide compatibility grant.
TRIOS = {
    "ecoli_canonical": ("P0A6Y8", "P08622", "P09372"),
    "psepk_inferred": ("Q88DU2", "Q88DU3", "Q88DU1"),
    "myctu_j1": ("P9WMJ9", "P9WNV9", "P9WMT5"),
    "myctu_j2": ("P9WMJ9", "P9WNV7", "P9WMT5"),
    "thermus_client_handoff": ("Q56235", "Q56237", "Q56236"),
}
SUPPORT_LEVELS = {
    "CURATED_REFERENCE_IMPLEMENTATION",
    "CURATED_ORTHOLOG_INFERENCE",
    "SPECIES_ASSAY_WITH_REFERENCE_SEQUENCE_INFERENCE",
    "EXPERIMENTAL_SYSTEM_WITH_IDENTITY_BRIDGES",
}
DAFA_FUNCTION = "DnaK-DnaJ chaperone inhibitor activity"


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
        return ROOT / "publications" / ("PMID_" + ref[5:] + ".md")
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


def grounded(core):
    sources = core.get("supported_by", [])
    return bool(sources) and all(
        (p := source_path(s.get("reference_id", "")))
        and p.is_file()
        and (not s.get("supporting_text") or quote_matches(s["supporting_text"], p))
        for s in sources
    )


def verify_quotes(value, inherited=""):
    n = 0
    if isinstance(value, dict):
        ref = value.get("reference_id") or value.get("source_id") or inherited
        if str(value.get("id", "")).startswith(("PMID:", "file:")):
            ref = value["id"]
        if value.get("supporting_text"):
            p = source_path(ref)
            assert p and p.is_file() and quote_matches(value["supporting_text"], p), (
                "quote",
                ref,
                value["supporting_text"],
            )
            n += 1
        for child in value.values():
            n += verify_quotes(child, ref)
    elif isinstance(value, list):
        n += sum(verify_quotes(child, inherited) for child in value)
    return n


def load_panel():
    baseline = read(AUDIT / "seed-baseline.yaml")
    panel, hashes, additions = {}, {}, []
    counts, actions = Counter(), Counter()
    for m in baseline["members"]:
        p = ROOT / m["review_path"]
        d = read(p)
        assert d["status"] == "COMPLETE" and d["id"] == m["accession"]
        assert IDENTITIES[d["id"]][0] == m["organism"]
        assert d["taxon"]["id"] == TAXA[m["organism"]]
        rows, originals = d.get("existing_annotations", []), m["original_rows"]
        assert len(rows) >= len(originals)
        for old, new in zip(originals, rows):
            assert {k: v for k, v in old.items() if k != "review"} == {
                k: v for k, v in new.items() if k != "review"
            }, ("changed payload", p)
            if old["review"]["action"] == "NEW":
                assert new["review"]["action"] == "NEW"
                counts["inherited_NEW"] += 1
        for new in rows[len(originals) :]:
            assert new["review"]["action"] == "NEW"
            additions.append({"accession": d["id"], "row": new})
        for row in rows:
            assert row["review"]["action"] != "PENDING"
            actions[row["review"]["action"]] += 1
        raw = p.with_name(m["gene"] + "-uniprot.txt").read_text()
        families = {
            db + ":" + ident
            for db, ident in re.findall(
                r"^DR\s+(PANTHER|Pfam|InterPro|NCBIfam); ([^;]+);", raw, re.M
            )
        }
        cores = deepcopy(d.get("core_functions", []))
        for c in cores:
            c["_supported"] = grounded(c)
        panel[d["id"]] = {
            "organism": m["organism"],
            "taxon": d["taxon"]["id"],
            "role": IDENTITIES[d["id"]][1],
            "families": families,
            "cores": cores,
            "proposals": d.get("proposed_new_terms", []),
        }
        counts.update(members=1, historical_rows=len(originals), current_rows=len(rows))
        hashes[m["review_path"]] = sha(p)
    for p, h in baseline["protected_sha256"].items():
        assert sha(ROOT / p) == h, ("changed protected source", p)
        counts[
            "raw_files"
            if p.endswith(("-goa.tsv", "-uniprot.txt"))
            else "provider_prediction_files"
        ] += 1
    # Ignored pristine captures are checked when available, but not required in a fresh checkout.
    captures = []
    for p, h in baseline["source_baseline_sha256"].items():
        if (ROOT / p).exists():
            assert sha(ROOT / p) == h
            captures.append(p)
    assert counts == Counter(
        members=14,
        historical_rows=227,
        current_rows=233,
        inherited_NEW=3,
        raw_files=28,
        provider_prediction_files=15,
    ), counts
    assert set(panel) == set(IDENTITIES) and len(additions) == 6
    assert {(a["accession"], a["row"]["term"]["id"]) for a in additions} == {
        ("Q56235", "GO:0140662"),
        ("Q56237", "GO:0044183"),
        ("P77527", "GO:0051087"),
        ("P9WNV9", "GO:0001671"),
        ("P9WNV7", "GO:0001671"),
        ("P9WNV7", "GO:0008428"),
    }, additions
    return panel, counts, actions, hashes, additions, captures


def enabled(record):
    return {
        c["molecular_function"]["id"]
        for c in record["cores"]
        if c.get("_supported") and c.get("molecular_function")
    }


def compatible(w, panel):
    if (
        w.get("id") not in TRIOS
        or w.get("state") != "productive"
        or w.get("support_level") not in SUPPORT_LEVELS
    ):
        return False
    actual = tuple(w.get("roles", {}).get(r) for r in ("dnak", "dnaj", "grpe"))
    if actual != TRIOS[w["id"]]:
        return False
    expected_branch = (
        "thermus_j_client_delivery"
        if actual[1] == "Q56237"
        else "canonical_j_activation"
    )
    if w.get("j_branch") != expected_branch or not w.get("references"):
        return False
    if not all((p := source_path(r)) and p.is_file() for r in w["references"]):
        return False
    return all(
        a in panel
        and IDENTITIES.get(a) == (w["organism"], role)
        and panel[a]["role"] == role
        and panel[a]["organism"] == w["organism"]
        and panel[a]["taxon"] == TAXA[w["organism"]]
        for role, a in w["roles"].items()
    )


def chemistry_ok(annoton, role):
    f = annoton.get("function", {})
    substrates = {
        x.get("preferred_term", "").casefold() for x in f.get("substrates", [])
    }
    products = {x.get("preferred_term", "").casefold() for x in f.get("products", [])}
    phosphate = {"phosphate", "orthophosphate", "inorganic phosphate"}
    if role == "dnak":
        return "atp" in substrates and "adp" in products and bool(phosphate & products)
    if products & phosphate:
        return False
    return not (role == "dnaj" and "adp" in products)


def evaluate(doc, panel, present, witnesses, state="productive"):
    nodes = {x["id"]: x for x in walk(doc["module"]) if "id" in x}
    circuit = compile_node(doc["module"])
    if state != "productive":
        return False  # this context represents the occupied inhibitory assembly, not gene presence
    for w in witnesses:
        if not compatible(w, panel):
            continue
        if not set(w["roles"].values()) <= set(present):
            continue

        def holds(atom):
            if atom.node_id not in ROLE_ATOMS:
                if atom.node_id != "dafa_inhibitory_assembly_activity":
                    return False
                # The optional inhibitor is exact-member/NTR grounded, never granted by MerR-like family.
                d = panel.get("P77527", {})
                return (
                    "P77527" in present
                    and "P77527" in atom.uniprots
                    and not atom.family_ids
                    and any(
                        c.get("_supported")
                        and c.get("proposed_molecular_function") == DAFA_FUNCTION
                        for c in d.get("cores", [])
                    )
                )
            role, mf = ROLE_ATOMS[atom.node_id]
            if role == "dnaj" and (
                (atom.node_id == "thermus_dnaj_client_handling")
                != (w["j_branch"] == "thermus_j_client_delivery")
            ):
                return False
            a = w["roles"][role]
            record = panel[a]
            return (
                a in atom.uniprots
                and FAMILIES[role] <= record["families"]
                and set(atom.family_ids) <= record["families"]
                and mf in atom.function_ids
                and set(atom.function_ids) <= enabled(record)
                and mf in enabled(record)
                and chemistry_ok(nodes[atom.node_id], role)
            )

        if is_satisfied(circuit, holds):
            return True
    return False


def topology_cases(doc):
    """Truth table independent of family/member oracle: K AND E AND (Jcanonical OR Jthermus)."""
    circuit = compile_node(doc["module"])
    atom_ids = {a.node_id for a in iter_atoms(circuit)}
    assert atom_ids == set(ROLE_ATOMS) | {"dafa_inhibitory_assembly_activity"}, atom_ids
    required = {
        p["node"]["id"] for p in doc["module"].get("parts", []) if not p.get("optional")
    }
    assert required == REQUIRED_NODES, required
    cases = []
    for k, j, t, e, regulator in product((False, True), repeat=5):
        truth = dict(zip(ROLE_ATOMS, (j, t, k, e)))
        observed = is_satisfied(circuit, lambda a: truth.get(a.node_id, regulator))
        expected = k and e and (j or t)
        assert observed == expected, ("topology", k, j, t, e, regulator, observed)
        cases.append(
            {
                "case": f"topology K{k} J{j} T{t} E{e} DafA{regulator}",
                "expected": expected,
                "observed": observed,
            }
        )
    return cases


def documentary_cases(doc, controls):
    """Evidence-bounded assay contexts, explicitly NOT sequence-grounded capacity."""
    source = ROOT / "publications/PMID_18323638.md"
    assert quote_matches(
        "DnaK did not cooperate with the purified DnaJ and GrpE from either T. halophilus or E. coli",
        source,
    )
    assert quote_matches(
        "E. coli DnaK, however, cross-reacted with those from both bacteria.", source
    )
    expected_roles = {
        "tetragenococcus_native_tested_negative": (
            "assay:T_halophilus_DnaK",
            "assay:T_halophilus_DnaJ",
            "assay:T_halophilus_GrpE",
        ),
        "ecoli_k_tetragenococcus_cofactors_positive": (
            "assay:E_coli_DnaK",
            "assay:T_halophilus_DnaJ",
            "assay:T_halophilus_GrpE",
        ),
    }
    cases = []
    for c in controls:
        roles = tuple(c["role_identifiers"][r] for r in ("dnak", "dnaj", "grpe"))
        assert roles == expected_roles[c["id"]] and c["reference"] == "PMID:18323638"
        # Independent source result, not the control's asserted flag and not a taxon-equality rule.
        productive = roles[0] == "assay:E_coli_DnaK"
        observed = is_satisfied(
            compile_node(doc["module"]),
            lambda a: productive and a.node_id != "thermus_dnaj_client_handling",
        )
        assert observed == c["productive_observed"] == productive
        cases.append(
            {
                "case": c["id"],
                "scope": "documentary_assay_only_no_accession_prediction",
                "expected": productive,
                "observed": observed,
                "reference": c["reference"],
                "limits": c["limits"],
            }
        )
    return cases


def main(write=True):
    panel, counts, actions, hashes, additions, captures = load_panel()
    doc = read(ROOT / "modules" / (SLUG + ".yaml"))
    catalog = read(AUDIT / "compatible-cycles.yaml")
    witnesses = catalog["cycles"]
    assert {w["id"] for w in witnesses} == set(TRIOS)
    dafa_atom = next(
        a
        for a in iter_atoms(compile_node(doc["module"]))
        if a.node_id == "dafa_inhibitory_assembly_activity"
    )
    assert dafa_atom.uniprots == ("P77527",) and not dafa_atom.family_ids
    dafa_node = next(
        x
        for x in walk(doc["module"])
        if x.get("id") == "dafa_inhibitory_assembly_activity"
    )
    assert dafa_node["function"]["preferred_term"] == DAFA_FUNCTION
    quote_count = verify_quotes(doc) + verify_quotes(
        read(AUDIT / "architecture-review.yaml")
    )
    cases = topology_cases(doc)

    def check(
        name,
        expected,
        present,
        current=None,
        model=None,
        cycles=None,
        state="productive",
    ):
        result = evaluate(
            model if model is not None else doc,
            current if current is not None else panel,
            set(present),
            witnesses if cycles is None else cycles,
            state,
        )
        assert result == expected, (name, result, expected)
        cases.append({"case": name, "expected": expected, "observed": result})

    for w in witnesses:
        trio = set(w["roles"].values())
        check(w["id"] + " productive witness", True, trio, cycles=[w])
        check(w["id"] + " no compatibility witness", False, trio, cycles=[])
        unsupported = deepcopy(w)
        unsupported["references"] = []
        check(
            w["id"] + " witness has no source evidence",
            False,
            trio,
            cycles=[unsupported],
        )
        for role, acc in w["roles"].items():
            check(w["id"] + " missing " + role, False, trio - {acc}, cycles=[w])
            changed = deepcopy(panel)
            changed[acc]["cores"] = []
            check(
                w["id"] + " no reviewed core " + role,
                False,
                trio,
                current=changed,
                cycles=[w],
            )
            changed = deepcopy(panel)
            changed[acc]["families"] = set()
            check(
                w["id"] + " no family evidence " + role,
                False,
                trio,
                current=changed,
                cycles=[w],
            )
            changed = deepcopy(panel)
            changed[acc]["taxon"] = "NCBITaxon:9606"
            check(
                w["id"] + " mismatched strain/taxon " + role,
                False,
                trio,
                current=changed,
                cycles=[w],
            )
            changed = deepcopy(panel)
            changed[acc]["role"] = "wrong_paralog"
            check(
                w["id"] + " wrong paralog role " + role,
                False,
                trio,
                current=changed,
                cycles=[w],
            )
            changed = deepcopy(panel)
            for c in changed[acc]["cores"]:
                c["_supported"] = False
            check(
                w["id"] + " ungrounded core " + role,
                False,
                trio,
                current=changed,
                cycles=[w],
            )
        changed = deepcopy(panel)
        changed[w["roles"]["dnak"]]["cores"] = [
            {"molecular_function": {"id": "GO:0016887"}, "_supported": True}
        ]
        check(w["id"] + " ATPase alone", False, trio, current=changed, cycles=[w])
        changed[w["roles"]["dnak"]]["cores"] = [
            {
                "proposed_molecular_function": "holdase chaperone activity",
                "_supported": True,
            }
        ]
        check(
            w["id"] + " ATP-independent holdase alone",
            False,
            trio,
            current=changed,
            cycles=[w],
        )
        unknown = deepcopy(w)
        unknown["support_level"] = "SAME_TAXON_ONLY"
        check(
            w["id"] + " same-taxon coupling unestablished",
            False,
            trio,
            cycles=[unknown],
        )
    mtb = {"P9WMJ9", "P9WNV9", "P9WNV7", "P9WMT5"}
    check("Mtb both J proteins allowed, not required", True, mtb)
    check("Mtb neither J protein", False, mtb - {"P9WNV9", "P9WNV7"})
    changed = deepcopy(panel)
    changed["P9WNV9"]["cores"] = []
    check("Mtb inactive J1 still permits J2 witness", True, mtb, current=changed)
    thermus = {"Q56235", "Q56237", "Q56236"}
    assert "GO:0001671" not in enabled(panel["Q56237"])
    check("Thermus does not require positive GO0001671", True, thermus)
    check("DafA genomic/protein presence is not veto", True, thermus | {"P77527"})
    check(
        "Explicit DafA-occupied inhibited state is not productive",
        False,
        thermus | {"P77527"},
        state="DafA-occupied DnaK-DnaJ assembly",
    )
    check("DafA alone is no folding cycle", False, {"P77527"})
    check(
        "Unwitnessed Ecoli-DnaK/PSEPK-cofactor mosaic",
        False,
        {"P0A6Y8", "Q88DU3", "Q88DU1"},
    )
    # Claiming identical taxon does not repair missing compatibility.
    changed = deepcopy(panel)
    for a in ["Q88DU3", "Q88DU1"]:
        changed[a]["taxon"] = TAXA["ECOLI"]
        changed[a]["organism"] = "ECOLI"
    check(
        "Relabeled mosaic still lacks exact trio witness",
        False,
        {"P0A6Y8", "Q88DU3", "Q88DU1"},
        current=changed,
    )
    # Same family and role data on a non-exemplar must not acquire identity or compatibility.
    changed = deepcopy(panel)
    changed["test:unreviewed_J_paralog"] = deepcopy(panel["P08622"])
    check(
        "Arbitrary same-family J is insufficient",
        False,
        {"P0A6Y8", "test:unreviewed_J_paralog", "P09372"},
        current=changed,
    )
    for atom_id, (role, _) in ROLE_ATOMS.items():
        changed = deepcopy(doc)
        node = next(x for x in walk(changed) if x.get("id") == atom_id)
        node["function"]["term"]["id"] = (
            "GO:0016887" if role != "dnak" else "GO:0044183"
        )
        present = (
            thermus
            if atom_id == "thermus_dnaj_client_handling"
            else set(TRIOS["ecoli_canonical"])
        )
        check("Reject wrong declared MF " + atom_id, False, present, model=changed)
    for atom_id in ROLE_ATOMS:
        changed = deepcopy(doc)
        node = next(x for x in walk(changed) if x.get("id") == atom_id)
        node["participant"]["family"]["representative_members"] = []
        present = (
            thermus
            if atom_id == "thermus_dnaj_client_handling"
            else set(TRIOS["ecoli_canonical"])
        )
        check(
            "Family label alone without exact representative " + atom_id,
            False,
            present,
            model=changed,
        )
    changed = deepcopy(doc)
    node = next(
        x for x in walk(changed) if x.get("id") == "dnak_atp_dependent_chaperone"
    )
    node["function"]["substrates"] = [{"preferred_term": "non-native protein client"}]
    check(
        "DnaK folding gate without ATP chemistry",
        False,
        TRIOS["ecoli_canonical"],
        model=changed,
    )
    for atom_id in ["dnaj_atpase_activation", "grpe_nucleotide_exchange_factor"]:
        changed = deepcopy(doc)
        node = next(x for x in walk(changed) if x.get("id") == atom_id)
        node["function"].setdefault("products", []).append(
            {"preferred_term": "phosphate"}
        )
        check(
            "Reject ATP-hydrolysis chemistry on " + atom_id,
            False,
            TRIOS["ecoli_canonical"],
            model=changed,
        )
    # The test must detect weakened topology, not silently fit a broken module.
    mutations = []
    for node_id in REQUIRED_NODES:
        changed = deepcopy(doc)
        next(p for p in changed["module"]["parts"] if p["node"]["id"] == node_id)[
            "optional"
        ] = True
        missing_atoms = (
            {"dnaj_atpase_activation", "thermus_dnaj_client_handling"}
            if node_id == "dnaj_client_delivery"
            else {"dnak_atp_dependent_chaperone"}
            if node_id == "dnak_client_remodeling"
            else {"grpe_nucleotide_exchange_factor"}
        )

        def available(atom):
            return atom.node_id not in missing_atoms

        assert not is_satisfied(compile_node(doc["module"]), available)
        assert is_satisfied(compile_node(changed["module"]), available), (
            "Mutation must genuinely weaken production logic"
        )
        try:
            topology_cases(changed)
        except AssertionError:
            mutations.append(
                {
                    "mutation": "required role made optional: " + node_id,
                    "detected": True,
                }
            )
        else:
            raise AssertionError(("topology mutation escaped", node_id))
    assay_cases = documentary_cases(doc, catalog["documentary_assay_controls"])
    result = {
        "module": SLUG,
        "status": "PASS",
        "scope": "Curated compatible implementations, not genome discovery, universal necessity, or guaranteed native flux.",
        "preservation": {
            **dict(counts),
            "added_NEW_MF": len(additions),
            "payloads_unchanged": True,
            "protected_files_unchanged": True,
            "pristine_captures_rechecked_when_present": captures,
        },
        "actions": dict(actions),
        "added_rows": additions,
        "capacity_cases": cases,
        "documentary_assay_cases": assay_cases,
        "structural_mutation_checks": mutations,
        "case_counts": {
            "capacity_and_topology": len(cases),
            "documentary": len(assay_cases),
            "structural_mutations": len(mutations),
        },
        "verified_module_architecture_quotes": quote_count,
        "inputs_sha256": {
            str(p.relative_to(ROOT)): sha(p)
            for p in [
                ROOT / "modules" / (SLUG + ".yaml"),
                AUDIT / "seed-baseline.yaml",
                AUDIT / "compatible-cycles.yaml",
                AUDIT / "architecture-review.yaml",
                Path(__file__).resolve(),
            ]
        },
        "review_sha256": hashes,
        "limits": [
            "PSEPK capacity is curated ortholog inference, not a purified KT2440 assay.",
            "Mtb J1/J2 OR models basal support, not identical yield or every substrate.",
            "Thermus refolding at 30 C and sequence/strain bridges retain source-specific limits.",
            "Tetragenococcus and heterologous controls use assay role names only; neither is an accession prediction.",
            "DafA presence is optional context; explicitly occupied inhibitory assemblies cannot be productive witnesses.",
        ],
    }
    if write:
        (AUDIT / "capacity-results.yaml").write_text(
            yaml.safe_dump(result, sort_keys=False, allow_unicode=True, width=110)
        )
    print(
        yaml.safe_dump(
            {
                "status": "PASS",
                "case_counts": result["case_counts"],
                "preservation": result["preservation"],
            },
            sort_keys=False,
        )
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--check",
        action="store_true",
        help="Check without rewriting capacity-results.yaml",
    )
    main(write=not parser.parse_args().check)
