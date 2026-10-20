#!/usr/bin/env python3
"""Reproduce DST source joins from saved original data. Python 3.9+, standard library."""
from pathlib import Path
import argparse, json, hashlib, csv, base64, re, shlex

P = Path(__file__).resolve().parent
ap = argparse.ArgumentParser(description=__doc__)
for k in ["intact", "opencell", "cif", "tree", "msa", "ibd"]:
    ap.add_argument("--" + k, type=Path, required=True)
ap.add_argument("--check", action="store_true")
ap.add_argument("--output", type=Path)
a = ap.parse_args()
manifest = json.loads((P / "source-manifest.json").read_text())
h = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
for k in ["intact", "opencell", "cif", "tree", "msa", "ibd"]:
    assert h(getattr(a, k)) == manifest["external_inputs"][k]["sha256"], (
        k + " differs from analyzed snapshot"
    )
for k in ["products.fasta", "source-contexts.json"]:
    assert h(P / k) == manifest["bundled_inputs"][k]["sha256"], k
products = {}
current = None
for line in (P / "products.fasta").read_text().splitlines():
    if line.startswith(">"):
        current = line.split("|")[1]
        products[current] = ""
    else:
        products[current] += line.strip()
source = json.loads((P / "source-contexts.json").read_text())
rogids = {
    base64.b64encode(hashlib.sha1(s.encode()).digest()).decode().rstrip("=") + "9606": p
    for p, s in products.items()
}
raw = list(csv.reader(a.intact.open(), delimiter="\t"))
joins = []
for i, s in enumerate(source):
    if s["evidence_type"] != "IPI":
        continue
    pm = s["original_reference_id"].removeprefix("PMID:")
    partners = [
        x.removeprefix("UniProtKB:")
        for x in s.get("supporting_entities", [])
        if x.startswith("UniProtKB:")
    ]
    records = []
    for n, f in enumerate(raw, 1):
        if len(f) < 42 or "pubmed:" + pm not in f[8].split("|"):
            continue
        pair = [x.removeprefix("uniprotkb:") for x in f[:2]]
        if "Q03001" not in pair or not any((x in pair for x in partners)):
            continue
        side = pair.index("Q03001")
        records.append(
            {
                "line_1based": n,
                "participants": f[:2],
                "method": f[6],
                "publication": f[8],
                "taxa": f[9:11],
                "interaction_type": f[11],
                "record_ids": f[13],
                "confidence": f[14],
                "host": f[28],
                "checksums": f[32:34],
                "negative": f[35],
                "features": f[36:38],
                "target_reference_sequence_matches": [
                    v
                    for k, v in rogids.items()
                    if "rogid:" + k in f[32 + side].split("|")
                ],
            }
        )
    joins.append(
        {
            "source_index_0based": i,
            "reference": s["original_reference_id"],
            "partners": partners,
            "records": records,
        }
    )
# Physical CSV line = zero-based data index + 2, because one header precedes records.
oc = [
    {"physical_line_1based": i + 2, "data_index_0based": i, "record": r}
    for i, r in enumerate(csv.DictReader(a.opencell.open()))
    if r["target_gene_name"] == "DST" or r["interactor_gene_name"] == "DST"
]
lines = [x.strip() for x in a.cif.read_text().splitlines()]
loops = []
i = 0
while i < len(lines):
    if lines[i] != "loop_":
        i += 1
        continue
    i += 1
    cols = []
    while i < len(lines) and lines[i].startswith("_"):
        cols.append(lines[i])
        i += 1
    vals = []
    while i < len(lines) and lines[i] != "#":
        vals.extend(shlex.split(lines[i]))
        i += 1
    if cols and len(vals) % len(cols) == 0:
        loops.append(
            (
                cols,
                [
                    dict(zip(cols, vals[j : j + len(cols)]))
                    for j in range(0, len(vals), len(cols))
                ],
            )
        )
entities = next(
    (v for c, v in loops if "_entity_poly.pdbx_seq_one_letter_code_can" in c)
)
refs = next((v for c, v in loops if "_struct_ref.pdbx_db_accession" in c))
sp = []
for r in entities:
    seq = r["_entity_poly.pdbx_seq_one_letter_code_can"]
    hits = []
    for product, s in products.items():
        n = s.find(seq)
        if n >= 0:
            hits.append({"product": product, "start": n + 1, "end": n + len(seq)})
    sp.append(
        {
            "entity": r["_entity_poly.entity_id"],
            "sequence": seq,
            "historical_references": [
                x
                for x in refs
                if x["_struct_ref.entity_id"] == r["_entity_poly.entity_id"]
            ],
            "current_product_matches": hits,
        }
    )
tree = json.loads(a.tree.read_text())["search"]["tree_topology"]["annotation_node"]
nodes = {}
parents = {}


def walk(n, parent=None):
    k = n["persistent_id"]
    nodes[k] = n
    parents[k] = parent
    cs = n.get("children", {}).get("annotation_node", [])
    for c in [cs] if isinstance(cs, dict) else cs:
        walk(c, k)


walk(tree)
leaf = next(
    (
        k
        for k, n in nodes.items()
        if "Q03001" in str({a: b for a, b in n.items() if a != "children"})
    )
)
path = []
k = leaf
while k:
    path.append(k)
    k = parents[k]
path = path[::-1]
msa = json.loads(a.msa.read_text())["search"]["MSA_list"]["sequence_info"]
aligned = next((x["sequence"] for x in msa if x["persistent_id"] == leaf))
seq = re.sub("[^A-Za-z]", "", aligned).upper()
assert seq == products["Q03001-7"]
ibds = []
with a.ibd.open() as f:
    for n, line in enumerate(f, 1):
        v = line.rstrip("\n").split("\t")
        if len(v) > 8 and v[6] == "IBD" and (v[1] in path):
            ibds.append({"line_1based": n, "fields": v})
paint = []
for i, s in enumerate(source):
    if s["evidence_type"] != "IBA":
        continue
    node = next(
        (
            x.removeprefix("PANTHER:")
            for x in s["supporting_entities"]
            if x.startswith("PANTHER:PTN")
        )
    )
    paint.append(
        {
            "source_index_0based": i,
            "term": s["term"],
            "node": node,
            "node_in_target_path": node in path,
            "ibds": [
                x
                for x in ibds
                if x["fields"][1] == node and x["fields"][4] == s["term"]["id"]
            ],
        }
    )
out = {
    "products": [
        {
            "id": k,
            "length": len(v),
            "sequence_sha256": hashlib.sha256(v.encode()).hexdigest(),
        }
        for k, v in products.items()
    ],
    "intact": {"raw_records": len(raw), "source_joins": joins},
    "opencell": oc,
    "structure_entities": sp,
    "paint": {
        "tree_nodes": len(nodes),
        "msa_sequences": len(msa),
        "target_leaf": leaf,
        "target_path": path,
        "target_sequence_match": True,
        "source_joins": paint,
    },
    "scope": "Sequence checks authenticate reference sequences or a deposited peptide, not complete experimental constructs. Fragment features, partner species and original Methods govern interpretation. OpenCell accession groups are not isoform assignments; empty current IntAct joins are not negative experiments.",
}
if a.check:
    assert out == json.loads(
        (P / "measurements.json").read_text()
    ), "Saved results differ"
if a.output:
    a.output.write_text(json.dumps(out, indent=2) + "\n")
print(
    json.dumps(
        {
            "result": "PASS",
            "ipi_source_rows": len(joins),
            "matched_interaction_records": sum((len(x["records"]) for x in joins)),
            "opencell_groups": len(oc),
            "products": len(products),
            "peptide_product_matches": len(sp[1]["current_product_matches"]),
            "iba_source_rows": len(paint),
            "literal_ibd_matches": sum((len(x["ibds"]) for x in paint)),
            "tree_nodes": len(nodes),
            "checked_saved_results": a.check,
        }
    )
)
