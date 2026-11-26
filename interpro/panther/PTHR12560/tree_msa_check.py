"""Tree topology and catalytic-residue conservation for a PANTHER family.

Run from the repository root:

    uv run python interpro/panther/PTHR12560/tree_msa_check.py

The family is the name of the folder holding this script. Inputs are fetched live and
kept only in the git-ignored ``.cache/panther_family_analysis/<FAMILY>/``:

* the PANTHER ``treeinfo`` tree (topology, event types, species labels);
* the PANTHER ``familymsa`` alignment (leaves and reconstructed internal nodes; only
  leaf rows are used). It is an HMM-style alignment: upper-case letters sit in match
  columns, lower-case letters are unaligned insert-state residues;
* UniProt JSON records of the reference proteins, from which the reference residues
  are read (``Active site`` and single-residue ``Mutagenesis`` features).

Output: ``<FAMILY>-tree-msa-check.txt``, with

1. for every node named in ``<FAMILY>-paint.tsv``: its event type, species label,
   leaf and species counts, and its child nodes; then every duplication node with at
   least ``MIN_DUP`` leaves;
2. for every reference residue: the alignment column, whether it is a match column,
   and the residue counts over all leaves and per clade;
3. every leaf whose residue differs from the reference at an ``Active site`` column or
   at a column whose mutation abolishes activity in both reference proteins (a
   substitution that a reference feature reports as not affecting activity is allowed);
4. for named leaves: the residue and its own sequence position at each such column;
5. for every leaf below a PAINT loss (negated) node: the UniProt entry type, EC numbers
   with their evidence, and mutagenesis features;
6. which reviewed members of ``<FAMILY>-entries.csv`` are leaves of the tree.

Nothing about the result is hard-coded; a residue the alignment does not show is
reported as a gap.
"""

from __future__ import annotations

import csv
import json
import re
from collections import Counter
from pathlib import Path

import requests

HERE = Path(__file__).resolve().parent
FAMILY = HERE.name
CACHE = Path(".cache") / "panther_family_analysis" / FAMILY
API = "https://pantherdb.org/services/oai/pantherdb"
# Reference proteins whose UniProt features define the residues that are checked.
REFERENCES = ["Q6ZMG9", "P28496"]
# Organisms whose leaves are listed individually in section 4.
NAMED_ORGANISMS = {
    "Homo sapiens", "Mus musculus", "Drosophila melanogaster", "Caenorhabditis elegans",
    "Caenorhabditis briggsae", "Saccharomyces cerevisiae", "Schizosaccharomyces pombe",
    "Arabidopsis thaliana", "Dictyostelium discoideum", "Candida albicans",
    "Emericella nidulans",
}
MIN_DUP = 20


def cached_json(name: str, url: str, params: dict | None = None) -> dict:
    """Fetch ``url`` as JSON, caching the payload under CACHE."""
    CACHE.mkdir(parents=True, exist_ok=True)
    path = CACHE / name
    if not path.exists():
        r = requests.get(url, params=params, timeout=300,
                         headers={"User-Agent": "family-msa-check"})
        r.raise_for_status()
        path.write_text(r.text)
    return json.loads(path.read_text())


def kids(node: dict) -> list[dict]:
    """Child nodes of a treeinfo node."""
    ch = node.get("children", {}).get("annotation_node", [])
    return [ch] if isinstance(ch, dict) else ch


def index_tree(root: dict) -> tuple[dict, dict, dict]:
    """Return (node by id, leaf ids below each node, parent id of each node)."""
    nodes: dict[str, dict] = {}
    below: dict[str, list[str]] = {}
    parent: dict[str, str] = {}

    def walk(n: dict) -> list[str]:
        pid = n["persistent_id"]
        nodes[pid] = n
        ks = kids(n)
        if not ks:
            below[pid] = [pid]
            return [pid]
        acc: list[str] = []
        for c in ks:
            parent[c["persistent_id"]] = pid
            acc.extend(walk(c))
        below[pid] = acc
        return acc

    walk(root)
    return nodes, below, parent


def describe(nodes: dict, below: dict, pid: str) -> str:
    """One-line description of a tree node."""
    n = nodes[pid]
    if not kids(n):
        name = n.get("node_name", "")
        acc = name.split("UniProtKB=")[-1] if "UniProtKB=" in name else "-"
        return (f"{pid} LEAF {n.get('organism', '')} {n.get('gene_symbol') or '-'} "
                f"UniProtKB:{acc} {n.get('prop_sf_id', '')}")
    leaves = below[pid]
    species = {nodes[x].get("organism", "") for x in leaves}
    sf = Counter(nodes[x].get("prop_sf_id", "").split(":")[-1] for x in leaves)
    sf_txt = ",".join(f"{k}={v}" for k, v in sf.most_common(6))
    return (f"{pid} {n.get('event_type', '?')} [{n.get('species', '') or 'no species label'}] "
            f"leaves={len(leaves)} species={len(species)} leaf_subfamilies({sf_txt}"
            f"{',...' if len(sf) > 6 else ''})")


def reference_residues(acc: str) -> tuple[str, list[tuple[int, str, str]]]:
    """Sequence and (position, feature type, note) of the checked residues of ``acc``."""
    rec = cached_json(f"{acc}.json", f"https://rest.uniprot.org/uniprotkb/{acc}.json")
    out = []
    for f in rec["features"]:
        s, e = f["location"]["start"]["value"], f["location"]["end"]["value"]
        if s != e:
            continue
        if f["type"] == "Active site" or (f["type"] == "Mutagenesis"):
            note = f.get("description", "")
            alt = f.get("alternativeSequence", {})
            if alt:
                note = (f"{alt.get('originalSequence', '')}->"
                        f"{','.join(alt.get('alternativeSequences', []))}: {note}")
            out.append((s, f["type"], note))
    return rec["sequence"]["value"], out


def column_of(aligned: str, position: int) -> tuple[int, str] | None:
    """Alignment column (0-based) and character of the 1-based residue ``position``."""
    seen = 0
    for col, ch in enumerate(aligned):
        if ch.isalpha():
            seen += 1
            if seen == position:
                return col, ch
    return None


def residue_at(aligned: str, col: int) -> tuple[str, int | None]:
    """Character at ``col`` and its 1-based position in the ungapped sequence."""
    ch = aligned[col]
    if not ch.isalpha():
        return "-", None
    return ch, sum(c.isalpha() for c in aligned[: col + 1])


def main() -> None:
    """Write the tree and alignment check for FAMILY."""
    tree = cached_json("tree.json", f"{API}/treeinfo", {"family": FAMILY})
    version = tree["search"]["product"]["version"]
    root = tree["search"]["tree_topology"]["annotation_node"]
    nodes, below, parent = index_tree(root)
    leaves = below[root["persistent_id"]]
    msa_payload = cached_json("msa.json", f"{API}/familymsa", {"family": FAMILY})
    msa = {x["persistent_id"]: x["sequence"]
           for x in msa_payload["search"]["MSA_list"]["sequence_info"]}
    acc_leaf = {}
    for pid in leaves:
        name = nodes[pid].get("node_name", "")
        if "UniProtKB=" in name:
            acc_leaf[name.split("UniProtKB=")[-1]] = pid

    out = [f"family {FAMILY} PANTHER release {version}: {len(leaves)} leaves, "
           f"{len(nodes) - len(leaves)} internal nodes, "
           f"{len({nodes[x].get('organism') for x in leaves})} species; "
           f"MSA rows {len(msa)}, leaf rows {sum(x in msa for x in leaves)}, "
           f"columns {len(next(iter(msa.values())))}"]

    out.append("")
    out.append("# 1. PAINT nodes in the tree")
    paint_nodes: list[str] = []
    loss_nodes: list[str] = []
    with (HERE / f"{FAMILY}-paint.tsv").open() as fh:
        for row in csv.reader(fh, delimiter="\t"):
            if len(row) > 5 and row[1].startswith("PTN"):
                out.append(f"paint row: {row[4]} {row[1]} {row[2]} negated={row[5]}")
                if row[5] == "true" and row[1] not in loss_nodes:
                    loss_nodes.append(row[1])
                if row[1] not in paint_nodes:
                    paint_nodes.append(row[1])
    for pid in paint_nodes:
        if pid not in nodes:
            out.append(f"{pid} NOT IN TREE")
            continue
        out.append(f"node {describe(nodes, below, pid)}")
        path, cur = [], pid
        while cur in parent:
            cur = parent[cur]
            path.append(f"{cur}({nodes[cur].get('event_type', '?')[:4]},"
                        f"{nodes[cur].get('species', '') or '-'})")
        out.append(f"  ancestors: {' < '.join(path) if path else 'none (root)'}")
        for c in kids(nodes[pid]):
            out.append(f"  child {describe(nodes, below, c['persistent_id'])}")
            for g in kids(c):
                out.append(f"    grandchild {describe(nodes, below, g['persistent_id'])}")
        if pid in parent:
            for sib in kids(nodes[parent[pid]]):
                if sib["persistent_id"] != pid:
                    out.append(f"  sister {describe(nodes, below, sib['persistent_id'])}")
                    for g in kids(sib):
                        out.append(f"    sister child {describe(nodes, below, g['persistent_id'])}")
    out.append(f"duplication nodes with >= {MIN_DUP} leaves:")
    for pid, n in nodes.items():
        if n.get("event_type") == "DUPLICATION" and len(below[pid]) >= MIN_DUP:
            par = parent.get(pid)
            out.append(f"  {describe(nodes, below, pid)} parent "
                       f"{par}[{nodes[par].get('species', '') if par else ''}]")
            for c in kids(n):
                out.append(f"    child {describe(nodes, below, c['persistent_id'])}")

    # Clades used to summarise conservation: children of the root, then their children
    # where a child holds more than a quarter of the tree.
    clades: list[str] = []

    def split(pid: str, depth: int) -> None:
        for c in kids(nodes[pid]):
            cid = c["persistent_id"]
            if kids(c) and len(below[cid]) > len(leaves) / 8 and depth < 6:
                split(cid, depth + 1)
            else:
                clades.append(cid)

    split(root["persistent_id"], 0)
    for pid in paint_nodes:
        if pid in nodes and pid not in clades and pid != root["persistent_id"]:
            clades.append(pid)

    out.append("")
    out.append("# 2. Reference residues and their alignment columns")
    key_cols: dict[int, list[str]] = {}
    tolerated: dict[int, set[str]] = {}
    abolish_by_ref: dict[int, set[str]] = {}
    for acc in REFERENCES:
        seq, feats = reference_residues(acc)
        pid = acc_leaf.get(acc)
        if pid is None or pid not in msa:
            out.append(f"reference {acc}: not a leaf of the alignment")
            continue
        same = msa[pid].replace(".", "").replace("-", "").upper() == seq
        out.append(f"reference UniProtKB:{acc} leaf {pid} length {len(seq)}; "
                   f"alignment row equals the UniProt canonical sequence: {same}")
        for pos, ftype, note in feats:
            hit = column_of(msa[pid], pos)
            if hit is None:
                continue
            col, ch = hit
            label = f"{acc}:{seq[pos - 1]}{pos}"
            out.append(f"  {label} column {col} {'match' if ch.isupper() else 'INSERT'} "
                       f"[{ftype}] {note[:110]}")
            key_cols.setdefault(col, []).append(label)
            tolerated.setdefault(col, set()).add(seq[pos - 1])
            neutral = re.match(r"\w->([\w,]+): Does not affect", note)
            if neutral:
                tolerated[col].update(neutral.group(1).split(","))
            if ftype == "Active site" or re.search(r"[Aa]bolish", note):
                abolish_by_ref.setdefault(col, set()).add(acc)
                if ftype == "Active site":
                    abolish_by_ref[col].add("ACT_SITE")

    strict = sorted(c for c, refs in abolish_by_ref.items()
                    if "ACT_SITE" in refs or len(refs - {"ACT_SITE"}) == len(REFERENCES))
    out.append("")
    out.append("# 3. Residue counts per reference column (upper case = match state)")
    for col in sorted(key_cols):
        allc = Counter(residue_at(msa[x], col)[0].upper() for x in leaves if x in msa)
        out.append(f"column {col} ({'; '.join(key_cols[col])})"
                   f"{' STRICT' if col in strict else ''}: all leaves "
                   + " ".join(f"{k}={v}" for k, v in allc.most_common()))
        if col in strict:
            for cid in clades:
                cc = Counter(residue_at(msa[x], col)[0].upper() for x in below[cid] if x in msa)
                out.append(f"    {describe(nodes, below, cid).split(' leaf_subfamilies')[0]}: "
                           + " ".join(f"{k}={v}" for k, v in cc.most_common()))
    out.append("")
    out.append("# 4. Leaves that differ from the reference at a STRICT column")
    out.append("a substitution that a reference Mutagenesis feature reports as not affecting "
               "activity is not counted as a difference")
    out.append("STRICT = Active site column, or a column whose mutation abolishes activity "
               "in every reference protein")
    n_dev = 0
    for pid in leaves:
        if pid not in msa:
            out.append(f"{pid} has no alignment row")
            continue
        devs = []
        for col in strict:
            ch, pos = residue_at(msa[pid], col)
            if ch.upper() not in tolerated[col]:
                devs.append(f"{key_cols[col][0]}->{ch}{pos if pos else ''}")
        if devs:
            n_dev += 1
            seq_len = sum(c.isalpha() for c in msa[pid])
            out.append(f"  {describe(nodes, below, pid)} length {seq_len}: {' '.join(devs)}")
    out.append(f"leaves differing at a STRICT column: {n_dev} of {len(leaves)}")

    out.append("")
    out.append("# 5. Named leaves: residue and own position at each STRICT column")
    out.append("columns: " + " | ".join("/".join(key_cols[c]) for c in strict))
    for pid in leaves:
        n = nodes[pid]
        if n.get("organism") not in NAMED_ORGANISMS or pid not in msa:
            continue
        cells = []
        for col in strict:
            ch, pos = residue_at(msa[pid], col)
            cells.append(f"{ch}{pos if pos else ''}")
        out.append(f"  {describe(nodes, below, pid)}: {' '.join(cells)}")

    out.append("")
    out.append("# 6. UniProt record of each leaf below a PAINT loss (negated) node")
    for node in loss_nodes:
        for pid in below.get(node, []):
            name = nodes[pid].get("node_name", "")
            if "UniProtKB=" not in name:
                continue
            acc = name.split("UniProtKB=")[-1]
            rec = cached_json(f"{acc}.json", f"https://rest.uniprot.org/uniprotkb/{acc}.json")
            desc = rec.get("proteinDescription", {})
            rname = desc.get("recommendedName") or (desc.get("submissionNames") or [{}])[0]
            ecs = []
            for ec in rname.get("ecNumbers", []):
                ev = ",".join(sorted(f"{e.get('evidenceCode')}|{e.get('source', '')}:{e.get('id', '')}"
                                     for e in ec.get("evidences", [])))
                ecs.append(f"EC {ec['value']} [{ev}]")
            out.append(f"below {node}: UniProtKB:{acc} {rec.get('entryType', '')}; "
                       f"name {rname.get('fullName', {}).get('value', '-')}; "
                       f"{'; '.join(ecs) if ecs else 'no EC number'}")
            for f in rec.get("features", []):
                if f["type"] == "Mutagenesis":
                    alt = f.get("alternativeSequence", {})
                    ev = ",".join(sorted(f"{e.get('source', '')}:{e.get('id', '')}"
                                         for e in f.get("evidences", [])))
                    out.append(f"  mutagenesis {acc} {f['location']['start']['value']}.."
                               f"{f['location']['end']['value']} "
                               f"{alt.get('originalSequence', '')}->"
                               f"{','.join(alt.get('alternativeSequences', []))}: "
                               f"{f.get('description', '')} [{ev}]")

    out.append("")
    out.append("# 7. Reviewed (Swiss-Prot) family members and the tree")
    with (HERE / f"{FAMILY}-entries.csv").open() as fh:
        members = list(csv.DictReader(fh))
    out.append(f"reviewed members {len(members)}; tree leaves among them "
               f"{sum(m['id'] in acc_leaf for m in members)}")
    for m in members:
        pid = acc_leaf.get(m["id"])
        tree_sf = nodes[pid].get("prop_sf_id", "") if pid else ""
        note = "" if not pid or tree_sf == m["subfamily"] else f" (tree leaf subfamily {tree_sf})"
        out.append(f"member UniProtKB:{m['id']} {m['gene'] or '-'} [{m['source_tax_name']}] "
                   f"{m['subfamily'] or '-'} {m['subfamily_name']} length {m['length']} "
                   f"{'TREE_LEAF ' + pid if pid else 'NOT_IN_TREE'}{note}")

    (HERE / f"{FAMILY}-tree-msa-check.txt").write_text("\n".join(out) + "\n")
    print(f"wrote {FAMILY}-tree-msa-check.txt ({len(out)} lines)")


if __name__ == "__main__":
    main()
