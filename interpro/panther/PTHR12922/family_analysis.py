"""Tree, alignment and experimental-annotation check for the PANTHER family of this folder.

Run from the repository root:

    uv run python interpro/panther/PTHR12922/family_analysis.py

Everything is fetched live and nothing about the result is hard-coded:

* the family tree (PANTHER ``treeinfo`` service) with node event types and taxon labels;
* the family alignment (PANTHER ``familymsa`` service, the alignment the tree was built from);
* the PAINT rows in ``<FAMILY>-paint.tsv``;
* the reference residues: every UniProt ``Binding site`` feature of ``REFERENCE``;
* experimental GO annotations of the tree leaves (QuickGO, queried by gene product and
  filtered on evidence code, so the query does not depend on a term-name field).

Raw payloads are kept only under the git-ignored ``.cache/``. Output:
``<FAMILY>-analysis.txt`` (compact, committed).
"""

from __future__ import annotations

import csv
import json
import re
import sys
import time
from collections import Counter
from pathlib import Path

import requests

HERE = Path(__file__).resolve().parent
FAMILY = HERE.name
CACHE = Path(".cache") / "panther_family_analysis" / FAMILY
PANTHER = "https://pantherdb.org/services/oai/pantherdb"
QUICKGO = "https://www.ebi.ac.uk/QuickGO/services/annotation/search"
#: Sequence whose UniProt binding-site features define the columns to check.
REFERENCE = "Q9Y3A0"
#: Leaves whose aligned motif region is printed in full (the experimentally studied
#: members and one per major lineage); any leaf that deviates is printed as well.
SHOW = ["Q9Y3A0", "Q8BGB8", "Q9VVG6", "P91428", "O13525", "O94453", "Q54CZ2",
        "Q9ZPR0", "Q8IIP1", "Q382H9", "A0A2K3DVY4", "Q7NKR1"]
EXPERIMENTAL = {"EXP", "IDA", "IMP", "IGI", "IPI", "IEP", "HDA", "HMP", "HGI", "HEP", "HTP"}


def get_json(url: str, name: str, params: dict | None = None) -> dict:
    """GET a JSON payload, cached under ``.cache/`` (delete the cache to refresh)."""
    CACHE.mkdir(parents=True, exist_ok=True)
    path = CACHE / name
    if path.exists():
        return json.loads(path.read_text())
    for attempt in range(4):
        try:
            r = requests.get(url, params=params, timeout=180,
                             headers={"Accept": "application/json"})
            r.raise_for_status()
            path.write_text(r.text)
            return r.json()
        except (requests.RequestException, ValueError) as e:
            print(f"{name}: {e}", file=sys.stderr)
            time.sleep(5 * (attempt + 1))
    raise SystemExit(f"could not fetch {name}")


def children(node: dict) -> list[dict]:
    ch = node.get("children", {}).get("annotation_node", [])
    return [ch] if isinstance(ch, dict) else ch


def accession(node: dict) -> str:
    for tok in node.get("node_name", "").split("|"):
        if tok.startswith("UniProtKB="):
            return tok.split("=", 1)[1]
    return ""


def index_tree(root: dict) -> tuple[dict, dict, dict]:
    """Return (nodes by PTN, parent PTN by PTN, leaf PTNs below each PTN)."""
    nodes: dict[str, dict] = {}
    parent: dict[str, str] = {}
    below: dict[str, list[str]] = {}

    def walk(n: dict, up: str | None) -> list[str]:
        pid = n["persistent_id"]
        nodes[pid] = n
        if up:
            parent[pid] = up
        kids = children(n)
        below[pid] = [pid] if not kids else [x for c in kids for x in walk(c, pid)]
        return below[pid]

    sys.setrecursionlimit(100000)
    walk(root, None)
    return nodes, parent, below


def label(n: dict) -> str:
    return n.get("species") or n.get("taxonomic_range") or "-"


def main() -> None:
    out: list[str] = []
    tree_payload = get_json(f"{PANTHER}/treeinfo", "treeinfo.json", {"family": FAMILY})
    root = tree_payload["search"]["tree_topology"]["annotation_node"]
    nodes, parent, below = index_tree(root)
    leaves = [p for p, n in nodes.items() if not children(n)]
    internal = [p for p in nodes if p not in leaves]
    out.append(f"# {FAMILY} family analysis")
    out.append(f"PANTHER release served: {tree_payload['search']['product']['version']}")
    out.append("")
    out.append("## 1. Tree")
    out.append(f"leaves {len(leaves)}; internal nodes {len(internal)}; "
               f"event types {dict(Counter(nodes[p].get('event_type') for p in internal))}")
    out.append(f"root {root['persistent_id']} event {root.get('event_type')}")
    for c in children(root):
        kind = "leaf" if not children(c) else f"{c.get('event_type')} {label(c)}"
        extra = f" UniProtKB:{accession(c)} {c.get('organism')}" if not children(c) else ""
        out.append(f"  root child {c['persistent_id']} {kind} leaves {len(below[c['persistent_id']])}{extra}")
    sf_nodes = [(p, n["sf_id"]) for p, n in nodes.items() if n.get("sf_id")]
    out.append("subfamily root nodes: " + "; ".join(
        f"{sf} at {p} ({nodes[p].get('event_type') or 'leaf'} {label(nodes[p])}, leaves {len(below[p])})"
        for p, sf in sf_nodes))

    def path_to_root(p: str) -> list[str]:
        chain = [p]
        while chain[-1] in parent:
            chain.append(parent[chain[-1]])
        return chain

    paint_rows = []
    with (HERE / f"{FAMILY}-paint.tsv").open() as fh:
        for row in csv.reader(fh, delimiter="\t"):
            if len(row) >= 6 and row[1].startswith("PTN"):
                paint_rows.append(row)
    out.append("")
    out.append("PAINT rows mapped on the tree:")
    for row in paint_rows:
        node, term, aspect, ev, neg = row[1:6]
        if node not in nodes:
            out.append(f"{ev} {node} {term}: NODE NOT IN TREE")
            continue
        n = nodes[node]
        inside = set(below[node])
        orgs = Counter(nodes[x].get("organism") for x in inside)
        out.append(f"{ev} {node} {term} {aspect} negated={neg}: {n.get('event_type')} "
                   f"{label(n)}; leaves {len(inside)} in {len(orgs)} species; "
                   f"path to root {' > '.join(path_to_root(node))}")
        sis = [c for c in children(nodes[parent[node]]) if c["persistent_id"] != node] if node in parent else []
        for s in sis:
            sp = s["persistent_id"]
            desc = (f"leaf UniProtKB:{accession(s)} {s.get('organism')}" if not children(s)
                    else f"{s.get('event_type')} {label(s)} leaves {len(below[sp])}")
            out.append(f"  sister of {node}: {sp} {desc}")
        for c in children(n):
            cp = c["persistent_id"]
            desc = (f"leaf UniProtKB:{accession(c)} {c.get('organism')}" if not children(c)
                    else f"{c.get('event_type')} {label(c)} leaves {len(below[cp])}")
            out.append(f"  child of {node}: {cp} {desc}")
    out.append("")
    out.append("Duplication nodes (parent taxon; leaves):")
    for p in internal:
        if nodes[p].get("event_type") == "DUPLICATION":
            up = parent.get(p)
            kids = ", ".join(f"{accession(nodes[x])}[{nodes[x].get('organism')}]" for x in below[p])
            out.append(f"  {p} under {up} ({label(nodes[up]) if up else '-'}): {kids}")
    out.append("")
    out.append("Leaves per first-level lineage below each child of the eukaryotic node:")
    for c in children(root):
        for g in children(c):
            for h in children(g) or [g]:
                hp = h["persistent_id"]
                out.append(f"  {c['persistent_id']} > {g['persistent_id']} ({label(g)}) > {hp} "
                           f"({label(h) if children(h) else nodes[hp].get('organism')}): leaves {len(below[hp])}")

    # ---- alignment ----
    msa_payload = get_json(f"{PANTHER}/familymsa", "familymsa.json", {"family": FAMILY})
    msa = {s["persistent_id"]: s["sequence"] for s in msa_payload["search"]["MSA_list"]["sequence_info"]}
    acc_of = {p: accession(nodes[p]) for p in leaves}
    ptn_of = {a: p for p, a in acc_of.items()}
    ref_entry = get_json(f"https://rest.uniprot.org/uniprotkb/{REFERENCE}.json", f"{REFERENCE}.json")
    ref_seq = ref_entry["sequence"]["value"]
    ref_version = ref_entry["entryAudit"]["sequenceVersion"]
    sites = []
    for f in ref_entry.get("features", []):
        if f["type"] == "Binding site":
            pos = f["location"]["start"]["value"]
            ev = sorted({f"{e.get('source')}:{e.get('id')}" for e in f.get("evidences", []) if e.get("id")})
            sites.append((pos, f.get("ligand", {}).get("name", ""), ev))
    ref_aln = msa[ptn_of[REFERENCE]]
    ungapped = "".join(ch for ch in ref_aln if ch.isalpha()).upper()
    out.append("")
    out.append("## 2. Alignment (PANTHER familymsa)")
    out.append(f"rows {len(msa)} (leaves {sum(p in msa for p in leaves)} of {len(leaves)}, the rest "
               f"reconstructed ancestral nodes); columns {len(ref_aln)}")
    out.append(f"reference UniProtKB:{REFERENCE} sequence version {ref_version} length {len(ref_seq)}; "
               f"alignment row equals the UniProt sequence: {ungapped == ref_seq}")
    col_of: dict[int, int] = {}
    i = 0
    for col, ch in enumerate(ref_aln):
        if ch.isalpha():
            i += 1
            col_of[i] = col
    site_cols = [(pos, col_of[pos], lig, ev) for pos, lig, ev in sites]
    for pos, col, lig, ev in site_cols:
        out.append(f"reference site {ref_seq[pos - 1]}{pos} ({lig}; {', '.join(ev)}) = alignment column {col + 1}")

    def own_pos(ptn: str, col: int) -> str:
        """Residue and own-sequence position of a row at an alignment column."""
        row = msa[ptn]
        ch = row[col]
        if not ch.isalpha():
            return "-"
        return f"{ch.upper()}{sum(c.isalpha() for c in row[:col + 1])}"

    if site_cols:
        lo, hi = min(c for _, c, _, _ in site_cols), max(c for _, c, _, _ in site_cols)
        ref_pattern = "".join(msa[ptn_of[REFERENCE]][c].upper() for _, c, _, _ in site_cols)
        out.append(f"reference residues at the site columns: {ref_pattern}; motif window = columns {lo + 1}-{hi + 1}")
        pat_count: Counter = Counter()
        deviants = []
        for p in leaves:
            if p not in msa:
                deviants.append((p, "NOT IN ALIGNMENT"))
                continue
            pat = "".join(msa[p][c].upper() if msa[p][c].isalpha() else "-" for _, c, _, _ in site_cols)
            pat_count[pat] += 1
            if pat != ref_pattern:
                deviants.append((p, pat))
        out.append(f"site-column patterns over leaves: {dict(pat_count)}")
        for row in paint_rows:
            node = row[1]
            if node in nodes:
                inside = [p for p in below[node] if p in msa]
                ok = sum("".join(msa[p][c].upper() for _, c, _, _ in site_cols) == ref_pattern for p in inside)
                out.append(f"  under {node}: {ok} of {len(inside)} aligned leaves carry {ref_pattern}")
        for p, sf in sf_nodes:
            inside = [x for x in below[p] if x in msa]
            ok = sum("".join(msa[x][c].upper() for _, c, _, _ in site_cols) == ref_pattern for x in inside)
            out.append(f"  under subfamily node {p} ({sf}): {ok} of {len(inside)} aligned leaves carry {ref_pattern}")
        out.append("Leaves deviating at a site column (own-sequence numbering from the PANTHER alignment row; "
                   "branch length to parent; aligned residues of the row):")
        for p, pat in deviants:
            n = nodes[p]
            if p not in msa:
                out.append(f"  {p} UniProtKB:{acc_of[p]} {n.get('organism')}: {pat}")
                continue
            res = " ".join(own_pos(p, c) for _, c, _, _ in site_cols)
            window = msa[p][lo:hi + 1].replace(".", "")
            out.append(f"  {p} UniProtKB:{acc_of[p]} {n.get('organism')} {n.get('sf_id') or ''} pattern {pat} "
                       f"[{res}] branch {n.get('branch_length')} residues {sum(c.isalpha() for c in msa[p])} "
                       f"window {window}")
        # Is a deviation real, or a property of the sequence PANTHER aligned? Compare each
        # deviant row with the current UniProt entry and search it for the reference motif.
        first = site_cols[0][0]
        motif_re = "".join(
            ref_seq[pos - 1] if pos in {s[0] for s in site_cols} else "."
            for pos in range(first, site_cols[-1][0] + 1))
        out.append(f"motif of the reference as a regular expression: {motif_re}")
        out.append("Deviant leaves against their current UniProt entry:")
        for p, _pat in deviants:
            a = acc_of[p]
            r = requests.get(f"https://rest.uniprot.org/uniprotkb/{a}.json", timeout=60)
            entry = r.json() if r.ok else {}
            if "sequence" not in entry:
                out.append(f"  UniProtKB:{a}: no current sequence in UniProt "
                           f"({entry.get('entryType', 'not found')}; "
                           f"{(entry.get('inactiveReason') or {}).get('inactiveReasonType', '-')})")
                continue
            seq = entry["sequence"]["value"]
            row = "".join(c for c in msa.get(p, "") if c.isalpha()).upper()
            m = re.search(motif_re, seq)
            cautions = [t["value"] for c in entry.get("comments", []) if c["commentType"] == "CAUTION"
                        for t in c.get("texts", [])]
            out.append(f"  UniProtKB:{a} {entry['entryType']}; {entry.get('proteinExistence')}; UniProt length "
                       f"{len(seq)} (sequence version {entry['entryAudit']['sequenceVersion']}); PANTHER row "
                       f"{len(row)} residues, identical to UniProt: {row == seq}, contained in UniProt: {row in seq}; "
                       f"motif in UniProt sequence: {f'{m.group(0)}@{m.start() + 1}' if m else 'none'}"
                       + (f"; UniProt caution: {' '.join(cautions)}" if cautions else ""))
        out.append("Motif window of selected leaves (gap-only columns of the family removed; own numbering of site residues):")
        for a in SHOW:
            p = ptn_of.get(a)
            if p is None or p not in msa:
                out.append(f"  UniProtKB:{a}: not a leaf of the alignment")
                continue
            res = " ".join(own_pos(p, c) for _, c, _, _ in site_cols)
            window = msa[p][lo:hi + 1].replace(".", "")
            out.append(f"  UniProtKB:{a} {nodes[p].get('organism')}: {window} [{res}] residues {sum(c.isalpha() for c in msa[p])}")
        out.append("Reconstructed ancestral rows at the PAINT nodes and the root:")
        for p in dict.fromkeys([root["persistent_id"]] + [r[1] for r in paint_rows]):
            if p in msa:
                out.append(f"  {p}: {msa[p][lo:hi + 1].replace('.', '')} "
                           f"[{''.join(msa[p][c].upper() if msa[p][c].isalpha() else '-' for _, c, _, _ in site_cols)}]")
            else:
                out.append(f"  {p}: no ancestral row in the alignment")
        # column conservation over the whole reference sequence
        full = [p for p in leaves if p in msa]
        cons = []
        for pos, col in col_of.items():
            cnt = Counter(msa[p][col].upper() for p in full if msa[p][col].isalpha())
            if cnt:
                aa, n_ = cnt.most_common(1)[0]
                if n_ / len(full) >= 0.95:
                    cons.append(f"{ref_seq[pos - 1]}{pos}({aa} {n_}/{len(full)})")
        out.append(f"Reference positions whose column is >=95% one residue over all {len(full)} leaves: " + " ".join(cons))

    # ---- experimental annotations ----
    out.append("")
    out.append("## 3. Experimental GO annotations of tree leaves (QuickGO)")
    accs = sorted(a for a in acc_of.values() if a)
    hits = []
    total = 0
    for k in range(0, len(accs), 40):
        chunk = accs[k:k + 40]
        page = 1
        while True:
            data = get_json(QUICKGO, f"quickgo-{k}-{page}.json",
                            {"geneProductId": ",".join(chunk), "limit": 200, "page": page})
            total += len(data["results"])
            hits.extend(r for r in data["results"] if r["goEvidence"] in EXPERIMENTAL)
            if page >= data["pageInfo"]["total"]:
                break
            page += 1
    out.append(f"annotation rows returned for {len(accs)} leaf accessions: {total} (all evidence codes); "
               f"experimental rows: {len(hits)}")
    ref_rows = [r for r in hits if r["geneProductId"].endswith(REFERENCE)]
    out.append(f"positive control: experimental rows on UniProtKB:{REFERENCE}: {len(ref_rows)}")
    paint_nodes = list(dict.fromkeys(r[1] for r in paint_rows if r[1] in nodes))
    seen = set()
    for r in sorted(hits, key=lambda r: (r["goAspect"], r["goId"], r["geneProductId"], r["reference"])):
        a = r["geneProductId"].split(":")[1].split("-")[0]
        key = (a, r["goId"], r["goEvidence"], r["reference"], r["qualifier"])
        if key in seen or a not in ptn_of:
            continue
        seen.add(key)
        p = ptn_of[a]
        under = [x for x in paint_nodes if p in below[x]]
        out.append(f"  {r['goAspect'][:1].upper()} {r['goId']} {r['qualifier']} {r['goEvidence']} "
                   f"{r['reference']} UniProtKB:{a} {r.get('symbol')} [{nodes[p].get('organism')}] "
                   f"assigned_by {r['assignedBy']} under {','.join(under) or 'no PAINT node'}")
    (HERE / f"{FAMILY}-analysis.txt").write_text("\n".join(out) + "\n")
    print("\n".join(out))


if __name__ == "__main__":
    main()
