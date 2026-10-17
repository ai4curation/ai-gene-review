#!/usr/bin/env python3
"""Trace a TreeGrafter term from the graft node up to the PAINT IBD it came from.

A TreeGrafter row names the PANTHER node the protein was grafted onto
(``PANTHER:PTN...`` in GOA WITH/FROM), not the node the GO term was placed on
by a PAINT curator. This script fetches the live PANTHER family tree, finds the
nearest ancestor of the graft node that carries an IBA for the same GO term,
and reports:

  * the path from that IBD node down to the graft node, with each node's
    event type (speciation / duplication) and taxonomic range;
  * the experimental "seed" genes cited in the IBA's WITH/FROM;
  * for each child clade of the IBD node: its size, its PANTHER subfamily
    names and the commonest leaf definitions, so one can see which clades
    inherit the term and what their members actually are.

Inputs are the cases in ``CASES`` below (the corpus examples used on the
project page and in the brief). The IBD is located by querying QuickGO for
IBA rows (GO_REF:0000033) on a sample of the family's leaves; leaves are
sampled from the graft node's ancestors outward, so the nearest IBD is found
first. Needs network access (PANTHER API and QuickGO).

Output: ``graft_paths.yaml`` next to this script.

``--all`` instead traces every reviewed TreeGrafter annotation in
``treegrafter_review.tsv`` against local copies of the PANTHER 19 trees (the
``Tree_MSF/*.tree`` files of PANTHER's TreeGrafter data download), PAINT's
current ``IBD.gaf`` and ``PAINT_TreeGrafter_Annotations_TOTAL.txt.gz`` (AN to
PTN map, and the GO set TreeGrafter now assigns at each node). Only the
taxonomy is fetched live: query lineages and the check that a PANTHER clade
name is an NCBI taxon name use the UniProt taxonomy API (cached per run). It writes one
row per annotation to ``graft_paths_all.tsv``: the nearest same-term IBD
ancestor (a NOT IBD met first blocks inheritance), the tree steps from it to
the graft node, its event type and taxon, whether it is the family root,
whether a duplication lies between, its leaf count and seeds, and whether
the term is still in the graft node's current TreeGrafter set. The online API
proved too slow for a full run (many families time out).

Downloads (see https://data.pantherdb.org/ftp/downloads/):
  TreeGrafter/PANTHER19.0_data_trees_hmms_only.tar.gz  (3 GB; only
      PANTHER19.0_data/Tree_MSF/*.tree is needed)
  paint/current/IBD.gaf
  paint/current/PAINT_TreeGrafter_Annotations_TOTAL.txt.gz

Run:
  python3 projects/TREEGRAFTER/trace_graft_paths.py
  python3 projects/TREEGRAFTER/trace_graft_paths.py --all \
      --panther-trees PANTHER19.0_data/Tree_MSF --ibd-gaf IBD.gaf \
      --paint-total PAINT_TreeGrafter_Annotations_TOTAL.txt.gz
"""
from __future__ import annotations

import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "graft_paths.yaml")
PANTHER = "https://www.pantherdb.org/services/oai/pantherdb/treeinfo"
QUICKGO = "https://www.ebi.ac.uk/QuickGO/services/annotation/search"

# gene, review file, family, GO term, graft node(s): all from treegrafter_placement.tsv
CASES = [
    {"case": "purM", "gene": "PSEPK/purM", "family": "PTHR10520",
     "term": "GO:0004637", "label": "phosphoribosylamine-glycine ligase activity",
     "grafts": ["PTN002237315"]},
    {"case": "moeB", "gene": "PSEPK/moeB", "family": "PTHR10953",
     "term": "GO:0004792", "label": "thiosulfate-cyanide sulfurtransferase activity",
     "grafts": ["PTN002250299"]},
    {"case": "moaA", "gene": "PSEPK/moaA", "family": "PTHR22960",
     "term": "GO:0061799", "label": "cyclic pyranopterin monophosphate synthase activity",
     "grafts": ["PTN002344120"]},
    {"case": "fliI_sctN", "gene": "CAUVC,HELPJ,PSEPK/fliI; SHIFL,YEREN/sctN",
     "family": "PTHR15184", "term": "GO:0046933",
     "label": "proton-transporting ATP synthase activity, rotational mechanism",
     "grafts": ["PTN000390110", "PTN002689426", "PTN002309653",
                "PTN001807734", "PTN001807733"]},
    {"case": "dapE", "gene": "PSEPK/dapE", "family": "PTHR43808",
     "term": "GO:0008777", "label": "acetylornithine deacetylase activity",
     "grafts": ["PTN002887524"]},
    {"case": "mdh", "gene": "PSEPK/mdh", "family": "PTHR43128",
     "term": "GO:0004459", "label": "L-lactate dehydrogenase (NAD+) activity",
     "grafts": ["PTN002454946"]},
    {"case": "eryAIII", "gene": "SACEN/eryAIII", "family": "PTHR43775",
     "term": "GO:0004312", "label": "fatty acid synthase activity",
     "grafts": ["PTN000918870"]},
]


def _get(url: str, timeout: int = 300) -> str:
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "ai-gene-review/treegrafter"})
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read().decode()
        except Exception:
            if attempt == 3:
                raise
            time.sleep(2 ** attempt)


def kids(n: dict) -> list:
    c = n.get("children", {}).get("annotation_node", [])
    return [c] if isinstance(c, dict) else c


def index(root: dict):
    parent, nodes = {}, {}
    stack = [root]
    while stack:
        n = stack.pop()
        nodes[n["persistent_id"]] = n
        for c in kids(n):
            parent[c["persistent_id"]] = n["persistent_id"]
            stack.append(c)
    return nodes, parent


def leaves_under(n: dict) -> list:
    out, stack = [], [n]
    while stack:
        x = stack.pop()
        ch = kids(x)
        if not ch:
            out.append(x)
        stack.extend(ch)
    return out


def accession(leaf: dict) -> str:
    m = re.search(r"UniProtKB=(\w+)", leaf.get("node_name", ""))
    return m.group(1) if m else ""


def iba_rows(accs: list[str], term: str) -> list:
    rows = []
    for i in range(0, len(accs), 50):
        params = {"geneProductId": ",".join(accs[i:i + 50]), "goId": term,
                  "goUsage": "exact", "reference": "GO_REF:0000033", "limit": 200}
        d = json.loads(_get(f"{QUICKGO}?{urllib.parse.urlencode(params)}"))
        rows.extend(d.get("results", []))
    return rows


def with_ids(row: dict) -> list[str]:
    return [f"{x['db']}:{x['id']}" for w in (row.get("withFrom") or [])
            for x in w["connectedXrefs"]]


def describe(n: dict) -> dict:
    return {k: n.get(k) for k in ("persistent_id", "event_type", "taxonomic_range",
                                  "species", "sf_id", "sf_name", "gene_symbol",
                                  "organism", "definition") if n.get(k)}


def trace(case: dict) -> dict:
    tree = json.loads(_get(f"{PANTHER}?{urllib.parse.urlencode({'family': case['family']})}"))
    root = tree["search"]["tree_topology"]["annotation_node"]
    nodes, parent = index(root)
    out = {"case": case["case"], "gene": case["gene"], "family": case["family"],
           "family_name": root.get("sf_name", ""), "term": f"{case['term']} {case['label']}",
           "family_leaves": len(leaves_under(root)), "grafts": []}
    ibd_nodes: dict = {}
    for g in case["grafts"]:
        if g not in nodes:
            out["grafts"].append({"graft": g, "error": "not in current PANTHER tree"})
            continue
        path = [g]
        while path[-1] in parent:
            path.append(parent[path[-1]])
        found = None
        # widen outward from the graft node, querying leaves under each ancestor
        seen: set = set()
        for anc in path:
            accs = [a for a in (accession(l) for l in leaves_under(nodes[anc])) if a and a not in seen]
            seen.update(accs)
            for r in iba_rows(accs, case["term"]):
                for w in with_ids(r):
                    ptn = w.split(":", 1)[1]
                    if w.startswith("PANTHER:") and ptn in path:
                        ibd_nodes.setdefault(ptn, set()).update(
                            x for x in with_ids(r) if not x.startswith("PANTHER:"))
                        if found is None or path.index(ptn) < path.index(found):
                            found = ptn
            if found:
                break
        rec = {"graft": g, "graft_node": describe(nodes[g])}
        if found:
            steps = path[:path.index(found) + 1]
            rec["ibd"] = found
            rec["steps_from_ibd"] = len(steps) - 1
            rec["path_ibd_to_graft"] = [describe(nodes[p]) for p in reversed(steps)]
        else:
            rec["ibd"] = None
        out["grafts"].append(rec)
    out["ibd_nodes"] = []
    for ptn, seeds in ibd_nodes.items():
        n = nodes[ptn]
        clades = []
        for c in kids(n):
            lv = leaves_under(c)
            defs = Counter(l.get("definition", "") for l in lv)
            sfs = Counter(l.get("sf_name", "") for l in lv)
            clades.append({
                "child": c["persistent_id"], "event_type": c.get("event_type", "LEAF"),
                "taxonomic_range": c.get("taxonomic_range", c.get("organism", "")),
                "leaves": len(lv),
                "subfamilies": [f"{k} ({v})" for k, v in sfs.most_common(4)],
                "top_definitions": [f"{k} ({v})" for k, v in defs.most_common(4)],
                "contains_graft": any(g in {x["persistent_id"] for x in _all(c)} for g in case["grafts"]),
            })
        out["ibd_nodes"].append({**describe(n), "leaves": len(leaves_under(n)),
                                 "seeds": sorted(seeds), "clades": clades})
    return out


def _all(n: dict) -> list:
    out, stack = [], [n]
    while stack:
        x = stack.pop()
        out.append(x)
        stack.extend(kids(x))
    return out


def dump(obj, ind: int = 0) -> str:
    """Minimal YAML writer (no PyYAML dependency)."""
    pad = "  " * ind
    if isinstance(obj, dict):
        lines = []
        for k, v in obj.items():
            if isinstance(v, (dict, list)) and v:
                lines.append(f"{pad}{k}:\n{dump(v, ind + 1)}")
            else:
                lines.append(f"{pad}{k}: {json.dumps(v) if not isinstance(v, (dict, list)) else ('[]' if isinstance(v, list) else '{}')}")
        return "\n".join(lines)
    if isinstance(obj, list):
        lines = []
        for v in obj:
            if isinstance(v, dict):
                body = dump(v, ind + 1).lstrip()
                lines.append(f"{pad}- {body}")
            else:
                lines.append(f"{pad}- {json.dumps(v)}")
        return "\n".join(lines)
    return f"{pad}{json.dumps(obj)}"


NHX = re.compile(r"\[&&NHX:([^\]]*)\]")


def parse_tree(path: str) -> dict:
    """PANTHER ``.tree`` (Newick + NHX) -> {AN: {parent, event, taxon, leaf}}."""
    text = open(path).read().strip().rstrip(";")
    nodes: dict = {}
    stack: list = []          # open internal nodes, children collected per level
    children: list = [[]]
    i, n = 0, len(text)
    while i < n:
        c = text[i]
        if c == "(":
            children.append([])
            i += 1
        elif c in ",)":
            if c == ")":
                kids_ = children.pop()
                # internal node label follows: [:len][NHX]
                j = i + 1
                k = j
                while k < n and text[k] not in ",()":
                    k += 1
                tail = text[j:k]
                m = NHX.search(tail)
                attrs = dict(kv.split("=", 1) for kv in m.group(1).split(":") if "=" in kv) if m else {}
                an = attrs.get("ID", f"_int{len(nodes)}")
                ev = attrs.get("Ev", "")
                nodes[an] = {"parent": None, "leaf": False, "taxon": attrs.get("S", ""),
                             "event": "DUPLICATION" if ev.startswith("1>0") else
                                      "HORIZONTAL_TRANSFER" if ev.startswith("0>0") else
                                      "SPECIATION" if ev else ""}
                for kid in kids_:
                    nodes[kid]["parent"] = an
                children[-1].append(an)
                i = k
            else:
                i += 1
        else:
            k = i
            while k < n and text[k] not in ",()":
                k += 1
            name = text[i:k].split(":")[0].split("[")[0]
            if name:
                nodes[name] = {"parent": None, "leaf": True, "taxon": "", "event": ""}
                children[-1].append(name)
            i = k
    return nodes


def trace_all(panther_dir: str, ibd_gaf: str, paint_total: str) -> None:
    """Offline trace of every reviewed row against PANTHER 19 trees + current IBDs."""
    import csv
    import gzip
    import sys
    sys.path.insert(0, HERE)
    from propagation_rules import ROOT, uniprot_info, goa_terms

    rows = list(csv.DictReader(open(os.path.join(HERE, "treegrafter_review.tsv")), delimiter="\t"))
    for r in rows:
        gdir = os.path.dirname(os.path.join(ROOT, r["file"]))
        _, nodes, _ = goa_terms(gdir)
        r["graft"] = nodes.get(r["term_id"], "")
        r["family"] = uniprot_info(gdir)["fam"]
        up = os.path.join(gdir, os.path.basename(gdir) + "-uniprot.txt")
        m = re.search(r"^OX   NCBI_TaxID=(\d+)", open(up).read(), re.M) if os.path.exists(up) else None
        r["taxid"] = m.group(1) if m else ""
    wanted = {r["graft"] for r in rows if r["graft"]}
    # PTN <-> (family, AN), and TreeGrafter's current per-node GO sets
    ptn_of, an_of, tg_terms = {}, {}, {}
    fams_needed = {r["family"] for r in rows if r["family"]}
    opener = gzip.open if paint_total.endswith(".gz") else open
    with opener(paint_total, "rt") as fh:
        for line in fh:
            c = line.rstrip("\n").split("\t")
            if len(c) < 2:
                continue
            fam_an = c[0]
            fam = fam_an.split(":")[0]
            ptn = c[-1].strip()
            if fam not in fams_needed and ptn not in wanted:
                continue
            ptn_of[fam_an] = ptn
            an_of[ptn] = fam_an
            if ptn in wanted:
                tg_terms[ptn] = set(re.findall(r"GO:\d{7}", c[1] if len(c) > 2 else ""))
    # current IBDs
    ibd = {}
    with open(ibd_gaf) as fh:
        for line in fh:
            if line.startswith("!"):
                continue
            c = line.rstrip("\n").split("\t")
            rec = {"not": "NOT" in c[3], "seeds": c[7]}
            prev = ibd.setdefault(c[1], {}).get(c[4])
            # a NOT IBD on the same node and term wins over a positive one,
            # whatever their order in the file
            if prev is None or (rec["not"] and not prev["not"]):
                ibd[c[1]][c[4]] = rec
    trees: dict = {}
    out_rows = []
    for r in rows:
        rec = {**r, "status": "", "graft_an": "", "ibd": "", "ibd_an": "", "steps_from_ibd": "",
               "ibd_event": "", "ibd_taxon": "", "ibd_is_root": "", "duplication_on_path": "",
               "ibd_leaves": "", "n_seeds": "", "seeds": "", "term_in_current_tg_set": "",
               "ibd_clade": "", "query_in_ibd_clade": ""}
        g = r["graft"]
        if not g:
            out_rows.append({**rec, "status": "no_graft_node"}); continue
        fam_an = an_of.get(g)
        if not fam_an:
            out_rows.append({**rec, "status": "graft_not_in_panther19"}); continue
        fam, an = fam_an.split(":")
        rec["graft_an"] = an
        rec["term_in_current_tg_set"] = r["term_id"] in tg_terms.get(g, set())
        if fam not in trees:
            tp = os.path.join(panther_dir, f"{fam}.tree")
            trees[fam] = parse_tree(tp) if os.path.exists(tp) else None
        t = trees[fam]
        if not t or an not in t:
            out_rows.append({**rec, "status": "tree_missing"}); continue
        path = [an]
        while t[path[-1]]["parent"]:
            path.append(t[path[-1]]["parent"])
        hit, blocked = None, False
        for a in path:
            e = ibd.get(ptn_of.get(f"{fam}:{a}", ""), {}).get(r["term_id"])
            if e:
                if e["not"]:
                    blocked = True
                    break
                hit = a
                break
        if blocked:
            out_rows.append({**rec, "status": "not_ibd_on_path"}); continue
        if not hit:
            out_rows.append({**rec, "status": "no_same_term_ibd_on_path"}); continue
        steps = path[:path.index(hit) + 1]
        leaves = sum(1 for x, v in t.items() if v["leaf"] and _under(t, x, hit))
        seeds = ibd[ptn_of[f"{fam}:{hit}"]][r["term_id"]]["seeds"]
        clade, x = "", hit
        while x and not clade:          # a duplication node takes its nearest speciation ancestor's clade
            clade, x = t[x]["taxon"], t[x]["parent"]
        inside = in_clade(clade, lineage(r["taxid"])) if r["taxid"] and clade else None
        rec["ibd_clade"] = clade
        rec["query_in_ibd_clade"] = "" if inside is None else inside
        out_rows.append({**rec, "status": "ok", "ibd": ptn_of[f"{fam}:{hit}"], "ibd_an": hit,
                         "steps_from_ibd": len(steps) - 1,
                         "ibd_event": t[hit]["event"], "ibd_taxon": t[hit]["taxon"],
                         "ibd_is_root": t[hit]["parent"] is None,
                         "duplication_on_path": any(t[x]["event"] == "DUPLICATION" for x in steps[1:]),
                         "ibd_leaves": leaves, "n_seeds": len([x for x in seeds.split("|") if x]),
                         "seeds": seeds})
    cols = ["gene", "term_id", "term_label", "aspect", "action", "file", "family", "graft",
            "graft_an", "status", "term_in_current_tg_set", "ibd", "ibd_an", "steps_from_ibd",
            "ibd_event", "ibd_taxon", "ibd_clade", "query_in_ibd_clade", "ibd_is_root",
            "duplication_on_path", "ibd_leaves", "n_seeds", "seeds"]
    out = os.path.join(HERE, "graft_paths_all.tsv")
    with open(out, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, delimiter="\t", lineterminator="\n",
                           extrasaction="ignore")
        w.writeheader()
        w.writerows(sorted(out_rows, key=lambda r: (r["file"], r["term_id"])))
    print(f"wrote {out}")
    print(Counter(r["status"] for r in out_rows))
    score_path_rules(out_rows)


def score_path_rules(rows: list) -> None:
    """Score tree-structure rules against reviewer actions -> graft_path_rules.tsv."""
    import csv
    dg_set = {"REMOVE", "MODIFY", "MARK_AS_OVER_ANNOTATED", "TOO_GENERAL"}  # TOO_GENERAL counts as down-graded
    rated = [r for r in rows if r["action"] != "UNDECIDED"]
    ok = [r for r in rated if r["status"] == "ok"]
    base = sum(r["action"] in dg_set for r in rated) / len(rated)
    rules = [
        ("query outside the IBD node's clade", [r for r in ok if r["query_in_ibd_clade"] is False]),
        ("query inside the IBD node's clade", [r for r in ok if r["query_in_ibd_clade"] is True]),
        ("IBD on the graft node itself (0 steps)", [r for r in ok if r["steps_from_ibd"] == 0]),
        ("no same-term IBD on the path (term no longer in TreeGrafter's set)",
         [r for r in rated if r["status"] == "no_same_term_ibd_on_path"]),
        ("NOT IBD on the path", [r for r in rated if r["status"] == "not_ibd_on_path"]),
        ("MF term, duplication between IBD and graft",
         [r for r in ok if r["aspect"] == "molecular_function" and r["duplication_on_path"]]),
        ("MF term, no duplication between IBD and graft",
         [r for r in ok if r["aspect"] == "molecular_function" and not r["duplication_on_path"]]),
        ("IBD on the family root", [r for r in ok if r["ibd_is_root"]]),
        ("IBD below the family root", [r for r in ok if not r["ibd_is_root"]]),
        ("IBD node is a duplication", [r for r in ok if r["ibd_event"] == "DUPLICATION"]),
    ]
    out = os.path.join(HERE, "graft_path_rules.tsv")
    with open(out, "w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(["rule", "flagged", "downgraded", "downgrade_rate", "base_rate", "lift",
                    "removed", "accepted"])
        w.writerow(["(all rated TreeGrafter rows)", len(rated),
                    sum(r["action"] in dg_set for r in rated), f"{base:.3f}", f"{base:.3f}",
                    "1.00", sum(r["action"] == "REMOVE" for r in rated),
                    sum(r["action"] == "ACCEPT" for r in rated)])
        for name, sub in rules:
            if not sub:
                continue
            d = sum(r["action"] in dg_set for r in sub)
            w.writerow([name, len(sub), d, f"{d / len(sub):.3f}", f"{base:.3f}",
                        f"{d / len(sub) / base:.2f}", sum(r["action"] == "REMOVE" for r in sub),
                        sum(r["action"] == "ACCEPT" for r in sub)])
    print(open(out).read())


# PANTHER clade names that differ from NCBI's; a hyphenated name is a union.
PANTHER_TAXA = {
    "Eubacteria": ["Bacteria"], "Proteobacteria": ["Pseudomonadota"],
    "Opisthokonts": ["Opisthokonta"], "Unikonts": ["Opisthokonta", "Amoebozoa"],
    "Choanoflagellida": ["Choanoflagellata"], "Terrabacteria": ["Terrabacteria group"],
    "SAR/HA_supergroup": ["Sar", "Haptista"],
}
_LINEAGE: dict = {}


def lineage(taxid: str) -> list[str]:
    """Full NCBI lineage names for a taxon (UniProt taxonomy API, cached)."""
    if taxid not in _LINEAGE:
        try:
            d = json.loads(_get(f"https://rest.uniprot.org/taxonomy/{taxid}?format=json"))
            _LINEAGE[taxid] = [x["scientificName"] for x in d.get("lineage", [])] + [d.get("scientificName", "")]
        except Exception:
            _LINEAGE[taxid] = []
    return _LINEAGE[taxid]


_NCBI_NAME: dict = {}


def is_ncbi_name(name: str):
    """True/False if UniProt taxonomy knows a taxon by this exact scientific
    name; None if the lookup fails (cached)."""
    if name not in _NCBI_NAME:
        try:
            q = urllib.parse.urlencode({"query": f'scientific:"{name}"', "fields": "scientific_name",
                                        "format": "tsv", "size": 50})
            got = _get(f"https://rest.uniprot.org/taxonomy/search?{q}").splitlines()[1:]
            _NCBI_NAME[name] = name in [g.strip() for g in got]
        except Exception as e:
            print(f"warning: taxonomy lookup failed for clade name {name!r} ({e}); "
                  "rows under it count as undecidable", file=sys.stderr)
            _NCBI_NAME[name] = None
    return _NCBI_NAME[name]


def in_clade(panther_taxon: str, names: list[str]):
    """True/False when decidable, None when it is not.

    Undecidable means the lineage is unknown, or part of the PANTHER clade name
    is neither mapped in PANTHER_TAXA nor a known NCBI taxon name (so its
    absence from the lineage says nothing).
    """
    if panther_taxon == "LUCA":
        return True
    if not names:
        return None
    wanted, undecidable = [], False
    for part in panther_taxon.split("-"):
        if part in PANTHER_TAXA:
            wanted += PANTHER_TAXA[part]
        elif part in names:
            return True
        elif is_ncbi_name(part):
            wanted.append(part)
        else:
            undecidable = True
    if any(w in names for w in wanted):
        return True
    return None if undecidable else False


def _under(t: dict, x: str, anc: str) -> bool:
    while x:
        if x == anc:
            return True
        x = t[x]["parent"]
    return False


def main() -> None:
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--panther-trees", help="PANTHER19.0_data/Tree_MSF directory")
    ap.add_argument("--ibd-gaf", help="PAINT IBD.gaf")
    ap.add_argument("--paint-total", help="PAINT_TreeGrafter_Annotations_TOTAL.txt[.gz]")
    args = ap.parse_args()
    if args.all:
        missing = [f"--{n.replace('_', '-')}" for n in ("panther_trees", "ibd_gaf", "paint_total")
                   if not getattr(args, n)]
        if missing:
            ap.error("--all needs " + ", ".join(missing))
        trace_all(args.panther_trees, args.ibd_gaf, args.paint_total)
        return
    results = []
    for case in CASES:
        r = trace(case)
        results.append(r)
        for g in r["grafts"]:
            print(case["case"], g["graft"], "IBD", g.get("ibd"), "steps", g.get("steps_from_ibd"))
    with open(OUT, "w") as fh:
        fh.write("# Generated by trace_graft_paths.py from the live PANTHER tree API and QuickGO.\n")
        fh.write(dump({"cases": results}) + "\n")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
