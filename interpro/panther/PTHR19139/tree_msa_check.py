"""Tree, alignment and experimental-annotation check for this PANTHER family.

Run from the repository root:

    uv run python interpro/panther/PTHR19139/tree_msa_check.py

The family is the name of the folder holding this script. Three public sources are
fetched (and cached, raw, under the git-ignored ``.cache/panther_family_review/``):

* the PANTHER ``treeinfo`` service (full topology with event types and taxon labels);
  the served release must equal the repository's pinned ``PANTHER_RELEASE``;
* the PANTHER ``familymsa`` service (the family's own alignment, one row per tree leaf);
* QuickGO, for experimental (ECO:0000269 and descendants) annotations of the tree leaves
  to each PAINT term and its descendants, and for every experimental annotation of the
  leaves below a PAINT loss node.

PAINT rows are read from ``<FAMILY>-paint.tsv``. For rows whose node is not in this
family's tree, the other cached PAINT slices under ``interpro/panther/`` are scanned for
the same node and the tree of each such family is loaded to see where the node sits.

Residue sites are defined in ``SITES`` by anchor protein and anchor residue numbering.
The anchor row of the PANTHER alignment is compared with the UniProt sequence before any
number is used, each anchor residue is read from the alignment (never assumed), and the
aligned residues of every leaf are tabulated per PANTHER subfamily and per PAINT node.
Nothing about the result is hard-coded. Output: ``<FAMILY>-tree-msa-check.txt``.
"""

from __future__ import annotations

import csv
import json
import re
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path

import requests

from ai_gene_review.etl.panther_families import PANTHER_RELEASE, same_release
from ai_gene_review.etl.panther_trees import leaves_below, load_family

HERE = Path(__file__).resolve().parent
FAMILY = HERE.name
PANTHER_DIR = HERE.parent
CACHE = Path(".cache") / "panther_family_review" / FAMILY
API = "https://pantherdb.org/services/oai/pantherdb"
QUICKGO = "https://www.ebi.ac.uk/QuickGO/services/annotation/search"

# Residue sites: (site id, anchor UniProt accession, anchor positions or None, note).
# With positions None the site is every occurrence of the motif in the anchor sequence.
SITES = [
    ("NPA_motifs", "P29972", None, "both Asn-Pro-Ala motifs, located in the anchor by regex"),
    ("arR_filter", "P29972", [56, 180, 189, 195], "aromatic/arginine constriction of human AQP1"),
    ("AQP1_bovine_H182", "P47865", [182], "bovine AQP1 His182, the residue named in the AQP1 structure paper"),
    ("AQP6_N60", "Q9WTY0", [60], "rat AQP6 Asn60 (Gly in other mammalian aquaporins)"),
    ("AQP6_T63", "Q9WTY0", [63], "rat AQP6 Thr63 (pore-lining, nitrate permeation)"),
    ("AQP6_K72", "Q9WTY0", [72], "rat AQP6 Lys72 (anion/cation selectivity)"),
]
NPA = re.compile("NPA")
MODEL_ORGS = {
    "HUMAN", "MOUSE", "RAT", "CHICK", "XENTR", "DANRE", "DROME", "CAEEL", "YEAST", "SCHPO",
    "CANAL", "DICDI", "ARATH", "ORYSJ", "ECOLI", "LEIMA", "PLAF7",
}


def cached_json(name: str, url: str, params: dict) -> dict:
    """Fetch a JSON payload, caching the raw response under CACHE."""
    CACHE.mkdir(parents=True, exist_ok=True)
    path = CACHE / name
    if path.exists():
        return json.loads(path.read_text())
    for attempt in range(4):
        try:
            r = requests.get(url, params=params, timeout=300, headers={"Accept": "application/json"})
            if r.status_code == 200:
                path.write_text(r.text)
                return r.json()
        except requests.RequestException:
            pass
        time.sleep(2 ** attempt)
    raise SystemExit(f"could not fetch {url} {params}")


def children(node: dict) -> list[dict]:
    ch = node.get("children", {}).get("annotation_node", [])
    return [ch] if isinstance(ch, dict) else ch


class Tree:
    """Full topology of the family tree."""

    def __init__(self, payload: dict) -> None:
        self.nodes: dict[str, dict] = {}
        self.parent: dict[str, str | None] = {}
        self.root = payload["search"]["tree_topology"]["annotation_node"]
        sys.setrecursionlimit(100000)
        self._walk(self.root, None)

    def _walk(self, node: dict, parent: str | None) -> None:
        pid = node["persistent_id"]
        self.nodes[pid] = node
        self.parent[pid] = parent
        for c in children(node):
            self._walk(c, pid)

    def leaves(self, pid: str) -> list[dict]:
        node = self.nodes[pid]
        kids = children(node)
        if not kids:
            return [node]
        return [leaf for c in kids for leaf in self.leaves(c["persistent_id"])]

    def ancestors(self, pid: str) -> list[str]:
        out = []
        cur = self.parent[pid]
        while cur:
            out.append(cur)
            cur = self.parent[cur]
        return out

    def label(self, pid: str) -> str:
        n = self.nodes[pid]
        if not children(n):
            return f"LEAF {org(n)} {acc(n)} {n.get('gene_symbol') or '-'}"
        return f"{n.get('event_type')} {n.get('species') or '-'}"


def acc(leaf: dict) -> str:
    return leaf["node_name"].split("UniProtKB=")[-1]


def org(leaf: dict) -> str:
    return leaf["node_name"].split("|")[0]


def sf(leaf: dict) -> str:
    return (leaf.get("prop_sf_id") or leaf.get("sf_id") or "").split(":")[-1]


def read_paint(path: Path) -> list[dict]:
    with path.open() as fh:
        return [r for r in csv.DictReader(fh, delimiter="\t") if r["node"].startswith("PTN")]


def fmt_counter(c: Counter) -> str:
    return ", ".join(f"{k}={v}" for k, v in sorted(c.items(), key=lambda kv: (-kv[1], kv[0])))


def tree_section(tree: Tree, paint: list[dict], out: list[str]) -> None:
    events = Counter(
        (n.get("event_type") if children(n) else "LEAF") for n in tree.nodes.values()
    )
    out.append(f"## Tree ({FAMILY}, PANTHER {PANTHER_RELEASE})")
    out.append(f"nodes: {fmt_counter(events)}; organisms: {len({org(x) for x in tree.leaves(tree.root['persistent_id'])})}")
    model = Counter(org(x) for x in tree.leaves(tree.root["persistent_id"]) if org(x) in MODEL_ORGS)
    out.append(f"leaves per model organism: {fmt_counter(model)}")
    out.append(f"model organisms with no leaf: {', '.join(sorted(MODEL_ORGS - set(model)))}")
    sf_names = {}
    for leaf in tree.leaves(tree.root["persistent_id"]):
        sf_names[sf(leaf)] = leaf.get("sf_name", "")
    sf_count = Counter(sf(x) for x in tree.leaves(tree.root["persistent_id"]))
    out.append("subfamilies (leaf count, name):")
    for k, v in sorted(sf_count.items(), key=lambda kv: -kv[1]):
        out.append(f"  {k} {v} {sf_names[k]}")

    paint_nodes = sorted({r["node"] for r in paint})
    out.append("")
    out.append("## PAINT nodes")
    for node in paint_nodes:
        rows = [r for r in paint if r["node"] == node]
        row_txt = "; ".join(
            f"{r['evidence']}{' NOT' if r['negated'] == 'true' else ''} {r['go_id']}" for r in rows
        )
        if node not in tree.nodes:
            out.append(f"{node}: NOT IN THIS TREE. rows: {row_txt}")
            continue
        lv = tree.leaves(node)
        anc = tree.ancestors(node)
        out.append(
            f"{node}: {tree.label(node)}; leaves {len(lv)}; organisms {len({org(x) for x in lv})}; "
            f"parent {anc[0] if anc else '-'} ({tree.label(anc[0]) if anc else '-'})"
        )
        out.append(f"  rows: {row_txt}")
        out.append(f"  PAINT ancestors: {', '.join(a for a in anc if a in paint_nodes) or '-'}")
        out.append(f"  subfamilies: {fmt_counter(Counter(sf(x) for x in lv))}")
        model_txt = ", ".join(
            f"{org(x)}:{acc(x)}:{x.get('gene_symbol') or '-'}" for x in lv if org(x) in MODEL_ORGS
        )
        out.append(f"  model-organism leaves: {model_txt or '-'}")
        kids = children(tree.nodes[node])
        for c in kids:
            cid = c["persistent_id"]
            clv = tree.leaves(cid)
            out.append(
                f"  child {cid}: {tree.label(cid)}; leaves {len(clv)}; "
                f"subfamilies {fmt_counter(Counter(sf(x) for x in clv))}"
            )
        dups = [
            p for p in tree.nodes
            if node in tree.ancestors(p) and tree.nodes[p].get("event_type") == "DUPLICATION"
            and children(tree.nodes[p]) and len({org(x) for x in tree.leaves(p)}) > 1
        ]
        out.append(
            "  multi-species duplications below: "
            + (", ".join(f"{d} (leaves {len(tree.leaves(d))})" for d in dups) or "-")
        )


def foreign_nodes(tree: Tree, paint: list[dict], out: list[str]) -> None:
    missing = sorted({r["node"] for r in paint} - set(tree.nodes))
    out.append("")
    out.append("## PAINT rows whose node is outside this tree")
    if not missing:
        out.append("none")
        return
    for node in missing:
        homes = []
        for other in sorted(PANTHER_DIR.glob("PTHR*/PTHR*-paint.tsv")):
            fam = other.parent.name
            if fam == FAMILY:
                continue
            if any(r["node"] == node for r in read_paint(other)):
                homes.append(fam)
        if not homes:
            # Fall back on the PANTHER family that UniProt records for the row's UniProtKB seeds.
            seeds = sorted({
                x.split(":", 1)[1] for r in paint if r["node"] == node
                for x in r["seeds"].split("|") if x.startswith("UniProtKB:")
            })
            for seed in seeds:
                homes.extend(f for f in uniprot_panther_families(seed) if f != FAMILY and f not in homes)
            if not homes:
                out.append(f"{node}: in no other cached PAINT slice and no UniProtKB seed to trace")
                continue
            out.append(f"{node}: in no other cached PAINT slice; UniProt places its seed(s) {', '.join(seeds)} in {', '.join(homes)}")
        for fam in homes:
            other_tree = load_family(fam)
            if other_tree is None:
                out.append(f"{node}: candidate family {fam}; {fam} tree not available")
                continue
            below = leaves_below(other_tree, node)
            orgs = Counter(other_tree["leaves"][x]["organism"] for x in below)
            out.append(
                f"{node}: candidate family {fam}; in the {fam} tree: "
                f"{'yes' if below else 'no'}, leaves {len(below)}, top organisms "
                f"{fmt_counter(Counter(dict(orgs.most_common(4))))}"
            )


def ungapped_index(row: str) -> list[int | None]:
    """For each alignment column, the 1-based residue number of this row (None for a gap)."""
    out: list[int | None] = []
    n = 0
    for ch in row:
        if ch in ".-":
            out.append(None)
        else:
            n += 1
            out.append(n)
    return out


def uniprot_sequence(accession: str) -> tuple[str, str]:
    """(sequence, sequence version) of a UniProtKB entry."""
    CACHE.mkdir(parents=True, exist_ok=True)
    path = CACHE / f"uniprot-{accession}.json"
    if path.exists():
        data = json.loads(path.read_text())
    else:
        r = requests.get(
            f"https://rest.uniprot.org/uniprotkb/{accession}",
            params={"fields": "sequence,sequence_version", "format": "json"}, timeout=120,
        )
        r.raise_for_status()
        path.write_text(r.text)
        data = r.json()
    return data["sequence"]["value"], str(data["entryAudit"]["sequenceVersion"])


def uniprot_panther_families(accession: str) -> list[str]:
    """PANTHER family ids cross-referenced by a UniProtKB entry."""
    r = requests.get(
        f"https://rest.uniprot.org/uniprotkb/{accession}",
        params={"fields": "xref_panther", "format": "json"}, timeout=120,
    )
    if r.status_code != 200:
        return []
    refs = r.json().get("uniProtKBCrossReferences", [])
    return sorted({x["id"].split(":")[0] for x in refs if x.get("database") == "PANTHER"})


def msa_section(tree: Tree, paint: list[dict], msa: dict, out: list[str]) -> None:
    rows = {x["persistent_id"]: x["sequence"] for x in msa["search"]["MSA_list"]["sequence_info"]}
    leaf_ids = [x["persistent_id"] for x in tree.leaves(tree.root["persistent_id"])]
    out.append("")
    out.append("## Alignment (PANTHER familymsa)")
    widths = {len(v) for v in rows.values()}
    out.append(
        f"rows {len(rows)}; columns {sorted(widths)}; tree leaves with a row "
        f"{sum(x in rows for x in leaf_ids)} of {len(leaf_ids)}; rows that are not leaves "
        f"{len(set(rows) - set(leaf_ids))} (ancestral reconstructions)"
    )
    by_acc = {acc(tree.nodes[x]): x for x in leaf_ids}
    paint_nodes = sorted({r["node"] for r in paint if r["node"] in tree.nodes})
    for site_id, anchor, positions, note in SITES:
        out.append("")
        out.append(f"### site {site_id}: anchor UniProtKB:{anchor}; {note}")
        if anchor not in by_acc or by_acc[anchor] not in rows:
            out.append("anchor is not an aligned tree leaf; site skipped")
            continue
        arow = rows[by_acc[anchor]]
        aseq = re.sub(r"[.\-]", "", arow).upper()
        useq, version = uniprot_sequence(anchor)
        out.append(
            f"anchor row equals UniProt sequence (version {version}, length {len(useq)}): {aseq == useq}"
        )
        if aseq != useq:
            out.append("anchor numbering cannot be trusted; site skipped")
            continue
        if positions is None:
            positions = [m.start() + i + 1 for m in NPA.finditer(useq) for i in range(3)]
        idx = ungapped_index(arow)
        cols = [idx.index(p) for p in positions]
        out.append(
            "anchor residues: " + " ".join(f"{useq[p - 1]}{p}" for p in positions)
            + "; match-state columns: " + " ".join("yes" if arow[c].isupper() else "no" for c in cols)
        )

        def pattern(leaf_id: str) -> str:
            row = rows.get(leaf_id)
            if row is None:
                return "?" * len(cols)
            return "".join("-" if row[c] in ".-" else row[c].upper() for c in cols)

        pats = {x: pattern(x) for x in leaf_ids}
        out.append(f"all leaves: {fmt_counter(Counter(pats.values()))}")
        out.append("per subfamily:")
        per_sf: dict[str, Counter] = defaultdict(Counter)
        for x in leaf_ids:
            per_sf[sf(tree.nodes[x])][pats[x]] += 1
        for k in sorted(per_sf, key=lambda k: -sum(per_sf[k].values())):
            out.append(f"  {k}: {fmt_counter(per_sf[k])}")
        out.append("per PAINT node:")
        for node in paint_nodes:
            c = Counter(pats[x["persistent_id"]] for x in tree.leaves(node))
            out.append(f"  {node}: {fmt_counter(c)}")
        if len(cols) == 1:
            # A single position: say which anchor residues of the other sites share its column.
            for other_id, other_anchor, other_pos, _ in SITES:
                if other_pos and other_anchor in by_acc and other_anchor != anchor:
                    orow = rows[by_acc[other_anchor]]
                    oidx = ungapped_index(orow)
                    if oidx[cols[0]] in other_pos:
                        out.append(
                            f"same column as {other_id} anchor UniProtKB:{other_anchor} "
                            f"{orow[cols[0]].upper()}{oidx[cols[0]]}"
                        )
            continue
        out.append("model-organism leaves:")
        for x in leaf_ids:
            n = tree.nodes[x]
            if org(n) in MODEL_ORGS:
                row = rows.get(x, "")
                li = ungapped_index(row) if row else []
                num = " ".join(
                    f"{row[c].upper()}{li[c]}" if row and li[c] else "-" for c in cols
                )
                out.append(f"  {org(n)} {acc(n)} {n.get('gene_symbol') or '-'} {sf(n)}: {num}")


def quickgo(params: dict) -> list[dict]:
    results: list[dict] = []
    page = 1
    while True:
        r = None
        for attempt in range(4):
            try:
                r = requests.get(
                    QUICKGO, params={**params, "limit": 200, "page": page},
                    headers={"Accept": "application/json"}, timeout=120,
                )
                if r.status_code == 200:
                    break
            except requests.RequestException:
                r = None
            time.sleep(2 ** attempt)
        if r is None or r.status_code != 200:
            raise SystemExit(f"QuickGO query failed: {params}")
        data = r.json()
        results.extend(data["results"])
        if page >= data["pageInfo"]["total"]:
            return results
        page += 1


def experimental(accessions: list[str], go_id: str | None) -> list[dict]:
    """Experimental annotations of the accessions (to go_id and its descendants, or all)."""
    hits: list[dict] = []
    for i in range(0, len(accessions), 40):
        params = {
            "geneProductId": ",".join(accessions[i:i + 40]),
            "evidenceCode": "ECO:0000269", "evidenceCodeUsage": "descendants",
        }
        if go_id:
            params.update({"goId": go_id, "goUsage": "descendants", "goUsageRelationships": "is_a,part_of"})
        hits.extend(quickgo(params))
    return hits


GO_NAMES: dict[str, str] = {}


def go_name(go_id: str) -> str:
    """Label of a GO term from the QuickGO ontology service (cached in memory)."""
    if go_id not in GO_NAMES:
        try:
            r = requests.get(
                f"https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/{go_id}",
                headers={"Accept": "application/json"}, timeout=60,
            )
            GO_NAMES[go_id] = r.json()["results"][0]["name"] if r.status_code == 200 else "?"
        except (requests.RequestException, KeyError, IndexError, ValueError):
            GO_NAMES[go_id] = "?"
    return GO_NAMES[go_id]


def collapse(hits: list[dict], info: dict[str, dict], keep) -> list[str]:
    """One line per (leaf, qualifier, term): evidence codes with reference counts."""
    grouped: dict[tuple, dict[str, set]] = defaultdict(lambda: defaultdict(set))
    for h in hits:
        a = h["geneProductId"].split(":")[1]
        if a in info and keep(a):
            key = (org(info[a]), a, info[a].get("gene_symbol") or "-", sf(info[a]), h["qualifier"], h["goId"])
            grouped[key][h["goEvidence"]].add(h["reference"])
    lines = []
    for key in sorted(grouped):
        ev = "; ".join(
            f"{code} x{len(refs)} ({', '.join(sorted(refs)[:3])}{', ...' if len(refs) > 3 else ''})"
            for code, refs in sorted(grouped[key].items())
        )
        o, a, sym, s, qual, go = key
        lines.append(f"{o}:{a}:{sym}:{s} {qual} {go} {go_name(go)}: {ev}")
    return lines


def annotation_section(tree: Tree, paint: list[dict], out: list[str]) -> None:
    all_leaves = tree.leaves(tree.root["persistent_id"])
    accs = sorted({acc(x) for x in all_leaves})
    info = {acc(x): x for x in all_leaves}
    out.append("")
    out.append("## Experimental annotations of tree leaves (QuickGO, ECO:0000269 and descendants)")
    out.append("each PAINT term with its is_a/part_of descendants; references are counted per evidence code")
    cache: dict[str, list[dict]] = {}
    for r in paint:
        node, term = r["node"], r["go_id"]
        if node not in tree.nodes:
            continue
        if term not in cache:
            cache[term] = experimental(accs, term)
        hits = cache[term]
        below = {acc(x) for x in tree.leaves(node)}
        seeds = {s.split(":", 1)[1] for s in r["seeds"].split("|") if s.startswith("UniProtKB:")}
        got = {h["geneProductId"].split(":")[1] for h in hits}
        control = (
            f"positive control: {len(seeds & got)} of {len(seeds & set(accs))} UniProtKB seed leaves returned"
            if seeds & set(accs) else f"positive control: no UniProtKB seed leaf; term returned {len(hits)} rows tree-wide"
        )
        out.append("")
        out.append(f"{r['evidence']}{' NOT' if r['negated'] == 'true' else ''} {node} {term}: {control}")
        inside = collapse(hits, info, lambda a: a in below)
        outside = collapse(hits, info, lambda a: a not in below)
        out.append(f"  below the node: {len(inside)} leaf/term pairs")
        out.extend(f"    {x}" for x in inside)
        if r["negated"] != "true":
            out.append(
                f"  elsewhere in the tree: {len(outside)} leaf/term pairs on "
                f"{len({x.split()[0] for x in outside})} leaves"
            )

    out.append("")
    out.append("## Every experimental annotation of the leaves below PAINT loss nodes")
    for node in sorted({r["node"] for r in paint if r["negated"] == "true" and r["node"] in tree.nodes}):
        below = sorted({acc(x) for x in tree.leaves(node)})
        hits = experimental(below, None)
        lines = collapse(hits, info, lambda a: True)
        out.append(f"{node} ({len(below)} leaves): {len(lines)} leaf/term pairs")
        out.extend(f"  {x}" for x in lines)


def main() -> None:
    payload = cached_json("treeinfo.json", f"{API}/treeinfo", {"family": FAMILY})
    served = str(payload["search"]["product"]["version"])
    if not same_release(served, PANTHER_RELEASE):
        raise SystemExit(f"PANTHER serves release {served}; repository pinned to {PANTHER_RELEASE}")
    msa = cached_json("familymsa.json", f"{API}/familymsa", {"family": FAMILY})
    tree = Tree(payload)
    paint = read_paint(HERE / f"{FAMILY}-paint.tsv")
    out: list[str] = [
        f"# {FAMILY} tree, alignment and annotation check",
        "Generated by tree_msa_check.py; do not edit by hand.",
        "",
    ]
    tree_section(tree, paint, out)
    foreign_nodes(tree, paint, out)
    msa_section(tree, paint, msa, out)
    annotation_section(tree, paint, out)
    (HERE / f"{FAMILY}-tree-msa-check.txt").write_text("\n".join(out) + "\n")
    print(f"wrote {FAMILY}-tree-msa-check.txt ({len(out)} lines)")


if __name__ == "__main__":
    main()
