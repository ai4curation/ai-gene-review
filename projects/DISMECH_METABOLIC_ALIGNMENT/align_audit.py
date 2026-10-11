"""Audit dismech metabolic entries against ai-gene-review core functions and modules.

For each in-scope disorder and each gene bound in its genetic records, compare the GO
terms on pathograph nodes naming that gene with the gene's AIGR core-function terms
(exact, or related through is_a/part_of ancestry), and list AIGR modules containing the
gene's UniProt accession. Emits a YAML report.

Usage, from the ai-gene-review root with a dismech checkout beside it:

    DISMECH_DIR=../dismech uv run python projects/DISMECH_METABOLIC_ALIGNMENT/align_audit.py \
        projects/DISMECH_METABOLIC_ALIGNMENT/scope.json report.yaml
    python3 projects/DISMECH_METABOLIC_ALIGNMENT/make_page.py report.yaml \
        projects/DISMECH_METABOLIC_ALIGNMENT.md
"""
import glob
import json
import os
import re
import sys

import yaml
from oaklib import get_adapter

DM = os.environ.get("DISMECH_DIR", "../dismech")
AG = os.environ.get("AIGR_DIR", ".")
SCOPE = json.load(open(sys.argv[1]))
OUT = sys.argv[2]

go = get_adapter(os.environ.get("GO_ADAPTER", "sqlite:obo:go"))
PRED = ["rdfs:subClassOf", "BFO:0000050"]
_anc = {}


def anc(t):
    if t not in _anc:
        try:
            _anc[t] = set(go.ancestors(t, predicates=PRED, reflexive=True))
        except Exception:
            _anc[t] = {t}
    return _anc[t]


def related(a, b):
    return a == b or b in anc(a) or a in anc(b)


# AIGR: symbol -> (uniprot, status, core term sets)
aigr = {}
for p in glob.glob(f"{AG}/genes/human/*/*-ai-review.yaml"):
    sym = os.path.basename(os.path.dirname(p))
    try:
        d = yaml.safe_load(open(p))
    except Exception:
        continue
    mf, bp, cc = set(), set(), set()
    for cf in d.get("core_functions") or []:
        for k, dest in (("molecular_function", mf), ("contributes_to_molecular_function", mf)):
            v = cf.get(k)
            if isinstance(v, dict) and v.get("id"):
                dest.add(v["id"])
        for k, dest in (("directly_involved_in", bp), ("locations", cc), ("in_complex", cc)):
            v = cf.get(k) or []
            if isinstance(v, dict):
                v = [v]
            for x in v:
                if isinstance(x, dict) and x.get("id"):
                    dest.add(x["id"])
    # Terms the review keeps (ACCEPT or KEEP_AS_NON_CORE, or proposed NEW) but does not
    # treat as core: used to tell "consistent with a non-core function" from "no match".
    kept = set()
    for a in d.get("existing_annotations") or []:
        act = ((a.get("review") or {}).get("action") or "")
        tid_ = (a.get("term") or {}).get("id")
        if tid_ and not a.get("negated") and act in ("ACCEPT", "KEEP_AS_NON_CORE", "NEW"):
            kept.add(tid_)
    aigr[sym] = dict(uniprot=d.get("id"), status=d.get("status"), mf=mf, bp=bp, cc=cc, kept=kept)

# modules: accession -> module names
mod_by_acc = {}
for p in glob.glob(f"{AG}/modules/*.yaml"):
    txt = open(p).read()
    for acc in set(re.findall(r"UniProtKB:([A-Z0-9]{6,10})", txt)):
        mod_by_acc.setdefault(acc, set()).add(os.path.basename(p)[:-5])

hgnc_sym = {}
for line in open(f"{DM}/cache/hgnc/terms.csv"):
    parts = line.rstrip("\n").split(",")
    if len(parts) >= 2:
        hgnc_sym[parts[0].lower()] = parts[1]


def tid(x):
    if isinstance(x, dict):
        t = x.get("term") or {}
        return t.get("id")
    return None


report = []
for name in SCOPE:
    f = f"{DM}/kb/disorders/{name}.yaml"
    if not os.path.exists(f):
        report.append(dict(entry=name, problem="FILE_MISSING"))
        continue
    d = yaml.safe_load(open(f))
    genes = []
    for r in d.get("genetic") or []:
        gid = tid(r.get("gene_term"))
        if gid and gid.lower().startswith("hgnc:"):
            genes.append((gid.lower(), r.get("relationship_type"), r.get("variant_origin")))
    entry = dict(entry=name, genes=[])
    if not genes:
        entry["problem"] = "NO_GENE_RECORD"
    for gid, rel, origin in genes:
        sym = hgnc_sym.get(gid, gid)
        sym = {"TMEM251": "LYSET"}.get(sym, sym)  # HGNC rename; AIGR folder uses current symbol
        node_mf, node_bp, node_cc, nodes = set(), set(), set(), []
        for n in d.get("pathophysiology") or []:
            ng = [(tid(g) or "").lower() for g in n.get("genes") or []]
            if isinstance(n.get("gene"), dict):
                ng.append((tid(n["gene"]) or "").lower())
            gc = n.get("genetic_context") or {}
            for k in ("gene", "gene_term"):
                if isinstance(gc.get(k), dict):
                    ng.append((tid(gc[k]) or "").lower())
            if gid not in ng:
                continue
            nodes.append(n.get("name"))
            for x in n.get("molecular_functions") or []:
                node_mf.add(tid(x))
            for x in n.get("biological_processes") or []:
                node_bp.add(tid(x))
            for k in ("cellular_components", "locations"):
                for x in n.get(k) or []:
                    node_cc.add(tid(x))
        node_mf.discard(None); node_bp.discard(None); node_cc.discard(None)
        a = aigr.get(sym)
        g = dict(gene=sym, hgnc=gid, relationship=rel, origin=origin, nodes=len(nodes))
        flags = []
        if rel is None:
            flags.append("UNTYPED")
        if origin is None:
            flags.append("NO_ORIGIN")
        if not nodes:
            flags.append("GENE_ON_NO_NODE")
        if not node_mf and not node_bp:
            flags.append("NO_GO_ON_GENE_NODES")
        if a is None:
            flags.append("NO_AIGR_REVIEW")
        else:
            g["aigr_status"] = a["status"]
            if a["status"] != "COMPLETE":
                flags.append("AIGR_NOT_COMPLETE")
            core = a["mf"] | a["bp"]
            dm = node_mf | node_bp
            if dm and core:
                aligned = sorted(t for t in dm if any(related(t, c) for c in core))
                g["aligned_terms"] = aligned
                if not aligned:
                    noncore = sorted(t for t in dm if any(related(t, k) for k in a["kept"]))
                    if noncore:
                        g["aligned_noncore_terms"] = noncore
                        flags.append("ALIGNED_NONCORE")
                    else:
                        flags.append("NO_GO_ALIGNMENT")
                g["dismech_only"] = sorted(dm - set(aligned))
            mods = sorted(mod_by_acc.get(a["uniprot"], []))
            g["modules"] = mods
            if not mods:
                flags.append("NO_MODULE")
        g["flags"] = flags
        entry["genes"].append(g)
    report.append(entry)

yaml.safe_dump(report, open(OUT, "w"), sort_keys=False, width=120)
from collections import Counter
c = Counter(fl for e in report for g in e.get("genes", []) for fl in g["flags"])
print("entries", len(report), "gene-rows", sum(len(e.get("genes", [])) for e in report))
print(dict(c))
print("entries with problem:", [ (e["entry"], e["problem"]) for e in report if e.get("problem")])
