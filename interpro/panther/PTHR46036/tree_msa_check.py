"""Check this family's PAINT assertions against the PANTHER tree, the PANTHER MSA and GOA.

Run from the repository root:

    uv run python interpro/panther/PTHR46036/tree_msa_check.py

The family is the name of the folder holding this script. Nothing about the result is
hard-coded; every number in the report is recomputed from these inputs:

* the PANTHER ``treeinfo`` and ``familymsa`` services (refused unless they serve the
  repo's pinned ``PANTHER_RELEASE``), cached raw under the git-ignored
  ``.cache/panther_family_checks/<release>/``;
* ``<FAMILY>-paint.tsv`` (PAINT rows) and ``<FAMILY>-entries.csv`` (reviewed members);
* the reference member named in ``<FAMILY>-review.yaml`` (``reference_protein``), whose
  metal-binding and active-site positions are read from the ``FT BINDING`` / ``FT
  ACT_SITE`` lines of its cached UniProt flat file under ``genes/``;
* QuickGO, for the non-electronic annotations of the tree leaves.

Residue statements: a "site column" is the alignment column that holds a reference
site residue. For each leaf the report gives the residue in that column; where a leaf
position is printed it is numbered on the leaf sequence as it stands in the PANTHER MSA
(gaps removed). The MSA only aligns the reference to the first VOC domain of two-domain
members, so the second domain is checked separately by a pairwise alignment
(Biopython ``PairwiseAligner``, global with free end gaps, BLOSUM62, gap open -10, extend
-0.5) of the reference
sequence against the leaf sequence that follows the first domain.

Output: ``<FAMILY>-tree-msa-check.txt``.
"""

from __future__ import annotations

import csv
import gzip
import json
import re
import statistics
import sys
from collections import Counter
from pathlib import Path

import requests
import yaml
from Bio.Align import PairwiseAligner, substitution_matrices

from ai_gene_review.etl.panther_families import PANTHER_RELEASE, same_release
from ai_gene_review.etl.panther_trees import served_release

HERE = Path(__file__).resolve().parent
FAMILY = HERE.name
ROOT = HERE.parents[2]
CACHE = ROOT / ".cache" / "panther_family_checks" / PANTHER_RELEASE
API = "https://pantherdb.org/services/oai/pantherdb"
QUICKGO = "https://www.ebi.ac.uk/QuickGO/services/annotation/search"
ELECTRONIC = {"IEA", "IBA", "ND"}


def fetch(service: str) -> dict:
    """Return a PANTHER service payload for FAMILY, from cache or the API (release-checked)."""
    CACHE.mkdir(parents=True, exist_ok=True)
    path = CACHE / f"{FAMILY}-{service}.json.gz"
    if path.exists():
        with gzip.open(path, "rt") as fh:
            return json.load(fh)
    r = requests.get(f"{API}/{service}", params={"family": FAMILY}, timeout=300)
    r.raise_for_status()
    payload = r.json()
    served = served_release(payload)
    if served is None or not same_release(served, PANTHER_RELEASE):
        raise SystemExit(f"{service}: PANTHER serves release {served}, repo pins {PANTHER_RELEASE}")
    with gzip.open(path, "wt") as fh:
        json.dump(payload, fh)
    return payload


def kids(node: dict) -> list[dict]:
    """Child nodes of a treeinfo node (a single child comes back as a dict)."""
    ch = node.get("children", {}).get("annotation_node", [])
    return [ch] if isinstance(ch, dict) else ch


class Tree:
    """Parent, child and leaf relations of a PANTHER treeinfo payload."""

    def __init__(self, payload: dict) -> None:
        self.node: dict[str, dict] = {}
        self.parent: dict[str, str] = {}
        self.children: dict[str, list[str]] = {}
        self.leaves_under: dict[str, list[str]] = {}
        self.root = self._walk(payload["search"]["tree_topology"]["annotation_node"], None)

    def _walk(self, n: dict, parent: str | None) -> str:
        pid = n["persistent_id"]
        self.node[pid] = n
        if parent:
            self.parent[pid] = parent
        ch = [self._walk(c, pid) for c in kids(n)]
        self.children[pid] = ch
        self.leaves_under[pid] = [pid] if not ch else [x for c in ch for x in self.leaves_under[c]]
        return pid

    def is_leaf(self, pid: str) -> bool:
        return not self.children[pid]

    def acc(self, leaf: str) -> str:
        m = re.search(r"UniProtKB=(\w+)", self.node[leaf].get("node_name", ""))
        return m.group(1) if m else ""

    def sf(self, pid: str) -> str:
        return self.node[pid].get("prop_sf_id", "").split(":")[-1]

    def label(self, pid: str) -> str:
        n = self.node[pid]
        if self.is_leaf(pid):
            return f"{pid} UniProtKB:{self.acc(pid)} {n.get('gene_symbol') or '-'} {n['organism']} {self.sf(pid)}"
        return (f"{pid} {n.get('event_type', '?')} "
                f"[{n.get('species') or 'no taxon'}] leaves={len(self.leaves_under[pid])}")

    def path(self, pid: str) -> list[str]:
        out = [pid]
        while out[-1] in self.parent:
            out.append(self.parent[out[-1]])
        return out[::-1]


def reference_sites(review: dict) -> tuple[str, str, dict[int, str]]:
    """(accession, sequence, {position: label}) of the reference member's site residues."""
    ref = review["reference_protein"]
    acc = ref["id"].split(":")[1]
    flat = (ROOT / ref["gene_review"]).with_name(
        Path(ref["gene_review"]).name.replace("-ai-review.yaml", "-uniprot.txt"))
    text = flat.read_text()
    sites: dict[int, str] = {}
    lines = text.splitlines()
    for i, line in enumerate(lines):
        m = re.match(r"FT   (BINDING|ACT_SITE)\s+(\d+)\s*$", line)
        if not m:
            continue
        note = re.search(r'/(?:ligand|note)="([^"]+)"', lines[i + 1])
        what = note.group(1) if note else m.group(1)
        if m.group(1) == "BINDING" and what == "substrate":
            continue
        pos = int(m.group(2))
        sites[pos] = (sites[pos] + "+" if pos in sites else "") + (
            "active site" if m.group(1) == "ACT_SITE" else what)
    seq = "".join(re.sub(r"[^A-Z]", "", ln) for ln in text.split("\nSQ ")[1].splitlines()[1:]
                  if not ln.startswith("//"))
    return acc, seq, sites


def ungapped(row: str) -> str:
    return re.sub(r"[^A-Za-z]", "", row).upper()


def quickgo(accs: list[str]) -> list[dict]:
    """All QuickGO annotation rows for the accessions (paged)."""
    rows: list[dict] = []
    for i in range(0, len(accs), 40):
        page = 1
        while True:
            r = requests.get(QUICKGO, params={"geneProductId": ",".join(accs[i:i + 40]),
                                              "limit": 200, "page": page},
                             headers={"Accept": "application/json"}, timeout=120)
            r.raise_for_status()
            j = r.json()
            rows += j["results"]
            if page >= j["pageInfo"]["total"]:
                break
            page += 1
    return rows


def agi_to_uniprot(locus: str, candidates: set[str]) -> str:
    """UniProt accession for an Arabidopsis AGI locus (UniProt search), preferring a tree leaf."""
    r = requests.get("https://rest.uniprot.org/uniprotkb/search",
                     params={"query": f"gene:{locus} AND organism_id:3702", "fields": "accession",
                             "format": "tsv", "size": 25}, timeout=120)
    r.raise_for_status()
    accs = r.text.split()[1:]
    return next((a for a in accs if a in candidates), accs[0] if accs else locus)


def main() -> None:
    """Write the tree, MSA and annotation check report for FAMILY."""
    tree = Tree(fetch("treeinfo"))
    msa = {s["persistent_id"]: s["sequence"]
           for s in fetch("familymsa")["search"]["MSA_list"]["sequence_info"]}
    review = yaml.safe_load((HERE / f"{FAMILY}-review.yaml").read_text())
    ref_acc, ref_seq, sites = reference_sites(review)
    leaves = tree.leaves_under[tree.root]
    by_acc = {tree.acc(x): x for x in leaves}
    out: list[str] = []
    add = out.append

    add(f"# {FAMILY} tree, MSA and annotation check (PANTHER release {PANTHER_RELEASE})")
    add(f"tree: {len(leaves)} leaves, {len(tree.node) - len(leaves)} internal nodes, "
        f"root {tree.label(tree.root)}; MSA rows {len(msa)}, columns "
        f"{len(next(iter(msa.values())))}")
    events = Counter(n.get("event_type") for p, n in tree.node.items() if not tree.is_leaf(p))
    add("internal node events: " + ", ".join(f"{k}={v}" for k, v in sorted(events.items())))

    add("")
    add("## Backbone: nodes with at least 10 leaves, non-speciation events with at least 3")
    for pid in tree.node:
        if tree.is_leaf(pid):
            continue
        n = len(tree.leaves_under[pid])
        ev = tree.node[pid].get("event_type")
        if n >= 10 or (ev != "SPECIATION" and n >= 3):
            depth = len(tree.path(pid)) - 1
            sfs = Counter(tree.sf(x) for x in tree.leaves_under[pid])
            add(f"{'  ' * depth}{tree.label(pid)} subfamilies "
                + ",".join(f"{k}={v}" for k, v in sorted(sfs.items())))
    add("leaves that are direct children of backbone nodes outside the plant clades:")
    for leaf in leaves:
        orgs = tree.node[leaf]["organism"]
        if tree.node[leaf].get("definition") and len(tree.leaves_under[tree.parent[leaf]]) >= 100:
            add(f"  child of {tree.parent[leaf]}: {tree.label(leaf)} | {tree.node[leaf]['definition']} ({orgs})")

    add("")
    add("## Subfamilies (PANTHER subfamily root nodes)")
    sf_root = {n["sf_id"].split(":")[-1]: p for p, n in tree.node.items() if n.get("sf_id")}
    for sf, n_leaves in sorted(Counter(tree.sf(x) for x in leaves).items()):
        pid = sf_root.get(sf)
        orgs = Counter(tree.node[x]["organism"] for x in leaves if tree.sf(x) == sf)
        org_txt = ", ".join(f"{k}={v}" for k, v in orgs.most_common(6))
        name = tree.node[pid].get("sf_name", "") if pid else ""
        add(f"{sf} {name}: {n_leaves} leaves; subfamily node {tree.label(pid) if pid else 'none'}; "
            f"{len(orgs)} organisms ({org_txt}{', ...' if len(orgs) > 6 else ''})")

    add("")
    add("## PAINT rows mapped onto the tree")
    paint_rows = []
    with (HERE / f"{FAMILY}-paint.tsv").open() as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            paint_rows.append(row)
    seed_leaf: set[str] = set()
    for row in paint_rows:
        node = row["node"]
        below = tree.leaves_under.get(node, [])
        sfs = Counter(tree.sf(x) for x in below)
        orgs = Counter(tree.node[x]["organism"] for x in below)
        add(f"{row['evidence']} {node} {row['go_id']} {row['aspect']} negated={row['negated']}: "
            f"{tree.label(node) if node in tree.node else 'NODE NOT IN TREE'}; "
            f"{len(orgs)} organisms; subfamilies " + ",".join(f"{k}={v}" for k, v in sorted(sfs.items())))
        add("  path from root: " + " > ".join(
            f"{p} {tree.node[p].get('event_type', '')[:4]} [{tree.node[p].get('species') or '-'}]"
            for p in tree.path(node)))
        if node in tree.parent:
            sibs = [c for c in tree.children[tree.parent[node]] if c != node]
            add("  sister clade(s): " + "; ".join(tree.label(s) for s in sibs))
        add("  children: " + "; ".join(tree.label(c) for c in tree.children.get(node, [])))
        for seed in filter(None, row["seeds"].split("|")):
            acc = seed.split(":")[1]
            if seed.startswith("AGI_LocusCode"):
                acc = agi_to_uniprot(acc, set(by_acc))
            seed_leaf.add(acc)
            leaf = by_acc.get(acc)
            where = "NOT A TREE LEAF" if not leaf else (
                "under node" if leaf in below else "OUTSIDE node") + f": {tree.label(leaf)}"
            add(f"  seed {seed}: {where}")
        if len(below) <= 30:
            for leaf in below:
                add(f"  leaf: {tree.label(leaf)}")
        else:
            add("  leaves by child clade: " + "; ".join(
                f"{c}={len(tree.leaves_under[c])}" for c in tree.children[node]))

    # ---- MSA: reference site columns -------------------------------------------------
    add("")
    add(f"## MSA: reference site columns ({ref_acc}, positions from its UniProt FT lines)")
    ref_leaf = by_acc[ref_acc]
    ref_row = msa[ref_leaf]
    add(f"reference {ref_acc} leaf {ref_leaf}: MSA sequence identical to cached UniProt sequence: "
        f"{ungapped(ref_row) == ref_seq} (length {len(ref_seq)})")
    col_of: dict[int, int] = {}
    pos = 0
    for col, ch in enumerate(ref_row):
        if ch.isalpha():
            pos += 1
            if pos in sites:
                col_of[pos] = col
    order = sorted(sites)
    for p in order:
        add(f"site {ref_seq[p - 1]}{p} ({sites[p]}): MSA column {col_of[p] + 1}, "
            f"match-state column: {ref_row[col_of[p]].isupper()}")
    ref_cols = [i for i, c in enumerate(ref_row) if c.isalpha()]
    first_col = ref_cols[0]
    # End of the reference's contiguous aligned block: PANTHER may place the last few
    # reference residues far downstream, beside the C-terminus of two-domain members.
    last_col = ref_cols[max(sites) - 1]
    for prev, nxt in zip(ref_cols[max(sites) - 1:], ref_cols[max(sites):]):
        if nxt - prev > 30:
            break
        last_col = nxt

    def leaf_pos(leaf: str, col: int) -> int:
        return sum(c.isalpha() for c in msa[leaf][: col + 1])

    def pattern(leaf: str) -> str:
        return "".join(msa[leaf][col_of[p]].upper() if msa[leaf][col_of[p]].isalpha() else "-"
                       for p in order)

    ref_pat = pattern(ref_leaf)
    add(f"site pattern order: {','.join(ref_seq[p - 1] + str(p) for p in order)}; "
        f"reference pattern {ref_pat}")
    pats = {leaf: pattern(leaf) for leaf in leaves}
    add("first-domain site pattern counts over all leaves: "
        + ", ".join(f"{k}={v}" for k, v in Counter(pats.values()).most_common()))
    for sf in sorted({tree.sf(x) for x in leaves}):
        c = Counter(pats[x] for x in leaves if tree.sf(x) == sf)
        add(f"  {sf}: " + ", ".join(f"{k}={v}" for k, v in c.most_common()))
    add("leaves whose first-domain pattern differs from the reference:")
    for leaf in leaves:
        if pats[leaf] != ref_pat:
            detail = ",".join(
                f"{ref_seq[p - 1]}{p}->{msa[leaf][col_of[p]].upper()}{leaf_pos(leaf, col_of[p])}"
                if msa[leaf][col_of[p]].isalpha() else f"{ref_seq[p - 1]}{p}->gap" for p in order)
            add(f"  {tree.label(leaf)}: {pats[leaf]} ({detail}); "
                f"{tree.node[leaf].get('definition', '')}")

    add("first-domain site residues of the PAINT seeds (leaf numbering):")
    for acc in sorted(seed_leaf):
        leaf = by_acc[acc]
        add(f"  UniProtKB:{acc}: " + ",".join(
            f"{ref_seq[p - 1]}{p}->{msa[leaf][col_of[p]].upper()}{leaf_pos(leaf, col_of[p])}"
            for p in order))

    # ---- second VOC domain by pairwise alignment --------------------------------------
    add("")
    add("## Second VOC domain: pairwise alignment (free end gaps) of the reference to the leaf tail")
    aligner = PairwiseAligner()
    aligner.mode = "global"
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score, aligner.extend_gap_score = -10, -0.5
    aligner.end_gap_score = 0  # end gaps free: the tail may be longer or shorter than the reference
    tail_pat: dict[str, str] = {}
    tail_detail: dict[str, str] = {}
    for leaf in leaves:
        row = msa[leaf]
        head_len = sum(c.isalpha() for c in row[: last_col + 1])
        tail = ungapped(row)[head_len:]
        if len(tail) < 0.6 * len(ref_seq):
            continue
        aln = aligner.align(ref_seq, tail)[0]
        mapping = {}
        for (r0, r1), (t0, t1) in zip(*aln.aligned):
            for k in range(r1 - r0):
                mapping[r0 + k + 1] = t0 + k
        tail_pat[leaf] = "".join(tail[mapping[p]] if p in mapping else "-" for p in order)
        tail_detail[leaf] = ",".join(
            f"{ref_seq[p - 1]}{p}->{tail[mapping[p]]}{head_len + mapping[p] + 1}" if p in mapping
            else f"{ref_seq[p - 1]}{p}->unaligned" for p in order) + f"; score {aln.score:.0f}"
    add(f"leaves with a tail of at least 60% of the reference length (two-domain members): "
        f"{len(tail_pat)} of {len(leaves)}; single-domain leaves {len(leaves) - len(tail_pat)}")
    single = Counter(tree.node[x]["organism"] for x in leaves if x not in tail_pat)
    add("single-domain leaves by organism: " + ", ".join(f"{k}={v}" for k, v in sorted(single.items())))
    add("single-domain leaves below the plant duplication nodes (fragments or truncated models): "
        + ", ".join(f"UniProtKB:{tree.acc(x)}({len(ungapped(msa[x]))} aa)" for x in leaves
                    if x not in tail_pat and "Embryophyta" in
                    [tree.node[p].get("species") for p in tree.path(x)]))
    add("second-domain site pattern counts: "
        + ", ".join(f"{k}={v}" for k, v in Counter(tail_pat.values()).most_common()))
    add("first-domain|second-domain pattern pairs per subfamily (two-domain leaves):")
    for sf in sorted({tree.sf(x) for x in tail_pat}):
        c = Counter(f"{pats[x]}|{tail_pat[x]}" for x in tail_pat if tree.sf(x) == sf)
        add(f"  {sf}: " + ", ".join(f"{k}={v}" for k, v in c.most_common()))
    add("two-domain leaves outside the plant clades, and PAINT seeds:")
    seed_accs = set(seed_leaf)
    for leaf in tail_pat:
        org = tree.node[leaf]["organism"]
        if tree.acc(leaf) in seed_accs or len(tree.leaves_under[tree.parent[leaf]]) >= 100:
            add(f"  {tree.label(leaf)}: first {pats[leaf]}, second {tail_pat[leaf]} "
                f"({tail_detail[leaf]}) ({org})")

    # ---- targeting proxies for cellular-component rows --------------------------------
    add("")
    add("## Targeting proxies (from the MSA sequences)")
    add("N-terminal extension = residues before the column of reference residue 1; "
        "C-terminal tripeptide = last three residues of the PANTHER sequence")

    def n_ext(leaf: str) -> int:
        return sum(c.isalpha() for c in msa[leaf][:first_col])

    clades = {row["node"] for row in paint_rows if row["aspect"] == "C"}
    clades |= {p for p in tree.node if not tree.is_leaf(p)
               and tree.node[p].get("event_type") == "DUPLICATION"
               and len(tree.leaves_under[p]) >= 30
               for p in tree.children[p]}
    for node in sorted(clades, key=lambda p: -len(tree.leaves_under[p])):
        below = tree.leaves_under[node]
        ext = [n_ext(x) for x in below]
        tri = Counter(ungapped(msa[x])[-3:] for x in below)
        add(f"{tree.label(node)}: N-terminal extension median {statistics.median(ext):.0f} "
            f"(min {min(ext)}, max {max(ext)}, at least 40 residues in "
            f"{sum(e >= 40 for e in ext)} of {len(ext)}); C-terminal tripeptides "
            + ", ".join(f"{k}={v}" for k, v in tri.most_common(6)))

    # ---- reviewed members and current sequences ----------------------------------------
    add("")
    add("## Reviewed (Swiss-Prot) members in the entries file")
    with (HERE / f"{FAMILY}-entries.csv").open() as fh:
        members = list(csv.DictReader(fh))
    add(f"reviewed members {len(members)}; tree leaves among them "
        f"{sum(m['id'] in by_acc for m in members)}")
    for m in members:
        leaf = by_acc.get(m["id"])
        extra = f"TREE_LEAF {leaf} first-domain {pats[leaf]}" if leaf else "NOT_IN_TREE"
        add(f"member {m['id']} {m['gene'] or '-'} {m['subfamily'].split(':')[-1]} length "
            f"{m['length']} {extra}: {m['name']} ({m['source_tax_name']})")

    # ---- GOA ---------------------------------------------------------------------------
    add("")
    add("## QuickGO annotations of the tree leaves")
    rows = quickgo(sorted(by_acc))
    add(f"rows returned {len(rows)} for {len(by_acc)} leaf accessions; evidence codes "
        + ", ".join(f"{k}={v}" for k, v in sorted(Counter(r['goEvidence'] for r in rows).items())))
    terms = sorted({row["go_id"] for row in paint_rows})
    for term in terms:
        hits = [r for r in rows if r["goId"] == term]
        exp = sorted({r["geneProductId"] for r in hits if r["goEvidence"] not in ELECTRONIC})
        add(f"positive control {term}: {len(hits)} rows on leaves, {len(exp)} leaves with "
            f"non-electronic evidence ({', '.join(exp) or 'none'})")
    add("non-electronic rows (accession symbol qualifier term evidence reference assigned_by with):")
    for r in sorted(rows, key=lambda r: (r["geneProductId"], r["goId"], r["reference"])):
        if r["goEvidence"] in ELECTRONIC:
            continue
        with_ = ",".join(f"{x['db']}:{x['id']}" for w in (r.get("withFrom") or [])
                         for x in w["connectedXrefs"])
        add(f"  {r['geneProductId']} {r['symbol']} {r['qualifier']} {r['goId']} "
            f"{r['goEvidence']} {r['reference']} {r['assignedBy']} {with_ or '-'}")

    (HERE / f"{FAMILY}-tree-msa-check.txt").write_text("\n".join(out) + "\n")
    print(f"wrote {FAMILY}-tree-msa-check.txt ({len(out)} lines)", file=sys.stderr)


if __name__ == "__main__":
    main()
