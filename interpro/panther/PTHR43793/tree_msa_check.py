"""Tree, alignment and annotation check for this PANTHER family.

Run from the repository root:

    uv run python interpro/panther/PTHR43793/tree_msa_check.py

The family is the name of the folder holding this script. Everything in the report is
read from a service at run time; nothing about the result is written in this file. The
only inputs chosen by hand are the accessions in ``ANCHORS`` and ``COMPARATORS`` (which
proteins to measure against), never a residue, a count or a verdict.

Sources, all fetched and cached under the git-ignored ``.cache/family_checks/<FAMILY>/``:

* PANTHER ``treeinfo`` (topology, event type and species of every node) and
  ``familymsa`` (PANTHER's own family alignment). The release each response names is
  checked against the repository's pinned ``PANTHER_RELEASE``.
* UniProt REST (sequence, sequence version, names, features, cross-references).
* QuickGO (IBA rows with their PTN source; experimental rows).

Sections of ``<FAMILY>-tree-msa-check.txt``:

1. TREE      every node with event, species and leaf count; every leaf.
2b.          leaves the ``OTHER_TREES`` trees hold from the same genomes (shows where a
             genome's paralogue of a leaf was placed).
2. PAINT     each row of ``<FAMILY>-paint.tsv``: whether the node is in this tree and
             which leaves sit below it; for a node that is not, the family whose tree
             it roots or sits in, when one of ``OTHER_TREES`` holds it.
3. IBA       the PTN source of every IBA row carried by a tree leaf or a reviewed
             member in ``<FAMILY>-entries.csv`` (this is what explains a foreign node
             in the PAINT slice).
4. MSA       residues of every leaf at the alignment columns of the anchor protein's
             UniProt binding-site and mutagenesis positions. A lower-case letter is a
             PANTHER insert state (not aligned to the column); it is reported as such.
5. PAIRWISE  global BLOSUM62 alignments of selected leaves to characterised
             comparators: identity, and the residues aligned to the comparator's
             mutagenesis positions.
6. EXP       experimental GO rows of leaves and comparators, after a positive control.
"""

from __future__ import annotations

import csv
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

import requests
from Bio.Align import PairwiseAligner, substitution_matrices

from ai_gene_review.etl.panther_families import PANTHER_RELEASE, same_release
from ai_gene_review.etl.panther_trees import served_release

HERE = Path(__file__).resolve().parent
FAMILY = HERE.name
CACHE = Path(".cache") / "family_checks" / FAMILY
PANTHER_API = "https://pantherdb.org/services/oai/pantherdb"
UNIPROT = "https://rest.uniprot.org/uniprotkb"
QUICKGO = "https://www.ebi.ac.uk/QuickGO/services/annotation/search"

# Anchor for alignment columns: the member with curated UniProt binding-site and
# mutagenesis features (B. subtilis TagD, the structural prototype of the fold).
ANCHORS = ["P27623"]
# Characterised proteins the leaves are compared with pairwise. Q58579 is the assayed
# archaeal FAD synthase (a tree leaf); Q9UYT0 and Q5JHE8 are the assayed archaeal
# phosphopantetheine adenylyltransferases (not leaves of this tree).
COMPARATORS = ["Q58579", "Q9UYT0", "Q5JHE8"]
# Families whose trees are searched for PAINT nodes that are not in this family's tree.
OTHER_TREES = ["PTHR10695", "PTHR46969"]
# Positive control for the experimental-annotation query: must return a row.
POSITIVE_CONTROL = ("Q58579", "GO:0003919")
FEATURE_TYPES = ("Binding site", "Mutagenesis")


def cached_json(name: str, url: str, params: dict | None = None) -> Any:
    """Fetch JSON once and keep it under the git-ignored cache."""
    CACHE.mkdir(parents=True, exist_ok=True)
    path = CACHE / name
    if path.exists():
        return json.loads(path.read_text())
    r = requests.get(url, params=params, headers={"Accept": "application/json"}, timeout=300)
    r.raise_for_status()
    path.write_text(r.text)
    return r.json()


def panther(service: str, family: str) -> Any:
    """A PANTHER service response for ``family``, refused unless it is the pinned release."""
    payload = cached_json(f"{service}-{family}.json", f"{PANTHER_API}/{service}", {"family": family})
    served = served_release(payload)
    if served is None or not same_release(served, PANTHER_RELEASE):
        raise SystemExit(f"{service} {family}: served release {served!r}, pinned {PANTHER_RELEASE}")
    return payload


def children(node: dict) -> list[dict]:
    """Child nodes (the API returns a dict for a single child)."""
    ch = node.get("children", {}).get("annotation_node", [])
    return [ch] if isinstance(ch, dict) else ch


def flatten(family: str) -> tuple[list[dict], dict[str, list[str]]]:
    """Pre-order node records of a family tree, and the leaf ids below each node."""
    root = panther("treeinfo", family)["search"]["tree_topology"]["annotation_node"]
    nodes: list[dict] = []
    below: dict[str, list[str]] = {}

    def walk(n: dict, depth: int, parent: str) -> list[str]:
        pid = n["persistent_id"]
        rec = {
            "id": pid,
            "depth": depth,
            "parent": parent,
            "event": n.get("event_type", ""),
            "species": n.get("species") or "",
            "sf": n.get("prop_sf_id", "") or n.get("sf_id", ""),
            "leaf": not children(n),
        }
        nodes.append(rec)
        if rec["leaf"]:
            name = n.get("node_name", "")
            rec["acc"] = next(
                (t.split("=", 1)[1] for t in name.split("|") if t.startswith("UniProtKB=")), ""
            )
            rec["org"] = n.get("organism", "")
            rec["symbol"] = n.get("gene_symbol", "")
            below[pid] = [pid]
            return [pid]
        got: list[str] = []
        for c in children(n):
            got.extend(walk(c, depth + 1, pid))
        below[pid] = got
        return got

    walk(root, 0, "")
    return nodes, below


def uniprot(acc: str) -> dict:
    """The UniProt JSON record for an accession."""
    return cached_json(f"uniprot-{acc}.json", f"{UNIPROT}/{acc}.json")


def protein_name(rec: dict) -> str:
    """Recommended or submitted name of a UniProt record."""
    desc = rec.get("proteinDescription", {})
    if "recommendedName" in desc:
        return desc["recommendedName"]["fullName"]["value"]
    sub = desc.get("submissionNames") or [{}]
    return sub[0].get("fullName", {}).get("value", "")


def xrefs(rec: dict, databases: tuple[str, ...]) -> str:
    """Cross-reference ids of the named databases, space separated."""
    return " ".join(
        x["id"] for x in rec.get("uniProtKBCrossReferences", []) if x["database"] in databases
    )


def features(rec: dict) -> list[tuple[str, int, int, str]]:
    """Binding-site and mutagenesis features as (type, start, end, text)."""
    out = []
    for f in rec.get("features", []):
        if f["type"] in FEATURE_TYPES:
            text = f.get("description", "") or f.get("ligand", {}).get("name", "")
            alt = f.get("alternativeSequence", {})
            if alt:
                text = f"{alt.get('originalSequence', '')}->{','.join(alt.get('alternativeSequences', []))}: {text}"
            out.append((f["type"], f["location"]["start"]["value"], f["location"]["end"]["value"], text))
    return out


def quickgo(accs: list[str], extra: dict) -> list[dict]:
    """All QuickGO rows for the accessions with the given filter (paged)."""
    rows: list[dict] = []
    for i in range(0, len(accs), 40):
        page = 1
        while True:
            params = {"geneProductId": ",".join(accs[i : i + 40]), "limit": 200, "page": page, **extra}
            r = requests.get(QUICKGO, params=params, headers={"Accept": "application/json"}, timeout=120)
            r.raise_for_status()
            data = r.json()
            rows.extend(data["results"])
            if page >= data["pageInfo"]["total"]:
                break
            page += 1
    return rows


def ptn_sources(row: dict) -> list[str]:
    """PTN ids in a QuickGO row's with/from."""
    return [
        x["id"]
        for grp in row.get("withFrom") or []
        for x in grp["connectedXrefs"]
        if x["db"] == "PANTHER"
    ]


def column_of(aligned: str, position: int) -> int | None:
    """Alignment column holding the 1-based residue ``position`` of a gapped sequence."""
    seen = 0
    for col, ch in enumerate(aligned):
        if ch not in "-.":
            seen += 1
            if seen == position:
                return col
    return None


def residue_number(aligned: str, col: int) -> int:
    """1-based residue number of the residue at ``col`` (gaps not counted)."""
    return sum(1 for ch in aligned[: col + 1] if ch not in "-.")


def pairwise(a: str, b: str) -> tuple[int, int, dict[int, tuple[int, str]]]:
    """Global BLOSUM62 alignment of a to b: identities, aligned pairs, b position -> (a position, a residue)."""
    aligner = PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score, aligner.extend_gap_score = -10, -0.5
    aligner.end_gap_score = 0  # do not penalise the unaligned tails of a longer protein
    aln = aligner.align(a, b)[0]
    ident = pairs = 0
    b_to_a: dict[int, tuple[int, str]] = {}
    for (a0, a1), (b0, b1) in zip(*aln.aligned):
        for i, j in zip(range(a0, a1), range(b0, b1)):
            pairs += 1
            ident += a[i] == b[j]
            b_to_a[j + 1] = (i + 1, a[i])
    return ident, pairs, b_to_a


def main() -> None:
    """Write the report for FAMILY."""
    out: list[str] = []
    nodes, below = flatten(FAMILY)
    by_id = {n["id"]: n for n in nodes}
    leaves = [n for n in nodes if n["leaf"]]
    recs = {n["acc"]: uniprot(n["acc"]) for n in leaves}

    out.append(f"# {FAMILY} tree and alignment check (PANTHER release {PANTHER_RELEASE})")
    out.append("")
    out.append(f"## 1. TREE: {len(leaves)} leaves, {len(nodes) - len(leaves)} internal nodes")
    for n in nodes:
        pad = "  " * n["depth"]
        if n["leaf"]:
            r = recs[n["acc"]]
            out.append(
                f"{pad}leaf {n['id']} UniProtKB:{n['acc']} {n['symbol'] or '-'} | {n['org']} | "
                f"{protein_name(r)} | {r['sequence']['length']} aa | {n['sf']} | "
                f"{xrefs(r, ('HAMAP', 'NCBIfam', 'Pfam'))}"
            )
        else:
            sf = Counter(by_id[x]["sf"] for x in below[n["id"]])
            out.append(
                f"{pad}node {n['id']} {n['event']} species={n['species'] or '-'} "
                f"leaves={len(below[n['id']])} ({', '.join(f'{k}={v}' for k, v in sorted(sf.items()))})"
            )

    out.append("")
    out.append("## 2. PAINT rows mapped onto the tree")
    other = {fam: flatten(fam) for fam in OTHER_TREES}
    with (HERE / f"{FAMILY}-paint.tsv").open() as fh:
        paint = [r for r in csv.reader(fh, delimiter="\t") if len(r) > 5 and r[1].startswith("PTN")]
    for row in paint:
        node, term, evidence, negated = row[1], row[2], row[4], row[5]
        if node in by_id:
            got = below[node]
            n = by_id[node]
            out.append(
                f"{evidence} {node} {term} negated={negated}: IN TREE, {n['event']} "
                f"species={n['species'] or '-'}, {len(got)} of {len(leaves)} leaves below: "
                + " ".join(by_id[x]["acc"] for x in got)
            )
        else:
            where = []
            for fam, (onodes, obelow) in other.items():
                hit = next((x for x in onodes if x["id"] == node), None)
                if hit:
                    role = "root" if not hit["parent"] else "internal node"
                    where.append(
                        f"{role} of the {fam} tree (species={hit['species'] or '-'}, "
                        f"{len(obelow[node])} of {sum(x['leaf'] for x in onodes)} leaves below)"
                    )
            out.append(
                f"{evidence} {node} {term} negated={negated}: NOT IN THE {FAMILY} TREE; "
                + ("; ".join(where) if where else f"not found in {', '.join(OTHER_TREES)}")
            )

    out.append("")
    out.append("## 2b. Leaves of the other trees from the genomes of this tree's leaves")
    orgs = sorted({n["org"] for n in leaves})
    for fam, (onodes, _) in other.items():
        hits = [x for x in onodes if x["leaf"] and x["org"] in orgs]
        out.append(f"{fam}: {len(hits)} leaves from {len({x['org'] for x in hits})} of the {len(orgs)} genomes")
        for x in hits:
            path, cur = [], x["parent"]
            lookup = {y["id"]: y for y in onodes}
            while cur:
                path.append(f"{cur}:{lookup[cur]['species'] or lookup[cur]['event']}")
                cur = lookup[cur]["parent"]
            r = uniprot(x["acc"])
            out.append(
                f"  {x['org']}: UniProtKB:{x['acc']} {x['symbol'] or '-'} | {protein_name(r)} | "
                f"{r['sequence']['length']} aa | {xrefs(r, ('HAMAP',))} | below {' < '.join(path[:3])}"
            )
        missing = [o for o in orgs if o not in {x["org"] for x in hits}]
        out.append(f"  genomes of this tree with no leaf in {fam}: {'; '.join(missing)}")

    out.append("")
    out.append("## 3. IBA rows carried by tree leaves and reviewed members, with PTN source")
    with (HERE / f"{FAMILY}-entries.csv").open() as fh:
        members = list(csv.DictReader(fh))
    leaf_accs = [n["acc"] for n in leaves]
    all_accs = leaf_accs + [m["id"] for m in members if m["id"] not in leaf_accs]
    iba = quickgo(all_accs, {"evidenceCode": "ECO:0000318"})
    per_node: dict[tuple[str, str], list[str]] = defaultdict(list)
    for r in iba:
        acc = r["geneProductId"].split(":")[1]
        for ptn in ptn_sources(r):
            per_node[(ptn, r["goId"])].append(acc)
    names = {m["id"]: (m["gene"] or "-", m["name"], m["length"]) for m in members}
    for (ptn, go), accs in sorted(per_node.items()):
        status = "in this tree" if ptn in by_id else "NOT in this tree"
        accs = sorted(set(accs))
        in_tree = [a for a in accs if a in leaf_accs]
        out.append(f"{ptn} ({status}) {go}: {len(accs)} recipients, {len(in_tree)} of them tree leaves")
        for a in accs:
            if a in leaf_accs:
                n = next(x for x in leaves if x["acc"] == a)
                out.append(f"  {a} tree leaf {n['id']} {n['symbol'] or '-'} | {protein_name(recs[a])}")
            else:
                g, nm, ln = names[a]
                out.append(f"  {a} reviewed member, not a leaf of this tree: {g} | {nm} | {ln} aa")
    no_iba = [a for a in leaf_accs if not any(a in v for v in per_node.values())]
    out.append(f"tree leaves with no IBA row: {' '.join(no_iba) or 'none'}")

    out.append("")
    out.append("## 4. MSA: PANTHER family alignment at the anchor's UniProt feature positions")
    msa = {
        x["persistent_id"]: x["sequence"]
        for x in panther("familymsa", FAMILY)["search"]["MSA_list"]["sequence_info"]
    }
    mismatch = [
        n["acc"]
        for n in leaves
        if msa[n["id"]].replace("-", "").replace(".", "").upper() != recs[n["acc"]]["sequence"]["value"]
    ]
    out.append(
        f"alignment rows {len(msa)} ({len(leaves)} leaves plus reconstructed internal nodes); "
        f"columns {len(next(iter(msa.values())))}; leaf rows that differ from the current UniProt "
        f"sequence: {' '.join(mismatch) or 'none'}"
    )
    for anchor in ANCHORS:
        arec = uniprot(anchor)
        aleaf = next(n for n in leaves if n["acc"] == anchor)
        arow = msa[aleaf["id"]]
        positions: dict[int, list[str]] = defaultdict(list)
        for ftype, start, end, text in features(arec):
            for p in range(start, end + 1):
                positions[p].append(f"{ftype}: {text}" if text else ftype)
        out.append(
            f"anchor UniProtKB:{anchor} ({protein_name(arec)}), sequence version "
            f"{arec['entryAudit']['sequenceVersion']}; positions are its UniProt binding-site and "
            "mutagenesis features"
        )
        for p in sorted(positions):
            out.append(f"  {anchor} {arec['sequence']['value'][p - 1]}{p}: {'; '.join(sorted(set(positions[p])))}")
        out.append("  residue at each anchor position, as residue+number in the leaf's own sequence")
        out.append("  (lower case = PANTHER insert state, not aligned; '-' = gap):")
        out.append("  " + "leaf".ljust(14) + " ".join(f"{anchor[-3:]}:{p}".rjust(7) for p in sorted(positions)))
        tally: dict[int, Counter] = defaultdict(Counter)
        for n in leaves:
            row = msa[n["id"]]
            cells = []
            for p in sorted(positions):
                col = column_of(arow, p)
                ch = row[col] if col is not None else "?"
                if ch in "-.":
                    cells.append("-")
                else:
                    cells.append(f"{ch}{residue_number(row, col)}")
                tally[p][ch.upper() if ch.isupper() else ("-" if ch in "-." else "insert")] += 1
            out.append("  " + n["acc"].ljust(14) + " ".join(c.rjust(7) for c in cells))
        out.append("  column composition over the leaves:")
        for p in sorted(positions):
            comp = ", ".join(f"{k}={v}" for k, v in tally[p].most_common())
            out.append(f"  {anchor} {arec['sequence']['value'][p - 1]}{p}: {comp}")

    out.append("")
    out.append("## 5. PAIRWISE: global BLOSUM62 alignments to characterised comparators")
    comps = {c: uniprot(c) for c in COMPARATORS}
    for c, crec in comps.items():
        out.append(
            f"comparator UniProtKB:{c} {protein_name(crec)} | {crec['organism']['scientificName']} | "
            f"{crec['sequence']['length']} aa | sequence version {crec['entryAudit']['sequenceVersion']} | "
            f"{xrefs(crec, ('PANTHER', 'HAMAP'))}"
        )
    out.append("identity = identical aligned pairs / aligned pairs (aligned pairs in brackets)")
    out.append("leaf".ljust(14) + " ".join(c.rjust(16) for c in COMPARATORS))
    mut_positions = {
        c: sorted({s for t, s, e, _ in features(crec) if t == "Mutagenesis" and s == e})
        for c, crec in comps.items()
    }
    site_lines: list[str] = []
    for n in leaves:
        seq = recs[n["acc"]]["sequence"]["value"]
        cells = []
        for c, crec in comps.items():
            ident, pairs, b_to_a = pairwise(seq, crec["sequence"]["value"])
            cells.append(f"{100 * ident / pairs:.1f}% ({pairs})")
            if mut_positions[c]:
                got = []
                for p in mut_positions[c]:
                    ref = crec["sequence"]["value"][p - 1]
                    got.append(f"{ref}{p}->" + (f"{b_to_a[p][1]}{b_to_a[p][0]}" if p in b_to_a else "gap"))
                site_lines.append(f"  {n['acc']} vs {c}: " + " ".join(got))
        out.append(n["acc"].ljust(14) + " ".join(x.rjust(16) for x in cells))
    out.append("residues aligned to the comparators' single-residue mutagenesis positions:")
    out.extend(site_lines)
    out.append("cysteine count in the last 40 residues of each leaf:")
    for n in leaves:
        seq = recs[n["acc"]]["sequence"]["value"]
        tail = seq[-40:]
        where = " ".join(f"C{len(seq) - 40 + i + 1}" for i, ch in enumerate(tail) if ch == "C")
        out.append(f"  {n['acc']} {n['sf']} {len(seq)} aa: {tail.count('C')} {where}")

    out.append("")
    out.append("## 6. EXP: experimental GO rows (QuickGO, ECO:0000269 and descendants)")
    acc, go = POSITIVE_CONTROL
    control = [
        r for r in quickgo([acc], {"goId": go, "evidenceCode": "ECO:0000269", "evidenceCodeUsage": "descendants"})
    ]
    if not control:
        raise SystemExit(f"positive control {acc} {go} returned nothing: the query cannot be trusted")
    out.append(f"positive control {acc} {go}: {len(control)} row(s) returned, so an empty result below is real")
    exp = quickgo(
        leaf_accs + [c for c in COMPARATORS if c not in leaf_accs] + [m["id"] for m in members if m["id"] not in leaf_accs],
        {"evidenceCode": "ECO:0000269", "evidenceCodeUsage": "descendants"},
    )
    seen = set()
    for r in sorted(exp, key=lambda r: (r["geneProductId"], r["goId"])):
        key = (r["geneProductId"], r["goId"], r["qualifier"], r["goEvidence"], r["reference"])
        if key in seen:
            continue
        seen.add(key)
        out.append(f"  {r['geneProductId']} {r['qualifier']} {r['goId']} {r['goEvidence']} {r['reference']} {r['assignedBy']}")
    with_exp = {r["geneProductId"].split(":")[1] for r in exp}
    out.append(
        f"tree leaves with any experimental GO row: {' '.join(a for a in leaf_accs if a in with_exp) or 'none'} "
        f"({sum(a in with_exp for a in leaf_accs)} of {len(leaf_accs)})"
    )

    (HERE / f"{FAMILY}-tree-msa-check.txt").write_text("\n".join(out) + "\n")
    print(f"wrote {FAMILY}-tree-msa-check.txt ({len(out)} lines)", file=sys.stderr)


if __name__ == "__main__":
    main()
