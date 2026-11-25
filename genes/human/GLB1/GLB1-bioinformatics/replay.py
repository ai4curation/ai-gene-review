"""Replay a specified PANTHER book, literal PAINT joins and target alignment.

Only deterministic identities and topology are emitted. Biological interpretation
belongs in RESULTS.md. Uses Python standard library; no network or canonical writes.
"""
import argparse
import csv
import gzip
import hashlib
import json
from pathlib import Path
import re
import sys


def pin(p):
    p = Path(p).resolve()
    b = p.read_bytes()
    try:
        display = p.relative_to(Path(__file__).resolve().parent)
    except ValueError:
        display = p
    return {"path": str(display), "bytes": len(b), "sha256": hashlib.sha256(b).hexdigest()}


def fasta(p):
    seq, name = {}, None
    with gzip.open(p, "rt") if str(p).endswith(".gz") else Path(p).open() as stream:
        lines = stream.read().splitlines()
    for line in lines:
        if line.startswith(">"):
            name = line[1:]
            assert name not in seq
            seq[name] = ""
        elif line.strip():
            assert name is not None
            seq[name] += line.strip()
    assert seq
    return seq


def ungap(seq):
    return re.sub(r"[.\-\s]", "", seq).upper().removesuffix("*")


class Tree:
    def __init__(self, text, mapping):
        self.text, self.pos, self.mapping = text, 0, mapping

    def subtree(self):
        children = []
        if self.text[self.pos] == "(":
            self.pos += 1
            while True:
                children.append(self.subtree())
                if self.text[self.pos] == ",":
                    self.pos += 1
                    continue
                assert self.text[self.pos] == ")"
                self.pos += 1
                break
        start = self.pos
        while self.text[self.pos] not in ":,()[];":
            self.pos += 1
        name = self.text[start:self.pos]
        branch = None
        if self.text[self.pos] == ":":
            self.pos += 1
            start = self.pos
            while self.text[self.pos] not in ",()[];":
                self.pos += 1
            branch = float(self.text[start:self.pos])
        props = {}
        if self.text[self.pos] == "[":
            end = self.text.index("]", self.pos)
            comment = self.text[self.pos+1:end]
            assert comment.startswith("&&NHX:")
            props = dict(x.split("=", 1) for x in comment[6:].split(":"))
            self.pos = end+1
        an = props.get("ID", name)
        assert an in self.mapping
        return {"an": an, "ptn": self.mapping[an], "branch_length": branch, "props": props, "children": children}


def main():
    ap = argparse.ArgumentParser()
    for k in ["family", "book", "mapping", "ibd", "raw", "fasta", "accession", "output"]:
        ap.add_argument("--"+k, required=True)
    ap.add_argument("--paint")
    ap.add_argument("--entries")
    ap.add_argument("--agi-crosswalk")
    ap.add_argument("--zfin-crosswalk")
    ap.add_argument("--domain-start", type=int)
    ap.add_argument("--domain-end", type=int)
    a = ap.parse_args()
    book = Path(a.book)
    maprows = []
    with gzip.open(a.mapping, "rt") as f:
        for i, line in enumerate(f, 1):
            if line.startswith(a.family+":"):
                fields = line.rstrip("\n").split("\t")
                maprows.append({"line": i, "text": line.rstrip("\n"), "an": fields[0].split(":", 1)[1], "ptn": fields[1]})
    mapping = {x["an"]: x["ptn"] for x in maprows}
    assert len(mapping) == len(maprows) and mapping
    reverse = {p: an for an, p in mapping.items()}
    assert len(reverse) == len(mapping)
    lines = (book/"tree.tree").read_text().splitlines()
    parser = Tree(lines[0], mapping)
    root = parser.subtree()
    assert parser.text[parser.pos:] == ";"
    nodes, parents = {}, {}

    def visit(n, parent=None):
        assert n["an"] not in nodes
        nodes[n["an"]] = n
        if parent:
            parents[n["an"]] = parent
        for child in n["children"]:
            visit(child, n["an"])

    visit(root)
    names = {}
    for line in lines[1:]:
        if line:
            an, label = line.rstrip(";").split(":", 1)
            names[an] = label
    assert set(nodes) == set(mapping)
    assert set(names) == {an for an, n in nodes.items() if not n["children"]}
    _leaf_reverse = {label: an for an, label in names.items()}
    duplicate_leaf_names = {label: [an for an, n in names.items() if n == label] for label in names.values() if list(names.values()).count(label) > 1}
    attributes = list(csv.DictReader((book/"attr.tab").open(), delimiter="\t", quotechar="'"))
    for row in attributes:
        node = row["Protein_Id"]
        if node not in nodes:
            # Public node disambiguates repeated leaf identifiers without collapsing topology.
            label = node
            node = reverse[row["Public_node_id"]]
            assert names[node] == label
        assert row["Public_node_id"] == mapping[node]

    def lineage(an):
        path = [an]
        while an in parents:
            an = parents[an]
            path.append(an)
        return path[::-1]

    def node_info(an):
        return {"an": an, "ptn": mapping[an], "name": names.get(an), "props": nodes[an]["props"], "lineage": lineage(an)}

    targets = [an for an, label in names.items() if "UniProtKB="+a.accession in label.split("|")]
    assert len(targets) == 1
    target = targets[0]
    target_path = lineage(target)
    msa, cluster = fasta(book/"tree.mia.gz"), fasta(book/"cluster.fasta.gz")
    assert set(msa) == set(nodes)
    assert len({len(s) for s in msa.values()}) == 1
    assert set(names.values()) <= set(cluster)
    cluster_extra_labels = sorted(set(cluster)-set(names.values()))
    canonical = fasta(a.fasta)
    assert len(canonical) == 1
    target_seq = ungap(msa[target])
    assert target_seq == ungap(cluster[names[target]]) == ungap(next(iter(canonical.values())))
    records = []
    with Path(a.ibd).open() as f:
        for i, line in enumerate(f, 1):
            fields = line.rstrip("\n").split("\t")
            if len(fields) > 7 and fields[1] in reverse:
                records.append({"line": i, "text": line.rstrip("\n"), "fields": fields, "node": node_info(reverse[fields[1]])})

    _entries = list(csv.DictReader(Path(a.entries).open())) if a.entries else []

    def donor_nodes(donor):
        db, identifier = donor.split(":", 1)
        if db == "PANTHER":
            return [reverse[identifier]]
        db = {"FB": "FlyBase", "WB": "WormBase"}.get(db, db)
        needle = db+"="+identifier.replace(":", "=")
        found = [an for an, label in names.items() if needle in label.split("|")]
        if not found and db == "AGI_LocusCode":
            official = json.loads(Path(a.agi_crosswalk).read_text())["results"]
            accessions = {e["primaryAccession"] for e in official if any(g["value"].upper() == identifier.upper() for gene in e.get("genes", []) for g in gene.get("orderedLocusNames", []))}
            found = [an for an, label in names.items() if any("UniProtKB="+acc in label.split("|") for acc in accessions)]
        if not found and db == "ZFIN":
            official = json.loads(Path(a.zfin_crosswalk).read_text())["results"]
            accessions = {e["primaryAccession"] for e in official if any(x["database"] == "ZFIN" and x["id"] == identifier for x in e.get("uniProtKBCrossReferences", []))}
            found = [an for an, label in names.items() if any("UniProtKB="+acc in label.split("|") for acc in accessions)]
        assert found, donor
        return found

    raw = json.loads(Path(a.raw).read_text())
    joins = []
    selected_nodes = {target}
    for record in records:
        fields = record["fields"]
        selected_nodes.add(record["node"]["an"])
        record["donor_mapping"] = []
        for donor in fields[7].split("|"):
            dns = donor_nodes(donor)
            selected_nodes.update(dns)
            if fields[6] == "IBD":
                assert all(record["node"]["an"] in lineage(n) for n in dns)
            record["donor_mapping"].append({"literal": donor, "nodes": [node_info(n) for n in dns]})
    for i, row in enumerate(raw):
        if row["goEvidence"] != "IBA":
            continue
        incoming = [x["db"]+":"+x["id"] for group in row["withFrom"] for x in group["connectedXrefs"]]
        ptns = [x.split(":", 1)[1] for x in incoming if x.startswith("PANTHER:")]
        assert len(ptns) == 1
        an = reverse[ptns[0]]
        assert an in target_path
        matches = [r for r in records if r["fields"][1] == ptns[0] and r["fields"][4] == row["goId"] and r["fields"][6] == "IBD"]
        assert len(matches) == 1
        record = matches[0]
        donors = record["fields"][7].split("|")
        mapped = []
        for donor in donors:
            dns = donor_nodes(donor)
            selected_nodes.update(dns)
            assert all(an in lineage(n) for n in dns)
            mapped.append({"literal": donor, "nodes": [node_info(n) for n in dns], "target_self": target in dns})
        selected_nodes.add(an)
        joins.append({"raw_index": i, "original": row, "assertion": node_info(an), "literal_gaf": record, "donors": mapped, "incoming_donor_set_equal": set(donors) == {x for x in incoming if not x.startswith("PANTHER:")}})
    negative = []
    for r in records:
        f = r["fields"]
        if f[6] in ["IRD", "IKR"] or "NOT" in f[3].split("|"):
            neg = dict(r)
            neg["on_target_lineage"] = r["node"]["an"] in target_path
            neg["referenced_source_nodes"] = [node_info(n) for donor in f[7].split("|") for n in donor_nodes(donor)]
            negative.append(neg)
            selected_nodes.add(r["node"]["an"])
            for donor in f[7].split("|"):
                selected_nodes.update(donor_nodes(donor))
    paint = None
    paint_comparisons = []
    if a.paint:
        paint = list(csv.DictReader(Path(a.paint).open(), delimiter="\t"))
        for row in paint:
            match = [r for r in records if r["fields"][1] == row["node"] and r["fields"][4] == row["go_id"] and r["fields"][6] == row["evidence"]]
            assert len(match) == 1
            original_seeds = match[0]["fields"][7]
            assert set(original_seeds.split("|")) == set(row["seeds"].split("|"))
            paint_comparisons.append({"node": row["node"], "term": row["go_id"], "evidence": row["evidence"], "gaf_seed_literal": original_seeds, "paint_seed_literal": row["seeds"], "exact_order_equal": original_seeds == row["seeds"], "donor_set_equal": True})
            assert ("NOT" in match[0]["fields"][3].split("|")) == (row["negated"] == "true")
    domain = None
    if a.domain_start is not None:
        assert 1 <= a.domain_start <= a.domain_end <= len(target_seq)
        position, columns = 0, []
        for col, residue in enumerate(msa[target]):
            if residue not in "-. ":
                position += 1
                if a.domain_start <= position <= a.domain_end:
                    columns.append(col)
        domain = {"target_start": a.domain_start, "target_end": a.domain_end, "msa_columns_zero_based": columns, "sequences": []}
        for an in sorted(selected_nodes, key=lambda n: int(n[2:])):
            projected = "".join(msa[an][c] for c in columns).upper()
            positions, n = {}, 0
            for col, residue in enumerate(msa[an]):
                if residue not in "-. ":
                    n += 1
                    positions[col] = n
            domain["sequences"].append({"node": node_info(an), "projected": projected, "residue_positions": [positions.get(c) for c in columns]})
    files = [a.mapping, a.ibd, a.raw, a.fasta, __file__] + [book/f for f in ["tree.tree", "tree.mia.gz", "attr.tab", "cluster.fasta.gz"]]
    files += [x for x in [a.paint, a.entries, a.agi_crosswalk, a.zfin_crosswalk] if x]
    result = {"family": a.family, "python": sys.version, "target": {**node_info(target), "length": len(target_seq), "sequence_sha256": hashlib.sha256(target_seq.encode()).hexdigest()}, "duplicate_leaf_names": duplicate_leaf_names, "cluster_extra_labels": cluster_extra_labels, "tree_node_count": len(nodes), "leaf_count": len(names), "alignment_columns": len(msa[target]), "attribute_rows": len(attributes), "literal_mapping": maprows, "target_lineage_nodes": [node_info(n) for n in target_path], "joins": joins, "negative_records": negative, "all_family_records": records, "retained_paint_rows": paint, "paint_comparisons": paint_comparisons, "selected_domain_alignment": domain, "inputs": [pin(f) for f in files], "limits": ["No experimental literature or functional loss inferred by this mechanical replay.", "Negative records are node- and GO-term-specific; no incoming NOT field is manufactured.", "Donor count or target-self membership is not a quality test."]}
    out = Path(a.output)
    out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"output": pin(out), "target": result["target"], "nodes": len(nodes), "leaves": len(names), "columns": len(msa[target]), "joins": [(j["raw_index"], j["assertion"]["an"]) for j in joins], "negative": [(n["fields"][4], n["node"]["an"], n["on_target_lineage"]) for n in negative]}, indent=2))


if __name__ == "__main__":
    main()
