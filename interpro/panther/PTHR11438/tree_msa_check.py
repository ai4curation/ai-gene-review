"""Tree and alignment check for this PANTHER family's PAINT rows.

Run from the repository root:

    uv run python interpro/panther/PTHR11438/tree_msa_check.py

The family is the name of the folder holding this script. Three inputs are fetched and
cached under the git-ignored ``.cache/panther_family_checks/<release>/``; none of them is
committed:

* the PANTHER tree (``treeinfo`` service; refused unless it serves the pinned
  ``PANTHER_RELEASE``), read here in full because the compact cache used by
  ``panther_trees.load_family`` drops internal-node event types and taxa;
* the PANTHER family alignment (``familymsa`` service), one row per tree leaf. Upper-case
  letters are HMM match columns and are the only residues treated as aligned; lower-case
  letters are insert states;
* the UniProt entries (sequence and feature table) of the human tree leaves, which serve
  as anchors, and the sequences of the other reviewed tree leaves, so that every position
  printed can be tied to a UniProt sequence version.

Outputs ``<FAMILY>-tree-msa-check.txt`` beside this script. Nothing about the result is
hard-coded: the opioid core is searched as the pattern below, anchors are whichever
leaves are human, and peptide and disulfide positions come from their UniProt features.
"""

from __future__ import annotations

import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

import requests

from ai_gene_review.etl.panther_families import PANTHER_RELEASE, same_release
from ai_gene_review.etl.panther_trees import served_release

HERE = Path(__file__).resolve().parent
FAMILY = HERE.name
CACHE = Path(".cache") / "panther_family_checks" / PANTHER_RELEASE
API = "https://pantherdb.org/services/oai/pantherdb"
UNIPROT = "https://rest.uniprot.org/uniprotkb"
# Opioid message core: Tyr-Gly-Gly-Phe, or the Phe-Gly-Gly-Phe of mammalian nociceptin,
# plus the fifth residue. Flanks are reported, not required.
CORE = re.compile(r"[YF]GGF[A-Z]")
BASIC = set("KR")


def cached_json(name: str, url: str, params: dict | None = None) -> dict:
    """Fetch a JSON document once and keep it in the git-ignored cache."""
    CACHE.mkdir(parents=True, exist_ok=True)
    path = CACHE / name
    if path.exists():
        return json.loads(path.read_text())
    r = requests.get(url, params=params, timeout=300, headers={"Accept": "application/json"})
    r.raise_for_status()
    data = r.json()
    path.write_text(json.dumps(data))
    return data


def children(node: dict) -> list[dict]:
    """Child nodes of a treeinfo node (the API returns a dict for a single child)."""
    ch = node.get("children", {}).get("annotation_node", [])
    return [ch] if isinstance(ch, dict) else ch


class Tree:
    """The full PANTHER tree: parent links, leaves below each node, clade labels."""

    def __init__(self, root: dict) -> None:
        self.nodes: dict[str, dict] = {}
        self.parent: dict[str, str] = {}
        self.kids: dict[str, list[str]] = {}
        self.below: dict[str, list[str]] = {}
        self.sf_root: dict[str, str] = {}
        self.root = root["persistent_id"]
        self._walk(root, None)

    def _walk(self, n: dict, sf: str | None) -> list[str]:
        pid = n["persistent_id"]
        self.nodes[pid] = n
        if n.get("sf_id"):
            sf = n["sf_id"]
        self.sf_root[pid] = sf or ""
        ks = children(n)
        self.kids[pid] = [k["persistent_id"] for k in ks]
        if not ks:
            self.below[pid] = [pid]
            return [pid]
        out: list[str] = []
        for k in ks:
            self.parent[k["persistent_id"]] = pid
            out.extend(self._walk(k, sf))
        self.below[pid] = out
        return out

    def is_leaf(self, pid: str) -> bool:
        return not self.kids[pid]

    def acc(self, leaf: str) -> str:
        return self.nodes[leaf]["node_name"].rsplit("UniProtKB=", 1)[-1]

    def org(self, leaf: str) -> str:
        return self.nodes[leaf]["node_name"].split("|", 1)[0]

    def label(self, pid: str) -> str:
        n = self.nodes[pid]
        if self.is_leaf(pid):
            return f"{self.org(pid)} {n.get('gene_symbol') or '-'} UniProtKB:{self.acc(pid)}"
        return f"[{n.get('event_type', '?')}] {n.get('species') or 'no taxon'}"

    def leaf_for_seed(self, seed: str) -> str | None:
        """Tree leaf named by a PAINT seed id (MOD id or UniProtKB accession)."""
        db, _, ident = seed.partition(":")
        for leaf in self.below[self.root]:
            name = self.nodes[leaf]["node_name"]
            if db == "UniProtKB" and name.endswith(f"UniProtKB={ident}"):
                return leaf
            if f"|{db}={ident}|" in name or f"|{db}={ident.replace(':', '=')}|" in name:
                return leaf
        return None

    def child_holding(self, node: str, leaf: str) -> str | None:
        for k in self.kids[node]:
            if leaf in self.below[k]:
                return k
        return None


def ungapped(row: str) -> str:
    return re.sub(r"[.\-]", "", row).upper()


def col_of_position(row: str) -> dict[int, tuple[int, bool]]:
    """Map 1-based sequence positions to (alignment column, is HMM match column)."""
    out: dict[int, tuple[int, bool]] = {}
    pos = 0
    for col, ch in enumerate(row):
        if ch.isalpha():
            pos += 1
            out[pos] = (col, ch.isupper())
    return out


def pos_at_column(row: str, col: int) -> int | None:
    """1-based sequence position of the residue at an alignment column, if any."""
    if not row[col].isalpha():
        return None
    return sum(c.isalpha() for c in row[: col + 1])


def cores(seq: str) -> list[tuple[int, str, str, str]]:
    """Every opioid core in a sequence: (1-based start, two residues before, core, three after)."""
    return [
        (m.start() + 1, seq[max(0, m.start() - 2) : m.start()], m.group(), seq[m.end() : m.end() + 3])
        for m in CORE.finditer(seq)
    ]


def fmt_core(c: tuple[int, str, str, str]) -> str:
    start, before, core, after = c
    dibasic = "dibasic" if len(before) == 2 and set(before) <= BASIC else "NOT-dibasic"
    return f"{before.lower()}|{core}|{after.lower()}@{start}({dibasic})"


def features(entry: dict, kinds: tuple[str, ...]) -> list[tuple[str, int, int, str]]:
    out = []
    for f in entry.get("features", []):
        if f["type"] in kinds:
            loc = f["location"]
            if loc["start"].get("value") and loc["end"].get("value"):
                out.append((f["type"], loc["start"]["value"], loc["end"]["value"], f.get("description", "")))
    return out


def main() -> None:
    """Write the tree and alignment report for FAMILY."""
    payload = cached_json(f"{FAMILY}.treeinfo.json", f"{API}/treeinfo", {"family": FAMILY})
    served = served_release(payload)
    if served is None or not same_release(served, PANTHER_RELEASE):
        raise SystemExit(f"PANTHER API serves release {served}, repo pinned to {PANTHER_RELEASE}")
    tree = Tree(payload["search"]["tree_topology"]["annotation_node"])
    msa_payload = cached_json(f"{FAMILY}.familymsa.json", f"{API}/familymsa", {"family": FAMILY})
    rows = {s["persistent_id"]: s["sequence"] for s in msa_payload["search"]["MSA_list"]["sequence_info"]}
    leaves = tree.below[tree.root]
    out: list[str] = []
    w = out.append

    w(f"# {FAMILY} tree and alignment check (PANTHER {served}; generated by tree_msa_check.py)")
    w(f"tree: {len(leaves)} leaves, {len(tree.nodes) - len(leaves)} internal nodes; "
      f"alignment rows {len(rows)}, of which tree leaves {sum(x in rows for x in leaves)}; "
      f"alignment length {len(next(iter(rows.values())))} columns")
    w("")

    # ---- 1. topology: subfamily roots, duplications, taxa -----------------------------
    w("## 1. Topology")
    root = tree.nodes[tree.root]
    w(f"root {tree.root} {tree.label(tree.root)}; children: "
      + "; ".join(f"{k} {tree.label(k)} sf={tree.nodes[k].get('sf_id', '-')} "
                  f"{tree.nodes[k].get('sf_name', '')} leaves={len(tree.below[k])}" for k in tree.kids[tree.root]))
    w(f"root taxonomic_range attribute: {root.get('taxonomic_range', '-')}")
    for pid, n in tree.nodes.items():
        if n.get("sf_id"):
            orgs = Counter(tree.org(x) for x in tree.below[pid])
            w(f"subfamily root {n['sf_id']} ({n.get('sf_name', '')}) at {pid} {tree.label(pid)}: "
              f"{len(tree.below[pid])} leaves; " + " ".join(f"{o}={c}" for o, c in sorted(orgs.items())))
    for pid, n in tree.nodes.items():
        if not tree.is_leaf(pid) and n.get("event_type") == "DUPLICATION":
            w(f"duplication {pid} (within {tree.sf_root[pid] or 'family root'}): "
              + " | ".join(f"{k} {tree.label(k)} leaves={len(tree.below[k])}" for k in tree.kids[pid]))
    w("")

    # ---- 2. PAINT rows: clade below each node and where the seeds sit ------------------
    w("## 2. PAINT rows mapped onto the tree")
    with (HERE / f"{FAMILY}-paint.tsv").open() as fh:
        paint = [r for r in csv.reader(fh, delimiter="\t") if len(r) > 6 and r[1].startswith("PTN")]
    for r in paint:
        node, term, aspect, ev, neg, seeds, date = r[1], r[2], r[3], r[4], r[5], r[6], r[-1]
        if node not in tree.nodes:
            w(f"{ev} {node} {term}: NODE NOT IN TREE")
            continue
        sf = Counter(tree.sf_root[x] for x in tree.below[node])
        w(f"{ev} {node} {term} ({aspect}) negated={neg} date={date}: {tree.label(node)}; "
          f"{len(tree.below[node])} leaves; " + ", ".join(f"{k}={v}" for k, v in sorted(sf.items())))
        for seed in filter(None, seeds.split("|")):
            leaf = tree.leaf_for_seed(seed)
            if leaf is None:
                w(f"    seed {seed}: no tree leaf carries this id (not resolved from the tree)")
            elif leaf not in tree.below[node]:
                w(f"    seed {seed}: leaf {leaf} {tree.label(leaf)} is OUTSIDE the node's clade")
            else:
                child = tree.child_holding(node, leaf)
                where = f"child clade {child} {tree.label(child)} sf={tree.sf_root[child]}" if child else "the node itself"
                w(f"    seed {seed}: leaf {leaf} {tree.label(leaf)} in {where}")
        seeded = {tree.child_holding(node, lf) for lf in map(tree.leaf_for_seed, filter(None, seeds.split("|"))) if lf}
        unseeded = [k for k in tree.kids[node] if k not in seeded]
        if unseeded:
            w("    child clades with no resolved seed: "
              + "; ".join(f"{k} {tree.label(k)} sf={tree.sf_root[k]} leaves={len(tree.below[k])}" for k in unseeded))
    w("")

    # ---- 3. reviewed members: tree leaf or not, alignment sequence vs UniProt ----------
    w("## 3. Reviewed (Swiss-Prot) members and sequence identity with UniProt")
    acc_leaf = {tree.acc(x): x for x in leaves}
    entries: dict[str, dict] = {}
    with (HERE / f"{FAMILY}-entries.csv").open() as fh:
        members = list(csv.DictReader(fh))
    for m in members:
        acc = m["id"]
        if acc not in acc_leaf:
            w(f"{acc} {m['gene'] or '-'} {m['source_tax_name']} {m['subfamily']} length {m['length']}: NOT a tree leaf")
            continue
        entry = cached_json(f"uniprot-{acc}.json", f"{UNIPROT}/{acc}.json")
        entries[acc] = entry
        same = entry["sequence"]["value"] == ungapped(rows[acc_leaf[acc]])
        w(f"{acc} {m['gene'] or '-'} {m['source_tax_name']} {m['subfamily']}: tree leaf {acc_leaf[acc]}; "
          f"UniProt length {entry['sequence']['length']} sequence version {entry['entryAudit']['sequenceVersion']}; "
          f"alignment row identical to UniProt sequence: {same}")
    w("")

    # ---- 4. opioid cores per leaf -----------------------------------------------------
    w("## 4. Opioid cores ([YF]GGF + 1) in every tree leaf, numbered on the alignment row's own sequence")
    w("format: two residues before | core | three after @ start (dibasic = both preceding residues K/R)")
    summary: dict[str, list[tuple[str, int, int, int]]] = defaultdict(list)
    for leaf in leaves:
        seq = ungapped(rows[leaf])
        cs = cores(seq)
        ny = sum(c[2][0] == "Y" for c in cs)
        nf = sum(c[2][0] == "F" for c in cs)
        nd = sum(len(c[1]) == 2 and set(c[1]) <= BASIC for c in cs)
        summary[tree.sf_root[leaf]].append((tree.org(leaf), ny, nf, nd))
        fifth = Counter(c[2][4] for c in cs if c[2][0] == "Y")
        w(f"{tree.sf_root[leaf]} {tree.org(leaf)} {tree.acc(leaf)} len={len(seq)} Y-cores={ny} F-cores={nf} "
          f"fifth-residue-of-Y-cores={dict(sorted(fifth.items()))}: " + " ".join(fmt_core(c) for c in cs))
    w("")
    w("summary per subfamily root (leaves; range of Y-core and F-core counts; leaves with every core dibasic-preceded):")
    for sf, items in sorted(summary.items()):
        ys = [i[1] for i in items]
        fs = [i[2] for i in items]
        alld = sum(i[3] == i[1] + i[2] for i in items)
        w(f"  {sf}: {len(items)} leaves; Y-cores {min(ys)}-{max(ys)}; F-cores {min(fs)}-{max(fs)}; "
          f"all cores dibasic-preceded in {alld}/{len(items)}; leaves with no Y-core: "
          + (", ".join(i[0] for i in items if i[1] == 0) or "none"))
    w("")

    # ---- 5. anchor features projected through the alignment ---------------------------
    w("## 5. UniProt features of the human leaves projected through the alignment")
    w("Residues are read at the alignment column of the anchor position; lower case = insert state "
      "(not an aligned column), '-' = gap. Counts are over the leaves of the anchor's own subfamily clade "
      "unless stated.")
    humans = [x for x in leaves if tree.org(x) == "HUMAN"]
    for h in humans:
        acc = tree.acc(h)
        entry = entries.get(acc) or cached_json(f"uniprot-{acc}.json", f"{UNIPROT}/{acc}.json")
        useq = entry["sequence"]["value"]
        if useq != ungapped(rows[h]):
            w(f"anchor {acc}: alignment row differs from UniProt sequence; features not projected")
            continue
        colmap = col_of_position(rows[h])
        # clade = the child of the family root holding this leaf
        clade_root = tree.child_holding(tree.root, h) or tree.root
        clade = tree.below[clade_root]
        gene = entry.get("genes", [{}])[0].get("geneName", {}).get("value", "")
        w(f"### anchor UniProtKB:{acc} ({gene}, human, sequence version "
          f"{entry['entryAudit']['sequenceVersion']}, length {len(useq)}); clade {clade_root} "
          f"{tree.nodes[clade_root].get('sf_id', '')} with {len(clade)} leaves")
        for kind, s, e, desc in features(entry, ("Disulfide bond",)):
            for p in (s, e):
                col, match = colmap[p]
                fam = Counter(rows[x][col] for x in leaves)
                w(f"  disulfide Cys{p} ({s}-{e}) column {col} match={match}: anchor {useq[p - 1]}; "
                  f"all {len(leaves)} leaves: " + " ".join(f"{k}={v}" for k, v in fam.most_common()))
        for kind, s, e, desc in features(entry, ("Peptide",)):
            seg = useq[s - 1 : e]
            n5 = seg[:5]
            before = useq[max(0, s - 3) : s - 1]
            after = useq[e : e + 2]
            w(f"  peptide {desc or '?'} {s}-{e} {seg if len(seg) <= 40 else seg[:37] + '...'} "
              f"(preceded by {before}, followed by {after})")
            cols = [colmap[p] for p in range(s, min(e, s + 4) + 1)]
            variants: Counter = Counter()
            per_leaf: list[str] = []
            for x in clade:
                frag = "".join(rows[x][c] if rows[x][c].isalpha() else "-" for c, _ in cols)
                variants[frag] += 1
                per_leaf.append(f"{tree.org(x)}:{frag}")
            w(f"    first {len(cols)} residues ({n5}) at columns {[c for c, _ in cols]} "
              f"(match columns: {all(m for _, m in cols)}); variants in clade: "
              + " ".join(f"{k}={v}" for k, v in variants.most_common()))
            if len(variants) > 1 and e - s + 1 <= 5:
                w("    per leaf: " + " ".join(per_leaf))
            if e - s + 1 <= 40 and e - s + 1 > 5:
                # whole-peptide identity to the anchor over the anchor's columns
                pcols = [colmap[p] for p in range(s, e + 1)]
                idents = []
                for x in clade:
                    frag = "".join(rows[x][c] if rows[x][c].isalpha() else "-" for c, _ in pcols)
                    ident = sum(a.upper() == b for a, b in zip(frag, seg))
                    idents.append(f"{tree.org(x)}:{frag}({ident}/{len(seg)})")
                w("    whole peptide, anchor columns, identities to anchor: " + " ".join(idents))
        w("")

    (HERE / f"{FAMILY}-tree-msa-check.txt").write_text("\n".join(out) + "\n")
    print(f"wrote {FAMILY}-tree-msa-check.txt ({len(out)} lines)")


if __name__ == "__main__":
    main()
