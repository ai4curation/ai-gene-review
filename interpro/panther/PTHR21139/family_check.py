"""Tree, alignment and experimental-annotation check for this PANTHER family.

Run from the repository root:

    uv run python interpro/panther/PTHR21139/family_check.py

The family is the name of the folder holding this script. Inputs are fetched from
primary services and cached, git-ignored, under ``.cache/family_check/<FAMILY>/``:

* the PANTHER ``treeinfo`` tree (topology, event types, taxa, subfamilies);
* the PANTHER ``familymsa`` alignment (one row per tree node, leaves and ancestors);
* UniProt records of every tree leaf (sequence, review status, active-site and
  binding-site features, transit peptides);
* QuickGO experimental annotations of every tree leaf;
* UniProt records of the reviewed family members listed in ``<FAMILY>-entries.csv``
  that are not tree leaves. These have no row in the PANTHER alignment, so each is
  aligned pairwise (Biopython, global, BLOSUM62) to its best-scoring reference leaf
  and read at that reference's functional positions.

Nothing about the result is hard-coded: functional columns are the alignment columns
of the ``ACT_SITE`` and ``BINDING`` features of the reviewed leaves, and only a leaf
whose alignment row matches its current UniProt sequence is used as an anchor.

Outputs, next to this script: ``<FAMILY>-tree-check.txt`` (tree and PAINT nodes),
``<FAMILY>-msa-check.txt`` (functional residues) and ``<FAMILY>-go-check.txt``
(experimental annotations under each PAINT node).
"""

from __future__ import annotations

import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

import requests
from Bio.Align import PairwiseAligner, substitution_matrices

from ai_gene_review.etl.panther_families import PANTHER_RELEASE, same_release

HERE = Path(__file__).resolve().parent
FAMILY = HERE.name
CACHE = Path(".cache") / "family_check" / FAMILY
PANTHER = "https://pantherdb.org/services/oai/pantherdb"
UNIPROT = "https://rest.uniprot.org/uniprotkb/search"
QUICKGO = "https://www.ebi.ac.uk/QuickGO/services/annotation/search"
EXPERIMENTAL = {"EXP", "IDA", "IMP", "IGI", "IPI", "IEP", "HTP", "HDA", "HMP", "HGI", "HEP"}
UNIPROT_FIELDS = (
    "accession,id,reviewed,sequence,ft_act_site,ft_binding,ft_transit,gene_names,"
    "organism_name,protein_name,sequence_version"
)

Node = dict[str, Any]


def cached_json(name: str, url: str, params: dict[str, str]) -> Any:
    """Return JSON from ``url``, cached as ``name`` under the family cache."""
    path = CACHE / name
    if path.exists():
        return json.loads(path.read_text())
    r = requests.get(url, params=params, headers={"Accept": "application/json"}, timeout=300)
    r.raise_for_status()
    data = r.json()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data))
    return data


def children(node: Node) -> list[Node]:
    """Child nodes of a treeinfo node (a single child is served as a dict)."""
    ch = node.get("children", {}).get("annotation_node", [])
    return [ch] if isinstance(ch, dict) else ch


def leaves_of(node: Node) -> list[Node]:
    """Leaf nodes at or below ``node``."""
    kids = children(node)
    return [node] if not kids else [leaf for k in kids for leaf in leaves_of(k)]


def accession(leaf: Node) -> str:
    """UniProt accession parsed from a leaf's ``node_name``."""
    for tok in leaf.get("node_name", "").split("|"):
        if tok.startswith("UniProtKB="):
            return tok.split("=", 1)[1]
    return ""


def short_sf(node: Node) -> str:
    """Subfamily suffix (``SF2``) of a node."""
    return (node.get("prop_sf_id") or node.get("sf_id") or "").split(":")[-1]


def taxon(node: Node) -> str:
    """Taxon label PANTHER gives an internal node."""
    return node.get("species") or node.get("taxonomic_range") or "-"


def fetch_uniprot(accs: list[str], prefix: str = "uniprot") -> dict[str, dict]:
    """UniProt records for ``accs`` (batched search), keyed by primary accession."""
    out: dict[str, dict] = {}
    for i in range(0, len(accs), 80):
        batch = accs[i : i + 80]
        data = cached_json(
            f"{prefix}-{i:04d}.json",
            UNIPROT,
            {
                "query": " OR ".join(f"accession:{a}" for a in batch),
                "fields": UNIPROT_FIELDS,
                "format": "json",
                "size": "500",
            },
        )
        for rec in data["results"]:
            if "sequence" in rec:  # deleted or merged entries are served without one
                out[rec["primaryAccession"]] = rec
    return out


def fetch_quickgo(accs: list[str]) -> list[dict]:
    """All GO annotations of ``accs`` from QuickGO, all pages.

    QuickGO has no filter on the GO evidence code (an unknown parameter is ignored
    without error), so every row is fetched and the caller filters on ``goEvidence``.
    """
    rows: list[dict] = []
    for i in range(0, len(accs), 60):
        batch = accs[i : i + 60]
        page = 1
        while True:
            data = cached_json(
                f"quickgo-{i:04d}-p{page}.json",
                QUICKGO,
                {
                    "geneProductId": ",".join(batch),
                    "includeFields": "goName",
                    "limit": "200",
                    "page": str(page),
                },
            )
            rows.extend(data["results"])
            if page >= data["pageInfo"]["total"]:
                break
            page += 1
    return rows


def features(rec: dict, kind: str) -> list[tuple[int, int, str]]:
    """(start, end, ligand-or-description) of a UniProt record's features of ``kind``."""
    out = []
    for f in rec.get("features", []):
        if f["type"] == kind:
            lig = (f.get("ligand") or {}).get("name", "") or f.get("description", "")
            out.append((f["location"]["start"]["value"], f["location"]["end"]["value"], lig))
    return out


def column_map(row: str) -> dict[int, int]:
    """Map 1-based residue positions of an alignment row to 0-based columns.

    >>> column_map("..A.c-G")
    {1: 2, 2: 4, 3: 6}
    """
    out: dict[int, int] = {}
    pos = 0
    for col, ch in enumerate(row):
        if ch.isalpha():
            pos += 1
            out[pos] = col
    return out


def protein_name(rec: dict) -> str:
    """Recommended (or first submitted) protein name of a UniProt record."""
    desc = rec.get("proteinDescription", {})
    name = desc.get("recommendedName") or (desc.get("submissionNames") or [{}])[0]
    return name.get("fullName", {}).get("value", "?")


def pairwise_positions(aligner: PairwiseAligner, ref: str, query: str) -> tuple[float, dict[int, int]]:
    """Score and 1-based ref-to-query position map of the best global alignment."""
    aln = aligner.align(ref, query)[0]
    mapping: dict[int, int] = {}
    for (r0, r1), (q0, _q1) in zip(*aln.aligned):
        for k in range(r1 - r0):
            mapping[r0 + k + 1] = q0 + k + 1
    return aln.score, mapping


def ungapped(row: str) -> str:
    """Alignment row with gap characters removed, upper-cased."""
    return "".join(ch for ch in row if ch.isalpha()).upper()


def main() -> None:
    """Write the three check reports for FAMILY."""
    tree_payload = cached_json("treeinfo.json", f"{PANTHER}/treeinfo", {"family": FAMILY})
    version = str(tree_payload["search"]["product"]["version"])
    if not same_release(version, PANTHER_RELEASE):
        raise SystemExit(f"PANTHER serves release {version}, repo pinned to {PANTHER_RELEASE}")
    root: Node = tree_payload["search"]["tree_topology"]["annotation_node"]
    msa_payload = cached_json("familymsa.json", f"{PANTHER}/familymsa", {"family": FAMILY})
    msa = {s["persistent_id"]: s["sequence"] for s in msa_payload["search"]["MSA_list"]["sequence_info"]}

    parent: dict[str, Node | None] = {}
    nodes: dict[str, Node] = {}

    def walk(n: Node, par: Node | None) -> None:
        nodes[n["persistent_id"]] = n
        parent[n["persistent_id"]] = par
        for k in children(n):
            walk(k, n)

    walk(root, None)
    all_leaves = leaves_of(root)
    accs = sorted({accession(x) for x in all_leaves if accession(x)})
    uni = fetch_uniprot(accs)
    go_rows = fetch_quickgo(accs)

    def lineage(pid: str) -> list[Node]:
        out = []
        cur = parent[pid]
        while cur is not None:
            out.append(cur)
            cur = parent[cur["persistent_id"]]
        return out

    with (HERE / f"{FAMILY}-paint.tsv").open() as fh:
        paint = [r for r in csv.DictReader(fh, delimiter="\t") if r["node"].startswith("PTN")]
    paint_nodes = sorted({r["node"] for r in paint})

    # ------------------------------------------------------------------ tree
    out: list[str] = [
        f"family {FAMILY} PANTHER release {version}: leaves {len(all_leaves)}, "
        f"internal nodes {len(nodes) - len(all_leaves)}, alignment rows {len(msa)}"
    ]
    sf_count = Counter(short_sf(x) for x in all_leaves)
    out.append("leaf subfamilies: " + ", ".join(f"{k}={v}" for k, v in sorted(sf_count.items())))
    out.append("")
    out.append("# internal nodes that are not plain speciations, and nodes with a PAINT row")
    for pid, n in nodes.items():
        if not children(n):
            continue
        ev = n.get("event_type", "")
        if ev == "SPECIATION" and pid not in paint_nodes:
            continue
        below = leaves_of(n)
        sfs = Counter(short_sf(x) for x in below)
        kids = "; ".join(
            f"{k['persistent_id']} {taxon(k) if children(k) else accession(k)} n={len(leaves_of(k))}"
            for k in children(n)
        )
        tag = " PAINT" if pid in paint_nodes else ""
        out.append(
            f"node {pid} {ev} taxon={taxon(n)} leaves={len(below)} species="
            f"{len({x['organism'] for x in below})} subfamilies "
            + ",".join(f"{k}={v}" for k, v in sorted(sfs.items()))
            + f" children [{kids}]{tag}"
        )
    out.append("")
    out.append("# subfamily clades: the deepest node holding every leaf of the subfamily")
    for sf in sorted(sf_count):
        members = [x["persistent_id"] for x in all_leaves if short_sf(x) == sf]
        common = None
        for anc in [nodes[members[0]]] + lineage(members[0]):
            below = {x["persistent_id"] for x in leaves_of(anc)}
            if set(members) <= below:
                common = (anc, len(below))
                break
        assert common is not None
        out.append(
            f"subfamily {sf} leaves={len(members)} common ancestor {common[0]['persistent_id']} "
            f"taxon={taxon(common[0])} leaves below={common[1]} "
            f"({'monophyletic' if common[1] == len(members) else 'not monophyletic'})"
        )
    out.append("")
    out.append("# PAINT rows mapped onto the tree")
    for r in paint:
        n = nodes.get(r["node"])
        if n is None:
            out.append(f"{r['evidence']} {r['node']} {r['go_id']} NOT IN TREE")
            continue
        below = leaves_of(n)
        sfs = Counter(short_sf(x) for x in below)
        path = " < ".join(f"{a['persistent_id']}({a.get('event_type', '')},{taxon(a)})" for a in lineage(r["node"]))
        out.append(
            f"{r['evidence']} {r['node']} {r['go_id']} {r['aspect']} negated={r['negated']} "
            f"taxon={taxon(n) if children(n) else accession(n)}: leaves {len(below)}; "
            f"species {len({x['organism'] for x in below})}; leaf subfamilies "
            + ", ".join(f"{k}={v}" for k, v in sorted(sfs.items()))
            + f"; ancestors {path or 'none (root)'}"
        )
    out.append("")
    out.append("# leaves (tree order) with the PAINT nodes above each")
    for x in all_leaves:
        pid = x["persistent_id"]
        above = [a["persistent_id"] for a in lineage(pid) if a["persistent_id"] in paint_nodes]
        above = ([pid] if pid in paint_nodes else []) + above
        rec = uni.get(accession(x), {})
        status = "not in UniProt" if not rec else "TrEMBL" if "unreviewed" in rec["entryType"].lower() else "Swiss-Prot"
        out.append(
            f"leaf {pid} UniProtKB:{accession(x)} {x.get('gene_symbol') or '-'} | {x['organism']} | "
            f"{short_sf(x)} | {status} | under {','.join(above)}"
        )
    (HERE / f"{FAMILY}-tree-check.txt").write_text("\n".join(out) + "\n")

    # ------------------------------------------------------------------- msa
    out = [f"family {FAMILY} PANTHER release {version} alignment: {len(msa)} rows, {len(next(iter(msa.values())))} columns"]
    leaf_by_acc = {accession(x): x for x in all_leaves}
    match_state: dict[str, bool] = {}
    for x in all_leaves:
        rec = uni.get(accession(x))
        row = msa.get(x["persistent_id"], "")
        match_state[x["persistent_id"]] = bool(rec) and ungapped(row) == rec["sequence"]["value"]
    out.append(
        f"leaves whose alignment row equals the current UniProt sequence: "
        f"{sum(match_state.values())} of {len(all_leaves)}"
    )
    # functional columns from reviewed leaves' UniProt features
    col_sources: dict[int, list[str]] = defaultdict(list)
    col_kind: dict[int, set[str]] = defaultdict(set)
    anchors = []
    for acc, rec in sorted(uni.items()):
        x = leaf_by_acc.get(acc)
        if x is None or "unreviewed" in rec["entryType"].lower() or not match_state[x["persistent_id"]]:
            continue
        cmap = column_map(msa[x["persistent_id"]])
        feats = [("ACT_SITE", f) for f in features(rec, "Active site")] + [
            ("BINDING", f) for f in features(rec, "Binding site")
        ]
        if not feats:
            continue
        anchors.append(acc)
        for kind, (start, end, _lig) in feats:
            for pos in range(start, end + 1):
                col_sources[cmap[pos]].append(f"{acc}:{rec['sequence']['value'][pos - 1]}{pos}")
                col_kind[cmap[pos]].add(kind)
    out.append(f"anchor proteins (reviewed leaves with active-site or binding-site features): {len(anchors)}")
    ref_accs = [a for a in ("P00942", "P60174", "P0A858", "P48491", "Q9SKP6", "Q58923") if a in leaf_by_acc]
    out.append("")
    out.append("# functional columns: residues across all leaves; positions in reference sequences")
    func_cols = sorted(col_sources)
    consensus: dict[int, str] = {}
    for col in func_cols:
        counts = Counter(msa[x["persistent_id"]][col].upper() for x in all_leaves)
        consensus[col] = counts.most_common(1)[0][0]
        refs = []
        for acc in ref_accs:
            row = msa[leaf_by_acc[acc]["persistent_id"]]
            inv = {c: p for p, c in column_map(row).items()}
            refs.append(f"{acc}:{row[col].upper()}{inv[col]}" if col in inv else f"{acc}:gap")
        out.append(
            f"column {col} {'+'.join(sorted(col_kind[col]))} annotated in {len(col_sources[col])} anchors; "
            f"residues " + ", ".join(f"{k}={v}" for k, v in counts.most_common()) + "; " + " ".join(refs)
        )
    act_cols = [c for c in func_cols if "ACT_SITE" in col_kind[c]]
    out.append("")
    out.append("# UniProt sequence versions of the reference proteins")
    for acc in ref_accs:
        rec = uni[acc]
        out.append(
            f"reference {acc} {rec['uniProtkbId']} sequence version {rec['entryAudit']['sequenceVersion']} "
            f"length {rec['sequence']['length']} alignment row equals UniProt sequence: "
            f"{match_state[leaf_by_acc[acc]['persistent_id']]}"
        )
    out.append("")
    out.append("# leaves that differ from the family consensus at a functional column")

    def site_string(pid: str, cols: list[int]) -> str:
        return "".join(msa[pid][c].upper() if msa[pid][c].isalpha() else "-" for c in cols)

    def native(pid: str) -> str:
        """Residues at the functional columns in the leaf's own numbering."""
        inv = {c: p for p, c in column_map(msa[pid]).items()}
        return ",".join(f"{msa[pid][c].upper()}{inv[c]}" if c in inv else "-" for c in func_cols)

    cons_all = "".join(consensus[c] for c in func_cols)
    cons_act = "".join(consensus[c] for c in act_cols)
    out.append(f"consensus at active-site columns {act_cols}: {cons_act}")
    out.append(f"consensus at all functional columns {func_cols}: {cons_all}")
    # occupancy of the reference's columns, to tell fragments from substitutions
    ref_cols = sorted(column_map(msa[leaf_by_acc[ref_accs[0]]["persistent_id"]]).values()) if ref_accs else []
    deviants = 0
    for x in all_leaves:
        pid = x["persistent_id"]
        s_all = site_string(pid, func_cols)
        if s_all == cons_all:
            continue
        deviants += 1
        cover = sum(msa[pid][c].isalpha() for c in ref_cols) / len(ref_cols) if ref_cols else 0.0
        rec = uni.get(accession(x), {})
        out.append(
            f"deviant {pid} UniProtKB:{accession(x)} {x.get('gene_symbol') or '-'} | {x['organism']} | {short_sf(x)} | "
            f"active site {site_string(pid, act_cols)} | functional {s_all} | own numbering {native(pid)} | length "
            f"{rec.get('sequence', {}).get('length', '?')} | coverage of {ref_accs[0] if ref_accs else '-'} columns {cover:.2f}"
        )
    out.append(f"leaves differing at any functional column: {deviants} of {len(all_leaves)}")
    out.append("")
    out.append("# per-subfamily and per-PAINT-node conservation of the active-site columns")
    groups: dict[str, list[Node]] = {f"subfamily {sf}": [x for x in all_leaves if short_sf(x) == sf] for sf in sorted(sf_count)}
    for pn in paint_nodes:
        if pn in nodes:
            groups[f"PAINT node {pn}"] = leaves_of(nodes[pn])
    for name, members in groups.items():
        c_act = Counter(site_string(x["persistent_id"], act_cols) for x in members)
        c_all = sum(site_string(x["persistent_id"], func_cols) == cons_all for x in members)
        out.append(
            f"{name}: leaves {len(members)}; active-site strings "
            + ", ".join(f"{k}={v}" for k, v in c_act.most_common())
            + f"; all functional columns at consensus {c_all}"
        )
    out.append("")
    out.append("# identity to the first reference over its own columns, per subfamily")
    if ref_accs:
        ref_row = msa[leaf_by_acc[ref_accs[0]]["persistent_id"]]
        for sf in sorted(sf_count):
            ids = []
            for x in all_leaves:
                if short_sf(x) != sf:
                    continue
                row = msa[x["persistent_id"]]
                ids.append(sum(row[c].upper() == ref_row[c].upper() for c in ref_cols) / len(ref_cols))
            out.append(
                f"subfamily {sf} identity to {ref_accs[0]}: min {min(ids):.2f} median "
                f"{sorted(ids)[len(ids) // 2]:.2f} max {max(ids):.2f} (n={len(ids)})"
            )
    out.append("")
    out.append("# UniProt transit peptides among tree leaves")
    for x in all_leaves:
        rec = uni.get(accession(x))
        if not rec:
            continue
        for start, end, desc in features(rec, "Transit peptide"):
            out.append(
                f"transit {x['persistent_id']} UniProtKB:{accession(x)} {x.get('gene_symbol') or '-'} | "
                f"{x['organism']} | {short_sf(x)} | {start}-{end} {desc}"
            )
    out.append("")
    out.append("# reviewed family members that are not tree leaves, aligned pairwise to a reference leaf")
    with (HERE / f"{FAMILY}-entries.csv").open() as fh:
        members = [m["id"] for m in csv.DictReader(fh) if m["id"] not in leaf_by_acc]
    extra = fetch_uniprot(members, prefix="uniprot-members")
    aligner = PairwiseAligner()
    aligner.mode = "global"
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score, aligner.extend_gap_score = -10, -0.5
    aligner.end_gap_score = 0
    ref_seq = {a: uni[a]["sequence"]["value"] for a in ref_accs}
    ref_pos = {
        a: {c: p for p, c in column_map(msa[leaf_by_acc[a]["persistent_id"]]).items()} for a in ref_accs
    }
    detail: list[str] = []
    by_name: dict[str, Counter] = defaultdict(Counter)
    example: dict[tuple[str, str], str] = {}
    for acc in sorted(extra):
        seq = extra[acc]["sequence"]["value"]
        best = max(((pairwise_positions(aligner, ref_seq[a], seq), a) for a in ref_accs), key=lambda t: t[0][0])
        (_score, mapping), ref = best
        sig = "".join(
            seq[mapping[ref_pos[ref][c]] - 1] if ref_pos[ref].get(c) in mapping else "-" for c in func_cols
        )
        name = protein_name(extra[acc])
        if "triose" not in name.lower():
            own = ",".join(
                f"{seq[mapping[ref_pos[ref][c]] - 1]}{mapping[ref_pos[ref][c]]}"
                if ref_pos[ref].get(c) in mapping
                else "-"
                for c in func_cols
            )
            detail.append(
                f"member {acc} {extra[acc]['uniProtkbId']} '{name}' sequence version "
                f"{extra[acc]['entryAudit']['sequenceVersion']} via {ref}: functional {sig} | own numbering {own}"
            )
        by_name[name][sig] += 1
        example.setdefault((name, sig), f"{acc} {extra[acc]['organism']['scientificName']} via {ref}")
    out.append(f"reviewed members not in the tree: {len(members)}; UniProt records fetched: {len(extra)}")
    for name, sigs in sorted(by_name.items(), key=lambda kv: -sum(kv[1].values())):
        for sig, n in sigs.most_common():
            out.append(f"member name '{name}': functional {sig} x{n} (e.g. {example[(name, sig)]})")
    out.append("")
    out.append("# reviewed non-tree members not named as a triosephosphate isomerase")
    out.extend(detail)
    (HERE / f"{FAMILY}-msa-check.txt").write_text("\n".join(out) + "\n")

    # -------------------------------------------------------------------- go
    all_rows = len(go_rows)
    code_counts = Counter(row["goEvidence"] for row in go_rows)
    go_rows = [row for row in go_rows if row["goEvidence"] in EXPERIMENTAL]
    out = [
        f"family {FAMILY}: QuickGO annotations of {len(accs)} tree-leaf accessions: {all_rows} rows "
        f"({', '.join(f'{k}={v}' for k, v in code_counts.most_common())}); experimental rows kept "
        f"({','.join(sorted(EXPERIMENTAL))}): {len(go_rows)}"
    ]
    by_acc: dict[str, dict[tuple[str, str, bool], set[str]]] = defaultdict(lambda: defaultdict(set))
    for row in go_rows:
        acc = row["geneProductId"].split(":")[1].split("-")[0]
        neg = "NOT" in row["qualifier"]
        by_acc[acc][(row["goId"], row.get("goName") or "", neg)].add(f"{row['goEvidence']}:{row['reference']}")
    out.append(f"leaves with at least one experimental annotation: {len(by_acc)}")
    out.append("")
    out.append("# PAINT terms: leaves below each node with experimental annotation to exactly that term")
    for r in paint:
        if r["node"] not in nodes:
            continue
        below = leaves_of(nodes[r["node"]])
        hits = []
        for x in below:
            for (go, _name, neg), refs in by_acc.get(accession(x), {}).items():
                if go == r["go_id"]:
                    hits.append(f"{accession(x)}({x['organism']}{' NOT' if neg else ''}; {'; '.join(sorted(refs))})")
        outside = []
        for x in all_leaves:
            if x in below:
                continue
            for (go, _name, neg), refs in by_acc.get(accession(x), {}).items():
                if go == r["go_id"]:
                    outside.append(f"{accession(x)}({x['organism']}{' NOT' if neg else ''})")
        out.append(
            f"{r['evidence']} {r['node']} {r['go_id']} negated={r['negated']} PAINT seeds {len(r['seeds'].split('|'))}: "
            f"leaves below with experimental {r['go_id']}: {len(hits)}"
        )
        for h in hits:
            out.append(f"  below {r['node']} {r['go_id']}: {h}")
        out.append(f"  outside {r['node']} with experimental {r['go_id']}: {', '.join(outside) or 'none'}")
    out.append("")
    out.append("# every experimental annotation of a tree leaf (protein binding GO:0005515 counted only)")
    for x in all_leaves:
        acc = accession(x)
        if acc not in by_acc:
            continue
        above = [a["persistent_id"] for a in lineage(x["persistent_id"]) if a["persistent_id"] in paint_nodes]
        out.append(f"leaf UniProtKB:{acc} {x.get('gene_symbol') or '-'} | {x['organism']} | {short_sf(x)} | under {','.join(above)}")
        for (go, name, neg), refs in sorted(by_acc[acc].items()):
            if go == "GO:0005515":
                out.append(f"  {acc} GO:0005515 protein binding: {len(refs)} rows")
                continue
            codes = re.sub(r"\s+", " ", "; ".join(sorted(refs)))
            out.append(f"  {acc} {'NOT ' if neg else ''}{go} {name}: {codes}")
    (HERE / f"{FAMILY}-go-check.txt").write_text("\n".join(out) + "\n")
    print("wrote tree-check, msa-check and go-check reports")


if __name__ == "__main__":
    main()
