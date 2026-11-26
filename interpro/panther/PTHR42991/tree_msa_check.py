"""Tree, MSA, annotation and member check for one PANTHER family (the folder's name).

Run from the repository root:

    uv run python interpro/panther/PTHR42991/tree_msa_check.py

Everything is fetched live and nothing about the result is hard-coded:

* the family tree (PANTHER ``treeinfo``) and the family alignment (PANTHER
  ``familymsa``), both refused unless served for the repository's pinned release;
* the anchor protein's UniProt record, whose ACT_SITE and short BINDING features
  define the positions that are read in the alignment;
* QuickGO annotations of every tree leaf and reviewed member;
* PubMed titles of the PMIDs listed under ``references`` in ``<FAMILY>-review.yaml``.

The anchor (``ANCHOR``) is not itself a tree leaf, so its positions are carried to
alignment columns through a pairwise alignment to the tree leaf most identical to it.
Members that are not tree leaves are compared with the anchor pairwise (BLOSUM62,
gap open -10, extend -0.5). Output: ``<FAMILY>-tree-msa-check.txt``.
"""

from __future__ import annotations

import csv
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any

import requests
from Bio import Align
from Bio.Align import substitution_matrices

from ai_gene_review.etl.panther_trees import PANTHER_RELEASE, same_release, served_release

HERE = Path(__file__).resolve().parent
FAMILY = HERE.name
API = "https://pantherdb.org/services/oai/pantherdb/"
QUICKGO = "https://www.ebi.ac.uk/QuickGO/services/annotation/search"
UNIPROT = "https://rest.uniprot.org/uniprotkb/"
PUBMED = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
#: Best-characterized member with experiment-backed UniProt site features.
ANCHOR = "Q59931"
#: Non-tree accessions compared pairwise in addition to the reviewed members.
EXTRA_PAIRWISE: tuple[str, ...] = ()
EXPERIMENTAL = {"EXP", "IDA", "IMP", "IGI", "IPI", "IEP", "HDA", "HMP", "HTP", "HGI", "HEP"}
TREEGRAFTER_REF = "GO_REF:0000118"


def get_json(url: str, params: dict[str, Any]) -> Any:
    """GET a JSON document, failing loudly on any HTTP error."""
    r = requests.get(url, params=params, headers={"Accept": "application/json"}, timeout=300)
    r.raise_for_status()
    return r.json()


def panther(endpoint: str) -> Any:
    """Fetch a PANTHER family payload and refuse one from another release."""
    payload = get_json(API + endpoint, {"family": FAMILY})
    served = served_release(payload)
    if served is None or not same_release(served, PANTHER_RELEASE):
        raise SystemExit(f"{endpoint}: PANTHER serves {served}, repo pinned to {PANTHER_RELEASE}")
    return payload


def uniprot_text(acc: str) -> str:
    """The UniProt flat-file record of ``acc``."""
    r = requests.get(f"{UNIPROT}{acc}.txt", timeout=120)
    r.raise_for_status()
    return r.text


def record_sequence(text: str) -> str:
    """Sequence from a UniProt flat file.

    >>> record_sequence("ID   X\\nSQ   SEQUENCE 4 AA;\\n     MK LV\\n//\\n")
    'MKLV'
    """
    body = text.split("\nSQ   ", 1)[1].split("\n", 1)[1]
    return re.sub(r"[^A-Z]", "", body.split("//")[0])


def site_positions(text: str) -> dict[int, str]:
    """Positions of ACT_SITE and short (<=3 residue) BINDING features, with their labels.

    >>> t = 'FT   ACT_SITE        250\\nFT   BINDING         154..155\\nFT                   /ligand="substrate"\\n'
    >>> site_positions(t)
    {250: 'ACT_SITE', 154: 'BINDING substrate', 155: 'BINDING substrate'}
    """
    out: dict[int, str] = {}
    lines = text.splitlines()
    for i, line in enumerate(lines):
        m = re.match(r"FT   (ACT_SITE|BINDING)\s+(\d+)(?:\.\.(\d+))?\s*$", line)
        if not m:
            continue
        start, end = int(m.group(2)), int(m.group(3) or m.group(2))
        if end - start > 2:
            continue
        label = m.group(1)
        if label == "BINDING" and i + 1 < len(lines):
            lig = re.search(r'/ligand="([^"]+)"', lines[i + 1])
            label += f" {lig.group(1)}" if lig else ""
        for p in range(start, end + 1):
            out.setdefault(p, label)
    return out


def curated_statements(text: str) -> list[str]:
    """FUNCTION and CATALYTIC ACTIVITY comments that cite a publication (ECO:0000269)."""
    out = []
    for block in re.split(r"\nCC   -!- ", "\n" + "\n".join(x for x in text.splitlines() if x.startswith("CC"))):
        flat = " ".join(x.replace("CC       ", "").replace("CC   ", "").strip() for x in block.splitlines())
        if flat.startswith(("FUNCTION", "CATALYTIC ACTIVITY")) and "ECO:0000269" in flat:
            out.append(re.sub(r"\s+", " ", flat))
    return out


def children(node: dict) -> list[dict]:
    """Child nodes of a treeinfo node (a single child is served as a dict)."""
    ch = node.get("children", {}).get("annotation_node", [])
    return [ch] if isinstance(ch, dict) else ch


class Tree:
    """Parent, child and leaf relations of a PANTHER treeinfo payload."""

    def __init__(self, root: dict) -> None:
        self.nodes: dict[str, dict] = {}
        self.parent: dict[str, str] = {}
        self.leaf_order: list[str] = []
        self._walk(root)
        self.root = root["persistent_id"]

    def _walk(self, n: dict) -> None:
        pid = n["persistent_id"]
        self.nodes[pid] = n
        kids = children(n)
        if not kids:
            self.leaf_order.append(pid)
        for c in kids:
            self.parent[c["persistent_id"]] = pid
            self._walk(c)

    def path(self, pid: str) -> list[str]:
        """Nodes from the root down to ``pid``, inclusive."""
        out = [pid]
        while out[-1] in self.parent:
            out.append(self.parent[out[-1]])
        return out[::-1]

    def leaves(self, pid: str) -> list[str]:
        """Leaf ids at or below ``pid`` in tree order."""
        return [x for x in self.leaf_order if pid in self.path(x)]

    def acc(self, leaf: str) -> str:
        """UniProt accession of a leaf."""
        return next(t.split("=", 1)[1] for t in self.nodes[leaf]["node_name"].split("|") if t.startswith("UniProtKB="))

    def org(self, leaf: str) -> str:
        """PANTHER organism mnemonic of a leaf."""
        return self.nodes[leaf]["node_name"].split("|")[0]

    def describe(self, pid: str) -> str:
        """One-line description of an internal node or leaf."""
        n = self.nodes[pid]
        if not children(n):
            return f"{pid} leaf {self.org(pid)} UniProtKB:{self.acc(pid)} {n.get('gene_symbol', '') or '-'}"
        sf = f" {n['sf_id']}" if n.get("sf_id") else ""
        return f"{pid} {n.get('event_type', '?')} {n.get('species', '') or '-'} leaves={len(self.leaves(pid))}{sf}"


def pairwise_map(a: str, b: str) -> dict[int, int]:
    """1-based position map from ``a`` to ``b`` over a global alignment.

    >>> pairwise_map("MKLV", "MKLV")[3]
    3
    """
    aligner = Align.PairwiseAligner(mode="global")
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score, aligner.extend_gap_score = -10, -0.5
    aln = aligner.align(a, b)[0]
    out: dict[int, int] = {}
    for (rs, re_), (qs, _qe) in zip(*aln.aligned):
        for i in range(re_ - rs):
            out[rs + i + 1] = qs + i + 1
    return out


def identity(a: str, b: str) -> float:
    """Identical aligned positions over the shorter sequence length."""
    mp = pairwise_map(a, b)
    return sum(a[p - 1] == b[q - 1] for p, q in mp.items()) / min(len(a), len(b))


def ungap(s: str) -> str:
    """An alignment row without gap characters, upper-cased."""
    return re.sub(r"[.\-]", "", s).upper()


def quickgo(params: dict[str, Any]) -> list[dict]:
    """All pages of a QuickGO annotation search."""
    out: list[dict] = []
    page = 1
    while True:
        r = get_json(QUICKGO, dict(params, limit=200, page=page))
        out += r["results"]
        if page >= r["pageInfo"]["total"]:
            return out
        page += 1


def with_from(row: dict) -> list[str]:
    """Flat list of ``DB:id`` with/from values of a QuickGO row."""
    return [f"{x['db']}:{x['id']}" for w in (row.get("withFrom") or []) for x in w["connectedXrefs"]]


def main() -> None:
    """Write the report for FAMILY."""
    tree = Tree(panther("treeinfo")["search"]["tree_topology"]["annotation_node"])
    msa = {x["persistent_id"]: x["sequence"] for x in panther("familymsa")["search"]["MSA_list"]["sequence_info"]}
    out: list[str] = [
        f"# {FAMILY} tree and MSA check (PANTHER release {PANTHER_RELEASE}; treeinfo and familymsa services)",
        f"tree leaves {len(tree.leaf_order)}; internal nodes {len(tree.nodes) - len(tree.leaf_order)}; "
        f"MSA rows {len(msa)} (leaves and reconstructed ancestors); MSA columns {len(next(iter(msa.values())))}",
        "",
        "## 1. Topology",
        "events: " + ", ".join(f"{k}={v}" for k, v in sorted(Counter(
            n.get("event_type", "?") for n in tree.nodes.values() if children(n)).items())),
        "subfamily labels on nodes: " + "; ".join(
            f"{n['sf_id']} at {pid} ({n.get('species') or n.get('event_type')}, leaves={len(tree.leaves(pid))})"
            for pid, n in tree.nodes.items() if n.get("sf_id") and children(n)),
        "top of tree:",
    ]
    for pid in [tree.root] + [c["persistent_id"] for c in children(tree.nodes[tree.root])]:
        out.append(f"  {tree.describe(pid)}")
        if pid != tree.root:
            out += [f"    child {tree.describe(c['persistent_id'])}" for c in children(tree.nodes[pid])]

    paint_rows = []
    with (HERE / f"{FAMILY}-paint.tsv").open() as fh:
        for row in csv.reader(fh, delimiter="\t"):
            if len(row) > 6 and row[1].startswith("PTN"):
                paint_rows.append(row)
    out += ["", "## 2. PAINT rows on the tree"]
    for row in paint_rows:
        node, term, evidence, seeds = row[1], row[2], row[4], row[6]
        below = tree.leaves(node)
        out.append(f"{evidence} {node} {term} negated={row[5]} seeds={seeds}: {tree.describe(node)}")
        out.append("  path from root: " + " > ".join(
            f"{p}[{tree.nodes[p].get('event_type', '')}:{tree.nodes[p].get('species', '') or '-'}]" for p in tree.path(node)))
        out.append("  leaf organisms: " + ", ".join(f"{k}={v}" for k, v in sorted(Counter(tree.org(x) for x in below).items())))
        dups = [p for p in tree.nodes if node in tree.path(p) and tree.nodes[p].get("event_type") == "DUPLICATION"]
        out.append(f"  duplication nodes at or below: {len(dups)}")

        def show(pid: str, depth: int, limit: int) -> None:
            out.append("  " * (depth + 1) + tree.describe(pid))
            if depth < limit:
                for c in children(tree.nodes[pid]):
                    show(c["persistent_id"], depth + 1, limit)

        show(node, 0, 3 if len(below) <= 30 else 1)
        sib = [c["persistent_id"] for c in children(tree.nodes[tree.parent[node]]) if c["persistent_id"] != node] if node in tree.parent else []
        out += [f"  sibling {tree.describe(s)}" for s in sib]
    paint_nodes = [r[1] for r in paint_rows]

    # --- anchor sites carried to alignment columns ---
    anchor_text = uniprot_text(ANCHOR)
    anchor_seq = record_sequence(anchor_text)
    version = re.search(r"sequence version (\d+)", anchor_text)
    sites = site_positions(anchor_text)
    leaf_seq = {leaf: ungap(msa[leaf]) for leaf in tree.leaf_order}
    best = max(tree.leaf_order, key=lambda x: identity(anchor_seq, leaf_seq[x]) if len(leaf_seq[x]) > 0.8 * len(anchor_seq) else 0)
    to_best = pairwise_map(anchor_seq, leaf_seq[best])
    col_of: dict[int, int] = {}
    n = 0
    for c, ch in enumerate(msa[best]):
        if ch not in ".-":
            n += 1
            col_of[n] = c
    cols = {p: col_of[to_best[p]] for p in sorted(sites) if p in to_best}
    out += [
        "", "## 3. Function-defining positions in the PANTHER alignment",
        f"anchor UniProtKB:{ANCHOR} sequence version {version.group(1) if version else '?'} length {len(anchor_seq)}; "
        f"positions are its ACT_SITE and short BINDING features, read live from UniProt:",
        "  " + "; ".join(f"{anchor_seq[p - 1]}{p} {sites[p]}" for p in cols),
        f"anchor is not a tree leaf; columns found through leaf {best} UniProtKB:{tree.acc(best)} "
        f"(identity to anchor {identity(anchor_seq, leaf_seq[best]):.2f}; its MSA row equals its UniProt sequence: "
        f"{leaf_seq[best] == record_sequence(uniprot_text(tree.acc(best)))})",
        "each cell is the residue and its position in that protein's own MSA-row numbering; '-' is an alignment gap;",
        "lower case is a PANTHER insert-state residue. clade = PAINT nodes above the leaf, else the child of the root.",
        "leaf\torg\taccession\tlength\tclade\t" + "\t".join(f"{anchor_seq[p - 1]}{p}" for p in cols),
    ]
    patterns: dict[str, Counter] = {}
    for leaf in tree.leaf_order:
        row = msa[leaf]
        cells = []
        for p, c in cols.items():
            ch = row[c]
            cells.append("-" if ch in ".-" else f"{ch}{len(ungap(row[: c + 1]))}")
        path = tree.path(leaf)
        clade = ",".join(x for x in paint_nodes if x in path) or (path[1] if len(path) > 1 else path[0])
        out.append(f"{leaf}\t{tree.org(leaf)}\t{tree.acc(leaf)}\t{len(leaf_seq[leaf])}\t{clade}\t" + "\t".join(cells))
        patterns.setdefault(clade, Counter())["".join(x[0].upper() for x in cells)] += 1
    out.append("residue patterns per clade (one letter per position above, in order; count of leaves):")
    for clade, counter in patterns.items():
        out.append(f"  {clade}: " + ", ".join(f"{k} x{v}" for k, v in counter.most_common()))

    # --- reviewed members that are not tree leaves ---
    with (HERE / f"{FAMILY}-entries.csv").open() as fh:
        members = list(csv.DictReader(fh))
    tree_accs = {tree.acc(x): x for x in tree.leaf_order}
    out += ["", "## 4. Reviewed (Swiss-Prot) members",
            f"members {len(members)}; tree leaves among them {sum(m['id'] in tree_accs for m in members)}",
            "non-leaf members are aligned pairwise to the anchor; closest tree leaf by pairwise identity is given.",
            "accession\tgene\tlength\tstatus\tclosest_leaf(identity)\t" + "\t".join(f"{anchor_seq[p - 1]}{p}" for p in cols) + "\tname"]
    records: dict[str, str] = {}
    full_leaves = [x for x in tree.leaf_order if len(leaf_seq[x]) > 300]
    for acc in [m["id"] for m in members] + list(EXTRA_PAIRWISE):
        records[acc] = uniprot_text(acc)
        seq = record_sequence(records[acc])
        meta = next((m for m in members if m["id"] == acc), {"gene": "", "name": ""})
        if acc in tree_accs:
            status, closest = f"TREE_LEAF {tree_accs[acc]}", "-"
        else:
            near = max(full_leaves, key=lambda x: identity(seq, leaf_seq[x]))
            status, closest = "NOT_IN_TREE", f"{near} {tree.org(near)} {tree.acc(near)} ({identity(seq, leaf_seq[near]):.2f})"
        mp = pairwise_map(anchor_seq, seq)
        cells = [f"{seq[mp[p] - 1]}{mp[p]}" if p in mp else "-" for p in cols]
        out.append(f"{acc}\t{meta['gene'] or '-'}\t{len(seq)}\t{status}\t{closest}\t" + "\t".join(cells) + f"\t{meta['name']}")
    out.append("curated UniProt statements citing a publication (FUNCTION and CATALYTIC ACTIVITY, ECO:0000269):")
    for acc, text in records.items():
        for s in curated_statements(text):
            out.append(f"  {acc}: {s}")

    # --- annotations ---
    accs = sorted(set(tree_accs) | {m["id"] for m in members})
    rows: list[dict] = []
    for i in range(0, len(accs), 50):
        rows += quickgo({"geneProductId": ",".join(accs[i:i + 50])})
    out += ["", "## 5. GO annotations of tree leaves and reviewed members (QuickGO, live)",
            f"rows {len(rows)}; by evidence: " + ", ".join(f"{k}={v}" for k, v in sorted(Counter(r["goEvidence"] for r in rows).items())),
            "experimental rows (the query returns positives, so an absence below is a real absence in QuickGO):"]
    for r in rows:
        if r["goEvidence"] in EXPERIMENTAL:
            acc = r["geneProductId"].split(":")[1]
            where = tree_accs.get(acc, "not a tree leaf")
            out.append(f"  {acc} {r['symbol']} {r['qualifier']} {r['goId']} {r['goEvidence']} {r['reference']} {r['assignedBy']} ({where})")
    for row in paint_rows:
        node, term = row[1], row[2]
        below = {tree.acc(x) for x in tree.leaves(node)}
        iba = {r["geneProductId"].split(":")[1] for r in rows if r["goEvidence"] == "IBA" and r["goId"] == term}
        total = get_json(QUICKGO, {"goId": term, "limit": 1})["numberOfHits"]
        exp_below = sorted({r["geneProductId"].split(":")[1] for r in rows
                            if r["goId"] == term and r["goEvidence"] in EXPERIMENTAL and r["geneProductId"].split(":")[1] in below})
        out.append(f"{term} at {node}: QuickGO hits for the term overall {total}; leaves below node {len(below)}; "
                   f"IBA rows on family leaves {len(iba)}, of which below the node {len(iba & below)}, outside it {len(iba - below)}; "
                   f"leaves below the node with an experimental row for the term: {', '.join(exp_below) or 'none'}")
        grafts = Counter()
        for r in rows:
            if r["goId"] == term and r["reference"] == TREEGRAFTER_REF:
                for w in with_from(r):
                    if w.startswith("PANTHER:PTN"):
                        g = w.split(":")[1]
                        inside = "below the IBD node" if g in tree.nodes and node in tree.path(g) else "NOT below the IBD node"
                        grafts[f"{r['geneProductId'].split(':')[1]} grafted at {g} ({inside})"] += 1
        out.append(f"  TreeGrafter ({TREEGRAFTER_REF}) rows for {term}: {len(grafts)}")
        out += [f"    {k}" for k in sorted(grafts)]
    review = HERE / f"{FAMILY}-review.yaml"
    pmids = sorted(set(re.findall(r"^- id: PMID:(\d+)$", review.read_text(), flags=re.M)), key=int) if review.exists() else []
    if pmids:
        summary = get_json(PUBMED, {"db": "pubmed", "id": ",".join(pmids), "retmode": "json"})["result"]
        out += ["", "## 6. PubMed records of the PMIDs cited in the review (esummary, live)"]
        out += [f"PMID:{p} {summary[p]['pubdate'][:4]} {summary[p]['source']}: {summary[p]['title']}" for p in pmids]
    (HERE / f"{FAMILY}-tree-msa-check.txt").write_text("\n".join(out) + "\n")
    print(f"wrote {FAMILY}-tree-msa-check.txt ({len(out)} lines)", file=sys.stderr)


if __name__ == "__main__":
    main()
