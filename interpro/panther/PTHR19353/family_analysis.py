"""Tree and alignment check for this PANTHER family's PAINT assertions.

Run from the repository root:

    uv run python interpro/panther/PTHR19353/family_analysis.py

The family is the name of the folder holding this script. Two PANTHER API payloads
are fetched (and cached, git-ignored, under ``.cache/panther_family_analysis/``):

* ``treeinfo``  - the family tree with event types (speciation, duplication,
  horizontal transfer), taxon labels and leaf identifiers;
* ``familymsa`` - PANTHER's own family alignment, one row per tree node.

Both must report the repo's pinned ``PANTHER_RELEASE``; otherwise the script stops.

What is reported (``<FAMILY>-analysis.txt``):

1. the tree outline down to clades of at most ``OUTLINE_MIN`` leaves, with event
   type, taxon, leaf count, leaf subfamilies and taxonomic composition;
2. every PAINT row of ``<FAMILY>-paint.tsv`` mapped onto the tree: leaves below the
   node, and for every seed the leaf it resolves to and its path from the root;
3. motif conservation read from the alignment (and every leaf, with its motifs,
   of the top-level clades of at most ``SMALL_CLADE`` leaves). The motif columns are located on a
   reference row (``MOTIF_REFERENCE``) by regular expression, and every other row
   is read at the same alignment columns, so each motif statement refers to the
   reference numbering given in the report. Rows are then summarised per top-level
   clade and per subfamily, and every leaf deviating from the motif class is listed;
4. experimental GO annotations of every tree leaf (QuickGO, queried by gene
   product and evidence class, never by term name), grouped by top-level clade,
   with the leaves that carry each PAINT term or one of its descendants;
5. the reviewed (Swiss-Prot) members of ``<FAMILY>-entries.csv`` with their leaf,
   top-level clade and motif strings, or NOT_IN_TREE.

Nothing about the result is hard-coded: the reference accession and the motif
patterns are method parameters, and the report says so when a pattern does not
match the reference.
"""

from __future__ import annotations

import csv
import gzip
import json
import re
import sys
from collections import Counter
from pathlib import Path

import requests

from ai_gene_review.etl.panther_families import PANTHER_RELEASE, same_release

HERE = Path(__file__).resolve().parent
FAMILY = HERE.name
CACHE = Path(".cache") / "panther_family_analysis" / PANTHER_RELEASE
API = "https://pantherdb.org/services/oai/pantherdb/"
OUTLINE_MIN = 20
SMALL_CLADE = 20
QUICKGO = "https://www.ebi.ac.uk/QuickGO/services/"
UNIPROT = "https://rest.uniprot.org/uniprotkb/search"

# Motif columns are located on this row of the PANTHER alignment.
MOTIF_REFERENCE = "O95864"  # human FADS2, the Swiss-Prot entry the family is named after
# name -> (regex on the ungapped reference, class each aligned row is tested against)
MOTIFS = {
    "cytb5_HPGG": (r"HPGG", r"HPGG"),
    "His_box_1": (r"H[A-Z]{3}H(?=.{20,45}H[A-Z]{2}HH)", r"H...H"),
    "His_box_2": (r"H[A-Z]{2}HH(?=.{100,220}[QH][A-Z]{2}HH)", r"H..HH"),
    "His_box_3": (r"[QH][A-Z]{2}HH(?!.*[QH][A-Z]{2}HH)", r"[QH]..HH"),
}
# A second, independent anchor: these rows have their own motifs searched without
# reference to the alignment, to confirm the alignment columns are the true boxes.
SELF_CHECK = ["O34653", "P9WNZ3", "O60427", "Q8N9I5", "Q39982", "A0A0H3C677"]


def fetch(service: str) -> dict:
    """Return a PANTHER API payload for FAMILY from the cache or the service."""
    CACHE.mkdir(parents=True, exist_ok=True)
    path = CACHE / f"{FAMILY}-{service}.json.gz"
    if path.exists():
        with gzip.open(path, "rt") as fh:
            return json.load(fh)
    r = requests.get(API + service, params={"family": FAMILY}, timeout=300)
    r.raise_for_status()
    payload = r.json()
    version = str(payload.get("search", {}).get("product", {}).get("version", ""))
    if not same_release(version, PANTHER_RELEASE):
        raise SystemExit(f"{service}: PANTHER serves {version!r}, repo pinned to {PANTHER_RELEASE}")
    with gzip.open(path, "wt") as fh:
        json.dump(payload, fh)
    return payload


def kids(node: dict) -> list[dict]:
    """Child nodes (the API returns a dict for a single child)."""
    ch = node.get("children", {}).get("annotation_node", [])
    return [ch] if isinstance(ch, dict) else ch


class Tree:
    """Parent, leaf and path lookups over a treeinfo payload."""

    def __init__(self, payload: dict) -> None:
        self.root = payload["search"]["tree_topology"]["annotation_node"]
        self.node: dict[str, dict] = {}
        self.parent: dict[str, str] = {}
        self.below: dict[str, list[str]] = {}
        sys.setrecursionlimit(100000)
        self._walk(self.root)
        self.by_acc: dict[str, str] = {}
        self.by_gene: dict[str, str] = {}
        for pid in self.below[self.root["persistent_id"]]:
            n = self.node[pid]
            for tok in n.get("node_name", "").split("|"):
                if tok.startswith("UniProtKB="):
                    self.by_acc[tok[10:]] = pid
                elif "=" in tok:
                    self.by_gene[tok.split("=", 1)[1]] = pid
            if n.get("gene_id"):
                self.by_gene[n["gene_id"].split(":", 1)[-1]] = pid

    def _walk(self, n: dict) -> list[str]:
        pid = n["persistent_id"]
        self.node[pid] = n
        ch = kids(n)
        if not ch:
            self.below[pid] = [pid]
            return [pid]
        out: list[str] = []
        for c in ch:
            self.parent[c["persistent_id"]] = pid
            out.extend(self._walk(c))
        self.below[pid] = out
        return out

    def is_leaf(self, pid: str) -> bool:
        return not kids(self.node[pid])

    def path(self, pid: str) -> list[str]:
        """Node ids from the root down to ``pid``."""
        out = [pid]
        while out[-1] in self.parent:
            out.append(self.parent[out[-1]])
        return out[::-1]

    def acc(self, pid: str) -> str:
        for tok in self.node[pid].get("node_name", "").split("|"):
            if tok.startswith("UniProtKB="):
                return tok[10:]
        return ""

    def org(self, pid: str) -> str:
        return self.node[pid].get("node_name", "").split("|")[0]

    def sf(self, pid: str) -> str:
        n = self.node[pid]
        return (n.get("sf_id") or n.get("prop_sf_id") or "").split(":")[-1]

    def describe(self, pid: str) -> str:
        n = self.node[pid]
        if self.is_leaf(pid):
            return (f"{pid} leaf {self.org(pid)} UniProtKB:{self.acc(pid)} "
                    f"{n.get('gene_symbol') or '-'} {self.sf(pid)} [{n.get('definition', '')}]")
        ls = self.below[pid]
        sf = Counter(self.sf(x) for x in ls)
        orgs = Counter(self.org(x) for x in ls)
        return (f"{pid} {n.get('event_type', '?')} {n.get('species', '') or '-'} leaves={len(ls)} "
                f"species={len(orgs)} subfamilies: "
                + ", ".join(f"{k}={v}" for k, v in sf.most_common()))


def resolve_seed(tree: Tree, seed: str) -> str | None:
    """Leaf PTN for a PAINT seed id (``UniProtKB:ACC`` or a MOD gene id), if in the tree."""
    db, _, local = seed.partition(":")
    if db == "UniProtKB":
        return tree.by_acc.get(local)
    for key in (local, local.split(":")[-1], local.replace(":", "=")):
        if key in tree.by_gene:
            return tree.by_gene[key]
    # e.g. an AGI locus code, which the tree does not carry: ask UniProt which
    # accessions carry the identifier and keep the one that is a leaf of this tree.
    try:
        r = requests.get(UNIPROT, params={"query": local.split(":")[-1], "fields": "accession",
                                          "format": "tsv", "size": 25}, timeout=60)
        r.raise_for_status()
    except requests.RequestException:
        return None
    hits = [a for a in r.text.split()[1:] if a in tree.by_acc]
    return tree.by_acc[hits[0]] if len(hits) == 1 else None


def experimental_annotations(accessions: list[str]) -> tuple[list[dict], dict[str, str]]:
    """Experimental GO annotations (ECO:0000269 and descendants) from QuickGO, with term names.

    The query is by gene product and evidence only (no term-name filter), so a clean
    absence cannot come from a filter on a field the service leaves empty.
    """
    rows: list[dict] = []
    for i in range(0, len(accessions), 100):
        page = 1
        while True:
            r = requests.get(QUICKGO + "annotation/search", params={
                "geneProductId": ",".join(accessions[i:i + 100]),
                "evidenceCode": "ECO:0000269", "evidenceCodeUsage": "descendants",
                "limit": 200, "page": page}, headers={"Accept": "application/json"}, timeout=120)
            r.raise_for_status()
            d = r.json()
            rows.extend(d["results"])
            if page >= d["pageInfo"]["total"]:
                break
            page += 1
    names: dict[str, str] = {}
    ids = sorted({x["goId"] for x in rows})
    for i in range(0, len(ids), 50):
        r = requests.get(QUICKGO + "ontology/go/terms/" + ",".join(ids[i:i + 50]),
                         headers={"Accept": "application/json"}, timeout=120)
        r.raise_for_status()
        names.update({t["id"]: t["name"] for t in r.json()["results"]})
    return rows, names


def descendants(term: str) -> set[str]:
    """``term`` and its is_a/part_of descendants, from QuickGO."""
    r = requests.get(QUICKGO + f"ontology/go/terms/{term}/descendants",
                     params={"relations": "is_a,part_of"}, headers={"Accept": "application/json"},
                     timeout=120)
    r.raise_for_status()
    return {term, *r.json()["results"][0].get("descendants", [])}


def motif_columns(ref_row: str) -> tuple[dict[str, tuple[int, list[int]]], list[str]]:
    """Locate each motif on the reference row: name -> (1-based start, alignment columns)."""
    cols = [i for i, c in enumerate(ref_row) if c not in ".-"]
    ungapped = "".join(ref_row[i] for i in cols).upper()
    found: dict[str, tuple[int, list[int]]] = {}
    problems: list[str] = []
    for name, (pattern, _) in MOTIFS.items():
        hits = list(re.finditer(pattern, ungapped))
        if len(hits) != 1:
            problems.append(f"{name}: pattern {pattern} matched {len(hits)} times on reference")
            continue
        h = hits[0]
        found[name] = (h.start() + 1, cols[h.start():h.end()])
    return found, problems


def read_motif(row: str, cols: list[int]) -> str:
    """Residues of ``row`` at alignment columns (gap shown as '-')."""
    return "".join(row[c].upper() if row[c].isalpha() else "-" for c in cols)


def main() -> None:
    tree = Tree(fetch("treeinfo"))
    msa = {x["persistent_id"]: x["sequence"]
           for x in fetch("familymsa")["search"]["MSA_list"]["sequence_info"]}
    root = tree.root["persistent_id"]
    leaves = tree.below[root]
    out: list[str] = [
        f"PANTHER release {PANTHER_RELEASE}; family {FAMILY}; root {root}; "
        f"leaves {len(leaves)}; alignment rows {len(msa)}; "
        f"alignment columns {len(next(iter(msa.values())))}; "
        f"leaves with an alignment row {sum(x in msa for x in leaves)}",
        "",
        "== 1. Tree outline ==",
    ]

    def outline(pid: str, depth: int) -> None:
        out.append("  " * depth + tree.describe(pid))
        if not tree.is_leaf(pid) and len(tree.below[pid]) > OUTLINE_MIN:
            for c in kids(tree.node[pid]):
                outline(c["persistent_id"], depth + 1)

    outline(root, 0)
    events = Counter(tree.node[p].get("event_type", "LEAF") for p in tree.node if not tree.is_leaf(p))
    out.append("internal node events: " + ", ".join(f"{k}={v}" for k, v in events.most_common()))

    # Top-level clades: the children of the first duplication reached from the root
    # on the larger side, plus the remaining root children.  Used only as labels.
    top: dict[str, str] = {}

    def assign_top(pid: str) -> None:
        for c in kids(tree.node[pid]):
            cid = c["persistent_id"]
            ev = c.get("event_type", "")
            if not tree.is_leaf(cid) and ev != "SPECIATION" and len(tree.below[cid]) > 50:
                assign_top(cid)
            else:
                for leaf in tree.below[cid]:
                    top[leaf] = cid

    assign_top(root)
    out += ["", "== 2. PAINT rows on the tree =="]
    paint = HERE / f"{FAMILY}-paint.tsv"
    with paint.open() as fh:
        for row in csv.reader(fh, delimiter="\t"):
            if len(row) < 7 or not row[1].startswith("PTN"):
                continue
            node, term, aspect, evidence, negated, seeds = row[1:7]
            below = tree.below.get(node, [])
            out.append(f"{evidence} {node} {term} {aspect} negated={negated} date={row[8]}: "
                       f"{tree.describe(node) if node in tree.node else 'NODE NOT IN TREE'}")
            hit_tops = Counter()
            for seed in filter(None, seeds.split("|")):
                leaf = resolve_seed(tree, seed)
                if leaf is None:
                    out.append(f"  seed {seed}: NOT RESOLVED to a tree leaf")
                    continue
                inside = "below node" if leaf in below else "OUTSIDE node"
                hit_tops[top.get(leaf, "?")] += 1
                out.append(f"  seed {seed}: {tree.describe(leaf)}; {inside}; "
                           f"top clade {top.get(leaf, '?')}; path {' > '.join(tree.path(leaf)[:-1])}")
            all_tops = Counter(top.get(x, "?") for x in below)
            out.append("  top clades below node with / without a seed: " + ", ".join(
                f"{k}(leaves={v},seeds={hit_tops.get(k, 0)})" for k, v in all_tops.most_common()))

    out += ["", "== 3. Motifs in the PANTHER alignment =="]
    ref_leaf = tree.by_acc.get(MOTIF_REFERENCE)
    if ref_leaf is None or ref_leaf not in msa:
        out.append(f"reference {MOTIF_REFERENCE} has no alignment row; motif analysis not done")
        located: dict[str, tuple[int, list[int]]] = {}
    else:
        located, problems = motif_columns(msa[ref_leaf])
        out += [f"PROBLEM {p}" for p in problems]
        for name, (start, cols) in located.items():
            out.append(f"{name}: UniProtKB:{MOTIF_REFERENCE} residues {start}-{start + len(cols) - 1} "
                       f"= {read_motif(msa[ref_leaf], cols)}; test class {MOTIFS[name][1]}")
    names = list(located)
    motif_of = {leaf: {n: read_motif(msa[leaf], located[n][1]) for n in names}
                for leaf in leaves if leaf in msa}

    def ok(leaf: str, name: str) -> bool:
        return re.fullmatch(MOTIFS[name][1], motif_of[leaf][name]) is not None

    out.append("-- self-check: motifs searched on the ungapped sequence, not by column --")
    for acc in SELF_CHECK:
        leaf = tree.by_acc.get(acc)
        if leaf is None or leaf not in msa:
            out.append(f"  {acc}: no alignment row")
            continue
        seq = "".join(c for c in msa[leaf] if c.isalpha()).upper()
        own = {n: [(m.start() + 1, m.group()) for m in re.finditer(MOTIFS[n][1], seq)] for n in names}
        out.append(f"  {acc} (alignment-row length {len(seq)}): by column "
                   + ", ".join(f"{n}={motif_of[leaf][n]}" for n in names))
        for n in names:
            col_motif = motif_of[leaf][n]
            agree = [p for p, s in own[n] if s == col_motif]
            out.append(f"    {n}: own matches {own[n][:8]}; column motif found at own position {agree or 'none'}")

    def summarise(label: str, group: list[str]) -> None:
        group = [x for x in group if x in motif_of]
        parts = []
        for n in names:
            c = Counter(motif_of[x][n] for x in group)
            good = sum(ok(x, n) for x in group)
            parts.append(f"{n} {good}/{len(group)} [{', '.join(f'{k}:{v}' for k, v in c.most_common(4))}]")
        out.append(f"  {label}: " + "; ".join(parts))

    out.append("-- per top-level clade --")
    for cid in dict.fromkeys(top[x] for x in leaves):
        summarise(tree.describe(cid), [x for x in leaves if top[x] == cid])
    out.append("-- per subfamily --")
    for sf in sorted({tree.sf(x) for x in leaves}, key=lambda s: (len(s), s)):
        group = [x for x in leaves if tree.sf(x) == sf]
        name = tree.node[group[0]].get("sf_name", "")
        orgs = Counter(tree.org(x) for x in group)
        summarise(f"{sf} {name} (leaves={len(group)}, species={len(orgs)}, "
                  f"top clades {sorted({top[x] for x in group})})", group)
    out.append("-- leaves deviating from a motif class (His boxes; cytb5 listed per clade above) --")
    his = [n for n in names if n.startswith("His")]
    for leaf in leaves:
        if leaf in motif_of and not all(ok(leaf, n) for n in his):
            out.append(f"  {tree.describe(leaf)}: "
                       + ", ".join(f"{n}={motif_of[leaf][n]}" for n in names)
                       + f"; top clade {top[leaf]}")
    if "cytb5_HPGG" in located:
        out.append("-- leaves lacking the cytochrome b5 HPGG motif at the reference columns --")
        for cid in dict.fromkeys(top[x] for x in leaves):
            lacking = [x for x in leaves if top[x] == cid and x in motif_of and not ok(x, "cytb5_HPGG")]
            total = sum(top[x] == cid for x in leaves)
            out.append(f"  top clade {cid}: {len(lacking)}/{total} lack HPGG"
                       + ("" if len(lacking) in (0, total) else ": " + "; ".join(
                           f"{tree.org(x)}:{tree.acc(x)}({tree.sf(x)},{motif_of[x]['cytb5_HPGG']})"
                           for x in lacking)))

        out.append("-- HPGG anywhere N-terminal of His box 1 (ungapped row; catches column shifts) --")
        for cid in dict.fromkeys(top[x] for x in leaves):
            group = [x for x in leaves if top[x] == cid and x in msa]
            n_any = 0
            shifted = []
            for x in group:
                box1 = located["His_box_1"][1][0] if "His_box_1" in located else len(msa[x])
                nterm = "".join(c for c in msa[x][:box1] if c.isalpha()).upper()
                if "HPGG" in nterm:
                    n_any += 1
                    if not ok(x, "cytb5_HPGG"):
                        shifted.append(f"{tree.org(x)}:{tree.acc(x)}")
            out.append(f"  top clade {cid}: {n_any}/{len(group)} have HPGG N-terminal of box 1"
                       + (f"; of these not at the reference columns: {', '.join(shifted)}" if shifted else ""))

    out.append(f"-- every leaf of the top-level clades with at most {SMALL_CLADE} leaves --")
    for cid in dict.fromkeys(top[x] for x in leaves):
        group = [x for x in leaves if top[x] == cid]
        if len(group) > SMALL_CLADE:
            continue
        for x in group:
            motifs = ", ".join(f"{n}={motif_of[x][n]}" for n in names) if x in motif_of else "no row"
            out.append(f"  top clade {cid}: {tree.describe(x)}; parent {tree.parent.get(x, '-')}; {motifs}")

    out += ["", "== 4. Experimental GO annotations of tree leaves (QuickGO) =="]
    accs = sorted({tree.acc(x) for x in leaves if tree.acc(x)})
    rows, go_names = experimental_annotations(accs)
    out.append(f"leaf accessions queried {len(accs)}; experimental annotation rows returned {len(rows)} "
               f"on {len({r['geneProductId'] for r in rows})} leaves "
               "(a zero here would mean the query, not the family, is at fault)")
    paint_terms = []
    with paint.open() as fh:
        paint_terms = sorted({row[2] for row in csv.reader(fh, delimiter="\t")
                              if len(row) > 2 and row[2].startswith("GO:")})
    under = {t: descendants(t) for t in paint_terms}
    per_leaf: dict[str, set[tuple[str, str, str, str]]] = {}
    for r in rows:
        per_leaf.setdefault(r["geneProductId"].split(":")[-1], set()).add(
            (r["goAspect"][0].upper(), r["goId"], r["goEvidence"], r["qualifier"]))
    for cid in dict.fromkeys(top[x] for x in leaves):
        group = [x for x in leaves if top[x] == cid]
        out.append(f"top clade {tree.describe(cid)}")
        for t in paint_terms:
            have = [x for x in group if any(g in under[t] and not q.startswith("NOT")
                                            for _, g, _, q in per_leaf.get(tree.acc(x), ()))]
            out.append(f"  leaves with an experimental annotation to {t} or a descendant: {len(have)}/{len(group)}"
                       + (": " + ", ".join(f"{tree.org(x)}:{tree.acc(x)}" for x in have) if have else ""))
        for x in group:
            anns = per_leaf.get(tree.acc(x))
            if not anns:
                continue
            n = tree.node[x]
            out.append(f"  {tree.org(x)} UniProtKB:{tree.acc(x)} {n.get('gene_symbol') or '-'} {tree.sf(x)}")
            for aspect, go, ev, qual in sorted(anns):
                if go == "GO:0005515":
                    continue
                flags = [t for t in paint_terms if go in under[t]]
                out.append(f"    {aspect} {go} {go_names.get(go, '?')} {ev} {qual}"
                           + (f" [under {','.join(flags)}]" if flags else ""))

    out += ["", "== 5. Reviewed members =="]
    with (HERE / f"{FAMILY}-entries.csv").open() as fh:
        members = list(csv.DictReader(fh))
    out.append(f"reviewed members {len(members)}; tree leaves among them "
               f"{sum(m['id'] in tree.by_acc for m in members)}")
    for m in members:
        leaf = tree.by_acc.get(m["id"])
        if leaf is None:
            out.append(f"member {m['id']} {m['gene'] or '-'} {m['subfamily'] or '-'} len {m['length']} "
                       f"NOT_IN_TREE: {m['name']} ({m['source_tax_name']})")
            continue
        motifs = ", ".join(f"{n}={motif_of[leaf][n]}" for n in names) if leaf in motif_of else "no row"
        out.append(f"member {m['id']} {m['gene'] or '-'} entries-subfamily {m['subfamily'] or '-'} "
                   f"tree-subfamily {tree.sf(leaf)} len {m['length']} leaf {leaf} top clade {top[leaf]}: "
                   f"{m['name']} ({m['source_tax_name']}); {motifs}")

    (HERE / f"{FAMILY}-analysis.txt").write_text("\n".join(out) + "\n")
    print(f"wrote {FAMILY}-analysis.txt ({len(out)} lines)")


if __name__ == "__main__":
    main()
