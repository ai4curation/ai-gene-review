#!/usr/bin/env python3
"""Reproduce ELP2 database joins offline, without extracting archive members."""
import argparse
import csv
import hashlib
import io
import json
from pathlib import Path, PurePosixPath
import re
import stat
import xml.etree.ElementTree as ET
import zipfile


def require(value, message):
    if not value:
        raise ValueError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def encoded(value):
    return (json.dumps(value, indent=2, ensure_ascii=False) + "\n").encode()


def read_inputs(root):
    config = json.loads((root / "config.json").read_text())
    inventory = json.loads((root / "inputs.json").read_text())
    archive_name = config["archive"]
    require(Path(archive_name).name == archive_name, "archive must be a local basename")
    archive = (root / archive_name).read_bytes()
    require(digest(archive) == config["archive_sha256"], "archive hash mismatch")
    members = inventory["members"]
    expected = {x["member"]: x for x in members}
    require(len(expected) == len(members), "duplicate input-manifest member")
    data = {}
    with zipfile.ZipFile(io.BytesIO(archive)) as bundle:
        infos = bundle.infolist()
        require(len(infos) == len({x.filename for x in infos}), "duplicate archive member")
        require({x.filename for x in infos} == set(expected), "archive membership mismatch")
        require(sum(x.file_size for x in infos) <= 16 * 1024 * 1024, "oversize archive")
        for item in infos:
            path = PurePosixPath(item.filename)
            require(not path.is_absolute() and all(x not in ("", ".", "..") for x in item.filename.split("/")), "unsafe member path")
            require("\\" not in item.filename and ":" not in item.filename, "unsafe member name")
            mode = item.external_attr >> 16
            require(stat.S_ISREG(mode) and not item.is_dir(), "non-regular archive member")
            require(not item.flag_bits & 1, "encrypted archive member")
            raw = bundle.read(item)
            pin = expected[item.filename]
            require(mode == pin["mode"] and len(raw) == pin["bytes"] and digest(raw) == pin["sha256"], "input integrity mismatch: " + item.filename)
            data[item.filename] = raw
    return data


def project(data):
    get = lambda name: json.loads(data[name])
    sources = get("source/source-objects.json")
    goa = list(csv.DictReader(io.StringIO(data["source/ELP2-goa.tsv"].decode()), delimiter="\t"))
    def source_key(row):
        return (row["term"]["id"], row["evidence_type"], row["original_reference_id"], row.get("qualifier", ""), tuple(sorted(row.get("supporting_entities", []))))
    def goa_key(row):
        return (row["GO TERM"], row["GO EVIDENCE CODE"], row["REFERENCE"], row["QUALIFIER"], tuple(sorted(filter(None, row["WITH/FROM"].split("|")))))
    joins = []
    for i, source in enumerate(sources):
        hits = [j for j, row in enumerate(goa) if source_key(source) == goa_key(row)]
        require(hits, "source lacks literal GOA context")
        joins.append({"source_index": i, "goa_data_indices": hits})
    require(sorted(j for x in joins for j in x["goa_data_indices"]) == list(range(len(goa))), "GOA context coverage")

    official = get("official/UniProt-Q6IA86.json")
    sequence = official["sequence"]["value"]
    products = next(c["isoforms"] for c in official["comments"] if c["commentType"] == "ALTERNATIVE PRODUCTS")
    features = {x["featureId"]: x for x in official["features"] if x["type"] == "Alternative sequence"}
    product_checks = []
    for product in products:
        product_id = product["isoformIds"][0]
        reconstructed = sequence
        edits = [features[k] for k in product.get("sequenceIds", [])]
        for edit in sorted(edits, key=lambda x: x["location"]["start"]["value"], reverse=True):
            start, end = edit["location"]["start"]["value"] - 1, edit["location"]["end"]["value"]
            alternate = edit.get("alternativeSequence", {})
            if "originalSequence" in alternate:
                require(sequence[start:end] == alternate["originalSequence"], "VSP original sequence mismatch")
            replacement = alternate.get("alternativeSequences", [""])
            require(len(replacement) == 1, "ambiguous VSP replacement")
            reconstructed = reconstructed[:start] + replacement[0] + reconstructed[end:]
        fasta = data["official/" + product_id + ".fasta"].decode().splitlines()
        require(len([x for x in fasta if x.startswith(">")]) == 1, "FASTA cardinality")
        actual = "".join(x.strip() for x in fasta if not x.startswith(">"))
        require(actual == reconstructed, "product reconstruction mismatch: " + product_id)
        product_checks.append({"id": product_id, "length": len(actual), "sequence_sha256": digest(actual.encode()), "sequence_ids": product.get("sequenceIds", [])})

    tree = get("database/PTHR44111-treeinfo.json")["search"]["tree_topology"]["annotation_node"]
    nodes, paths = {}, {}
    def walk(node, path):
        key = node["persistent_id"]
        require(key not in nodes, "duplicate phylogenetic node")
        nodes[key], paths[key] = node, path + [key]
        children = node.get("children", {}).get("annotation_node", [])
        for child in [children] if isinstance(children, dict) else children:
            walk(child, path + [key])
    walk(tree, [])
    msa = get("database/PTHR44111-familymsa.json")["search"]["MSA_list"]["sequence_info"]
    sequence_checks = []
    for accession in ("Q6IA86", "Q7K4B3", "P42935"):
        leaves = [k for k, node in nodes.items() if node.get("node_name", "").endswith("UniProtKB=" + accession)]
        require(len(leaves) == 1, "unique accession leaf")
        leaf = leaves[0]
        hits = [x for x in msa if x["persistent_id"] == leaf]
        require(len(hits) == 1, "unique MSA sequence")
        aligned = re.sub("[^A-Za-z]", "", hits[0]["sequence"]).upper()
        require(aligned == get("official/UniProt-" + accession + ".json")["sequence"]["value"], "MSA/official sequence mismatch")
        sequence_checks.append({"accession": accession, "node": leaf, "length": len(aligned), "sequence_sha256": digest(aligned.encode())})
    human = sequence_checks[0]["node"]
    ibd = [x.split("\t") for x in data["database/target-path-IBD.gaf"].decode().splitlines() if x and not x.startswith("!")]
    require(all(x[1] in paths[human] for x in ibd), "IBD subset outside human path")
    literal = [x for x in ibd if x[1] == "PTN000521836" and x[4] == "GO:0033588" and x[6] == "IBD"]
    require(len(literal) == 1, "unique operative IBD")
    require(set(literal[0][7].split("|")) == set(sources[16]["supporting_entities"]) - {"PANTHER:PTN000521836"}, "literal IBD donor mismatch")
    donor_annotations = {}
    for accession in ("Q91WG4", "Q7K4B3", "P42935"):
        result = get("database/QuickGO-" + accession + ".json")
        require(result["pageInfo"]["total"] == 1 and result["numberOfHits"] == len(result["results"]), "incomplete captured donor query")
        donor_annotations[accession] = {"captured_total": result["numberOfHits"], "operative_records": [x for x in result["results"] if x["goId"] in ("GO:0033588", "GO:0019901")]}

    terms = {x["id"]: {"name": x["name"], "definition": x["definition"]["text"], "isObsolete": x["isObsolete"]} for x in get("database/GO-terms.json")["results"]}
    require(set(terms) == {x["term"]["id"] for x in sources}, "source term coverage")
    ancestry = {}
    for term in sorted(terms):
        response = get("database/" + term.replace(":", "") + "-ancestors.json")["results"]
        require(len(response) == 1 and response[0]["id"] == term, "ancestor identity")
        ancestry[term] = response[0].get("ancestors", [])
    require("GO:0005737" in ancestry["GO:0005829"], "cytosol/cytoplasm typed-path join")
    core_term = get("core-ontology/GO0106261.json")["results"]
    require(len(core_term) == 1 and core_term[0]["id"] == "GO:0106261" and not core_term[0]["isObsolete"], "core term identity")
    core_paths = {}
    for term, top in (("GO0106261", "GO:0003674"), ("GO0002098", "GO:0008150"), ("GO0005829", "GO:0110165"), ("GO0033588", "GO:0032991")):
        paths_for_term = get("core-ontology/" + term + "-paths-is_a.json")["results"]
        require(paths_for_term, "missing typed core path")
        for path in paths_for_term:
            require(path and path[0]["child"] == term.replace("GO", "GO:", 1) and path[-1]["parent"] == top, "core branch endpoints")
            require(all(edge["relationship"] == "is_a" for edge in path), "core path relation")
            require(all(a["parent"] == b["child"] for a, b in zip(path, path[1:])), "discontinuous core path")
        core_paths[term] = paths_for_term
    entry = get("database/InterPro-IPR037289.json")["metadata"]
    matches = get("database/InterPro-Q6IA86.json")
    require(matches["next"] is None, "incomplete InterPro result")
    target = [x for x in matches["results"] if x["metadata"]["accession"] == "IPR037289"]
    require(len(target) == 1, "unique target InterPro match")
    locations = {key: get("database/" + key + ".json")["geneOntologies"] for key in ("SL-0086", "SL-0191")}

    xml = data["database/HPA-ELP2.xml"]
    require(b"<!DOCTYPE" not in xml.upper() and b"<!ENTITY" not in xml.upper(), "unsupported XML entity declaration")
    hpa = ET.fromstring(xml).find("entry")
    require(hpa is not None and hpa.findtext("name") == "ELP2", "HPA identity")
    overall = hpa.find("cellExpression")
    antibodies = []
    for antibody in hpa.findall("antibody"):
        for expression in antibody.findall("cellExpression"):
            assays = []
            for assay in expression.findall("subAssay"):
                assays.append({"validation": assay.findtext("verification"), "cells": [{"cell": x.findtext("cellLine"), "locations": [{"go": y.get("GOId"), "label": y.text} for y in x.findall("location")]} for x in assay.findall("data")]})
            antibodies.append({"id": antibody.get("id"), "assays": assays})
    return {"source_rows": len(sources), "raw_GOA_contexts": len(goa), "source_joins": joins, "products": product_checks,
            "terms": terms, "ancestors_via_is_a_and_part_of": ancestry, "core_ontology": {"activity_term": core_term[0], "typed_paths": core_paths, "scope": "Ontology identity and branch placement only; not an independent ELP2 catalytic assay."},
            "paint": {"tree_nodes": len(nodes), "MSA_entries": len(msa), "human_leaf": human, "human_path": paths[human], "assertion_taxon": nodes["PTN000521836"]["species"], "bundled_path_records": ibd, "sequence_checks": sequence_checks, "donor_annotations": donor_annotations, "scope": "The archived GAF is an explicitly selected human-path subset. This replay establishes its positive literal join, not global absence of losses or complete historical donor evidence."},
            "interpro": {"entry_GO_mapping": entry["go_terms"], "target_match": target[0]}, "SL_mappings": locations,
            "HPA": {"summary": overall.findtext("summary"), "reliability": overall.findtext("verification"), "locations": [{"go": x.get("GOId"), "status": x.get("status"), "label": x.text} for x in overall.findall("data/location")], "antibodies": antibodies, "image_pixels_inspected": False},
            "limits": "Database and sequence provenance only. No article bodies, figure pixels, provider output or annotation verdicts are generated or validated by this program. Seven products do not imply seven validated activities."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument("--output", type=Path, help="Optional new path for independently derived JSON; never overwrites.")
    args = parser.parse_args()
    result = project(read_inputs(args.root))
    output = encoded(result)
    require(output == (args.root / "results.json").read_bytes(), "saved projection differs from raw-derived result")
    if args.output:
        with args.output.open("xb") as handle:
            handle.write(output)
    print(json.dumps({"status": "PASS", "sources": result["source_rows"], "raw_contexts": result["raw_GOA_contexts"], "products": len(result["products"]), "tree_nodes": result["paint"]["tree_nodes"], "MSA_sequence_checks": len(result["paint"]["sequence_checks"]), "result_sha256": digest(output)}, sort_keys=True))


if __name__ == "__main__":
    main()
