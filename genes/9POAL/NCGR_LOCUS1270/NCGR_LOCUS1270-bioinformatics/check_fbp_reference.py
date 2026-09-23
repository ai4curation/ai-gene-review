# /// script
# requires-python = ">=3.12"
# dependencies = ["biopython==1.85", "requests==2.32.5"]
# ///
"""Check the named TreeGrafter reference and compare public FBPase sequences.

This verifies the reference leaf, not the unpublished query insertion edge.
Pairwise identities are descriptive, not a replacement for a gene tree.
"""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re

from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices
import requests

HERE = Path(__file__).resolve().parent


def main():
    target = SeqIO.read(HERE.parent / "NCGR_LOCUS1270-uniprot.txt", "swiss")
    aligner = PairwiseAligner(mode="global", substitution_matrix=substitution_matrices.load("BLOSUM62"),
                              open_gap_score=-10, extend_gap_score=-0.5)
    comparisons = []
    for accession in ["A0A1B6QP66", "P25851", "Q9MA79"]:
        path = HERE / f"{accession}.json"
        url = f"https://rest.uniprot.org/uniprotkb/{accession}.json"
        if not path.exists():
            response = requests.get(url, timeout=45)
            response.raise_for_status()
            path.write_text(response.text)
        data = json.loads(path.read_text())
        if data["primaryAccession"] != accession:
            raise ValueError("Accession changed; inspect before comparing")
        seq = data["sequence"]["value"]
        alignment = aligner.align(str(target.seq), seq)[0]
        a, b = alignment[0], alignment[1]
        identical = sum(x == y and x != "-" for x, y in zip(a, b))
        comparisons.append({"accession": accession, "name": data["proteinDescription"]["recommendedName"]["fullName"]["value"],
                            "url": url, "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                            "length": len(seq), "identical_positions": identical,
                            "alignment_columns": len(a), "identity_all_columns": identical / len(a),
                            "locations": [x for x in data.get("comments", []) if x["commentType"] == "SUBCELLULAR LOCATION"]})
        (HERE / f"alignment-{accession}.txt").write_text(str(alignment))
    # The complete server tree is a reproducible input; retain only the relevant
    # accession-mapped lineage and a response checksum, not an unrelated large tree.
    url = "https://www.pantherdb.org/services/oai/pantherdb/treeinfo"
    response = requests.post(url, data={"family": "PTHR11556"}, headers={"Accept": "application/json"}, timeout=60)
    response.raise_for_status()
    topology = response.json()["search"]["tree_topology"]["annotation_node"]
    found = []

    def walk(node, path):
        if isinstance(node, list):
            for child in node:
                walk(child, path)
            return
        lineage = path + [node.get("persistent_id")]
        if node.get("persistent_id") == "PTN004269459":
            found.append({"lineage": lineage, "node": {k: v for k, v in node.items() if k != "children"}})
        children = node.get("children", {}).get("annotation_node", [])
        if children:
            walk(children, lineage)

    walk(topology, [])
    if len(found) != 1 or "UniProtKB=A0A1B6QP66" not in found[0]["node"].get("node_name", ""):
        raise ValueError("Reference leaf identity changed or is ambiguous")
    seq = str(target.seq)
    result = {"observed_at": datetime.now(timezone.utc).isoformat(), "target": target.id, "length": len(target),
              "comparisons": comparisons, "alignment_method": "Global BLOSUM62; gap-open -10, extension -0.5; terminal gaps included",
              "first50_DE_count": sum(seq[:50].count(x) for x in "DE"),
              "FDPLDGS_starts_1based": [m.start() + 1 for m in re.finditer("FDPLDGS", seq)],
              "CIVSVC_starts_1based": [m.start() + 1 for m in re.finditer("CIVSVC", seq)],
              "tree_request": {"url": url, "family": "PTHR11556", "response_sha256": hashlib.sha256(response.content).hexdigest()},
              "reference": found[0], "limitation": "Reference-leaf mapping does not reconstruct the original TreeGrafter query insertion or demonstrate exclusive localization."}
    (HERE / "reference-comparison.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"target": target.id, "comparisons": [{k: r[k] for k in ("accession", "length", "identical_positions", "alignment_columns", "identity_all_columns")} for r in comparisons]}, indent=2))


if __name__ == "__main__":
    main()
