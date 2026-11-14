"""Reproduce Q47690 structure and PAINT placement from frozen official inputs."""

import hashlib
import json
from pathlib import Path
import re

AUDIT = Path(__file__).resolve().parent
ROOT = AUDIT.parents[3]


def main():
    raw = ROOT / "genes/ECOLI/mmuM/mmuM-uniprot.txt"
    sequence_block = raw.read_text().split("SQ   SEQUENCE")[1].split("\n", 1)[1]
    sequence = re.sub("[^A-Z]", "", sequence_block.split("//")[0])
    entity = json.loads((AUDIT / "5DMM-protein.json").read_text())
    pdb_sequence = entity["entity_poly"]["pdbx_seq_one_letter_code_can"]
    entry = json.loads((AUDIT / "5DMM-entry.json").read_text())
    zinc = json.loads((AUDIT / "5DMM-ligand-2.json").read_text())
    substrate = json.loads((AUDIT / "5DMM-ligand-4.json").read_text())
    assert sequence == pdb_sequence and len(sequence) == 310
    assert entity["entity_poly"]["rcsb_mutation_count"] == 0
    assert entity["rcsb_polymer_entity_container_identifiers"]["uniprot_ids"] == [
        "Q47690"
    ]
    assert entry["rcsb_entry_container_identifiers"]["pubmed_id"] == 26564203
    assert zinc["pdbx_entity_nonpoly"]["comp_id"] == "ZN"
    assert substrate["pdbx_entity_nonpoly"]["comp_id"] == "HCS"
    tree = json.loads((AUDIT / "PTHR46015-treeinfo.json").read_text())["search"][
        "tree_topology"
    ]["annotation_node"]
    paths = []

    def walk(node, ancestry):
        path = ancestry + [node["persistent_id"]]
        if node.get("node_name", "").endswith("UniProtKB=Q47690"):
            paths.append(path)
        children = node.get("children", {}).get("annotation_node", [])
        if isinstance(children, dict):
            children = [children]
        for child in children:
            walk(child, path)

    walk(tree, [])
    assert paths == [["PTN001843930", "PTN000472791", "PTN000473134", "PTN001078917"]]
    result = {
        "pass": True,
        "length": 310,
        "structure_exact_sequence": True,
        "structural_zinc": True,
        "structural_homocysteine": True,
        "raw_sha256": hashlib.sha256(raw.read_bytes()).hexdigest(),
        "official_tree_ancestry": paths[0],
        "limit": "Structural identity does not establish byte-identical historical KL19/JM109 constructs or complete native SMM cycling.",
    }
    (AUDIT / "identity-verification.json").write_text(
        json.dumps(result, indent=2) + "\n"
    )
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
